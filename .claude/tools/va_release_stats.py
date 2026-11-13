"""Inhaltszahlen je Release (Kono 2026-11-12): zählt eigene Mod-Inhalte und vergleicht zwei Stände.

"Eigen" = Objektname (bzw. Loc-Key, Event-ID) gibt es in Vanilla nicht. So fallen Abschalt-Hüllen, Overrides und
umgezogene Vollkopien raus, auch eigene Inhalte in Dateien mit Vanilla-Namen zählen mit. Grafiken: Pfad nicht in Vanilla.
Quelle ist der Arbeitsstand oder ein Git-Stand (nur lesend: git ls-tree / git cat-file).

Aufrufe:
  python -I .claude/tools/va_release_stats.py                       Arbeitsstand anzeigen
  python -I .claude/tools/va_release_stats.py --ref main            Git-Stand anzeigen
  python -I .claude/tools/va_release_stats.py --save 2              Arbeitsstand als .claude/releases/version_2.json sichern
  python -I .claude/tools/va_release_stats.py --ref main --save 1   Git-Stand sichern
  python -I .claude/tools/va_release_stats.py --compare 1           Arbeitsstand gegen version_1.json, Markdown für das Release-Statement
"""
import argparse
import json
import logging
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

log = logging.getLogger("va_release_stats")

REPO = Path(__file__).resolve().parents[2]
VANILLA = Path(r"C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\game")
RELEASES = REPO / ".claude" / "releases"

# Anzeige-Name, Ordner, Zählart. "objects" = Objekte auf oberster Ebene, "events" = <namespace>.<n>, "states" = STATE_…
CATEGORIES = [
    ("Journal Entries", "common/journal_entries", "objects"),
    ("Events", "events", "events"),
    ("Decisions", "common/decisions", "objects"),
    ("Scripted Buttons", "common/scripted_buttons", "objects"),
    ("Progress Bars", "common/scripted_progress_bars", "objects"),
    ("Modifiers", "common/static_modifiers", "objects"),
    ("Scripted Effects", "common/scripted_effects", "objects"),
    ("Scripted Triggers", "common/scripted_triggers", "objects"),
    ("Script Values", "common/script_values", "objects"),
    ("Diplomatic Plays", "common/diplomatic_plays", "objects"),
    ("Buildings", "common/buildings", "objects"),
    ("Production Methods", "common/production_methods", "objects"),
    ("Goods", "common/goods", "objects"),
    ("Countries", "common/country_definitions", "objects"),
    ("States", "map_data/state_regions", "states"),
    ("Cultures", "common/cultures", "objects"),
    ("Religions", "common/religions", "objects"),
    ("Character Templates", "common/character_templates", "objects"),
    ("Government Types", "common/government_types", "objects"),
    ("Cultural Traits", "common/discrimination_traits", "objects"),
]
# Technische Pflicht-Objekte, kein Content (Modifier je Kultur/Religion, vom Spiel erwartet)
TECHNICAL_FILES = ("common/static_modifiers/va_culture_modifiers.txt", "common/static_modifiers/va_religion_modifiers.txt")
# Alte Vanilla-Kopien aus der Zeit vor der Pause: ihre Objekte gibt es im heutigen Vanilla nicht mehr, sie sind aber
# kein Mod-Content (Kono 2026-11-13: vor der Pause nur Worgen-JE, Wretched-JE und ein Gilneas-Event). Erde-Hüllen
# (va_earth_*) sind abgeschaltete Vanilla-Objekte und zählen ebenfalls nicht.
VANILLA_RELICS = (
    "common/journal_entries/00_communism.txt", "common/journal_entries/01_coup.txt",
    "events/agitators_events/coup_events.txt", "events/royal_wedding.txt",
    "common/decisions/canada_australia.txt", "common/decisions/ionian_islands.txt",
    "common/scripted_effects/00_ip3_victoria_scripted_effects.txt", "common/scripted_effects/00_victoria_scripted_effects.txt",
    "common/scripted_triggers/00_ai_triggers.txt", "common/scripted_triggers/00_geography_triggers.txt",
    "common/scripted_triggers/00_scripted_triggers.txt", "common/scripted_triggers/00_victoria_scripted_triggers.txt",
)


def is_counted(path):
    """Datei zählt als Mod-Content: keine technische Datei, kein Vanilla-Rest, keine Erde-Hülle."""
    if path in TECHNICAL_FILES or path in VANILLA_RELICS:
        return False
    return "va_earth" not in path.lower()
LOC_DIR = "localization/replace/english"
GFX_DIR = "gfx"
GFX_EXT = (".dds", ".png", ".tga")

RE_OBJECT = re.compile(r"^([A-Za-z_][\w.:\-]*)\s*=\s*\{", re.M)
RE_EVENT = re.compile(r"^([A-Za-z_]\w*\.\d+)\s*=\s*\{", re.M)
RE_STATE = re.compile(r"^(STATE_\w+)\s*=\s*\{", re.M)
RE_LOC = re.compile(r'^\s+([\w.\-]+):\d*\s+"(.*)"\s*$', re.M)
RE_COMMENT = re.compile(r"#[^\n\"]*$", re.M)


class Source:
    """Arbeitsstand (ref None) oder Git-Stand, nur lesend."""

    def __init__(self, ref=None):
        self.ref = ref
        if ref:
            out = self._git("ls-tree", "-r", "--name-only", ref)
            self.files = out.decode("utf-8").splitlines()
        else:
            self.files = [p.relative_to(REPO).as_posix() for p in REPO.rglob("*")
                          if p.is_file() and ".git" not in p.parts and ".claude" not in p.parts]

    def _git(self, *args):
        try:
            return subprocess.run(["git", "-C", str(REPO), *args], check=True, capture_output=True).stdout
        except subprocess.CalledProcessError as exc:
            log.error("git %s fehlgeschlagen: %s", " ".join(args), exc.stderr.decode("utf-8", "replace").strip())
            raise

    def read(self, path):
        try:
            raw = self._git("show", f"{self.ref}:{path}") if self.ref else (REPO / path).read_bytes()
        except (OSError, subprocess.CalledProcessError) as exc:
            log.warning("Datei nicht lesbar, übersprungen: %s (%s)", path, exc)
            return ""
        return raw.decode("utf-8-sig", "replace")

    def own(self, folder, suffixes):
        """Eigene Dateien im Ordner: nicht unter gleichem Pfad in Vanilla."""
        prefix = folder.rstrip("/") + "/"
        return [f for f in self.files
                if f.startswith(prefix) and f.lower().endswith(suffixes) and not (VANILLA / f).exists()]


def names_in(text, mode):
    text = RE_COMMENT.sub("", text)
    if mode == "events":
        return set(RE_EVENT.findall(text))
    if mode == "states":
        return set(RE_STATE.findall(text))
    return {n for n in RE_OBJECT.findall(text) if n != "namespace" and not n.startswith("@")}


_VANILLA_CACHE = {}


def vanilla_names(folder, mode):
    """Alle Objektnamen der Kategorie im Vanilla-Spiel (einmal je Lauf gelesen)."""
    key = (folder, mode)
    if key not in _VANILLA_CACHE:
        names = set()
        for path in (VANILLA / folder).rglob("*.txt"):
            try:
                names |= names_in(path.read_text(encoding="utf-8-sig", errors="replace"), mode)
            except OSError as exc:
                log.warning("Vanilla-Datei nicht lesbar: %s (%s)", path, exc)
        _VANILLA_CACHE[key] = names
    return _VANILLA_CACHE[key]


def count_category(src, folder, mode):
    names = set()
    prefix = folder + "/"
    for path in src.files:
        if path.startswith(prefix) and path.lower().endswith(".txt") and is_counted(path):
            names |= names_in(src.read(path), mode)
    return len(names - vanilla_names(folder, mode))


def vanilla_loc_keys():
    if "loc" not in _VANILLA_CACHE:
        keys = set()
        for path in (VANILLA / "localization" / "english").rglob("*.yml"):
            try:
                keys.update(k for k, _v in RE_LOC.findall(path.read_text(encoding="utf-8-sig", errors="replace")))
            except OSError as exc:
                log.warning("Vanilla-Loc nicht lesbar: %s (%s)", path, exc)
        _VANILLA_CACHE["loc"] = keys
    return _VANILLA_CACHE["loc"]


def count_loc(src):
    entries, words, ai = 0, 0, 0
    vanilla = vanilla_loc_keys()
    seen = set()
    for path in [f for f in src.files if f.startswith("localization/") and "english" in f and f.endswith(".yml")]:
        for key, value in RE_LOC.findall(src.read(path)):
            if key in vanilla or key in seen:
                continue
            seen.add(key)
            entries += 1
            if "(AI WRITTEN)" in value:
                ai += 1
            plain = re.sub(r"\[[^\]]*\]|\$[^$]*\$|#\w+|#!|\\n|\(AI WRITTEN\)", " ", value)
            words += len(re.findall(r"[A-Za-z']+", plain))
    return entries, words, ai


def collect(src):
    stats = {name: count_category(src, folder, mode) for name, folder, mode in CATEGORIES}
    entries, words, ai = count_loc(src)
    stats["Text Entries"] = entries
    stats["Words of Text"] = words
    stats["Texts marked AI WRITTEN"] = ai
    stats["Graphics"] = len(src.own(GFX_DIR, GFX_EXT))
    return stats


def show(stats, title):
    print(f"## {title}\n")
    print("| What | Count |\n|---|---:|")
    for key, value in stats.items():
        print(f"| {key} | {value:,} |")


def compare(old, new, old_name):
    print(f"## New since version {old_name}\n")
    print("| What | Added | Total now |\n|---|---:|---:|")
    for key, value in new.items():
        diff = value - old.get(key, 0)
        # nur Zuwachs: alte Stände enthielten Vanilla-Vollkopien mit inzwischen umbenannten Objekten (Minus wäre Messfehler)
        if diff > 0 and key != "Texts marked AI WRITTEN":
            print(f"| {key} | {diff:+,} | {value:,} |")
    print(f"\nTexts still marked AI WRITTEN: {new.get('Texts marked AI WRITTEN', 0):,} "
          f"(version {old_name}: {old.get('Texts marked AI WRITTEN', 0):,})")


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s", stream=sys.stderr)
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ref", help="Git-Stand statt Arbeitsstand (z. B. main)")
    ap.add_argument("--save", metavar="VERSION", help="als .claude/releases/version_<VERSION>.json sichern")
    ap.add_argument("--compare", metavar="VERSION", help="gegen gesicherte version_<VERSION>.json vergleichen")
    args = ap.parse_args()

    if not VANILLA.exists():
        log.error("Vanilla-Ordner fehlt: %s", VANILLA)
        return 1
    src = Source(args.ref)
    log.info("Quelle: %s, %d Dateien", args.ref or "Arbeitsstand", len(src.files))
    stats = collect(src)

    if args.save:
        RELEASES.mkdir(exist_ok=True)
        target = RELEASES / f"version_{args.save}.json"
        payload = {"version": args.save, "source": args.ref or "Arbeitsstand", "date": date.today().isoformat(), "stats": stats}
        target.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        log.info("gesichert: %s", target.relative_to(REPO))

    if args.compare:
        ref_file = RELEASES / f"version_{args.compare}.json"
        if not ref_file.exists():
            log.error("Vergleichsstand fehlt: %s (vorher mit --save anlegen)", ref_file.relative_to(REPO))
            return 1
        compare(json.loads(ref_file.read_text(encoding="utf-8"))["stats"], stats, args.compare)
    else:
        show(stats, f"Victorian Azeroth – {args.ref or 'current state'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

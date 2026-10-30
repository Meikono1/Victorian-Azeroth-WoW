"""Statische Prüfung des Mods vor jeder Testrunde.

Aufruf: python -I .claude/tools/va_lint.py [--regions 26 27] [--full] [--all-files] [--update-baseline]
  --regions    zusätzlich va_check_states.py für diese State-Region-Präfixe
  --full       alle Befunde ausgeben statt der ersten 15 je Gruppe
  --all-files  auch Mod-Dateien prüfen, die gleichnamige Vanilla-Dateien überschreiben (alte Kopien)

Geprüft wird nur, was der Mod selbst besitzt (Dateien ohne gleichnamiges Vanilla-Gegenstück),
außer bei --all-files. Exit-Code 1 nur bei neuen Fehlern: Warnungen und Fehler aus
va_lint_baseline.txt (bekannte Altlasten, Abbau in VA-023) zählen nicht. --update-baseline
nur nach Absprache mit Kono, sonst versteckt man neue Fehler.
"""
import argparse
import logging
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

sys.dont_write_bytecode = True  # kein __pycache__ im Repo
sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I nimmt das Skriptverzeichnis aus sys.path
from va_script import REPO, VANILLA, effective_files, parse_file, replace_paths

log = logging.getLogger("va_lint")

# Ordner, deren Objekte einen gleichnamigen Loc-Key brauchen (Zusatz-Keys je Ordner)
LOC_FOLDERS = {
    "common/goods": [""],
    "common/buildings": [""],
    "common/building_groups": [""],
    "common/production_methods": [""],
    "common/production_method_groups": [""],
    "common/country_definitions": ["", "_ADJ"],
    "common/cultures": [""],
    "common/religions": [""],
    "common/journal_entries": ["", "_reason"],
    "common/modifier_type_definitions": [""],
}
# Ordner ohne sinnvolle Doppel-Prüfung (Wurzelblöcke wie STATES/POPS, Listen statt Objekte)
NO_DUP = ("common/history", "common/defines", "common/on_actions", "common/coat_of_arms")
REF = re.compile(r"\b(cu|c|s|rel):([A-Za-z_][A-Za-z0-9_]*)(\s*\?=)?")
LOC_LINE = re.compile(r"^\s+([A-Za-z0-9_.\-']+):\d*\s*\"")
EVENT_KEYS = re.compile(r"^\s*(?:title|desc|flavor|name)\s*=\s*\"?([A-Za-z0-9_.]+\.[A-Za-z0-9_]+)\"?\s*$", re.M)
TOP_KEY = re.compile(r"^([A-Za-z_][A-Za-z0-9_:\-]*)\s*=\s*\{", re.M)


# Vanilla legt diese Modifier-Typen je Kultur/Religion an und hat selbst keine Loc dafür
GENERATED_MODIFIER = re.compile(r"^(country_\w+_cultural_acceptance_add|state_\w+_standard_of_living_add|country_fervor_target_\w+_add)$")
BASELINE = Path(__file__).with_name("va_lint_baseline.txt")


class Findings:
    """Befunde je Gruppe. Warnungen und Befunde aus der Baseline lassen den Lauf nicht scheitern."""

    def __init__(self, baseline):
        self.groups = defaultdict(list)
        self.warn = set()
        self.baseline = baseline

    def add(self, group, text, warn=False):
        self.groups[group].append(text)
        if warn:
            self.warn.add(group)

    def lines(self):
        return [f"{g} | {t}" for g, items in self.groups.items() for t in items]

    def new_errors(self):
        return [l for l in self.lines() if l.split(" | ", 1)[0] not in self.warn and l not in self.baseline]

    def print(self, full):
        new = set(self.new_errors())
        for group, items in sorted(self.groups.items()):
            kind = "Warnung" if group in self.warn else "Fehler"
            fresh = [t for t in items if f"{group} | {t}" in new]
            known = len(items) - len(fresh)
            print(f"\n## [{kind}] {group} ({len(items)}, davon neu {len(fresh)}, bekannt {known})")
            shown = fresh + [t for t in items if t not in fresh]
            for t in shown if full else shown[:15]:
                print(f"- {'NEU ' if t in fresh else ''}{t}")
            if not full and len(items) > 15:
                print(f"- … {len(items) - 15} weitere (--full)")


def load_baseline():
    try:
        return set(BASELINE.read_text(encoding="utf-8-sig").splitlines())
    except FileNotFoundError:
        log.warning("Keine Baseline (%s), alle Fehler gelten als neu", BASELINE.name)
        return set()


def read(path):
    try:
        return path.read_bytes()
    except OSError as e:
        log.error("Kann %s nicht lesen: %s", path, e)
        return b""


def mod_owned(path, all_files):
    """Gehört die Datei dem Mod (kein gleichnamiges Vanilla-Gegenstück)?"""
    rel = path.relative_to(REPO)
    return all_files or not (VANILLA / rel).exists()


def mod_script_files(all_files):
    for top in ("common", "events"):
        for f in sorted((REPO / top).rglob("*.txt")):
            if mod_owned(f, all_files):
                yield f


def load_loc():
    keys = set()
    for base in (VANILLA / "localization/english", REPO / "localization"):
        for f in base.rglob("*_l_english.yml"):
            for line in read(f).decode("utf-8-sig", errors="replace").splitlines():
                m = LOC_LINE.match(line)
                if m:
                    keys.add(m.group(1))
    log.info("%d Loc-Keys geladen", len(keys))
    return keys


def check_encoding(fd, all_files):
    for f in list(mod_script_files(all_files)) + sorted((REPO / "map_data/state_regions").glob("*.txt")):
        if not read(f).startswith(b"\xef\xbb\xbf"):
            fd.add("Kodierung Script", f"{f.relative_to(REPO)}: kein UTF-8-BOM", warn=True)
    for f in sorted((REPO / "localization").rglob("*.yml")):
        raw = read(f)
        rel = f.relative_to(REPO)
        if not raw.startswith(b"\xef\xbb\xbf"):
            fd.add("Kodierung", f"{rel}: kein UTF-8-BOM")
        lang = re.search(r"_l_(\w+)\.yml$", f.name)
        first = raw.decode("utf-8-sig", errors="replace").lstrip().split("\n", 1)[0].strip()
        if not lang or first != f"l_{lang.group(1)}:":
            fd.add("Kodierung", f"{rel}: erste Zeile '{first[:30]}' statt l_<sprache>:")
        for n, line in enumerate(raw.decode("utf-8-sig", errors="replace").splitlines()[1:], 2):
            if line.strip() and not line.lstrip().startswith("#") and not line.startswith("  ") and not line.startswith(" "):
                fd.add("Kodierung", f"{rel}:{n}: Eintrag nicht eingerückt")
                break


def defined_names(folder):
    """Objektnamen je Ordner über die wirksamen Dateien, mit Herkunft."""
    out = defaultdict(list)
    for f in effective_files(folder):
        text = read(f).decode("utf-8-sig", errors="replace")
        for m in TOP_KEY.finditer(text):
            out[m.group(1)].append(f)
    return out


def check_duplicates(fd):
    folders = sorted({str(p.parent.relative_to(REPO)).replace("\\", "/")
                      for p in (REPO / "common").rglob("*.txt")})
    for folder in folders:
        if folder.startswith(NO_DUP):
            continue
        for name, files in defined_names(folder).items():
            if ":" in name or len(files) < 2:
                continue  # INJECT:/REPLACE:/TRY_INJECT: sind gewollt
            where = ", ".join(sorted({("vanilla:" if VANILLA in f.parents else "") + f.name for f in files}))
            fd.add("Doppelt definiert", f"{folder}: {name} in {where}")


def check_loc(fd, loc, all_files):
    for folder, suffixes in LOC_FOLDERS.items():
        for f in (REPO / folder).glob("*.txt"):
            if not mod_owned(f, all_files):
                continue
            for k, _, v in parse_file(f):
                if not k or ":" in k or not isinstance(v, list) or GENERATED_MODIFIER.match(k):
                    continue
                for suf in suffixes:
                    if k + suf not in loc:
                        fd.add(f"Loc fehlt: {folder}", f"{k + suf} ({f.name})")
    for f in sorted((REPO / "events").rglob("*.txt")):
        if not mod_owned(f, all_files):
            continue
        for key in EVENT_KEYS.findall(read(f).decode("utf-8-sig", errors="replace")):
            if key not in loc:
                fd.add("Loc fehlt: events", f"{key} ({f.relative_to(REPO)})")
    states = set()
    for f in (REPO / "map_data/state_regions").glob("*.txt"):
        for k, _, v in parse_file(f):
            if k and isinstance(v, list):
                states.add(k)
    for s in sorted(states):
        if s not in loc:
            fd.add("Loc fehlt: state_regions", s)
    return states


def check_refs(fd, states, all_files):
    known = {
        "cu": set(defined_names("common/cultures")),
        "c": set(defined_names("common/country_definitions")),
        "rel": set(defined_names("common/religions")),
        "s": states,
    }
    for f in mod_script_files(all_files):
        text = read(f).decode("utf-8-sig", errors="replace")
        for n, line in enumerate(text.splitlines(), 1):
            code = line.split("#", 1)[0]
            for kind, name, optional in REF.findall(code):
                if optional or name in known[kind] or name.isupper() and kind == "c" and name in ("THIS", "ROOT", "PREV"):
                    continue
                fd.add(f"Unbekannter Verweis {kind}:", f"{f.relative_to(REPO)}:{n}: {kind}:{name}")


def run_regions(regions):
    ok = True
    for r in regions:
        out = subprocess.run([sys.executable, "-I", str(Path(__file__).with_name("va_check_states.py")), r],
                             capture_output=True, text=True, encoding="utf-8")
        if out.returncode != 0:
            log.error("va_check_states.py %s fehlgeschlagen: %s", r, out.stderr[-500:])
            ok = False
            continue
        print(f"\n# State-Prüfung Region {r}")
        print(out.stdout.strip())
    return ok


def main():
    sys.stdout.reconfigure(encoding="utf-8")  # -I ignoriert PYTHONIOENCODING
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    ap = argparse.ArgumentParser()
    ap.add_argument("--regions", nargs="*", default=[])
    ap.add_argument("--full", action="store_true")
    ap.add_argument("--all-files", action="store_true")
    ap.add_argument("--update-baseline", action="store_true", help="aktuelle Fehler als bekannt speichern")
    a = ap.parse_args()
    if not replace_paths():
        log.warning("replace_paths leer oder unlesbar, Auflösung der wirksamen Dateien ungenau")

    fd = Findings(set() if a.update_baseline else load_baseline())
    check_encoding(fd, a.all_files)
    check_duplicates(fd)
    loc = load_loc()
    states = check_loc(fd, loc, a.all_files)
    check_refs(fd, states, a.all_files)
    if a.update_baseline:
        errors = sorted(l for l in fd.lines() if l.split(" | ", 1)[0] not in fd.warn)
        BASELINE.write_text("\n".join(errors) + "\n", encoding="utf-8-sig")
        log.info("Baseline mit %d bekannten Fehlern geschrieben", len(errors))
        return
    fd.print(a.full)
    regions_ok = run_regions(a.regions)
    new = fd.new_errors()
    print(f"\n{len(fd.lines())} Befunde, davon {len(new)} neue Fehler")
    sys.exit(1 if new or not regions_ok else 0)


if __name__ == "__main__":
    main()

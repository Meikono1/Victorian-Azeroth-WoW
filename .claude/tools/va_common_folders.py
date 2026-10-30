"""common-Ordner klassifizieren: Erde-Inhalt, allgemeine Mechanik oder WoW-Inhalt (VA-002 Teil 2).

Aufruf: python -I .claude/tools/va_common_folders.py <ordner> [--details] [--stubs] [--apply-copies]
  <ordner>        z. B. common/journal_entries, common/scripted_buttons
  --details       je Datei die gefundenen Erde-Verweise und aufgerufene, nicht geladene Events ausgeben
  --stubs         für Vanilla-Dateien mit Erde-Inhalt ohne Mod-Gegenstück eine leere Datei anlegen
  --apply-copies  alte Mod-Kopien bereinigen: "kopie-allgemein" und "stub-allgemein" löschen, "kopie-erde" leeren.
                  Löscht Repo-Dateien (Kono hat Claude das Ausführen eigener Skripte erlaubt, 2026-10-30).

Gleiche Regeln wie va_events.py: s:/sr: auf States/Regionen, die der Mod nicht hat, machen eine Datei zu Erde.
Verweise auf Erde-Länder/-Kulturen/-Religionen (c:/cu:/rel:) machen sie zu Erde, außer sie steht in GENERIC.
Dateien ohne solche Verweise, die thematisch trotzdem Erde sind, stehen in EARTH.
Ausgewertet wird der Stand ohne den Ordner in replace_paths.
"""
import argparse
import logging
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # kein __pycache__ im Repo
sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I nimmt das Skriptverzeichnis aus sys.path
from va_script import REPO, VANILLA, replace_paths
from va_events import CRLF, earth_refs, event_files, known_objects, read, strip_comments, wow_refs

log = logging.getLogger("va_common_folders")

EVENT_ID = re.compile(r"\bid\s*=\s*([A-Za-z_][A-Za-z0-9_]*\.\d+)")
EVENT_DEF = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*\.\d+)\s*=\s*\{", re.M)  # Vanilla rückt teils ein
# Allgemeine Mechaniken, die Erde-Länder/-Kulturen/-Religionen nur nebenbei nennen (Namensverzweigung, Ausschluss).
# Von Hand ausgewählt, Liste bei Patches ergänzen. s:/sr:-Verweise machen eine Datei trotzdem zu Erde.
GENERIC = {
	"common/journal_entries/00_slave_owner_paranoia.txt",  # nur NOT = { c:BRZ ?= this }
}
# Ohne direkte Erde-Verweise, aber Erde-Thema (Expeditionen, Japan, Frankreich, Lateinamerika, Afrika).
# Von Hand ausgewählt 2026-10-30; gestartet nur über abgeschaltete Events/History oder per Erde-Region.
EARTH = {
	"common/journal_entries/00_antarctica.txt",
	"common/journal_entries/00_central_africa.txt",
	"common/journal_entries/00_congo.txt",
	"common/journal_entries/00_krakatoa.txt",
	"common/journal_entries/00_land_reclamation.txt",
	"common/journal_entries/00_manifest_destiny.txt",
	"common/journal_entries/00_niger_river.txt",
	"common/journal_entries/00_scramble_for_africa.txt",  # geographic_region_africa
	"common/journal_entries/00_west_america.txt",
	"common/journal_entries/01_dreyfus_affair.txt",
	"common/journal_entries/02_caudillo.txt",
	"common/journal_entries/07_iwakura_mission.txt",
	"common/journal_entries/07_sakoku.txt",
	"common/journal_entries/07_tenpo_crisis.txt",
	# Buttons, die nur von abgeschalteten Erde-JEs benutzt werden
	"common/scripted_buttons/00_christ_of_europe_buttons.txt",
	"common/scripted_buttons/04_indian_famines_buttons.txt",
	"common/scripted_buttons/05_serbia_buttons.txt",
	"common/scripted_buttons/06_canada_australia_buttons.txt",
	"common/scripted_buttons/06_spa_economic_regeneration_buttons.txt",
	"common/scripted_buttons/07_iwakura_buttons.txt",
	"common/scripted_buttons/07_meiji_buttons.txt",
	"common/scripted_buttons/caudillo_buttons.txt",
	"common/scripted_buttons/china_buttons.txt",
	"common/scripted_buttons/meiji_reform_buttons.txt",
	"common/scripted_buttons/sakoku_buttons.txt",
	# VA-002 Teil 3: nur Erde-Kulturen/-Religionen, keine States
	"common/character_templates/country_kaf.txt",
	"common/character_templates/french_dynastic_template.txt",
}
# Bewusste Vanilla-Overrides (siehe ABLAUFPLAN): gleichnamige Mod-Datei mit WoW-Anteil ohne c:/cu:/rel:-Verweis.
# Ohne diese Liste stünden sie unter "kopie-allgemein" und --apply-copies würde sie löschen.
OVERRIDE = {
	"common/character_templates/00_default_template.txt",
	# vorübergehend: alte Kopie passt zu den alten Gebäudenamen in common/buildings/0*.txt. Mit VA-003 (buildings) löschen.
	"common/company_types/99_basic_companies.txt",
}
STUB = "\ufeff# Abgeschaltet (VA-002): Vanilla-Datei mit Erde-Inhalt. Erzeugt von .claude/tools/va_common_folders.py.\n"


def loaded_events():
    """IDs aller Events, die das Spiel lädt (wirksame Eventdateien)."""
    ids = set()
    for _, (van, own) in event_files().items():
        ids |= set(EVENT_DEF.findall(strip_comments(read(own if own is not None else van))))
    return ids


def folder_files(folder):
    """Relativer Pfad → (Vanilla-Datei oder None, Mod-Datei oder None)."""
    files = {}
    for root, slot in ((VANILLA, 0), (REPO, 1)):
        for f in (root / folder).glob("*.txt"):
            files.setdefault(f"{folder}/{f.name}", [None, None])[slot] = f
    return files


def vanilla_is_earth(rel, van, earth, mod):
    """(Erde?, Verweise) für die Vanilla-Datei. JE-Querverweise zählen nicht, sie folgen aus dieser Einteilung."""
    hard, soft = earth_refs(strip_comments(read(van)), earth, mod)
    hard = {r for r in hard if not r.startswith("je_")}
    geo = {r for r in hard if r.startswith(("s:", "sr:"))}
    if rel in EARTH:
        return True, hard | soft | {"EARTH"}
    return bool(geo) or (bool(soft) and rel not in GENERIC), hard | soft


def classify(rel, van, own, earth, mod):
    """(Gruppe, Verweise)."""
    if own is not None:
        text = strip_comments(read(own))
        if not text.strip():
            if van is None:
                return "stub", set()
            is_earth, refs = vanilla_is_earth(rel, van, earth, mod)
            if not is_earth:
                return "stub-allgemein", refs
            if any(r.startswith(("s:", "sr:")) for r in refs) or rel in EARTH:
                return "stub", set()
            return "stub-pruefen", refs
        if rel in OVERRIDE:
            return "override", set()
        wow = wow_refs(text, mod)
        if van is None:
            return ("wow" if wow else "mod-ohne-vanilla"), wow
        if wow:
            return "kopie-mit-wow", wow
    is_earth, refs = vanilla_is_earth(rel, van, earth, mod)
    prefix = "kopie" if own is not None else "vanilla"
    return (f"{prefix}-erde" if is_earth else f"{prefix}-allgemein"), refs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--details", action="store_true")
    ap.add_argument("--stubs", action="store_true")
    ap.add_argument("--apply-copies", action="store_true")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    sys.stdout.reconfigure(encoding="utf-8")
    folder = args.folder.strip("/").replace("\\", "/")
    if not (VANILLA / folder).is_dir():
        log.error("%s gibt es in Vanilla nicht", folder)
        return 1
    if folder in replace_paths():
        log.warning("`%s` steht noch in replace_paths; Auswertung zeigt den Stand ohne diesen Eintrag", folder)

    earth, mod = known_objects()
    events = loaded_events()
    groups = {}
    for rel, (van, own) in sorted(folder_files(folder).items()):
        kind, refs = classify(rel, van, own, earth, mod)
        src = own if own is not None and strip_comments(read(own)).strip() else van
        missing = set(EVENT_ID.findall(strip_comments(read(src)))) - events if src is not None else set()
        groups.setdefault(kind, []).append((rel, refs, missing))

    hints = {
        "vanilla-erde": "Vanilla mit Erde-Inhalt, keine Mod-Datei → leer abschalten (--stubs)",
        "vanilla-allgemein": "Vanilla ohne Erde-Inhalt → lädt aus Vanilla",
        "kopie-erde": "Mod-Kopie ohne WoW-Bezug, Vanilla hat Erde-Inhalt → durch leere Datei ersetzen",
        "kopie-allgemein": "Mod-Kopie ohne WoW-Bezug, Vanilla allgemein → Kopie löschen",
        "kopie-mit-wow": "Mod-Kopie mit WoW-Bezug → prüfen, WoW-Teil in va_-Datei umziehen",
        "mod-ohne-vanilla": "Mod-Datei ohne Vanilla-Gegenstück und ohne WoW-Bezug → alte Vanilla-Datei? prüfen",
        "wow": "eigener WoW-Inhalt → bleibt",
        "override": "bewusster Vanilla-Override (OVERRIDE, ABLAUFPLAN) → bleibt, bei Patches gegen Vanilla vergleichen",
        "stub": "leere Datei → schaltet Vanilla ab (Erde-States/-Regionen oder EARTH)",
        "stub-pruefen": "leere Datei, Vanilla ohne s:/sr: → von Hand prüfen, ggf. in GENERIC aufnehmen",
        "stub-allgemein": "leere Datei, Vanilla allgemein → Stub löschen (--apply-copies)",
    }
    for kind, hint in hints.items():
        entries = groups.get(kind, [])
        print(f"\n## {kind} ({len(entries)}): {hint}")
        for rel, refs, missing in entries:
            extra = ""
            if args.details and refs:
                extra += f"  [{', '.join(sorted(refs)[:8])}{' …' if len(refs) > 8 else ''}]"
            if args.details and missing:
                extra += f"  ruft ungeladene Events: {len(missing)} ({', '.join(sorted(missing)[:3])} …)"
            print(f"- {rel}{extra}")

    if args.stubs:
        for rel, _, _ in groups.get("vanilla-erde", []):
            try:
                (REPO / rel).write_text(STUB, encoding="utf-8", newline=CRLF)
                log.info("abgeschaltet: %s", rel)
            except OSError as e:
                log.error("%s nicht anlegbar: %s", rel, e)

    if args.apply_copies:
        for rel, _, _ in groups.get("kopie-erde", []):
            try:
                (REPO / rel).write_text(STUB, encoding="utf-8", newline=CRLF)
                log.info("geleert: %s", rel)
            except OSError as e:
                log.error("%s nicht leerbar: %s", rel, e)
        for rel, _, _ in groups.get("kopie-allgemein", []) + groups.get("stub-allgemein", []):
            try:
                (REPO / rel).unlink()
                log.info("gelöscht: %s", rel)
            except OSError as e:
                log.error("%s nicht löschbar: %s", rel, e)
    return 0


if __name__ == "__main__":
    sys.exit(main())

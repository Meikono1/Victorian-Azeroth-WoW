"""Eventdateien klassifizieren: Erde-Inhalt, allgemeine Mechanik oder WoW-Inhalt (VA-002/VA-025).

Aufruf: python -I .claude/tools/va_events.py [--details] [--stubs] [--apply-copies]
  --details       je Datei die gefundenen Erde-Verweise ausgeben
  --stubs         für Vanilla-Dateien mit Erde-Inhalt ohne Mod-Gegenstück eine leere Datei anlegen
                  (abschalten nach Projektregel)
  --apply-copies  alte Mod-Kopien bereinigen: "kopie-allgemein" und "stub-allgemein" löschen, "kopie-erde" leeren.
                  Löscht Repo-Dateien (Christian hat Claude das Ausführen erlaubt, 2026-10-30).

Grundlage ist, was das Spiel ohne `events` in replace_paths lädt: Vanilla-Dateien unter events/
(rekursiv), gleichnamige Mod-Dateien ersetzen sie. Erde-Verweise sind c:/cu:/rel: auf Objekte, die nur
Vanilla definiert, s:/sr: auf States/Regionen, die der Mod nicht hat, und JEs, die der Mod nicht hat.
"""
import argparse
import logging
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # kein __pycache__ im Repo
sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I nimmt das Skriptverzeichnis aus sys.path
from va_script import REPO, VANILLA, replace_paths

log = logging.getLogger("va_events")

REF = re.compile(r"\b(cu|c|s|sr|rel):([A-Za-z_][A-Za-z0-9_]*)")
JE_REF = re.compile(r"\b(je_[A-Za-z0-9_]+)\b")
TOP_KEY = re.compile(r"^([A-Za-z_][A-Za-z0-9_\-]*)\s*=\s*\{", re.M)
STATE_KEY = re.compile(r"^\s*(STATE_[A-Za-z0-9_]+)\s*=", re.M)
# Allgemeine Mechaniken (Wahlen, Gesetze, Petitionen, Putsche …), die Erde-Länder/-Kulturen/-Religionen oder
# Vanilla-JEs nur nebenbei erwähnen. Sie laden aus Vanilla; fehlende JEs kommen mit journal_entries (VA-002).
# Von Hand ausgewählt 2026-10-30, Liste bei Patches ergänzen. s:/sr:-Verweise machen eine Datei trotzdem zu Erde.
GENERIC = {
	"events/agitators_events/agitators_election_events.txt",
	"events/agitators_events/coup_events.txt",
	"events/agitators_events/government_petition_events.txt",
	"events/agitators_events/land_ownership_law_events.txt",
	"events/agitators_events/revolution_events_02.txt",
	"events/assassination_events.txt",
	"events/character_events.txt",
	"events/cholera.txt",
	"events/communism.txt",
	"events/decree_events.txt",
	"events/election_events/election_other_parties_events.txt",
	"events/fascism_events.txt",
	"events/government_conflicts_events.txt",
	"events/iberia_events/subject_interaction_evts.txt",
	"events/ig_petitions.txt",
	"events/ig_suppression_events.txt",
	"events/law_events/education_laws.txt",
	"events/law_events/labor_rights_laws.txt",
	"events/law_events/labour_associations_events.txt",
	"events/law_events/slavery_laws.txt",
	"events/law_events/state_atheism.txt",
	"events/law_events/theocracy.txt",
	"events/law_events/welfare_laws_events.txt",
	"events/law_imposition_events.txt",
	"events/neighbor_events.txt",
	"events/prohibition_events.txt",
	"events/psychology_events.txt",
	"events/red_scare_events.txt",
	"events/secession_situations.txt",
	"events/standard_of_living_events.txt",
	"events/urbanization_events.txt",
	"events/soi_events/00_lobbies_events_04.txt",
	# Nachgeprüft 2026-10-30 (Hinweis Christian): Erde-Länder/-Kulturen nur als Namensverzweigung mit Fallback
	"events/nihilism.txt",
	"events/agitators_events/silkworm_diseases.txt",
	"events/agitators_events/slave_revolt_events.txt",
	"events/balkans_events/grunderzeit.txt",
	"events/balkans_events/hungry_forties.txt",
	"events/iberia_events/ip4_anarchism_events.txt",
	"events/iberia_events/ip4_coup_events.txt",
	"events/iberia_events/ip4_election_rigging.txt",
	"events/iberia_events/negotiation_events.txt",
}
# Mod-Kopien, die bleiben, bis common/journal_entries aus replace_paths kommt: Die Mod-JE-Kopie passt nur
# zu dieser alten Eventfassung (01_coup.txt ruft coup.2 … auf, die Vanilla 1.13 nicht mehr hat).
KEEP_COPY = {"events/agitators_events/coup_events.txt"}
CRLF = chr(13) + chr(10)  # Zeilenende wie in den übrigen Mod-Dateien
STUB ="\ufeff# Abgeschaltet (VA-002): Vanilla-Eventdatei mit Erde-Inhalt. Erzeugt von .claude/tools/va_events.py.\n"


def read(path):
    try:
        return path.read_text(encoding="utf-8-sig", errors="replace")
    except OSError as e:
        log.error("%s nicht lesbar: %s", path, e)
        return ""


def strip_comments(text):
    return "\n".join(line.split("#", 1)[0] for line in text.splitlines())


def names(root, folder, pattern=TOP_KEY):
    found = set()
    for f in (root / folder).glob("*.txt"):
        found |= {m.split(":", 1)[-1] for m in pattern.findall(strip_comments(read(f)))}
    return found


def known_objects():
    """Erde- und Mod-Objekte je Verweisart.

    hart: s/sr, die der Mod nicht hat, und Vanilla-JEs, die der Mod nicht hat (Lade- bzw. Laufzeitfehler).
    weich: c/cu/rel, die nur Vanilla definiert. Der Mod lädt die Vanilla-Definitionen mit, die Verweise sind
    also gültig, gehören aber zu Erde-Inhalt (Land existiert nie, Kultur/Religion kommt nicht vor).
    """
    earth, mod = {}, {}
    for kind, folder in (("c", "common/country_definitions"), ("cu", "common/cultures"), ("rel", "common/religions")):
        van, own = names(VANILLA, folder), names(REPO, folder)
        earth[kind], mod[kind] = van, own - van
    # religion.txt überschreibt Vanilla gleichnamig und enthält Erde- und WoW-Religionen gemischt
    earth["rel"] = names(VANILLA, "common/religions")
    mod["s"] = names(REPO, "map_data/state_regions", STATE_KEY)
    mod["sr"] = names(REPO, "common/strategic_regions")
    mod["je"] = names(REPO, "common/journal_entries")
    if "common/journal_entries" not in replace_paths():
        mod["je"] |= names(VANILLA, "common/journal_entries")
    earth["je"] = names(VANILLA, "common/journal_entries") - mod["je"]
    log.info("Mod: %d Länder, %d Kulturen, %d States, %d Regionen, %d JEs", len(mod["c"]), len(mod["cu"]),
             len(mod["s"]), len(mod["sr"]), len(mod["je"]))
    return earth, mod


def event_files():
    """Relativer Pfad → (Vanilla-Datei oder None, Mod-Datei oder None)."""
    files = {}
    for root, slot in ((VANILLA, 0), (REPO, 1)):
        for f in (root / "events").rglob("*.txt"):
            rel = f.relative_to(root).as_posix()
            files.setdefault(rel, [None, None])[slot] = f
    return files


def earth_refs(text, earth, mod):
    """(harte, weiche) Erde-Verweise, siehe known_objects."""
    hard, soft = set(), set()
    for kind, name in REF.findall(text):
        if kind in ("c", "cu", "rel"):
            if name in earth[kind]:
                soft.add(f"{kind}:{name}")
        elif name not in mod[kind]:
            hard.add(f"{kind}:{name}")
    hard |= {je for je in JE_REF.findall(text) if je in earth["je"]}
    return hard, soft


def wow_refs(text, mod):
    return {f"{k}:{n}" for k, n in REF.findall(text) if k in ("c", "cu", "rel") and n in mod[k]} |            {f"s:{n}" for k, n in REF.findall(text) if k == "s" and n in mod["s"]}


def classify_stub(rel, van, earth, mod):
    """Leere Mod-Datei: abgeschaltete allgemeine Dateien und Grenzfälle ohne s:/sr: getrennt ausweisen."""
    if van is None:
        return "stub", set()
    hard, soft = earth_refs(strip_comments(read(van)), earth, mod)
    if rel in GENERIC:
        missing_je = {r for r in hard if r.startswith("je_")}
        return ("stub-wartet-je" if missing_je else "stub-allgemein"), missing_je
    if any(r.startswith(("s:", "sr:")) for r in hard):
        return "stub", set()
    return "stub-pruefen", hard | soft


def classify(rel, van, own, earth, mod):
    """(Gruppe, Verweise). Erde = s:/sr:-Verweise, oder andere Erde-Verweise ohne Eintrag in GENERIC."""
    if own is not None:
        text = strip_comments(read(own))
        if not text.strip():
            return classify_stub(rel, van, earth, mod)
        wow = wow_refs(text, mod)
        if van is None:
            return ("wow" if wow else "mod-ohne-vanilla"), wow
        if wow:
            return "kopie-mit-wow", wow
        if rel in KEEP_COPY:
            return "kopie-behalten", set()
    hard, soft = earth_refs(strip_comments(read(van)), earth, mod)
    geo = {r for r in hard if r.startswith(("s:", "sr:"))}
    is_earth = bool(geo) or (bool(hard | soft) and rel not in GENERIC)
    prefix = "kopie" if own is not None else "vanilla"
    return (f"{prefix}-erde" if is_earth else f"{prefix}-allgemein"), hard | soft


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--details", action="store_true")
    ap.add_argument("--stubs", action="store_true")
    ap.add_argument("--apply-copies", action="store_true")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    sys.stdout.reconfigure(encoding="utf-8")
    if "events" in replace_paths():
        log.warning("`events` steht noch in replace_paths; Auswertung zeigt den Stand ohne diesen Eintrag")

    earth, mod = known_objects()
    groups = {}
    for rel, (van, own) in sorted(event_files().items()):
        kind, refs = classify(rel, van, own, earth, mod)
        groups.setdefault(kind, []).append((rel, refs))

    hints = {
        "vanilla-erde": "Vanilla mit Erde-Inhalt, keine Mod-Datei → leer abschalten (--stubs)",
        "vanilla-allgemein": "Vanilla ohne Erde-Inhalt → lädt aktuell aus Vanilla",
        "kopie-erde": "Mod-Kopie ohne WoW-Bezug, Vanilla hat Erde-Inhalt → durch leere Datei ersetzen",
        "kopie-allgemein": "Mod-Kopie ohne WoW-Bezug, Vanilla allgemein → Kopie löschen",
        "kopie-mit-wow": "Mod-Kopie mit WoW-Bezug → prüfen, WoW-Teil in va_-Datei umziehen",
        "kopie-behalten": "Mod-Kopie bleibt vorerst (KEEP_COPY, siehe Kommentar)",
        "mod-ohne-vanilla": "Mod-Datei ohne Vanilla-Gegenstück und ohne WoW-Bezug → alte Vanilla-Datei? prüfen",
        "wow": "eigener WoW-Inhalt → bleibt",
        "stub": "leere Datei → schaltet Vanilla ab (Erde-States/-Regionen)",
        "stub-pruefen": "leere Datei, Vanilla ohne s:/sr: → von Hand prüfen, ggf. in GENERIC aufnehmen",
        "stub-allgemein": "leere Datei, aber in GENERIC → Stub löschen (--apply-copies)",
        "stub-wartet-je": "leere Datei in GENERIC, braucht noch nicht geladene Vanilla-JEs → bleibt bis journal_entries",
    }
    for kind, hint in hints.items():
        entries = groups.get(kind, [])
        print(f"\n## {kind} ({len(entries)}): {hint}")
        for rel, refs in entries:
            extra = f"  [{', '.join(sorted(refs)[:8])}{' …' if len(refs) > 8 else ''}]" if args.details and refs else ""
            print(f"- {rel}{extra}")

    if args.stubs:
        for rel, _ in groups.get("vanilla-erde", []):
            target = REPO / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(STUB, encoding="utf-8", newline=CRLF)
            log.info("abgeschaltet: %s", rel)

    if args.apply_copies:
        for rel, _ in groups.get("kopie-erde", []):
            try:
                (REPO / rel).write_text(STUB, encoding="utf-8", newline=CRLF)
                log.info("geleert: %s", rel)
            except OSError as e:
                log.error("%s nicht leerbar: %s", rel, e)
        for rel, _ in groups.get("kopie-allgemein", []) + groups.get("stub-allgemein", []):
            try:
                (REPO / rel).unlink()
                log.info("gelöscht: %s", rel)
            except OSError as e:
                log.error("%s nicht löschbar: %s", rel, e)


if __name__ == "__main__":
    main()

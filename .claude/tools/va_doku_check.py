"""Größe der Projekt-Doku in .claude/ gegen feste Grenzen prüfen (VA-074, Kono 2026-11-14).

Die Doku ist das Projektgedächtnis für 2–3 Jahre Weiterentwicklung. Was vor fast jeder Aufgabe geladen wird,
muss klein bleiben, sonst kostet jede Session unnötig Tokens. Gemessen wird in Zeichen (grob 4 Zeichen ≈ 1 Token).

Grenzen (Regel in CLAUDE.md, Abschnitt „Doku schlank halten“):
  Index-Dateien (CLAUDE.md, KARTE.md, karte/*, ABLAUFPLAN.md, tickets/README.md, skills/*/SKILL.md)  15.000 Zeichen
  Skills zusätzlich                                                                                    150 Zeilen
  ablauf/<land>.md                                                                                     25.000 Zeichen
  offene Tickets VA-*.md (in einer Session erledigbar, Verlauf nach tickets/verlauf/)                 10.000 Zeichen
  TESTPROTOKOLL.md (nur offene Fälle)                                                                  50.000 Zeichen
Ohne Grenze (nur gezielt gelesen oder generiert): Archive, tickets/verlauf/, ERLEDIGT.md, ablauf/lore/, konzepte/, recherche/,
regionen/, laender_uebersicht.md, Zusatzdateien der Skills.

Aufrufe:
  python -I .claude/tools/va_doku_check.py         nur Überschreitungen und Dateien ab 80 % der Grenze
  python -I .claude/tools/va_doku_check.py --all   alle geprüften Dateien mit Größe
Exit-Code 1, wenn eine Grenze überschritten ist. Abhilfe: aufteilen (Index + Teildatei, Sammel- + Teiltickets),
Erledigtes archivieren, Verlauf/Lore auslagern.
"""
import argparse
import logging
import sys
from pathlib import Path

log = logging.getLogger("va_doku_check")

DOC = Path(__file__).resolve().parents[1]

INDEX_LIMIT = 15_000
SKILL_LINES = 150
DETAIL_LIMIT = 25_000
TICKET_LIMIT = 10_000
TESTPROTOKOLL_LIMIT = 50_000
WARN_SHARE = 0.8


def rules():
    """Liefert (Pfad, Zeichengrenze, Zeilengrenze oder None) für alle geprüften Dateien."""
    out = []
    for name in ("CLAUDE.md", "KARTE.md", "ABLAUFPLAN.md", "tickets/README.md"):
        out.append((DOC / name, INDEX_LIMIT, None))
    out += [(p, INDEX_LIMIT, None) for p in sorted((DOC / "karte").glob("*.md"))]
    out += [(p, INDEX_LIMIT, SKILL_LINES) for p in sorted((DOC / "skills").glob("*/SKILL.md"))]
    out += [(p, DETAIL_LIMIT, None) for p in sorted((DOC / "ablauf").glob("*.md"))]
    out += [(p, TICKET_LIMIT, None) for p in sorted((DOC / "tickets").glob("VA-*.md"))]
    out.append((DOC / "TESTPROTOKOLL.md", TESTPROTOKOLL_LIMIT, None))
    return out


def measure(path):
    """Zeichen und Zeilen einer Datei (BOM zählt nicht)."""
    text = path.read_text(encoding="utf-8-sig")
    return len(text), text.count("\n") + 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--all", action="store_true", help="alle geprüften Dateien anzeigen")
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")  # -I ignoriert PYTHONIOENCODING
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    over = 0
    for path, char_limit, line_limit in rules():
        rel = path.relative_to(DOC).as_posix()
        if not path.exists():
            log.warning("fehlt: %s", rel)
            continue
        try:
            chars, lines = measure(path)
        except (OSError, UnicodeDecodeError) as exc:
            log.error("nicht lesbar: %s (%s)", rel, exc)
            over += 1
            continue
        problems = []
        if chars > char_limit:
            problems.append(f"{chars:,} > {char_limit:,} Zeichen")
        if line_limit and lines > line_limit:
            problems.append(f"{lines} > {line_limit} Zeilen")
        if problems:
            over += 1
            print(f"ÜBER  {rel}: {', '.join(problems)}")
        elif chars > char_limit * WARN_SHARE:
            print(f"knapp {rel}: {chars:,} von {char_limit:,} Zeichen")
        elif args.all:
            print(f"ok    {rel}: {chars:,} von {char_limit:,} Zeichen")

    print(f"Doku-Prüfung: {over} Datei(en) über der Grenze.")
    return 1 if over else 0


if __name__ == "__main__":
    sys.exit(main())

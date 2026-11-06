"""Erde-JEs als nie aktivierbare Platzhalter definieren (VA-003/VA-043).

Aufruf: python -I .claude/tools/va_gen_earth_je_stubs.py [--apply]
  ohne --apply  nur zählen

Der Mod schaltet Vanillas Erde-JEs per leerer gleichnamiger Datei ab. Vanilla-Scripts (KI, Gesetze, Ideologien,
Events …) fragen sie aber weiter ab (has_journal_entry = je_acw_war …) und erzeugen je Start über 1.400 Fehlerzeilen.
Dieses Skript schreibt für jede JE aus einer abgeschalteten Vanilla-Datei eine Hülle gleichen Namens, die nie
sichtbar, nie möglich und sofort ungültig ist. Die Loc liefert Vanilla. Bei jedem Patch und nach neuen Stubs neu laufen lassen.
"""
import argparse
import logging
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # kein __pycache__ im Repo
sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I nimmt das Skriptverzeichnis aus sys.path
from va_script import REPO, VANILLA

log = logging.getLogger("va_gen_earth_je_stubs")

FOLDER = "common/journal_entries"
OUT = REPO / FOLDER / "va_earth_je_stubs.txt"
JE = re.compile(r'^﻿?(je_\w+)\s*=\s*\{', re.M)  # nur erste Spalte; eingerückt sind Effekte wie je_tsarpoints_add_partial (1.15)
STUB_LIMIT = 200  # Bytes; kleinere Mod-Dateien gelten als Abschalt-Stub
GROUP = "je_group_historical_content"
TEMPLATE = """
{key} = {{
	group = {group}
	icon = "gfx/interface/icons/event_icons/event_portrait.dds"
	is_shown_when_inactive = {{ always = no }}
	possible = {{ always = no }}
	disable_evaluation = {{ always = yes }}
	outcome = {{
		flags = {{ hidden invalid_outcome }}
		conclusion_desc = je_standard_failure_conclusion_desc
		trigger = {{ always = yes }}
	}}
}}
"""
# Seit 1.15 ersetzt `outcome` die Blöcke complete/fail/invalid/timeout (Vanilla journal_entries.md). Die Hülle wird per
# disable_evaluation nie geprüft; kommt sie doch per add_journal_entry, endet sie sofort still (Vorbild 00_abolish_monarchy.txt).


def keys(path):
	return JE.findall(path.read_text(encoding="utf-8-sig", errors="replace"))


def main():
	ap = argparse.ArgumentParser()
	ap.add_argument("--apply", action="store_true")
	args = ap.parse_args()
	logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

	van, mod = VANILLA / FOLDER, REPO / FOLDER
	if not van.is_dir():
		log.error("Vanilla-Ordner fehlt: %s", van)
		return 1
	groups = set()
	for f in (VANILLA / "common/journal_entry_groups").glob("*.txt"):
		groups |= set(re.findall(r'^\W*(je_group_\w+)\s*=', f.read_text(encoding="utf-8-sig"), re.M))
	if GROUP not in groups:
		log.error("Gruppe %s gibt es in Vanilla nicht mehr, GROUP anpassen", GROUP)
		return 1

	# Was der Mod tatsächlich lädt: eigene Dateien (ohne diese) plus Vanilla-Dateien ohne Mod-Gegenstück
	loaded = set()
	for f in mod.glob("*.txt"):
		if f != OUT:
			loaded |= set(keys(f))
	stubbed = []
	for f in sorted(van.glob("*.txt")):
		m = mod / f.name
		if not m.exists():
			loaded |= set(keys(f))
		elif m.stat().st_size < STUB_LIMIT:
			stubbed.append(f)
	missing = []
	for f in stubbed:
		missing += [k for k in keys(f) if k not in loaded and k not in missing]

	text = ["﻿# Hüllen für abgeschaltete Erde-JEs (VA-043), erzeugt von .claude/tools/va_gen_earth_je_stubs.py – nicht von Hand ändern.\n"
	        "# Vorbild: Vanilla journal_entries.md. Nie sichtbar, nie möglich, sofort ungültig; hält nur Vanilla-Verweise gültig.\n"]
	text += [TEMPLATE.format(key=k, group=GROUP) for k in missing]
	log.info("%d abgeschaltete Dateien, %d JE-Hüllen", len(stubbed), len(missing))
	if args.apply:
		OUT.write_text("".join(text), encoding="utf-8", newline="\n")
		log.info("geschrieben: %s", OUT.relative_to(REPO).as_posix())
	return 0


if __name__ == "__main__":
	sys.exit(main())

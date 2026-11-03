"""Abgeschaltete Erde-Charaktervorlagen als leere Hüllen definieren (VA-043).

Aufruf: python -I .claude/tools/va_gen_earth_template_stubs.py [--apply]
  ohne --apply  nur zählen

Der Mod schaltet Vanillas Erde-Vorlagen (common/character_templates/country_*.txt u. a.) per leerer gleichnamiger
Datei ab. Vanillas Porträt-, Erbfolge- und KI-Scripts fragen sie weiter ab (has_template = JAP_ninko_yamato …,
rund 1.200 Logzeilen je Start). Dieses Skript schreibt für jede aufgerufene Vorlage eine Hülle nach dem Muster
von Vanillas test_template.txt: nur `age`, keine Kultur, Religion, Rolle oder Verwendungsregel (usage/trigger),
damit das Spiel sie nie selbst aufgreift. Bei jedem Patch und nach neuen Stubs neu laufen lassen.
"""
import argparse
import logging
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # kein __pycache__ im Repo
sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I nimmt das Skriptverzeichnis aus sys.path
from va_script import REPO, VANILLA, replace_paths

log = logging.getLogger("va_gen_earth_template_stubs")

FOLDER = "common/character_templates"
OUT = REPO / FOLDER / "va_earth_template_stubs.txt"
STUB_LIMIT = 200  # Bytes; kleinere Mod-Dateien gelten als Abschalt-Stub
KEY = re.compile(r"^﻿?([^\s=#{}\"]+)\s*=\s*\{", re.M)  # nur Spalte 0; Namen mit - und ć kommen vor
WORD = re.compile(r"[^\s=#{}\"<>!?]+")
TEMPLATE = "\n{key} = {{\n\tage = 40\n}}\n"


def read(path):
	return path.read_text(encoding="utf-8-sig", errors="replace")


def main():
	ap = argparse.ArgumentParser()
	ap.add_argument("--apply", action="store_true")
	args = ap.parse_args()
	logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

	van, mod = VANILLA / FOLDER, REPO / FOLDER
	if not van.is_dir():
		log.error("Vanilla-Ordner fehlt: %s", van)
		return 1
	loaded, candidates = set(), []
	for f in mod.glob("*.txt"):
		if f != OUT:
			loaded |= set(KEY.findall(read(f)))
	for f in sorted(van.glob("*.txt")):
		m = mod / f.name
		if not m.exists():
			loaded |= set(KEY.findall(read(f)))
		elif m.stat().st_size < STUB_LIMIT:
			candidates += KEY.findall(read(f))
	candidates = [k for k in dict.fromkeys(candidates) if k not in loaded]

	# Nur Vorlagen, die eine geladene Datei nennt (Mod-Dateien plus Vanilla ohne Mod-Gegenstück, ohne die Vorlagen selbst)
	referenced = set()
	replaced = replace_paths()  # z. B. common/history/*: Vanilla lädt dort gar nicht
	for base, sub in [(REPO, "common"), (REPO, "events"), (REPO, "gfx"), (VANILLA, "common"), (VANILLA, "events"), (VANILLA, "gfx")]:
		for f in (base / sub).rglob("*.txt"):
			rel = f.relative_to(base)
			if base == VANILLA and ((REPO / rel).exists() or any(rel.as_posix().startswith(p + "/") for p in replaced)):
				continue
			if rel.parts[:2] == ("common", "character_templates"):
				continue
			referenced |= set(WORD.findall(read(f)))
	stubs = [k for k in candidates if k in referenced]

	text = ["﻿# Hüllen für abgeschaltete Erde-Charaktervorlagen (VA-043), erzeugt von .claude/tools/va_gen_earth_template_stubs.py – nicht von Hand ändern.\n"
	        "# Vorbild: Vanilla test_template.txt. Ohne Kultur und Verwendungsregel, hält nur Vanilla-Verweise (has_template …) gültig.\n"]
	text += [TEMPLATE.format(key=k) for k in stubs]
	log.info("%d abgeschaltete Vorlagen, davon %d aufgerufen", len(candidates), len(stubs))
	if args.apply:
		OUT.write_text("".join(text), encoding="utf-8", newline="\n")
		log.info("geschrieben: %s", OUT.relative_to(REPO).as_posix())
	return 0


if __name__ == "__main__":
	sys.exit(main())

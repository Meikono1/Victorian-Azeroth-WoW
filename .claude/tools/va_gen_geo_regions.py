"""Leere Gegenstücke zu Vanillas geographic_regions erzeugen (VA-026).

Aufruf: python -I .claude/tools/va_gen_geo_regions.py [--apply]
  ohne --apply  nur zählen, was geschrieben würde

Jede Vanilla-Region listet Erde-State-/Strategic-Regionen, die es im Mod nicht gibt (rund 1.300 Fehler je Start).
Die Datei gleichen Namens im Mod definiert dieselben Regionen mit gleichem short_key, aber ohne Inhalt.
So bleiben Verweise in Vanilla-Scripts (geographic_region:…, any_state_in_<short_key>) gültig und sind einfach leer.
Regionen, die der Mod in va_*-Dateien selbst füllt, werden übersprungen. Bei jedem Patch neu laufen lassen.
"""
import argparse
import logging
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # kein __pycache__ im Repo
sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I nimmt das Skriptverzeichnis aus sys.path
from va_script import REPO, VANILLA

log = logging.getLogger("va_gen_geo_regions")

FOLDER = "common/geographic_regions"
REGION = re.compile(r'^\W*(geographic_region_\w+)\s*=\s*\{', re.M)
SHORT_KEY = re.compile(r'short_key\s*=\s*"([^"]*)"')
HEADER = ("# Erde-Regionen ohne Inhalt (VA-026), erzeugt von .claude/tools/va_gen_geo_regions.py – nicht von Hand ändern.\n"
          "# Vorbild: Vanilla {name}. Gleiche Schlüssel und short_keys, damit Vanilla-Verweise gültig bleiben.\n")


def regions(text):
	"""(Schlüssel, short_key) je Region in Dateireihenfolge."""
	out = []
	starts = [m for m in REGION.finditer(text)]
	for i, m in enumerate(starts):
		end = starts[i + 1].start() if i + 1 < len(starts) else len(text)
		sk = SHORT_KEY.search(text, m.end(), end)
		out.append((m.group(1), sk.group(1) if sk else None))
	return out


def own_regions():
	"""Regionen, die eigene va_-Dateien definieren."""
	own = set()
	for f in (REPO / FOLDER).glob("va_*.txt"):
		own |= {k for k, _ in regions(f.read_text(encoding="utf-8-sig"))}
	return own


def main():
	ap = argparse.ArgumentParser()
	ap.add_argument("--apply", action="store_true")
	args = ap.parse_args()
	logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

	src = VANILLA / FOLDER
	if not src.is_dir():
		log.error("Vanilla-Ordner fehlt: %s", src)
		return 1
	own = own_regions()
	(REPO / FOLDER).mkdir(parents=True, exist_ok=True)
	total = 0
	for f in sorted(src.glob("*.txt")):
		regs = [(k, sk) for k, sk in regions(f.read_text(encoding="utf-8-sig")) if k not in own]
		if not regs:
			log.warning("%s: keine Regionen gefunden", f.name)
			continue
		lines = [HEADER.format(name=f.name)]
		for key, sk in regs:
			lines.append(f'\n{key} = {{\n\tshort_key = "{sk}"\n}}\n' if sk else f'\n{key} = {{\n}}\n')
			if not sk:
				log.warning("%s: %s ohne short_key", f.name, key)
		total += len(regs)
		log.info("%s: %d Regionen", f.name, len(regs))
		if args.apply:
			(REPO / FOLDER / f.name).write_text("﻿" + "".join(lines), encoding="utf-8", newline="\n")
	log.info("%d Regionen %s", total, "geschrieben" if args.apply else "(Probelauf, --apply schreibt)")
	return 0


if __name__ == "__main__":
	sys.exit(main())

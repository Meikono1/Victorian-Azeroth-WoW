"""Vanilla-Dateien, deren Bedingungen Erde-States prüfen, als entschärfte Kopie erzeugen (VA-043).

Aufruf: python -I .claude/tools/va_gen_earth_overrides.py [--apply]
  ohne --apply  nur auflisten, was entschärft würde

Vanilla prüft in oft ausgewerteten Bedingungen Erde-States (state_region = s:STATE_HOME_COUNTIES). Die gibt es im
Mod nicht; das Spiel schreibt dann je Prüfung "Invalid right side during comparison 's'" (bis 9.000 Zeilen in
wenigen Spielmonaten). Leere Dateien gehen nicht, weil Vanilla-Scripts die Objekte beim Namen nennen.
Deshalb wird jede Datei aus FILES 1:1 übernommen; nur in Objekten mit unbekannten STATE_-Namen werden die in FILES
genannten Blöcke erster Ebene durch `= { always = no }` ersetzt, sofern sie selbst einen unbekannten State enthalten,
und die genannten Zeilen (DROP) gestrichen. Neue Fälle: Datei aus dem error.log in FILES aufnehmen.
Bei jedem Patch neu laufen lassen.
"""
import argparse
import logging
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # kein __pycache__ im Repo
sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I nimmt das Skriptverzeichnis aus sys.path
from va_script import REPO, VANILLA

log = logging.getLogger("va_gen_earth_overrides")

# Datei → (zu entschärfende Blöcke erster Ebene, zu streichende Zeilen erster Ebene)
FILES = {
	"common/buildings/08_monuments.txt": (("potential", "possible"), ()),
	"common/buildings/10_canals.txt": (("potential", "possible"), ("strait",)),  # strait_definitions ist leer
	"common/power_bloc_names/00_power_bloc_names.txt": (("trigger",), ()),
	"common/political_movements/03_pan_national_movements.txt": (("creation_trigger",), ()),
	# Regierungsformen nur für Erde-Tags (gov_nawabate: c:BHW …), je Start ~290 "Failed to find country"
	"common/government_types/01_monarchies.txt": (("possible",), ()),
	"common/government_types/01_regencies.txt": (("possible",), ()),
	"common/government_types/01_social_monarchies.txt": (("possible",), ()),
	"common/government_types/05_council_republics.txt": (("possible",), ()),
	# Errungenschaften: achievement_groups.txt nennt sie beim Namen, deshalb keine leeren Dateien
	"common/achievements/base_achievements.txt": (("possible", "happened"), ()),
	"common/achievements/ep1_sphere_of_influence_achievements.txt": (("possible", "happened"), ()),
	"common/achievements/ep2_the_great_wave_achievements.txt": (("possible", "happened"), ()),
	"common/achievements/ip2_pivot_of_empire_achievements.txt": (("possible", "happened"), ()),
	"common/achievements/ip3_national_awakening_achievements.txt": (("possible", "happened"), ()),
	"common/achievements/ip4_iberian_twilight_achievements.txt": (("possible", "happened"), ()),
}
STATE = re.compile(r"\bSTATE_[A-Z0-9_]+")
REGION = re.compile(r"\bsr:(region_\w+)")
COUNTRY = re.compile(r"\bc:([A-Z][A-Z0-9_]*)\b")
TOP = re.compile(r"^([A-Za-z_]\w*)\s*=\s*\{", re.M)
HEADER = ("# Erzeugt von .claude/tools/va_gen_earth_overrides.py aus Vanilla {name} – nicht von Hand ändern (VA-043).\n"
          "# Objekte mit Erde-States, -Regionen oder -Tags: {keys} = always = no{drop}. Rest unverändert Vanilla.\n")


def mod_states():
	"""State- und Strategic-Regionen des Mods (eine Menge, die Namen kollidieren nicht)."""
	known = set()
	for f in (REPO / "map_data/state_regions").glob("*.txt"):
		known |= set(re.findall(r"^(STATE_\w+)\s*=", f.read_text(encoding="utf-8-sig"), re.M))
	for f in (REPO / "common/strategic_regions").glob("*.txt"):
		known |= set(re.findall(r"^(region_\w+)\s*=", f.read_text(encoding="utf-8-sig"), re.M))
	# Länder-Tags, die das Spiel lädt: Mod-Definitionen plus Vanilla-Dateien ohne Mod-Gegenstück
	tags = set()
	for base in (REPO, VANILLA):
		for f in (base / "common/country_definitions").glob("*.txt"):
			if base == VANILLA and (REPO / "common/country_definitions" / f.name).exists():
				continue
			tags |= set(re.findall(r"^﻿?([A-Z][A-Z0-9_]*)\s*=\s*\{", f.read_text(encoding="utf-8-sig", errors="replace"), re.M))
	known |= {"c:" + t for t in tags}
	return known


def earth(text, known):
	"""Enthält text State-/Strategic-Regionen oder Länder-Tags, die der Mod nicht hat?"""
	return (any(s not in known for s in STATE.findall(text)) or any(r not in known for r in REGION.findall(text))
	        or any("c:" + t not in known for t in COUNTRY.findall(text)))


def block_end(text, open_pos):
	"""Index hinter der schließenden Klammer zum '{' an open_pos."""
	depth = 0
	for i in range(open_pos, len(text)):
		if text[i] == "{":
			depth += 1
		elif text[i] == "}":
			depth -= 1
			if depth == 0:
				return i + 1
	raise ValueError(f"Klammer ab {open_pos} nicht geschlossen")


def first_level(body, key):
	"""Start/Ende aller Blöcke `key = {` direkt unter der obersten Klammer von body."""
	out, depth, i = [], 0, 0
	pat = re.compile(rf"\b{key}\s*=\s*\{{")
	while i < len(body):
		c = body[i]
		if c == "#":
			i = body.find("\n", i) if "\n" in body[i:] else len(body)
			continue
		if c == "{":
			depth += 1
		elif c == "}":
			depth -= 1
		elif depth == 1:
			m = pat.match(body, i)
			if m and (i == 0 or not (body[i - 1].isalnum() or body[i - 1] == "_")):
				end = block_end(body, m.end() - 1)
				out.append((i, end))
				i = end
				continue
		i += 1
	return out


def neutralize(body, keys, drop, states):
	for key in drop:
		body = re.sub(rf"^\t{key}\s*=\s*\S+[ \t]*\n", "", body, flags=re.M)
	hits = []
	for key in keys:
		for s, e in first_level(body, key):
			if earth(body[s:e], states):
				hits.append((s, e, key))
	for s, e, key in sorted(hits, reverse=True):
		body = body[:s] + f"{key} = {{ always = no }} # VA: Erde-Bezug" + body[e:]
	return body, bool(hits)


def convert(text, keys, drop, states):
	out, pos, changed = [], 0, []
	for m in TOP.finditer(text):
		if m.start() < pos:
			continue
		end = block_end(text, m.end() - 1)
		block = text[m.start():end]
		if earth(block, states):
			block, hit = neutralize(block, keys, drop, states)
			if hit:
				changed.append(m.group(1))
		out.append(text[pos:m.start()])
		out.append(block)
		pos = end
	out.append(text[pos:])
	return "".join(out), changed


def main():
	ap = argparse.ArgumentParser()
	ap.add_argument("--apply", action="store_true")
	args = ap.parse_args()
	logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

	states = mod_states()
	if not states:
		log.error("keine State-Regionen im Mod gefunden")
		return 1
	for rel, (keys, drop) in FILES.items():
		src = VANILLA / rel
		if not src.exists():
			log.error("Vanilla-Datei fehlt: %s", rel)
			return 1
		text, changed = convert(src.read_text(encoding="utf-8-sig"), keys, drop, states)
		log.info("%s: %d Objekte entschärft", rel, len(changed))
		log.debug("%s", ", ".join(changed))
		if args.apply:
			(REPO / rel).parent.mkdir(parents=True, exist_ok=True)
			head = HEADER.format(name=src.name, keys="/".join(keys), drop=", " + "/".join(drop) + " gestrichen" if drop else "")
			(REPO / rel).write_text("﻿" + head + text, encoding="utf-8", newline="\n")
	return 0


if __name__ == "__main__":
	sys.exit(main())

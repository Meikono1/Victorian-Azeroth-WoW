"""Abgeschaltete Erde-Events als versteckte, nie auslösende Hüllen definieren (VA-043).

Aufruf: python -I .claude/tools/va_gen_earth_event_stubs.py [--apply]
  ohne --apply  nur zählen

Der Mod schaltet Vanillas Erde-Eventdateien per leerer gleichnamiger Datei ab. Vanillas On-Actions und Effekte
rufen die Events aber weiter auf ("does not have a valid namespace", "unknown random event", rund 580 Zeilen je Start).
Dieses Skript schreibt je abgeschalteter Vanilla-Datei eine Datei unter events/va_earth_event_stubs/ mit denselben
Namespaces und den Event-IDs, die irgendwo aufgerufen werden: hidden, trigger = always = no, Gewicht 0. random_events wählt nur gültige Events
(Vanilla _on_actions.md), die Häufigkeit anderer Events ändert sich also nicht. Bei Patches und nach neuen Stubs neu laufen lassen.
"""
import argparse
import logging
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # kein __pycache__ im Repo
sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I nimmt das Skriptverzeichnis aus sys.path
from va_script import REPO, VANILLA, replace_paths

log = logging.getLogger("va_gen_earth_event_stubs")

OUT = REPO / "events" / "va_earth_event_stubs"
STUB_LIMIT = 200  # Bytes; kleinere Mod-Dateien gelten als Abschalt-Stub
NAMESPACE = re.compile(r"^\s*namespace\s*=\s*([A-Za-z0-9_]+)", re.M)
EVENT = re.compile(r"^\s*([A-Za-z0-9_]+)\.(\d+)\s*=\s*\{", re.M)
TYPE = re.compile(r"^\s+type\s*=\s*(\w+_event)\b", re.M)
COMMENT = re.compile(r"#[^\n]*")
REF = re.compile(r"(?<![\w.])([A-Za-z0-9_]+\.\d+)\b(?!\.\d)")  # Namespaces dürfen mit Ziffer beginnen (1848.1); Datum 1848.4.7 ist kein Aufruf
TEMPLATE = """
{eid} = {{
	type = {etype}
	hidden = yes
	trigger = {{ always = no }}
	weight_multiplier = {{ factor = 0 }}
}}
"""


def read(path):
	return path.read_text(encoding="utf-8-sig", errors="replace")


def events(text):
	"""(ID, Typ) je Event; Typ aus dem ersten type = …_event im Block."""
	starts = list(EVENT.finditer(text))
	out = []
	for i, m in enumerate(starts):
		end = starts[i + 1].start() if i + 1 < len(starts) else len(text)
		t = TYPE.search(text, m.end(), end)
		out.append((f"{m.group(1)}.{m.group(2)}", t.group(1) if t else "country_event"))
	return out


def main():
	ap = argparse.ArgumentParser()
	ap.add_argument("--apply", action="store_true")
	args = ap.parse_args()
	logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

	van = VANILLA / "events"
	if not van.is_dir():
		log.error("Vanilla-Ordner fehlt: %s", van)
		return 1
	# IDs, die der Mod sonst lädt (eigene Dateien und Vanilla ohne Mod-Gegenstück), nicht doppelt anlegen
	loaded, stubbed = set(), []
	for f in (REPO / "events").rglob("*.txt"):
		if OUT not in f.parents:
			loaded |= {e for e, _ in events(read(f))}
	for f in sorted(van.rglob("*.txt")):
		mod = REPO / "events" / f.relative_to(van)
		if not mod.exists():
			loaded |= {e for e, _ in events(read(f))}
		elif mod.stat().st_size < STUB_LIMIT:
			stubbed.append(f)

	# Nur aufgerufene Events bekommen eine Hülle; unbenutzte meldet das Spiel sonst als "orphaned" (1.008× im Lauf 03.11.)
	referenced = set()
	sources = [f for f in (REPO / "common").rglob("*.txt")] + [f for f in (REPO / "events").rglob("*.txt") if OUT not in f.parents]
	replaced = replace_paths()  # z. B. common/history/*: Vanilla lädt dort gar nicht
	sources += [f for f in (VANILLA / "common").rglob("*.txt") if not (REPO / f.relative_to(VANILLA)).exists()
	            and not any(f.relative_to(VANILLA).as_posix().startswith(p + "/") for p in replaced)]
	sources += [f for f in van.rglob("*.txt") if not (REPO / "events" / f.relative_to(van)).exists()]
	for f in sources:
		text = EVENT.sub("", COMMENT.sub("", read(f)))  # Definitionen und Kommentare (# … serbian_throne.4) zählen nicht als Aufruf
		referenced |= set(REF.findall(text))

	files, total = {}, 0
	for f in stubbed:
		text = read(f)
		evs = [(e, t) for e, t in events(text) if e not in loaded and e in referenced]
		if not evs:
			continue
		used = {e.split(".")[0] for e, _ in evs}
		spaces = [n for n in dict.fromkeys(NAMESPACE.findall(text)) if n in used]
		missing = used - set(spaces)
		if missing:
			log.warning("%s: Events ohne Namespace in der Datei: %s", f.name, ", ".join(sorted(missing)))
			spaces += sorted(missing)
		rel = f.relative_to(van).as_posix()
		body = [f"﻿# Hüllen für abgeschaltete Vanilla-Events aus events/{rel} (VA-043), erzeugt von .claude/tools/va_gen_earth_event_stubs.py – nicht von Hand ändern.\n"]
		body += [f"namespace = {n}\n" for n in spaces]
		body += [TEMPLATE.format(eid=e, etype=t) for e, t in evs]
		files["va_stub_" + rel.replace("/", "__")] = "".join(body)
		total += len(evs)
	log.info("%d abgeschaltete Dateien, %d Stub-Dateien, %d Event-Hüllen", len(stubbed), len(files), total)
	if args.apply:
		OUT.mkdir(parents=True, exist_ok=True)
		for old in OUT.glob("va_stub_*.txt"):
			if old.name not in files:
				old.unlink()  # eigener Ausgabeordner, nur erzeugte Dateien
				log.info("veraltet, entfernt: %s", old.relative_to(REPO).as_posix())
		for name, text in files.items():
			(OUT / name).write_text(text, encoding="utf-8", newline="\n")
		log.info("geschrieben nach %s", OUT.relative_to(REPO).as_posix())
	return 0


if __name__ == "__main__":
	sys.exit(main())

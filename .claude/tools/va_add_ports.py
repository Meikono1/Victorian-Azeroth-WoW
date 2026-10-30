"""Start-Häfen für Länder mit Küste, aber ohne Hafen (VA-029, Weltmarkt-Anbindung).

Aufruf: python -I .claude/tools/va_add_ports.py 21 22 23 24 25 26 27 28 [--apply]
  Präfixe der Regionen, die Häfen bekommen. Bestehende Häfen zählen aus allen Regionen.

1.13 bestimmt den Weltmarkt-Zugang über Handelsknoten; Hafenstufen zählen dort stark (Vanilla-Defines
WORLD_MARKET_HUB_SCORE_PORT_FACTOR). Ohne Hafen hängt ein Küstenland nicht am Weltmarkt (Kono: Stormwind, Defias,
Gnomeregan). Regeln:
- Land hat create_state in mindestens einem Küsten-State (naval_exit_id) und nirgends einen Hafen.
- Land hat navigation (Tech-Stufe 1–5); Stufe 6/7 bekommt keinen Hafen, sonst Ladefehler.
- Hafen in der Hauptstadt, wenn sie an der Küste liegt, sonst im Küsten-State mit den meisten eigenen Pops.
- Stufe 1, je volle 5 Mio. Pops des Landes +1, höchstens 3. Länder unter MIN_POPS bekommen keinen.
Vorbild: Vanilla building_port (11_private_infrastructure.txt), pm_basic_port. Besitz: Land.
"""
import argparse
import logging
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.dont_write_bytecode = True  # kein __pycache__ im Repo
sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I nimmt das Skriptverzeichnis aus sys.path
from va_fill_buildings import entry, insert, without_tech
from va_region_overview import rows
from va_script import REPO

log = logging.getLogger("va_add_ports")

MIN_POPS = 100_000
POPS_PER_LEVEL = 5_000_000
MAX_LEVEL = 3


def capitals():
    """Land → Hauptstadt-State aus common/country_definitions."""
    caps = {}
    for f in sorted((REPO / "common/country_definitions").glob("*.txt")):
        try:
            text = f.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeDecodeError) as e:
            log.error("%s nicht lesbar: %s", f, e)
            continue
        for m in re.finditer(r"^(\w+)\s*=\s*\{(.*?)^\}", text, re.S | re.M):
            cap = re.search(r"capital\s*=\s*(STATE_\w+)", m.group(2))
            if cap:
                caps[m.group(1)] = cap.group(1)
    return caps


def plan(targets):
    """Land → (Präfix, State, Stufen); nur Küsten-States in den Regionen targets."""
    prefixes = sorted({f.name[:2] for f in (REPO / "map_data/state_regions").glob("[23]?_*.txt")})
    pops, has_port = Counter(), set()
    coastal = defaultdict(list)  # Land → [(eigene Pops, State, Präfix)]
    for p in prefixes:
        _, data = rows(p)
        for r in data:
            pops.update(r["owners"])
            if r["levels"].get("building_port"):
                has_port.update(r["owners"])
            if r["coastal"] and p in targets:
                for tag in r["created"]:
                    coastal[tag].append((r["owners"].get(tag, 0), r["state"], p))
    no_nav = without_tech("navigation")
    caps = capitals()
    result = {}
    for tag, states in coastal.items():
        if tag in has_port or pops[tag] < MIN_POPS:
            continue
        if tag in no_nav:
            log.info("%s: ohne navigation (Tech-Stufe 6/7), kein Hafen", tag)
            continue
        at_cap = [s for s in states if s[1] == caps.get(tag)]
        _, state, p = (at_cap or sorted(states, reverse=True))[0]
        result[tag] = (p, state, min(MAX_LEVEL, 1 + int(pops[tag] // POPS_PER_LEVEL)))
    return result, pops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prefixes", nargs="+")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    sys.stdout.reconfigure(encoding="utf-8")
    result, pops = plan(set(args.prefixes))
    print("| Land | Pops (Mio.) | State | Stufen |\n|---|---|---|---|")
    for tag, (p, state, lv) in sorted(result.items(), key=lambda kv: -pops[kv[0]]):
        print(f"| {tag} | {pops[tag] / 1e6:.2f} | {state} ({p}) | {lv} |")
    print(f"\n{len(result)} Häfen, {sum(lv for _, _, lv in result.values())} Stufen")
    if not args.apply:
        return 0
    by_file = defaultdict(list)
    for tag, (p, state, lv) in result.items():
        by_file[p].append((tag, state, lv))
    for p, items in sorted(by_file.items()):
        files = sorted((REPO / "common/history/buildings").glob(f"{p}_*.txt"))
        if len(files) != 1:
            log.error("erwarte genau eine Gebäude-History mit Präfix %s, gefunden %d", p, len(files))
            return 1
        target = files[0]
        try:
            raw = target.read_bytes()
            text = raw.decode("utf-8-sig")
        except (OSError, UnicodeDecodeError) as e:
            log.error("%s nicht lesbar: %s", target, e)
            return 1
        for tag, state, lv in items:
            text = insert(text, state, tag, entry("building_port", tag, lv))
        try:
            target.write_text(("﻿" if raw.startswith(b"\xef\xbb\xbf") else "") + text, encoding="utf-8", newline="")
            log.info("geschrieben: %s (%d Häfen)", target.relative_to(REPO), len(items))
        except OSError as e:
            log.error("%s nicht schreibbar: %s", target, e)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

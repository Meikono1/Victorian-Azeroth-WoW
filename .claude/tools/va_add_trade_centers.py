"""Start-Handelszentralen für handelsfähige Länder mit Hafen (VA-040, Weltmarkt).

Aufruf: python -I .claude/tools/va_add_trade_centers.py 21 22 23 24 25 26 27 28 [--apply]
  Präfixe der Regionen, deren Länder Handelszentralen bekommen. Pops und Häfen zählen aus allen Regionen.

1.13 handelt nur über building_trade_center (Vanilla 11_private_infrastructure.txt): Jede Stufe bringt
state_weekly_trades und state_trade_capacity, ohne Zentrale gibt es weder Import noch Export. Vanilla setzt sie in
der Gebäude-History (FRA 1836: 27 Stufen bei 34,6 Mio. Pops, GBR 60 bei 26 Mio.), der Mod hatte keine einzige.
Regeln:
- Land hat einen Hafen (Merchant Marine ist Input der Zentrale) und mindestens MIN_POPS.
- Kein Isolationismus (sperrt trade_center_construction_allowed). Ohne Handelsgesetz in der Länder-History setzt
  effect_starting_politics_traditional für decentralized Isolationismus, sonst Merkantilismus.
- Zentrale in der Hauptstadt, wenn das Land dort Pops hat, sonst im State mit den meisten eigenen Pops.
- Stufen: LEVELS_PER_MIO je Mio. Pops des Landes, mindestens 1, höchstens MAX_LEVEL.
- Länder mit vorhandener Zentrale werden übersprungen.
Besitz: Land. PMs wie Vanilla-History: pm_trade_center_trade_quantity_normal.
"""
import argparse
import logging
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.dont_write_bytecode = True  # kein __pycache__ im Repo
sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I nimmt das Skriptverzeichnis aus sys.path
from va_add_ports import capitals
from va_fill_buildings import block_end, entry, insert
from va_region_overview import building_levels, by_state, rows
from va_script import REPO

log = logging.getLogger("va_add_trade_centers")

BUILDING = "building_trade_center"
MIN_POPS = 100_000
LEVELS_PER_MIO = 1.0  # Vanilla FRA 0,78, PRU 1,07, SPA 1,01, GBR 2,31
MAX_LEVEL = 10
TRADE_LAW = re.compile(r"law_type:law_(isolationism|mercantilism|protectionism|free_trade)\b")


def country_types():
    """Land → country_type aus common/country_definitions."""
    types = {}
    for f in sorted((REPO / "common/country_definitions").glob("*.txt")):
        try:
            text = f.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeDecodeError) as e:
            log.error("%s nicht lesbar: %s", f, e)
            continue
        for m in re.finditer(r"^(\w+)\s*=\s*\{(.*?)^\}", text, re.S | re.M):
            t = re.search(r"country_type\s*=\s*(\w+)", m.group(2))
            if t:
                types[m.group(1)] = t.group(1)
    return types


def trade_laws():
    """Land → Handelsgesetz aus common/history/countries (letztes activate_law gewinnt), fehlt = kein Eintrag."""
    laws = {}
    for f in sorted((REPO / "common/history/countries").glob("*.txt")):
        try:
            text = f.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeDecodeError) as e:
            log.error("%s nicht lesbar: %s", f, e)
            continue
        for m in re.finditer(r"c:(\w+)\s*\??=\s*\{", text):
            end = block_end(text, m.end() - 1)
            if end < 0:
                log.error("%s: Block c:%s nicht geschlossen", f.name, m.group(1))
                continue
            found = TRADE_LAW.findall(text[m.end():end])
            if found:
                laws[m.group(1)] = found[-1]
    return laws


def can_trade(tag, laws, types):
    law = laws.get(tag)
    if law is None:
        law = "isolationism" if types.get(tag) == "decentralized" else "mercantilism"
    return law != "isolationism"


def plan(targets):
    """Land → (Präfix, State, Stufen) für Länder, deren Ziel-State in den Regionen targets liegt."""
    prefixes = sorted({f.name[:2] for f in (REPO / "map_data/state_regions").glob("[23]?_*.txt")})
    pops = Counter()
    own_states = defaultdict(list)  # Land → [(eigene Pops, State, Präfix)]
    for p in prefixes:
        _, data = rows(p)
        for r in data:
            pops.update(r["owners"])
            for tag, n in r["owners"].items():
                if tag in r["created"]:
                    own_states[tag].append((n, r["state"], p))
    has_port, has_center = set(), set()
    for st, by_tag in by_state("common/history/buildings", "BUILDINGS").items():
        for tag, block in by_tag.items():
            lv = building_levels(block)
            if lv.get("building_port"):
                has_port.add(tag)
            if lv.get(BUILDING):
                has_center.add(tag)
    laws, types, caps = trade_laws(), country_types(), capitals()
    result = {}
    for tag, states in own_states.items():
        if tag in has_center or tag not in has_port or pops[tag] < MIN_POPS:
            continue
        if not can_trade(tag, laws, types):
            log.info("%s: Isolationismus, keine Handelszentrale", tag)
            continue
        at_cap = [s for s in states if s[1] == caps.get(tag)]
        _, state, p = (at_cap or sorted(states, reverse=True))[0]
        if p not in targets:
            continue
        levels = max(1, min(MAX_LEVEL, round(pops[tag] / 1e6 * LEVELS_PER_MIO)))
        result[tag] = (p, state, levels)
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
    print(f"\n{len(result)} Handelszentralen, {sum(lv for _, _, lv in result.values())} Stufen")
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
            text = insert(text, state, tag, entry(BUILDING, tag, lv))
        try:
            target.write_text(("﻿" if raw.startswith(b"\xef\xbb\xbf") else "") + text, encoding="utf-8", newline="")
            log.info("geschrieben: %s (%d Handelszentralen)", target.relative_to(REPO), len(items))
        except OSError as e:
            log.error("%s nicht schreibbar: %s", target, e)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

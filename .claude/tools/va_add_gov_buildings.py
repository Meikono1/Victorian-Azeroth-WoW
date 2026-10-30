"""Start-Verwaltung und Bausektor für Länder ohne (VA-044, KI stapelt Verwaltung und Bausektoren).

Aufruf: python -I .claude/tools/va_add_gov_buildings.py 26 27 28 [--apply]
  Präfixe der Regionen, deren Länder Gebäude bekommen (Ziel-State liegt dort). Pops zählen aus allen Regionen.

Vanilla 1836 setzt beides in der Gebäude-History (FRA 50 Verwaltung / 7 Bausektor bei 34,6 Mio. Pops, PRU 20 / 7,
SPA 18 / 5, GBR 35 / 9). Im Mod hatten nur 13 Länder Verwaltung, Stormwind (15 Mio.) keine von beiden. Folge:
Bürokratie-Defizit und keine Baukapazität, die KI füllt die Bauliste mit genau diesen Gebäuden.
Regeln je Gebäude (siehe RULES):
- Land ist nicht decentralized, hat die Tech (Ära 1, Stufe 1–5) und mindestens min_pops.
- Land hat das Gebäude noch nirgends; vorhandene Stufen bleiben unangetastet.
- Gebäude in der Hauptstadt, wenn das Land dort Pops hat, sonst im State mit den meisten eigenen Pops.
- Stufen: per_mio je Mio. Pops, mindestens 1, höchstens max.
Vorbild: Vanilla building_government_administration (07_government.txt), building_construction_sector
(13_construction.txt), PMs wie Vanilla-History. Besitz: Land.
"""
import argparse
import logging
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.dont_write_bytecode = True  # kein __pycache__ im Repo
sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I nimmt das Skriptverzeichnis aus sys.path
from va_add_ports import capitals
from va_add_trade_centers import country_types
from va_fill_buildings import insert, without_tech
from va_region_overview import building_levels, by_state, rows
from va_script import REPO

log = logging.getLogger("va_add_gov_buildings")

# Vanilla 1836 je Mio. Pops: Verwaltung FRA 1,45, PRU 1,42, SPA 1,51, GBR 1,35; Bausektor FRA 0,2, PRU 0,5, GBR 0,35
RULES = {
    "building_government_administration": {
        "tech": "centralization", "per_mio": 1.4, "max": 25, "min_pops": 100_000,
        "pms": '"pm_horizontal_drawer_cabinets"',  # 50 Bürokratie je Stufe, braucht Papier; Gesetzes-PMs wählt das Spiel
    },
    "building_construction_sector": {
        "tech": "urbanization", "per_mio": 0.3, "max": 6, "min_pops": 1_000_000,
        "pms": '"pm_wooden_buildings"',
    },
}


def entry(b, tag, levels, pms):
    return (f'\t\t\tcreate_building={{\n\t\t\t\tbuilding="{b}"\n\t\t\t\tadd_ownership={{\n\t\t\t\t\tcountry={{\n'
            f'\t\t\t\t\t\tcountry="c:{tag}"\n\t\t\t\t\t\tlevels={levels}\n\t\t\t\t\t}}\n\t\t\t\t}}\n'
            f'\t\t\t\treserves=1\n\t\t\t\tactivate_production_methods={{ {pms} }}\n\t\t\t}}\n')


def plan(targets):
    """Liste (Gebäude, Land, Präfix, State, Stufen) für Länder, deren Ziel-State in den Regionen targets liegt."""
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
    has = defaultdict(set)  # Gebäude → Länder
    for by_tag in by_state("common/history/buildings", "BUILDINGS").values():
        for tag, block in by_tag.items():
            for b in building_levels(block):
                has[b].add(tag)
    types, caps = country_types(), capitals()
    result = []
    for b, rule in RULES.items():
        no_tech = without_tech(rule["tech"])
        for tag, states in sorted(own_states.items()):
            if tag in has[b] or pops[tag] < rule["min_pops"]:
                continue
            if types.get(tag) == "decentralized":
                continue
            if tag in no_tech:
                log.info("%s: ohne %s (Tech-Stufe 6/7), kein %s", tag, rule["tech"], b)
                continue
            at_cap = [s for s in states if s[1] == caps.get(tag)]
            _, state, p = (at_cap or sorted(states, reverse=True))[0]
            if p not in targets:
                continue
            levels = max(1, min(rule["max"], round(pops[tag] / 1e6 * rule["per_mio"])))
            result.append((b, tag, p, state, levels))
    return result, pops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prefixes", nargs="+")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    sys.stdout.reconfigure(encoding="utf-8")
    result, pops = plan(set(args.prefixes))
    print("| Gebäude | Land | Pops (Mio.) | State | Stufen |\n|---|---|---|---|---|")
    for b, tag, p, state, lv in sorted(result, key=lambda x: (x[0], -pops[x[1]])):
        print(f"| {b.replace('building_', '')} | {tag} | {pops[tag] / 1e6:.2f} | {state} ({p}) | {lv} |")
    for b in RULES:
        mine = [x for x in result if x[0] == b]
        print(f"{b}: {len(mine)} Länder, {sum(x[4] for x in mine)} Stufen")
    if not args.apply:
        return 0
    by_file = defaultdict(list)
    for b, tag, p, state, lv in result:
        by_file[p].append((b, tag, state, lv))
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
        for b, tag, state, lv in items:
            text = insert(text, state, tag, entry(b, tag, lv, RULES[b]["pms"]))
        try:
            target.write_text(("﻿" if raw.startswith(b"\xef\xbb\xbf") else "") + text, encoding="utf-8", newline="")
            log.info("geschrieben: %s (%d Gebäude)", target.relative_to(REPO), len(items))
        except OSError as e:
            log.error("%s nicht schreibbar: %s", target, e)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

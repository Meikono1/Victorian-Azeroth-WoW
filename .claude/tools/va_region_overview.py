"""Übersicht einer Kartenregion je State: Besitzer, Pops, Kulturen, Ackerland, Ressourcen, Start-Gebäude (VA-029).

Aufruf: python -I .claude/tools/va_region_overview.py 27 [--md DATEI]
  27        Präfix der Datei in map_data/state_regions/ (z. B. 27_va_center_eastern_kingdoms.txt)
  --md      Tabelle zusätzlich als Markdown-Datei schreiben

Grundlage für das Setzen von Ressourcen und Gebäuden Region für Region. Nur lesend.
"""
import argparse
import logging
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.dont_write_bytecode = True  # kein __pycache__ im Repo
sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I nimmt das Skriptverzeichnis aus sys.path
from va_script import REPO, effective_files, get, get_all, parse_file, values

log = logging.getLogger("va_region_overview")

FOOD = ("farm", "ranch", "fishing", "whaling", "orchard", "plantation", "food_industry")
SUBSISTENCE_PEASANTS = 5000  # building_employment_peasants_add je Stufe, Vanilla 12_subsistence


def state_key(k):
    return k.split(":", 1)[-1] if k else k


def load_region(prefix):
    files = sorted((REPO / "map_data/state_regions").glob(f"{prefix}_*.txt"))
    if not files:
        log.error("keine State-Region-Datei mit Präfix %s", prefix)
        return None, {}
    regions = {}
    for k, _, v in parse_file(files[0]):
        if k and isinstance(v, list):
            capped = get(v, "capped_resources") or []
            regions[k] = {
                "arable": int(get(v, "arable_land", "0") or 0),
                "arable_res": values(get(v, "arable_resources")),
                "capped": {ck: cv for ck, _, cv in capped if ck},
                "subsistence": get(v, "subsistence_building", "-"),
                "coastal": get(v, "naval_exit_id") is not None,
            }
    return files[0].name, regions


def by_state(folder, top):
    """s:STATE → {Land: Block} aus History-Dateien (POPS/BUILDINGS)."""
    result = defaultdict(dict)
    for f in sorted((REPO / folder).glob("*.txt")):
        root = get(parse_file(f), top) or []
        for sk, _, sv in root:
            if not isinstance(sv, list):
                continue
            for ck, _, cv in sv:
                if ck and ck.startswith("region_state:") and isinstance(cv, list):
                    result[state_key(sk)].setdefault(ck.split(":", 1)[1], []).extend(cv)
    return result


def state_owners():
    """s:STATE → Länder mit create_state (nur diese können Gebäude besitzen)."""
    owners = defaultdict(set)
    for f in effective_files("common/history/states"):
        root = get(parse_file(f), "STATES") or []
        for sk, _, sv in root:
            if isinstance(sv, list):
                for cs in get_all(sv, "create_state"):
                    owners[state_key(sk)].add((get(cs, "country") or "").split(":", 1)[-1])
    return owners


def building_levels(block):
    """Gebäude → Summe der Stufen (aus add_ownership bzw. level)."""
    levels = Counter()
    for cb in get_all(block, "create_building"):
        name = get(cb, "building", "?")
        total = 0
        own = get(cb, "add_ownership") or []
        for _, _, ov in own:
            if isinstance(ov, list):
                total += int(get(ov, "levels", "0") or 0)
        total = total or int(get(cb, "level", "0") or 0)
        levels[name] += total
    return levels


def rows(prefix):
    fname, regions = load_region(prefix)
    if fname is None:
        return None, []
    pops, blds = by_state("common/history/pops", "POPS"), by_state("common/history/buildings", "BUILDINGS")
    created = state_owners()
    out = []
    for st, info in regions.items():
        owners = Counter()
        cultures = Counter()
        for tag, block in pops.get(st, {}).items():
            for cp in get_all(block, "create_pop"):
                size = int(get(cp, "size", "0") or 0)
                owners[tag] += size
                cultures[get(cp, "culture", "?")] += size
        levels = Counter()
        for block in blds.get(st, {}).values():
            levels += building_levels(block)
        out.append({
            "state": st, "owners": owners, "pops": sum(owners.values()), "cultures": cultures,
            "levels": levels, "created": created.get(st, set()), **info,
        })
    return fname, out


def short(name):
    return name.replace("building_", "").replace("bg_", "")


def render(fname, data):
    lines = [f"# Regionsübersicht {fname}", ""]
    tp = sum(r["pops"] for r in data)
    ta = sum(r["arable"] for r in data)
    food = sum(v for r in data for k, v in r["levels"].items() if any(f in k for f in FOOD))
    allv = sum(sum(r["levels"].values()) for r in data)
    empty = sum(1 for r in data if r["pops"] and not r["levels"])
    lines.append(f"States {len(data)}, Pops {tp / 1e6:.1f} Mio., Ackerland {ta}, Gebäudestufen {allv} "
                 f"(davon Nahrung {food}), States mit Pops ohne Gebäude: {empty}.")
    lines.append(f"Subsistenz trägt grob {SUBSISTENCE_PEASANTS} Bauern je Ackerland-Stufe; Pops je Ackerland-Stufe: "
                 f"{tp / max(ta, 1):,.0f}.")
    lines += ["", "| State | Besitzer | Pops (Tsd.) | Kulturen | Acker | Acker-Ressourcen | Gedeckelte Ressourcen | Gebäude |",
              "|---|---|---|---|---|---|---|---|"]
    for r in sorted(data, key=lambda r: -r["pops"]):
        owners = ", ".join(t for t, _ in r["owners"].most_common())
        cult = ", ".join(c for c, _ in r["cultures"].most_common(2))
        ares = " ".join(short(a) for a in r["arable_res"])
        cap = " ".join(f"{short(k)} {v}" for k, v in r["capped"].items())
        bld = " ".join(f"{short(k)} {v}" for k, v in r["levels"].most_common()) or "–"
        lines.append(f"| {short(r['state'].replace('STATE_', ''))} | {owners} | {r['pops'] / 1e3:,.0f} | {cult} | "
                     f"{r['arable']} | {ares} | {cap} | {bld} |")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prefix")
    ap.add_argument("--md")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    sys.stdout.reconfigure(encoding="utf-8")
    fname, data = rows(args.prefix)
    if fname is None:
        return 1
    text = render(fname, data)
    print(text)
    if args.md:
        try:
            Path(args.md).write_text(text + "\n", encoding="utf-8")
            log.info("geschrieben: %s", args.md)
        except OSError as e:
            log.error("%s nicht schreibbar: %s", args.md, e)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

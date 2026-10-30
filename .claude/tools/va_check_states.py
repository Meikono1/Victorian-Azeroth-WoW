"""Prüft eine Kartenregion (State-Region-Datei) gegen Karte, History, Pops, Gebäude, Länder.

Aufruf: python -I .claude/tools/va_check_states.py 26 [--no-png] [--assign-test]
  26            Präfix der Datei in map_data/state_regions/ (z. B. 26_va_north_eastern_kingdoms.txt)
  --no-png      provinces.png nicht laden (schneller, ohne Existenz-/Nachbarschaftsprüfung)
  --assign-test Für Provinzen aus STATE_TEST den Nachbar-State mit der längsten Grenze vorschlagen
"""
import argparse
import logging
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.dont_write_bytecode = True  # kein __pycache__ im Repo
sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I nimmt das Skriptverzeichnis aus sys.path
from va_script import REPO, effective_files, get, get_all, parse_file, top_level_keys, values

log = logging.getLogger("va_check_states")
HUBS = ("city", "farm", "mine", "wood", "port")


class Report:
    def __init__(self):
        self.items = defaultdict(list)

    def add(self, topic, text):
        self.items[topic].append(text)

    def print(self):
        for topic, lines in self.items.items():
            print(f"\n## {topic} ({len(lines)})")
            for line in lines:
                print(f"- {line}")


def load_regions():
    """Alle State Regions: name -> Block, plus Provinz -> [States]."""
    regions, owner, files = {}, defaultdict(list), {}
    for f in sorted((REPO / "map_data/state_regions").glob("*.txt")):
        for k, _, v in parse_file(f):
            if k and isinstance(v, list):
                regions[k] = v
                files[k] = f.name
                for p in values(get(v, "provinces")):
                    owner[p.upper()].append(k)
    return regions, owner, files


def load_png():
    try:
        import numpy as np
        from PIL import Image
    except ImportError as e:
        log.error("numpy/PIL fehlen, Kartenprüfung entfällt: %s", e)
        return None, None
    img = np.asarray(Image.open(REPO / "map_data/provinces.png").convert("RGB")).astype(np.int32)
    ids = (img[..., 0] << 16) | (img[..., 1] << 8) | img[..., 2]
    return ids, np


def neighbours(ids, np, colors):
    """Grenzlänge zwischen Provinzpaaren, nur für Provinzen aus `colors`."""
    wanted = np.array(sorted(colors), dtype=np.int32)
    out = defaultdict(Counter)
    for a, b in ((ids[:, :-1], ids[:, 1:]), (ids[:-1, :], ids[1:, :])):
        diff = a != b
        pa, pb = a[diff], b[diff]
        for x, y in ((pa, pb), (pb, pa)):
            m = np.isin(x, wanted)
            pairs, counts = np.unique(np.stack([x[m], y[m]]), axis=1, return_counts=True)
            for (p, q), c in zip(pairs.T, counts):
                out[int(p)][int(q)] += int(c)
    return out


def hexid(p):
    return int(p[1:], 16)


def resource_buildings(region):
    """Gebäude/Gruppen, die ein State erlaubt, mit Obergrenze (None = unbegrenzt)."""
    res = {b: None for b in values(get(region, "arable_resources"))}
    for k, _, v in get(region, "capped_resources") or []:
        if k:
            res[k] = int(v)
    for r in get_all(region, "resource"):
        for key in ("type", "depleted_type"):
            t = get(r, key)
            if t:
                amount = get(r, "discovered_amount") or get(r, "undiscovered_amount") or 0
                res[t] = res.get(t) or 0
                res[t] += int(amount)
    return res


def check_regions(names, regions, prov_owner, rep, png_ids, buildings, seas):
    for name in names:
        r = regions[name]
        provs = [p.upper() for p in values(get(r, "provinces"))]
        if not provs:
            rep.add("State Regions", f"{name}: keine Provinzen")
            continue
        for p, c in Counter(provs).items():
            if c > 1:
                rep.add("State Regions", f"{name}: Provinz {p} {c}× gelistet")
        for p in provs:
            others = [s for s in prov_owner[p] if s != name]
            if others:
                rep.add("State Regions", f"{name}: Provinz {p} auch in {', '.join(sorted(set(others)))}")
            if png_ids is not None and hexid(p) not in png_ids:
                rep.add("State Regions", f"{name}: Provinz {p} gibt es in provinces.png nicht")
        for p in values(get(r, "impassable")):
            if p.upper() not in provs:
                rep.add("State Regions", f"{name}: impassable {p} gehört nicht zum State")
        for hub in HUBS:
            p = (get(r, hub) or "").upper()
            if not p:
                if hub != "port":
                    rep.add("Hubs", f"{name}: {hub}-Hub fehlt")
            elif p not in provs:
                where = ", ".join(prov_owner.get(p, [])) or ("nirgends" if png_ids is None or hexid(p) in png_ids else "nicht auf der Karte")
                rep.add("Hubs", f"{name}: {hub}-Hub {p} liegt in {where}")
        exit_id = get(r, "naval_exit_id")
        if get(r, "port") and not exit_id:
            rep.add("Hubs", f"{name}: Port-Hub ohne naval_exit_id")
        if exit_id and exit_id not in seas:
            rep.add("Hubs", f"{name}: naval_exit_id {exit_id} ist keine Seeregion")
        sub = get(r, "subsistence_building")
        if sub not in buildings:
            rep.add("Ressourcen", f"{name}: subsistence_building {sub} unbekannt")
        for b in resource_buildings(r):
            if not b.startswith("building_"):
                rep.add("Ressourcen", f"{name}: {b} ist kein Gebäudename (1.13-Format: building_…)")
            elif b not in buildings:
                rep.add("Ressourcen", f"{name}: {b} unbekannt")


def state_blocks(path):
    """s:STATE_X-Blöcke einer History-Datei (unter dem Wurzelblock STATES/POPS/BUILDINGS)."""
    out = defaultdict(list)
    for k, _, root in parse_file(path):
        if not isinstance(root, list):
            continue
        for sk, _, sv in root:
            if sk and sk.startswith("s:") and isinstance(sv, list):
                out[sk[2:]].append(sv)
    return out


def region_states(blocks):
    """(State, Land) -> Block für region_state:TAG."""
    out = {}
    for state, lst in blocks.items():
        for b in lst:
            for k, _, v in b:
                if k and k.startswith("region_state:") and isinstance(v, list):
                    out[(state, k.split(":", 1)[1])] = v
    return out


def check_history(names, regions, rep, countries, cultures):
    """create_state-Besitz. Gibt (State, Land) -> Provinzen zurück."""
    hist = defaultdict(list)
    for f in effective_files("common/history/states"):
        for s, lst in state_blocks(f).items():
            hist[s] += lst
    owned = {}
    for name in names:
        provs = {p.upper() for p in values(get(regions[name], "provinces"))}
        if name not in hist:
            rep.add("State-History", f"{name}: kein Eintrag (State ist unbesiedelt)")
            continue
        seen = {}
        for block in hist[name]:
            for cs in get_all(block, "create_state"):
                tag = (get(cs, "country") or "?").split(":", 1)[-1]
                if tag not in countries:
                    rep.add("State-History", f"{name}: Land {tag} nicht definiert")
                mine = [p.upper().strip('"') for p in values(get(cs, "owned_provinces"))]
                if not mine:
                    rep.add("State-History", f"{name}/{tag}: leeres owned_provinces")
                for p in mine:
                    if p not in provs:
                        rep.add("State-History", f"{name}/{tag}: {p} gehört nicht zur State Region")
                    if p in seen and seen[p] != tag:
                        rep.add("State-History", f"{name}: {p} doppelt vergeben ({seen[p]} und {tag})")
                    seen[p] = tag
                owned.setdefault((name, tag), set()).update(mine)
            for hl in get_all(block, "add_homeland"):
                if hl.split(":", 1)[-1] not in cultures:
                    rep.add("State-History", f"{name}: Homeland-Kultur {hl} unbekannt")
        free = provs - set(seen)
        if free and seen:
            rep.add("State-History", f"{name}: {len(free)} von {len(provs)} Provinzen ohne Besitzer")
    return owned


def check_pops(names, owned, rep, cultures, religions):
    pops = {}
    for f in effective_files("common/history/pops"):
        pops.update(region_states(state_blocks(f)))
    for key in owned:
        if key not in pops:
            rep.add("Pops", f"{key[0]}/{key[1]}: keine Pops")
    for (state, tag), block in pops.items():
        if state not in names:
            continue
        if (state, tag) not in owned:
            rep.add("Pops", f"{state}/{tag}: Pops ohne create_state")
        total = 0
        for cp in get_all(block, "create_pop"):
            total += int(get(cp, "size") or 0)
            cu, rel = get(cp, "culture"), get(cp, "religion")
            if cu not in cultures:
                rep.add("Pops", f"{state}/{tag}: Kultur {cu} unbekannt")
            if rel and rel not in religions:
                rep.add("Pops", f"{state}/{tag}: Religion {rel} unbekannt")
        if total == 0:
            rep.add("Pops", f"{state}/{tag}: Größe 0")
    return pops


def pm_index():
    pmgs = top_level_keys("common/production_method_groups")
    return {g: set(values(get(b, "production_methods"))) for g, b in pmgs.items()}, set(top_level_keys("common/production_methods"))


def check_buildings(names, owned, regions, rep, buildings, countries):
    pmg_pms, all_pms = pm_index()
    hist = {}
    for f in effective_files("common/history/buildings"):
        hist.update(region_states(state_blocks(f)))
    usage = defaultdict(Counter)
    for (state, tag), block in hist.items():
        if state not in names:
            continue
        if (state, tag) not in owned:
            rep.add("Gebäude", f"{state}/{tag}: Gebäude ohne create_state")
        for cb in get_all(block, "create_building"):
            b = get(cb, "building")
            if b not in buildings:
                rep.add("Gebäude", f"{state}/{tag}: Gebäude {b} unbekannt")
                continue
            allowed = set()
            for g in values(get(buildings[b], "production_method_groups")):
                allowed |= pmg_pms.get(g, set())
            for pm in values(get(cb, "activate_production_methods")):
                if pm not in all_pms:
                    rep.add("Gebäude", f"{state}/{tag}: {b}: PM {pm} unbekannt")
                elif pm not in allowed:
                    rep.add("Gebäude", f"{state}/{tag}: {b}: PM {pm} gehört nicht zum Gebäude")
            levels = 0
            for own in get_all(cb, "add_ownership"):
                for kind, _, o in own:
                    if not isinstance(o, list):
                        continue
                    c = (get(o, "country") or "").split(":", 1)[-1]
                    if c and c not in countries:
                        rep.add("Gebäude", f"{state}/{tag}: {b}: Eigentümer {c} nicht definiert")
                    reg = get(o, "region")
                    if reg and reg not in regions:
                        rep.add("Gebäude", f"{state}/{tag}: {b}: Region {reg} unbekannt")
                    levels += int(get(o, "levels") or 0)
            usage[state][b] += levels or int(get(cb, "level") or 0)
    for state in names:
        res = resource_buildings(regions[state])
        group_of = {}
        for b in usage[state]:
            group_of[b] = get(buildings.get(b, []), "building_group")
        for b, lv in usage[state].items():
            if b in res or group_of[b] in res:
                cap = res.get(b, res.get(group_of[b]))
                if cap is not None and lv > cap:
                    rep.add("Ressourcen", f"{state}: {b} Stufe {lv} > Obergrenze {cap}")
            elif needs_resource(b, buildings):
                rep.add("Ressourcen", f"{state}: {b} ({lv}) ohne passende Ressource im State")
        if not usage[state] and any(k[0] == state for k in owned):
            rep.add("Gebäude", f"{state}: keine Start-Gebäude")


def needs_resource(b, buildings):
    grp = get(buildings.get(b, []), "building_group") or ""
    return any(x in b or x in grp for x in ("farm", "mine", "plantation", "ranch", "logging", "fishing", "whaling", "rig", "oil", "rubber", "mining"))


def check_countries(owned, regions, rep, countries, templates):
    tags = sorted({t for _, t in owned})
    hist = {}
    for f in effective_files("common/history/countries"):
        for _, _, root in parse_file(f):
            if isinstance(root, list):
                for k, _, v in root:
                    if k and k.startswith("c:"):
                        hist[k[2:]] = v
    chars = defaultdict(list)
    for f in effective_files("common/history/characters"):
        for _, _, root in parse_file(f):
            if isinstance(root, list):
                for k, _, v in root:
                    if k and k.startswith("c:") and isinstance(v, list):
                        for cc in get_all(v, "create_character"):
                            chars[k[2:]].append(cc)
    # Hauptstädte können außerhalb der geprüften Region liegen: Besitz weltweit
    world = defaultdict(set)
    for f in effective_files("common/history/states"):
        for s, lst in state_blocks(f).items():
            for block in lst:
                for cs in get_all(block, "create_state"):
                    world[s].add((get(cs, "country") or "").split(":", 1)[-1])
    for tag in tags:
        d = countries.get(tag)
        if d is None:
            continue
        cap = get(d, "capital")
        if not cap:
            rep.add("Länder", f"{tag}: keine Hauptstadt")
        elif tag not in world.get(cap, ()):
            holders = sorted(world.get(cap, ()))
            rep.add("Länder", f"{tag}: Hauptstadt {cap} gehört nicht dem Land ({', '.join(holders) or 'niemand'})")
        if tag not in hist:
            rep.add("Länder", f"{tag}: kein Eintrag in history/countries")
        ruler = False
        for cc in chars.get(tag, []):
            t = get(cc, "template")
            block = templates.get(t, cc) if t else cc
            if t and t not in templates:
                rep.add("Charaktere", f"{tag}: Template {t} unbekannt")
            if get(block, "ruler") == "yes":
                ruler = True
        if not ruler:
            rep.add("Charaktere", f"{tag}: kein historischer Herrscher ({len(chars.get(tag, []))} Charaktere)")
        states = sorted(s for s, t in owned if t == tag)
        rep.add("Länder-Übersicht", f"{tag} [{get(d, 'tier')}, {' '.join(values(get(d, 'cultures')))}]: {len(states)} States")


def assign_test(regions, png, np, rep, focus):
    ids, = png
    test = {hexid(p.upper()) for p in values(get(regions.get("STATE_TEST", []), "provinces"))}
    if not test:
        return
    state_of = {}
    for s, r in regions.items():
        if s != "STATE_TEST":
            for p in values(get(r, "provinces")):
                state_of[hexid(p.upper())] = s
    nb = neighbours(ids, np, test)
    hits = Counter()
    for p in sorted(test):
        border = Counter()
        for q, c in nb[p].items():
            if q in state_of:
                border[state_of[q]] += c
        best = border.most_common(1)[0][0] if border else "?"
        hits[best] += 1
        if best in focus:
            rep.add("STATE_TEST", f"x{p:06X} → {best} ({dict(border.most_common(3))})")
    rep.add("STATE_TEST", "Verteilung gesamt: " + ", ".join(f"{s} {c}" for s, c in hits.most_common()))


def main():
    sys.stdout.reconfigure(encoding="utf-8")  # -I ignoriert PYTHONIOENCODING
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    ap = argparse.ArgumentParser()
    ap.add_argument("prefix")
    ap.add_argument("--no-png", action="store_true")
    ap.add_argument("--assign-test", action="store_true")
    a = ap.parse_args()

    regions, prov_owner, files = load_regions()
    names = [s for s, f in files.items() if f.startswith(a.prefix + "_")]
    if not names:
        log.error("Keine State-Region-Datei mit Präfix %s", a.prefix)
        return
    log.info("%d States in %s", len(names), files[names[0]])
    seas = {get(r, "id") for s, r in regions.items() if files[s].startswith("80_")}
    buildings = top_level_keys("common/buildings")
    countries = top_level_keys("common/country_definitions")
    cultures = top_level_keys("common/cultures")
    religions = top_level_keys("common/religions")
    templates = top_level_keys("common/character_templates")

    ids = np = None
    if not a.no_png:
        ids, np = load_png()
    png_ids = set(np.unique(ids).tolist()) if ids is not None else None

    rep = Report()
    check_regions(names, regions, prov_owner, rep, png_ids, buildings, seas)
    owned = check_history(names, regions, rep, countries, cultures)
    check_pops(names, owned, rep, cultures, religions)
    check_buildings(names, owned, regions, rep, buildings, countries)
    check_countries(owned, regions, rep, countries, templates)
    if a.assign_test and ids is not None:
        assign_test(regions, (ids,), np, rep, set(names))
    rep.print()


if __name__ == "__main__":
    main()

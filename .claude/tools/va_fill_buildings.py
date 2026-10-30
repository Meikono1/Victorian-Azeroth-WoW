"""Start-Gebäude einer Region grob auffüllen: Nahrung, Rohstoffe, Plantagen (VA-029).

Aufruf: python -I .claude/tools/va_fill_buildings.py 26 [--trim GEBÄUDE] [--apply]
  26        Präfix der Region (map_data/state_regions/26_*.txt, common/history/buildings/26_*.txt)
  --trim    statt auffüllen: diese Gebäudeart (z. B. building_iron_mine, oder fish) auf RATES kürzen; das letzte
            Gebäude dieses Typs eines Landes bleibt, auf 0 gekürzte Einträge werden entfernt
  --apply   Änderungen in die Gebäude-History schreiben; ohne Option nur Probelauf

Maßstab: Vanilla-Frankreich 1836 (Kono: nicht zu viele Ressourcen am Start), Stufen je Mio. Pops, siehe RATES.
Je Gebäudeart bekommt die Region RATES × Pops Stufen. Vorhandene Stufen der ganzen Region werden angerechnet,
also gibt es nur dort Neues, wo die Region insgesamt unter dem Maßstab liegt. Verteilt wird auf die States mit
dem größten eigenen Rückstand. Grenzen: Farmen, Ranches, Plantagen zusammen höchstens arable_land; gedeckelte
Ressourcen höchstens bis zum Deckel. Mehrere Besitzer teilen nach Pop-Anteil mal Länderfaktor.
Länder- und Kulturprofile (va_profiles.py) skalieren den Maßstab je State: mächtige Reiche bekommen mehr,
Lore verschiebt die Gewichte (Zwerge Minen, Goblins Fisch und Handel).
Nur Gebäude, deren Name sich mit 1.13 nicht ändert (gültig vor und nach VA-003). Besitz: Land.
"""
import argparse
import logging
import re
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True  # kein __pycache__ im Repo
sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I nimmt das Skriptverzeichnis aus sys.path
from va_profiles import country_factor, culture_factor, state_factor
from va_region_overview import rows
from va_script import REPO

log = logging.getLogger("va_fill_buildings")

# Vanilla 1.13, FRA 1836 (34,6 Mio. Pops), Stufen je Mio. Pops. Wein (2,26) fehlt: Name ändert sich mit 1.13.
RATES = {
	"grain": 2.75,
	"building_livestock_ranch": 0.75,
	"fish": 0.46,  # Fischerei und Walfang
	"plantation": 0.8,  # Seide 0,52, Zucker 0,14, Kaffee/Tabak/Färbepflanzen je < 0,1
	"building_logging_camp": 0.93,
	"building_coal_mine": 0.38,
	"building_iron_mine": 0.17,
	"building_sulfur_mine": 0.12,
	"building_lead_mine": 0.09,
}
MIN_POPS = 100_000  # darunter Platzhalter-States, nichts setzen
# Minen (Kohle, Eisen, Blei, Schwefel) brauchen shaft_mining, Häfen navigation (beide Ära 1). Vanilla-Tech-Stufe
# 6 und 7 haben Ära 1 nicht (00_starting_inventions.txt). Sonst Fehler „must have invented …“ wie bei Deathholme.
NEEDS_SHAFT_MINING = ("building_coal_mine", "building_iron_mine", "building_lead_mine", "building_sulfur_mine")


def without_tech(tech="shaft_mining"):
    """Länder ohne diese Ära-1-Tech laut common/history/countries (Stufe 6/7 oder gar keine, ohne eigene Freigabe)."""
    tags = set()
    for f in sorted((REPO / "common/history/countries").glob("*.txt")):
        try:
            text = f.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeDecodeError) as e:
            log.error("%s nicht lesbar: %s", f, e)
            continue
        for m in re.finditer(r"c:(\w+)\s*\??=\s*\{", text):
            body = text[m.end():block_end(text, m.end() - 1)]
            tier = re.search(r"effect_starting_technology_tier_(\d)_tech", body)
            if (not tier or int(tier.group(1)) >= 6) and tech not in body:
                tags.add(m.group(1))
    return tags

GRAIN = ("building_wheat_farm", "building_rye_farm", "building_maize_farm", "building_millet_farm",
         "building_rice_farm")
PLANTATIONS_OK = ("cotton", "dye", "silk", "tea", "tobacco", "sugar", "coffee", "opium", "banana")
PMS = {
    "farm": '"pm_simple_farming" "pm_no_secondary" "pm_tools_disabled"',
    "building_rice_farm": '"pm_simple_farming_building_rice_farm" "pm_no_secondary" "pm_tools_disabled"',
    "building_livestock_ranch": '"pm_open_air_stockyards" "pm_simple_ranch" "pm_standard_fences" "pm_unrefrigerated"',
    "building_fishing_wharf": '"pm_simple_fishing" "pm_unrefrigerated"',
    "building_port": '"pm_basic_port"',
    "building_whaling_station": '"pm_simple_whaling" "pm_unrefrigerated"',
    "building_logging_camp": '"pm_simple_forestry" "pm_no_hardwood" "pm_no_equipment" "pm_road_carts"',
    "mine": '"pm_picks_and_shovels_{b}" "pm_no_explosives" "pm_no_steam_automation" "pm_road_carts"',
    "plantation": '"default_{b}" "pm_road_carts"',
}
AGRO = GRAIN + ("building_livestock_ranch",)
ARABLE_KINDS = ("grain", "building_livestock_ranch", "plantation")


def pms_for(b):
    if b in PMS:
        return PMS[b]
    if b in GRAIN:
        return PMS["farm"]
    if b.endswith("_mine"):
        return PMS["mine"].format(b=b)
    return PMS["plantation"].format(b=b)


def split(total, weights):
    """Ganzzahlige Aufteilung von total nach Gewichten (größter Rest)."""
    s = sum(weights.values())
    if total <= 0 or s <= 0:
        return Counter()
    raw = {k: total * w / s for k, w in weights.items()}
    out = Counter({k: int(v) for k, v in raw.items()})
    for k in sorted(raw, key=lambda k: raw[k] - out[k], reverse=True)[:total - sum(out.values())]:
        out[k] += 1
    return +out


BG_SPECIAL = {"bg_logging": "building_logging_camp", "bg_fishing": "building_fishing_wharf",
              "bg_whaling": "building_whaling_station"}


def building_name(res):
    """Ressource → Gebäude. State Regions nutzen teils Gebäudenamen (1.13), teils noch bg_-Gruppen."""
    if res.startswith("building_"):
        return res
    if res in BG_SPECIAL:
        return BG_SPECIAL[res]
    name = "building_" + res[3:]
    for old, new in (("_mining", "_mine"), ("_farms", "_farm"), ("_ranches", "_ranch"), ("_plantations", "_plantation")):
        if name.endswith(old):
            return name[: -len(old)] + new
    return name


def kinds(r):
    """Gebäudeart → konkretes Gebäude für diesen State (None, wenn die Ressource fehlt)."""
    arable_res = [building_name(a) for a in r["arable_res"]]
    plant = next((a for a in arable_res if a.endswith("_plantation") and a.split("_")[1] in PLANTATIONS_OK), None)
    return {
        "grain": next((a for a in arable_res if a in GRAIN), None),
        "building_livestock_ranch": "building_livestock_ranch" if "building_livestock_ranch" in arable_res else None,
        "plantation": plant,
    }


def have_of(r, kind):
    lv = r["levels"]
    if kind == "grain":
        return sum(v for k, v in lv.items() if k in GRAIN)
    if kind == "fish":
        return lv["building_fishing_wharf"] + lv["building_whaling_station"]
    if kind == "plantation":
        return sum(v for k, v in lv.items() if "plantation" in k)
    return lv[kind]


def room_of(r, kind, cap, arable_free):
    lv = r["levels"]
    if kind in ARABLE_KINDS:
        return max(0, arable_free) if kinds(r)[kind] else 0
    if kind == "fish":
        if not r["coastal"]:  # Fischerei braucht Küste; Platzhalter-Deckel im Binnenland ignorieren
            return 0
        return sum(max(0, cap.get(b, 0) - lv[b]) for b in ("building_fishing_wharf", "building_whaling_station"))
    return max(0, cap.get(kind, 0) - lv[kind])


def alloc_units(budget, want, room):
    """budget Stufen einzeln an die (State, Land)-Einheit mit dem größten Rückstand want vergeben.

    room ist je State gedeckelt und wird von allen Ländern im State geteilt. Einzeln statt per Rundung, damit
    kleine Mitbesitzer nicht bei jedem State den Rest verlieren.
    """
    out, used = Counter(), Counter()
    for _ in range(max(0, budget)):
        options = [u for u in want if room.get(u[0], 0) > used[u[0]]]
        if not options:
            break
        u = max(options, key=lambda u: (want[u] - out[u], want[u]))
        out[u] += 1
        used[u[0]] += 1
    return +out


def plan_region(data):
    """State → Land → Counter(Gebäude → zusätzliche Stufen).

    Nur Länder mit create_state im State bekommen etwas (sonst schlägt das Gebäude beim Laden fehl).
    """
    states = {r["state"]: r for r in data if r["pops"] >= MIN_POPS}
    owners = {}
    for st, r in states.items():
        owners[st] = {tag: n for tag, n in r["owners"].items() if tag in r["created"]}
        if not owners[st]:
            log.warning("%s: kein Pop-Besitzer mit create_state, nichts gesetzt", st)
    plans = {st: {tag: Counter() for tag in owners[st]} for st in states}
    caps = {st: {building_name(k): int(v) for k, v in r["capped"].items() if str(v).isdigit()} for st, r in states.items()}
    arable_free = {st: r["arable"] - sum(v for k, v in r["levels"].items() if k in AGRO or "plantation" in k)
                   for st, r in states.items()}
    no_mines = without_tech("shaft_mining")
    for kind, rate in RATES.items():
        target, want, room = 0.0, {}, {}
        for st, r in states.items():
            total = sum(owners[st].values())
            for tag, n in owners[st].items():
                if kind in NEEDS_SHAFT_MINING and tag in no_mines:
                    continue
                t = rate * country_factor(tag, kind) * culture_factor(r, kind) * n / 1e6
                target += t
                want[(st, tag)] = t - have_of(r, kind) * n / total  # vorhandene Stufen nach Pop-Anteil
            room[st] = room_of(r, kind, caps[st], arable_free[st])
        budget = round(target) - sum(have_of(r, kind) for r in states.values())
        for (st, tag), n in alloc_units(budget, want, room).items():
            r, plan = states[st], plans[st][tag]
            if kind in ARABLE_KINDS:
                plan[kinds(r)[kind]] += n
                arable_free[st] -= n
            elif kind == "fish":
                done = sum(p["building_fishing_wharf"] for p in plans[st].values())
                free = max(0, caps[st].get("building_fishing_wharf", 0) - r["levels"]["building_fishing_wharf"] - done)
                plan["building_fishing_wharf"] += min(n, free)
                plan["building_whaling_station"] += n - min(n, free)
            else:
                plan[kind] += n
    return {st: {tag: +p for tag, p in by_tag.items() if +p} for st, by_tag in plans.items()
            if any(+p for p in by_tag.values())}


def entry(b, tag, levels):
    return (f'\t\t\tcreate_building={{\n\t\t\t\tbuilding="{b}"\n\t\t\t\tadd_ownership={{\n\t\t\t\t\tcountry={{\n'
            f'\t\t\t\t\t\tcountry="c:{tag}"\n\t\t\t\t\t\tlevels={levels}\n\t\t\t\t\t}}\n\t\t\t\t}}\n'
            f'\t\t\t\treserves=1\n\t\t\t\tactivate_production_methods={{ {pms_for(b)} }}\n\t\t\t}}\n')


def block_end(text, start):
    """Index der schließenden Klammer zum '{' an start."""
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return i
    return -1


def insert(text, state, tag, body):
    m = re.search(rf"s:{state}\s*=\s*\{{", text)
    if not m:
        root = re.search(r"BUILDINGS\s*=\s*\{", text)
        end = block_end(text, root.end() - 1)
        new = f"\ts:{state}={{\n\t\tregion_state:{tag}={{\n{body}\t\t}}\n\t}}\n"
        return text[:end] + new + text[end:]
    s_end = block_end(text, m.end() - 1)
    t = re.compile(rf"region_state:{tag}\s*=\s*\{{").search(text, m.end(), s_end)
    if not t:
        new = f"\t\tregion_state:{tag}={{\n{body}\t\t}}\n"
        line_start = text.rfind("\n", 0, s_end) + 1
        return text[:line_start] + new + text[line_start:]
    t_end = block_end(text, t.end() - 1)
    line_start = text.rfind("\n", 0, t_end) + 1
    return text[:line_start] + body + text[line_start:]


def raise_existing(text, state, tag, b, n):
    """Vorhandenes create_building gleichen Typs um n Stufen erhöhen (ein zweites gäbe 'already exists').

    Liefert den neuen Text oder None, wenn es im Block von tag keinen solchen Eintrag gibt.
    """
    m = re.search(rf"s:{state}\s*=\s*\{{", text)
    if not m:
        return None
    t = re.compile(rf"region_state:{tag}\s*=\s*\{{").search(text, m.end(), block_end(text, m.end() - 1))
    if not t:
        return None
    t_end = block_end(text, t.end() - 1)
    for cb in re.compile(r"create_building\s*=\s*\{").finditer(text, t.end(), t_end):
        cb_end = block_end(text, cb.end() - 1)
        if not re.search(rf'building\s*=\s*"{b}"', text[cb.end():cb_end]):
            continue
        lv = re.compile(r"levels\s*=\s*(\d+)").search(text, cb.end(), cb_end)
        if not lv:
            log.warning("%s/%s: %s ohne levels, lege nichts an", state, tag, b)
            return text
        new = int(lv.group(1)) + n
        if new > 0:
            return text[:lv.start(1)] + str(new) + text[lv.end(1):]
        # auf 0 gekürzt: ganzen Eintrag samt Zeile entfernen
        start = text.rfind("\n", 0, cb.start()) + 1
        end = text.find("\n", cb_end) + 1 or cb_end + 1
        return text[:start] + text[end:]
    return None


def entries_of(text, b):
    """(State, Land, Stufen) aller create_building des Typs b."""
    found = []
    for m in re.finditer(r"s:(STATE_\w+)\s*=\s*\{", text):
        s_end = block_end(text, m.end() - 1)
        for t in re.compile(r"region_state:(\w+)\s*=\s*\{").finditer(text, m.end(), s_end):
            t_end = block_end(text, t.end() - 1)
            for cb in re.compile(r"create_building\s*=\s*\{").finditer(text, t.end(), t_end):
                body = text[cb.end():block_end(text, cb.end() - 1)]
                if re.search(rf'building\s*=\s*"{b}"', body):
                    found.append((m.group(1), t.group(1), sum(int(x) for x in re.findall(r"levels\s*=\s*(\d+)", body))))
    return found


def plan_trim(text, data, b, rate, offset=0):
    """Schritte (State, Land) je -1 Stufe, bis die Region auf RATES[b] liegt.

    Gekürzt wird zuerst, wo ein State am weitesten über seinem Anteil liegt. Das letzte Gebäude dieses Typs
    eines Landes bleibt stehen.
    """
    kind = "fish" if b == "building_fishing_wharf" else b
    pops = {r["state"]: r["pops"] * state_factor(r, kind)
            for r in data if r["pops"] >= MIN_POPS}  # Profilfaktor wie beim Auffüllen, als gewichtete Pops
    lv = {(s, t): n for s, t, n in entries_of(text, b) if s in pops}
    target = round(rate * sum(pops.values()) / 1e6) - offset
    steps = []
    for _ in range(max(0, sum(lv.values()) - target)):
        per_state = Counter()
        per_tag = Counter()
        for (s, t), n in lv.items():
            per_state[s] += n
            per_tag[t] += n
        options = [(s, t) for (s, t), n in lv.items() if n > 0 and (n > 1 or per_tag[t] > 1)]
        if not options:
            log.warning("%s: Ziel %d nicht erreichbar, jedes Land hat nur noch ein Gebäude", b, target)
            break
        s, t = max(options, key=lambda k: (per_state[k[0]] - rate * pops[k[0]] / 1e6, lv[k]))
        lv[(s, t)] -= 1
        steps.append((s, t))
    return target, steps


def trim(target, data, b, apply):
    # "fish": Fischerei kürzen, Walfang zählt zum Maßstab mit und bleibt
    if b != "fish" and b not in RATES:
        log.error("%s hat keinen Maßstab in RATES", b)
        return 1
    rate = RATES[b]
    try:
        raw = target.read_bytes()
        text = raw.decode("utf-8-sig")
    except (OSError, UnicodeDecodeError) as e:
        log.error("%s nicht lesbar: %s", target, e)
        return 1
    offset = 0
    if b == "fish":
        b = "building_fishing_wharf"
        states = {r["state"] for r in data if r["pops"] >= MIN_POPS}
        offset = sum(n for s, _, n in entries_of(text, "building_whaling_station") if s in states)
        print(f"Walfang (bleibt, zählt mit): {offset}")
    goal, steps = plan_trim(text, data, b, rate, offset)
    cuts = Counter(steps)
    have = sum(n for _, _, n in entries_of(text, b))
    print(f"{b}: vorhanden {have}, Ziel {goal}, Kürzung {len(steps)}")
    for (s, t), n in cuts.most_common():
        print(f"- {s} ({t}): -{n}")
    if not apply:
        return 0
    for (s, t), n in cuts.items():
        changed = raise_existing(text, s, t, b, -n)
        if changed is None:
            log.error("%s/%s: %s nicht gefunden", s, t, b)
            return 1
        text = changed
    try:
        target.write_text(("﻿" if raw.startswith(b"\xef\xbb\xbf") else "") + text, encoding="utf-8", newline="")
        log.info("geschrieben: %s", target.relative_to(REPO))
    except OSError as e:
        log.error("%s nicht schreibbar: %s", target, e)
        return 1
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prefix")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--trim", metavar="GEBÄUDE", help="Gebäudeart (z. B. building_iron_mine) auf RATES kürzen "
                    "statt auffüllen; mit --apply schreiben")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    sys.stdout.reconfigure(encoding="utf-8")
    fname, data = rows(args.prefix)
    if fname is None:
        return 1
    files = sorted((REPO / "common/history/buildings").glob(f"{args.prefix}_*.txt"))
    if len(files) != 1:
        log.error("erwarte genau eine Gebäude-History mit Präfix %s, gefunden %d", args.prefix, len(files))
        return 1
    target = files[0]
    if args.trim:
        return trim(target, data, args.trim, args.apply)
    total = Counter()
    per_tag = Counter()
    plans = []
    print("| State | Land | Pops (Tsd.) | neu |\n|---|---|---|---|")
    planned = plan_region(data)
    for r in sorted(data, key=lambda r: -r["pops"]):
        for tag, add in planned.get(r["state"], {}).items():
            total += add
            per_tag[tag] += sum(add.values())
            plans.append((r, tag, add))
            print(f"| {r['state']} | {tag} | {r['owners'][tag] / 1e3:,.0f} | "
                  f"{' '.join(f'{k.replace(chr(98) + 'uilding_', '')} +{v}' for k, v in add.most_common())} |")
    print(f"\nSumme neu: {sum(total.values())} Stufen: {dict(total.most_common())}")
    pops = Counter()
    for r in data:
        pops.update(r["owners"])
    print("\n| Land | Pops (Mio.) | neu | je Mio. |\n|---|---|---|---|")
    for tag, n in pops.most_common():
        print(f"| {tag} | {n / 1e6:.2f} | {per_tag[tag]} | {per_tag[tag] / (n / 1e6):.1f} |")
    if not args.apply:
        return 0
    try:
        text = target.read_text(encoding="utf-8-sig")
    except OSError as e:
        log.error("%s nicht lesbar: %s", target, e)
        return 1
    bom = target.read_bytes().startswith(b"\xef\xbb\xbf")
    for r, tag, add in plans:
        for b, n in add.items():
            raised = raise_existing(text, r["state"], tag, b, n)
            text = raised if raised is not None else insert(text, r["state"], tag, entry(b, tag, n))
    try:
        target.write_text(("﻿" if bom else "") + text, encoding="utf-8", newline="")
        log.info("geschrieben: %s", target.relative_to(REPO))
    except OSError as e:
        log.error("%s nicht schreibbar: %s", target, e)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

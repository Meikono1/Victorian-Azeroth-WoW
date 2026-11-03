"""Länderübersicht: was jedes Azeroth-Land schon hat (Charaktere, JEs, Formables, Gebäude, Politik).

Aufruf:  python -I .claude/tools/va_country_overview.py [--md DATEI] [--tag TAG]
Ohne --md: Kurzfassung auf der Konsole. Liest nur, schreibt nur die --md-Datei.

Quellen (alle aus dem Repo):
  common/country_definitions/VA_*.txt         Tag, Rang, Kultur, Religion, Hauptstadt
  common/history/states, pops, buildings       States, Bevölkerung, Mod-eigene Gebäude
  common/history/countries/va_*.txt            Gesetze, Tech-Stufe, Politik-Preset
  common/history/characters + character_templates  Anführer/Charaktere mit Rolle
  common/history/global/*.txt                  gestartete JEs (c:TAG-Blöcke) plus Regeln (Mana, Todesschneise)
  common/history/diplomacy/*.txt               Subjekte und Oberherren
  common/country_formation/*.txt               Formables (Tag oder Kultur passt)
  localization/replace/english/va_countries_l_english.yml, common/coat_of_arms  Name und Flagge
"""
import argparse
import logging
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import va_script as vs  # noqa: E402

log = logging.getLogger("va_country_overview")

REPO = vs.REPO
MANA_CULTURES = {"sin_dorei", "quel_dorei"}  # wie va_is_mana_dependent_culture_trigger
GOVERNANCE_LAWS = {
    "law_chiefdom": "Häuptlingstum", "law_monarchy": "Monarchie", "law_theocracy": "Theokratie",
    "law_presidential_republic": "Präsidialrepublik", "law_parliamentary_republic": "Parlamentarische Republik",
    "law_council_republic": "Räterepublik", "law_oligarchy": "Oligarchie", "law_autocracy": "Autokratie",
}
ROLE_KEYS = [("ruler", "Herrscher"), ("heir", "Erbe"), ("is_general", "General"), ("is_admiral", "Admiral"),
             ("is_agitator", "Agitator"), ("ig_leader", "IG-Anführer")]


def tag_of(value):
    """'c:TAG' → 'TAG'."""
    return value.split(":", 1)[1] if isinstance(value, str) and value.startswith("c:") else None


def walk(block):
    """Alle (key, value)-Paare rekursiv."""
    for k, _, v in block or []:
        yield k, v
        if isinstance(v, list):
            yield from walk(v)


def files(folder, pattern="*.txt"):
    return sorted((REPO / folder).glob(pattern))


def load_definitions():
    defs = {}
    for f in files("common/country_definitions", "VA_*.txt"):
        continent = f.stem.replace("VA_", "")
        for tag, _, body in vs.parse_file(f):
            if not isinstance(body, list):
                continue
            defs[tag] = {
                "continent": continent,
                "tier": vs.get(body, "tier", "?"),
                "type": vs.get(body, "country_type", "?"),
                "cultures": vs.values(vs.get(body, "cultures")),
                "religion": vs.get(body, "religion", "aus Kultur"),  # optional, sonst Religion der Kultur
                "capital": vs.get(body, "capital", "?"),
            }
    log.info("%d Länder-Definitionen geladen", len(defs))
    return defs


def load_states():
    states = defaultdict(list)
    for f in files("common/history/states"):
        for _, _, top in vs.parse_file(f):
            for sname, _, sbody in top if isinstance(top, list) else []:
                if not isinstance(sbody, list):
                    continue
                for cs in vs.get_all(sbody, "create_state"):
                    tag = tag_of(vs.get(cs, "country"))
                    if tag:
                        states[tag].append(sname.split(":", 1)[-1])
    return states


def iter_region_states(folder):
    """(state, tag, block) aus POPS/BUILDINGS = { s:X = { region_state:TAG = { … } } }."""
    for f in files(folder):
        for _, _, top in vs.parse_file(f):
            for sname, _, sbody in top if isinstance(top, list) else []:
                for rk, _, rbody in sbody if isinstance(sbody, list) else []:
                    if rk and rk.startswith("region_state:") and isinstance(rbody, list):
                        yield sname.split(":", 1)[-1], rk.split(":", 1)[1], rbody


def load_pops():
    pops = defaultdict(int)
    bad = defaultdict(list)
    for state, tag, body in iter_region_states("common/history/pops"):
        for cp in vs.get_all(body, "create_pop"):
            size = vs.get(cp, "size", "0")
            try:
                pops[tag] += int(size)
            except ValueError:
                log.warning("Ungültige Pop-Größe '%s' bei %s in %s", size, tag, state)
                bad[tag].append(f"{state}: size = {size}")
    return pops, bad


def own_building_types():
    """Eigene Gebäudetypen: 20_Victorian_Azeroth.txt und va_*.txt. Die alten Vollkopien 01_…13_ zählen nicht (VA-003)."""
    keys = set()
    for f in files("common/buildings", "20_Victorian_Azeroth.txt") + files("common/buildings", "va_*.txt"):
        keys.update(k for k, _, v in vs.parse_file(f) if k and isinstance(v, list))
    if not keys:
        log.error("Keine eigenen Gebäudetypen gefunden")
    return keys


def load_special_buildings():
    """Eigene Gebäudetypen aus der Gebäude-History, je Land mit State."""
    own = own_building_types()
    special = defaultdict(set)
    for state, tag, body in iter_region_states("common/history/buildings"):
        for cb in vs.get_all(body, "create_building"):
            btype = vs.get(cb, "building")
            if btype in own:
                special[tag].add(f"{btype.replace('building_', '')} ({state.replace('STATE_', '').title()})")
    return special


def load_country_history():
    hist = {}
    for f in files("common/history/countries", "va_*.txt"):
        for _, _, top in vs.parse_file(f):
            for ck, _, body in top if isinstance(top, list) else []:
                tag = tag_of(ck)
                if not tag or not isinstance(body, list):
                    continue
                laws = [v.split(":", 1)[1] for k, v in walk(body) if k == "activate_law" and isinstance(v, str)]
                presets = [k for k, _, _ in body if k and k.startswith("effect_starting_politics_")]
                techs = [k for k, _, _ in body if k and k.startswith("effect_starting_technology_tier_")]
                hist[tag] = {"laws": laws, "preset": presets, "tech": techs}
    return hist


def load_characters():
    templates = {}
    for f in files("common/character_templates", "va_*.txt") + [REPO / "common/character_templates/00_default_template.txt"]:
        for name, _, body in vs.parse_file(f):
            if isinstance(body, list):
                templates[name] = body
    chars = defaultdict(list)
    for f in files("common/history/characters"):
        for _, _, top in vs.parse_file(f):
            for ck, _, body in top if isinstance(top, list) else []:
                tag = tag_of(ck)
                if not tag or not isinstance(body, list):
                    continue
                for cc in vs.get_all(body, "create_character"):
                    tname = vs.get(cc, "template")
                    tbody = templates.get(tname)
                    if tbody is None:
                        log.warning("%s: Vorlage %s fehlt", tag, tname)
                        chars[tag].append(f"{tname} (Vorlage fehlt)")
                        continue
                    name = f"{vs.get(tbody, 'first_name', '?')} {vs.get(tbody, 'last_name', '')}".replace("_", " ").strip()
                    roles = [label for key, label in ROLE_KEYS if vs.get(tbody, key) == "yes" or vs.get(cc, key) == "yes"]
                    chars[tag].append(f"{name} ({', '.join(roles) or 'ohne Rolle'})")
    return chars


def load_journal_entries(defs, states):
    jes = defaultdict(list)
    dead_scar_regions = set()
    for f in files("common/history/global"):
        parsed = vs.parse_file(f)
        for k, v in walk(parsed):
            if k and k.startswith("s:") and isinstance(v, list) and any(
                    kk == "set_variable" and isinstance(vv, list) and vs.get(vv, "name") == "va_dead_scar_region"
                    for kk, vv in walk(v)):
                dead_scar_regions.add(k[2:])
        for k, v in walk(parsed):
            tag = tag_of(k)
            if tag and isinstance(v, list):
                for kk, vv in walk(v):
                    if kk == "add_journal_entry" and isinstance(vv, list):
                        jes[tag].append(vs.get(vv, "type", "?"))
    # Regeln aus va_global_quel_thalas.txt (every_country mit limit)
    for tag, d in defs.items():
        if MANA_CULTURES & set(d["cultures"]):
            jes[tag].append("je_mana_hunger (Regel: Mana-Kultur)")
        if dead_scar_regions & set(states.get(tag, [])):
            jes[tag].append("je_va_dead_scar (Regel: Schneise, ab Quinine)")
    return jes


def load_subjects():
    rel = defaultdict(list)
    for f in files("common/history/diplomacy"):
        for _, _, top in vs.parse_file(f):
            for ck, _, body in top if isinstance(top, list) else []:
                over = tag_of(ck)
                if not over or not isinstance(body, list):
                    continue
                for pact in vs.get_all(body, "create_diplomatic_pact"):
                    sub = tag_of(vs.get(pact, "country"))
                    ptype = vs.get(pact, "type", "?")
                    if sub:
                        rel[over].append(f"Oberherr von {sub} ({ptype})")
                        rel[sub].append(f"{ptype} von {over}")
    return rel


def load_formables(defs):
    forms = defaultdict(list)
    for f in files("common/country_formation"):
        for ftag, _, body in vs.parse_file(f):
            if not isinstance(body, list):
                continue
            if ftag in defs:
                cultures = set(defs[ftag]["cultures"])
                for tag, d in defs.items():
                    if tag != ftag and cultures & set(d["cultures"]):
                        forms[tag].append(ftag)
            else:
                log.info("Formable %s (%s) ist kein Azeroth-Tag", ftag, f.name)
    return forms


def load_names_and_flags():
    names = {}
    loc = REPO / "localization/replace/english/va_countries_l_english.yml"
    try:
        for m in re.finditer(r'^\s+([A-Z0-9_]+):\d*\s*"(.*)"', loc.read_text(encoding="utf-8-sig"), re.M):
            names[m.group(1)] = m.group(2)
    except OSError as e:
        log.error("Länder-Loc nicht lesbar: %s", e)
    flags = set()
    for f in files("common/coat_of_arms/coat_of_arms"):
        flags.update(k for k, _, v in vs.parse_file(f) if k and isinstance(v, list))
    return names, flags


def politics(h):
    if not h:
        return "keine History"
    gov = [GOVERNANCE_LAWS[l] for l in h["laws"] if l in GOVERNANCE_LAWS]
    preset = ", ".join(p.replace("effect_starting_politics_", "") for p in h["preset"]) or "–"
    tech = ", ".join(t.replace("effect_starting_technology_tier_", "Tech ").replace("_tech", "") for t in h["tech"]) or "Tech ?"
    other = [l.replace("law_", "") for l in h["laws"] if l not in GOVERNANCE_LAWS]
    return f"{', '.join(gov) or 'Staatsform Standard'} · Preset {preset} · {tech} · Gesetze: {', '.join(other) or '–'}"


def build_rows():
    defs = load_definitions()
    states = load_states()
    pops, bad_pops = load_pops()
    special = load_special_buildings()
    hist = load_country_history()
    chars = load_characters()
    jes = load_journal_entries(defs, states)
    subs = load_subjects()
    forms = load_formables(defs)
    names, flags = load_names_and_flags()
    rows = []
    for tag in sorted(defs, key=lambda t: (defs[t]["continent"], t)):
        d = defs[tag]
        notes = []
        if tag not in names:
            notes.append("Name fehlt (VA-006)")
        if tag not in flags:
            notes.append("Flagge fehlt")
        if not states.get(tag):
            notes.append("kein State (spielt nicht)")
        if tag not in hist:
            notes.append("keine Länder-History")
        for b in bad_pops.get(tag, []):
            notes.append(f"Pop-Größe ungültig ({b})")
        rows.append({
            "continent": d["continent"], "tag": tag, "name": names.get(tag, "–"),
            "tier": d["tier"], "culture": ", ".join(d["cultures"]) + " · " + d["religion"],
            "capital": d["capital"].replace("STATE_", "").title(),
            "states": len(states.get(tag, [])), "pops": pops.get(tag, 0),
            "chars": "; ".join(chars.get(tag, [])) or "–",
            "jes": ", ".join(jes.get(tag, [])) or "–",
            "forms": ", ".join(forms.get(tag, [])) or "–",
            "buildings": ", ".join(sorted(special.get(tag, []))) or "–",
            "politics": politics(hist.get(tag)),
            "subjects": "; ".join(subs.get(tag, [])) or "–",
            "notes": "; ".join(notes) or "–",
        })
    return rows


def write_md(rows, path):
    lines = [
        "# Länderübersicht (generiert)",
        "",
        "Erzeugt von `python -I .claude/tools/va_country_overview.py --md .claude/laender_uebersicht.md`. **Nicht von Hand ändern**, sondern neu erzeugen.",
        "JEs mit „Regel“ startet `va_global_quel_thalas.txt` per `every_country`. Besondere Gebäude = eigene Gebäudetypen aus `20_Victorian_Azeroth.txt` und `va_*.txt` in der Gebäude-History. Formables zählen nur Azeroth-Tags (derzeit liegen in `country_formation` nur Vanilla-Formables, VA-017).",
        "",
    ]
    total = defaultdict(lambda: defaultdict(int))
    for r in rows:
        t = total[r["continent"]]
        t["Länder"] += 1
        t["mit Charakteren"] += r["chars"] != "–"
        t["mit JEs"] += r["jes"] != "–"
        t["ohne State"] += r["states"] == 0
    lines += ["## Zusammenfassung", "", "| Kontinent | Länder | mit Charakteren | mit JEs | ohne State |", "|---|---|---|---|---|"]
    for cont, t in total.items():
        lines.append(f"| {cont} | {t['Länder']} | {t['mit Charakteren']} | {t['mit JEs']} | {t['ohne State']} |")
    head = ("| Tag | Name | Rang | Kultur · Religion | Hauptstadt | States | Pops | Anführer/Charaktere | Journal Entries "
            "| Formables | Besondere Gebäude | Politik | Subjekt/Oberherr | Hinweise |")
    current = None
    for r in rows:
        if r["continent"] != current:
            current = r["continent"]
            lines += ["", f"## {current}", "", head, "|" + "---|" * 14]
        pops = f"{r['pops']:,}".replace(",", ".")
        lines.append(f"| `{r['tag']}` | {r['name']} | {r['tier']} | {r['culture']} | {r['capital']} | {r['states']} | "
                     f"{pops} | {r['chars']} | {r['jes']} | {r['forms']} | {r['buildings']} | {r['politics']} | "
                     f"{r['subjects']} | {r['notes']} |")
    try:
        Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")
    except OSError as e:
        log.error("Kann %s nicht schreiben: %s", path, e)
        raise
    log.info("%d Länder nach %s geschrieben", len(rows), path)


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--md", help="Markdown-Datei schreiben")
    ap.add_argument("--tag", help="nur dieses Land auf der Konsole zeigen")
    args = ap.parse_args()
    rows = build_rows()
    if args.tag:
        for r in rows:
            if r["tag"] == args.tag:
                for k, v in r.items():
                    print(f"{k:10} {v}")
                return
        log.error("Tag %s nicht gefunden", args.tag)
        sys.exit(1)
    if args.md:
        write_md(rows, args.md)
    else:
        for r in rows:
            print(f"{r['tag']:28} St {r['states']:2}  Char {r['chars'] != '–'!s:5}  JE {r['jes']}")


if __name__ == "__main__":
    main()

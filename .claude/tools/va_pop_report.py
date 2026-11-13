"""Bevölkerung zum Spielstart: Vanilla (1836) gegen Mod (VA-049). Liest common/history/pops und Länder-Loc.
Aufruf: python -I .claude/tools/va_pop_report.py "<Vanilla game-Ordner>" . .claude/regionen/bevoelkerung_vanilla_vs_mod.md"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


def tokens(text):
    text = re.sub(r"#[^\n]*", "", text)
    return re.findall(r'"[^"]*"|[{}=]|[^\s{}=]+', text)


def parse(tok, i=0):
    """Gibt Liste (key, value) zurück; value ist str oder Liste."""
    out = []
    while i < len(tok):
        t = tok[i]
        if t == "}":
            return out, i + 1
        if i + 1 < len(tok) and tok[i + 1] == "=":
            key = t
            v = tok[i + 2]
            if v == "{":
                sub, i = parse(tok, i + 3)
                out.append((key, sub))
            else:
                out.append((key, v.strip('"')))
                i += 3
        elif t == "{":
            sub, i = parse(tok, i + 1)
            out.append(("", sub))
        else:
            out.append((t, None))
            i += 1
    return out, i


def read_pops(folder):
    """-> {tag: {"pops": n, "states": set, "cultures": Counter, "slaves": n}}"""
    data = defaultdict(lambda: {"pops": 0, "states": set(), "cultures": Counter(), "slaves": 0})
    for f in sorted(Path(folder).glob("*.txt")):
        txt = f.read_bytes().decode("utf-8-sig", errors="replace")
        tree, _ = parse(tokens(txt))
        for k, v in tree:
            if k != "POPS" or not isinstance(v, list):
                continue
            for sk, sv in v:
                if not sk.startswith("s:STATE_") or not isinstance(sv, list):
                    continue
                for rk, rv in sv:
                    if not rk.startswith("region_state:") or not isinstance(rv, list):
                        continue
                    tag = rk.split(":", 1)[1]
                    for pk, pv in rv:
                        if pk != "create_pop" or not isinstance(pv, list):
                            continue
                        d = dict((a, b) for a, b in pv if isinstance(b, str))
                        try:
                            size = int(float(d.get("size", "0")))
                        except ValueError:
                            continue
                        e = data[tag]
                        e["pops"] += size
                        e["states"].add(sk[2:])
                        e["cultures"][d.get("culture", "?")] += size
                        if d.get("pop_type") == "slaves":
                            e["slaves"] += size
    return data


def read_names(folder):
    names = {}
    for f in Path(folder).rglob("*_l_english.yml"):
        for line in f.read_text(encoding="utf-8-sig", errors="replace").splitlines():
            m = re.match(r'\s+([A-Z][A-Z0-9_]*):\d*\s*"([^"]*)"', line)
            if m and m.group(1) not in names:
                names[m.group(1)] = m.group(2)
    return names


def fmt(n):
    return f"{n:,}".replace(",", ".")


def table(data, names, limit=None):
    rows = sorted(data.items(), key=lambda kv: -kv[1]["pops"])
    if limit:
        rows = rows[:limit]
    lines = ["| # | Tag | Name | Pops | States | Ø je State | Sklaven | Hauptkulturen (Anteil) |",
             "|---:|---|---|---:|---:|---:|---:|---|"]
    for i, (tag, e) in enumerate(rows, 1):
        st = len(e["states"])
        top = ", ".join(f"{c} {100 * s / e['pops']:.0f} %" for c, s in e["cultures"].most_common(3)) if e["pops"] else ""
        slaves = f"{100 * e['slaves'] / e['pops']:.0f} %" if e["slaves"] else "–"
        name = names.get(tag, "").replace("|", "/")
        lines.append(f"| {i} | {tag} | {name} | {fmt(e['pops'])} | {st} | {fmt(e['pops'] // st if st else 0)} | {slaves} | {top} |")
    return "\n".join(lines)


def summary(data):
    pops = [e["pops"] for e in data.values()]
    states = set().union(*(e["states"] for e in data.values())) if data else set()
    tot = sum(pops)
    s = sorted(pops)
    med = s[len(s) // 2] if s else 0
    cult = Counter()
    for e in data.values():
        cult.update(e["cultures"])
    slaves = sum(e["slaves"] for e in data.values())
    buckets = Counter()
    for p in pops:
        b = ("unter 100.000" if p < 1e5 else "100.000–500.000" if p < 5e5 else "0,5–1 Mio." if p < 1e6
             else "1–5 Mio." if p < 5e6 else "5–20 Mio." if p < 2e7 else "über 20 Mio.")
        buckets[b] += 1
    return tot, len(pops), len(states), med, cult, slaves, buckets


def section(title, data, names, limit=None):
    tot, n, nstates, med, cult, slaves, buckets = summary(data)
    order = ["unter 100.000", "100.000–500.000", "0,5–1 Mio.", "1–5 Mio.", "5–20 Mio.", "über 20 Mio."]
    out = [f"## {title}", "",
           f"- Bevölkerung gesamt: **{fmt(tot)}**",
           f"- Länder mit Pops: {n}; States mit Pops (State Regions): {nstates}",
           f"- Ø je Land: {fmt(tot // n if n else 0)}; Median je Land: {fmt(med)}; Ø je State Region: {fmt(tot // nstates if nstates else 0)}",
           f"- Sklaven: {fmt(slaves)} ({100 * slaves / tot:.1f} %)" if tot else "- Sklaven: –",
           f"- Kulturen: {len(cult)}; größte: " + ", ".join(f"{c} {fmt(s)}" for c, s in cult.most_common(8)),
           "- Länder nach Größe: " + ", ".join(f"{b}: {buckets[b]}" for b in order if buckets[b]),
           "", table(data, names, limit), ""]
    return "\n".join(out)


van_game, repo, outfile = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
van = read_pops(van_game / "common/history/pops")
mod = read_pops(repo / "common/history/pops")
names_v = read_names(van_game / "localization/english")
names_m = read_names(repo / "localization")
names_m = {**names_v, **names_m}

qt = {"SILVERMOON", "TRANQUILLIEN", "DEATHHOLME", "WRETCHED_BLOODELFES", "AMANI_TRIBE", "SHADOWPINE_TRIBE",
      "MOSSFLAYER_TROLLS", "DARNASSUS_OUTPOST_EK", "GRIMSCALE_MURLOCS", "HIGHVALE_HIGHELFES"}

doc = [
    "# Bevölkerung zum Spielstart: Vanilla gegen Victorian Azeroth",
    "",
    "Erzeugt 2026-11-12 von Claude aus `common/history/pops` (Vanilla 1.15, Start 1836, und Mod-Repo). Nur Startbevölkerung, keine Gebäude.",
    "„States“ = State Regions, in denen das Land Pops hat (geteilte States zählen bei jedem Besitzer). Kulturanteile je Land, Sklaven = `pop_type = slaves`.",
    "Neu erzeugen: `python -I .claude/tools/va_pop_report.py \"<Vanilla game-Ordner>\" . .claude/regionen/bevoelkerung_vanilla_vs_mod.md`.",
    "",
    section("Quel'Thalas (Mod) zum Vergleich", {k: v for k, v in mod.items() if k in qt}, names_m),
    section("Vanilla 1836 – alle Länder", van, names_v),
    section("Victorian Azeroth – alle Länder", mod, names_m),
]
outfile.write_text("\n".join(doc), encoding="utf-8")
print("Vanilla", len(van), "Länder,", summary(van)[0], "| Mod", len(mod), "Länder,", summary(mod)[0])

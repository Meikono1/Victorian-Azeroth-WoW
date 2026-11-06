"""Leitet das Provinz-Terrain (map_data/province_terrains.txt) aus der gemalten Karte ab (VA-051).

Der Ingame-Map-Editor kann das Terrain neu berechnen, speichert es im Mod aber nicht. Dieses Skript
macht dasselbe nach: je Provinz Anteil der Geländetexturen (gfx/map/terrain/mask_*.png) plus
Höhenrelief aus map_data/heightmap.png.

Regeln (Reihenfolge):
  1. Schnee-Textur > 35 %                         -> snow
  2. impassable im State                          -> mountain
  3. starkes Relief (Std. der Höhe >= 1400) oder
     Fels-Textur > 50 % bei Relief >= 1000         -> mountain
  4. Hügel-Felsen überwiegen die flachen Texturen,
     Relief >= 400 oder Hügel-Felsen > 40 % bei Relief >= 300
                                                  -> hills (Wald/Dschungel bleibt bis Relief 1000,
                                                     Feuchtgebiet bis 650)
  5. sonst die stärkste flache Textur (Gras -> plains, Wald, Sumpf, Wüste, Savanne, Tundra), Fallback plains
  6. STATE_OVERRIDES ersetzt danach Terrain je State (Lore-Korrekturen)

Farmland ist kein Grundterrain: Farmen wandeln plains dynamisch um (common/terrain_manipulators),
aber nur dort, wo die Farmland-Masken bemalt sind.

Aufruf: python -I .claude/tools/va_terrain.py 26 27 28 [--png DATEI] [--apply]
  NN        Präfixe der State-Region-Dateien (map_data/state_regions/NN_*.txt)
  --png     Vorschau (alt | neu) als PNG schreiben
  --apply   province_terrains.txt schreiben (ohne: nur Probelauf)
"""
import argparse
import logging
import re
import sys
from collections import Counter
from pathlib import Path

import numpy as np
from PIL import Image

sys.dont_write_bytecode = True  # kein __pycache__ im Repo
sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I nimmt das Skriptverzeichnis aus sys.path
from va_script import REPO

log = logging.getLogger("va_terrain")
Image.MAX_IMAGE_PIXELS = None  # Heightmap hat ~99 Mio. Pixel

TERRAIN_FILE = REPO / "map_data" / "province_terrains.txt"
PROVINCES_PNG = REPO / "map_data" / "provinces.png"
HEIGHTMAP_PNG = REPO / "map_data" / "heightmap.png"
MASK_DIR = REPO / "gfx" / "map" / "terrain"
STATE_DIR = REPO / "map_data" / "state_regions"

# Flache Texturen je Terrain (Vorbild: Vanilla common/terrain/01_terrain.txt, "materials"; ergänzt um Mod-Texturen)
FLAT = {
    "plains": [f"grasslands_0{i}" for i in range(1, 9)] + ["grassblue_01", "grasspurple_01"],
    "forest": ["woodlands_01", "woodlands_02"],
    "jungle": ["woodlands_03"],
    "wetland": [f"marchlands_0{i}" for i in range(1, 5)],
    "desert": ["desert_01", "desert_03", "desert_04", "desert_05", "desert_06", "red_desert_01"],
    "tundra": ["permafrost_01", "permafrost_03"],
    "savanna": ["savanna_01", "savanna_03"],
    "snow": ["snow_02"],
}
ROCK_MOUNTAIN = ["cliff_granite_02", "cliff_granite_06", "cliff_granite_07", "cliff_limestone_02",
                 "cliff_sandstone_03", "cliff_sandstone_04", "cliff_sandstone_05"]
ROCK_HILLS = ["cliff_granite_01", "cliff_limestone_03", "rocks_01", "ashrocks_01"]

SNOW_SHARE = 0.35
MOUNTAIN_RELIEF = 1400
MOUNTAIN_RELIEF_ROCK = 1000
MOUNTAIN_ROCK_SHARE = 0.5
HILLS_RELIEF = 400  # 2026-11-04 Kono: Hügel zu spärlich (650 -> 400)
HILLS_RELIEF_ROCK = 300
HILLS_ROCK_SHARE = 0.4
FOREST_HILLS_MAX = 1000
WETLAND_HILLS_MAX = 650
FLAT_MIN_SHARE = 0.05

# Lore-Korrekturen je State: { "STATE_X": { "alt": "neu", ... } } oder { "STATE_X": { "*": "neu" } }
# Eigene Terrain-Typen stehen in common/terrain/va_terrain.txt.
VASHJIR = ["STATE_IMMORTAL_COIL", "STATE_SMUGGLERS_SCAR", "STATE_GNAWS_BONEYARD", "STATE_SHIMMERING_GROTTO",
           "STATE_NESPIRAH", "STATE_BIELARAN_RIDGE", "STATE_VASHJ_IR", "STATE_ABYSSAL_BREACH",
           "STATE_KORTHUNS_END", "STATE_L_GHOREK", "STATE_PROMONTORY_POINT"]  # region_vashj_ir
STRANGLETHORN = ["STATE_GURUBASHI_ARENA", "STATE_EXPLORERS_LEAGUE_DIGSITE", "STATE_JAGUERO_ISLAND", "STATE_BOOTY_BAY",
                 "STATE_KURZENS_COMPOUND", "STATE_RUINS_OF_ZUL_KUNDA", "STATE_BAMBALA", "STATE_GROM_GOL_CAMP",
                 "STATE_FORT_LIVINGSTON", "STATE_ZUL_GURUB"]  # Kap und Nördliches Schlingendorntal
STATE_OVERRIDES: dict[str, dict[str, str]] = {
    **{s: {"*": "va_underwater"} for s in VASHJIR},  # 2026-11-04 Kono: Vashj'ir liegt unter Wasser
    **{s: {"plains": "jungle", "forest": "jungle", "savanna": "jungle"} for s in STRANGLETHORN},  # Textur fehlt dort
}
# TODO: Westfall (Savanne laut Textur) und Gilneas mit Kono abstimmen.

COLORS = {"plains": (170, 210, 100), "forest": (30, 110, 40), "hills": (170, 130, 70), "mountain": (110, 90, 80),
          "jungle": (0, 160, 120), "wetland": (80, 150, 170), "desert": (230, 210, 120), "tundra": (200, 200, 230),
          "savanna": (220, 170, 60), "snow": (255, 255, 255), "va_underwater": (40, 60, 160), "lakes": (0, 0, 255), "ocean": (0, 0, 140)}

PROV_RE = re.compile(r"x[0-9A-Fa-f]{6}")


def norm(key: str) -> str:
    return "x" + key[1:].upper()


def load_states(prefixes: list[str]) -> dict[str, dict]:
    """State -> {prov: [...], imp: set, hubs: {typ: prov}, capped: {bg_…/building_…: n}}. Nur die genannten Regionen."""
    states = {}
    for nn in prefixes:
        files = sorted(STATE_DIR.glob(f"{nn}_*.txt"))
        if not files:
            log.error("Keine State-Region-Datei für Präfix %s", nn)
            continue
        for f in files:
            text = f.read_text(encoding="utf-8-sig")
            for m in re.finditer(r"^(STATE_\w+)\s*=\s*\{(.*?)^\}", text, re.M | re.S):
                body = m.group(2)
                prov = re.search(r"provinces\s*=\s*\{([^}]*)\}", body)
                imp = re.search(r"impassable\s*=\s*\{([^}]*)\}", body)
                states[m.group(1)] = {
                    "prov": [norm(p) for p in PROV_RE.findall(prov.group(1))] if prov else [],
                    "imp": {norm(p) for p in PROV_RE.findall(imp.group(1))} if imp else set(),
                    "hubs": {h: norm(p) for h, p in re.findall(
                        r'^\s*(city|farm|mine|wood|port)\s*=\s*"(x[0-9A-Fa-f]{6})"', body, re.M)},
                    "capped": {k: int(v) for k, v in re.findall(  # EK/Kalimdor-Dateien nutzen building_…-Schlüssel (VA-062)
                        r"^\s*((?:bg|building)_\w+)\s*=\s*(\d+)", body, re.M)},
                }
            log.info("%s: %d States", f.name, len(states))
    return states


def load_terrain() -> tuple[list[str], dict[str, str]]:
    lines = TERRAIN_FILE.read_text(encoding="utf-8-sig").splitlines()
    terr = {}
    for line in lines:
        m = re.match(r'^(x[0-9A-Fa-f]{6})="(\w+)"', line)
        if m:
            terr[norm(m.group(1))] = m.group(2)
    return lines, terr


def province_stats(wanted: set[str]):
    """Mittlerer Masken-Anteil und Höhen-Std. je gewünschter Provinz."""
    log.info("Lade provinces.png")
    img = np.asarray(Image.open(PROVINCES_PNG).convert("RGB")).astype(np.uint32)
    packed = ((img[:, :, 0] << 16) | (img[:, :, 1] << 8) | img[:, :, 2]).ravel()
    del img
    uniq, inv = np.unique(packed, return_inverse=True)
    cnt = np.bincount(inv).astype(np.float64)
    keys = ["x%06X" % u for u in uniq]
    missing = wanted - set(keys)
    if missing:
        log.warning("%d Provinzen aus den States fehlen in provinces.png, z. B. %s", len(missing), sorted(missing)[:5])
    shape = (int(Image.open(PROVINCES_PNG).height), int(Image.open(PROVINCES_PNG).width))

    masks = {}
    needed = {m for ms in FLAT.values() for m in ms} | set(ROCK_MOUNTAIN) | set(ROCK_HILLS)
    for name in sorted(needed):
        f = MASK_DIR / f"mask_{name}.png"
        if not f.exists():
            log.warning("Maske fehlt: %s (zählt als 0)", f.name)
            continue
        m = Image.open(f).convert("L")
        if (m.height, m.width) != shape:
            log.error("Maske %s hat %sx%s statt %sx%s, übersprungen", f.name, m.width, m.height, shape[1], shape[0])
            continue
        masks[name] = np.bincount(inv, weights=np.asarray(m).ravel() / 255.0, minlength=len(uniq)) / cnt

    log.info("Lade heightmap.png (auf Provinzgröße skaliert)")
    h = np.asarray(Image.open(HEIGHTMAP_PNG).resize((shape[1], shape[0]), Image.BILINEAR)).astype(np.float64).ravel()
    mean = np.bincount(inv, weights=h, minlength=len(uniq)) / cnt
    sq = np.bincount(inv, weights=h * h, minlength=len(uniq)) / cnt
    relief = np.sqrt(np.maximum(sq - mean * mean, 0))
    return {k: i for i, k in enumerate(keys)}, masks, relief


def classify(i: int, impassable: bool, masks, relief) -> str:
    share = lambda names: sum(masks[n][i] for n in names if n in masks)
    flat = {t: share(ms) for t, ms in FLAT.items()}
    rock_m, rock_h, r = share(ROCK_MOUNTAIN), share(ROCK_HILLS), relief[i]
    best = max(flat, key=flat.get)
    if flat[best] < FLAT_MIN_SHARE:
        best = "plains"
    if flat["snow"] > SNOW_SHARE:
        return "snow"
    if impassable:
        return "mountain"
    if r >= MOUNTAIN_RELIEF or (rock_m > MOUNTAIN_ROCK_SHARE and r >= MOUNTAIN_RELIEF_ROCK):
        return "mountain"
    if rock_h > flat[best] or r >= HILLS_RELIEF or (rock_h > HILLS_ROCK_SHARE and r >= HILLS_RELIEF_ROCK):
        if best in ("forest", "jungle") and r < FOREST_HILLS_MAX and rock_h <= flat[best]:
            return best
        if best == "wetland" and r < WETLAND_HILLS_MAX and rock_h <= flat[best]:
            return best
        return "hills"
    return best


def apply_overrides(state: str, terrain: str) -> str:
    rule = STATE_OVERRIDES.get(state)
    if not rule:
        return terrain
    return rule.get(terrain, rule.get("*", terrain))


def write_png(path: Path, old: dict[str, str], new: dict[str, str]) -> None:
    img = np.asarray(Image.open(PROVINCES_PNG).convert("RGB")).astype(np.uint32)
    packed = (img[:, :, 0] << 16) | (img[:, :, 1] << 8) | img[:, :, 2]
    sel = np.isin(packed, [int(p[1:], 16) for p in new])
    ys, xs = np.where(sel)
    crop = packed[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    uniq, inv = np.unique(crop, return_inverse=True)
    halves = []
    for lookup in (old, new):
        pal = np.array([COLORS.get(lookup.get("x%06X" % u) if "x%06X" % u in new else None, (0, 0, 0))
                        for u in uniq], dtype=np.uint8)
        halves.append(pal[inv].reshape(crop.shape + (3,)))
    out = Image.fromarray(np.concatenate(halves, axis=1))
    out.thumbnail((2400, 2400))
    out.save(path)
    log.info("Vorschau (links alt, rechts neu): %s", path)


def write_terrain(lines: list[str], new: dict[str, str]) -> int:
    seen, changed, out = set(), 0, []
    for line in lines:
        m = re.match(r'^(x[0-9A-Fa-f]{6})="(\w+)"', line)
        if m and norm(m.group(1)) in new:
            key = norm(m.group(1))
            seen.add(key)
            if m.group(2) != new[key]:
                changed += 1
                line = f'{m.group(1)}="{new[key]}"'
        out.append(line)
    for key in sorted(set(new) - seen):
        log.warning("%s fehlte in province_terrains.txt, angehängt", key)
        out.append(f'{key}="{new[key]}"')
        changed += 1
    # Originalformat: ASCII ohne BOM, LF
    TERRAIN_FILE.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    return changed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("regions", nargs="+")
    ap.add_argument("--png", type=Path)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    states = load_states(args.regions)
    if not states:
        log.error("Keine States gefunden")
        return 1
    lines, old = load_terrain()
    wanted = {p for s in states.values() for p in s["prov"]}
    idx, masks, relief = province_stats(wanted)

    new = {}
    for name, st in states.items():
        for p in st["prov"]:
            if p in idx:
                new[p] = apply_overrides(name, classify(idx[p], p in st["imp"], masks, relief))

    moves = Counter((old.get(p, "-"), t) for p, t in new.items())
    log.info("Provinzen: %d, geändert: %d", len(new), sum(n for (a, b), n in moves.items() if a != b))
    log.info("Alt: %s", Counter(old.get(p, "-") for p in new).most_common())
    log.info("Neu: %s", Counter(new.values()).most_common())
    for (a, b), n in moves.most_common(15):
        log.info("  %-9s -> %-9s %5d", a, b, n)

    if args.png:
        write_png(args.png, old, new)
    if args.apply:
        log.info("Geschrieben: %d Zeilen geändert in %s", write_terrain(lines, new), TERRAIN_FILE.name)
    else:
        log.info("Probelauf, nichts geschrieben (--apply zum Schreiben)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

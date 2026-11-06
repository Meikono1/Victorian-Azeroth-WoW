"""Malt die dynamischen Masken (gfx/map/masks/mask_dynamic_*.png) je Region neu (VA-051, VA-061).

Die Masken legen fest, wo Gebäude die Provinz sichtbar umwandeln dürfen (Vanilla
common/terrain_manipulators): Farmen -> Felder (mask_dynamic_farmland), Holzfäller -> Rodung/Sägewerke
(mask_dynamic_forestry), Minen -> Tagebau (mask_dynamic_mining). Die Liste erlaubter Provinzen baut das
Spiel beim Start aus den Masken neu. Im Mod steckte darin die Erdkarte.

Vorgehen je Maske: Pixel der Provinzen in den genannten Regionen werden überschrieben, Rest bleibt
(mit --clear wird vorher die ganze Maske geleert, keine Erde-Reste).
  Stärke je Terrain (aus map_data/province_terrains.txt, daher erst va_terrain.py laufen lassen)
  x Rauschen (Flecken statt Flächen), Ränder weichgezeichnet, impassable -> 0.
  Forst/Bergbau nur in States mit passender Ressource (capped_resources), Hub-Provinz (wood/mine) voll.
Vorbild: Vanilla gfx/map/masks/ (8192x3616, L). Anteil an der Karte: Farmland 15 %, Forst 8 %, Bergbau 1 %.

Aufruf: python -I .claude/tools/va_dynamic_masks.py 26 27 28 [--masks farmland forestry mining] [--clear]
                                                     [--png ORDNER] [--apply]
  --masks   welche Masken (Standard: alle drei)
  --clear   ganze Maske vorher leeren
  --png     Vorschau je Maske in ORDNER schreiben
  --apply   Masken schreiben (ohne: Probelauf)
"""
import argparse
import logging
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

sys.dont_write_bytecode = True  # kein __pycache__ im Repo
sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I nimmt das Skriptverzeichnis aus sys.path
from va_script import REPO
from va_terrain import PROVINCES_PNG, load_states, load_terrain

log = logging.getLogger("va_dynamic_masks")
Image.MAX_IMAGE_PIXELS = None

MASK_DIR = REPO / "gfx" / "map" / "masks"
# Arbeitskopie des Map-Editors (paths.settings: map_masks_painter_tool). Fehlt sie im Mod, zeigt der Editor die
# Vanilla-Erdmasken und schreibt sie beim Speichern womöglich zurück (Kono 2026-11-06, VA-062).
PAINTER_DIR = REPO / "tools" / "mapeditor" / "mask_painter"
NOISE_OCTAVES = ((96, 0.5), (24, 0.3), (6, 0.2))  # (Pixel je Rasterpunkt, Gewicht)
EDGE_BLUR = 2.0
MIN_VALUE = 16  # wie Vanilla: kleinster Wert > 0

# weights: Anteil je Grundterrain; resource: nur States mit einem capped_resource, das so heißt/endet;
# hub: Hub-Provinz voll; cutoff: Rauschen darunter -> nichts (höher = fleckiger);
# floor/peak: Stärke eines Flecks (Vanilla-Median Farmland ~200, Forst ~100, Bergbau ~120)
MASKS = {
    "farmland": {"weights": {"plains": 1.0, "savanna": 0.9, "hills": 0.55, "forest": 0.2, "wetland": 0.15,
                             "jungle": 0.15},
                 "resource": None, "hub": None, "cutoff": 0.35, "floor": 0.6, "peak": 1.0, "seed": 51},
    "forestry": {"weights": {"forest": 1.0, "jungle": 0.9, "hills": 0.3, "wetland": 0.25, "plains": 0.12,
                             "savanna": 0.1},
                 "resource": ("bg_logging", "building_logging_camp"), "hub": "wood", "cutoff": 0.4, "floor": 0.35, "peak": 0.7, "seed": 52},
    "mining": {"weights": {"hills": 0.5, "mountain": 0.45, "desert": 0.2, "snow": 0.15, "plains": 0.08},
               "resource": ("_mining", "_mine"), "hub": "mine", "cutoff": 0.6, "floor": 0.4, "peak": 0.75, "seed": 53},
}


def noise(shape: tuple[int, int], rng: np.random.Generator) -> np.ndarray:
    """Mehrstufiges Wert-Rauschen 0..1 in Ausschnittgröße."""
    out = np.zeros(shape, dtype=np.float32)
    for step, weight in NOISE_OCTAVES:
        small = rng.random((shape[0] // step + 2, shape[1] // step + 2)).astype(np.float32)
        big = Image.fromarray(small).resize((shape[1] + step, shape[0] + step), Image.BICUBIC)
        out += weight * np.asarray(big)[:shape[0], :shape[1]]
    return np.clip(out, 0, 1)


def has_resource(state: dict, res: tuple[str, ...] | None) -> bool:
    """capped_resources mit bg_…- (Vanilla-Stil) oder building_…-Schlüsseln (EK, Kalimdor; vorher übersehen, VA-062)."""
    if res is None:
        return True
    return any(k == r or k.endswith(r) for k in state["capped"] for r in res)


class Region:
    """Ausschnitt der Karte mit den Provinzen der gewählten Regionen."""

    def __init__(self, states: dict):
        img = np.asarray(Image.open(PROVINCES_PNG).convert("RGB")).astype(np.uint32)
        packed = (img[:, :, 0] << 16) | (img[:, :, 1] << 8) | img[:, :, 2]
        del img
        self.shape = packed.shape
        keys = {int(p[1:], 16) for st in states.values() for p in st["prov"]}
        sel = np.isin(packed, list(keys))
        ys, xs = np.where(sel)
        if ys.size == 0:
            raise ValueError("Keine Pixel der Regionen in provinces.png")
        self.box = (ys.min(), ys.max() + 1, xs.min(), xs.max() + 1)
        crop = packed[self.box[0]:self.box[1], self.box[2]:self.box[3]]
        self.inside = sel[self.box[0]:self.box[1], self.box[2]:self.box[3]]
        self.uniq, self.inv = np.unique(crop, return_inverse=True)
        self.inv = self.inv.reshape(crop.shape)

    def paint(self, cfg: dict, states: dict, terrain: dict[str, str]) -> np.ndarray:
        weights = {}
        for st in states.values():
            if not has_resource(st, cfg["resource"]):
                continue
            for p in st["prov"]:
                if p not in st["imp"]:
                    weights[int(p[1:], 16)] = cfg["weights"].get(terrain.get(p, ""), 0.0)
            hub = st["hubs"].get(cfg["hub"]) if cfg["hub"] else None
            if hub and hub not in st["imp"]:
                weights[int(hub[1:], 16)] = 1.0
        w = np.array([weights.get(int(u), 0.0) for u in self.uniq], dtype=np.float32)[self.inv]
        n = noise(w.shape, np.random.default_rng(cfg["seed"]))
        spots = np.clip((n - cfg["cutoff"]) / (1 - cfg["cutoff"]), 0, 1)
        strength = np.where(spots > 0, cfg["floor"] + (cfg["peak"] - cfg["floor"]) * np.sqrt(spots), 0)
        val = Image.fromarray((w * strength * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(EDGE_BLUR))
        val = np.asarray(val).copy()
        val[val < MIN_VALUE] = 0
        val[~self.inside] = 0
        return val


def save_mask(mask: np.ndarray, path: Path) -> None:
    """Maske nach gfx/map/masks und gleichnamig in die Map-Editor-Kopie schreiben."""
    img = Image.fromarray(mask, mode="L")
    for target in (path, PAINTER_DIR / path.name):
        if not target.parent.exists():
            log.error("Ordner fehlt: %s", target.parent)
            continue
        img.save(target, optimize=True)
        log.info("Geschrieben: %s", target.relative_to(REPO))


def process(name: str, region: Region, states: dict, terrain: dict, args) -> bool:
    path = MASK_DIR / f"mask_dynamic_{name}.png"
    mask_img = Image.open(path)
    if mask_img.mode != "L" or (mask_img.height, mask_img.width) != region.shape:
        log.error("%s hat %s/%s, erwartet L in Kartengröße", path.name, mask_img.mode, mask_img.size)
        return False
    mask = np.asarray(mask_img).copy()
    log.info("%s: vorher %.1f %% der Karte bemalt", name, 100.0 * (mask > 0).mean())
    if args.clear:
        mask[:] = 0
    b = region.box
    part = mask[b[0]:b[1], b[2]:b[3]]
    val = region.paint(MASKS[name], states, terrain)
    part[region.inside] = val[region.inside]
    log.info("%s: Regionsfläche %.1f %% bemalt, ganze Karte jetzt %.2f %%", name,
             100.0 * (val[region.inside] > 0).mean(), 100.0 * (mask > 0).mean())
    if args.png:
        args.png.mkdir(parents=True, exist_ok=True)
        prev = Image.fromarray(part)
        prev.thumbnail((1200, 1200))
        prev.save(args.png / f"va_mask_{name}.png")
    if args.apply:
        save_mask(mask, path)
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("regions", nargs="+")
    ap.add_argument("--masks", nargs="+", choices=sorted(MASKS), default=sorted(MASKS))
    ap.add_argument("--clear", action="store_true")
    ap.add_argument("--png", type=Path)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    states = load_states(args.regions)
    if not states:
        log.error("Keine States gefunden")
        return 1
    _, terrain = load_terrain()
    try:
        region = Region(states)
    except ValueError as e:
        log.error("%s", e)
        return 1
    ok = all([process(name, region, states, terrain, args) for name in args.masks])
    if not args.apply:
        log.info("Probelauf, nichts geschrieben (--apply zum Schreiben)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

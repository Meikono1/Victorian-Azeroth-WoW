"""Malt die Todesschneise je State in die dynamische Bergbau-Maske (VA-062).

Das unsichtbare building_va_dead_scar färbt über den Terrain-Manipulator va_dead_scar
(common/terrain_manipulators/00_va_terrain_manipulators.txt) die Provinzen unter einer dynamischen Maske.
Eigene Masken-Schlüssel kennt das Spiel nicht (der Map-Editor wirft sie aus gfx/map/masks/manifest.json),
daher teilt sich die Schneise mask_dynamic_mining mit den Minen.
Form der Schneise: .claude/regionen/va_dead_scar_form.png (alte feste Maske mask_devastation_mud_01.png).
Die feste Bodentextur entfernt Kono im Map-Editor, nie per Skript (Masken-Gewichtung, VA-062).
Vorbild: va_dynamic_masks.py (Region-Ausschnitt), Vanilla gfx/map/masks/ (8192x3616, L).

Aufruf: python -I .claude/tools/va_scar_mask.py 26 STATE_EAST_SANCTUM [STATE_…] [--fill xRRGGBB …] [--free-others] [--scar-only] [--remove] [--apply]
  NN        Präfix der State-Region-Datei (map_data/state_regions/NN_*.txt)
  --fill    diese Provinzen ganz zur Schneise zählen (nur in der Kopie der Vorlage, nicht gespeichert)
  --free-others  Schneisen-Provinzen aus Farmland- und Forst-Maske nehmen (sonst belegen Farmen/Städte sie zuerst)
  --scar-only     in diesen States alle Nicht-Schneisen-Provinzen aus der Bergbau-Maske nehmen: das Schneisen-Gebäude
                 wandelt jede Bergbau-Fläche seines States um, nicht nur die Schneise (Kono-Test T-101)
  --remove  Schneisen-Pixel dieser States wieder aus der Bergbau-Maske nehmen
  --apply   schreiben (ohne: Probelauf)
"""
import argparse
import logging
import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.dont_write_bytecode = True  # kein __pycache__ im Repo
sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I nimmt das Skriptverzeichnis aus sys.path
from va_script import REPO
from va_terrain import load_states
from va_dynamic_masks import Region, save_mask

log = logging.getLogger("va_scar_mask")
Image.MAX_IMAGE_PIXELS = None

FORM = REPO / ".claude" / "regionen" / "va_dead_scar_form.png"
TARGET = REPO / "gfx" / "map" / "masks" / "mask_dynamic_mining.png"
FILL_VALUE = 200  # Stärke für --fill (Median der übrigen Schneisen-Provinzen ~170)
OTHERS = [REPO / "gfx" / "map" / "masks" / f"mask_dynamic_{n}.png" for n in ("farmland", "forestry")]
SHARE_MIN = 0.2  # ab diesem Schneisen-Anteil zählt eine Provinz für --free-others/--scar-only zur Schneise


def load_mask(path: Path, shape: tuple[int, int]) -> np.ndarray | None:
    if not path.exists():
        log.error("%s fehlt", path)
        return None
    img = Image.open(path)
    if img.mode != "L" or (img.height, img.width) != shape:
        log.error("%s hat %s/%s, erwartet L in Kartengröße", path.name, img.mode, img.size)
        return None
    return np.asarray(img).copy()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("prefix")
    ap.add_argument("states", nargs="+")
    ap.add_argument("--remove", action="store_true")
    ap.add_argument("--fill", nargs="+", metavar="xRRGGBB", default=[])
    ap.add_argument("--free-others", action="store_true")
    ap.add_argument("--scar-only", action="store_true")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    all_states = load_states([args.prefix])
    missing = [s for s in args.states if s not in all_states]
    if missing:
        log.error("Nicht in Region %s: %s", args.prefix, ", ".join(missing))
        return 1
    try:
        region = Region({s: all_states[s] for s in args.states})
    except ValueError as e:
        log.error("%s", e)
        return 1

    form = load_mask(FORM, region.shape)
    target = load_mask(TARGET, region.shape)
    if form is None or target is None:
        return 1

    b = region.box
    f_part = form[b[0]:b[1], b[2]:b[3]]
    t_part = target[b[0]:b[1], b[2]:b[3]]
    if args.fill:
        # Provinzen, die das Spiel trotz Teilabdeckung nie umwandelt (x1C0EED, xF017F6), ganz bemalen
        for p in args.fill:
            key = int(p.lstrip("xX"), 16)
            idx = np.where(region.uniq == key)[0]
            if idx.size == 0:
                log.error("Provinz %s liegt nicht in %s", p, ", ".join(args.states))
                return 1
            m = (region.inv == idx[0]) & region.inside
            f_part[m] = np.maximum(f_part[m], FILL_VALUE)
            log.info("%s: %d Pixel voll bemalt", p, int(m.sum()))
    sel = region.inside & (f_part > 0)
    log.info("%d Pixel der Schneise in %s", int(sel.sum()), ", ".join(args.states))
    if not sel.any():
        log.warning("Nichts zu tun")
        return 0
    if args.remove:
        t_part[sel] = 0
    else:
        # nur verstärken: frühere --fill-Läufe dürfen nicht wieder abgeschwächt werden
        t_part[sel] = np.maximum(t_part[sel], f_part[sel])
    log.info("%s jetzt %d Pixel", TARGET.name, int((target > 0).sum()))

    if args.scar_only and not args.remove:
        # Ausweichflächen für Minen (T-102) wurden selbst zur Schneise (West Sanctum x4BFDA4, x5B9E0E). Daher in den
        # Schneisen-States nur die Schneise in der Bergbau-Maske; spätere Minen dort überschreiben sie (Kono 2026-11-06).
        share = np.bincount(region.inv[sel], minlength=region.uniq.size) / np.maximum(
            np.bincount(region.inv[region.inside], minlength=region.uniq.size), 1)
        rest = np.isin(region.inv, np.where(share < SHARE_MIN)[0]) & region.inside
        log.info("--scar-only: %d Pixel außerhalb der Schneise aus der Bergbau-Maske genommen", int((t_part[rest] > 0).sum()))
        t_part[rest] = 0

    others = {}
    if args.free_others and not args.remove:
        # Eine Provinz bekommt nur ein umgewandeltes Gelände; Farmen/Städte (Farmland-Maske) und Holzfäller
        # nahmen sonst Schneisen-Provinzen weg (Kono-Test 2026-11-06). Schneisen-Provinzen dort ganz leeren.
        share = np.bincount(region.inv[sel], minlength=region.uniq.size) / np.maximum(
            np.bincount(region.inv[region.inside], minlength=region.uniq.size), 1)
        scar_idx = np.where(share >= SHARE_MIN)[0]
        prov = np.isin(region.inv, scar_idx) & region.inside
        log.info("%d Schneisen-Provinzen (Anteil >= %.0f %%)", scar_idx.size, 100 * SHARE_MIN)
        for path in OTHERS:
            mask = load_mask(path, region.shape)
            if mask is None:
                return 1
            part = mask[b[0]:b[1], b[2]:b[3]]
            log.info("%s: %d Pixel geleert", path.name, int((part[prov] > 0).sum()))
            part[prov] = 0
            others[path] = mask

    if not args.apply:
        log.info("Probelauf, nichts geschrieben (--apply zum Schreiben)")
        return 0
    save_mask(target, TARGET)
    for path, mask in others.items():
        save_mask(mask, path)
    return 0


if __name__ == "__main__":
    sys.exit(main())

# Wandelt ein Bild (PNG/JPG) in ein Vic3-Icon um: quadratisch, DDS BGRA unkomprimiert mit Mipmaps (VA-027).
# Vorbild: Vanilla gfx/interface/icons/goods_icons/*.dds (256x256, BGRA unkomprimiert, 9 Mipmaps).
# Aufruf: python -I .claude/tools/va_icon.py <quelle> <ziel.dds> [--size 256] [--keep-aspect]
# --keep-aspect: Seitenverhältnis behalten, --size ist dann die Breite (Event-Bilder, Eventfenster zeigt [Event.GetTexture]).
import argparse
import logging
import struct
import sys
from pathlib import Path

from PIL import Image

log = logging.getLogger("va_icon")


def convert(src: Path, dst: Path, size: int, keep_aspect: bool = False) -> None:
    im = Image.open(src).convert("RGBA")
    log.info("Quelle %s: %sx%s", src, im.width, im.height)
    if keep_aspect:
        _convert_keep_aspect(im, dst, size)
        return
    if im.width != im.height:
        side = max(im.width, im.height)
        canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
        canvas.paste(im, ((side - im.width) // 2, (side - im.height) // 2))
        im = canvas
        log.warning("Nicht quadratisch, transparent auf %sx%s aufgefüllt", side, side)
    if im.width < size:
        log.warning("Quelle kleiner als Ziel (%s < %s), Hochskalierung wird unscharf", im.width, size)
    im = im.resize((size, size), Image.LANCZOS)
    mips = [im]
    while mips[-1].width > 1:
        s = mips[-1].width // 2
        mips.append(im.resize((s, s), Image.LANCZOS))
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(_dds_header(size, size, len(mips)) + b"".join(_bgra(m) for m in mips))
    log.info("Geschrieben: %s (%sx%s, BGRA unkomprimiert, %s Mipmaps)", dst, size, size, len(mips))


def _convert_keep_aspect(im: Image.Image, dst: Path, width: int) -> None:
    if im.width < width:
        log.warning("Quelle schmaler als Ziel (%s < %s), Hochskalierung wird unscharf", im.width, width)
    height = round(im.height * width / im.width)
    im = im.resize((width, height), Image.LANCZOS)
    mips = [im]
    while mips[-1].width > 1 or mips[-1].height > 1:
        mips.append(im.resize((max(1, mips[-1].width // 2), max(1, mips[-1].height // 2)), Image.LANCZOS))
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(_dds_header(width, height, len(mips)) + b"".join(_bgra(m) for m in mips))
    log.info("Geschrieben: %s (%sx%s, BGRA unkomprimiert, %s Mipmaps)", dst, width, height, len(mips))


def _bgra(im: Image.Image) -> bytes:
    r, g, b, a = im.split()
    return Image.merge("RGBA", (b, g, r, a)).tobytes()


def _dds_header(width: int, height: int, mip_count: int) -> bytes:
    # Felder wie Vanilla electricity.dds: CAPS|HEIGHT|WIDTH|PITCH|PIXELFORMAT|MIPMAPCOUNT, RGBA 32 bit.
    flags = 0x1 | 0x2 | 0x4 | 0x8 | 0x1000 | 0x20000
    pf = struct.pack("<8I", 32, 0x41, 0, 32, 0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
    caps = 0x1000 | 0x8 | 0x400000  # TEXTURE | COMPLEX | MIPMAP
    return (b"DDS " + struct.pack("<7I", 124, flags, height, width, width * 4, 0, mip_count)
            + b"\0" * 44 + pf + struct.pack("<5I", caps, 0, 0, 0, 0))


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    ap = argparse.ArgumentParser()
    ap.add_argument("src", type=Path)
    ap.add_argument("dst", type=Path)
    ap.add_argument("--size", type=int, default=256)
    ap.add_argument("--keep-aspect", action="store_true")
    args = ap.parse_args()
    if not args.src.is_file():
        log.error("Quelle fehlt: %s", args.src)
        return 1
    try:
        convert(args.src, args.dst, args.size, args.keep_aspect)
    except Exception:
        log.exception("Umwandlung fehlgeschlagen")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

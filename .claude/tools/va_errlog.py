"""Fasst error.log des letzten Spielstarts zusammen (inkl. rotierter error.N.log).

Aufruf: python -I .claude/tools/va_errlog.py [--top N] [--filter TEXT]
Gruppiert nach Quelle (Script location / Datei) und Fehlertext, Zahlen normalisiert.
"""
import argparse
import logging
import os
import re
from collections import Counter
from pathlib import Path

log = logging.getLogger("va_errlog")
LOGS = Path(os.environ["USERPROFILE"]) / "Documents/Paradox Interactive/Victoria 3/logs"
ENTRY = re.compile(r"^\[(\d\d:\d\d:\d\d)\]\[([^\]]+)\]: ?(.*)")
LOCATION = re.compile(r"((?:common|events|gfx|map_data|localization|gui)/[\w./-]+\.(?:txt|gui|yml|gfx))")


def run_files():
    """error*.log des letzten Laufs, älteste zuerst. Lauf-Start = Zeitstempel von system.log."""
    start = (LOGS / "system.log").stat().st_mtime - 5
    files = [f for f in LOGS.glob("error*.log") if f.stat().st_mtime >= start]
    if not files:
        log.error("Keine error*.log seit dem letzten Start gefunden (%s)", LOGS)
    return sorted(files, key=lambda f: f.stat().st_mtime)


def entries(files):
    cur = None
    for f in files:
        for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
            m = ENTRY.match(line)
            if m:
                if cur:
                    yield cur
                cur = [m.group(2), m.group(3)]
            elif cur and line.strip():
                cur.append(line.strip())
    if cur:
        yield cur


def key(entry):
    text = " | ".join(entry[1:])
    loc = LOCATION.search(text)
    src = loc.group(1) if loc else entry[0]
    msg = next((t for t in entry[1:] if t.startswith("Error:")), entry[1])
    msg = re.sub(r"\d+", "N", LOCATION.sub("", msg))[:110]
    return src, msg


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=40)
    ap.add_argument("--filter", default="")
    ap.add_argument("--by-file", action="store_true", help="nur nach Quelldatei gruppieren")
    a = ap.parse_args()
    files = run_files()
    log.info("Dateien: %s", ", ".join(f.name for f in files))
    groups, total = Counter(), 0
    for e in entries(files):
        if a.filter and a.filter not in " ".join(e):
            continue
        total += 1
        k = key(e)
        groups[(k[0], "") if a.by_file else k] += 1
    print(f"{total} Einträge, {len(groups)} Gruppen")
    for (src, msg), n in groups.most_common(a.top):
        print(f"{n:6}  {src}" + (f"  ::  {msg}" if msg else ""))


if __name__ == "__main__":
    main()

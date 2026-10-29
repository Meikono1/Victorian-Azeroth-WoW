"""Minimaler Parser für Paradox-Script und Auflösung der wirksamen Dateien (Mod über Vanilla).

Ein Block ist eine Liste von Einträgen (key, op, value). Nackte Werte wie in
`provinces = { "x1" "x2" }` haben key None. value ist str oder wieder ein Block.
"""
import json
import logging
import re
from pathlib import Path

log = logging.getLogger("va_script")

REPO = Path(__file__).resolve().parents[2]
VANILLA = Path(r"C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\game")
TOKEN = re.compile(r'"[^"]*"|[{}]|\?=|[<>!]=|[=<>]|[^\s{}=<>!?"#]+|#[^\n]*')


def tokens(text):
    for t in TOKEN.findall(text):
        if t.startswith("#"):
            continue
        yield t[1:-1] if t.startswith('"') else t


def parse(text, origin="?"):
    stack = [[]]
    toks = list(tokens(text.lstrip("\ufeff")))
    i = 0
    while i < len(toks):
        t = toks[i]
        if t == "{":
            stack.append([])
        elif t == "}":
            if len(stack) == 1:
                log.warning("%s: überzählige '}' bei Token %d", origin, i)
            else:
                block = stack.pop()
                parent = stack[-1]
                # Block gehört zum vorherigen "key op" oder ist ein nackter Block
                if parent and parent[-1][2] is None:
                    k, op, _ = parent[-1]
                    parent[-1] = (k, op, block)
                else:
                    parent.append((None, None, block))
        elif i + 1 < len(toks) and toks[i + 1] in ("=", "?=", "<", ">", "<=", ">=", "!="):
            op = toks[i + 1]
            if i + 2 < len(toks) and toks[i + 2] == "{":
                stack[-1].append((t, op, None))
                i += 1
            else:
                stack[-1].append((t, op, toks[i + 2] if i + 2 < len(toks) else ""))
                i += 2
        else:
            stack[-1].append((None, None, t))
        i += 1
    if len(stack) != 1:
        log.warning("%s: %d nicht geschlossene Blöcke", origin, len(stack) - 1)
    return stack[0]


def parse_file(path):
    try:
        return parse(Path(path).read_text(encoding="utf-8-sig", errors="replace"), str(path))
    except OSError as e:
        log.error("Kann %s nicht lesen: %s", path, e)
        return []


def get(block, key, default=None):
    for k, _, v in block:
        if k == key:
            return v
    return default


def get_all(block, key):
    return [v for k, _, v in block if k == key]


def values(block):
    """Nackte Werte eines Blocks, z. B. Provinzlisten."""
    return [v for k, _, v in (block or []) if k is None and isinstance(v, str)]


def replace_paths():
    meta = REPO / ".metadata/metadata.json"
    try:
        data = json.loads(meta.read_text(encoding="utf-8-sig"))
        return set(data["game_custom_data"]["replace_paths"])
    except (OSError, KeyError, ValueError) as e:
        log.error("metadata.json nicht lesbar: %s", e)
        return set()


def effective_files(folder, pattern="*.txt"):
    """Dateien, die das Spiel für `folder` lädt: Mod ersetzt gleichnamige Vanilla-Dateien."""
    mod = {f.name: f for f in (REPO / folder).glob(pattern)}
    if folder in replace_paths():
        return sorted(mod.values())
    van = {f.name: f for f in (VANILLA / folder).glob(pattern)}
    van.update(mod)
    return sorted(van.values(), key=lambda f: f.name)


def top_level_keys(folder):
    """Alle definierten Objektnamen eines Ordners (über wirksame Dateien)."""
    keys = {}
    for f in effective_files(folder):
        for k, _, v in parse_file(f):
            if k and isinstance(v, list):
                keys[k.split(":", 1)[-1]] = v
    return keys

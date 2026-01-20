#!/usr/bin/env python3
import sys
from pathlib import Path

def die(msg):
    print("error:", msg, file=sys.stderr)
    sys.exit(1)

def replace_all(text: str, old: str, new: str) -> str:
    return text.replace(old, new)

def main():
    if len(sys.argv) < 4:
        die("usage: rename_actor_prefix.py <file> <oldPrefix> <newPrefix> [<oldPath> <newPath>]")
    p = Path(sys.argv[1])
    oldp = sys.argv[2]
    newp = sys.argv[3]

    old_path = None
    new_path = None
    if len(sys.argv) >= 6:
        old_path = sys.argv[4]
        new_path = sys.argv[5]

    s = p.read_text(encoding="utf-8", errors="ignore")

    # prefix rename (mario_ -> luigi_)
    s = replace_all(s, oldp, newp)

    # optional include-path swap (actors/mario/ -> actors/luigi/)
    if old_path and new_path:
        s = replace_all(s, old_path, new_path)

    p.write_text(s, encoding="utf-8")
    print(f"patched {p}")

if __name__ == "__main__":
    main()

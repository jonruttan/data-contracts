#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CLASS_MAP = {"must": "MUST", "can": "MAY", "cannot": "MUST_NOT"}
RE_CLASS = re.compile(r"(?m)^(\s*class:\s*)(must|can|cannot)(\s*)$")


def _iter_targets() -> list[Path]:
    out: list[Path] = []
    for base in ("docs/spec", "docs/book"):
        p = ROOT / base
        if not p.exists():
            continue
        out.extend(sorted(x for x in p.rglob("*.md") if x.is_file()))
    return out


def _apply(raw: str) -> str:
    return RE_CLASS.sub(lambda m: f"{m.group(1)}{CLASS_MAP[m.group(2)]}{m.group(3)}", raw)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Codemod class: must/can/cannot -> MUST/MAY/MUST_NOT")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--write", action="store_true")
    ns = ap.parse_args(argv)
    if ns.check == ns.write:
        ap.error("set exactly one of --check or --write")

    changed = 0
    for p in _iter_targets():
        raw = p.read_text(encoding="utf-8")
        updated = _apply(raw)
        if updated != raw:
            changed += 1
            if ns.write:
                p.write_text(updated, encoding="utf-8")
            else:
                print(p.relative_to(ROOT).as_posix())
    if ns.check and changed:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

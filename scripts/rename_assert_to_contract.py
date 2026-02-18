#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET_DIRS = (ROOT / "docs", ROOT / "tests")
EXTS = {".md", ".yaml", ".yml"}
ASSERT_RE = re.compile(r"(?m)^(\s*)assert:\s*$")


def iter_files() -> list[Path]:
    out: list[Path] = []
    for root in TARGET_DIRS:
        for p in root.rglob("*"):
            if p.is_file() and p.suffix.lower() in EXTS:
                out.append(p)
    return out


def main() -> int:
    changed = 0
    for path in iter_files():
        raw = path.read_text(encoding="utf-8")
        updated = ASSERT_RE.sub(r"\1contract:", raw)
        if updated != raw:
            path.write_text(updated, encoding="utf-8")
            changed += 1
    print(f"updated files: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

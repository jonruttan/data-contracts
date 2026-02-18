#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET_DIRS = (
    ROOT / "docs",
    ROOT / "spec_runner",
    ROOT / "scripts",
    ROOT / "tests",
    ROOT / "README.md",
)
EXTS = {".md", ".py", ".php", ".rs", ".yaml", ".yml", ".txt"}


def iter_files() -> list[Path]:
    out: list[Path] = []
    for item in TARGET_DIRS:
        if isinstance(item, Path) and item.is_file():
            out.append(item)
            continue
        if isinstance(item, Path) and item.is_dir():
            for p in item.rglob("*"):
                if p.is_file() and p.suffix.lower() in EXTS:
                    out.append(p)
    return out


def main() -> int:
    changed = 0
    for path in iter_files():
        raw = path.read_text(encoding="utf-8")
        updated = raw.replace("yaml contract-spec", "yaml contract-spec")
        if updated != raw:
            path.write_text(updated, encoding="utf-8")
            changed += 1
    print(f"updated files: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

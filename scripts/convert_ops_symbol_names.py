#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


MAPPINGS = (
    ("ops.fs.read_file", "ops.fs.file.read"),
    ("ops.fs.write_file", "ops.fs.file.write"),
    ("ops.fs.list_dir", "ops.fs.dir.list"),
    ("ops.fs.path_exists", "ops.fs.path.exists"),
    ("ops.time.now_utc", "ops.time.clock.now_utc"),
    ("ops.proc.exec", "ops.proc.command.exec"),
)


def _iter_files(path: Path):
    if path.is_file():
        if path.suffix == ".md":
            yield path
        return
    if path.is_dir():
        for p in sorted(path.rglob("*.md")):
            if p.is_file():
                yield p


def _rewrite(text: str) -> str:
    out = text
    for old, new in MAPPINGS:
        out = out.replace(old, new)
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Rewrite legacy ops symbol names to deep-dot canonical form.")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    ap.add_argument("paths", nargs="+", help="file or directory paths")
    ns = ap.parse_args(argv)

    changed: list[Path] = []
    for raw in ns.paths:
        p = Path(raw)
        for f in _iter_files(p):
            original = f.read_text(encoding="utf-8")
            updated = _rewrite(original)
            if updated != original:
                changed.append(f)
                if ns.write:
                    f.write_text(updated, encoding="utf-8")

    if ns.check:
        if changed:
            for f in changed:
                print(f"{f.as_posix()}: ops symbol normalization drift")
            return 1
        print("OK: ops symbols are canonical")
        return 0

    print(f"OK: rewrote {len(changed)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

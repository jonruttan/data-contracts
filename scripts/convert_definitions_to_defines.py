#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


_FENCE_RE = re.compile(r"```yaml contract-spec\n(.*?)\n```", re.DOTALL)
_DEFINITIONS_KEY_RE = re.compile(r"^(\s*)definitions:\s*$", re.MULTILINE)


def _iter_files(path: Path):
    if path.is_file():
        if path.suffix == ".md":
            yield path
        return
    if path.is_dir():
        for p in sorted(path.rglob("*.md")):
            if p.is_file():
                yield p


def _rewrite_block(block: str) -> str:
    if "type: spec_lang.export" not in block:
        return block
    updated = _DEFINITIONS_KEY_RE.sub(r"\1defines:", block)
    updated = updated.replace("definitions.public", "defines.public")
    updated = updated.replace("definitions.private", "defines.private")
    return updated


def _rewrite(text: str) -> str:
    out: list[str] = []
    last = 0
    for match in _FENCE_RE.finditer(text):
        out.append(text[last : match.start(1)])
        out.append(_rewrite_block(match.group(1)))
        last = match.end(1)
    out.append(text[last:])
    return "".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Convert legacy `definitions` key to `defines` in spec_lang.export yaml contract-spec blocks."
    )
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
                print(f"{f.as_posix()}: definitions->defines drift")
            return 1
        print("OK: defines key format is canonical")
        return 0

    print(f"OK: rewrote {len(changed)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

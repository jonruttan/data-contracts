#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

import yaml


_FENCE_RE = re.compile(r"```yaml contract-spec\n(.*?)\n```", re.DOTALL)


def _iter_files(path: Path):
    if path.is_file():
        if path.suffix == ".md":
            yield path
        return
    if path.is_dir():
        for p in sorted(path.rglob("*.md")):
            if p.is_file():
                yield p


def _migrate_block(block: str) -> tuple[str, bool]:
    try:
        doc = yaml.safe_load(block)
    except Exception:
        return block, False
    if not isinstance(doc, dict):
        return block, False

    harness = doc.get("harness")
    if not isinstance(harness, dict):
        return block, False
    chain = harness.get("chain")
    if not isinstance(chain, dict):
        return block, False
    if "exports" not in chain:
        return block, False
    if "exports" in harness:
        # Hard-cut migration: if both exist already, leave unchanged.
        return block, False

    harness["exports"] = chain.pop("exports")
    if not chain:
        harness.pop("chain", None)
    updated = yaml.safe_dump(doc, sort_keys=False).rstrip("\n")
    return updated, True


def _rewrite(text: str) -> tuple[str, bool]:
    out: list[str] = []
    last = 0
    changed = False
    for match in _FENCE_RE.finditer(text):
        out.append(text[last : match.start(1)])
        migrated, did_change = _migrate_block(match.group(1))
        out.append(migrated)
        changed = changed or did_change
        last = match.end(1)
    out.append(text[last:])
    return "".join(out), changed


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Move harness.exports to harness.exports in yaml contract-spec blocks."
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
            updated, did_change = _rewrite(original)
            if did_change:
                changed.append(f)
                if ns.write:
                    f.write_text(updated, encoding="utf-8")

    if ns.check:
        if changed:
            for f in changed:
                print(f"{f.as_posix()}: harness.exports drift")
            return 1
        print("OK: harness exports location is canonical")
        return 0

    print(f"OK: rewrote {len(changed)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

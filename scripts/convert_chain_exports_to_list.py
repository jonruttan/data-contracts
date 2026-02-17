#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

import yaml


_FENCE = re.compile(r"```yaml spec-test\n(.*?)\n```", re.DOTALL)


def _iter_files(path: Path):
    if path.is_file():
        if path.suffix == ".md":
            yield path
        return
    if path.is_dir():
        for p in sorted(path.rglob("*.md")):
            if p.is_file():
                yield p


def _dump_case(case: dict[str, Any]) -> str:
    return yaml.safe_dump(case, sort_keys=False, allow_unicode=False).rstrip("\n")


def _convert_exports(raw_exports: Any) -> tuple[Any, bool]:
    if not isinstance(raw_exports, dict):
        return raw_exports, False
    out: list[dict[str, Any]] = []
    for export_name, export_raw in raw_exports.items():
        if not isinstance(export_raw, dict):
            out.append(
                {
                    "as": str(export_name),
                    "from": "",
                    "required": True,
                }
            )
            continue
        row: dict[str, Any] = {
            "as": str(export_name),
            "from": export_raw.get("from", ""),
            "required": export_raw.get("required", True),
        }
        if "path" in export_raw:
            row["path"] = export_raw.get("path")
        out.append(row)
    return out, True


def _convert_case(case: dict[str, Any]) -> bool:
    harness = case.get("harness")
    if not isinstance(harness, dict):
        return False
    chain = harness.get("chain")
    if not isinstance(chain, dict):
        return False
    steps = chain.get("steps")
    if not isinstance(steps, list):
        return False
    changed = False
    for step in steps:
        if not isinstance(step, dict):
            continue
        converted, did = _convert_exports(step.get("exports"))
        if did:
            step["exports"] = converted
            changed = True
    return changed


def _rewrite(text: str) -> tuple[str, bool]:
    cursor = 0
    out: list[str] = []
    changed = False
    for m in _FENCE.finditer(text):
        out.append(text[cursor:m.start()])
        raw_block = m.group(1)
        try:
            case = yaml.safe_load(raw_block)
        except Exception:
            out.append(m.group(0))
            cursor = m.end()
            continue
        if not isinstance(case, dict):
            out.append(m.group(0))
            cursor = m.end()
            continue
        if _convert_case(case):
            changed = True
            out.append("```yaml spec-test\n" + _dump_case(case) + "\n```")
        else:
            out.append(m.group(0))
        cursor = m.end()
    out.append(text[cursor:])
    return "".join(out), changed


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Convert harness.chain.steps[*].exports mapping form to list form.")
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
            if did_change and updated != original:
                changed.append(f)
                if ns.write:
                    f.write_text(updated, encoding="utf-8")

    if ns.check:
        if changed:
            for f in changed:
                print(f"{f.as_posix()}: chain exports list migration drift")
            return 1
        print("OK: chain exports use list form")
        return 0
    print(f"OK: rewrote {len(changed)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


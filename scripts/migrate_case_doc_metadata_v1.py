#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

import yaml

FENCE_RE = re.compile(r"```yaml contract-spec\n(.*?)\n```", re.DOTALL)


def _doc_stub(case_id: str, case_type: str) -> dict[str, Any]:
    return {
        "summary": f"Case `{case_id}` for `{case_type}`.",
        "description": "Auto-generated root doc metadata stub. Replace with authored reference text.",
        "audience": "spec-authors",
        "since": "v1",
        "tags": [case_type],
        "see_also": [],
    }


def _update_case(case: dict[str, Any]) -> bool:
    if str(case.get("type", "")).strip() != "contract.export":
        return False
    raw_doc = case.get("doc")
    if isinstance(raw_doc, dict):
        return False
    case_id = str(case.get("id", "")).strip() or "<case>"
    case_type = str(case.get("type", "")).strip() or "contract.export"
    case["doc"] = _doc_stub(case_id, case_type)
    return True


def _dump_case(case: dict[str, Any]) -> str:
    return yaml.safe_dump(case, sort_keys=False, allow_unicode=False).rstrip()


def _migrate_file(path: Path, *, check: bool) -> tuple[bool, str]:
    text = path.read_text(encoding="utf-8")
    changed = False

    def repl(match: re.Match[str]) -> str:
        nonlocal changed
        block = match.group(1)
        parsed = yaml.safe_load(block)
        if not isinstance(parsed, dict):
            return match.group(0)
        if not _update_case(parsed):
            return match.group(0)
        changed = True
        return "```yaml contract-spec\n" + _dump_case(parsed) + "\n```"

    updated = FENCE_RE.sub(repl, text)
    if changed and not check:
        path.write_text(updated, encoding="utf-8")
    return changed, path.as_posix()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Populate v1 root doc metadata for contract.export cases.")
    ap.add_argument("--root", default="specs")
    ap.add_argument("--check", action="store_true")
    ns = ap.parse_args(argv)

    root = Path(ns.root)
    if not root.exists():
        print(f"ERROR: missing root: {root}")
        return 2

    changed_files: list[str] = []
    for path in sorted(root.rglob("*.spec.md")):
        changed, label = _migrate_file(path, check=bool(ns.check))
        if changed:
            changed_files.append(label)

    if ns.check:
        if changed_files:
            print("metadata migration required:")
            for label in changed_files:
                print(f"- {label}")
            return 1
        print("OK: root doc metadata is current")
        return 0

    if changed_files:
        print("updated files:")
        for label in changed_files:
            print(f"- {label}")
    else:
        print("no changes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

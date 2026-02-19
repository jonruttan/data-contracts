#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

import yaml

FENCE_RE = re.compile(r"```yaml contract-spec\n(.*?)\n```", re.DOTALL)


def _library_meta_for(path: Path) -> dict[str, Any]:
    rel = path.as_posix()
    parts = rel.split("/")
    module = parts[2] if len(parts) > 3 else "general"
    stem = path.stem.replace(".spec", "")
    suffix = stem.replace("_", ".")
    return {
        "id": f"{module}.{suffix}",
        "module": module,
        "stability": "alpha",
        "owner": "spec_runner",
        "tags": [module],
    }


def _doc_stub(symbol: str, params: list[str]) -> dict[str, Any]:
    input_payload = {name: f"<{name}>" for name in params}
    return {
        "summary": f"Contract export for `{symbol}`.",
        "description": "Auto-generated metadata stub. Replace with authored reference text.",
        "params": [
            {
                "name": name,
                "type": "any",
                "required": True,
                "description": f"Input parameter `{name}`.",
            }
            for name in params
        ],
        "returns": {
            "type": "any",
            "description": "Result payload for this symbol.",
        },
        "errors": [
            {
                "code": "SCHEMA_ERROR",
                "when": "Input payload does not satisfy contract shape requirements.",
                "category": "schema",
            }
        ],
        "examples": [
            {
                "title": "Basic usage",
                "input": input_payload,
                "expected": "<result>",
                "notes": "Replace with a concrete scenario.",
            }
        ],
        "portability": {
            "python": True,
            "php": True,
            "rust": True,
            "notes": "Confirm per-runtime behavior and caveats.",
        },
        "see_also": [],
        "since": "v1",
    }


def _update_case(case: dict[str, Any], *, path: Path) -> bool:
    if str(case.get("type", "")).strip() != "contract.export":
        return False
    changed = False
    if not isinstance(case.get("library"), dict):
        case["library"] = _library_meta_for(path)
        changed = True

    harness = case.get("harness")
    if not isinstance(harness, dict):
        return changed
    exports = harness.get("exports")
    if not isinstance(exports, list):
        return changed

    for exp in exports:
        if not isinstance(exp, dict):
            continue
        if isinstance(exp.get("doc"), dict):
            continue
        params = exp.get("params")
        pnames = [str(x).strip() for x in params] if isinstance(params, list) else []
        symbol = str(exp.get("as", "")).strip() or "<symbol>"
        exp["doc"] = _doc_stub(symbol, pnames)
        changed = True
    return changed


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
        if not _update_case(parsed, path=path):
            return match.group(0)
        changed = True
        return "```yaml contract-spec\n" + _dump_case(parsed) + "\n```"

    updated = FENCE_RE.sub(repl, text)
    if changed and not check:
        path.write_text(updated, encoding="utf-8")
    return changed, path.as_posix()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Populate v1 library/doc metadata for contract.export cases.")
    ap.add_argument("--root", default="specs/libraries")
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
        print("OK: library metadata is current")
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

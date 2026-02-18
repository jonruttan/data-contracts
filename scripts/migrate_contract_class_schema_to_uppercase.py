#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
FENCE_RE = re.compile(r"```yaml contract-spec\n(.*?)\n```", re.DOTALL)
DEFAULT_PATHS = [
    "docs/spec",
    "docs/book",
    "README.md",
    "docs/development.md",
]

CLASS_MAP = {"must": "MUST", "can": "MAY", "cannot": "MUST_NOT"}
GROUP_KEYS = ("must", "can", "cannot", "MUST", "MAY", "MUST_NOT")
GROUP_MAP = {"must": "MUST", "can": "MAY", "cannot": "MUST_NOT"}


def _load_yaml(payload: str) -> dict[str, Any] | None:
    try:
        data = yaml.safe_load(payload)
    except Exception:
        return None
    return data if isinstance(data, dict) else None


def _dump_yaml(data: dict[str, Any]) -> str:
    return yaml.safe_dump(data, sort_keys=False).rstrip("\n")


def _is_step_form(node: Any) -> bool:
    return (
        isinstance(node, dict)
        and "id" in node
        and "class" in node
        and "asserts" in node
        and isinstance(node.get("asserts"), list)
    )


def _migrate_contract_node(node: Any) -> tuple[Any, bool]:
    changed = False
    if isinstance(node, list):
        out: list[Any] = []
        for child in node:
            migrated, child_changed = _migrate_contract_node(child)
            out.append(migrated)
            changed = changed or child_changed
        return out, changed

    if not isinstance(node, dict):
        return node, False

    if _is_step_form(node):
        out = dict(node)
        class_raw = str(out.get("class", "")).strip()
        mapped = CLASS_MAP.get(class_raw)
        if mapped is not None:
            out["class"] = mapped
            changed = True
        asserts = out.get("asserts")
        migrated_asserts, asserts_changed = _migrate_contract_node(asserts)
        out["asserts"] = migrated_asserts
        changed = changed or asserts_changed
        return out, changed

    present_groups = [k for k in GROUP_KEYS if k in node]
    if present_groups:
        out: dict[str, Any] = {}
        for key, value in node.items():
            key_str = str(key)
            mapped_key = GROUP_MAP.get(key_str, key_str)
            if mapped_key != key_str:
                changed = True
            if mapped_key in {"MUST", "MAY", "MUST_NOT"} and isinstance(value, list):
                migrated_value, child_changed = _migrate_contract_node(value)
                out[mapped_key] = migrated_value
                changed = changed or child_changed
            else:
                out[mapped_key] = value
        return out, changed

    # Expression mapping or non-contract object; leave untouched.
    return node, False


def _migrate_case(case: dict[str, Any]) -> tuple[dict[str, Any], bool]:
    changed = False
    if "contract" in case:
        migrated, sub_changed = _migrate_contract_node(case.get("contract"))
        if sub_changed:
            case["contract"] = migrated
            changed = True
    return case, changed


def migrate_file(path: Path, *, write: bool) -> bool:
    raw = path.read_text(encoding="utf-8")
    changed_any = False

    def repl(m: re.Match[str]) -> str:
        nonlocal changed_any
        payload = m.group(1)
        case = _load_yaml(payload)
        if case is None:
            return m.group(0)
        migrated, changed = _migrate_case(case)
        if not changed:
            return m.group(0)
        changed_any = True
        return "```yaml contract-spec\n" + _dump_yaml(migrated) + "\n```"

    updated = FENCE_RE.sub(repl, raw)
    if changed_any and write:
        path.write_text(updated, encoding="utf-8")
    return changed_any


def _collect_files(paths: list[str]) -> list[Path]:
    files: list[Path] = []
    for p in paths:
        target = Path(p)
        if not target.is_absolute():
            target = (ROOT / p).resolve()
        if target.is_file() and target.suffix == ".md":
            files.append(target)
        elif target.is_dir():
            files.extend(sorted(x for x in target.rglob("*.md") if x.is_file()))
    return files


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", default=DEFAULT_PATHS)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--write", action="store_true")
    ns = ap.parse_args()
    if ns.check == ns.write:
        ap.error("choose exactly one of --check or --write")

    files = _collect_files(ns.paths)
    changed_files: list[Path] = []
    for path in files:
        if migrate_file(path, write=ns.write):
            changed_files.append(path)

    if ns.check:
        if changed_files:
            for path in changed_files:
                print(f"NEEDS_CLASS_SCHEMA_MIGRATION: {path.relative_to(ROOT).as_posix()}")
            return 1
        print("OK: contract class schema already uppercase")
        return 0

    print(f"OK: rewrote {len(changed_files)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

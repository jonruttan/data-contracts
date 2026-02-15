#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml

from spec_runner.settings import SETTINGS
from spec_runner.spec_lang_yaml_ast import is_sexpr_node, sexpr_to_yaml_ast


def _is_yaml_opening_fence(line: str) -> tuple[str, int] | None:
    stripped = line.lstrip(" \t")
    if not stripped:
        return None
    if stripped[0] not in ("`", "~"):
        return None
    ch = stripped[0]
    i = 0
    while i < len(stripped) and stripped[i] == ch:
        i += 1
    if i < 3:
        return None
    info = stripped[i:].strip().lower().split()
    if "yaml" not in info and "yml" not in info:
        return None
    return ch, i


def _is_closing_fence(line: str, *, ch: str, min_len: int) -> bool:
    stripped = line.lstrip(" \t").rstrip()
    if not stripped or stripped[0] != ch:
        return False
    i = 0
    while i < len(stripped) and stripped[i] == ch:
        i += 1
    return i >= min_len and i == len(stripped)


def _convert_expr_list_value(raw: Any) -> list[Any]:
    if is_sexpr_node(raw):
        return [sexpr_to_yaml_ast(raw)]
    if isinstance(raw, list):
        return [sexpr_to_yaml_ast(item) if is_sexpr_node(item) else item for item in raw]
    return [sexpr_to_yaml_ast(raw)]


def _walk_convert(node: Any) -> tuple[Any, bool]:
    changed = False
    if isinstance(node, list):
        out: list[Any] = []
        for x in node:
            got, ch = _walk_convert(x)
            out.append(got)
            changed = changed or ch
        return out, changed
    if isinstance(node, dict):
        out: dict[str, Any] = {}
        for k, v in node.items():
            key = str(k)
            if key in {"evaluate", "policy_evaluate"}:
                converted = _convert_expr_list_value(v)
                items: list[Any] = []
                for x in converted:
                    got, ch = _walk_convert(x)
                    items.append(got)
                    changed = changed or ch
                out[key] = items
                changed = changed or (converted != v)
            else:
                got, ch = _walk_convert(v)
                out[key] = got
                changed = changed or ch
        return out, changed
    return node, False


def _yaml_dump(payload: Any) -> str:
    return yaml.dump(payload, sort_keys=False, allow_unicode=False, width=1000)


def convert_markdown(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    while i < len(lines):
        opening = _is_yaml_opening_fence(lines[i])
        if not opening:
            out.append(lines[i])
            i += 1
            continue
        ch, fence_len = opening
        out.append(lines[i])
        i += 1
        block_lines: list[str] = []
        while i < len(lines) and not _is_closing_fence(lines[i], ch=ch, min_len=fence_len):
            block_lines.append(lines[i])
            i += 1
        if i >= len(lines):
            out.extend(block_lines)
            break
        block = "".join(block_lines)
        try:
            payload = yaml.safe_load(block)
        except yaml.YAMLError:
            out.append(block)
            out.append(lines[i])
            i += 1
            continue
        converted, changed = _walk_convert(payload)
        out.append(_yaml_dump(converted) if changed else block)
        out.append(lines[i])
        i += 1
    return "".join(out)


def convert_yaml_text(text: str) -> str:
    payload = yaml.safe_load(text)
    converted, changed = _walk_convert(payload)
    return _yaml_dump(converted) if changed else text


def _iter_files(paths: list[Path], *, pattern: str) -> list[Path]:
    out: list[Path] = []
    for p in paths:
        if p.is_file():
            out.append(p)
            continue
        if not p.exists():
            continue
        out.extend(sorted(x for x in p.rglob(pattern) if x.is_file()))
    seen: set[Path] = set()
    uniq: list[Path] = []
    for p in out:
        rp = p.resolve()
        if rp in seen:
            continue
        seen.add(rp)
        uniq.append(p)
    return uniq


def _convert_file(path: Path) -> tuple[bool, str]:
    if path.as_posix().endswith("docs/spec/schema/normalization_profile_v1.yaml"):
        return False, path.read_text(encoding="utf-8")
    original = path.read_text(encoding="utf-8")
    lower = path.name.lower()
    if lower.endswith(".md"):
        updated = convert_markdown(original)
    elif lower.endswith(".yaml") or lower.endswith(".yml"):
        updated = convert_yaml_text(original)
    else:
        return False, original
    return updated != original, updated


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Convert spec-lang YAML list s-expr syntax to mapping AST form")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="fail when files require conversion")
    mode.add_argument("--write", action="store_true", help="rewrite files in place")
    ap.add_argument("--pattern", default=SETTINGS.case.default_file_pattern, help="case-file glob for markdown discovery")
    ap.add_argument("paths", nargs="*", default=["docs/spec", "docs/book", "tests"], help="paths to scan")
    ns = ap.parse_args(argv)

    files = _iter_files([Path(x) for x in ns.paths], pattern="*.md")
    files.extend(_iter_files([Path(x) for x in ns.paths], pattern="*.yaml"))
    files.extend(_iter_files([Path(x) for x in ns.paths], pattern="*.yml"))
    uniq: list[Path] = []
    seen: set[Path] = set()
    for p in files:
        rp = p.resolve()
        if rp in seen:
            continue
        seen.add(rp)
        uniq.append(p)

    changed: list[Path] = []
    for p in uniq:
        was_changed, updated = _convert_file(p)
        if was_changed:
            changed.append(p)
            if ns.write:
                p.write_text(updated, encoding="utf-8")

    if ns.check:
        if changed:
            for p in changed:
                print(f"NEEDS_CONVERSION: {p.as_posix()}")
            return 1
        print("OK: mapping AST conversion is canonical")
        return 0

    print(f"converted {len(changed)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

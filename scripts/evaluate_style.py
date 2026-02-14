#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import yaml

from spec_runner.settings import SETTINGS

class _StyleDumper(yaml.SafeDumper):
    def increase_indent(self, flow: bool = False, indentless: bool = False):  # type: ignore[override]
        return super().increase_indent(flow, False)


class _ExprPlaceholder(str):
    """Marker scalar for post-dump evaluate expression injection."""


class _BlockSeq(list):
    """Marker sequence forced to block style."""


def _repr_placeholder(dumper: yaml.SafeDumper, data: _ExprPlaceholder):
    return dumper.represent_scalar("tag:yaml.org,2002:str", str(data), style='"')


_StyleDumper.add_representer(_ExprPlaceholder, _repr_placeholder)


def _repr_block_seq(dumper: yaml.SafeDumper, data: _BlockSeq):
    return dumper.represent_sequence("tag:yaml.org,2002:seq", data, flow_style=False)


_StyleDumper.add_representer(_BlockSeq, _repr_block_seq)


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


def _format_expr_atom(node: Any) -> str:
    if isinstance(node, str):
        return json.dumps(node)
    if isinstance(node, bool):
        return "true" if node else "false"
    if node is None:
        return "null"
    if isinstance(node, (int, float)):
        return str(node)
    raise TypeError(f"unsupported expression atom type: {type(node).__name__}")


def _format_expr_single_line(node: Any) -> str:
    if isinstance(node, list):
        return "[" + ", ".join(_format_expr_single_line(x) for x in node) + "]"
    return _format_expr_atom(node)


def _format_expr(node: Any, *, indent: int, width: int) -> str:
    one_line = _format_expr_single_line(node)
    if "\n" not in one_line and indent + len(one_line) <= width:
        return one_line
    if not isinstance(node, list):
        return one_line
    if not node:
        return "[]"

    first = _format_expr(node[0], indent=indent + 1, width=width)
    first_lines = first.splitlines()
    if len(first_lines) == 1:
        lines: list[str] = [f"[{first_lines[0]}"]
    else:
        lines = [f"[{first_lines[0]}"]
        for extra in first_lines[1:]:
            lines.append((" " * (indent + 1)) + extra)
    if len(node) > 1:
        lines[-1] = lines[-1] + ","

    for i, item in enumerate(node[1:]):
        item_is_last = i == len(node[1:]) - 1
        rendered = _format_expr(item, indent=indent + 1, width=width)
        rendered_lines = rendered.splitlines()
        if rendered_lines:
            rendered_lines[0] = (" " * (indent + 1)) + rendered_lines[0]
            for j in range(1, len(rendered_lines)):
                rendered_lines[j] = (" " * (indent + 1)) + rendered_lines[j]
            if not item_is_last:
                rendered_lines[-1] = rendered_lines[-1] + ","
            lines.extend(rendered_lines)
    lines[-1] = lines[-1] + "]"
    return "\n".join(lines)


def _normalize_evaluate_nodes(node: Any, expr_map: dict[str, str]) -> Any:
    if isinstance(node, dict):
        out: dict[str, Any] = {}
        for k, v in node.items():
            if k == "evaluate" and isinstance(v, list):
                formatted: _BlockSeq = _BlockSeq()
                for idx, item in enumerate(v):
                    if isinstance(item, list):
                        placeholder = f"__EVALUATE_EXPR_{len(expr_map)}_{idx}__"
                        expr_map[placeholder] = _format_expr(item, indent=0, width=60)
                        formatted.append(_ExprPlaceholder(placeholder))
                    else:
                        formatted.append(_normalize_evaluate_nodes(item, expr_map))
                out[k] = formatted
            else:
                out[k] = _normalize_evaluate_nodes(v, expr_map)
        return out
    if isinstance(node, list):
        return [_normalize_evaluate_nodes(x, expr_map) for x in node]
    return node


def _contains_evaluate(node: Any) -> bool:
    if isinstance(node, dict):
        if "evaluate" in node:
            return True
        return any(_contains_evaluate(v) for v in node.values())
    if isinstance(node, list):
        return any(_contains_evaluate(x) for x in node)
    return False


def _format_yaml_block(block: str) -> str:
    payload = yaml.safe_load(block)
    if payload is None:
        return block.strip() + "\n"
    if not _contains_evaluate(payload):
        return block
    expr_map: dict[str, str] = {}
    normalized = _normalize_evaluate_nodes(payload, expr_map)
    rendered = yaml.dump(
        normalized,
        Dumper=_StyleDumper,
        sort_keys=False,
        allow_unicode=False,
        width=1000,
        default_flow_style=None,
    )
    if not expr_map:
        return rendered

    lines = rendered.splitlines(keepends=False)
    out_lines: list[str] = []
    placeholder_re = re.compile(r'^(?P<indent>\s*-\s+)"(?P<ph>__EVALUATE_EXPR_[^"]+__)"\s*$')
    for line in lines:
        m = placeholder_re.match(line)
        if not m:
            out_lines.append(line)
            continue
        indent = m.group("indent")
        ph = m.group("ph")
        expr = expr_map.get(ph)
        if expr is None:
            out_lines.append(line)
            continue
        expr_lines = expr.splitlines()
        if not expr_lines:
            out_lines.append(line)
            continue
        out_lines.append(f"{indent}{expr_lines[0]}")
        continuation_indent = " " * len(indent)
        for rest in expr_lines[1:]:
            out_lines.append(f"{continuation_indent}{rest}")
    return "\n".join(out_lines) + "\n"


def format_spec_markdown(text: str) -> str:
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
            formatted = _format_yaml_block(block)
        except yaml.YAMLError:
            formatted = block
        out.append(formatted)
        out.append(lines[i])
        i += 1
    return "".join(out)


def _iter_case_files(paths: list[Path], *, pattern: str) -> list[Path]:
    out: list[Path] = []
    for p in paths:
        if p.is_file():
            if p.match(pattern):
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


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Lint/format evaluate expression layout inside yaml spec-test blocks.",
    )
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="fail if files need formatting")
    mode.add_argument("--write", action="store_true", help="rewrite files in place")
    ap.add_argument(
        "--pattern",
        default=SETTINGS.case.default_file_pattern,
        help="Case doc filename glob (default from settings)",
    )
    ap.add_argument(
        "paths",
        nargs="*",
        default=["docs/spec"],
        help="Files or directories to process",
    )
    ns = ap.parse_args(argv)

    files = _iter_case_files([Path(x) for x in ns.paths], pattern=str(ns.pattern))
    changed: list[Path] = []
    for p in files:
        original = p.read_text(encoding="utf-8")
        updated = format_spec_markdown(original)
        if updated != original:
            changed.append(p)
            if ns.write:
                p.write_text(updated, encoding="utf-8")

    if ns.check:
        if changed:
            for p in changed:
                print(f"NEEDS_FORMAT: {p.as_posix()}")
            return 1
        print("OK: evaluate style formatting is canonical")
        return 0

    print(f"formatted {len(changed)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml

from spec_runner.settings import SETTINGS
from spec_runner.spec_lang_yaml_ast import (
    SpecLangYamlAstError,
    compile_yaml_expr_to_sexpr,
    compile_yaml_expr_list,
    is_sexpr_node,
    sexpr_to_yaml_ast,
)

_COMPACT_MAX_ITEMS = 4


class _FlowSeq(list):
    pass


class _FlowMap(dict):
    pass


class _CompactDumper(yaml.SafeDumper):
    pass


def _flow_seq_representer(dumper: yaml.Dumper, data: _FlowSeq) -> yaml.nodes.SequenceNode:
    return dumper.represent_sequence("tag:yaml.org,2002:seq", list(data), flow_style=True)


def _flow_map_representer(dumper: yaml.Dumper, data: _FlowMap) -> yaml.nodes.MappingNode:
    return dumper.represent_mapping("tag:yaml.org,2002:map", dict(data), flow_style=True)


_CompactDumper.add_representer(_FlowSeq, _flow_seq_representer)
_CompactDumper.add_representer(_FlowMap, _flow_map_representer)


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
    if "spec-test" not in info:
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
        out: list[Any] = []
        for item in raw:
            out.append(sexpr_to_yaml_ast(item) if is_sexpr_node(item) else item)
        return out
    return [sexpr_to_yaml_ast(raw)]


def _is_scalar(node: Any) -> bool:
    return isinstance(node, (str, int, float, bool)) or node is None


def _is_compact_atom(node: Any, *, depth: int = 0) -> bool:
    if _is_scalar(node):
        return True
    if depth > 2:
        return False
    if isinstance(node, (list, _FlowSeq)):
        if len(node) > _COMPACT_MAX_ITEMS:
            return False
        return all(_is_compact_atom(x, depth=depth + 1) for x in node)
    if isinstance(node, (dict, _FlowMap)):
        if len(node) != 1:
            return False
        key = next(iter(node.keys()))
        if not isinstance(key, str):
            return False
        value = next(iter(node.values()))
        return _is_compact_atom(value, depth=depth + 1)
    return False


def _wrap_flow_literal(node: Any) -> Any:
    if isinstance(node, list):
        items = [_wrap_flow_literal(x) for x in node]
        if len(items) <= _COMPACT_MAX_ITEMS and all(_is_compact_atom(x, depth=1) for x in items):
            return _FlowSeq(items)
        return items
    if isinstance(node, dict):
        wrapped = {str(k): _wrap_flow_literal(v) for k, v in node.items()}
        if len(wrapped) <= _COMPACT_MAX_ITEMS and all(_is_compact_atom(v, depth=1) for v in wrapped.values()):
            return _FlowMap(wrapped)
        return wrapped
    return node


def _condense_expr_node(node: Any) -> Any:
    if _is_scalar(node):
        return node
    if isinstance(node, list):
        return [_condense_expr_node(x) for x in node]
    if isinstance(node, dict):
        if "lit" in node and len(node) == 1:
            return _FlowMap({"lit": _wrap_flow_literal(node["lit"])})
        if len(node) == 1:
            op = str(next(iter(node.keys())))
            raw_args = node[op]
            if op == "ref":
                # Legacy form rewrite: {var: subject} -> {var: subject}
                return _FlowMap({"var": "subject"})
            if op == "var":
                if isinstance(raw_args, list) and len(raw_args) == 1 and isinstance(raw_args[0], str):
                    return _FlowMap({"var": raw_args[0]})
                if isinstance(raw_args, str):
                    return _FlowMap({"var": raw_args})
                return {"var": _condense_expr_node(raw_args)}
            if op == "fn" and isinstance(raw_args, list) and len(raw_args) == 2:
                params = raw_args[0]
                if isinstance(params, dict) and "lit" in params and isinstance(params["lit"], list):
                    params = params["lit"]
                elif isinstance(params, dict) and len(params) == 1:
                    k = str(next(iter(params.keys())))
                    v = params[k]
                    if isinstance(v, list) and not v and k.strip():
                        params = [k.strip()]
                if (
                    isinstance(params, list)
                    and all(isinstance(x, str) and str(x).strip() for x in params)
                ):
                    body = _condense_expr_node(raw_args[1])
                    return {"fn": [_FlowSeq([str(x).strip() for x in params]), body]}
            if isinstance(raw_args, list):
                if op == "subject" and not raw_args:
                    return _FlowMap({"var": "subject"})
                args = [_condense_expr_node(x) for x in raw_args]
                if len(args) <= _COMPACT_MAX_ITEMS and all(_is_compact_atom(x, depth=1) for x in args):
                    return _FlowMap({op: _FlowSeq(args)})
                return {op: args}
        return {str(k): _condense_expr_node(v) for k, v in node.items()}
    return node


def _walk_convert(node: Any, *, path: str = "") -> tuple[Any, bool]:
    changed = False
    if isinstance(node, list):
        out: list[Any] = []
        for idx, x in enumerate(node):
            got, ch = _walk_convert(x, path=f"{path}[{idx}]")
            out.append(got)
            changed = changed or ch
        return out, changed
    if isinstance(node, dict):
        out: dict[str, Any] = {}
        for k, v in node.items():
            key = str(k)
            if key in {"evaluate", "policy_evaluate"}:
                converted = _convert_expr_list_value(v)
                out_items: list[Any] = []
                for idx, expr in enumerate(converted):
                    item, ch = _walk_convert(expr, path=f"{path}.{key}[{idx}]")
                    out_items.append(_condense_expr_node(item))
                    changed = changed or ch
                out[key] = out_items
                changed = changed or (converted != v)
            elif key == "functions" and isinstance(v, dict):
                functions: dict[str, Any] = {}
                for fn_name, fn_expr in v.items():
                    fn_path = f"{path}.{key}.{fn_name}" if path else f"{key}.{fn_name}"
                    expr_node = sexpr_to_yaml_ast(fn_expr) if is_sexpr_node(fn_expr) else fn_expr
                    fn_item, ch = _walk_convert(expr_node, path=fn_path)
                    functions[str(fn_name)] = _condense_expr_node(fn_item)
                    changed = changed or ch or (expr_node != fn_expr)
                out[key] = functions
            else:
                got, ch = _walk_convert(v, path=f"{path}.{key}")
                out[key] = got
                changed = changed or ch
        return out, changed
    return node, False


def _validate_expr_fields(node: Any, *, path: str = "") -> None:
    if isinstance(node, list):
        for idx, x in enumerate(node):
            _validate_expr_fields(x, path=f"{path}[{idx}]")
        return
    if isinstance(node, dict):
        for k, v in node.items():
            key = str(k)
            current = f"{path}.{key}" if path else key
            if key in {"evaluate", "policy_evaluate"}:
                if not isinstance(v, list) or not v:
                    raise SpecLangYamlAstError(f"{current}: expression list must be a non-empty list")
                compile_yaml_expr_list(v, field_path=current)
            if key == "functions":
                if not isinstance(v, dict):
                    raise SpecLangYamlAstError(f"{current}: functions must be a mapping")
                for fn_name, fn_expr in v.items():
                    compile_yaml_expr_to_sexpr(fn_expr, field_path=f"{current}.{fn_name}")
            _validate_expr_fields(v, path=current)


def _yaml_dump(payload: Any) -> str:
    return yaml.dump(payload, sort_keys=False, allow_unicode=False, width=1000, Dumper=_CompactDumper)


def _contains_expr_fields(node: Any) -> bool:
    if isinstance(node, list):
        return any(_contains_expr_fields(x) for x in node)
    if isinstance(node, dict):
        for k, v in node.items():
            key = str(k)
            if key in {"evaluate", "policy_evaluate", "functions"}:
                return True
            if _contains_expr_fields(v):
                return True
    return False


def _format_yaml_block(block: str) -> str:
    payload = yaml.safe_load(block)
    if payload is None:
        return block.strip() + "\n"
    if not _contains_expr_fields(payload):
        return block
    converted, _ = _walk_convert(payload)
    return _yaml_dump(converted)


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

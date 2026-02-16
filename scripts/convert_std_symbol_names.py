#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml

from spec_runner.settings import SETTINGS
from spec_runner.spec_lang_std_names import FLAT_TO_STD
from spec_runner.spec_lang_yaml_ast import (
    SpecLangYamlAstError,
    compile_yaml_expr_to_sexpr,
    sexpr_to_yaml_ast,
)


def _is_yaml_opening_fence(line: str) -> tuple[str, int] | None:
    stripped = line.lstrip(" \t")
    if not stripped or stripped[0] not in ("`", "~"):
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


def _rewrite_sexpr_ops(node: Any) -> Any:
    if isinstance(node, list):
        if node and isinstance(node[0], str):
            head = node[0]
            if head in FLAT_TO_STD:
                head = FLAT_TO_STD[head]
            if head == "fn" and len(node) >= 3:
                # fn parameter names are variables, not operator symbols.
                params = node[1]
                body = _rewrite_sexpr_ops(node[2])
                rest = [_rewrite_sexpr_ops(x) for x in node[3:]]
                return [head, params, body, *rest]
            return [head, *[_rewrite_sexpr_ops(x) for x in node[1:]]]
        return [_rewrite_sexpr_ops(x) for x in node]
    if isinstance(node, dict):
        return {str(k): _rewrite_sexpr_ops(v) for k, v in node.items()}
    return node


def _rewrite_expr_node(node: Any, *, field_path: str) -> Any:
    try:
        sexpr = compile_yaml_expr_to_sexpr(node, field_path=field_path)
    except SpecLangYamlAstError as exc:
        # Keep intentionally-invalid fixtures unchanged.
        _ = exc
        return node
    updated = _rewrite_sexpr_ops(sexpr)
    return sexpr_to_yaml_ast(updated)


def _rewrite_expr_list(raw: Any, *, field_path: str) -> list[Any]:
    if not isinstance(raw, list):
        raise ValueError(f"{field_path} must be a non-empty list")
    out: list[Any] = []
    for idx, item in enumerate(raw):
        out.append(_rewrite_expr_node(item, field_path=f"{field_path}[{idx}]"))
    return out


def _walk(node: Any, *, field_path: str = "$") -> tuple[Any, bool]:
    changed = False
    if isinstance(node, list):
        out = []
        for idx, item in enumerate(node):
            got, ch = _walk(item, field_path=f"{field_path}[{idx}]")
            out.append(got)
            changed = changed or ch
        return out, changed
    if isinstance(node, dict):
        out: dict[str, Any] = {}
        for raw_key, value in node.items():
            key = str(raw_key)
            if key in {"evaluate", "policy_evaluate"} and isinstance(value, list):
                rewritten = _rewrite_expr_list(value, field_path=f"{field_path}.{key}")
                out[key] = rewritten
                changed = changed or (rewritten != value)
                continue
            if key in {"public", "private"} and isinstance(value, dict) and field_path.endswith(".definitions"):
                rewritten_scope: dict[str, Any] = {}
                for sym, expr in value.items():
                    rewritten_scope[str(sym)] = _rewrite_expr_node(
                        expr, field_path=f"{field_path}.{key}.{sym}"
                    )
                out[key] = rewritten_scope
                changed = changed or (rewritten_scope != value)
                continue
            got, ch = _walk(value, field_path=f"{field_path}.{key}")
            out[key] = got
            changed = changed or ch
        return out, changed
    return node, False


def _yaml_dump(payload: Any) -> str:
    return yaml.dump(payload, sort_keys=False, allow_unicode=False, width=1000)


def _convert_markdown(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    while i < len(lines):
        opening = _is_yaml_opening_fence(lines[i])
        if not opening:
            out.append(lines[i])
            i += 1
            continue
        ch, min_len = opening
        out.append(lines[i])
        i += 1
        block_lines: list[str] = []
        while i < len(lines) and not _is_closing_fence(lines[i], ch=ch, min_len=min_len):
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
        rewritten, changed = _walk(payload)
        out.append(_yaml_dump(rewritten) if changed else block)
        out.append(lines[i])
        i += 1
    return "".join(out)


def _convert_yaml(text: str) -> str:
    payload = yaml.safe_load(text)
    rewritten, changed = _walk(payload)
    return _yaml_dump(rewritten) if changed else text


def _iter_files(paths: list[Path], pattern: str) -> list[Path]:
    out: list[Path] = []
    for p in paths:
        if p.is_file():
            out.append(p)
            continue
        if p.exists():
            out.extend(sorted(x for x in p.rglob(pattern) if x.is_file()))
    uniq: list[Path] = []
    seen: set[Path] = set()
    for p in out:
        rp = p.resolve()
        if rp in seen:
            continue
        seen.add(rp)
        uniq.append(p)
    return uniq


def _convert_file(path: Path) -> tuple[bool, str]:
    original = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".md":
        updated = _convert_markdown(original)
    elif path.suffix.lower() in {".yaml", ".yml"}:
        updated = _convert_yaml(original)
    else:
        return False, original
    return updated != original, updated


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Convert spec-lang expression operators to std.* names")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    ap.add_argument("--pattern", default=SETTINGS.case.default_file_pattern)
    ap.add_argument("paths", nargs="*", default=["docs/spec", "docs/book", "tests"])
    ns = ap.parse_args(argv)

    files = _iter_files([Path(x) for x in ns.paths], "*.md")
    files.extend(_iter_files([Path(x) for x in ns.paths], "*.yaml"))
    files.extend(_iter_files([Path(x) for x in ns.paths], "*.yml"))
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
                print(f"NEEDS_STD_NAMESPACE: {p.as_posix()}")
            return 1
        print("OK: std.* operator names are canonical")
        return 0

    print(f"converted {len(changed)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

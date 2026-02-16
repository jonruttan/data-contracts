#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml

from spec_runner.settings import SETTINGS
from spec_runner.virtual_paths import (
    VirtualPathError,
    contract_root_for,
    normalize_contract_path,
)


_EXACT_PATH_KEYS = {
    "path",
    "cases_path",
    "baseline_path",
    "manifest_path",
    "index_out",
    "coverage_out",
    "graph_out",
    "adapter_path",
    "cli_main_path",
    "required_library_path",
    "reference_manifest",
    "notes_path",
}
_LIST_PATH_KEYS = {"required_paths", "baseline_paths", "roots", "imports"}
_SKIP_ANCESTORS = {"setup_files", "request"}


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


def _normalize_path_string(raw: str, *, field: str, source_file: Path) -> tuple[str, bool]:
    s = str(raw).strip()
    if not s:
        return raw, False
    if "://" in s and not s.startswith("external://"):
        return raw, False
    if s.startswith("external://"):
        return raw, False
    normalized: str | None = None
    try:
        normalized = normalize_contract_path(s, field=field)
    except VirtualPathError:
        normalized = None

    if normalized is None and not s.startswith("/") and (s.startswith("./") or s.startswith("../")):
        root = contract_root_for(source_file)
        candidate = (source_file.parent / s).resolve()
        try:
            rel = candidate.relative_to(root.resolve())
        except ValueError:
            return raw, False
        normalized = "/" + rel.as_posix()

    if normalized is None:
        return raw, False
    return normalized, normalized != raw


def _walk(node: Any, *, source_file: Path, key_path: list[str] | None = None) -> tuple[Any, bool]:
    if key_path is None:
        key_path = []
    changed = False

    if isinstance(node, dict):
        out: dict[str, Any] = {}
        for k, v in node.items():
            key = str(k)
            next_path = [*key_path, key]
            if key in _EXACT_PATH_KEYS and isinstance(v, str):
                if not any(a in _SKIP_ANCESTORS for a in key_path):
                    nv, ch = _normalize_path_string(v, field=".".join(next_path), source_file=source_file)
                    out[key] = nv
                    changed = changed or ch
                    continue
            is_spec_lang_includes = key == "includes" and (
                key_path == ["harness", "spec_lang"]
                or key_path[-2:] == ["harness", "spec_lang"]
            )
            if (key in _LIST_PATH_KEYS or is_spec_lang_includes) and isinstance(v, list):
                items: list[Any] = []
                local_changed = False
                for idx, item in enumerate(v):
                    if isinstance(item, str):
                        ni, ch = _normalize_path_string(
                            item, field=f"{'.'.join(next_path)}[{idx}]", source_file=source_file
                        )
                        items.append(ni)
                        local_changed = local_changed or ch
                    else:
                        got, ch = _walk(item, source_file=source_file, key_path=next_path)
                        items.append(got)
                        local_changed = local_changed or ch
                out[key] = items
                changed = changed or local_changed
                continue
            got, ch = _walk(v, source_file=source_file, key_path=next_path)
            out[key] = got
            changed = changed or ch
        return out, changed

    if isinstance(node, list):
        out: list[Any] = []
        for item in node:
            got, ch = _walk(item, source_file=source_file, key_path=key_path)
            out.append(got)
            changed = changed or ch
        return out, changed

    return node, False


def _yaml_dump(payload: Any) -> str:
    return yaml.dump(payload, sort_keys=False, allow_unicode=False, width=1000)


def convert_markdown(text: str, *, source_file: Path) -> str:
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
        converted, changed = _walk(payload, source_file=source_file)
        out.append(_yaml_dump(converted) if changed else block)
        out.append(lines[i])
        i += 1
    return "".join(out)


def convert_yaml_text(text: str, *, source_file: Path) -> str:
    payload = yaml.safe_load(text)
    converted, changed = _walk(payload, source_file=source_file)
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
    original = path.read_text(encoding="utf-8")
    lower = path.name.lower()
    if lower.endswith(".md"):
        updated = convert_markdown(original, source_file=path)
    elif lower.endswith(".yaml") or lower.endswith(".yml"):
        updated = convert_yaml_text(original, source_file=path)
    else:
        return False, original
    return updated != original, updated


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Normalize path-bearing YAML fields to virtual-root canonical /... form")
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
                print(f"NEEDS_VIRTUAL_PATH_NORMALIZATION: {p.as_posix()}")
            return 1
        print("OK: virtual-root path conversion is canonical")
        return 0

    print(f"converted {len(changed)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

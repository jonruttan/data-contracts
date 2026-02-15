#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
PROFILE_PATH = ROOT / "docs/spec/schema/normalization_profile_v1.yaml"
_EXECUTABLE_CASE_TREE_ROOTS = (
    "docs/spec/conformance/cases",
    "docs/spec/governance/cases",
    "docs/spec/impl",
)
_NON_MD_SPEC_GLOBS = ("*.spec.yaml", "*.spec.yml", "*.spec.json")
_DATA_ARTIFACT_GLOBS = (
    "docs/spec/metrics/*.json",
    "docs/spec/metrics/*.yaml",
    "docs/book/reference_manifest.yaml",
    "docs/spec/schema/*.yaml",
)


def _load_profile(path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path}: profile must be a mapping")
    return payload


def _scope_paths(profile: dict[str, Any], scope: str) -> list[str]:
    paths = profile.get("paths")
    if not isinstance(paths, dict):
        raise ValueError("profile.paths must be a mapping")
    if scope == "all":
        keys = ("specs", "contracts", "tests")
    else:
        keys = (scope,)
    out: list[str] = []
    for key in keys:
        values = paths.get(key, [])
        if not isinstance(values, list):
            raise ValueError(f"profile.paths.{key} must be a list")
        for v in values:
            if isinstance(v, str) and v.strip():
                out.append(v.strip())
    return out


def _run(cmd: list[str]) -> tuple[int, str]:
    proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=False)
    stdout = (proc.stdout or "").strip()
    stderr = (proc.stderr or "").strip()
    merged = "\n".join(x for x in (stdout, stderr) if x)
    return int(proc.returncode), merged


def _line_for(text: str, token: str) -> int:
    if not token:
        return 1
    idx = text.find(token)
    if idx < 0:
        return 1
    return text[:idx].count("\n") + 1


def _check_docs_tokens(profile: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    token_sync = profile.get("docs_token_sync", {})
    if not isinstance(token_sync, dict):
        return ["docs/spec/schema/normalization_profile_v1.yaml:1: NORMALIZATION_PROFILE: docs_token_sync must be a mapping"]
    rules = token_sync.get("rules", [])
    if not isinstance(rules, list):
        return ["docs/spec/schema/normalization_profile_v1.yaml:1: NORMALIZATION_PROFILE: docs_token_sync.rules must be a list"]
    for rule in rules:
        if not isinstance(rule, dict):
            continue
        rule_id = str(rule.get("id", "NORMALIZATION_DOC_TOKEN_SYNC")).strip() or "NORMALIZATION_DOC_TOKEN_SYNC"
        rel = str(rule.get("file", "")).strip()
        if not rel:
            continue
        p = ROOT / rel
        if not p.exists():
            issues.append(f"{rel}:1: {rule_id}: missing file")
            continue
        text = p.read_text(encoding="utf-8")
        must = rule.get("must_contain", [])
        must_not = rule.get("must_not_contain", [])
        if isinstance(must, list):
            for tok in must:
                if isinstance(tok, str) and tok and tok not in text:
                    issues.append(f"{rel}:1: {rule_id}: missing token: {tok}")
        if isinstance(must_not, list):
            for tok in must_not:
                if isinstance(tok, str) and tok and tok in text:
                    line = _line_for(text, tok)
                    issues.append(f"{rel}:{line}: {rule_id}: forbidden token present: {tok}")
    return issues


def _apply_replacements(profile: dict[str, Any]) -> tuple[list[str], int]:
    changed = 0
    issues: list[str] = []
    repl = profile.get("replacements", {})
    if not isinstance(repl, dict):
        return (["docs/spec/schema/normalization_profile_v1.yaml:1: NORMALIZATION_PROFILE: replacements must be a mapping"], 0)
    rules = repl.get("rules", [])
    if not isinstance(rules, list):
        return (["docs/spec/schema/normalization_profile_v1.yaml:1: NORMALIZATION_PROFILE: replacements.rules must be a list"], 0)
    for rule in rules:
        if not isinstance(rule, dict):
            continue
        rule_id = str(rule.get("id", "NORMALIZATION_REPLACEMENT")).strip() or "NORMALIZATION_REPLACEMENT"
        rel = str(rule.get("file", "")).strip()
        if not rel:
            continue
        p = ROOT / rel
        if not p.exists():
            issues.append(f"{rel}:1: {rule_id}: missing file")
            continue
        edits = rule.get("edits", [])
        if not isinstance(edits, list):
            issues.append(f"{rel}:1: {rule_id}: edits must be a list")
            continue
        original = p.read_text(encoding="utf-8")
        updated = original
        for e in edits:
            if not isinstance(e, dict):
                continue
            old = e.get("old")
            new = e.get("new")
            if not isinstance(old, str) or not isinstance(new, str):
                continue
            updated = updated.replace(old, new)
        if updated != original:
            p.write_text(updated, encoding="utf-8")
            changed += 1
    return issues, changed


def _check_replacements_drift(profile: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    repl = profile.get("replacements", {})
    if not isinstance(repl, dict):
        return issues
    rules = repl.get("rules", [])
    if not isinstance(rules, list):
        return issues
    for rule in rules:
        if not isinstance(rule, dict):
            continue
        rule_id = str(rule.get("id", "NORMALIZATION_REPLACEMENT")).strip() or "NORMALIZATION_REPLACEMENT"
        rel = str(rule.get("file", "")).strip()
        p = ROOT / rel
        if not rel or not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        edits = rule.get("edits", [])
        if not isinstance(edits, list):
            continue
        for e in edits:
            if not isinstance(e, dict):
                continue
            old = e.get("old")
            if isinstance(old, str) and old and old in text:
                line = _line_for(text, old)
                issues.append(f"{rel}:{line}: {rule_id}: normalization drift requires normalize-fix")
    return issues


def _check_dogfood_executable_surface() -> list[str]:
    issues: list[str] = []
    for rel_root in _EXECUTABLE_CASE_TREE_ROOTS:
        base = ROOT / rel_root
        if not base.exists() or not base.is_dir():
            continue
        for pattern in _NON_MD_SPEC_GLOBS:
            for p in sorted(x for x in base.rglob(pattern) if x.is_file()):
                rel = p.relative_to(ROOT).as_posix()
                issues.append(
                    f"{rel}:1: NORMALIZATION_EXECUTABLE_SURFACE_MARKDOWN_ONLY: canonical executable surfaces must use .spec.md"
                )
    libs_root = ROOT / "docs/spec/libraries"
    if libs_root.exists():
        for pattern in _NON_MD_SPEC_GLOBS:
            for p in sorted(x for x in libs_root.rglob(pattern) if x.is_file()):
                rel = p.relative_to(ROOT).as_posix()
                issues.append(
                    f"{rel}:1: NORMALIZATION_LIBRARY_CASES_MARKDOWN_ONLY: spec_lang library cases must use .spec.md"
                )
    for glob in _DATA_ARTIFACT_GLOBS:
        for p in sorted(ROOT.glob(glob)):
            if not p.is_file():
                continue
            raw = p.read_text(encoding="utf-8")
            token = "```yaml spec-test"
            if token in raw:
                line = _line_for(raw, token)
                rel = p.relative_to(ROOT).as_posix()
                issues.append(
                    f"{rel}:{line}: NORMALIZATION_DATA_ARTIFACT_NON_EXECUTABLE: data artifacts must not embed yaml spec-test fences"
                )
    return issues


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Unified normalization check/fix runner for specs, contracts, and tests.")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="verify normalization without modifying files")
    mode.add_argument("--write", action="store_true", help="apply normalization rewrites")
    ap.add_argument("--scope", choices=("specs", "contracts", "tests", "all"), default="all")
    ap.add_argument("--profile", default=str(PROFILE_PATH), help="path to normalization profile yaml")
    ns = ap.parse_args(argv)

    profile = _load_profile(Path(ns.profile))
    scope_paths = _scope_paths(profile, ns.scope)
    if not scope_paths:
        print("docs/spec/schema/normalization_profile_v1.yaml:1: NORMALIZATION_PROFILE: no paths selected for scope")
        return 1

    mode_flag = "--check" if ns.check else "--write"
    domain_layout_cmd = [sys.executable, "scripts/migrate_spec_layout_domain_trees.py", mode_flag]
    vpath_cmd = [sys.executable, "scripts/convert_virtual_root_paths.py", mode_flag, *scope_paths]
    conv_cmd = [sys.executable, "scripts/convert_spec_lang_yaml_ast.py", mode_flag, *scope_paths]
    style_cmd = [sys.executable, "scripts/evaluate_style.py", mode_flag, *scope_paths]

    issues: list[str] = []
    domain_code, domain_out = _run(domain_layout_cmd)
    if domain_code != 0:
        for line in domain_out.splitlines():
            line = line.strip()
            if line:
                issues.append(f"docs/spec:1: NORMALIZATION_DOMAIN_TREE_LAYOUT: {line}")
    vpath_code, vpath_out = _run(vpath_cmd)
    if vpath_code != 0:
        for line in vpath_out.splitlines():
            line = line.strip()
            if line:
                issues.append(f"docs/spec:1: NORMALIZATION_VIRTUAL_ROOT_PATHS: {line}")
    conv_code, conv_out = _run(conv_cmd)
    if conv_code != 0:
        for line in conv_out.splitlines():
            line = line.strip()
            if line:
                issues.append(f"docs/spec:1: NORMALIZATION_MAPPING_AST_ONLY: {line}")
    style_code, style_out = _run(style_cmd)
    if style_code != 0:
        for line in style_out.splitlines():
            line = line.strip()
            if line:
                issues.append(f"docs/spec:1: NORMALIZATION_SPEC_STYLE: {line}")

    if ns.write:
        repl_issues, changed = _apply_replacements(profile)
        issues.extend(repl_issues)
        token_issues = _check_docs_tokens(profile)
        issues.extend(token_issues)
        issues.extend(_check_dogfood_executable_surface())
        if issues:
            for issue in sorted(issues):
                print(issue)
            return 1
        print(f"OK: normalization fix complete (replacement files changed: {changed})")
        return 0

    issues.extend(_check_replacements_drift(profile))
    issues.extend(_check_docs_tokens(profile))
    issues.extend(_check_dogfood_executable_surface())
    if issues:
        for issue in sorted(issues):
            print(issue)
        return 1

    print("OK: normalization check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

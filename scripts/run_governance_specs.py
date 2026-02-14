#!/usr/bin/env python3
from __future__ import annotations

import argparse
import inspect
import shlex
import sys
import re
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

import yaml
from spec_runner.assertions import assert_text_op, eval_assert_tree, iter_leaf_assertions
from spec_runner.dispatcher import SpecRunContext, iter_cases, run_case
from spec_runner.purpose_lint import (
    load_purpose_lint_policy,
    purpose_quality_warnings,
    resolve_purpose_lint_config,
)
from spec_runner.runtime_context import MiniCapsys, MiniMonkeyPatch
from spec_runner.settings import SETTINGS, governed_config_literals
from spec_runner.conformance_purpose import PURPOSE_WARNING_CODES


_SECURITY_WARNING_DOCS = (
    "README.md",
    "docs/book/00_first_10_minutes.md",
    "docs/spec/schema/schema_v1.md",
)
_SECURITY_WARNING_TOKENS = (
    "not a sandbox",
    "trusted inputs",
    "untrusted spec",
)
_V1_SCOPE_DOC = "docs/spec/contract/08_v1_scope.md"
_V1_SCOPE_REQUIRED_TOKENS = (
    "v1 in scope",
    "v1 non-goals",
    "compatibility commitments",
    "current-spec-only rule",
)
_PYTHON_RUNTIME_ROOTS = ("spec_runner", "scripts/python")
_CONFORMANCE_CASE_ID_PATTERN = r"\bSRCONF-[A-Z0-9-]+\b"
_CONFORMANCE_MAX_BLOCK_LINES = 50
_REGEX_PROFILE_DOC = "docs/spec/contract/03a_regex_portability_v1.md"
_ASSERTION_OPERATOR_DOC_SYNC_TOKENS = ("contain", "regex")
_CURRENT_SPEC_ONLY_DOCS = (
    "README.md",
    "docs/book/02_core_model.md",
    "docs/spec/schema/schema_v1.md",
    "docs/spec/contract/01_discovery.md",
    "docs/spec/contract/02_case_shape.md",
    "docs/spec/contract/03_assertions.md",
    "docs/spec/contract/04_harness.md",
    "docs/spec/contract/08_v1_scope.md",
)
_CURRENT_SPEC_ONLY_CODE_FILES = (
    "spec_runner/doc_parser.py",
    "scripts/php/spec_runner.php",
    "scripts/php/conformance_runner.php",
)
_CURRENT_SPEC_FORBIDDEN_PATTERNS = (
    r"\blegacy\b",
    r"\bkind\b",
    r"previous\s+spec",
    r"prior\s+spec",
    r"backward[- ]compatible",
)
_TYPE_CONTRACTS_DIR = "docs/spec/contract/types"
_CORE_TYPES = {"text.file", "cli.run"}
_COMMON_CASE_TOP_LEVEL_KEYS = {
    "id",
    "type",
    "title",
    "purpose",
    "assert",
    "expect",
    "requires",
    "assert_health",
    "harness",
}
_RUNNER_KEYS_MUST_BE_UNDER_HARNESS = {
    "entrypoint",
    "env",
    "stdin_isatty",
    "stdin_text",
    "block_imports",
    "stub_modules",
    "setup_files",
    "hook_before",
    "hook_after",
    "hook_kwargs",
    "tmp_path",
    "patcher",
    "capture",
}


def _scan_pending_no_resolved_markers(root: Path) -> list[str]:
    pending_dir = root / "docs/spec/pending"
    if not pending_dir.exists():
        return []
    violations: list[str] = []
    for p in sorted(pending_dir.glob("*.md")):
        lower = p.read_text(encoding="utf-8").lower()
        for tok in ("resolved:", "completed:"):
            if tok in lower:
                rel = p.relative_to(root)
                violations.append(f"{rel}: found '{tok}'")
    return violations


def _scan_security_warning_docs(root: Path) -> list[str]:
    violations: list[str] = []
    for rel in _SECURITY_WARNING_DOCS:
        p = root / rel
        if not p.exists():
            violations.append(f"{rel}: missing required doc")
            continue
        lower = p.read_text(encoding="utf-8").lower()
        missing = [tok for tok in _SECURITY_WARNING_TOKENS if tok not in lower]
        if missing:
            violations.append(f"{rel}: missing token(s): {', '.join(missing)}")
    return violations


def _scan_v1_scope_doc(root: Path) -> list[str]:
    p = root / _V1_SCOPE_DOC
    if not p.exists():
        return [f"{_V1_SCOPE_DOC}: missing required doc"]
    lower = p.read_text(encoding="utf-8").lower()
    missing = [tok for tok in _V1_SCOPE_REQUIRED_TOKENS if tok not in lower]
    if missing:
        return [f"{_V1_SCOPE_DOC}: missing token(s): {', '.join(missing)}"]
    return []


def _scan_runtime_config_literals(root: Path) -> list[str]:
    violations: list[str] = []
    governed = governed_config_literals()
    for rel_root in _PYTHON_RUNTIME_ROOTS:
        runtime_root = root / rel_root
        if not runtime_root.exists():
            continue
        for p in sorted(runtime_root.rglob("*.py")):
            if p.name == "settings.py":
                continue
            raw = p.read_text(encoding="utf-8")
            rel = p.relative_to(root)
            for literal, const_path in governed.items():
                if f'"{literal}"' in raw or f"'{literal}'" in raw:
                    violations.append(
                        f"{rel}: literal {literal!r} duplicated; use {const_path}"
                    )
    return violations


def _scan_runtime_settings_import_policy(root: Path) -> list[str]:
    violations: list[str] = []
    for rel_root in _PYTHON_RUNTIME_ROOTS:
        runtime_root = root / rel_root
        if not runtime_root.exists():
            continue
        for p in sorted(runtime_root.rglob("*.py")):
            if p.name == "settings.py":
                continue
            rel = p.relative_to(root)
            for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), start=1):
                s = line.strip()
                if not s.startswith("from spec_runner.settings import "):
                    continue
                imported = s.split("import ", 1)[1]
                names = [x.strip() for x in imported.split(",")]
                bad = [n for n in names if n.isupper() and n.startswith(("DEFAULT_", "ENV_"))]
                if bad:
                    violations.append(f"{rel}:{i}: banned settings constant import(s): {', '.join(bad)}")
    return violations


def _collect_conformance_fixture_ids(root: Path) -> set[str]:
    ids: set[str] = set()
    cases_dir = root / "docs/spec/conformance/cases"
    if not cases_dir.exists():
        return ids
    for spec in iter_cases(cases_dir, file_pattern=SETTINGS.case.default_file_pattern):
        rid = str(spec.test.get("id", "")).strip()
        if rid:
            ids.add(rid)
    return ids


def _scan_conformance_case_index_sync(root: Path) -> list[str]:
    violations: list[str] = []
    cases_dir = root / "docs/spec/conformance/cases"
    fixture_ids = _collect_conformance_fixture_ids(root)
    index_path = cases_dir / "README.md"
    if not fixture_ids and not index_path.exists():
        return violations
    if not index_path.exists():
        return [f"{index_path.relative_to(root)}: missing conformance case index"]

    raw = index_path.read_text(encoding="utf-8")
    indexed_ids = set(re.findall(_CONFORMANCE_CASE_ID_PATTERN, raw))
    for rid in sorted(fixture_ids - indexed_ids):
        violations.append(f"{index_path.relative_to(root)}: missing id {rid}")
    for rid in sorted(indexed_ids - fixture_ids):
        violations.append(f"{index_path.relative_to(root)}: stale id {rid}")
    return violations


def _scan_conformance_purpose_warning_codes_sync(root: Path) -> list[str]:
    p = root / "docs/spec/conformance/purpose_warning_codes.md"
    if not p.exists():
        return [f"{p.relative_to(root)}: missing purpose warning code doc"]
    raw = p.read_text(encoding="utf-8")
    doc_codes = set(re.findall(r"\bPUR\d{3}\b", raw))
    impl_codes = set(PURPOSE_WARNING_CODES)
    violations: list[str] = []
    for c in sorted(impl_codes - doc_codes):
        violations.append(f"{p.relative_to(root)}: missing code {c}")
    for c in sorted(doc_codes - impl_codes):
        violations.append(f"{p.relative_to(root)}: stale code {c}")
    return violations


def _is_spec_opening_fence(line: str) -> tuple[str, int] | None:
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
    if "spec-test" not in info:
        return None
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


def _is_markdown_fence_opening(line: str) -> tuple[str, int, str] | None:
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
    return ch, i, stripped[i:].strip()


def _scan_conformance_case_doc_style_guard(root: Path) -> list[str]:
    violations: list[str] = []
    policy, policy_errs, _ = load_purpose_lint_policy(root)
    violations.extend(policy_errs)
    cases_dir = root / "docs/spec/conformance/cases"
    if not cases_dir.exists():
        return violations

    global_ids: set[str] = set()
    for p in sorted(cases_dir.glob(SETTINGS.case.default_file_pattern)):
        raw = p.read_text(encoding="utf-8")
        lines = raw.splitlines()
        i = 0
        ids_in_file: list[str] = []
        while i < len(lines):
            opening = _is_spec_opening_fence(lines[i])
            if not opening:
                i += 1
                continue
            ch, fence_len = opening
            start = i
            i += 1
            block_lines: list[str] = []
            while i < len(lines) and not _is_closing_fence(lines[i], ch=ch, min_len=fence_len):
                block_lines.append(lines[i])
                i += 1
            if len(block_lines) > _CONFORMANCE_MAX_BLOCK_LINES:
                violations.append(
                    f"{p.relative_to(root)}:{start + 1}: block exceeds {_CONFORMANCE_MAX_BLOCK_LINES} lines"
                )
            payload = yaml.safe_load("\n".join(block_lines)) if block_lines else None
            if isinstance(payload, list):
                violations.append(f"{p.relative_to(root)}:{start + 1}: one case per spec-test block required")
            if isinstance(payload, dict):
                rid = str(payload.get("id", "")).strip()
                purpose = str(payload.get("purpose", "")).strip()
                cfg, cfg_errs = resolve_purpose_lint_config(payload, policy)
                for e in cfg_errs:
                    violations.append(f"{p.relative_to(root)}:{start + 1}: {e}")
                if not purpose:
                    violations.append(f"{p.relative_to(root)}:{start + 1}: case must include non-empty purpose")
                title = str(payload.get("title", "")).strip()
                for w in purpose_quality_warnings(title, purpose, cfg, honor_enabled=True):
                    if w == "purpose duplicates title":
                        violations.append(
                            f"{p.relative_to(root)}:{start + 1}: purpose must add context beyond title for case {rid or '<unknown>'}"
                        )
                    elif w.startswith("purpose word count "):
                        violations.append(
                            f"{p.relative_to(root)}:{start + 1}: case purpose must be at least {int(cfg.get('min_words', 8))} words for case {rid or '<unknown>'}"
                        )
                    elif w.startswith("purpose contains placeholder token(s): "):
                        violations.append(
                            f"{p.relative_to(root)}:{start + 1}: purpose contains placeholder token(s) {w.split(': ', 1)[1]} for case {rid or '<unknown>'}"
                        )
                if rid:
                    ids_in_file.append(rid)
                    if rid in global_ids:
                        violations.append(f"{p.relative_to(root)}:{start + 1}: duplicate conformance case id across files: {rid}")
                    global_ids.add(rid)
                    prev_idx = start - 1
                    while prev_idx >= 0 and not lines[prev_idx].strip():
                        prev_idx -= 1
                    expected_heading = f"## {rid}"
                    if prev_idx < 0 or lines[prev_idx].strip() != expected_heading:
                        violations.append(
                            f"{p.relative_to(root)}:{start + 1}: expected heading '{expected_heading}' immediately before block"
                        )
            i += 1
        if ids_in_file != sorted(ids_in_file):
            violations.append(f"{p.relative_to(root)}: case ids must be sorted within file")
    return violations


def _scan_regex_doc_sync(root: Path) -> list[str]:
    violations: list[str] = []
    assertions_doc = root / "docs/spec/contract/03_assertions.md"
    schema_doc = root / "docs/spec/schema/schema_v1.md"
    policy_doc = root / "docs/spec/contract/policy_v1.yaml"
    if not assertions_doc.exists() or not schema_doc.exists() or not policy_doc.exists():
        return violations

    assertions_text = assertions_doc.read_text(encoding="utf-8")
    schema_text = schema_doc.read_text(encoding="utf-8")
    policy_text = policy_doc.read_text(encoding="utf-8")

    if _REGEX_PROFILE_DOC not in assertions_text:
        violations.append(
            "docs/spec/contract/03_assertions.md: missing regex portability profile reference"
        )
    if _REGEX_PROFILE_DOC not in schema_text:
        violations.append(
            "docs/spec/schema/schema_v1.md: missing regex portability profile reference"
        )
    if _REGEX_PROFILE_DOC not in policy_text:
        violations.append(
            "docs/spec/contract/policy_v1.yaml: missing regex portability profile reference"
        )

    for tok in _ASSERTION_OPERATOR_DOC_SYNC_TOKENS:
        if tok not in assertions_text:
            violations.append(f"docs/spec/contract/03_assertions.md: missing operator token {tok}")
        if tok not in schema_text:
            violations.append(f"docs/spec/schema/schema_v1.md: missing operator token {tok}")
    return violations


def _scan_current_spec_only_contract(root: Path) -> list[str]:
    violations: list[str] = []
    patterns = [re.compile(p, re.IGNORECASE) for p in _CURRENT_SPEC_FORBIDDEN_PATTERNS]
    for rel in (*_CURRENT_SPEC_ONLY_DOCS, *_CURRENT_SPEC_ONLY_CODE_FILES):
        p = root / rel
        if not p.exists():
            continue
        for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), start=1):
            for pat in patterns:
                if pat.search(line):
                    violations.append(
                        f"{rel}:{i}: forbidden pre-current-spec reference matched /{pat.pattern}/"
                    )
                    break
    return violations


def _type_contract_doc_rel_for(case_type: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", case_type.lower()).strip("_")
    return f"{_TYPE_CONTRACTS_DIR}/{slug}.md"


def _scan_conformance_type_contract_docs(root: Path) -> list[str]:
    violations: list[str] = []
    cases_dir = root / "docs/spec/conformance/cases"
    if not cases_dir.exists():
        return violations

    seen_types: set[str] = set()
    for spec in iter_cases(cases_dir, file_pattern=SETTINGS.case.default_file_pattern):
        case_type = str(spec.test.get("type", "")).strip()
        if not case_type:
            continue
        seen_types.add(case_type)

    for case_type in sorted(seen_types):
        rel = _type_contract_doc_rel_for(case_type)
        p = root / rel
        if not p.exists():
            violations.append(f"missing type contract doc for '{case_type}': {rel}")
            continue
        raw = p.read_text(encoding="utf-8")
        heading = f"# Type Contract: {case_type}"
        if heading not in raw:
            violations.append(f"{rel}: missing heading '{heading}'")
    return violations


def _collect_assert_targets(node: object) -> list[str]:
    targets: list[str] = []
    if isinstance(node, list):
        for child in node:
            targets.extend(_collect_assert_targets(child))
        return targets
    if not isinstance(node, dict):
        return targets
    target = node.get("target")
    if isinstance(target, str) and target.strip():
        targets.append(target.strip())
    for key in ("must", "can", "cannot"):
        child = node.get(key)
        if child is not None:
            targets.extend(_collect_assert_targets(child))
    return targets


def _scan_conformance_api_http_portable_shape(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    cfg = h.get("api_http")
    if not isinstance(cfg, dict):
        return ["conformance.api_http_portable_shape requires harness.api_http mapping in governance spec"]
    raw_allowed_keys = cfg.get("allowed_top_level_keys")
    if not isinstance(raw_allowed_keys, list) or not raw_allowed_keys or any(not isinstance(x, str) for x in raw_allowed_keys):
        return ["harness.api_http.allowed_top_level_keys must be a non-empty list of strings"]
    allowed_top_level_keys = {x.strip() for x in raw_allowed_keys if x.strip()}
    if not allowed_top_level_keys:
        return ["harness.api_http.allowed_top_level_keys must include at least one non-empty key"]
    raw_allowed_targets = cfg.get("allowed_assert_targets")
    if not isinstance(raw_allowed_targets, list) or not raw_allowed_targets or any(not isinstance(x, str) for x in raw_allowed_targets):
        return ["harness.api_http.allowed_assert_targets must be a non-empty list of strings"]
    allowed_assert_targets = {x.strip() for x in raw_allowed_targets if x.strip()}
    if not allowed_assert_targets:
        return ["harness.api_http.allowed_assert_targets must include at least one non-empty target"]
    raw_required_request_fields = cfg.get("required_request_fields", ["method", "url"])
    if (
        not isinstance(raw_required_request_fields, list)
        or not raw_required_request_fields
        or any(not isinstance(x, str) for x in raw_required_request_fields)
    ):
        return ["harness.api_http.required_request_fields must be a non-empty list of strings"]
    required_request_fields = {x.strip() for x in raw_required_request_fields if x.strip()}
    if not required_request_fields:
        return ["harness.api_http.required_request_fields must include at least one non-empty field"]
    cases_dir = root / "docs/spec/conformance/cases"
    if not cases_dir.exists():
        return violations

    for spec in iter_cases(cases_dir, file_pattern=SETTINGS.case.default_file_pattern):
        case = spec.test
        case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
        case_type = str(case.get("type", "")).strip()
        if case_type != "api.http":
            continue
        expect = case.get("expect")
        schema_failure_fixture = False
        if isinstance(expect, dict):
            portable = expect.get("portable")
            if isinstance(portable, dict):
                status = str(portable.get("status", "")).strip().lower()
                category_raw = portable.get("category")
                category = None if category_raw is None else str(category_raw).strip().lower()
                schema_failure_fixture = status == "fail" and category == "schema"

        extra_top = sorted(k for k in case.keys() if str(k) not in allowed_top_level_keys)
        if extra_top:
            violations.append(
                f"{case_id}: unsupported top-level key(s) for api.http portable case: {', '.join(extra_top)}"
            )

        request = case.get("request")
        if not isinstance(request, dict):
            violations.append(f"{case_id}: api.http requires request mapping")
        elif not schema_failure_fixture:
            for field in sorted(required_request_fields):
                value = str(request.get(field, "")).strip()
                if not value:
                    violations.append(f"{case_id}: api.http request.{field} is required")

        targets = _collect_assert_targets(case.get("assert", []))
        for t in targets:
            if t not in allowed_assert_targets:
                violations.append(
                    f"{case_id}: unsupported api.http assert target '{t}' "
                    f"(allowed: {', '.join(sorted(allowed_assert_targets))})"
                )
    return violations


def _iter_string_values(node: object):
    if isinstance(node, dict):
        for v in node.values():
            yield from _iter_string_values(v)
        return
    if isinstance(node, list):
        for v in node:
            yield from _iter_string_values(v)
        return
    if isinstance(node, str):
        yield node


def _scan_conformance_no_runner_logic_outside_harness(root: Path) -> list[str]:
    violations: list[str] = []
    cases_dir = root / "docs/spec/conformance/cases"
    if not cases_dir.exists():
        return violations

    for spec in iter_cases(cases_dir, file_pattern=SETTINGS.case.default_file_pattern):
        case = spec.test
        case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
        bad = sorted(k for k in case.keys() if str(k) in _RUNNER_KEYS_MUST_BE_UNDER_HARNESS)
        if bad:
            violations.append(
                f"{case_id}: runner/setup key(s) must be under harness: {', '.join(bad)}"
            )
    return violations


def _scan_conformance_portable_determinism_guard(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    determinism = h.get("determinism")
    if not isinstance(determinism, dict):
        return ["conformance.portable_determinism_guard requires harness.determinism mapping in governance spec"]
    raw_patterns = determinism.get("patterns")
    if not isinstance(raw_patterns, list) or not raw_patterns:
        return ["conformance.portable_determinism_guard requires non-empty harness.determinism.patterns list"]
    compiled_patterns: list[re.Pattern[str]] = []
    for raw in raw_patterns:
        if not isinstance(raw, str) or not raw.strip():
            violations.append("harness.determinism.patterns entries must be non-empty strings")
            continue
        try:
            compiled_patterns.append(re.compile(raw, re.IGNORECASE))
        except re.error as e:
            violations.append(f"invalid regex in harness.determinism.patterns: {raw!r} ({e})")
    raw_exclude = determinism.get("exclude_case_keys", ["id", "title", "purpose", "expect", "requires", "assert_health"])
    if not isinstance(raw_exclude, list) or any(not isinstance(x, str) for x in raw_exclude):
        violations.append("harness.determinism.exclude_case_keys must be a list of strings")
        return violations
    exclude_case_keys = {x for x in raw_exclude if x}
    if not compiled_patterns:
        return violations
    cases_dir = root / "docs/spec/conformance/cases"
    if not cases_dir.exists():
        return violations

    for spec in iter_cases(cases_dir, file_pattern=SETTINGS.case.default_file_pattern):
        case = spec.test
        case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
        scoped = {
            k: v
            for k, v in case.items()
            if str(k) not in exclude_case_keys
        }
        for s in _iter_string_values(scoped):
            for pat in compiled_patterns:
                if pat.search(s):
                    violations.append(
                        f"{case_id}: non-deterministic token matched /{pat.pattern}/ in case content"
                    )
                    break
    return violations


def _scan_conformance_extension_requires_capabilities(root: Path) -> list[str]:
    violations: list[str] = []
    cases_dir = root / "docs/spec/conformance/cases"
    if not cases_dir.exists():
        return violations

    for spec in iter_cases(cases_dir, file_pattern=SETTINGS.case.default_file_pattern):
        case = spec.test
        case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
        case_type = str(case.get("type", "")).strip()
        if not case_type or case_type in _CORE_TYPES:
            continue

        requires = case.get("requires")
        if not isinstance(requires, dict):
            violations.append(f"{case_id}: extension type '{case_type}' requires mapping 'requires'")
            continue
        capabilities = requires.get("capabilities")
        if not isinstance(capabilities, list):
            violations.append(f"{case_id}: extension type '{case_type}' requires list requires.capabilities")
            continue
        cap_values = {str(v).strip() for v in capabilities if str(v).strip()}
        if case_type not in cap_values:
            violations.append(
                f"{case_id}: requires.capabilities must include extension type '{case_type}'"
            )
    return violations


def _load_type_contract_top_level_fields(root: Path, case_type: str) -> set[str]:
    rel = _type_contract_doc_rel_for(case_type)
    p = root / rel
    if not p.exists():
        return set()
    fields: set[str] = set()
    in_fields_section = False
    current_section = ""
    for raw in p.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("## "):
            current_section = line[3:].strip().lower()
            in_fields_section = current_section in {"required fields", "optional fields"}
            continue
        if not in_fields_section or not line.startswith("- "):
            continue
        m = re.search(r"`([^`]+)`", line)
        if not m:
            continue
        token = m.group(1).strip()
        if not token:
            continue
        fields.add(token.split(".", 1)[0])
    return fields


def _scan_conformance_type_contract_field_sync(root: Path) -> list[str]:
    violations: list[str] = []
    cases_dir = root / "docs/spec/conformance/cases"
    if not cases_dir.exists():
        return violations

    for spec in iter_cases(cases_dir, file_pattern=SETTINGS.case.default_file_pattern):
        case = spec.test
        case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
        case_type = str(case.get("type", "")).strip()
        if not case_type:
            continue
        type_fields = _load_type_contract_top_level_fields(root, case_type)
        if not type_fields:
            # Missing type doc is handled by conformance.type_contract_docs.
            continue
        allowed = _COMMON_CASE_TOP_LEVEL_KEYS | type_fields
        bad = sorted(k for k in case.keys() if str(k) not in allowed)
        if bad:
            violations.append(
                f"{case_id}: key(s) not declared in type contract for {case_type}: {', '.join(bad)}"
            )
    return violations


def _scan_docs_reference_surface_complete(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    cfg = h.get("docs_reference_surface")
    if not isinstance(cfg, dict):
        return ["docs.reference_surface_complete requires harness.docs_reference_surface mapping in governance spec"]

    required_files = cfg.get("required_files")
    if (
        not isinstance(required_files, list)
        or not required_files
        or any(not isinstance(x, str) or not x.strip() for x in required_files)
    ):
        return ["harness.docs_reference_surface.required_files must be a non-empty list of non-empty strings"]

    required_globs = cfg.get("required_globs", [])
    if not isinstance(required_globs, list) or any(not isinstance(x, str) or not x.strip() for x in required_globs):
        return ["harness.docs_reference_surface.required_globs must be a list of non-empty strings"]

    for rel in required_files:
        p = root / rel
        if not p.exists():
            violations.append(f"{rel}: missing required reference file")

    for pattern in required_globs:
        matches = sorted(root.glob(pattern))
        if not matches:
            violations.append(f"{pattern}: glob matched no files")
    return violations


def _extract_backtick_paths(text: str) -> list[str]:
    return [m.group(1).strip() for m in re.finditer(r"`([^`]+)`", text) if m.group(1).strip()]


def _scan_docs_reference_index_sync(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    cfg = h.get("reference_index")
    if not isinstance(cfg, dict):
        return ["docs.reference_index_sync requires harness.reference_index mapping in governance spec"]

    index_rel = str(cfg.get("path", "")).strip()
    include_glob = str(cfg.get("include_glob", "")).strip()
    if not index_rel:
        return ["harness.reference_index.path must be a non-empty string"]
    if not include_glob:
        return ["harness.reference_index.include_glob must be a non-empty string"]

    exclude_files = cfg.get("exclude_files", [])
    if not isinstance(exclude_files, list) or any(not isinstance(x, str) for x in exclude_files):
        return ["harness.reference_index.exclude_files must be a list of strings"]
    exclude = {x.strip() for x in exclude_files if x.strip()}

    index_path = root / index_rel
    if not index_path.exists():
        return [f"{index_rel}: missing reference index file"]

    expected = [
        str(p.relative_to(root))
        for p in sorted(root.glob(include_glob))
        if str(p.relative_to(root)) not in exclude
    ]
    raw = index_path.read_text(encoding="utf-8")
    listed = [p for p in _extract_backtick_paths(raw) if p.startswith("docs/book/") and p.endswith(".md")]
    seen: set[str] = set()
    deduped_listed: list[str] = []
    for rel in listed:
        if rel in seen:
            violations.append(f"{index_rel}: duplicate entry {rel}")
            continue
        seen.add(rel)
        deduped_listed.append(rel)

    for rel in expected:
        if rel not in seen:
            violations.append(f"{index_rel}: missing entry {rel}")
    for rel in deduped_listed:
        if rel not in expected:
            violations.append(f"{index_rel}: stale entry {rel}")
    if deduped_listed and expected and deduped_listed != expected:
        violations.append(f"{index_rel}: entries are out of sync or out of order with {include_glob}")
    return violations


def _scan_docs_required_sections(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    cfg = h.get("required_sections")
    if not isinstance(cfg, dict) or not cfg:
        return ["docs.required_sections requires non-empty harness.required_sections mapping in governance spec"]

    for rel, tokens in cfg.items():
        if not isinstance(rel, str) or not rel.strip():
            violations.append("harness.required_sections keys must be non-empty file paths")
            continue
        if not isinstance(tokens, list) or not tokens or any(not isinstance(x, str) or not x.strip() for x in tokens):
            violations.append(f"harness.required_sections[{rel!r}] must be a non-empty list of non-empty strings")
            continue
        p = root / rel
        if not p.exists():
            violations.append(f"{rel}: missing required section-checked file")
            continue
        lower = p.read_text(encoding="utf-8").lower()
        missing = [tok for tok in tokens if tok.lower() not in lower]
        if missing:
            violations.append(f"{rel}: missing required token(s): {', '.join(missing)}")
    return violations


def _has_docs_example_opt_out(lines: list[str], start: int, end: int) -> bool:
    lo = max(0, start - 3)
    hi = min(len(lines), end + 4)
    marker = re.compile(r"DOCS-EXAMPLE-OPT-OUT:\s*(.+)")
    for idx in range(lo, hi):
        m = marker.search(lines[idx])
        if m and m.group(1).strip():
            return True
    return False


def _validate_shell_block(block_lines: list[str]) -> str | None:
    pending = ""
    pending_start = 0
    for i, raw in enumerate(block_lines, start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if pending:
            line = f"{pending} {line}"
            pending = ""
        else:
            pending_start = i
        if line.startswith("$"):
            return f"shell line {i}: leading '$' prompt markers are not allowed"
        if line.endswith("\\"):
            pending = line[:-1].rstrip()
            continue
        try:
            parts = shlex.split(line)
        except ValueError as e:
            return f"shell line {i}: {e}"
        if not parts:
            continue
    if pending:
        return f"shell line {pending_start}: trailing line-continuation without command tail"
    return None


def _validate_python_block(block_lines: list[str]) -> str | None:
    src = "\n".join(block_lines)
    try:
        compile(src, "<docs-python-example>", "exec")
    except SyntaxError as e:
        return f"python syntax error: line {e.lineno}: {e.msg}"
    return None


def _scan_docs_examples_runnable(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    cfg = h.get("docs_examples")
    if not isinstance(cfg, dict):
        return ["docs.examples_runnable requires harness.docs_examples mapping in governance spec"]
    docs = cfg.get("files")
    if not isinstance(docs, list) or not docs or any(not isinstance(x, str) or not x.strip() for x in docs):
        return ["harness.docs_examples.files must be a non-empty list of non-empty strings"]

    for rel in docs:
        p = root / rel
        if not p.exists():
            violations.append(f"{rel}: missing docs file for example scan")
            continue
        lines = p.read_text(encoding="utf-8").splitlines()
        i = 0
        while i < len(lines):
            opening = _is_markdown_fence_opening(lines[i])
            if not opening:
                i += 1
                continue
            ch, fence_len, info = opening
            start = i
            info_tokens = info.lower().split()
            i += 1
            block_lines: list[str] = []
            while i < len(lines) and not _is_closing_fence(lines[i], ch=ch, min_len=fence_len):
                block_lines.append(lines[i])
                i += 1
            end = i
            err: str | None = None
            if "spec-test" in info_tokens and ("yaml" in info_tokens or "yml" in info_tokens):
                try:
                    payload = yaml.safe_load("\n".join(block_lines))
                    if payload is None:
                        err = "empty spec-test block"
                except Exception as e:  # noqa: BLE001
                    err = f"yaml parse error: {e}"
            elif info_tokens and info_tokens[0] in {"sh", "bash", "shell", "zsh"}:
                err = _validate_shell_block(block_lines)
            elif info_tokens and info_tokens[0] == "python":
                err = _validate_python_block(block_lines)
            if err and not _has_docs_example_opt_out(lines, start, end):
                violations.append(f"{rel}:{start + 1}: invalid example block ({err})")
            i += 1
    return violations


def _extract_python_script_flags(path: Path) -> set[str]:
    raw = path.read_text(encoding="utf-8")
    return set(re.findall(r"add_argument\(\s*['\"](--[a-z0-9-]+)['\"]", raw))


def _extract_php_script_flags(path: Path) -> set[str]:
    raw = path.read_text(encoding="utf-8")
    return set(re.findall(r"\$arg\s*===\s*['\"](--[a-z0-9-]+)['\"]", raw))


def _scan_docs_cli_flags_documented(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    cfg = h.get("cli_docs")
    if not isinstance(cfg, dict):
        return ["docs.cli_flags_documented requires harness.cli_docs mapping in governance spec"]

    python_scripts = cfg.get("python_scripts", [])
    php_scripts = cfg.get("php_scripts", [])
    python_docs = cfg.get("python_docs", [])
    php_docs = cfg.get("php_docs", [])
    for name, value in (
        ("python_scripts", python_scripts),
        ("php_scripts", php_scripts),
        ("python_docs", python_docs),
        ("php_docs", php_docs),
    ):
        if not isinstance(value, list) or any(not isinstance(x, str) or not x.strip() for x in value):
            return [f"harness.cli_docs.{name} must be a list of non-empty strings"]

    python_flags: dict[str, set[str]] = {}
    for rel in python_scripts:
        p = root / rel
        if not p.exists():
            violations.append(f"{rel}: missing python script for CLI docs scan")
            continue
        python_flags[rel] = _extract_python_script_flags(p)

    php_flags: dict[str, set[str]] = {}
    for rel in php_scripts:
        p = root / rel
        if not p.exists():
            violations.append(f"{rel}: missing php script for CLI docs scan")
            continue
        php_flags[rel] = _extract_php_script_flags(p)

    doc_cache: dict[str, str] = {}
    for rel in [*python_docs, *php_docs]:
        p = root / rel
        if not p.exists():
            violations.append(f"{rel}: missing documentation file for CLI docs scan")
            continue
        doc_cache[rel] = p.read_text(encoding="utf-8")

    for script_rel, flags in sorted(python_flags.items()):
        for flag in sorted(flags):
            for doc_rel in python_docs:
                text = doc_cache.get(doc_rel)
                if text is None:
                    continue
                if flag not in text:
                    violations.append(f"{doc_rel}: missing CLI flag {flag} documented from {script_rel}")

    for script_rel, flags in sorted(php_flags.items()):
        for flag in sorted(flags):
            for doc_rel in php_docs:
                text = doc_cache.get(doc_rel)
                if text is None:
                    continue
                if flag not in text:
                    violations.append(f"{doc_rel}: missing CLI flag {flag} documented from {script_rel}")
    return violations


def _scan_docs_contract_schema_book_sync(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    cfg = h.get("doc_sync")
    if not isinstance(cfg, dict):
        return ["docs.contract_schema_book_sync requires harness.doc_sync mapping in governance spec"]
    files = cfg.get("files")
    tokens = cfg.get("tokens")
    if not isinstance(files, list) or len(files) < 2 or any(not isinstance(x, str) or not x.strip() for x in files):
        return ["harness.doc_sync.files must be a list of at least two non-empty strings"]
    if not isinstance(tokens, list) or not tokens or any(not isinstance(x, str) or not x.strip() for x in tokens):
        return ["harness.doc_sync.tokens must be a non-empty list of non-empty strings"]

    loaded: dict[str, str] = {}
    for rel in files:
        p = root / rel
        if not p.exists():
            violations.append(f"{rel}: missing doc_sync file")
            continue
        loaded[rel] = p.read_text(encoding="utf-8").lower()
    if len(loaded) < 2:
        return violations

    for tok in tokens:
        want = tok.lower()
        for rel, text in loaded.items():
            if want not in text:
                violations.append(f"{rel}: missing sync token {tok}")
    return violations


GovernanceCheck = Callable[..., list[str]]

_CHECKS: dict[str, GovernanceCheck] = {
    "pending.no_resolved_markers": _scan_pending_no_resolved_markers,
    "docs.security_warning_contract": _scan_security_warning_docs,
    "docs.v1_scope_contract": _scan_v1_scope_doc,
    "runtime.config_literals": _scan_runtime_config_literals,
    "runtime.settings_import_policy": _scan_runtime_settings_import_policy,
    "conformance.case_index_sync": _scan_conformance_case_index_sync,
    "conformance.purpose_warning_codes_sync": _scan_conformance_purpose_warning_codes_sync,
    "conformance.case_doc_style_guard": _scan_conformance_case_doc_style_guard,
    "docs.regex_doc_sync": _scan_regex_doc_sync,
    "docs.current_spec_only_contract": _scan_current_spec_only_contract,
    "conformance.type_contract_docs": _scan_conformance_type_contract_docs,
    "conformance.api_http_portable_shape": _scan_conformance_api_http_portable_shape,
    "conformance.no_runner_logic_outside_harness": _scan_conformance_no_runner_logic_outside_harness,
    "conformance.portable_determinism_guard": _scan_conformance_portable_determinism_guard,
    "conformance.extension_requires_capabilities": _scan_conformance_extension_requires_capabilities,
    "conformance.type_contract_field_sync": _scan_conformance_type_contract_field_sync,
    "docs.reference_surface_complete": _scan_docs_reference_surface_complete,
    "docs.reference_index_sync": _scan_docs_reference_index_sync,
    "docs.required_sections": _scan_docs_required_sections,
    "docs.examples_runnable": _scan_docs_examples_runnable,
    "docs.cli_flags_documented": _scan_docs_cli_flags_documented,
    "docs.contract_schema_book_sync": _scan_docs_contract_schema_book_sync,
}


def run_governance_check(case, *, ctx) -> None:
    t = case.test
    check_id = str(t.get("check", "")).strip()
    if not check_id:
        raise ValueError("governance.check requires 'check'")
    fn = _CHECKS.get(check_id)
    if fn is None:
        supported = ", ".join(sorted(_CHECKS))
        raise ValueError(f"unknown governance check: {check_id} (supported: {supported})")

    h = t.get("harness") or {}
    if not isinstance(h, dict):
        raise TypeError("harness must be a mapping")
    root = Path(str(h.get("root", "."))).resolve()
    fn_params = inspect.signature(fn).parameters
    if "harness" in fn_params:
        violations = fn(root, harness=h)
    else:
        violations = fn(root)

    text = (
        f"PASS: {check_id}"
        if not violations
        else f"FAIL: {check_id}\n" + "\n".join(violations)
    )

    assert_spec = t.get("assert", []) or []

    def _eval_leaf(leaf: dict, *, inherited_target: str | None = None, assert_path: str = "assert") -> None:
        for target, op, value, is_true in iter_leaf_assertions(leaf, target_override=inherited_target):
            if target != "text":
                raise ValueError(f"unknown assert target for governance.check: {target}")
            assert_text_op(text, op, value, is_true=is_true)

    eval_assert_tree(assert_spec, eval_leaf=_eval_leaf)
    if violations:
        raise AssertionError(text)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Run governance spec cases with project-owned governance.check harness."
    )
    ap.add_argument("--cases", default="docs/spec/governance/cases", help="Path to governance case docs directory")
    ap.add_argument(
        "--case-file-pattern",
        default=SETTINGS.case.default_file_pattern,
        help="Glob pattern for case files when --cases points to a directory",
    )
    ns = ap.parse_args(argv)

    case_pattern = str(ns.case_file_pattern).strip()
    if not case_pattern:
        print("ERROR: --case-file-pattern requires a non-empty value", file=sys.stderr)
        return 2

    cases_path = Path(str(ns.cases))
    if not cases_path.exists():
        print(f"ERROR: cases path does not exist: {cases_path}", file=sys.stderr)
        return 2

    failures: list[str] = []
    with TemporaryDirectory(prefix="spec-runner-governance-") as td:
        ctx = SpecRunContext(
            tmp_path=Path(td),
            patcher=MiniMonkeyPatch(),
            capture=MiniCapsys(),
        )
        for case in iter_cases(cases_path, file_pattern=case_pattern):
            try:
                run_case(case, ctx=ctx, type_runners={"governance.check": run_governance_check})
            except BaseException as e:  # noqa: BLE001
                failures.append(f"{case.test.get('id', '<unknown>')}: {e}")

    if failures:
        for line in failures:
            print(f"ERROR: {line}", file=sys.stderr)
        return 1

    print(f"OK: governance specs passed ({cases_path})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

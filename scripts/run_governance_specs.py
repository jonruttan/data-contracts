#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import inspect
import shlex
import subprocess
import sys
import re
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable

import yaml
from spec_runner.assertions import eval_assert_tree, iter_leaf_assertions
from spec_runner.codecs import load_external_cases
from spec_runner.dispatcher import SpecRunContext, iter_cases, run_case
from spec_runner.doc_parser import iter_spec_doc_tests
from spec_runner.purpose_lint import (
    load_purpose_lint_policy,
    purpose_quality_warnings,
    resolve_purpose_lint_config,
)
from spec_runner.runtime_context import MiniCapsys, MiniMonkeyPatch
from spec_runner.settings import SETTINGS, governed_config_literals
from spec_runner.spec_lang import SpecLangLimits, _builtin_arity_table, eval_predicate
from spec_runner.spec_lang_stdlib_profile import spec_lang_stdlib_report_jsonable
from spec_runner.spec_lang_libraries import load_spec_lang_symbols_for_case
from spec_runner.spec_lang_yaml_ast import SpecLangYamlAstError, compile_yaml_expr_to_sexpr
from spec_runner.conformance_purpose import PURPOSE_WARNING_CODES
from spec_runner.conformance_purpose import conformance_purpose_report_jsonable
from spec_runner.contract_governance import check_contract_governance
from spec_runner.contract_governance import contract_coverage_jsonable
from spec_runner.docs_quality import build_docs_graph
from spec_runner.docs_quality import check_command_examples_verified
from spec_runner.docs_quality import check_example_id_uniqueness
from spec_runner.docs_quality import check_instructions_complete
from spec_runner.docs_quality import check_token_dependency_resolved
from spec_runner.docs_quality import check_token_ownership_unique
from spec_runner.docs_quality import load_docs_meta_for_paths
from spec_runner.docs_quality import load_reference_manifest
from spec_runner.docs_quality import manifest_chapter_paths
from spec_runner.docs_quality import render_reference_coverage
from spec_runner.docs_quality import render_reference_index
from spec_runner.quality_metrics import compare_metric_non_regression
from spec_runner.quality_metrics import contract_assertions_report_jsonable
from spec_runner.quality_metrics import docs_operability_report_jsonable
from spec_runner.quality_metrics import objective_scorecard_report_jsonable
from spec_runner.quality_metrics import python_dependency_report_jsonable
from spec_runner.quality_metrics import runner_independence_report_jsonable
from spec_runner.quality_metrics import spec_lang_adoption_report_jsonable
from spec_runner.quality_metrics import validate_metric_baseline_notes
from spec_runner.quality_metrics import _load_baseline_json
from spec_runner.governance_engine import GovernancePolicyResult, normalize_policy_evaluate, run_governance_policy
from spec_runner.spec_portability import spec_portability_report_jsonable
from spec_runner.virtual_paths import VirtualPathError, normalize_contract_path, parse_external_ref, resolve_contract_path


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
_CONFORMANCE_MAX_BLOCK_LINES = 120
_REGEX_PROFILE_DOC = "docs/spec/contract/03a_regex_portability_v1.md"
_ASSERTION_OPERATOR_DOC_SYNC_TOKENS = ("evaluate",)
_ASSERT_UNIVERSAL_DOC_FILES = (
    "docs/spec/schema/schema_v1.md",
    "docs/spec/contract/03_assertions.md",
    "docs/spec/contract/09_internal_representation.md",
)
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
    r"previous\s+spec",
    r"prior\s+spec",
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
_NORMALIZATION_PROFILE_PATH = "docs/spec/schema/normalization_profile_v1.yaml"
_PATH_LIKE_KEYS = {
    "path",
    "library_paths",
    "cases_path",
    "baseline_path",
    "manifest_path",
    "index_out",
    "coverage_out",
    "graph_out",
    "required_paths",
    "adapter_path",
    "cli_main_path",
    "required_library_path",
    "reference_manifest",
    "roots",
}
_DOMAIN_TREE_ROOTS = (
    "docs/spec/conformance/cases",
    "docs/spec/governance/cases",
    "docs/spec/libraries",
)
_SUBJECT_PROFILE_CONTRACT_DOC = "docs/spec/contract/20_subject_profiles_v1.md"
_SUBJECT_PROFILE_SCHEMA_DOC = "docs/spec/schema/subject_profiles_v1.yaml"
_SUBJECT_PROFILE_TYPE_DOCS = (
    "docs/spec/contract/types/python_profile.md",
    "docs/spec/contract/types/php_profile.md",
    "docs/spec/contract/types/http_profile.md",
    "docs/spec/contract/types/markdown_profile.md",
    "docs/spec/contract/types/makefile_profile.md",
)
_SUBJECT_PROFILE_DOMAIN_LIBS = (
    "docs/spec/libraries/domain/python_core.spec.md",
    "docs/spec/libraries/domain/php_core.spec.md",
    "docs/spec/libraries/domain/http_core.spec.md",
    "docs/spec/libraries/domain/markdown_core.spec.md",
    "docs/spec/libraries/domain/make_core.spec.md",
)


def _resolve_contract_config_path(root: Path, raw: str, *, field: str) -> Path:
    return resolve_contract_path(root, str(raw), field=field)


def _join_contract_path(root: Path, raw: object) -> Path:
    return root / str(raw).lstrip("/")


def _iter_path_fields(node: object, *, key_path: str = ""):
    if isinstance(node, dict):
        for k, v in node.items():
            key = str(k)
            current = f"{key_path}.{key}" if key_path else key
            if key in {"request", "setup_files"}:
                yield from _iter_path_fields(v, key_path=current)
                continue
            if key in _PATH_LIKE_KEYS:
                if isinstance(v, str):
                    yield current, v
                elif isinstance(v, list):
                    for idx, item in enumerate(v):
                        if isinstance(item, str):
                            yield f"{current}[{idx}]", item
                elif isinstance(v, dict):
                    for kk, vv in v.items():
                        if isinstance(vv, str):
                            yield f"{current}.{kk}", vv
            yield from _iter_path_fields(v, key_path=current)
    elif isinstance(node, list):
        for idx, item in enumerate(node):
            current = f"{key_path}[{idx}]" if key_path else f"[{idx}]"
            yield from _iter_path_fields(item, key_path=current)


def _iter_all_spec_cases(base: Path):
    if not base.exists():
        return
    for file_path in sorted(base.rglob(SETTINGS.case.default_file_pattern)):
        if not file_path.is_file():
            continue
        for doc_path, case in load_external_cases(file_path, formats={"md"}):
            yield doc_path, case


def _scan_contract_governance_check(root: Path) -> list[str]:
    return list(check_contract_governance(root))


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
        p = _join_contract_path(root, rel)
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
        runtime_root = _join_contract_path(root, rel_root)
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
        runtime_root = _join_contract_path(root, rel_root)
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


def _scan_runtime_assertions_via_spec_lang(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    cfg = h.get("assert_engine")
    if not isinstance(cfg, dict):
        return ["runtime.assertions_via_spec_lang requires harness.assert_engine mapping in governance spec"]
    files = cfg.get("files")
    if not isinstance(files, list) or not files:
        return ["harness.assert_engine.files must be a non-empty list"]
    for entry in files:
        if not isinstance(entry, dict):
            violations.append("harness.assert_engine.files entries must be mappings")
            continue
        rel = str(entry.get("path", "")).strip()
        if not rel:
            violations.append("harness.assert_engine.files[].path must be non-empty")
            continue
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing runtime assertion file")
            continue
        raw = p.read_text(encoding="utf-8")
        required = entry.get("required_tokens", [])
        forbidden = entry.get("forbidden_tokens", [])
        if not isinstance(required, list) or any(not isinstance(x, str) or not x.strip() for x in required):
            violations.append(f"{rel}:1: required_tokens must be list of non-empty strings")
            continue
        if not isinstance(forbidden, list) or any(not isinstance(x, str) or not x.strip() for x in forbidden):
            violations.append(f"{rel}:1: forbidden_tokens must be list of non-empty strings")
            continue
        for tok in required:
            if tok not in raw:
                violations.append(f"{rel}:1: missing required token for spec-lang assertion path: {tok}")
        for tok in forbidden:
            if tok in raw:
                violations.append(f"{rel}:1: forbidden direct assertion token present: {tok}")
    return violations


def _scan_spec_lang_pure_no_effect_builtins(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("spec_lang_purity")
    if not isinstance(cfg, dict):
        return ["runtime.spec_lang_pure_no_effect_builtins requires harness.spec_lang_purity mapping in governance spec"]

    files = cfg.get("files")
    forbidden_tokens = cfg.get("forbidden_tokens")
    if not isinstance(files, list) or not files or any(not isinstance(x, str) or not x.strip() for x in files):
        return ["harness.spec_lang_purity.files must be a non-empty list of non-empty strings"]
    if (
        not isinstance(forbidden_tokens, list)
        or not forbidden_tokens
        or any(not isinstance(x, str) or not x.strip() for x in forbidden_tokens)
    ):
        return ["harness.spec_lang_purity.forbidden_tokens must be a non-empty list of non-empty strings"]

    violations: list[str] = []
    for rel in files:
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing spec-lang implementation file")
            continue
        raw = p.read_text(encoding="utf-8")
        for tok in forbidden_tokens:
            if tok in raw:
                violations.append(f"{rel}:1: forbidden side-effect token in spec-lang core: {tok}")
    return violations


def _scan_runtime_orchestration_policy_via_spec_lang(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("orchestration_policy")
    if not isinstance(cfg, dict):
        return [
            "runtime.orchestration_policy_via_spec_lang requires harness.orchestration_policy mapping in governance spec"
        ]
    files = cfg.get("files")
    required_tokens = cfg.get("required_tokens", [])
    forbidden_tokens = cfg.get("forbidden_tokens", [])
    if not isinstance(files, list) or not files:
        return ["harness.orchestration_policy.files must be a non-empty list"]
    if not isinstance(required_tokens, list) or any(not isinstance(x, str) or not x.strip() for x in required_tokens):
        return ["harness.orchestration_policy.required_tokens must be a list of non-empty strings"]
    if not isinstance(forbidden_tokens, list) or any(not isinstance(x, str) or not x.strip() for x in forbidden_tokens):
        return ["harness.orchestration_policy.forbidden_tokens must be a list of non-empty strings"]

    violations: list[str] = []
    for entry in files:
        file_required = required_tokens
        file_forbidden = forbidden_tokens
        if isinstance(entry, str) and entry.strip():
            rel = entry.strip()
        elif isinstance(entry, dict):
            rel = str(entry.get("path", "")).strip()
            if not rel:
                violations.append("harness.orchestration_policy.files[].path must be non-empty")
                continue
            raw_required = entry.get("required_tokens")
            if raw_required is not None:
                if not isinstance(raw_required, list) or any(
                    not isinstance(x, str) or not x.strip() for x in raw_required
                ):
                    violations.append(f"{rel}:1: files[].required_tokens must be list of non-empty strings")
                    continue
                file_required = raw_required
            raw_forbidden = entry.get("forbidden_tokens")
            if raw_forbidden is not None:
                if not isinstance(raw_forbidden, list) or any(
                    not isinstance(x, str) or not x.strip() for x in raw_forbidden
                ):
                    violations.append(f"{rel}:1: files[].forbidden_tokens must be list of non-empty strings")
                    continue
                file_forbidden = raw_forbidden
        else:
            violations.append("harness.orchestration_policy.files entries must be strings or mappings")
            continue
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing orchestration file")
            continue
        raw = p.read_text(encoding="utf-8")
        for tok in file_required:
            if tok not in raw:
                violations.append(f"{rel}:1: missing required orchestration spec-lang token: {tok}")
        for tok in file_forbidden:
            if tok in raw:
                violations.append(f"{rel}:1: forbidden hardcoded orchestration verdict token present: {tok}")
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


def _scan_conformance_purpose_quality_gate(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("purpose_quality")
    if not isinstance(cfg, dict):
        return ["conformance.purpose_quality_gate requires harness.purpose_quality mapping in governance spec"]
    cases_rel = str(cfg.get("cases", "docs/spec/conformance/cases")).strip() or "docs/spec/conformance/cases"
    cases_dir = _join_contract_path(root, cases_rel)
    if not cases_dir.exists():
        return [f"{cases_rel}:1: conformance cases path does not exist"]
    max_total_warnings = int(cfg.get("max_total_warnings", 0))
    fail_on_policy_errors = bool(cfg.get("fail_on_policy_errors", True))
    fail_on_severity = str(cfg.get("fail_on_severity", "")).strip().lower()
    if fail_on_severity and fail_on_severity not in {"warn", "error"}:
        return ["harness.purpose_quality.fail_on_severity must be one of: warn, error"]
    payload = conformance_purpose_report_jsonable(cases_dir, repo_root=root)
    summary = payload.get("summary") or {}
    total_warning_count = int(summary.get("total_warning_count", 0))
    policy_error_count = int(summary.get("policy_error_count", 0))
    severity_counts = summary.get("warning_severity_counts") or {}
    warn_count = int(severity_counts.get("warn", 0))
    error_count = int(severity_counts.get("error", 0))
    violations: list[str] = []
    if fail_on_policy_errors and policy_error_count > 0:
        violations.append(
            f"docs/spec/conformance/purpose_lint_v1.yaml:1: policy error count {policy_error_count} > 0"
        )
    if total_warning_count > max_total_warnings:
        violations.append(
            f"{cases_rel}:1: total purpose warnings {total_warning_count} exceed max_total_warnings={max_total_warnings}"
        )
    if fail_on_severity:
        at_or_above = error_count if fail_on_severity == "error" else (warn_count + error_count)
        if at_or_above > 0:
            violations.append(
                f"{cases_rel}:1: warnings at or above severity '{fail_on_severity}' = {at_or_above}"
            )
    return violations


def _scan_contract_coverage_threshold(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("contract_coverage")
    if not isinstance(cfg, dict):
        return ["contract.coverage_threshold requires harness.contract_coverage mapping in governance spec"]
    require_all_must = bool(cfg.get("require_all_must_covered", True))
    min_coverage_ratio = float(cfg.get("min_coverage_ratio", 0.0))
    payload = contract_coverage_jsonable(root)
    summary = payload.get("summary") or {}
    must_rules = int(summary.get("must_rules", 0))
    must_covered = int(summary.get("must_covered", 0))
    coverage_ratio = float(summary.get("coverage_ratio", 0.0))
    violations: list[str] = []
    if require_all_must and must_covered != must_rules:
        violations.append(
            "docs/spec/contract/traceability_v1.yaml:1: "
            f"must_covered={must_covered} does not equal must_rules={must_rules}"
        )
    if coverage_ratio < min_coverage_ratio:
        violations.append(
            "docs/spec/contract/traceability_v1.yaml:1: "
            f"coverage_ratio={coverage_ratio:.4f} below min_coverage_ratio={min_coverage_ratio:.4f}"
        )
    return violations


def _scan_spec_portability_metric(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("portability_metric")
    if not isinstance(cfg, dict):
        return ["spec.portability_metric requires harness.portability_metric mapping in governance spec"]
    policy_evaluate = None
    if "policy_evaluate" in cfg:
        try:
            policy_evaluate = normalize_policy_evaluate(
                cfg.get("policy_evaluate"), field="harness.portability_metric.policy_evaluate"
            )
        except ValueError as exc:
            return [str(exc)]
    payload = spec_portability_report_jsonable(root, config=cfg)
    errs = payload.get("errors") or []
    if not isinstance(errs, list):
        return ["spec.portability_metric report contains invalid errors shape"]
    violations = [str(e) for e in errs if str(e).strip()]
    return _policy_outcome(
        subject=payload,
        policy_evaluate=policy_evaluate,
        policy_path="harness.portability_metric.policy_evaluate",
        violations=violations,
    )


def _lookup_number_field(payload: object, dotted: str) -> float | None:
    cur = payload
    for part in dotted.split("."):
        key = part.strip()
        if not key:
            return None
        if not isinstance(cur, dict) or key not in cur:
            return None
        cur = cur[key]
    if isinstance(cur, (int, float)):
        return float(cur)
    return None


def _scan_spec_portability_non_regression(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("portability_non_regression")
    if not isinstance(cfg, dict):
        return ["spec.portability_non_regression requires harness.portability_non_regression mapping in governance spec"]

    baseline_path = str(cfg.get("baseline_path", "")).strip()
    if not baseline_path:
        return ["harness.portability_non_regression.baseline_path must be a non-empty string"]
    summary_fields = cfg.get("summary_fields")
    if (
        not isinstance(summary_fields, list)
        or not summary_fields
        or any(not isinstance(x, str) or not x.strip() for x in summary_fields)
    ):
        return ["harness.portability_non_regression.summary_fields must be a non-empty list of non-empty strings"]
    segment_fields = cfg.get("segment_fields", {})
    if not isinstance(segment_fields, dict):
        return ["harness.portability_non_regression.segment_fields must be a mapping"]
    for seg, fields in segment_fields.items():
        if not isinstance(seg, str) or not seg.strip():
            return ["harness.portability_non_regression.segment_fields keys must be non-empty strings"]
        if not isinstance(fields, list) or not fields or any(not isinstance(x, str) or not x.strip() for x in fields):
            return [
                f"harness.portability_non_regression.segment_fields.{seg} must be a non-empty list of non-empty strings"
            ]
    epsilon_raw = cfg.get("epsilon", 1e-12)
    try:
        epsilon = float(epsilon_raw)
    except (TypeError, ValueError):
        return ["harness.portability_non_regression.epsilon must be numeric"]
    if epsilon < 0:
        return ["harness.portability_non_regression.epsilon must be >= 0"]

    report_config = cfg.get("portability_metric")
    if report_config is not None and not isinstance(report_config, dict):
        return ["harness.portability_non_regression.portability_metric must be a mapping when provided"]
    current = spec_portability_report_jsonable(root, config=report_config)
    current_errs = current.get("errors") or []
    if isinstance(current_errs, list) and any(str(e).strip() for e in current_errs):
        return [f"current portability report has errors: {str(e)}" for e in current_errs if str(e).strip()]

    baseline_file = _join_contract_path(root, baseline_path)
    if not baseline_file.exists():
        return [f"{baseline_path}:1: missing baseline portability metrics file"]
    try:
        baseline = json.loads(baseline_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{baseline_path}:1: invalid JSON baseline: {exc.msg} at line {exc.lineno} column {exc.colno}"]
    if not isinstance(baseline, dict):
        return [f"{baseline_path}:1: baseline payload must be a JSON object"]

    violations: list[str] = []
    for field in summary_fields:
        cur_val = _lookup_number_field(current, f"summary.{field}")
        base_val = _lookup_number_field(baseline, f"summary.{field}")
        if cur_val is None:
            violations.append(f"summary.{field}: missing numeric current metric")
            continue
        if base_val is None:
            violations.append(f"{baseline_path}: summary.{field}: missing numeric baseline metric")
            continue
        if cur_val + epsilon < base_val:
            violations.append(
                f"summary.{field}: regressed from baseline {base_val:.12g} to {cur_val:.12g}"
            )

    for segment, fields in segment_fields.items():
        for field in fields:
            cur_val = _lookup_number_field(current, f"segments.{segment}.{field}")
            base_val = _lookup_number_field(baseline, f"segments.{segment}.{field}")
            if cur_val is None:
                violations.append(f"segments.{segment}.{field}: missing numeric current metric")
                continue
            if base_val is None:
                violations.append(f"{baseline_path}: segments.{segment}.{field}: missing numeric baseline metric")
                continue
            if cur_val + epsilon < base_val:
                violations.append(
                    f"segments.{segment}.{field}: regressed from baseline {base_val:.12g} to {cur_val:.12g}"
                )
    return violations


def _scan_spec_lang_adoption_metric(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("spec_lang_adoption")
    if not isinstance(cfg, dict):
        return ["spec.spec_lang_adoption_metric requires harness.spec_lang_adoption mapping in governance spec"]
    policy_evaluate = None
    if "policy_evaluate" in cfg:
        try:
            policy_evaluate = normalize_policy_evaluate(
                cfg.get("policy_evaluate"), field="harness.spec_lang_adoption.policy_evaluate"
            )
        except ValueError as exc:
            return [str(exc)]
    payload = spec_lang_adoption_report_jsonable(root, config=cfg)
    errs = payload.get("errors") or []
    if not isinstance(errs, list):
        return ["spec.spec_lang_adoption_metric report contains invalid errors shape"]
    violations = [str(e) for e in errs if str(e).strip()]
    return _policy_outcome(
        subject=payload,
        policy_evaluate=policy_evaluate,
        policy_path="harness.spec_lang_adoption.policy_evaluate",
        violations=violations,
    )


def _scan_spec_lang_adoption_non_regression(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("spec_lang_adoption_non_regression")
    if not isinstance(cfg, dict):
        return [
            "spec.spec_lang_adoption_non_regression requires harness.spec_lang_adoption_non_regression mapping in governance spec"
        ]
    baseline_path = str(cfg.get("baseline_path", "")).strip()
    if not baseline_path:
        return ["harness.spec_lang_adoption_non_regression.baseline_path must be a non-empty string"]
    report_cfg = cfg.get("spec_lang_adoption")
    if report_cfg is not None and not isinstance(report_cfg, dict):
        return ["harness.spec_lang_adoption_non_regression.spec_lang_adoption must be a mapping when provided"]
    epsilon_raw = cfg.get("epsilon", 1e-12)
    try:
        epsilon = float(epsilon_raw)
    except (TypeError, ValueError):
        return ["harness.spec_lang_adoption_non_regression.epsilon must be numeric"]
    if epsilon < 0:
        return ["harness.spec_lang_adoption_non_regression.epsilon must be >= 0"]

    current = spec_lang_adoption_report_jsonable(root, config=report_cfg)
    current_errs = current.get("errors") or []
    if isinstance(current_errs, list) and any(str(e).strip() for e in current_errs):
        return [f"current spec-lang adoption report has errors: {str(e)}" for e in current_errs if str(e).strip()]
    baseline, baseline_errs = _load_baseline_json(root, baseline_path)
    if baseline is None:
        return baseline_errs
    return compare_metric_non_regression(
        current=current,
        baseline=baseline,
        summary_fields=cfg.get("summary_fields"),
        segment_fields=cfg.get("segment_fields", {}),
        epsilon=epsilon,
    )


def _scan_conformance_evaluate_first_ratio_non_regression(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("conformance_evaluate_first_non_regression")
    if not isinstance(cfg, dict):
        return [
            "conformance.evaluate_first_ratio_non_regression requires harness.conformance_evaluate_first_non_regression mapping in governance spec"
        ]
    baseline_path = str(cfg.get("baseline_path", "")).strip()
    if not baseline_path:
        return ["harness.conformance_evaluate_first_non_regression.baseline_path must be a non-empty string"]
    report_cfg = cfg.get("spec_lang_adoption")
    if report_cfg is not None and not isinstance(report_cfg, dict):
        return ["harness.conformance_evaluate_first_non_regression.spec_lang_adoption must be a mapping when provided"]
    epsilon_raw = cfg.get("epsilon", 1e-12)
    try:
        epsilon = float(epsilon_raw)
    except (TypeError, ValueError):
        return ["harness.conformance_evaluate_first_non_regression.epsilon must be numeric"]
    if epsilon < 0:
        return ["harness.conformance_evaluate_first_non_regression.epsilon must be >= 0"]

    current = spec_lang_adoption_report_jsonable(root, config=report_cfg)
    current_errs = current.get("errors") or []
    if isinstance(current_errs, list) and any(str(e).strip() for e in current_errs):
        return [f"current spec-lang adoption report has errors: {str(e)}" for e in current_errs if str(e).strip()]
    baseline, baseline_errs = _load_baseline_json(root, baseline_path)
    if baseline is None:
        return baseline_errs
    return compare_metric_non_regression(
        current=current,
        baseline=baseline,
        summary_fields=cfg.get(
            "summary_fields",
            {"overall_logic_self_contained_ratio": "non_decrease"},
        ),
        segment_fields=cfg.get(
            "segment_fields",
            {"conformance": {"mean_logic_self_contained_ratio": "non_decrease"}},
        ),
        epsilon=epsilon,
    )


def _scan_policy_library_usage_non_regression(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("policy_library_usage_non_regression")
    if not isinstance(cfg, dict):
        return [
            "governance.policy_library_usage_non_regression requires harness.policy_library_usage_non_regression mapping in governance spec"
        ]
    baseline_path = str(cfg.get("baseline_path", "")).strip()
    if not baseline_path:
        return ["harness.policy_library_usage_non_regression.baseline_path must be a non-empty string"]
    report_cfg = cfg.get("spec_lang_adoption")
    if report_cfg is not None and not isinstance(report_cfg, dict):
        return ["harness.policy_library_usage_non_regression.spec_lang_adoption must be a mapping when provided"]
    epsilon_raw = cfg.get("epsilon", 1e-12)
    try:
        epsilon = float(epsilon_raw)
    except (TypeError, ValueError):
        return ["harness.policy_library_usage_non_regression.epsilon must be numeric"]
    if epsilon < 0:
        return ["harness.policy_library_usage_non_regression.epsilon must be >= 0"]

    current = spec_lang_adoption_report_jsonable(root, config=report_cfg)
    current_errs = current.get("errors") or []
    if isinstance(current_errs, list) and any(str(e).strip() for e in current_errs):
        return [f"current spec-lang adoption report has errors: {str(e)}" for e in current_errs if str(e).strip()]
    baseline, baseline_errs = _load_baseline_json(root, baseline_path)
    if baseline is None:
        return baseline_errs
    return compare_metric_non_regression(
        current=current,
        baseline=baseline,
        summary_fields=cfg.get(
            "summary_fields",
            {"governance_library_backed_policy_ratio": "non_decrease"},
        ),
        segment_fields=cfg.get(
            "segment_fields",
            {"governance": {"library_backed_policy_ratio": "non_decrease"}},
        ),
        epsilon=epsilon,
    )


def _scan_runner_independence_metric(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("runner_independence")
    if not isinstance(cfg, dict):
        return ["runtime.runner_independence_metric requires harness.runner_independence mapping in governance spec"]
    policy_evaluate = None
    if "policy_evaluate" in cfg:
        try:
            policy_evaluate = normalize_policy_evaluate(
                cfg.get("policy_evaluate"), field="harness.runner_independence.policy_evaluate"
            )
        except ValueError as exc:
            return [str(exc)]
    payload = runner_independence_report_jsonable(root, config=cfg)
    errs = payload.get("errors") or []
    if not isinstance(errs, list):
        return ["runtime.runner_independence_metric report contains invalid errors shape"]
    violations = [str(e) for e in errs if str(e).strip()]
    return _policy_outcome(
        subject=payload,
        policy_evaluate=policy_evaluate,
        policy_path="harness.runner_independence.policy_evaluate",
        violations=violations,
    )


def _scan_runner_independence_non_regression(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("runner_independence_non_regression")
    if not isinstance(cfg, dict):
        return [
            "runtime.runner_independence_non_regression requires harness.runner_independence_non_regression mapping in governance spec"
        ]
    baseline_path = str(cfg.get("baseline_path", "")).strip()
    if not baseline_path:
        return ["harness.runner_independence_non_regression.baseline_path must be a non-empty string"]
    report_cfg = cfg.get("runner_independence")
    if report_cfg is not None and not isinstance(report_cfg, dict):
        return ["harness.runner_independence_non_regression.runner_independence must be a mapping when provided"]
    epsilon_raw = cfg.get("epsilon", 1e-12)
    try:
        epsilon = float(epsilon_raw)
    except (TypeError, ValueError):
        return ["harness.runner_independence_non_regression.epsilon must be numeric"]
    if epsilon < 0:
        return ["harness.runner_independence_non_regression.epsilon must be >= 0"]

    current = runner_independence_report_jsonable(root, config=report_cfg)
    current_errs = current.get("errors") or []
    if isinstance(current_errs, list) and any(str(e).strip() for e in current_errs):
        return [f"current runner independence report has errors: {str(e)}" for e in current_errs if str(e).strip()]
    baseline, baseline_errs = _load_baseline_json(root, baseline_path)
    if baseline is None:
        return baseline_errs
    return compare_metric_non_regression(
        current=current,
        baseline=baseline,
        summary_fields=cfg.get("summary_fields"),
        segment_fields=cfg.get("segment_fields", {}),
        epsilon=epsilon,
    )


def _scan_python_dependency_metric(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("python_dependency")
    if not isinstance(cfg, dict):
        return ["runtime.python_dependency_metric requires harness.python_dependency mapping in governance spec"]
    policy_evaluate = None
    if "policy_evaluate" in cfg:
        try:
            policy_evaluate = normalize_policy_evaluate(
                cfg.get("policy_evaluate"), field="harness.python_dependency.policy_evaluate"
            )
        except ValueError as exc:
            return [str(exc)]
    payload = python_dependency_report_jsonable(root, config=cfg)
    errs = payload.get("errors") or []
    if not isinstance(errs, list):
        return ["runtime.python_dependency_metric report contains invalid errors shape"]
    violations = [str(e) for e in errs if str(e).strip()]
    return _policy_outcome(
        subject=payload,
        policy_evaluate=policy_evaluate,
        policy_path="harness.python_dependency.policy_evaluate",
        violations=violations,
    )


def _scan_python_dependency_non_regression(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("python_dependency_non_regression")
    if not isinstance(cfg, dict):
        return [
            "runtime.python_dependency_non_regression requires harness.python_dependency_non_regression mapping in governance spec"
        ]
    baseline_path = str(cfg.get("baseline_path", "")).strip()
    if not baseline_path:
        return ["harness.python_dependency_non_regression.baseline_path must be a non-empty string"]
    report_cfg = cfg.get("python_dependency")
    if report_cfg is not None and not isinstance(report_cfg, dict):
        return ["harness.python_dependency_non_regression.python_dependency must be a mapping when provided"]
    epsilon_raw = cfg.get("epsilon", 1e-12)
    try:
        epsilon = float(epsilon_raw)
    except (TypeError, ValueError):
        return ["harness.python_dependency_non_regression.epsilon must be numeric"]
    if epsilon < 0:
        return ["harness.python_dependency_non_regression.epsilon must be >= 0"]

    current = python_dependency_report_jsonable(root, config=report_cfg)
    current_errs = current.get("errors") or []
    if isinstance(current_errs, list) and any(str(e).strip() for e in current_errs):
        return [f"current python dependency report has errors: {str(e)}" for e in current_errs if str(e).strip()]
    baseline, baseline_errs = _load_baseline_json(root, baseline_path)
    if baseline is None:
        return baseline_errs
    return compare_metric_non_regression(
        current=current,
        baseline=baseline,
        summary_fields=cfg.get("summary_fields"),
        segment_fields=cfg.get("segment_fields", {}),
        epsilon=epsilon,
    )


def _scan_docs_operability_metric(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("docs_operability")
    if not isinstance(cfg, dict):
        return ["docs.operability_metric requires harness.docs_operability mapping in governance spec"]
    policy_evaluate = None
    if "policy_evaluate" in cfg:
        try:
            policy_evaluate = normalize_policy_evaluate(
                cfg.get("policy_evaluate"), field="harness.docs_operability.policy_evaluate"
            )
        except ValueError as exc:
            return [str(exc)]
    payload = docs_operability_report_jsonable(root, config=cfg)
    errs = payload.get("errors") or []
    if not isinstance(errs, list):
        return ["docs.operability_metric report contains invalid errors shape"]
    violations = [str(e) for e in errs if str(e).strip()]
    return _policy_outcome(
        subject=payload,
        policy_evaluate=policy_evaluate,
        policy_path="harness.docs_operability.policy_evaluate",
        violations=violations,
    )


def _scan_docs_operability_non_regression(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("docs_operability_non_regression")
    if not isinstance(cfg, dict):
        return ["docs.operability_non_regression requires harness.docs_operability_non_regression mapping in governance spec"]
    baseline_path = str(cfg.get("baseline_path", "")).strip()
    if not baseline_path:
        return ["harness.docs_operability_non_regression.baseline_path must be a non-empty string"]
    report_cfg = cfg.get("docs_operability")
    if report_cfg is not None and not isinstance(report_cfg, dict):
        return ["harness.docs_operability_non_regression.docs_operability must be a mapping when provided"]
    epsilon_raw = cfg.get("epsilon", 1e-12)
    try:
        epsilon = float(epsilon_raw)
    except (TypeError, ValueError):
        return ["harness.docs_operability_non_regression.epsilon must be numeric"]
    if epsilon < 0:
        return ["harness.docs_operability_non_regression.epsilon must be >= 0"]

    current = docs_operability_report_jsonable(root, config=report_cfg)
    current_errs = current.get("errors") or []
    if isinstance(current_errs, list) and any(str(e).strip() for e in current_errs):
        return [f"current docs operability report has errors: {str(e)}" for e in current_errs if str(e).strip()]
    baseline, baseline_errs = _load_baseline_json(root, baseline_path)
    if baseline is None:
        return baseline_errs
    return compare_metric_non_regression(
        current=current,
        baseline=baseline,
        summary_fields=cfg.get("summary_fields"),
        segment_fields=cfg.get("segment_fields", {}),
        epsilon=epsilon,
    )


def _scan_contract_assertions_metric(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("contract_assertions")
    if not isinstance(cfg, dict):
        return ["spec.contract_assertions_metric requires harness.contract_assertions mapping in governance spec"]
    policy_evaluate = None
    if "policy_evaluate" in cfg:
        try:
            policy_evaluate = normalize_policy_evaluate(
                cfg.get("policy_evaluate"), field="harness.contract_assertions.policy_evaluate"
            )
        except ValueError as exc:
            return [str(exc)]
    payload = contract_assertions_report_jsonable(root, config=cfg)
    errs = payload.get("errors") or []
    if not isinstance(errs, list):
        return ["spec.contract_assertions_metric report contains invalid errors shape"]
    violations = [str(e) for e in errs if str(e).strip()]
    return _policy_outcome(
        subject=payload,
        policy_evaluate=policy_evaluate,
        policy_path="harness.contract_assertions.policy_evaluate",
        violations=violations,
    )


def _scan_contract_assertions_non_regression(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("contract_assertions_non_regression")
    if not isinstance(cfg, dict):
        return [
            "spec.contract_assertions_non_regression requires harness.contract_assertions_non_regression mapping in governance spec"
        ]
    baseline_path = str(cfg.get("baseline_path", "")).strip()
    if not baseline_path:
        return ["harness.contract_assertions_non_regression.baseline_path must be a non-empty string"]
    report_cfg = cfg.get("contract_assertions")
    if report_cfg is not None and not isinstance(report_cfg, dict):
        return ["harness.contract_assertions_non_regression.contract_assertions must be a mapping when provided"]
    epsilon_raw = cfg.get("epsilon", 1e-12)
    try:
        epsilon = float(epsilon_raw)
    except (TypeError, ValueError):
        return ["harness.contract_assertions_non_regression.epsilon must be numeric"]
    if epsilon < 0:
        return ["harness.contract_assertions_non_regression.epsilon must be >= 0"]

    current = contract_assertions_report_jsonable(root, config=report_cfg)
    current_errs = current.get("errors") or []
    if isinstance(current_errs, list) and any(str(e).strip() for e in current_errs):
        return [f"current contract assertions report has errors: {str(e)}" for e in current_errs if str(e).strip()]
    baseline, baseline_errs = _load_baseline_json(root, baseline_path)
    if baseline is None:
        return baseline_errs
    return compare_metric_non_regression(
        current=current,
        baseline=baseline,
        summary_fields=cfg.get("summary_fields"),
        segment_fields=cfg.get("segment_fields", {}),
        epsilon=epsilon,
    )


def _scan_objective_scorecard_metric(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("objective_scorecard")
    if not isinstance(cfg, dict):
        return ["objective.scorecard_metric requires harness.objective_scorecard mapping in governance spec"]
    policy_evaluate = None
    if "policy_evaluate" in cfg:
        try:
            policy_evaluate = normalize_policy_evaluate(
                cfg.get("policy_evaluate"), field="harness.objective_scorecard.policy_evaluate"
            )
        except ValueError as exc:
            return [str(exc)]
    payload = objective_scorecard_report_jsonable(root, config=cfg)
    errs = payload.get("errors") or []
    if not isinstance(errs, list):
        return ["objective.scorecard_metric report contains invalid errors shape"]
    violations = [str(e) for e in errs if str(e).strip()]
    return _policy_outcome(
        subject=payload,
        policy_evaluate=policy_evaluate,
        policy_path="harness.objective_scorecard.policy_evaluate",
        violations=violations,
    )


def _scan_objective_scorecard_non_regression(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("objective_scorecard_non_regression")
    if not isinstance(cfg, dict):
        return [
            "objective.scorecard_non_regression requires harness.objective_scorecard_non_regression mapping in governance spec"
        ]
    baseline_path = str(cfg.get("baseline_path", "")).strip()
    if not baseline_path:
        return ["harness.objective_scorecard_non_regression.baseline_path must be a non-empty string"]
    report_cfg = cfg.get("objective_scorecard")
    if report_cfg is not None and not isinstance(report_cfg, dict):
        return ["harness.objective_scorecard_non_regression.objective_scorecard must be a mapping when provided"]
    epsilon_raw = cfg.get("epsilon", 1e-12)
    try:
        epsilon = float(epsilon_raw)
    except (TypeError, ValueError):
        return ["harness.objective_scorecard_non_regression.epsilon must be numeric"]
    if epsilon < 0:
        return ["harness.objective_scorecard_non_regression.epsilon must be >= 0"]

    current = objective_scorecard_report_jsonable(root, config=report_cfg)
    current_errs = current.get("errors") or []
    if isinstance(current_errs, list) and any(str(e).strip() for e in current_errs):
        return [f"current objective scorecard report has errors: {str(e)}" for e in current_errs if str(e).strip()]

    baseline, baseline_errs = _load_baseline_json(root, baseline_path)
    if baseline is None:
        return baseline_errs

    note_cfg = cfg.get("baseline_notes")
    if isinstance(note_cfg, dict):
        notes_path = str(note_cfg.get("path", "")).strip()
        baseline_paths = note_cfg.get("baseline_paths")
        if not notes_path:
            return ["harness.objective_scorecard_non_regression.baseline_notes.path must be non-empty"]
        if (
            not isinstance(baseline_paths, list)
            or not baseline_paths
            or any(not isinstance(x, str) or not x.strip() for x in baseline_paths)
        ):
            return [
                "harness.objective_scorecard_non_regression.baseline_notes.baseline_paths must be a non-empty list"
            ]
        note_violations = validate_metric_baseline_notes(
            root,
            notes_path=notes_path,
            baseline_paths=[str(x).strip() for x in baseline_paths],
        )
        if note_violations:
            return note_violations

    return compare_metric_non_regression(
        current=current,
        baseline=baseline,
        summary_fields=cfg.get("summary_fields"),
        segment_fields=cfg.get("segment_fields", {}),
        epsilon=epsilon,
    )


def _scan_objective_tripwires_clean(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("objective_tripwires")
    if not isinstance(cfg, dict):
        return ["objective.tripwires_clean requires harness.objective_tripwires mapping in governance spec"]
    manifest_path = str(cfg.get("manifest_path", "")).strip() or "docs/spec/metrics/objective_manifest.yaml"
    cases_path = str(cfg.get("cases_path", "")).strip() or "docs/spec/governance/cases"
    case_file_pattern = str(cfg.get("case_file_pattern", "")).strip() or SETTINGS.case.default_file_pattern

    manifest_file = _join_contract_path(root, manifest_path)
    if not manifest_file.exists():
        return [f"{manifest_path}:1: missing objective manifest"]
    try:
        manifest = yaml.safe_load(manifest_file.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        return [f"{manifest_path}:1: invalid YAML: {exc}"]
    if not isinstance(manifest, dict):
        return [f"{manifest_path}:1: manifest must be a mapping"]

    objectives = manifest.get("objectives")
    if not isinstance(objectives, list):
        return [f"{manifest_path}:1: objectives must be a list"]

    check_ids: set[str] = set()
    for row in objectives:
        if not isinstance(row, dict):
            continue
        tripwires = row.get("tripwires")
        if not isinstance(tripwires, list):
            continue
        for tw in tripwires:
            if not isinstance(tw, dict):
                continue
            cid = str(tw.get("check_id", "")).strip()
            if cid:
                check_ids.add(cid)

    if not check_ids:
        return [f"{manifest_path}:1: no tripwire check_id entries found"]

    cases_dir = _join_contract_path(root, cases_path)
    if not cases_dir.exists() or not cases_dir.is_dir():
        return [f"{cases_path}:1: cases path does not exist"]

    check_to_cases: dict[str, list[dict]] = {}
    for spec in iter_cases(cases_dir, file_pattern=case_file_pattern):
        case = spec.test if isinstance(spec.test, dict) else {}
        case_check = str(case.get("check", "")).strip()
        if case_check:
            check_to_cases.setdefault(case_check, []).append(case)

    violations: list[str] = []
    for cid in sorted(check_ids):
        if cid in {
            "objective.tripwires_clean",
            "objective.scorecard_metric",
            "objective.scorecard_non_regression",
        }:
            continue
        fn = _CHECKS.get(cid)
        if fn is None:
            violations.append(f"{manifest_path}:1: tripwire references unknown check id {cid}")
            continue
        cases = check_to_cases.get(cid, [])
        if not cases:
            violations.append(f"{cases_path}:1: no governance case found for tripwire check {cid}")
            continue
        matched = False
        for case in cases:
            harness_case = case.get("harness") if isinstance(case.get("harness"), dict) else {}
            local_harness = dict(harness_case)
            local_harness["root"] = str(root)
            params = inspect.signature(fn).parameters
            outcome = fn(root, harness=local_harness) if "harness" in params else fn(root)
            if isinstance(outcome, dict):
                out_violations = outcome.get("violations")
                case_violations = [str(v) for v in out_violations if str(v).strip()] if isinstance(out_violations, list) else []
            else:
                case_violations = [str(v) for v in outcome if str(v).strip()]
            if not case_violations:
                matched = True
                break
        if not matched:
            violations.append(f"tripwire check {cid} is failing in all matching governance cases")
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


def _scan_assert_universal_core_sync(root: Path) -> list[str]:
    violations: list[str] = []
    required_tokens_by_file: dict[str, tuple[object, ...]] = {
        "docs/spec/schema/schema_v1.md": (
            "universal core",
            "evaluate",
            ("conformance/cases/*.spec.md", "conformance/cases/**/*.spec.md"),
            ("governance/cases/*.spec.md", "governance/cases/**/*.spec.md"),
            "must use",
        ),
        "docs/spec/contract/03_assertions.md": (
            "universal core",
            "evaluate",
            ("conformance/cases/*.spec.md", "conformance/cases/**/*.spec.md"),
            ("governance/cases/*.spec.md", "governance/cases/**/*.spec.md"),
            "must use",
        ),
        "docs/spec/contract/09_internal_representation.md": (
            "universal core",
            "evaluate",
            "evaluate-only",
            "conformance",
            "governance",
        ),
    }
    for rel in _ASSERT_UNIVERSAL_DOC_FILES:
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing assertion universal-core doc")
            continue
        lower = p.read_text(encoding="utf-8").lower()
        for tok in required_tokens_by_file.get(rel, ()):
            if isinstance(tok, tuple):
                if not any(str(opt) in lower for opt in tok):
                    joined = " or ".join(repr(str(opt)) for opt in tok)
                    violations.append(f"{rel}:1: missing universal-core token ({joined})")
                continue
            if str(tok) not in lower:
                violations.append(f"{rel}:1: missing universal-core token {tok!r}")
    return violations


def _scan_assert_sugar_compile_only_sync(root: Path) -> list[str]:
    violations: list[str] = []
    compiler_path = root / "spec_runner/compiler.py"
    assertions_path = root / "spec_runner/assertions.py"
    if not compiler_path.exists():
        violations.append("spec_runner/compiler.py:1: missing compiler implementation")
        return violations
    if not assertions_path.exists():
        violations.append("spec_runner/assertions.py:1: missing assertions implementation")
        return violations

    compiler_raw = compiler_path.read_text(encoding="utf-8")
    assertions_raw = assertions_path.read_text(encoding="utf-8")

    compiler_required = (
        'supported = {"evaluate"}',
        'op == "evaluate"',
    )
    for tok in compiler_required:
        if tok not in compiler_raw:
            violations.append(
                f"spec_runner/compiler.py:1: missing compile-only sugar mapping token {tok}"
            )

    compiler_forbidden = (
        "if type_name == ",
        "allowed = {",
        'op == "contain"',
        'op == "regex"',
        'op == "json_type"',
        'op == "exists"',
    )
    for tok in compiler_forbidden:
        if tok in compiler_raw:
            violations.append(
                f"spec_runner/compiler.py:1: forbidden per-type operator allowlist token {tok}"
            )

    if "eval_predicate(" not in assertions_raw:
        violations.append(
            "spec_runner/assertions.py:1: missing spec-lang predicate evaluation call"
        )
    return violations


def _scan_assert_type_contract_subject_semantics_sync(root: Path) -> list[str]:
    violations: list[str] = []
    files = (
        "docs/spec/contract/04_harness.md",
        "docs/spec/contract/types/text_file.md",
        "docs/spec/contract/types/cli_run.md",
        "docs/spec/contract/types/api_http.md",
    )
    required_tokens = {
        "docs/spec/contract/04_harness.md": ("subject", "availability", "shape"),
        "docs/spec/contract/types/text_file.md": ("subject semantics",),
        "docs/spec/contract/types/cli_run.md": ("target semantics",),
        "docs/spec/contract/types/api_http.md": ("target semantics",),
    }
    forbidden_tokens = {
        "docs/spec/contract/types/cli_run.md": ("only supports `exists`",),
    }
    for rel in files:
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing type/harness contract doc")
            continue
        lower = p.read_text(encoding="utf-8").lower()
        for tok in required_tokens.get(rel, ()):
            if tok not in lower:
                violations.append(f"{rel}:1: missing required subject-semantics token {tok!r}")
        for tok in forbidden_tokens.get(rel, ()):
            if tok in lower:
                violations.append(f"{rel}:1: forbidden per-operator allowlist token {tok!r}")
    return violations


def _scan_assert_compiler_schema_matrix_sync(root: Path) -> list[str]:
    violations: list[str] = []
    compiler = root / "spec_runner/compiler.py"
    schema = root / "docs/spec/schema/schema_v1.md"
    assertions_doc = root / "docs/spec/contract/03_assertions.md"
    if not compiler.exists() or not schema.exists() or not assertions_doc.exists():
        return ["assert.compiler_schema_matrix_sync requires compiler + schema + assertion contract docs"]
    compiler_raw = compiler.read_text(encoding="utf-8")
    schema_lower = schema.read_text(encoding="utf-8").lower()
    assertions_lower = assertions_doc.read_text(encoding="utf-8").lower()

    if "universal core operator" not in schema_lower:
        violations.append("docs/spec/schema/schema_v1.md:1: missing universal core operator section")
    if "only universal assertion operator contract" not in assertions_lower:
        violations.append("docs/spec/contract/03_assertions.md:1: missing universal evaluate-only contract text")
    if 'supported = {"evaluate"}' not in compiler_raw:
        violations.append("spec_runner/compiler.py:1: compiler operator matrix does not match universal-core contract")
    if "if type_name == " in compiler_raw:
        violations.append("spec_runner/compiler.py:1: forbidden per-type operator matrix branching present")
    return violations


def _scan_assert_spec_lang_builtin_surface_sync(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    cfg = h.get("spec_lang_builtin_sync")
    if not isinstance(cfg, dict):
        return [
            "assert.spec_lang_builtin_surface_sync requires harness.spec_lang_builtin_sync mapping in governance spec"
        ]
    required_ops = cfg.get("required_ops")
    if (
        not isinstance(required_ops, list)
        or not required_ops
        or any(not isinstance(x, str) or not x.strip() for x in required_ops)
    ):
        return ["harness.spec_lang_builtin_sync.required_ops must be a non-empty list of non-empty strings"]
    required = {str(x).strip() for x in required_ops if str(x).strip()}

    contract = root / "docs/spec/contract/03b_spec_lang_v1.md"
    py_impl = root / "spec_runner/spec_lang.py"
    php_impl = root / "scripts/php/spec_runner.php"
    if not contract.exists() or not py_impl.exists() or not php_impl.exists():
        return [
            "assert.spec_lang_builtin_surface_sync requires contract + python/php implementation files"
        ]

    contract_raw = contract.read_text(encoding="utf-8")
    try:
        core_start = contract_raw.index("## Core Forms")
        core_end = contract_raw.index("## Equality + Set Algebra Semantics")
    except ValueError:
        return [
            "docs/spec/contract/03b_spec_lang_v1.md:1: missing Core Forms or Equality + Set Algebra Semantics section"
        ]
    core_raw = contract_raw[core_start:core_end]
    contract_ops = {str(x).strip() for x in re.findall(r"- `([a-z_]+)`", core_raw) if str(x).strip()}
    # Internal/runtime forms are not builtin operator symbols.
    contract_ops -= {"fn", "if", "let", "call", "var"}
    if not contract_ops:
        return ["docs/spec/contract/03b_spec_lang_v1.md:1: no builtin operator tokens found in Core Forms"]
    unknown = sorted(required - contract_ops)
    for op in unknown:
        violations.append(f"docs/spec/contract/03b_spec_lang_v1.md:1: required_ops entry is not documented builtin: {op}")
    contract_ops = set(required)
    if not contract_ops:
        return violations

    py_ops = set(_builtin_arity_table().keys())
    py_missing = sorted(contract_ops - py_ops)
    for op in py_missing:
        violations.append(f"spec_runner/spec_lang.py:1: missing builtin documented in contract: {op}")

    php_raw = php_impl.read_text(encoding="utf-8")
    # PHP builtin handlers are implemented with a mix of direct branches and grouped forms.
    # Use contract-token presence as the sync signal to avoid false negatives from parser shape.
    php_ops = {op for op in contract_ops if f"'{op}'" in php_raw}
    php_missing = sorted(contract_ops - php_ops)
    for op in php_missing:
        violations.append(f"scripts/php/spec_runner.php:1: missing builtin documented in contract: {op}")

    return violations


def _scan_spec_lang_stdlib_profile_complete(root: Path) -> list[str]:
    payload = spec_lang_stdlib_report_jsonable(root)
    violations: list[str] = []
    errors = payload.get("errors") or []
    for err in errors:
        s = str(err).strip()
        if s:
            violations.append(s)
    for item in payload.get("missing_in_python") or []:
        violations.append(f"spec_lang stdlib profile missing in python: {item}")
    for item in payload.get("missing_in_php") or []:
        violations.append(f"spec_lang stdlib profile missing in php: {item}")
    for item in payload.get("arity_mismatch") or []:
        violations.append(f"spec_lang stdlib profile arity mismatch: {item}")
    return violations


def _scan_spec_lang_stdlib_py_php_parity(root: Path) -> list[str]:
    payload = spec_lang_stdlib_report_jsonable(root)
    violations: list[str] = []
    for item in payload.get("missing_in_python") or []:
        violations.append(f"python missing stdlib symbol: {item}")
    for item in payload.get("missing_in_php") or []:
        violations.append(f"php missing stdlib symbol: {item}")
    return violations


def _scan_spec_lang_stdlib_docs_sync(root: Path) -> list[str]:
    payload = spec_lang_stdlib_report_jsonable(root)
    violations: list[str] = []
    for item in payload.get("docs_sync_missing") or []:
        violations.append(str(item))
    return violations


def _scan_spec_lang_stdlib_conformance_coverage(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("stdlib_conformance")
    if not isinstance(cfg, dict):
        return [
            "spec_lang.stdlib_conformance_coverage requires harness.stdlib_conformance mapping in governance spec"
        ]
    required_paths = cfg.get("required_paths")
    if (
        not isinstance(required_paths, list)
        or not required_paths
        or any(not isinstance(x, str) or not x.strip() for x in required_paths)
    ):
        return ["harness.stdlib_conformance.required_paths must be a non-empty list of paths"]
    violations: list[str] = []
    for raw in required_paths:
        rel = str(raw).strip()
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}: missing required conformance file")
    return violations


def _scan_assert_subject_profiles_declared(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    required_paths = (
        _SUBJECT_PROFILE_CONTRACT_DOC,
        _SUBJECT_PROFILE_SCHEMA_DOC,
        *_SUBJECT_PROFILE_TYPE_DOCS,
        "docs/spec/libraries/domain/index.md",
        *_SUBJECT_PROFILE_DOMAIN_LIBS,
    )
    for rel in required_paths:
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing required subject-profile artifact")
    return violations


def _scan_assert_subject_profiles_json_only(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    schema = _join_contract_path(root, _SUBJECT_PROFILE_SCHEMA_DOC)
    evaluator = _join_contract_path(root, "spec_runner/spec_lang.py")
    if not schema.exists():
        return [f"{_SUBJECT_PROFILE_SCHEMA_DOC}:1: missing subject profile schema"]
    if not evaluator.exists():
        return ["spec_runner/spec_lang.py:1: missing evaluator implementation"]
    schema_raw = schema.read_text(encoding="utf-8")
    eval_raw = evaluator.read_text(encoding="utf-8")
    required_schema_tokens = ("json_core_only: true", "non_json_native_values_must_be_projected: true")
    for tok in required_schema_tokens:
        if tok not in schema_raw:
            violations.append(f"{_SUBJECT_PROFILE_SCHEMA_DOC}:1: missing required JSON-core token {tok}")
    required_eval_tokens = (
        "def _is_json_value(",
        "spec_lang subject must be a JSON value",
    )
    for tok in required_eval_tokens:
        if tok not in eval_raw:
            violations.append(f"spec_runner/spec_lang.py:1: missing JSON-core evaluator token {tok}")
    return violations


def _scan_assert_domain_profiles_docs_sync(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    schema = _join_contract_path(root, _SUBJECT_PROFILE_SCHEMA_DOC)
    if not schema.exists():
        return [f"{_SUBJECT_PROFILE_SCHEMA_DOC}:1: missing subject profile schema"]
    schema_raw = schema.read_text(encoding="utf-8")
    required_profile_ids = {
        "python_profile.md": "python.generic/v1",
        "php_profile.md": "php.generic/v1",
        "http_profile.md": "api.http/v1",
        "markdown_profile.md": "markdown.generic/v1",
        "makefile_profile.md": "makefile.generic/v1",
    }
    for rel in _SUBJECT_PROFILE_TYPE_DOCS:
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing profile contract doc")
            continue
        raw = p.read_text(encoding="utf-8")
        profile_id = required_profile_ids.get(Path(rel).name)
        if profile_id and profile_id not in raw:
            violations.append(f"{rel}:1: missing profile id token {profile_id}")
        if profile_id and profile_id not in schema_raw:
            violations.append(f"{_SUBJECT_PROFILE_SCHEMA_DOC}:1: missing profile id {profile_id}")
    return violations


def _scan_assert_domain_library_usage_required(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    cases_dir = root / "docs/spec/conformance/cases/core"
    if not cases_dir.exists():
        return ["docs/spec/conformance/cases/core:1: missing conformance core cases directory"]
    target_file = cases_dir / "domain_libraries.spec.md"
    if not target_file.exists():
        return [f"{target_file.relative_to(root)}:1: missing domain library conformance coverage case"]
    found = False
    for _doc_path, case in load_external_cases(target_file, formats={"md"}):
        if str(case.get("id", "")).strip().startswith("SRCONF-DOMAIN-LIB-"):
            found = True
            harness_map = case.get("harness")
            if not isinstance(harness_map, dict):
                violations.append(
                    f"{target_file.relative_to(root)}: case {case.get('id', '<unknown>')} missing harness mapping"
                )
                continue
            spec_lang_cfg = harness_map.get("spec_lang")
            if not isinstance(spec_lang_cfg, dict):
                violations.append(
                    f"{target_file.relative_to(root)}: case {case.get('id', '<unknown>')} missing harness.spec_lang mapping"
                )
                continue
            lib_paths = spec_lang_cfg.get("library_paths")
            if not isinstance(lib_paths, list) or not any(
                isinstance(x, str) and "/docs/spec/libraries/domain/" in str(x) for x in lib_paths
            ):
                violations.append(
                    f"{target_file.relative_to(root)}: case {case.get('id', '<unknown>')} missing domain library path in harness.spec_lang.library_paths"
                )
    if not found:
        violations.append(f"{target_file.relative_to(root)}:1: expected SRCONF-DOMAIN-LIB-* cases")
    return violations


def _scan_assert_adapter_projection_contract_sync(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    required = {
        "spec_runner/harnesses/text_file.py": ("context_json", "profile_id", "profile_version"),
        "spec_runner/harnesses/cli_run.py": ("context_json", "profile_id", "profile_version"),
        "spec_runner/harnesses/api_http.py": ("context_json", "profile_id", "profile_version"),
    }
    for rel, tokens in required.items():
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing adapter for projection sync check")
            continue
        raw = p.read_text(encoding="utf-8")
        for tok in tokens:
            if tok not in raw:
                violations.append(f"{rel}:1: missing adapter projection token {tok}")
    return violations


def _scan_current_spec_only_contract(root: Path) -> list[str]:
    violations: list[str] = []
    patterns = [re.compile(p, re.IGNORECASE) for p in _CURRENT_SPEC_FORBIDDEN_PATTERNS]
    for rel in (*_CURRENT_SPEC_ONLY_DOCS, *_CURRENT_SPEC_ONLY_CODE_FILES):
        p = _join_contract_path(root, rel)
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


def _iter_mapping_key_paths(value: object, *, path: str = ""):
    if isinstance(value, dict):
        for k, v in value.items():
            key = str(k)
            next_path = f"{path}.{key}" if path else key
            yield next_path, key
            yield from _iter_mapping_key_paths(v, path=next_path)
    elif isinstance(value, list):
        for idx, item in enumerate(value):
            next_path = f"{path}[{idx}]" if path else f"[{idx}]"
            yield from _iter_mapping_key_paths(item, path=next_path)


def _scan_current_spec_policy_key_names(root: Path) -> list[str]:
    violations: list[str] = []
    specs_root = root / "docs/spec"
    if not specs_root.exists():
        return violations
    for p in sorted(specs_root.rglob("*.spec.md")):
        try:
            tests = list(iter_spec_doc_tests(p.parent, file_pattern=p.name))
        except Exception as exc:  # noqa: BLE001
            rel = p.relative_to(root)
            violations.append(f"{rel}:1: unable to parse spec-test blocks: {exc}")
            continue
        for spec in tests:
            case_id = str(spec.test.get("id", "<unknown>")).strip() or "<unknown>"
            for key_path, key in _iter_mapping_key_paths(spec.test):
                if key.endswith("_expr"):
                    rel = p.relative_to(root)
                    violations.append(
                        f"{rel}: case {case_id} uses unsupported policy-expression key at {key_path}; "
                        "use 'policy_evaluate'"
                    )
    return violations


def _scan_governance_policy_evaluate_required(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("policy_requirements")
    if not isinstance(cfg, dict):
        return ["governance.policy_evaluate_required requires harness.policy_requirements mapping in governance spec"]
    cases_rel = str(cfg.get("cases_path", "docs/spec/governance/cases")).strip() or "docs/spec/governance/cases"
    case_pattern = str(cfg.get("case_file_pattern", SETTINGS.case.default_file_pattern)).strip() or SETTINGS.case.default_file_pattern
    ignore_checks_raw = cfg.get("ignore_checks", [])
    if not isinstance(ignore_checks_raw, list) or any(not isinstance(x, str) for x in ignore_checks_raw):
        return ["harness.policy_requirements.ignore_checks must be a list of strings"]
    ignore_checks = {x.strip() for x in ignore_checks_raw if x.strip()}

    cases_dir = _join_contract_path(root, cases_rel)
    if not cases_dir.exists():
        return [f"{cases_rel}:1: governance cases path does not exist"]

    violations: list[str] = []
    for spec in iter_cases(cases_dir, file_pattern=case_pattern):
        case = spec.test if isinstance(spec.test, dict) else {}
        if str(case.get("type", "")).strip() != "governance.check":
            continue
        case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
        check_id = str(case.get("check", "")).strip()
        if check_id in ignore_checks:
            continue
        harness_map = case.get("harness")
        if not isinstance(harness_map, dict):
            violations.append(f"{spec.doc_path.relative_to(root)}: case {case_id} missing harness mapping")
            continue
        if "policy_evaluate" not in harness_map:
            violations.append(
                f"{spec.doc_path.relative_to(root)}: case {case_id} check {check_id} missing required policy_evaluate"
            )
    return violations


def _scan_governance_policy_library_usage_required(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("policy_library_requirements")
    if not isinstance(cfg, dict):
        return [
            "governance.policy_library_usage_required requires harness.policy_library_requirements mapping in governance spec"
        ]
    cases_rel = str(cfg.get("cases_path", "docs/spec/governance/cases")).strip() or "docs/spec/governance/cases"
    case_pattern = str(cfg.get("case_file_pattern", SETTINGS.case.default_file_pattern)).strip() or SETTINGS.case.default_file_pattern
    ignore_checks_raw = cfg.get("ignore_checks", [])
    if not isinstance(ignore_checks_raw, list) or any(not isinstance(x, str) for x in ignore_checks_raw):
        return ["harness.policy_library_requirements.ignore_checks must be a list of strings"]
    ignore_checks = {x.strip() for x in ignore_checks_raw if x.strip()}

    cases_dir = _join_contract_path(root, cases_rel)
    if not cases_dir.exists():
        return [f"{cases_rel}:1: governance cases path does not exist"]

    def _policy_uses_library_call(expr: object) -> bool:
        if isinstance(expr, dict):
            if "call" in expr:
                raw = expr.get("call")
                if isinstance(raw, list) and raw:
                    fn_node = raw[0]
                    if (
                        isinstance(fn_node, dict)
                        and len(fn_node) == 1
                        and "var" in fn_node
                        and isinstance(fn_node.get("var"), str)
                        and str(fn_node.get("var", "")).strip()
                    ):
                        return True
            return any(_policy_uses_library_call(v) for v in expr.values())
        if isinstance(expr, list):
            return any(_policy_uses_library_call(v) for v in expr)
        return False

    violations: list[str] = []
    for spec in iter_cases(cases_dir, file_pattern=case_pattern):
        case = spec.test if isinstance(spec.test, dict) else {}
        if str(case.get("type", "")).strip() != "governance.check":
            continue
        case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
        check_id = str(case.get("check", "")).strip()
        if check_id in ignore_checks:
            continue
        harness_map = case.get("harness")
        if not isinstance(harness_map, dict):
            violations.append(f"{spec.doc_path.relative_to(root)}: case {case_id} missing harness mapping")
            continue
        spec_lang_cfg = harness_map.get("spec_lang")
        has_library_paths = False
        if isinstance(spec_lang_cfg, dict):
            lib_paths = spec_lang_cfg.get("library_paths")
            has_library_paths = isinstance(lib_paths, list) and any(
                isinstance(x, str) and x.strip() for x in lib_paths
            )
        if not has_library_paths:
            violations.append(
                f"{spec.doc_path.relative_to(root)}: case {case_id} check {check_id} must declare non-empty harness.spec_lang.library_paths"
            )
            continue
        policy = harness_map.get("policy_evaluate")
        if not isinstance(policy, list) or not policy:
            violations.append(
                f"{spec.doc_path.relative_to(root)}: case {case_id} check {check_id} must declare non-empty harness.policy_evaluate"
            )
            continue
        if not _policy_uses_library_call(policy):
            violations.append(
                f"{spec.doc_path.relative_to(root)}: case {case_id} check {check_id} policy_evaluate must call library symbol via call -> var"
            )
    return violations


def _scan_conformance_library_policy_usage_required(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("conformance_policy_library_requirements")
    if not isinstance(cfg, dict):
        return [
            "conformance.library_policy_usage_required requires harness.conformance_policy_library_requirements mapping in governance spec"
        ]
    cases_rel = str(cfg.get("cases_path", "docs/spec/governance/cases")).strip() or "docs/spec/governance/cases"
    case_pattern = str(cfg.get("case_file_pattern", SETTINGS.case.default_file_pattern)).strip() or SETTINGS.case.default_file_pattern
    ignore_checks_raw = cfg.get("ignore_checks", [])
    if not isinstance(ignore_checks_raw, list) or any(not isinstance(x, str) for x in ignore_checks_raw):
        return ["harness.conformance_policy_library_requirements.ignore_checks must be a list of strings"]
    ignore_checks = {x.strip() for x in ignore_checks_raw if x.strip()}

    cases_dir = _join_contract_path(root, cases_rel)
    if not cases_dir.exists():
        return [f"{cases_rel}:1: governance cases path does not exist"]

    def _policy_uses_library_call(expr: object) -> bool:
        if isinstance(expr, dict):
            if "call" in expr:
                raw = expr.get("call")
                if isinstance(raw, list) and raw:
                    fn_node = raw[0]
                    if (
                        isinstance(fn_node, dict)
                        and len(fn_node) == 1
                        and "var" in fn_node
                        and isinstance(fn_node.get("var"), str)
                        and str(fn_node.get("var", "")).strip()
                    ):
                        return True
            return any(_policy_uses_library_call(v) for v in expr.values())
        if isinstance(expr, list):
            return any(_policy_uses_library_call(v) for v in expr)
        return False

    violations: list[str] = []
    for spec in iter_cases(cases_dir, file_pattern=case_pattern):
        case = spec.test if isinstance(spec.test, dict) else {}
        if str(case.get("type", "")).strip() != "governance.check":
            continue
        case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
        check_id = str(case.get("check", "")).strip()
        if not check_id.startswith("conformance.") or check_id in ignore_checks:
            continue
        harness_map = case.get("harness")
        if not isinstance(harness_map, dict):
            violations.append(f"{spec.doc_path.relative_to(root)}: case {case_id} missing harness mapping")
            continue
        spec_lang_cfg = harness_map.get("spec_lang")
        has_library_paths = False
        if isinstance(spec_lang_cfg, dict):
            lib_paths = spec_lang_cfg.get("library_paths")
            has_library_paths = isinstance(lib_paths, list) and any(
                isinstance(x, str) and x.strip() for x in lib_paths
            )
        if not has_library_paths:
            violations.append(
                f"{spec.doc_path.relative_to(root)}: case {case_id} check {check_id} must declare non-empty harness.spec_lang.library_paths"
            )
            continue
        policy = harness_map.get("policy_evaluate")
        if not isinstance(policy, list) or not policy:
            violations.append(
                f"{spec.doc_path.relative_to(root)}: case {case_id} check {check_id} must declare non-empty harness.policy_evaluate"
            )
            continue
        if not _policy_uses_library_call(policy):
            violations.append(
                f"{spec.doc_path.relative_to(root)}: case {case_id} check {check_id} policy_evaluate must call library symbol via call -> var"
            )
    return violations


def _scan_governance_extractor_only_no_verdict_branching(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("extractor_policy")
    if not isinstance(cfg, dict):
        return ["governance.extractor_only_no_verdict_branching requires harness.extractor_policy mapping in governance spec"]
    rel = str(cfg.get("path", "scripts/run_governance_specs.py")).strip() or "scripts/run_governance_specs.py"
    p = _join_contract_path(root, rel)
    if not p.exists():
        return [f"{rel}:1: missing governance runner script"]
    forbidden_tokens = cfg.get("forbidden_tokens", [])
    if (
        not isinstance(forbidden_tokens, list)
        or not forbidden_tokens
        or any(not isinstance(x, str) or not x.strip() for x in forbidden_tokens)
    ):
        return ["harness.extractor_policy.forbidden_tokens must be a non-empty list of non-empty strings"]
    raw = p.read_text(encoding="utf-8")
    violations: list[str] = []
    for tok in forbidden_tokens:
        if tok in raw:
            violations.append(f"{rel}:1: forbidden check-level verdict token present: {tok}")
    return violations


def _scan_governance_structured_assertions_required(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("structured_assertions")
    if not isinstance(cfg, dict):
        return ["governance.structured_assertions_required requires harness.structured_assertions mapping in governance spec"]
    cases_rel = str(cfg.get("cases_path", "docs/spec/governance/cases")).strip() or "docs/spec/governance/cases"
    case_pattern = str(cfg.get("case_file_pattern", SETTINGS.case.default_file_pattern)).strip() or SETTINGS.case.default_file_pattern
    ignore_checks_raw = cfg.get("ignore_checks", [])
    if not isinstance(ignore_checks_raw, list) or any(not isinstance(x, str) for x in ignore_checks_raw):
        return ["harness.structured_assertions.ignore_checks must be a list of strings"]
    ignore_checks = {x.strip() for x in ignore_checks_raw if x.strip()}

    cases_dir = _join_contract_path(root, cases_rel)
    if not cases_dir.exists():
        return [f"{cases_rel}:1: governance cases path does not exist"]

    violations: list[str] = []
    for spec in iter_cases(cases_dir, file_pattern=case_pattern):
        case = spec.test if isinstance(spec.test, dict) else {}
        if str(case.get("type", "")).strip() != "governance.check":
            continue
        case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
        check_id = str(case.get("check", "")).strip()
        if check_id in ignore_checks:
            continue
        assert_tree = case.get("assert", []) or []
        has_structured_target = False
        text_pass_only = True

        leaf_rows: list[tuple[str, str, object, bool]] = []

        def _collect_leaf(leaf: dict, *, inherited_target: str | None = None, assert_path: str = "assert") -> None:
            del assert_path  # scanner only needs leaf tuples
            for row in iter_leaf_assertions(leaf, target_override=inherited_target):
                leaf_rows.append(row)

        try:
            eval_assert_tree(assert_tree, eval_leaf=_collect_leaf)
        except Exception as exc:  # noqa: BLE001
            violations.append(
                f"{spec.doc_path.relative_to(root)}: case {case_id} check {check_id} has invalid assert tree ({exc})"
            )
            continue
        for target, op, value, _ in leaf_rows:
            if target in {"summary_json", "violation_count"} and op == "evaluate":
                has_structured_target = True
            if not (target == "text" and op == "contain" and str(value).strip().startswith("PASS: ")):
                text_pass_only = False
        if not has_structured_target:
            violations.append(
                f"{spec.doc_path.relative_to(root)}: case {case_id} check {check_id} missing structured evaluate assertions"
            )
        elif text_pass_only:
            violations.append(
                f"{spec.doc_path.relative_to(root)}: case {case_id} check {check_id} relies solely on PASS text assertions"
            )
    return violations


def _scan_runtime_rust_adapter_no_python_exec(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("rust_no_python_exec")
    if not isinstance(cfg, dict):
        return ["runtime.rust_adapter_no_python_exec requires harness.rust_no_python_exec mapping in governance spec"]
    rel = str(cfg.get("path", "scripts/rust/spec_runner_cli/src/main.rs")).strip() or "scripts/rust/spec_runner_cli/src/main.rs"
    p = _join_contract_path(root, rel)
    if not p.exists():
        return [f"{rel}:1: missing rust runner interface implementation"]
    forbidden_tokens = cfg.get("forbidden_tokens", [])
    if (
        not isinstance(forbidden_tokens, list)
        or not forbidden_tokens
        or any(not isinstance(x, str) or not x.strip() for x in forbidden_tokens)
    ):
        return ["harness.rust_no_python_exec.forbidden_tokens must be a non-empty list of non-empty strings"]
    raw = p.read_text(encoding="utf-8")
    violations: list[str] = []
    for tok in forbidden_tokens:
        if tok in raw:
            violations.append(f"{rel}:1: forbidden python-coupling token present: {tok}")
    return violations


def _scan_runtime_non_python_lane_no_python_exec(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("python_dependency")
    if not isinstance(cfg, dict):
        return [
            "runtime.non_python_lane_no_python_exec requires harness.python_dependency mapping in governance spec"
        ]
    payload = python_dependency_report_jsonable(root, config=cfg)
    errors = payload.get("errors") or []
    if isinstance(errors, list) and any(str(e).strip() for e in errors):
        return [str(e) for e in errors if str(e).strip()]
    summary = payload.get("summary") if isinstance(payload, dict) else {}
    if not isinstance(summary, dict):
        return ["python dependency payload missing summary mapping"]
    count = int(summary.get("non_python_lane_python_exec_count", 0))
    violations: list[str] = []
    if count > 0:
        violations.append(
            f".artifacts/python-dependency.json:1: non_python_lane_python_exec_count={count} (expected 0)"
        )
    return violations


def _scan_runtime_rust_adapter_transitive_no_python(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("rust_transitive_no_python")
    if not isinstance(cfg, dict):
        return [
            "runtime.rust_adapter_transitive_no_python requires harness.rust_transitive_no_python mapping in governance spec"
        ]
    files = cfg.get("files")
    forbidden_tokens = cfg.get("forbidden_tokens", [])
    if (
        not isinstance(files, list)
        or not files
        or any(not isinstance(x, str) or not x.strip() for x in files)
    ):
        return ["harness.rust_transitive_no_python.files must be a non-empty list of non-empty strings"]
    if (
        not isinstance(forbidden_tokens, list)
        or not forbidden_tokens
        or any(not isinstance(x, str) or not x.strip() for x in forbidden_tokens)
    ):
        return [
            "harness.rust_transitive_no_python.forbidden_tokens must be a non-empty list of non-empty strings"
        ]
    violations: list[str] = []
    for rel in files:
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing rust adapter file for transitive no-python check")
            continue
        raw = p.read_text(encoding="utf-8")
        for tok in forbidden_tokens:
            if tok in raw:
                violations.append(f"{rel}:1: forbidden rust transitive python token present: {tok}")
    return violations


def _scan_runtime_public_runner_entrypoint_single(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("public_runner_entrypoint")
    if not isinstance(cfg, dict):
        return [
            "runtime.public_runner_entrypoint_single requires harness.public_runner_entrypoint mapping in governance spec"
        ]
    required_entrypoint = str(cfg.get("required_entrypoint", "")).strip()
    gate_files = cfg.get("gate_files")
    forbidden_tokens = cfg.get("forbidden_tokens", [])
    if not required_entrypoint:
        return ["harness.public_runner_entrypoint.required_entrypoint must be a non-empty string"]
    if (
        not isinstance(gate_files, list)
        or not gate_files
        or any(not isinstance(x, str) or not x.strip() for x in gate_files)
    ):
        return ["harness.public_runner_entrypoint.gate_files must be a non-empty list of non-empty strings"]
    if not isinstance(forbidden_tokens, list) or any(not isinstance(x, str) or not x.strip() for x in forbidden_tokens):
        return ["harness.public_runner_entrypoint.forbidden_tokens must be a list of non-empty strings"]

    violations: list[str] = []
    for rel in gate_files:
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing gate file")
            continue
        text = p.read_text(encoding="utf-8")
        if required_entrypoint not in text:
            violations.append(f"{rel}:1: missing required public runner entrypoint token {required_entrypoint}")
        for tok in forbidden_tokens:
            if tok in text:
                violations.append(f"{rel}:1: forbidden direct runner token {tok}")
    return violations


def _scan_runtime_public_runner_default_rust(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("public_runner_default")
    if not isinstance(cfg, dict):
        return ["runtime.public_runner_default_rust requires harness.public_runner_default mapping in governance spec"]
    path = str(cfg.get("path", "")).strip()
    required_tokens = cfg.get("required_tokens", [])
    forbidden_tokens = cfg.get("forbidden_tokens", [])
    if not path:
        return ["harness.public_runner_default.path must be a non-empty string"]
    if (
        not isinstance(required_tokens, list)
        or not required_tokens
        or any(not isinstance(x, str) or not x.strip() for x in required_tokens)
    ):
        return ["harness.public_runner_default.required_tokens must be a non-empty list of non-empty strings"]
    if not isinstance(forbidden_tokens, list) or any(not isinstance(x, str) or not x.strip() for x in forbidden_tokens):
        return ["harness.public_runner_default.forbidden_tokens must be a list of non-empty strings"]
    p = _join_contract_path(root, path)
    if not p.exists():
        return [f"{path}:1: missing public runner adapter script"]
    text = p.read_text(encoding="utf-8")
    violations: list[str] = []
    for tok in required_tokens:
        if tok not in text:
            violations.append(f"{path}:1: missing required rust-default token {tok}")
    for tok in forbidden_tokens:
        if tok in text:
            violations.append(f"{path}:1: forbidden default token {tok}")
    return violations


def _scan_runtime_python_lane_explicit_opt_in(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("python_lane_opt_in")
    if not isinstance(cfg, dict):
        return ["runtime.python_lane_explicit_opt_in requires harness.python_lane_opt_in mapping in governance spec"]
    files = cfg.get("files")
    required_opt_in_tokens = cfg.get("required_opt_in_tokens", [])
    forbidden_default_tokens = cfg.get("forbidden_default_tokens", [])
    if (
        not isinstance(files, list)
        or not files
        or any(not isinstance(x, str) or not x.strip() for x in files)
    ):
        return ["harness.python_lane_opt_in.files must be a non-empty list of non-empty strings"]
    if (
        not isinstance(required_opt_in_tokens, list)
        or not required_opt_in_tokens
        or any(not isinstance(x, str) or not x.strip() for x in required_opt_in_tokens)
    ):
        return ["harness.python_lane_opt_in.required_opt_in_tokens must be a non-empty list of non-empty strings"]
    if not isinstance(forbidden_default_tokens, list) or any(
        not isinstance(x, str) or not x.strip() for x in forbidden_default_tokens
    ):
        return ["harness.python_lane_opt_in.forbidden_default_tokens must be a list of non-empty strings"]
    violations: list[str] = []
    for rel in files:
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing file for python lane opt-in policy check")
            continue
        text = p.read_text(encoding="utf-8")
        for tok in forbidden_default_tokens:
            if tok in text:
                violations.append(f"{rel}:1: forbidden implicit python-lane token {tok}")
        if not any(tok in text for tok in required_opt_in_tokens):
            violations.append(f"{rel}:1: missing explicit python opt-in token")
    return violations


def _scan_runtime_no_public_direct_rust_adapter_docs(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("public_docs")
    if not isinstance(cfg, dict):
        return ["runtime.no_public_direct_rust_adapter_docs requires harness.public_docs mapping in governance spec"]
    files = cfg.get("files")
    forbidden_tokens = cfg.get("forbidden_tokens", [])
    allowlist = cfg.get("allowlist", [])
    if (
        not isinstance(files, list)
        or not files
        or any(not isinstance(x, str) or not x.strip() for x in files)
    ):
        return ["harness.public_docs.files must be a non-empty list of non-empty strings"]
    if (
        not isinstance(forbidden_tokens, list)
        or not forbidden_tokens
        or any(not isinstance(x, str) or not x.strip() for x in forbidden_tokens)
    ):
        return ["harness.public_docs.forbidden_tokens must be a non-empty list of non-empty strings"]
    if not isinstance(allowlist, list) or any(not isinstance(x, str) or not x.strip() for x in allowlist):
        return ["harness.public_docs.allowlist must be a list of non-empty strings"]
    allow = {str(x).lstrip("/") for x in allowlist}
    violations: list[str] = []
    for rel in files:
        normalized = str(rel).lstrip("/")
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing public doc for rust-adapter invocation check")
            continue
        if normalized in allow:
            continue
        text = p.read_text(encoding="utf-8")
        for tok in forbidden_tokens:
            if tok in text:
                violations.append(f"{rel}:1: forbidden direct rust-adapter public doc token {tok}")
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
        p = _join_contract_path(root, rel)
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


def _any_pattern_matches(text: str, patterns: list[re.Pattern[str]]) -> bool:
    for pat in patterns:
        if pat.search(text):
            return True
    return False


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
    try:
        policy_evaluate = normalize_policy_evaluate(
            determinism.get("policy_evaluate"), field="harness.determinism.policy_evaluate"
        )
    except ValueError as exc:
        return [str(exc)]
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

    rows: list[dict[str, object]] = []
    for spec in iter_cases(cases_dir, file_pattern=SETTINGS.case.default_file_pattern):
        case = spec.test
        case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
        scoped = {
            k: v
            for k, v in case.items()
            if str(k) not in exclude_case_keys
        }
        rows.append(
            {
                "id": case_id,
                "strings": list(_iter_string_values(scoped)),
            }
        )

    pattern_values = [p.pattern for p in compiled_patterns]
    for row in rows:
        case_id = str(row.get("id", "<unknown>")).strip() or "<unknown>"
        strings = row.get("strings")
        if not isinstance(strings, list):
            continue
        if any(_any_pattern_matches(str(s), compiled_patterns) for s in strings):
            violations.append(
                f"{case_id}: non-deterministic token matched configured pattern in case content"
            )
    return _policy_outcome(
        subject=rows,
        policy_evaluate=policy_evaluate,
        policy_path="harness.determinism.policy_evaluate",
        symbols={"patterns": pattern_values},
        violations=violations,
    )


def _scan_conformance_no_ambient_assumptions(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    ambient = h.get("ambient_assumptions")
    if not isinstance(ambient, dict):
        return ["conformance.no_ambient_assumptions requires harness.ambient_assumptions mapping in governance spec"]
    try:
        policy_evaluate = normalize_policy_evaluate(
            ambient.get("policy_evaluate"), field="harness.ambient_assumptions.policy_evaluate"
        )
    except ValueError as exc:
        return [str(exc)]
    raw_patterns = ambient.get("patterns")
    if not isinstance(raw_patterns, list) or not raw_patterns:
        return ["conformance.no_ambient_assumptions requires non-empty harness.ambient_assumptions.patterns list"]
    compiled_patterns: list[re.Pattern[str]] = []
    for raw in raw_patterns:
        if not isinstance(raw, str) or not raw.strip():
            violations.append("harness.ambient_assumptions.patterns entries must be non-empty strings")
            continue
        try:
            compiled_patterns.append(re.compile(raw, re.IGNORECASE))
        except re.error as e:
            violations.append(f"invalid regex in harness.ambient_assumptions.patterns: {raw!r} ({e})")
    raw_exclude = ambient.get("exclude_case_keys", ["id", "title", "purpose", "expect", "requires", "assert_health"])
    if not isinstance(raw_exclude, list) or any(not isinstance(x, str) for x in raw_exclude):
        violations.append("harness.ambient_assumptions.exclude_case_keys must be a list of strings")
        return violations
    exclude_case_keys = {x for x in raw_exclude if x}
    if not compiled_patterns:
        return violations
    cases_dir = root / "docs/spec/conformance/cases"
    if not cases_dir.exists():
        return violations

    rows: list[dict[str, object]] = []
    for spec in iter_cases(cases_dir, file_pattern=SETTINGS.case.default_file_pattern):
        case = spec.test
        case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
        scoped = {k: v for k, v in case.items() if str(k) not in exclude_case_keys}
        rows.append(
            {
                "id": case_id,
                "strings": list(_iter_string_values(scoped)),
            }
        )

    pattern_values = [p.pattern for p in compiled_patterns]
    for row in rows:
        case_id = str(row.get("id", "<unknown>")).strip() or "<unknown>"
        strings = row.get("strings")
        if not isinstance(strings, list):
            continue
        if any(_any_pattern_matches(str(s), compiled_patterns) for s in strings):
            violations.append(
                f"{case_id}: ambient-assumption token matched configured pattern in case content"
            )
    return _policy_outcome(
        subject={"rows": rows, "violations": violations},
        policy_evaluate=policy_evaluate,
        policy_path="harness.ambient_assumptions.policy_evaluate",
        symbols={"patterns": pattern_values},
        violations=violations,
    )


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
    p = _join_contract_path(root, rel)
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


def _scan_conformance_spec_lang_preferred(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    cfg = h.get("spec_lang_preferred")
    if not isinstance(cfg, dict):
        return ["conformance.spec_lang_preferred requires harness.spec_lang_preferred mapping in governance spec"]
    roots = cfg.get("roots")
    if (
        not isinstance(roots, list)
        or not roots
        or any(not isinstance(x, str) or not x.strip() for x in roots)
    ):
        return ["harness.spec_lang_preferred.roots must be a non-empty list of non-empty strings"]
    if "allow_sugar_files" in cfg:
        return ["harness.spec_lang_preferred.allow_sugar_files is not supported; assertions are evaluate-only in this surface"]
    try:
        policy_evaluate = normalize_policy_evaluate(
            cfg.get("policy_evaluate"), field="harness.spec_lang_preferred.policy_evaluate"
        )
    except ValueError as exc:
        return [str(exc)]

    all_rows: list[dict[str, object]] = []
    for rel_root in roots:
        base = _join_contract_path(root, rel_root)
        if not base.exists():
            violations.append(f"{rel_root}:1: missing conformance root for spec-lang preference scan")
            continue
        for spec in iter_cases(base, file_pattern=SETTINGS.case.default_file_pattern):
            try:
                rel = str(spec.doc_path.resolve().relative_to(root))
            except ValueError:
                rel = str(spec.doc_path)
            non_evaluate_ops: set[str] = set()

            def _collect_ops(node: object, *, inherited_target: str | None = None) -> None:
                if node is None:
                    return
                if isinstance(node, list):
                    for child in node:
                        _collect_ops(child, inherited_target=inherited_target)
                    return
                if not isinstance(node, dict):
                    return
                present_groups = [k for k in ("must", "can", "cannot") if k in node]
                if present_groups:
                    node_target = str(node.get("target", "")).strip() or inherited_target
                    for key in present_groups:
                        children = node.get(key, [])
                        if isinstance(children, list):
                            for child in children:
                                _collect_ops(child, inherited_target=node_target)
                    return
                for _target, op, _value, _is_true in iter_leaf_assertions(
                    node, target_override=inherited_target
                ):
                    if op != "evaluate":
                        non_evaluate_ops.add(op)

            _collect_ops(spec.test.get("assert", []) or [])
            case_id = str(spec.test.get("id", "<unknown>")).strip() or "<unknown>"
            all_rows.append(
                {
                    "id": case_id,
                    "file": rel,
                    "non_evaluate_ops": sorted(non_evaluate_ops),
                }
            )

    for row in all_rows:
        ops = row.get("non_evaluate_ops")
        if not isinstance(ops, list) or not ops:
            continue
        case_id = str(row.get("id", "<unknown>")).strip() or "<unknown>"
        rel = str(row.get("file", "<unknown>"))
        found = ", ".join(str(x) for x in ops)
        violations.append(
            f"{rel}: case {case_id} uses unsupported sugar ops ({found}); "
            "use evaluate-only assertions for conformance/governance surfaces"
        )
    return _policy_outcome(
        subject=all_rows,
        policy_evaluate=policy_evaluate,
        policy_path="harness.spec_lang_preferred.policy_evaluate",
        violations=violations,
    )


def _scan_conformance_spec_lang_fixture_library_usage(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("spec_lang_fixture_library_usage")
    if not isinstance(cfg, dict):
        return ["conformance.spec_lang_fixture_library_usage requires harness.spec_lang_fixture_library_usage mapping in governance spec"]
    rel = str(cfg.get("path", "docs/spec/conformance/cases/core/spec_lang.spec.md")).strip() or "docs/spec/conformance/cases/core/spec_lang.spec.md"
    required_library_path = str(cfg.get("required_library_path", "")).strip()
    if not required_library_path:
        return ["harness.spec_lang_fixture_library_usage.required_library_path must be a non-empty string"]
    required_call_prefix = str(cfg.get("required_call_prefix", "conf.")).strip() or "conf."
    min_call_count = cfg.get("min_call_count", 1)
    if not isinstance(min_call_count, int) or min_call_count < 1:
        return ["harness.spec_lang_fixture_library_usage.min_call_count must be a positive int"]
    required_case_ids_raw = cfg.get("required_case_ids", [])
    if not isinstance(required_case_ids_raw, list) or any(not isinstance(x, str) or not x.strip() for x in required_case_ids_raw):
        return ["harness.spec_lang_fixture_library_usage.required_case_ids must be a list of non-empty strings"]
    required_case_ids = {str(x).strip() for x in required_case_ids_raw if str(x).strip()}

    fixture = _join_contract_path(root, rel)
    if not fixture.exists():
        return [f"{rel}:1: missing conformance fixture file"]

    def _count_helper_calls(node: object) -> int:
        if isinstance(node, list):
            return sum(_count_helper_calls(x) for x in node)
        if not isinstance(node, dict):
            return 0
        count = 0
        call_node = node.get("call")
        if isinstance(call_node, list) and call_node:
            fn_node = call_node[0]
            if (
                isinstance(fn_node, dict)
                and len(fn_node) == 1
                and "var" in fn_node
                and isinstance(fn_node.get("var"), str)
                and str(fn_node.get("var", "")).startswith(required_call_prefix)
            ):
                count += 1
        for v in node.values():
            count += _count_helper_calls(v)
        return count

    total_calls = 0
    seen_required: set[str] = set()
    violations: list[str] = []
    for spec in iter_spec_doc_tests(fixture.parent, file_pattern=fixture.name):
        case = spec.test if isinstance(spec.test, dict) else {}
        case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
        if str(case.get("type", "")).strip() != "text.file":
            continue
        harness_map = case.get("harness")
        lib_ok = False
        if isinstance(harness_map, dict):
            spec_lang_cfg = harness_map.get("spec_lang")
            if isinstance(spec_lang_cfg, dict):
                lib_paths = spec_lang_cfg.get("library_paths")
                lib_ok = isinstance(lib_paths, list) and any(
                    isinstance(x, str) and str(x).strip() == required_library_path for x in lib_paths
                )
        calls = _count_helper_calls(case.get("assert"))
        total_calls += calls
        if case_id in required_case_ids:
            seen_required.add(case_id)
            if not lib_ok:
                violations.append(f"{rel}: case {case_id} missing harness.spec_lang.library_paths entry {required_library_path}")
            if calls < 1:
                violations.append(f"{rel}: case {case_id} missing helper call with prefix {required_call_prefix!r}")

    missing_ids = sorted(required_case_ids - seen_required)
    for case_id in missing_ids:
        violations.append(f"{rel}: required_case_ids entry not found: {case_id}")
    if total_calls < min_call_count:
        violations.append(
            f"{rel}: helper call count {total_calls} is below min_call_count {min_call_count} for prefix {required_call_prefix!r}"
        )
    return violations


def _scan_conformance_library_contract_cases_present(
    root: Path, *, harness: dict | None = None
) -> list[str]:
    h = harness or {}
    cfg = h.get("conformance_library_contract_cases_present")
    if not isinstance(cfg, dict):
        return [
            "conformance.library_contract_cases_present requires harness.conformance_library_contract_cases_present mapping in governance spec"
        ]
    rel = str(cfg.get("path", "")).strip()
    if not rel:
        return [
            "harness.conformance_library_contract_cases_present.path must be a non-empty string"
        ]
    required_case_ids_raw = cfg.get("required_case_ids")
    if (
        not isinstance(required_case_ids_raw, list)
        or not required_case_ids_raw
        or any(not isinstance(x, str) or not x.strip() for x in required_case_ids_raw)
    ):
        return [
            "harness.conformance_library_contract_cases_present.required_case_ids must be a non-empty list of non-empty strings"
        ]
    required_case_ids = {str(x).strip() for x in required_case_ids_raw}

    fixture = _join_contract_path(root, rel)
    if not fixture.exists():
        return [f"{rel}:1: missing conformance fixture file"]

    found_case_ids: set[str] = set()
    evaluate_case_ids: set[str] = set()
    for spec in iter_spec_doc_tests(fixture.parent, file_pattern=fixture.name):
        case = spec.test if isinstance(spec.test, dict) else {}
        case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
        found_case_ids.add(case_id)
        raw_assert = case.get("assert")
        if isinstance(raw_assert, list) and any(True for _ in _iter_evaluate_expr_nodes(raw_assert)):
            evaluate_case_ids.add(case_id)

    violations: list[str] = []
    for case_id in sorted(required_case_ids):
        if case_id not in found_case_ids:
            violations.append(f"{rel}: missing required conformance case id {case_id}")
            continue
        if case_id not in evaluate_case_ids:
            violations.append(f"{rel}: required case {case_id} must include evaluate assertions")
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
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing required reference file")

    for pattern in required_globs:
        matches = sorted(root.glob(pattern))
        if not matches:
            violations.append(f"{pattern}:1: glob matched no files")
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

    index_path = _join_contract_path(root, index_rel)
    if not index_path.exists():
        return [f"{index_rel}:1: missing reference index file"]

    include_norm = include_glob.lstrip("/")
    expected = []
    for p in sorted(root.glob(include_norm)):
        relp = str(p.relative_to(root)).replace("\\", "/")
        if relp in exclude or ("/" + relp) in exclude:
            continue
        expected.append(relp)
    raw = index_path.read_text(encoding="utf-8")
    listed = [
        p.lstrip("/")
        for p in _extract_backtick_paths(raw)
        if p.lstrip("/").startswith("docs/book/") and p.lstrip("/").endswith(".md")
    ]
    seen: set[str] = set()
    deduped_listed: list[str] = []
    for rel in listed:
        if rel in seen:
            violations.append(f"{index_rel}:1: duplicate entry {rel}")
            continue
        seen.add(rel)
        deduped_listed.append(rel)

    for rel in expected:
        if rel not in seen:
            violations.append(f"{index_rel}:1: missing entry {rel}")
    for rel in deduped_listed:
        if rel not in expected:
            violations.append(f"{index_rel}:1: stale entry {rel}")
    if deduped_listed and expected and deduped_listed != expected:
        violations.append(
            f"{index_rel}:1: entries are out of sync or out of order with {include_glob}"
        )
    return violations


def _load_docs_quality_context(root: Path, harness: dict | None = None) -> tuple[dict, list[str], dict[str, dict], list[str]]:
    h = harness or {}
    cfg = h.get("docs_quality")
    if not isinstance(cfg, dict):
        return {}, [], {}, ["docs_quality config required in harness.docs_quality"]
    manifest_rel = str(cfg.get("manifest", "")).strip()
    if not manifest_rel:
        return {}, [], {}, ["harness.docs_quality.manifest must be a non-empty string"]
    manifest, manifest_issues = load_reference_manifest(root, manifest_rel)
    if manifest_issues:
        return {}, [], {}, [x.render() for x in manifest_issues]
    docs = manifest_chapter_paths(manifest)
    metas, meta_issues, _meta_lines = load_docs_meta_for_paths(root, docs)
    meta_msgs = [x.render() for x in meta_issues]
    for rel in docs:
        if rel in metas:
            metas[rel]["__text__"] = (_join_contract_path(root, rel)).read_text(encoding="utf-8")
    return manifest, docs, metas, meta_msgs


def _scan_docs_meta_schema_valid(root: Path, *, harness: dict | None = None) -> list[str]:
    _manifest, _docs, _metas, meta_msgs = _load_docs_quality_context(root, harness)
    if meta_msgs:
        return meta_msgs
    return []


def _scan_docs_reference_manifest_sync(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("docs_quality")
    if not isinstance(cfg, dict):
        return ["docs.reference_manifest_sync requires harness.docs_quality mapping in governance spec"]
    manifest, _docs, _metas, msgs = _load_docs_quality_context(root, harness)
    if msgs:
        return msgs
    index_rel = str(cfg.get("index_out", "docs/book/reference_index.md")).strip()
    index_path = _join_contract_path(root, index_rel)
    expected = render_reference_index(manifest)
    if not index_path.exists():
        return [f"{index_rel}:1: missing generated reference index"]
    if index_path.read_text(encoding="utf-8") != expected:
        return [f"{index_rel}:1: out of sync with docs_quality manifest"]
    return []


def _scan_docs_token_ownership_unique(root: Path, *, harness: dict | None = None) -> list[str]:
    _manifest, _docs, metas, msgs = _load_docs_quality_context(root, harness)
    if msgs:
        return msgs
    return [x.render() for x in check_token_ownership_unique(metas)]


def _scan_docs_token_dependency_resolved(root: Path, *, harness: dict | None = None) -> list[str]:
    _manifest, _docs, metas, msgs = _load_docs_quality_context(root, harness)
    if msgs:
        return msgs
    return [x.render() for x in check_token_dependency_resolved(metas)]


def _scan_docs_instructions_complete(root: Path, *, harness: dict | None = None) -> list[str]:
    _manifest, _docs, metas, msgs = _load_docs_quality_context(root, harness)
    if msgs:
        return msgs
    return [x.render() for x in check_instructions_complete(root, metas)]


def _scan_docs_command_examples_verified(root: Path, *, harness: dict | None = None) -> list[str]:
    _manifest, docs, _metas, msgs = _load_docs_quality_context(root, harness)
    if msgs:
        return msgs
    return [x.render() for x in check_command_examples_verified(root, docs)]


def _scan_docs_example_id_uniqueness(root: Path, *, harness: dict | None = None) -> list[str]:
    _manifest, _docs, metas, msgs = _load_docs_quality_context(root, harness)
    if msgs:
        return msgs
    return [x.render() for x in check_example_id_uniqueness(metas)]


def _scan_docs_generated_files_clean(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("docs_quality")
    if not isinstance(cfg, dict):
        return ["docs.generated_files_clean requires harness.docs_quality mapping in governance spec"]
    manifest, _docs, metas, msgs = _load_docs_quality_context(root, harness)
    if msgs:
        return msgs

    index_rel = str(cfg.get("index_out", "docs/book/reference_index.md")).strip()
    coverage_rel = str(cfg.get("coverage_out", "docs/book/reference_coverage.md")).strip()
    graph_rel = str(cfg.get("graph_out", "docs/book/docs_graph.json")).strip()
    index_path = _join_contract_path(root, index_rel)
    coverage_path = _join_contract_path(root, coverage_rel)
    graph_path = _join_contract_path(root, graph_rel)

    out: list[str] = []
    expected_index = render_reference_index(manifest)
    expected_coverage = render_reference_coverage(root, metas)
    expected_graph = json.dumps(build_docs_graph(root, metas), indent=2, sort_keys=True) + "\n"

    def _append_mismatch(rel: str, path: Path, expected: str) -> None:
        if not path.exists():
            out.append(f"{rel}:1: generated file missing")
            return
        actual = path.read_text(encoding="utf-8")
        if actual == expected:
            return
        exp_lines = expected.splitlines()
        act_lines = actual.splitlines()
        max_len = max(len(exp_lines), len(act_lines))
        line_no = 1
        for i in range(max_len):
            e = exp_lines[i] if i < len(exp_lines) else "<EOF>"
            a = act_lines[i] if i < len(act_lines) else "<EOF>"
            if e != a:
                line_no = i + 1
                out.append(
                    f"{rel}:{line_no}: generated file out of date "
                    f"(expected={e!r} actual={a!r})"
                )
                return
        out.append(f"{rel}:1: generated file out of date")

    _append_mismatch(index_rel, index_path, expected_index)
    _append_mismatch(coverage_rel, coverage_path, expected_coverage)
    _append_mismatch(graph_rel, graph_path, expected_graph)
    return out


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
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing required section-checked file")
            continue
        lower = p.read_text(encoding="utf-8").lower()
        missing = [tok for tok in tokens if tok.lower() not in lower]
        if missing:
            violations.append(f"{rel}:1: missing required token(s): {', '.join(missing)}")
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
        p = _join_contract_path(root, rel)
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
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing python script for CLI docs scan")
            continue
        python_flags[rel] = _extract_python_script_flags(p)

    php_flags: dict[str, set[str]] = {}
    for rel in php_scripts:
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing php script for CLI docs scan")
            continue
        php_flags[rel] = _extract_php_script_flags(p)

    doc_cache: dict[str, str] = {}
    for rel in [*python_docs, *php_docs]:
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing documentation file for CLI docs scan")
            continue
        doc_cache[rel] = p.read_text(encoding="utf-8")

    for script_rel, flags in sorted(python_flags.items()):
        for flag in sorted(flags):
            for doc_rel in python_docs:
                text = doc_cache.get(doc_rel)
                if text is None:
                    continue
                if flag not in text:
                    violations.append(
                        f"{doc_rel}:1: missing CLI flag {flag} documented from {script_rel}"
                    )

    for script_rel, flags in sorted(php_flags.items()):
        for flag in sorted(flags):
            for doc_rel in php_docs:
                text = doc_cache.get(doc_rel)
                if text is None:
                    continue
                if flag not in text:
                    violations.append(
                        f"{doc_rel}:1: missing CLI flag {flag} documented from {script_rel}"
                    )
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
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing doc_sync file")
            continue
        loaded[rel] = p.read_text(encoding="utf-8").lower()
    if len(loaded) < 2:
        return violations

    for tok in tokens:
        want = tok.lower()
        for rel, text in loaded.items():
            if want not in text:
                violations.append(f"{rel}:1: missing sync token {tok}")
    return violations


def _scan_docs_make_commands_sync(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    cfg = h.get("make_commands")
    if not isinstance(cfg, dict):
        return ["docs.make_commands_sync requires harness.make_commands mapping in governance spec"]
    files = cfg.get("files")
    required_tokens = cfg.get("required_tokens")
    if (
        not isinstance(files, list)
        or not files
        or any(not isinstance(x, str) or not x.strip() for x in files)
    ):
        return ["harness.make_commands.files must be a non-empty list of non-empty strings"]
    if (
        not isinstance(required_tokens, list)
        or not required_tokens
        or any(not isinstance(x, str) or not x.strip() for x in required_tokens)
    ):
        return ["harness.make_commands.required_tokens must be a non-empty list of non-empty strings"]
    for rel in files:
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing docs file for make command sync check")
            continue
        text = p.read_text(encoding="utf-8")
        for tok in required_tokens:
            if tok not in text:
                violations.append(f"{rel}:1: missing required make command token {tok}")
    return violations


def _scan_docs_adoption_profiles_sync(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    cfg = h.get("adoption_profiles")
    if not isinstance(cfg, dict):
        return ["docs.adoption_profiles_sync requires harness.adoption_profiles mapping in governance spec"]
    files = cfg.get("files")
    required_tokens = cfg.get("required_tokens")
    if (
        not isinstance(files, list)
        or not files
        or any(not isinstance(x, str) or not x.strip() for x in files)
    ):
        return ["harness.adoption_profiles.files must be a non-empty list of non-empty strings"]
    if (
        not isinstance(required_tokens, list)
        or not required_tokens
        or any(not isinstance(x, str) or not x.strip() for x in required_tokens)
    ):
        return ["harness.adoption_profiles.required_tokens must be a non-empty list of non-empty strings"]
    for rel in files:
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing docs file for adoption profile sync check")
            continue
        text = p.read_text(encoding="utf-8")
        for tok in required_tokens:
            if tok not in text:
                violations.append(f"{rel}:1: missing required adoption-profile token {tok}")
    return violations


def _scan_docs_release_contract_automation_policy(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    cfg = h.get("release_contract")
    if not isinstance(cfg, dict):
        return ["docs.release_contract_automation_policy requires harness.release_contract mapping in governance spec"]
    files = cfg.get("files")
    required_tokens = cfg.get("required_tokens")
    forbidden_patterns = cfg.get("forbidden_patterns", [])
    if (
        not isinstance(files, list)
        or not files
        or any(not isinstance(x, str) or not x.strip() for x in files)
    ):
        return ["harness.release_contract.files must be a non-empty list of non-empty strings"]
    if (
        not isinstance(required_tokens, list)
        or not required_tokens
        or any(not isinstance(x, str) or not x.strip() for x in required_tokens)
    ):
        return ["harness.release_contract.required_tokens must be a non-empty list of non-empty strings"]
    if not isinstance(forbidden_patterns, list) or any(not isinstance(x, str) or not x.strip() for x in forbidden_patterns):
        return ["harness.release_contract.forbidden_patterns must be a list of non-empty strings"]

    compiled: list[re.Pattern[str]] = []
    for pat in forbidden_patterns:
        try:
            compiled.append(re.compile(str(pat), re.MULTILINE))
        except re.error as exc:
            return [f"harness.release_contract.forbidden_patterns invalid regex {pat!r}: {exc}"]

    for rel in files:
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing release contract doc")
            continue
        text = p.read_text(encoding="utf-8")
        for tok in required_tokens:
            if tok not in text:
                violations.append(f"{rel}:1: missing required release-contract token {tok}")
        for pat in compiled:
            if pat.search(text):
                violations.append(
                    f"{rel}:1: forbidden manual-choreography pattern matched /{pat.pattern}/"
                )
    return violations


def _scan_runtime_scope_sync(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    cfg = h.get("runtime_scope")
    if not isinstance(cfg, dict):
        return ["runtime.scope_sync requires harness.runtime_scope mapping in governance spec"]
    files = cfg.get("files")
    required_tokens = cfg.get("required_tokens")
    forbidden_tokens = cfg.get("forbidden_tokens", [])
    if (
        not isinstance(files, list)
        or not files
        or any(not isinstance(x, str) or not x.strip() for x in files)
    ):
        return ["harness.runtime_scope.files must be a non-empty list of non-empty strings"]
    if (
        not isinstance(required_tokens, list)
        or not required_tokens
        or any(not isinstance(x, str) or not x.strip() for x in required_tokens)
    ):
        return ["harness.runtime_scope.required_tokens must be a non-empty list of non-empty strings"]
    if not isinstance(forbidden_tokens, list) or any(not isinstance(x, str) or not x.strip() for x in forbidden_tokens):
        return ["harness.runtime_scope.forbidden_tokens must be a list of non-empty strings"]
    for rel in files:
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing runtime-scope doc")
            continue
        text = p.read_text(encoding="utf-8")
        for tok in required_tokens:
            if tok not in text:
                violations.append(f"{rel}:1: missing required runtime-scope token {tok}")
        for tok in forbidden_tokens:
            if tok in text:
                violations.append(f"{rel}:1: forbidden runtime-scope token present {tok}")
    return violations


def _scan_runtime_python_bin_resolver_sync(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    cfg = h.get("python_bin_resolver")
    if not isinstance(cfg, dict):
        return [
            "runtime.python_bin_resolver_sync requires harness.python_bin_resolver mapping in governance spec"
        ]
    files = cfg.get("files")
    helper = str(cfg.get("helper", "")).strip()
    forbidden_tokens = cfg.get("forbidden_tokens", [])
    required_tokens = cfg.get("required_tokens", [])
    if (
        not isinstance(files, list)
        or not files
        or any(not isinstance(x, str) or not x.strip() for x in files)
    ):
        return ["harness.python_bin_resolver.files must be a non-empty list of non-empty strings"]
    if not helper:
        return ["harness.python_bin_resolver.helper must be a non-empty string"]
    if not isinstance(forbidden_tokens, list) or any(not isinstance(x, str) or not x.strip() for x in forbidden_tokens):
        return ["harness.python_bin_resolver.forbidden_tokens must be a list of non-empty strings"]
    if not isinstance(required_tokens, list) or any(not isinstance(x, str) or not x.strip() for x in required_tokens):
        return ["harness.python_bin_resolver.required_tokens must be a list of non-empty strings"]

    helper_path = _join_contract_path(root, helper)
    if not helper_path.exists():
        violations.append(f"{helper}:1: missing shared python-bin resolver helper")

    for rel in files:
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing script for python-bin resolver sync check")
            continue
        text = p.read_text(encoding="utf-8")
        for tok in required_tokens:
            if tok not in text:
                violations.append(f"{rel}:1: missing required python-bin resolver token {tok}")
        for tok in forbidden_tokens:
            if tok in text:
                violations.append(f"{rel}:1: forbidden inline python-bin resolver token {tok}")
    return violations


def _scan_runtime_runner_interface_gate_sync(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    cfg = h.get("runner_interface")
    if not isinstance(cfg, dict):
        return [
            "runtime.runner_interface_gate_sync requires harness.runner_interface mapping in governance spec"
        ]
    files = cfg.get("files")
    required_tokens = cfg.get("required_tokens", [])
    forbidden_tokens = cfg.get("forbidden_tokens", [])
    required_paths = cfg.get("required_paths", [])
    if (
        not isinstance(files, list)
        or not files
        or any(not isinstance(x, str) or not x.strip() for x in files)
    ):
        return ["harness.runner_interface.files must be a non-empty list of non-empty strings"]
    if not isinstance(required_tokens, list) or any(not isinstance(x, str) or not x.strip() for x in required_tokens):
        return ["harness.runner_interface.required_tokens must be a list of non-empty strings"]
    if not isinstance(forbidden_tokens, list) or any(not isinstance(x, str) or not x.strip() for x in forbidden_tokens):
        return ["harness.runner_interface.forbidden_tokens must be a list of non-empty strings"]
    if not isinstance(required_paths, list) or any(not isinstance(x, str) or not x.strip() for x in required_paths):
        return ["harness.runner_interface.required_paths must be a list of non-empty strings"]

    for rel in required_paths:
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing required runner interface path")

    for rel in files:
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: missing gate file for runner interface sync check")
            continue
        text = p.read_text(encoding="utf-8")
        for tok in required_tokens:
            if tok not in text:
                violations.append(f"{rel}:1: missing required runner-interface token {tok}")
        for tok in forbidden_tokens:
            if tok in text:
                violations.append(f"{rel}:1: forbidden direct runtime token {tok}")
    return violations


def _scan_runtime_runner_interface_subcommands(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    cfg = h.get("runner_interface_subcommands")
    if not isinstance(cfg, dict):
        return [
            "runtime.runner_interface_subcommands requires harness.runner_interface_subcommands mapping in governance spec"
        ]
    path = str(cfg.get("path", "")).strip()
    required_subcommands = cfg.get("required_subcommands")
    if not path:
        return ["harness.runner_interface_subcommands.path must be a non-empty string"]
    if (
        not isinstance(required_subcommands, list)
        or not required_subcommands
        or any(not isinstance(x, str) or not x.strip() for x in required_subcommands)
    ):
        return [
            "harness.runner_interface_subcommands.required_subcommands must be a non-empty list of non-empty strings"
        ]

    p = _join_contract_path(root, path)
    if not p.exists():
        return [f"{path}:1: missing runner adapter script"]
    text = p.read_text(encoding="utf-8")
    declared = {m.group(1) for m in re.finditer(r"^\s*([a-z0-9_-]+)\)\s*$", text, flags=re.MULTILINE)}
    for cmd in required_subcommands:
        if cmd not in declared:
            violations.append(f"{path}:1: missing runner-interface subcommand case label: {cmd}")
    return violations


def _scan_runtime_runner_interface_ci_lane(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    cfg = h.get("runner_interface_ci_lane")
    if not isinstance(cfg, dict):
        return [
            "runtime.runner_interface_ci_lane requires harness.runner_interface_ci_lane mapping in governance spec"
        ]
    workflow = str(cfg.get("workflow", "")).strip()
    required_tokens = cfg.get("required_tokens", [])
    if not workflow:
        return ["harness.runner_interface_ci_lane.workflow must be a non-empty string"]
    if (
        not isinstance(required_tokens, list)
        or not required_tokens
        or any(not isinstance(x, str) or not x.strip() for x in required_tokens)
    ):
        return ["harness.runner_interface_ci_lane.required_tokens must be a non-empty list of non-empty strings"]
    p = _join_contract_path(root, workflow)
    if not p.exists():
        return [f"{workflow}:1: missing workflow file for runner interface CI lane check"]
    text = p.read_text(encoding="utf-8")
    for tok in required_tokens:
        if tok not in text:
            violations.append(f"{workflow}:1: missing required CI lane token {tok}")
    return violations


def _scan_runtime_rust_adapter_no_delegate(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    cfg = h.get("rust_adapter")
    if not isinstance(cfg, dict):
        return ["runtime.rust_adapter_no_delegate requires harness.rust_adapter mapping in governance spec"]
    path = str(cfg.get("path", "")).strip()
    required_tokens = cfg.get("required_tokens", [])
    forbidden_tokens = cfg.get("forbidden_tokens", [])
    if not path:
        return ["harness.rust_adapter.path must be a non-empty string"]
    if not isinstance(required_tokens, list) or any(not isinstance(x, str) or not x.strip() for x in required_tokens):
        return ["harness.rust_adapter.required_tokens must be a list of non-empty strings"]
    if not isinstance(forbidden_tokens, list) or any(not isinstance(x, str) or not x.strip() for x in forbidden_tokens):
        return ["harness.rust_adapter.forbidden_tokens must be a list of non-empty strings"]
    p = _join_contract_path(root, path)
    if not p.exists():
        return [f"{path}:1: missing rust adapter script"]
    text = p.read_text(encoding="utf-8")
    for tok in required_tokens:
        if tok not in text:
            violations.append(f"{path}:1: missing required rust-adapter token {tok}")
    for tok in forbidden_tokens:
        if tok in text:
            violations.append(f"{path}:1: forbidden rust-adapter delegation token {tok}")
    return violations


def _scan_runtime_rust_adapter_exec_smoke(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("rust_adapter_exec_smoke")
    if not isinstance(cfg, dict):
        return ["runtime.rust_adapter_exec_smoke requires harness.rust_adapter_exec_smoke mapping in governance spec"]

    raw_command = cfg.get("command")
    command: list[str]
    if isinstance(raw_command, str):
        command = shlex.split(raw_command)
    elif isinstance(raw_command, list) and raw_command:
        if any(not isinstance(x, str) or not x.strip() for x in raw_command):
            return ["harness.rust_adapter_exec_smoke.command list must contain only non-empty strings"]
        command = [x.strip() for x in raw_command]
    else:
        return ["harness.rust_adapter_exec_smoke.command must be a non-empty string or list of strings"]
    if not command:
        return ["harness.rust_adapter_exec_smoke.command must not be empty"]

    expected_exit_codes = cfg.get("expected_exit_codes", [0])
    if (
        not isinstance(expected_exit_codes, list)
        or not expected_exit_codes
        or any(not isinstance(x, int) for x in expected_exit_codes)
    ):
        return ["harness.rust_adapter_exec_smoke.expected_exit_codes must be a non-empty list of integers"]

    required_output_tokens = cfg.get("required_output_tokens", [])
    if not isinstance(required_output_tokens, list) or any(
        not isinstance(x, str) or not x.strip() for x in required_output_tokens
    ):
        return ["harness.rust_adapter_exec_smoke.required_output_tokens must be a list of non-empty strings"]

    forbidden_output_tokens = cfg.get("forbidden_output_tokens", [])
    if not isinstance(forbidden_output_tokens, list) or any(
        not isinstance(x, str) or not x.strip() for x in forbidden_output_tokens
    ):
        return ["harness.rust_adapter_exec_smoke.forbidden_output_tokens must be a list of non-empty strings"]

    timeout_seconds = cfg.get("timeout_seconds", 120)
    if not isinstance(timeout_seconds, (int, float)) or timeout_seconds <= 0:
        return ["harness.rust_adapter_exec_smoke.timeout_seconds must be a positive number"]

    display_cmd = shlex.join(command)
    try:
        result = subprocess.run(
            command,
            cwd=root,
            capture_output=True,
            text=True,
            timeout=float(timeout_seconds),
            check=False,
        )
    except FileNotFoundError:
        return [f"{display_cmd}:1: command not found for rust adapter exec smoke"]
    except PermissionError:
        return [f"{display_cmd}:1: permission denied for rust adapter exec smoke command"]
    except subprocess.TimeoutExpired:
        return [f"{display_cmd}:1: rust adapter exec smoke command timed out after {timeout_seconds}s"]

    violations: list[str] = []
    if result.returncode not in expected_exit_codes:
        violations.append(
            f"{display_cmd}:1: unexpected exit code {result.returncode} "
            f"(expected one of: {expected_exit_codes})"
        )

    combined_output = f"{result.stdout}\n{result.stderr}"
    for tok in required_output_tokens:
        if tok not in combined_output:
            violations.append(f"{display_cmd}:1: missing required output token {tok!r}")
    for tok in forbidden_output_tokens:
        if tok in combined_output:
            violations.append(f"{display_cmd}:1: forbidden output token present {tok!r}")

    return violations


def _scan_runtime_rust_adapter_subcommand_parity(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("rust_subcommand_parity")
    if not isinstance(cfg, dict):
        return [
            "runtime.rust_adapter_subcommand_parity requires harness.rust_subcommand_parity mapping in governance spec"
        ]

    adapter_path = str(cfg.get("adapter_path", "")).strip()
    cli_main_path = str(cfg.get("cli_main_path", "")).strip()
    if not adapter_path:
        return ["harness.rust_subcommand_parity.adapter_path must be a non-empty string"]
    if not cli_main_path:
        return ["harness.rust_subcommand_parity.cli_main_path must be a non-empty string"]

    adapter_file = _join_contract_path(root, adapter_path)
    cli_main_file = _join_contract_path(root, cli_main_path)
    if not adapter_file.exists():
        return [f"{adapter_path}:1: missing rust adapter script for subcommand parity check"]
    if not cli_main_file.exists():
        return [f"{cli_main_path}:1: missing rust cli main source for subcommand parity check"]

    adapter_text = adapter_file.read_text(encoding="utf-8")
    cli_text = cli_main_file.read_text(encoding="utf-8")

    adapter_subcommands = {
        m.group(1)
        for m in re.finditer(r"^\s*([a-z0-9_-]+)\)\s*$", adapter_text, flags=re.MULTILINE)
        if m.group(1) != "*"
    }
    cli_subcommands: set[str] = set()
    for arm in re.finditer(
        r'((?:"[a-z0-9_-]+"\s*(?:\|\s*)?)+)\s*=>',
        cli_text,
        flags=re.MULTILINE,
    ):
        for lit in re.finditer(r'"([a-z0-9_-]+)"', arm.group(1)):
            cli_subcommands.add(lit.group(1))

    if not adapter_subcommands:
        return [f"{adapter_path}:1: no adapter subcommand labels found"]
    if not cli_subcommands:
        return [f"{cli_main_path}:1: no rust cli subcommand match arms found"]

    violations: list[str] = []
    for cmd in sorted(adapter_subcommands - cli_subcommands):
        violations.append(
            f"{cli_main_path}:1: missing rust cli subcommand handler for adapter-exposed command {cmd}"
        )
    for cmd in sorted(cli_subcommands - adapter_subcommands):
        violations.append(
            f"{adapter_path}:1: missing adapter subcommand label for rust cli-exposed command {cmd}"
        )
    return violations


def _scan_naming_filename_policy(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    h = harness or {}
    cfg = h.get("filename_policy")
    if not isinstance(cfg, dict):
        return ["naming.filename_policy requires harness.filename_policy mapping in governance spec"]

    paths = cfg.get("paths")
    if not isinstance(paths, list) or not paths or any(not isinstance(x, str) or not x.strip() for x in paths):
        return ["harness.filename_policy.paths must be a non-empty list of non-empty strings"]

    include_exts = cfg.get("include_extensions", [])
    if not isinstance(include_exts, list) or any(not isinstance(x, str) or not x.strip() for x in include_exts):
        return ["harness.filename_policy.include_extensions must be a list of non-empty strings"]
    include_exts_set = {x.strip().lower() for x in include_exts}

    allow_exact = cfg.get("allow_exact", [])
    if not isinstance(allow_exact, list) or any(not isinstance(x, str) or not x.strip() for x in allow_exact):
        return ["harness.filename_policy.allow_exact must be a list of non-empty strings"]
    allow_exact_set = {x.strip() for x in allow_exact}

    allowed_name_regex = str(
        cfg.get("allowed_name_regex", r"^[a-z0-9]+(?:[._-][a-z0-9]+)*$")
    ).strip()
    if not allowed_name_regex:
        return ["harness.filename_policy.allowed_name_regex must be non-empty"]
    try:
        allowed_re = re.compile(allowed_name_regex)
    except re.error as exc:
        return [f"harness.filename_policy.allowed_name_regex invalid: {exc}"]

    for rel_root in paths:
        base = _join_contract_path(root, rel_root)
        if not base.exists():
            violations.append(f"{rel_root}:1: missing path for filename policy scan")
            continue
        if not base.is_dir():
            violations.append(f"{rel_root}:1: expected directory for filename policy scan")
            continue
        for p in sorted(base.rglob("*")):
            if not p.is_file():
                continue
            if include_exts_set and p.suffix.lower() not in include_exts_set:
                continue
            name = p.name
            if name in allow_exact_set:
                continue
            if not allowed_re.fullmatch(name):
                rel = p.relative_to(root)
                violations.append(
                    f"{rel}: filename {name!r} must match {allowed_name_regex} "
                    "(lowercase words with '_' for spaces and '-' for section separators)"
                )
    return violations


def _scan_normalization_virtual_root_paths_only(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    scope = [
        root / "docs/spec/conformance/cases",
        root / "docs/spec/governance/cases",
        root / "docs/spec/libraries",
    ]
    for base in scope:
        if not base.exists():
            continue
        for doc_path, case in _iter_all_spec_cases(base):
            rel = doc_path.relative_to(root)
            case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
            for field, raw in _iter_path_fields(case):
                s = str(raw).strip()
                if not s or s.startswith("external://"):
                    continue
                try:
                    normalized = normalize_contract_path(s, field=f"{case_id}.{field}")
                except VirtualPathError:
                    violations.append(f"{rel}: case {case_id} has invalid virtual path at {field}: {s}")
                    continue
                if s != normalized:
                    violations.append(
                        f"{rel}: case {case_id} non-canonical path at {field}: {s!r} -> {normalized!r}"
                    )
    return violations


def _scan_reference_contract_paths_exist(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    scope = [
        root / "docs/spec/conformance/cases",
        root / "docs/spec/governance/cases",
        root / "docs/spec/libraries",
    ]
    must_exist_keys = {
        "path",
        "library_paths",
        "cases_path",
        "baseline_path",
        "manifest_path",
        "required_paths",
        "adapter_path",
        "cli_main_path",
        "required_library_path",
        "reference_manifest",
    }
    for base in scope:
        if not base.exists():
            continue
        for doc_path, case in _iter_all_spec_cases(base):
            rel = doc_path.relative_to(root)
            case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
            for field, raw in _iter_path_fields(case):
                if field.split(".")[-1].split("[", 1)[0] not in must_exist_keys:
                    continue
                s = str(raw).strip()
                if not s or s.startswith("external://"):
                    continue
                try:
                    p = _resolve_contract_config_path(root, s, field=field)
                except VirtualPathError:
                    violations.append(f"{rel}: case {case_id} has invalid path at {field}: {s}")
                    continue
                if not p.exists():
                    violations.append(f"{rel}: case {case_id} references missing path at {field}: {s}")
    return violations


def _scan_reference_check_ids_exist(root: Path, *, harness: dict | None = None) -> list[str]:
    cases_dir = root / "docs/spec/governance/cases"
    if not cases_dir.exists():
        return []
    violations: list[str] = []
    for spec in iter_cases(cases_dir, file_pattern=SETTINGS.case.default_file_pattern):
        case_id = str(spec.test.get("id", "<unknown>")).strip() or "<unknown>"
        check_id = str(spec.test.get("check", "")).strip()
        if not check_id:
            violations.append(f"{spec.doc_path.relative_to(root)}: case {case_id} missing check id")
            continue
        if check_id not in _CHECKS:
            violations.append(f"{spec.doc_path.relative_to(root)}: case {case_id} unknown check id: {check_id}")
    return violations


def _scan_reference_symbols_exist(root: Path, *, harness: dict | None = None) -> list[str]:
    cases_dir = root / "docs/spec/governance/cases"
    if not cases_dir.exists():
        return []
    violations: list[str] = []
    limits = SpecLangLimits()
    for spec in iter_cases(cases_dir, file_pattern=SETTINGS.case.default_file_pattern):
        harness_map = spec.test.get("harness")
        if not isinstance(harness_map, dict):
            continue
        spec_lang_cfg = harness_map.get("spec_lang")
        if not isinstance(spec_lang_cfg, dict):
            continue
        if not spec_lang_cfg.get("library_paths"):
            continue
        try:
            load_spec_lang_symbols_for_case(
                doc_path=spec.doc_path,
                harness=harness_map,
                limits=limits,
            )
        except Exception as exc:  # noqa: BLE001
            case_id = str(spec.test.get("id", "<unknown>")).strip() or "<unknown>"
            violations.append(
                f"{spec.doc_path.relative_to(root)}: case {case_id} library symbol/path reference error ({exc})"
            )
    return violations


def _collect_var_symbols(expr: object) -> set[str]:
    out: set[str] = set()
    if isinstance(expr, dict):
        raw_var = expr.get("var")
        if isinstance(raw_var, str):
            sym = raw_var.strip()
            if sym:
                out.add(sym)
        for value in expr.values():
            out.update(_collect_var_symbols(value))
        return out
    if isinstance(expr, list):
        for value in expr:
            out.update(_collect_var_symbols(value))
    return out


def _iter_evaluate_expr_nodes(assert_node: object) -> list[object]:
    out: list[object] = []
    if isinstance(assert_node, list):
        for child in assert_node:
            out.extend(_iter_evaluate_expr_nodes(child))
        return out
    if not isinstance(assert_node, dict):
        return out
    for key in ("must", "can", "cannot"):
        raw_children = assert_node.get(key)
        if isinstance(raw_children, list):
            for child in raw_children:
                out.extend(_iter_evaluate_expr_nodes(child))
    raw_eval = assert_node.get("evaluate")
    if isinstance(raw_eval, list):
        out.extend(raw_eval)
    return out


def _scan_reference_policy_symbols_resolve(root: Path, *, harness: dict | None = None) -> list[str]:
    cases_dir = root / "docs/spec/governance/cases"
    if not cases_dir.exists():
        return []
    limits = SpecLangLimits()
    violations: list[str] = []
    for spec in iter_cases(cases_dir, file_pattern=SETTINGS.case.default_file_pattern):
        case = spec.test if isinstance(spec.test, dict) else {}
        if str(case.get("type", "")).strip() != "governance.check":
            continue
        case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
        harness_map = case.get("harness")
        if not isinstance(harness_map, dict):
            continue
        policy = harness_map.get("policy_evaluate")
        if not isinstance(policy, list) or not policy:
            continue
        policy_refs = {sym for sym in _collect_var_symbols(policy) if "." in sym}
        if not policy_refs:
            continue
        try:
            symbols = load_spec_lang_symbols_for_case(
                doc_path=spec.doc_path,
                harness=harness_map,
                limits=limits,
            )
        except Exception as exc:  # noqa: BLE001
            violations.append(
                f"{spec.doc_path.relative_to(root)}: case {case_id} unable to load policy symbols ({exc})"
            )
            continue
        unresolved = sorted(sym for sym in policy_refs if sym not in symbols)
        if unresolved:
            violations.append(
                f"{spec.doc_path.relative_to(root)}: case {case_id} unresolved policy symbols: "
                + ", ".join(unresolved)
            )
    return violations


def _scan_reference_library_exports_used(root: Path, *, harness: dict | None = None) -> list[str]:
    libs_root = root / "docs/spec/libraries"
    if not libs_root.exists():
        return []
    exported: dict[str, Path] = {}
    violations: list[str] = []
    for lib_file in sorted(libs_root.rglob("*.spec.md")):
        if not lib_file.is_file():
            continue
        try:
            loaded = load_external_cases(lib_file, formats={"md"})
        except Exception as exc:  # noqa: BLE001
            violations.append(f"{lib_file.relative_to(root)}: unable to parse library file ({exc})")
            continue
        for _doc_path, case in loaded:
            if str(case.get("type", "")).strip() != "spec_lang.library":
                continue
            raw_definitions = case.get("definitions")
            if not isinstance(raw_definitions, dict):
                continue
            raw_public = raw_definitions.get("public")
            if not isinstance(raw_public, dict):
                continue
            for raw in raw_public.keys():
                sym = str(raw).strip()
                if not sym:
                    continue
                prior = exported.get(sym)
                if prior is not None and prior != lib_file:
                    violations.append(
                        f"{lib_file.relative_to(root)}: duplicate export symbol '{sym}' also exported by {prior.relative_to(root)}"
                    )
                    continue
                exported[sym] = lib_file
    if violations:
        return violations

    referenced: set[str] = set()
    scan_roots = [
        root / "docs/spec/conformance/cases",
        root / "docs/spec/governance/cases",
        root / "docs/spec/impl",
        root / "docs/spec/libraries",
    ]
    for base in scan_roots:
        if not base.exists():
            continue
        for doc_path, case in _iter_all_spec_cases(base):
            h = case.get("harness")
            if isinstance(h, dict):
                spec_lang = h.get("spec_lang")
                if isinstance(spec_lang, dict):
                    raw_exports = spec_lang.get("exports")
                    if isinstance(raw_exports, list):
                        for raw in raw_exports:
                            sym = str(raw).strip()
                            if sym and "." in sym:
                                referenced.add(sym)
                policy = h.get("policy_evaluate")
                if isinstance(policy, list):
                    referenced.update(sym for sym in _collect_var_symbols(policy) if "." in sym)
            raw_assert = case.get("assert")
            if isinstance(raw_assert, list):
                for expr in _iter_evaluate_expr_nodes(raw_assert):
                    referenced.update(sym for sym in _collect_var_symbols(expr) if "." in sym)
            if str(case.get("type", "")).strip() == "spec_lang.library":
                raw_definitions = case.get("definitions")
                if isinstance(raw_definitions, dict):
                    for scope in ("public", "private"):
                        scoped = raw_definitions.get(scope)
                        if isinstance(scoped, dict):
                            for expr in scoped.values():
                                referenced.update(
                                    sym for sym in _collect_var_symbols(expr) if "." in sym
                                )

    for sym, src in sorted(exported.items(), key=lambda item: item[0]):
        if sym not in referenced:
            violations.append(
                f"{src.relative_to(root)}: exported symbol '{sym}' is not referenced by any case policy/expression or harness.spec_lang.exports"
            )
    return violations


def _scan_library_public_surface_model(root: Path, *, harness: dict | None = None) -> list[str]:
    libs_root = root / "docs/spec/libraries"
    if not libs_root.exists():
        return []
    violations: list[str] = []
    for lib_file in sorted(libs_root.rglob("*.spec.md")):
        if not lib_file.is_file():
            continue
        try:
            loaded = load_external_cases(lib_file, formats={"md"})
        except Exception as exc:  # noqa: BLE001
            violations.append(f"{lib_file.relative_to(root)}: unable to parse library file ({exc})")
            continue
        for _doc_path, case in loaded:
            if str(case.get("type", "")).strip() != "spec_lang.library":
                continue
            raw_definitions = case.get("definitions")
            if not isinstance(raw_definitions, dict):
                violations.append(
                    f"{lib_file.relative_to(root)}: spec_lang.library requires definitions mapping"
                )
                continue
            raw_public = raw_definitions.get("public")
            raw_private = raw_definitions.get("private")
            if not isinstance(raw_public, dict) and not isinstance(raw_private, dict):
                violations.append(
                    f"{lib_file.relative_to(root)}: spec_lang.library requires definitions.public or definitions.private mapping"
                )
                continue
            public_symbols: set[str] = set()
            private_symbols: set[str] = set()
            if isinstance(raw_public, dict):
                public_symbols.update(str(k).strip() for k in raw_public)
            if isinstance(raw_private, dict):
                private_symbols.update(str(k).strip() for k in raw_private)
            if public_symbols and private_symbols:
                overlap = sorted(public_symbols.intersection(private_symbols))
                overlap = [s for s in overlap if s]
                if overlap:
                    violations.append(
                        f"{lib_file.relative_to(root)}: duplicate symbol across definitions.public/definitions.private: "
                        + ", ".join(overlap)
                    )
    return violations


def _scan_reference_private_symbols_forbidden(root: Path, *, harness: dict | None = None) -> list[str]:
    libs_root = root / "docs/spec/libraries"
    private_symbols: set[str] = set()
    if libs_root.exists():
        for lib_file in sorted(libs_root.rglob("*.spec.md")):
            if not lib_file.is_file():
                continue
            try:
                loaded = load_external_cases(lib_file, formats={"md"})
            except Exception:
                continue
            for _doc_path, case in loaded:
                if str(case.get("type", "")).strip() != "spec_lang.library":
                    continue
                raw_definitions = case.get("definitions")
                if not isinstance(raw_definitions, dict):
                    continue
                raw_private = raw_definitions.get("private")
                if not isinstance(raw_private, dict):
                    continue
                for sym in raw_private.keys():
                    s = str(sym).strip()
                    if s:
                        private_symbols.add(s)
    if not private_symbols:
        return []

    violations: list[str] = []
    scan_roots = [
        root / "docs/spec/conformance/cases",
        root / "docs/spec/governance/cases",
        root / "docs/spec/impl",
    ]
    for base in scan_roots:
        if not base.exists():
            continue
        for doc_path, case in _iter_all_spec_cases(base):
            case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
            rel = doc_path.relative_to(root)
            refs: set[str] = set()
            h = case.get("harness")
            if isinstance(h, dict):
                policy = h.get("policy_evaluate")
                if isinstance(policy, list):
                    refs.update(sym for sym in _collect_var_symbols(policy) if "." in sym)
                spec_lang = h.get("spec_lang")
                if isinstance(spec_lang, dict):
                    raw_exports = spec_lang.get("exports")
                    if isinstance(raw_exports, list):
                        for raw in raw_exports:
                            sym = str(raw).strip()
                            if sym and "." in sym:
                                refs.add(sym)
            raw_assert = case.get("assert")
            if isinstance(raw_assert, list):
                for expr in _iter_evaluate_expr_nodes(raw_assert):
                    refs.update(sym for sym in _collect_var_symbols(expr) if "." in sym)
            bad = sorted(sym for sym in refs if sym in private_symbols)
            if bad:
                violations.append(
                    f"{rel}: case {case_id} references private library symbols: " + ", ".join(bad)
                )
    return violations


def _scan_reference_external_refs_policy(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    scope = [
        root / "docs/spec/conformance/cases",
        root / "docs/spec/governance/cases",
        root / "docs/spec/libraries",
    ]
    for base in scope:
        if not base.exists():
            continue
        for doc_path, case in _iter_all_spec_cases(base):
            rel = doc_path.relative_to(root)
            case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
            requires = dict(case.get("requires") or {})
            caps = set(str(x).strip() for x in (requires.get("capabilities") or []) if str(x).strip())
            h = dict(case.get("harness") or {})
            ext_cfg = dict(h.get("external_refs") or {})
            mode = str(ext_cfg.get("mode", "deny")).strip().lower() or "deny"
            providers = set(
                str(x).strip() for x in (ext_cfg.get("providers") or []) if str(x).strip()
            )
            for field, raw in _iter_path_fields(case):
                ext = parse_external_ref(str(raw).strip())
                if ext is None:
                    continue
                if "external.ref.v1" not in caps:
                    violations.append(
                        f"{rel}: case {case_id} external ref at {field} requires capabilities including external.ref.v1"
                    )
                if mode != "allow":
                    violations.append(
                        f"{rel}: case {case_id} external ref at {field} requires harness.external_refs.mode=allow"
                    )
                if ext.provider not in providers:
                    violations.append(
                        f"{rel}: case {case_id} external provider {ext.provider} not allowlisted at {field}"
                    )
    return violations


def _scan_reference_token_anchors_exist(root: Path, *, harness: dict | None = None) -> list[str]:
    h = harness or {}
    cfg = h.get("token_anchors")
    if cfg is None:
        return []
    if not isinstance(cfg, dict):
        return ["reference.token_anchors_exist requires harness.token_anchors mapping in governance spec"]
    files = cfg.get("files")
    if not isinstance(files, list):
        return ["harness.token_anchors.files must be a list"]
    violations: list[str] = []
    for idx, entry in enumerate(files):
        if not isinstance(entry, dict):
            violations.append(f"harness.token_anchors.files[{idx}] must be a mapping")
            continue
        rel = str(entry.get("path", "")).strip()
        tokens = entry.get("tokens")
        if not rel:
            violations.append(f"harness.token_anchors.files[{idx}].path must be non-empty")
            continue
        if not isinstance(tokens, list) or any(not isinstance(t, str) or not t.strip() for t in tokens):
            violations.append(f"harness.token_anchors.files[{idx}].tokens must be a list of non-empty strings")
            continue
        try:
            p = _resolve_contract_config_path(root, rel, field=f"token_anchors.files[{idx}].path")
        except VirtualPathError as exc:
            violations.append(str(exc))
            continue
        if not p.exists():
            violations.append(f"{rel}:1: token anchor file does not exist")
            continue
        text = p.read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                violations.append(f"{rel}:1: missing token anchor {token!r}")
    return violations


def _scan_spec_layout_domain_trees(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    for rel_root in _DOMAIN_TREE_ROOTS:
        base = _join_contract_path(root, rel_root)
        if not base.exists():
            violations.append(f"{rel_root}:1: missing required domain root")
            continue
        if not base.is_dir():
            violations.append(f"{rel_root}:1: expected directory")
            continue
        direct_cases = sorted(p for p in base.glob("*.spec.md") if p.is_file())
        for p in direct_cases:
            violations.append(
                f"{p.relative_to(root)}: spec files must live under domain subdirectories (for example {rel_root}/core/)"
            )
        domain_dirs = sorted(
            p for p in base.iterdir() if p.is_dir() and not p.name.startswith(".")
        )
        if not domain_dirs:
            violations.append(f"{rel_root}:1: expected at least one domain subdirectory")
            continue
        for domain_dir in domain_dirs:
            has_specs = any(domain_dir.rglob("*.spec.md"))
            if not has_specs:
                continue
            index_path = domain_dir / "index.md"
            if not index_path.exists():
                violations.append(
                    f"{index_path.relative_to(root)}: missing required domain index.md"
                )
    return violations


def _scan_spec_domain_index_sync(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    for rel_root in _DOMAIN_TREE_ROOTS:
        base = _join_contract_path(root, rel_root)
        if not base.exists() or not base.is_dir():
            continue
        domain_dirs = sorted(
            p for p in base.iterdir() if p.is_dir() and not p.name.startswith(".")
        )
        for domain_dir in domain_dirs:
            spec_files = sorted(p for p in domain_dir.glob("*.spec.md") if p.is_file())
            if not spec_files:
                continue
            index_path = domain_dir / "index.md"
            if not index_path.exists():
                continue
            raw = index_path.read_text(encoding="utf-8")
            for p in spec_files:
                rel = "/" + p.relative_to(root).as_posix()
                if rel not in raw:
                    violations.append(
                        f"{index_path.relative_to(root)}: missing indexed path: {rel}"
                    )
            # Ensure stale entries are not retained.
            for m in re.finditer(r"`(/docs/spec/[^`]+\.spec\.md)`", raw):
                rel = m.group(1)
                target = _join_contract_path(root, rel)
                if not target.exists():
                    line = raw[: m.start()].count("\n") + 1
                    violations.append(
                        f"{index_path.relative_to(root)}:{line}: stale indexed path missing from tree: {rel}"
                    )
    return violations


def _scan_library_domain_ownership(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    # Conformance cases: conformance libraries only.
    conformance_root = root / "docs/spec/conformance/cases"
    if conformance_root.exists():
        for doc_path, case in _iter_all_spec_cases(conformance_root):
            case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
            h = case.get("harness")
            if not isinstance(h, dict):
                continue
            spec_lang = h.get("spec_lang")
            if not isinstance(spec_lang, dict):
                continue
            libs = spec_lang.get("library_paths")
            if not isinstance(libs, list):
                continue
            for idx, raw in enumerate(libs):
                s = str(raw).strip()
                if not s or s.startswith("external://"):
                    continue
                try:
                    normalized = normalize_contract_path(
                        s, field=f"{case_id}.harness.spec_lang.library_paths[{idx}]"
                    )
                except VirtualPathError:
                    continue
                if not (
                    normalized.startswith("/docs/spec/libraries/conformance/")
                    or normalized.startswith("/docs/spec/libraries/domain/")
                ):
                    rel = doc_path.relative_to(root)
                    violations.append(
                        f"{rel}: case {case_id} library_paths[{idx}] must be under "
                        "/docs/spec/libraries/conformance/ or /docs/spec/libraries/domain/"
                    )

    # Governance cases: policy/path libraries only.
    governance_root = root / "docs/spec/governance/cases"
    if governance_root.exists():
        for doc_path, case in _iter_all_spec_cases(governance_root):
            case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
            h = case.get("harness")
            if not isinstance(h, dict):
                continue
            spec_lang = h.get("spec_lang")
            if not isinstance(spec_lang, dict):
                continue
            libs = spec_lang.get("library_paths")
            if not isinstance(libs, list):
                continue
            for idx, raw in enumerate(libs):
                s = str(raw).strip()
                if not s or s.startswith("external://"):
                    continue
                try:
                    normalized = normalize_contract_path(
                        s, field=f"{case_id}.harness.spec_lang.library_paths[{idx}]"
                    )
                except VirtualPathError:
                    continue
                allowed = (
                    normalized.startswith("/docs/spec/libraries/policy/")
                    or normalized.startswith("/docs/spec/libraries/path/")
                )
                if not allowed:
                    rel = doc_path.relative_to(root)
                    violations.append(
                        f"{rel}: case {case_id} library_paths[{idx}] must be under "
                        "/docs/spec/libraries/policy/ or /docs/spec/libraries/path/"
                    )
    return violations


def _scan_library_domain_index_sync(root: Path, *, harness: dict | None = None) -> list[str]:
    violations: list[str] = []
    libs_root = root / "docs/spec/libraries"
    if not libs_root.exists():
        return ["docs/spec/libraries:1: missing libraries root"]

    for domain_dir in sorted(p for p in libs_root.iterdir() if p.is_dir() and not p.name.startswith(".")):
        spec_files = sorted(p for p in domain_dir.glob("*.spec.md") if p.is_file())
        if not spec_files:
            continue
        index_path = domain_dir / "index.md"
        if not index_path.exists():
            violations.append(f"{index_path.relative_to(root)}: missing required domain index.md")
            continue
        raw = index_path.read_text(encoding="utf-8")
        if "## Exported Symbols" not in raw:
            violations.append(f"{index_path.relative_to(root)}: missing '## Exported Symbols' section")
        for p in spec_files:
            rel = "/" + p.relative_to(root).as_posix()
            if rel not in raw:
                violations.append(f"{index_path.relative_to(root)}: missing indexed path: {rel}")
            try:
                loaded = load_external_cases(p, formats={"md"})
            except Exception as exc:  # noqa: BLE001
                violations.append(f"{p.relative_to(root)}: unable to parse library file ({exc})")
                continue
            exports: list[str] = []
            for _doc_path, case in loaded:
                if str(case.get("type", "")).strip() != "spec_lang.library":
                    continue
                raw_definitions = case.get("definitions")
                if not isinstance(raw_definitions, dict):
                    continue
                raw_public = raw_definitions.get("public")
                if not isinstance(raw_public, dict):
                    continue
                for item in raw_public.keys():
                    sym = str(item).strip()
                    if sym:
                        exports.append(sym)
            for sym in sorted(dict.fromkeys(exports)):
                token = f"`{sym}` ({rel})"
                if token not in raw:
                    violations.append(
                        f"{index_path.relative_to(root)}: missing exported symbol entry {token}"
                    )
        for m in re.finditer(r"`(/docs/spec/libraries/[^`]+\.spec\.md)`", raw):
            rel = m.group(1)
            target = _join_contract_path(root, rel)
            if not target.exists():
                line = raw[: m.start()].count("\n") + 1
                violations.append(
                    f"{index_path.relative_to(root)}:{line}: stale indexed path missing from tree: {rel}"
                )
    return violations


def _load_normalization_profile(root: Path) -> tuple[dict[str, object] | None, list[str]]:
    p = root / _NORMALIZATION_PROFILE_PATH
    if not p.exists():
        return None, [f"{_NORMALIZATION_PROFILE_PATH}:1: missing normalization profile"]
    try:
        payload = yaml.safe_load(p.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        return None, [f"{_NORMALIZATION_PROFILE_PATH}:1: invalid yaml ({exc})"]
    if not isinstance(payload, dict):
        return None, [f"{_NORMALIZATION_PROFILE_PATH}:1: profile must be a mapping"]
    return payload, []


def _scan_normalization_profile_sync(root: Path, *, harness: dict | None = None) -> list[str]:
    profile, errs = _load_normalization_profile(root)
    if errs:
        return errs
    assert profile is not None
    violations: list[str] = []
    required_top = ("version", "paths", "expression", "spec_style", "docs_token_sync")
    for key in required_top:
        if key not in profile:
            violations.append(f"{_NORMALIZATION_PROFILE_PATH}:1: missing required key: {key}")
    paths = profile.get("paths")
    if not isinstance(paths, dict):
        violations.append(f"{_NORMALIZATION_PROFILE_PATH}:1: paths must be a mapping")
    else:
        for key in ("specs", "contracts", "tests"):
            vals = paths.get(key)
            if not isinstance(vals, list) or not vals or any(not isinstance(x, str) or not x.strip() for x in vals):
                violations.append(f"{_NORMALIZATION_PROFILE_PATH}:1: paths.{key} must be a non-empty list of strings")
    expr = profile.get("expression")
    if not isinstance(expr, dict):
        violations.append(f"{_NORMALIZATION_PROFILE_PATH}:1: expression must be a mapping")
    else:
        fields = expr.get("expression_fields")
        if not isinstance(fields, list) or "evaluate" not in fields or "policy_evaluate" not in fields:
            violations.append(
                f"{_NORMALIZATION_PROFILE_PATH}:1: expression.expression_fields must include evaluate and policy_evaluate"
            )
    return violations


def _scan_normalization_mapping_ast_only(root: Path, *, harness: dict | None = None) -> list[str]:
    cmd = [sys.executable, "scripts/normalize_repo.py", "--check", "--scope", "all"]
    proc = subprocess.run(cmd, cwd=root, capture_output=True, text=True, check=False)
    if proc.returncode == 0:
        return []
    out = (proc.stdout or "").splitlines() + (proc.stderr or "").splitlines()
    violations = [line.strip() for line in out if line.strip()]
    return violations or ["normalization.mapping_ast_only: normalize check failed"]


def _scan_normalization_library_mapping_ast_only(root: Path, *, harness: dict | None = None) -> list[str]:
    libs_root = root / "docs/spec/libraries"
    if not libs_root.exists():
        return []
    violations: list[str] = []
    for p in sorted(libs_root.rglob(SETTINGS.case.default_file_pattern)):
        if not p.is_file():
            continue
        rel = p.relative_to(root)
        try:
            specs = list(iter_spec_doc_tests(p.parent, file_pattern=p.name))
        except Exception as exc:  # noqa: BLE001
            violations.append(f"{rel}:1: unable to parse library spec file: {exc}")
            continue
        for spec in specs:
            case = spec.test
            case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
            if str(case.get("type", "")).strip() != "spec_lang.library":
                continue
            definitions = case.get("definitions")
            if not isinstance(definitions, dict) or not definitions:
                violations.append(f"{rel}: case {case_id} must provide non-empty definitions mapping")
                continue
            scopes = []
            raw_public = definitions.get("public")
            raw_private = definitions.get("private")
            if isinstance(raw_public, dict):
                scopes.append(("public", raw_public))
            if isinstance(raw_private, dict):
                scopes.append(("private", raw_private))
            if not scopes:
                violations.append(
                    f"{rel}: case {case_id} must provide definitions.public or definitions.private mapping"
                )
                continue
            for scope_name, scoped_map in scopes:
                for raw_name, expr in scoped_map.items():
                    name = str(raw_name).strip()
                    if not name:
                        violations.append(
                            f"{rel}: case {case_id} has empty symbol name in definitions.{scope_name}"
                        )
                        continue
                    try:
                        compile_yaml_expr_to_sexpr(
                            expr,
                            field_path=(
                                f"{rel.as_posix()} case {case_id} "
                                f"definitions.{scope_name}.{name}"
                            ),
                        )
                    except SpecLangYamlAstError as exc:
                        violations.append(str(exc))
    return violations


def _scan_normalization_docs_token_sync(root: Path, *, harness: dict | None = None) -> list[str]:
    profile, errs = _load_normalization_profile(root)
    if errs:
        return errs
    assert profile is not None
    token_sync = profile.get("docs_token_sync")
    if not isinstance(token_sync, dict):
        return [f"{_NORMALIZATION_PROFILE_PATH}:1: docs_token_sync must be a mapping"]
    rules = token_sync.get("rules")
    if not isinstance(rules, list):
        return [f"{_NORMALIZATION_PROFILE_PATH}:1: docs_token_sync.rules must be a list"]
    violations: list[str] = []
    for rule in rules:
        if not isinstance(rule, dict):
            continue
        rid = str(rule.get("id", "NORMALIZATION_DOC_TOKEN_SYNC")).strip() or "NORMALIZATION_DOC_TOKEN_SYNC"
        rel = str(rule.get("file", "")).strip()
        if not rel:
            continue
        p = _join_contract_path(root, rel)
        if not p.exists():
            violations.append(f"{rel}:1: {rid}: missing file")
            continue
        text = p.read_text(encoding="utf-8")
        must = rule.get("must_contain", [])
        must_not = rule.get("must_not_contain", [])
        if isinstance(must, list):
            for tok in must:
                if isinstance(tok, str) and tok and tok not in text:
                    violations.append(f"{rel}:1: {rid}: missing token: {tok}")
        if isinstance(must_not, list):
            for tok in must_not:
                if isinstance(tok, str) and tok and tok in text:
                    line = text[: text.find(tok)].count("\n") + 1
                    violations.append(f"{rel}:{line}: {rid}: forbidden token present: {tok}")
    return violations


def _scan_normalization_spec_style_sync(root: Path, *, harness: dict | None = None) -> list[str]:
    profile, errs = _load_normalization_profile(root)
    if errs:
        return errs
    assert profile is not None
    style = profile.get("spec_style")
    if not isinstance(style, dict):
        return [f"{_NORMALIZATION_PROFILE_PATH}:1: spec_style must be a mapping"]
    max_lines = style.get("conformance_max_block_lines")
    if not isinstance(max_lines, int) or max_lines < 1:
        return [f"{_NORMALIZATION_PROFILE_PATH}:1: spec_style.conformance_max_block_lines must be a positive int"]

    violations: list[str] = []
    if _CONFORMANCE_MAX_BLOCK_LINES != max_lines:
        violations.append(
            "scripts/run_governance_specs.py:1: NORMALIZATION_SPEC_STYLE_SYNC: "
            f"_CONFORMANCE_MAX_BLOCK_LINES={_CONFORMANCE_MAX_BLOCK_LINES} must match profile value {max_lines}"
        )

    style_doc = root / "docs/spec/conformance/style.md"
    if not style_doc.exists():
        violations.append("docs/spec/conformance/style.md:1: NORMALIZATION_SPEC_STYLE_SYNC: missing style doc")
        return violations
    raw = style_doc.read_text(encoding="utf-8")
    expected_token = f"({max_lines} lines max)"
    if expected_token not in raw:
        violations.append(
            f"docs/spec/conformance/style.md:1: NORMALIZATION_SPEC_STYLE_SYNC: missing block-size token {expected_token}"
        )
    if "flow-sequence" in raw:
        line = raw[: raw.find("flow-sequence")].count("\n") + 1
        violations.append(
            f"docs/spec/conformance/style.md:{line}: NORMALIZATION_SPEC_STYLE_SYNC: forbidden legacy token flow-sequence"
        )
    return violations


GovernanceCheckOutcome = list[str] | dict[str, object]
GovernanceCheck = Callable[..., GovernanceCheckOutcome]


def _policy_outcome(
    *,
    subject: object,
    policy_evaluate: list[object] | None = None,
    policy_path: str = "harness.policy_evaluate",
    symbols: dict[str, object] | None = None,
    violations: list[str] | None = None,
) -> dict[str, object]:
    return {
        "subject": subject,
        "policy_evaluate": policy_evaluate,
        "policy_path": policy_path,
        "symbols": symbols or {},
        "violations": list(violations or []),
    }

_CHECKS: dict[str, GovernanceCheck] = {
    "contract.governance_check": _scan_contract_governance_check,
    "pending.no_resolved_markers": _scan_pending_no_resolved_markers,
    "docs.security_warning_contract": _scan_security_warning_docs,
    "docs.v1_scope_contract": _scan_v1_scope_doc,
    "runtime.config_literals": _scan_runtime_config_literals,
    "runtime.settings_import_policy": _scan_runtime_settings_import_policy,
    "runtime.python_bin_resolver_sync": _scan_runtime_python_bin_resolver_sync,
    "runtime.runner_interface_gate_sync": _scan_runtime_runner_interface_gate_sync,
    "runtime.public_runner_entrypoint_single": _scan_runtime_public_runner_entrypoint_single,
    "runtime.public_runner_default_rust": _scan_runtime_public_runner_default_rust,
    "runtime.python_lane_explicit_opt_in": _scan_runtime_python_lane_explicit_opt_in,
    "runtime.no_public_direct_rust_adapter_docs": _scan_runtime_no_public_direct_rust_adapter_docs,
    "runtime.runner_interface_subcommands": _scan_runtime_runner_interface_subcommands,
    "runtime.runner_interface_ci_lane": _scan_runtime_runner_interface_ci_lane,
    "runtime.rust_adapter_no_delegate": _scan_runtime_rust_adapter_no_delegate,
    "runtime.rust_adapter_exec_smoke": _scan_runtime_rust_adapter_exec_smoke,
    "runtime.rust_adapter_subcommand_parity": _scan_runtime_rust_adapter_subcommand_parity,
    "runtime.assertions_via_spec_lang": _scan_runtime_assertions_via_spec_lang,
    "runtime.spec_lang_pure_no_effect_builtins": _scan_spec_lang_pure_no_effect_builtins,
    "runtime.orchestration_policy_via_spec_lang": _scan_runtime_orchestration_policy_via_spec_lang,
    "conformance.case_index_sync": _scan_conformance_case_index_sync,
    "conformance.purpose_warning_codes_sync": _scan_conformance_purpose_warning_codes_sync,
    "conformance.purpose_quality_gate": _scan_conformance_purpose_quality_gate,
    "contract.coverage_threshold": _scan_contract_coverage_threshold,
    "spec.portability_metric": _scan_spec_portability_metric,
    "spec.portability_non_regression": _scan_spec_portability_non_regression,
    "spec.spec_lang_adoption_metric": _scan_spec_lang_adoption_metric,
    "spec.spec_lang_adoption_non_regression": _scan_spec_lang_adoption_non_regression,
    "governance.policy_library_usage_non_regression": _scan_policy_library_usage_non_regression,
    "runtime.runner_independence_metric": _scan_runner_independence_metric,
    "runtime.runner_independence_non_regression": _scan_runner_independence_non_regression,
    "runtime.python_dependency_metric": _scan_python_dependency_metric,
    "runtime.python_dependency_non_regression": _scan_python_dependency_non_regression,
    "runtime.non_python_lane_no_python_exec": _scan_runtime_non_python_lane_no_python_exec,
    "runtime.rust_adapter_transitive_no_python": _scan_runtime_rust_adapter_transitive_no_python,
    "docs.operability_metric": _scan_docs_operability_metric,
    "docs.operability_non_regression": _scan_docs_operability_non_regression,
    "spec.contract_assertions_metric": _scan_contract_assertions_metric,
    "spec.contract_assertions_non_regression": _scan_contract_assertions_non_regression,
    "objective.scorecard_metric": _scan_objective_scorecard_metric,
    "objective.scorecard_non_regression": _scan_objective_scorecard_non_regression,
    "objective.tripwires_clean": _scan_objective_tripwires_clean,
    "conformance.case_doc_style_guard": _scan_conformance_case_doc_style_guard,
    "docs.regex_doc_sync": _scan_regex_doc_sync,
    "assert.universal_core_sync": _scan_assert_universal_core_sync,
    "assert.sugar_compile_only_sync": _scan_assert_sugar_compile_only_sync,
    "assert.type_contract_subject_semantics_sync": _scan_assert_type_contract_subject_semantics_sync,
    "assert.compiler_schema_matrix_sync": _scan_assert_compiler_schema_matrix_sync,
    "assert.spec_lang_builtin_surface_sync": _scan_assert_spec_lang_builtin_surface_sync,
    "assert.subject_profiles_declared": _scan_assert_subject_profiles_declared,
    "assert.subject_profiles_json_only": _scan_assert_subject_profiles_json_only,
    "assert.domain_profiles_docs_sync": _scan_assert_domain_profiles_docs_sync,
    "assert.domain_library_usage_required": _scan_assert_domain_library_usage_required,
    "assert.adapter_projection_contract_sync": _scan_assert_adapter_projection_contract_sync,
    "spec_lang.stdlib_profile_complete": _scan_spec_lang_stdlib_profile_complete,
    "spec_lang.stdlib_py_php_parity": _scan_spec_lang_stdlib_py_php_parity,
    "spec_lang.stdlib_docs_sync": _scan_spec_lang_stdlib_docs_sync,
    "spec_lang.stdlib_conformance_coverage": _scan_spec_lang_stdlib_conformance_coverage,
    "docs.current_spec_only_contract": _scan_current_spec_only_contract,
    "docs.current_spec_policy_key_names": _scan_current_spec_policy_key_names,
    "governance.policy_evaluate_required": _scan_governance_policy_evaluate_required,
    "governance.policy_library_usage_required": _scan_governance_policy_library_usage_required,
    "conformance.library_policy_usage_required": _scan_conformance_library_policy_usage_required,
    "governance.extractor_only_no_verdict_branching": _scan_governance_extractor_only_no_verdict_branching,
    "governance.structured_assertions_required": _scan_governance_structured_assertions_required,
    "runtime.rust_adapter_no_python_exec": _scan_runtime_rust_adapter_no_python_exec,
    "conformance.type_contract_docs": _scan_conformance_type_contract_docs,
    "conformance.api_http_portable_shape": _scan_conformance_api_http_portable_shape,
    "conformance.no_runner_logic_outside_harness": _scan_conformance_no_runner_logic_outside_harness,
    "conformance.portable_determinism_guard": _scan_conformance_portable_determinism_guard,
    "conformance.no_ambient_assumptions": _scan_conformance_no_ambient_assumptions,
    "conformance.extension_requires_capabilities": _scan_conformance_extension_requires_capabilities,
    "conformance.type_contract_field_sync": _scan_conformance_type_contract_field_sync,
    "conformance.spec_lang_preferred": _scan_conformance_spec_lang_preferred,
    "conformance.spec_lang_fixture_library_usage": _scan_conformance_spec_lang_fixture_library_usage,
    "conformance.library_contract_cases_present": _scan_conformance_library_contract_cases_present,
    "conformance.evaluate_first_ratio_non_regression": _scan_conformance_evaluate_first_ratio_non_regression,
    "docs.reference_surface_complete": _scan_docs_reference_surface_complete,
    "docs.reference_index_sync": _scan_docs_reference_index_sync,
    "docs.meta_schema_valid": _scan_docs_meta_schema_valid,
    "docs.reference_manifest_sync": _scan_docs_reference_manifest_sync,
    "docs.token_ownership_unique": _scan_docs_token_ownership_unique,
    "docs.token_dependency_resolved": _scan_docs_token_dependency_resolved,
    "docs.instructions_complete": _scan_docs_instructions_complete,
    "docs.command_examples_verified": _scan_docs_command_examples_verified,
    "docs.example_id_uniqueness": _scan_docs_example_id_uniqueness,
    "docs.generated_files_clean": _scan_docs_generated_files_clean,
    "docs.required_sections": _scan_docs_required_sections,
    "docs.examples_runnable": _scan_docs_examples_runnable,
    "docs.cli_flags_documented": _scan_docs_cli_flags_documented,
    "docs.contract_schema_book_sync": _scan_docs_contract_schema_book_sync,
    "docs.make_commands_sync": _scan_docs_make_commands_sync,
    "docs.adoption_profiles_sync": _scan_docs_adoption_profiles_sync,
    "docs.release_contract_automation_policy": _scan_docs_release_contract_automation_policy,
    "runtime.scope_sync": _scan_runtime_scope_sync,
    "naming.filename_policy": _scan_naming_filename_policy,
    "normalization.virtual_root_paths_only": _scan_normalization_virtual_root_paths_only,
    "reference.contract_paths_exist": _scan_reference_contract_paths_exist,
    "reference.symbols_exist": _scan_reference_symbols_exist,
    "reference.policy_symbols_resolve": _scan_reference_policy_symbols_resolve,
    "reference.library_exports_used": _scan_reference_library_exports_used,
    "reference.private_symbols_forbidden": _scan_reference_private_symbols_forbidden,
    "reference.check_ids_exist": _scan_reference_check_ids_exist,
    "reference.external_refs_policy": _scan_reference_external_refs_policy,
    "reference.token_anchors_exist": _scan_reference_token_anchors_exist,
    "spec.layout_domain_trees": _scan_spec_layout_domain_trees,
    "spec.domain_index_sync": _scan_spec_domain_index_sync,
    "library.domain_ownership": _scan_library_domain_ownership,
    "library.domain_index_sync": _scan_library_domain_index_sync,
    "library.public_surface_model": _scan_library_public_surface_model,
    "normalization.profile_sync": _scan_normalization_profile_sync,
    "normalization.mapping_ast_only": _scan_normalization_mapping_ast_only,
    "normalization.library_mapping_ast_only": _scan_normalization_library_mapping_ast_only,
    "normalization.docs_token_sync": _scan_normalization_docs_token_sync,
    "normalization.spec_style_sync": _scan_normalization_spec_style_sync,
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
        raw_outcome = fn(root, harness=h)
    else:
        raw_outcome = fn(root)

    subject: object = {}
    symbols: dict[str, object] = {}
    policy_evaluate: list[object] | None = None
    policy_path = "harness.policy_evaluate"
    if isinstance(raw_outcome, dict):
        subject = raw_outcome.get("subject")
        symbols_raw = raw_outcome.get("symbols")
        symbols = symbols_raw if isinstance(symbols_raw, dict) else {}
        policy_raw = raw_outcome.get("policy_evaluate")
        policy_evaluate = policy_raw if isinstance(policy_raw, list) else None
        policy_path = str(raw_outcome.get("policy_path", policy_path))
        violations_raw = raw_outcome.get("violations")
        if isinstance(violations_raw, list):
            violations = [str(v) for v in violations_raw if str(v).strip()]
        else:
            violations = []
    else:
        violations = [str(v) for v in raw_outcome if str(v).strip()]
        subject = {"violations": violations}

    if isinstance(subject, dict) and "violations" not in subject:
        subject = {**subject, "violations": list(violations)}
    if policy_evaluate is None:
        raw_case_policy = h.get("policy_evaluate")
        if raw_case_policy is not None:
            policy_evaluate = normalize_policy_evaluate(raw_case_policy, field="harness.policy_evaluate")
            policy_path = "harness.policy_evaluate"
    if policy_evaluate is None:
        case_id = str(t.get("id", "<unknown>")).strip() or "<unknown>"
        raise ValueError(
            f"governance.check {check_id} case {case_id} requires harness.policy_evaluate"
        )

    # Governance policies can import reusable spec-lang function libraries
    # via harness.spec_lang.library_paths/exports.
    lib_symbols = load_spec_lang_symbols_for_case(
        doc_path=case.doc_path,
        harness=h,
        limits=SpecLangLimits(),
    )
    if lib_symbols:
        symbols = {**lib_symbols, **symbols}

    policy_result: GovernancePolicyResult = run_governance_policy(
        check_id=check_id,
        case_id=str(t.get("id", "<unknown>")).strip() or "<unknown>",
        policy_evaluate=policy_evaluate,
        subject=subject,
        symbols=symbols,
        policy_path=policy_path,
    )
    if policy_result.passed:
        violations = []
    elif violations:
        violations = policy_result.diagnostics + violations
    else:
        violations = policy_result.diagnostics

    case_id = str(t.get("id", "<unknown>")).strip() or "<unknown>"
    summary = {
        "passed": not violations,
        "check_id": check_id,
        "case_id": case_id,
        "violation_count": len(violations),
    }
    text = (
        f"PASS: {check_id}"
        if not violations
        else f"FAIL: {check_id}\n" + "\n".join(violations)
    )

    assert_spec = t.get("assert", []) or []
    spec_lang_limits = SpecLangLimits()

    def _eval_leaf(leaf: dict, *, inherited_target: str | None = None, assert_path: str = "assert") -> None:
        for target, op, value, is_true in iter_leaf_assertions(leaf, target_override=inherited_target):
            if target == "text":
                subject_value = text
            elif target == "summary_json":
                subject_value = summary
            elif target == "violation_count":
                subject_value = len(violations)
            else:
                raise ValueError(f"unknown assert target for governance.check: {target}")
            if op != "evaluate":
                raise ValueError(f"unsupported governance assertion op: {op}")
            if isinstance(value, list):
                raw_expr_list = value
            elif isinstance(value, dict):
                raw_expr_list = [value]
            else:
                raise TypeError("evaluate assertion op value must be a list or mapping AST expression")
            expr = normalize_policy_evaluate(raw_expr_list, field=f"{assert_path}.{target}.evaluate")
            ok = eval_predicate(expr, subject=subject_value, limits=spec_lang_limits)
            if bool(ok) is not bool(is_true):
                raise AssertionError(f"{op} assertion failed")

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
            if str(case.test.get("type", "")).strip() != "governance.check":
                continue
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

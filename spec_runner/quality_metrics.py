from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from spec_runner.codecs import load_external_cases
from spec_runner.contract_governance import contract_coverage_jsonable
from spec_runner.dispatcher import iter_cases
from spec_runner.docs_quality import (
    check_command_examples_verified,
    check_instructions_complete,
    check_token_dependency_resolved,
    check_token_ownership_unique,
    load_docs_meta_for_paths,
    load_reference_manifest,
    manifest_chapter_paths,
)
from spec_runner.settings import SETTINGS


def _as_list_of_strings(value: object) -> list[str]:
    if not isinstance(value, list):
        return []
    out: list[str] = []
    for item in value:
        if isinstance(item, str):
            s = item.strip()
            if s:
                out.append(s)
    return out


def _match_segment(rel_path: str, segment_rules: list[dict[str, str]]) -> str:
    normalized = rel_path.replace("\\", "/")
    for rule in segment_rules:
        prefix = str(rule["prefix"]).replace("\\", "/").rstrip("/")
        if normalized == prefix or normalized.startswith(prefix + "/"):
            return str(rule["segment"])
    return "other"


def _safe_ratio(num: float, den: float, *, default: float = 0.0) -> float:
    if den <= 0:
        return default
    return num / den


def _summarize_segment(rows: list[dict[str, Any]], fields: list[str]) -> dict[str, Any]:
    count = len(rows)
    out: dict[str, Any] = {"case_count": count}
    for field in fields:
        if count == 0:
            out[f"mean_{field}"] = 0.0
        else:
            out[f"mean_{field}"] = sum(float(r.get(field, 0.0)) for r in rows) / count
    return out


def _compile_direction_map(value: object, *, default_direction: str = "non_decrease") -> dict[str, str]:
    out: dict[str, str] = {}
    if isinstance(value, list):
        for item in value:
            if isinstance(item, str) and item.strip():
                out[item.strip()] = default_direction
        return out
    if isinstance(value, dict):
        for k, v in value.items():
            key = str(k).strip()
            if not key:
                continue
            direction = str(v).strip() if isinstance(v, str) else default_direction
            if direction not in {"non_decrease", "non_increase"}:
                direction = default_direction
            out[key] = direction
    return out


def compare_metric_non_regression(
    *,
    current: dict[str, Any],
    baseline: dict[str, Any],
    summary_fields: object,
    segment_fields: object,
    epsilon: float,
) -> list[str]:
    violations: list[str] = []
    summary_map = _compile_direction_map(summary_fields)
    if not summary_map:
        return ["non-regression config summary_fields must declare at least one field"]

    seg_map_in = segment_fields if isinstance(segment_fields, dict) else {}
    compiled_seg_map: dict[str, dict[str, str]] = {}
    for segment, fields in seg_map_in.items():
        seg = str(segment).strip()
        if not seg:
            continue
        compiled = _compile_direction_map(fields)
        if not compiled:
            violations.append(f"segment_fields.{seg} must declare at least one field")
            continue
        compiled_seg_map[seg] = compiled

    def _resolve(payload: object, dotted: str) -> float | None:
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

    for field, direction in summary_map.items():
        cur = _resolve(current, f"summary.{field}")
        base = _resolve(baseline, f"summary.{field}")
        if cur is None:
            violations.append(f"summary.{field}: missing numeric current metric")
            continue
        if base is None:
            violations.append(f"baseline summary.{field}: missing numeric baseline metric")
            continue
        if direction == "non_decrease" and cur + epsilon < base:
            violations.append(f"summary.{field}: regressed from baseline {base:.12g} to {cur:.12g}")
        if direction == "non_increase" and cur - epsilon > base:
            violations.append(f"summary.{field}: increased from baseline {base:.12g} to {cur:.12g}")

    for segment, fields in compiled_seg_map.items():
        for field, direction in fields.items():
            cur = _resolve(current, f"segments.{segment}.{field}")
            base = _resolve(baseline, f"segments.{segment}.{field}")
            if cur is None:
                violations.append(f"segments.{segment}.{field}: missing numeric current metric")
                continue
            if base is None:
                violations.append(f"baseline segments.{segment}.{field}: missing numeric baseline metric")
                continue
            if direction == "non_decrease" and cur + epsilon < base:
                violations.append(
                    f"segments.{segment}.{field}: regressed from baseline {base:.12g} to {cur:.12g}"
                )
            if direction == "non_increase" and cur - epsilon > base:
                violations.append(
                    f"segments.{segment}.{field}: increased from baseline {base:.12g} to {cur:.12g}"
                )

    return violations


def _load_baseline_json(repo_root: Path, baseline_path: str) -> tuple[dict[str, Any] | None, list[str]]:
    path = repo_root / baseline_path
    if not path.exists():
        return None, [f"{baseline_path}:1: missing baseline metrics file"]
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return None, [f"{baseline_path}:1: invalid JSON baseline: {exc.msg} at line {exc.lineno} column {exc.colno}"]
    if not isinstance(payload, dict):
        return None, [f"{baseline_path}:1: baseline payload must be a JSON object"]
    return payload, []


def default_spec_lang_adoption_config() -> dict[str, Any]:
    cfg = SETTINGS.spec_portability
    return {
        "roots": list(cfg.roots),
        "segment_rules": [{"prefix": r.prefix, "segment": r.segment} for r in cfg.segment_rules],
        "recursive": bool(cfg.recursive),
        "tests_glob": "tests/test_*_unit.py",
        "native_escape_test_tokens": ["not yet representable", "DSL", "spec model"],
    }


def _collect_leaf_ops(node: object, *, inherited_target: str | None = None) -> list[str]:
    ops: list[str] = []
    if isinstance(node, list):
        for child in node:
            ops.extend(_collect_leaf_ops(child, inherited_target=inherited_target))
        return ops
    if not isinstance(node, dict):
        return ops
    present_groups = [k for k in ("must", "can", "cannot") if k in node]
    if present_groups:
        node_target = str(node.get("target", "")).strip() or inherited_target
        for key in present_groups:
            children = node.get(key, [])
            if isinstance(children, list):
                for child in children:
                    ops.extend(_collect_leaf_ops(child, inherited_target=node_target))
        return ops
    known_ops = {"contain", "regex", "json_type", "exists", "evaluate"}
    for key, value in node.items():
        if key in {"target", "must", "can", "cannot"}:
            continue
        if key in known_ops and isinstance(value, list):
            ops.extend([key] * len(value))
    return ops


def _contains_key_recursive(payload: object, key: str) -> bool:
    if isinstance(payload, dict):
        if key in payload:
            return True
        return any(_contains_key_recursive(v, key) for v in payload.values())
    if isinstance(payload, list):
        return any(_contains_key_recursive(v, key) for v in payload)
    return False


def spec_lang_adoption_report_jsonable(repo_root: Path, config: dict[str, Any] | None = None) -> dict[str, Any]:
    root = repo_root.resolve()
    cfg = default_spec_lang_adoption_config()
    if isinstance(config, dict):
        cfg.update(config)

    roots = _as_list_of_strings(cfg.get("roots"))
    raw_rules = cfg.get("segment_rules") if isinstance(cfg.get("segment_rules"), list) else []
    rules: list[dict[str, str]] = []
    for item in raw_rules:
        if isinstance(item, dict):
            prefix = str(item.get("prefix", "")).strip()
            seg = str(item.get("segment", "")).strip()
            if prefix and seg:
                rules.append({"prefix": prefix, "segment": seg})

    recursive = bool(cfg.get("recursive", True))
    rows: list[dict[str, Any]] = []
    errs: list[str] = []

    for rel_root in roots:
        base = root / rel_root
        if not base.exists() or not base.is_dir():
            errs.append(f"{rel_root}: missing spec root directory")
            continue

        if recursive:
            files = sorted(base.rglob(SETTINGS.case.default_file_pattern))
            case_pairs: list[tuple[Path, dict[str, Any]]] = []
            for file_path in files:
                if not file_path.is_file():
                    continue
                for doc_path, case in load_external_cases(file_path, formats={"md"}):
                    case_pairs.append((doc_path, case))
        else:
            case_pairs = [(spec.doc_path, spec.test) for spec in iter_cases(base, file_pattern=SETTINGS.case.default_file_pattern)]

        for doc_path, case in case_pairs:
            case_id = str(case.get("id", "<unknown>")).strip() or "<unknown>"
            case_type = str(case.get("type", "")).strip()
            try:
                rel_path = str(doc_path.resolve().relative_to(root)).replace("\\", "/")
            except ValueError:
                rel_path = str(doc_path)
            segment = _match_segment(rel_path, rules)
            ops = _collect_leaf_ops(case.get("assert", []) or [])
            total_leaf = len(ops)
            eval_leaf = sum(1 for op in ops if op == "evaluate")
            logic_ratio = 1.0 if total_leaf == 0 else _safe_ratio(eval_leaf, total_leaf, default=1.0)
            native_hint = False
            if case_type == "governance.check":
                native_hint = not _contains_key_recursive(case.get("harness"), "policy_evaluate")
            rows.append(
                {
                    "id": case_id,
                    "type": case_type,
                    "file": rel_path,
                    "segment": segment,
                    "logic_self_contained_ratio": logic_ratio,
                    "native_logic_escape_hint": 1.0 if native_hint else 0.0,
                }
            )

    tests_glob = str(cfg.get("tests_glob", "tests/test_*_unit.py")).strip() or "tests/test_*_unit.py"
    escape_tokens = [t.lower() for t in _as_list_of_strings(cfg.get("native_escape_test_tokens"))]
    unit_opt_out_count = 0
    for p in sorted(root.glob(tests_glob)):
        text = p.read_text(encoding="utf-8")
        if "# SPEC-OPT-OUT:" not in text:
            continue
        lower = text.lower()
        if not escape_tokens or any(tok in lower for tok in escape_tokens):
            unit_opt_out_count += 1

    rows.sort(key=lambda r: (str(r["segment"]), str(r["file"]), str(r["id"])))
    segments_order = [str(r["segment"]) for r in rules] + ["other"]
    seen: list[str] = []
    for seg in segments_order + [str(r["segment"]) for r in rows]:
        if seg not in seen:
            seen.append(seg)

    segments: dict[str, Any] = {}
    for seg in seen:
        seg_rows = [r for r in rows if str(r["segment"]) == seg]
        summary = _summarize_segment(seg_rows, ["logic_self_contained_ratio", "native_logic_escape_hint"])
        summary["native_logic_escape_case_ratio"] = summary.pop("mean_native_logic_escape_hint")
        segments[seg] = summary

    total = len(rows)
    overall_logic = _safe_ratio(sum(float(r["logic_self_contained_ratio"]) for r in rows), float(total), default=0.0)
    native_ratio = _safe_ratio(sum(float(r["native_logic_escape_hint"]) for r in rows), float(total), default=0.0)

    return {
        "version": 1,
        "summary": {
            "total_cases": total,
            "overall_logic_self_contained_ratio": overall_logic,
            "native_logic_escape_case_ratio": native_ratio,
            "unit_opt_out_count": unit_opt_out_count,
        },
        "segments": segments,
        "cases": rows,
        "config": cfg,
        "errors": errs,
    }


def default_runner_independence_config() -> dict[str, Any]:
    return {
        "segment_files": {
            "gate_scripts": ["scripts/*.sh"],
            "ci_workflows": [".github/workflows/*.yml", ".github/workflows/*.yaml"],
            "adapter_interfaces": [
                "scripts/runner_adapter.sh",
                "scripts/rust/runner_adapter.sh",
                "scripts/rust/spec_runner_cli/src/main.rs",
            ],
        },
        "direct_runtime_tokens": [
            "scripts/run_governance_specs.py",
            "scripts/evaluate_style.py --check docs/spec",
            "scripts/spec_portability_report.py",
            "python -m pytest",
            "php scripts/php/spec_runner.php",
        ],
        "gate_required_tokens": ["SPEC_RUNNER_BIN", "scripts/runner_adapter.sh"],
        "rust_ci_required_tokens": [
            "core-gate-rust-adapter:",
            "SPEC_RUNNER_BIN: ./scripts/rust/runner_adapter.sh",
            "run: ./scripts/core_gate.sh",
        ],
    }


def runner_independence_report_jsonable(repo_root: Path, config: dict[str, Any] | None = None) -> dict[str, Any]:
    root = repo_root.resolve()
    cfg = default_runner_independence_config()
    if isinstance(config, dict):
        cfg.update(config)

    segment_files = cfg.get("segment_files") if isinstance(cfg.get("segment_files"), dict) else {}
    direct_tokens = _as_list_of_strings(cfg.get("direct_runtime_tokens"))
    gate_required = _as_list_of_strings(cfg.get("gate_required_tokens"))
    rust_required = _as_list_of_strings(cfg.get("rust_ci_required_tokens"))

    rows: list[dict[str, Any]] = []
    errors: list[str] = []

    for segment, patterns in segment_files.items():
        seg = str(segment).strip()
        if not seg:
            continue
        if not isinstance(patterns, list):
            errors.append(f"segment_files.{seg} must be a list")
            continue
        files: set[Path] = set()
        for pat in patterns:
            if not isinstance(pat, str) or not pat.strip():
                continue
            for p in root.glob(pat.strip()):
                if p.is_file():
                    files.add(p)
        for path in sorted(files):
            rel = str(path.resolve().relative_to(root)).replace("\\", "/")
            text = path.read_text(encoding="utf-8")
            direct_hits = sum(text.count(tok) for tok in direct_tokens)

            if seg == "gate_scripts":
                iface_ratio = _safe_ratio(
                    float(sum(1 for tok in gate_required if tok in text)),
                    float(max(1, len(gate_required))),
                    default=1.0,
                )
                rust_ratio = 1.0
            elif seg == "ci_workflows":
                iface_ratio = 1.0 if "SPEC_RUNNER_BIN" in text else 0.0
                rust_ratio = _safe_ratio(
                    float(sum(1 for tok in rust_required if tok in text)),
                    float(max(1, len(rust_required))),
                    default=1.0,
                )
            else:
                iface_ratio = 1.0
                rust_ratio = 1.0

            no_direct = 1.0 if direct_hits == 0 else 0.0
            score = (no_direct + iface_ratio + rust_ratio) / 3.0
            rows.append(
                {
                    "file": rel,
                    "segment": seg,
                    "direct_runtime_invocation_count": float(direct_hits),
                    "runner_interface_usage_ratio": iface_ratio,
                    "rust_primary_path_coverage_ratio": rust_ratio,
                    "runner_independence_ratio": score,
                }
            )

    rows.sort(key=lambda r: (str(r["segment"]), str(r["file"])))
    segments: dict[str, Any] = {}
    segment_order = [str(k).strip() for k in segment_files.keys() if str(k).strip()]
    seen = []
    for seg in segment_order + [str(r["segment"]) for r in rows]:
        if seg not in seen:
            seen.append(seg)

    for seg in seen:
        seg_rows = [r for r in rows if str(r["segment"]) == seg]
        summary = _summarize_segment(
            seg_rows,
            [
                "runner_independence_ratio",
                "runner_interface_usage_ratio",
                "rust_primary_path_coverage_ratio",
                "direct_runtime_invocation_count",
            ],
        )
        summary["direct_runtime_invocation_count"] = sum(
            int(r.get("direct_runtime_invocation_count", 0)) for r in seg_rows
        )
        segments[seg] = summary

    total = len(rows)
    overall_ratio = _safe_ratio(sum(float(r["runner_independence_ratio"]) for r in rows), float(total), default=0.0)
    direct_total = sum(int(r.get("direct_runtime_invocation_count", 0)) for r in rows)

    return {
        "version": 1,
        "summary": {
            "total_files": total,
            "overall_runner_independence_ratio": overall_ratio,
            "direct_runtime_invocation_count": direct_total,
        },
        "segments": segments,
        "files": rows,
        "config": cfg,
        "errors": errors,
    }


def default_docs_operability_config() -> dict[str, Any]:
    return {
        "reference_manifest": "docs/book/reference_manifest.yaml",
        "segment_rules": [
            {"prefix": "docs/book", "segment": "book"},
            {"prefix": "docs/spec/contract", "segment": "contract"},
            {"prefix": "docs/spec/schema", "segment": "schema"},
            {"prefix": "docs/spec/impl", "segment": "impl_docs"},
        ],
    }


def docs_operability_report_jsonable(repo_root: Path, config: dict[str, Any] | None = None) -> dict[str, Any]:
    root = repo_root.resolve()
    cfg = default_docs_operability_config()
    if isinstance(config, dict):
        cfg.update(config)

    manifest_rel = str(cfg.get("reference_manifest", "")).strip() or "docs/book/reference_manifest.yaml"
    manifest, manifest_errs = load_reference_manifest(root, manifest_rel)
    rel_paths = manifest_chapter_paths(manifest)
    metas, meta_issues, _meta_lines = load_docs_meta_for_paths(root, rel_paths)

    for rel in rel_paths:
        if rel in metas:
            metas[rel]["__text__"] = (root / rel).read_text(encoding="utf-8")

    token_owner_issues = check_token_ownership_unique(metas)
    token_dep_issues = check_token_dependency_resolved(metas)
    section_issues = check_instructions_complete(root, metas)
    example_issues = check_command_examples_verified(root, rel_paths)

    issue_paths = {
        "token": {i.path for i in [*token_owner_issues, *token_dep_issues]},
        "sections": {i.path for i in section_issues},
        "examples": {i.path for i in example_issues},
    }

    rules = cfg.get("segment_rules") if isinstance(cfg.get("segment_rules"), list) else []
    segment_rules: list[dict[str, str]] = []
    for item in rules:
        if isinstance(item, dict):
            prefix = str(item.get("prefix", "")).strip()
            seg = str(item.get("segment", "")).strip()
            if prefix and seg:
                segment_rules.append({"prefix": prefix, "segment": seg})

    rows: list[dict[str, Any]] = []
    for rel in rel_paths:
        meta = metas.get(rel, {})
        segment = _match_segment(rel, segment_rules)
        examples = meta.get("examples", []) if isinstance(meta, dict) else []
        if not isinstance(examples, list):
            examples = []
        total_examples = 0
        runnable = 0
        opted_out = 0
        for ex in examples:
            if not isinstance(ex, dict):
                continue
            total_examples += 1
            if ex.get("runnable") is True:
                runnable += 1
            elif ex.get("runnable") is False:
                opted_out += 1

        runnable_ratio = _safe_ratio(float(runnable), float(total_examples), default=1.0)
        opt_out_density = _safe_ratio(float(opted_out), float(total_examples), default=0.0)
        command_ratio = 0.0 if rel in issue_paths["examples"] else 1.0
        section_ratio = 0.0 if rel in issue_paths["sections"] else 1.0
        token_ratio = 0.0 if rel in issue_paths["token"] else 1.0
        operability_ratio = (runnable_ratio + command_ratio + section_ratio + token_ratio) / 4.0

        rows.append(
            {
                "path": rel,
                "segment": segment,
                "runnable_example_coverage_ratio": runnable_ratio,
                "command_doc_validation_ratio": command_ratio,
                "required_sections_compliance_ratio": section_ratio,
                "token_sync_compliance_ratio": token_ratio,
                "opt_out_density_ratio": opt_out_density,
                "docs_operability_ratio": operability_ratio,
            }
        )

    rows.sort(key=lambda r: (str(r["segment"]), str(r["path"])))

    segments: dict[str, Any] = {}
    order = [str(rule["segment"]) for rule in segment_rules] + ["other"]
    seen: list[str] = []
    for seg in order + [str(r["segment"]) for r in rows]:
        if seg not in seen:
            seen.append(seg)

    for seg in seen:
        seg_rows = [r for r in rows if str(r["segment"]) == seg]
        segments[seg] = _summarize_segment(
            seg_rows,
            [
                "docs_operability_ratio",
                "runnable_example_coverage_ratio",
                "command_doc_validation_ratio",
                "required_sections_compliance_ratio",
                "token_sync_compliance_ratio",
                "opt_out_density_ratio",
            ],
        )

    total = len(rows)
    overall_ratio = _safe_ratio(sum(float(r["docs_operability_ratio"]) for r in rows), float(total), default=0.0)

    errors = [i.render() for i in [*manifest_errs, *meta_issues, *token_owner_issues, *token_dep_issues, *section_issues, *example_issues]]

    return {
        "version": 1,
        "summary": {
            "total_docs": total,
            "overall_docs_operability_ratio": overall_ratio,
        },
        "segments": segments,
        "docs": rows,
        "config": cfg,
        "errors": errors,
    }


def default_contract_assertions_config() -> dict[str, Any]:
    return {
        "paths": [
            "docs/spec/contract/03_assertions.md",
            "docs/spec/schema/schema_v1.md",
            "docs/book/03_assertions.md",
            "docs/spec/contract/03b_spec_lang_v1.md",
        ],
        "segment_rules": [
            {"prefix": "docs/spec/contract", "segment": "contract"},
            {"prefix": "docs/spec/schema", "segment": "schema"},
            {"prefix": "docs/book", "segment": "book"},
        ],
        "required_tokens": ["must", "can", "cannot", "contain", "regex", "evaluate"],
    }


def contract_assertions_report_jsonable(repo_root: Path, config: dict[str, Any] | None = None) -> dict[str, Any]:
    root = repo_root.resolve()
    cfg = default_contract_assertions_config()
    if isinstance(config, dict):
        cfg.update(config)

    paths = _as_list_of_strings(cfg.get("paths"))
    required_tokens = _as_list_of_strings(cfg.get("required_tokens"))
    raw_rules = cfg.get("segment_rules") if isinstance(cfg.get("segment_rules"), list) else []
    rules: list[dict[str, str]] = []
    for item in raw_rules:
        if isinstance(item, dict):
            prefix = str(item.get("prefix", "")).strip()
            seg = str(item.get("segment", "")).strip()
            if prefix and seg:
                rules.append({"prefix": prefix, "segment": seg})

    errors: list[str] = []
    rows: list[dict[str, Any]] = []
    token_presence_map: dict[str, set[str]] = {}

    for rel in paths:
        p = root / rel
        if not p.exists():
            errors.append(f"{rel}:1: missing contract assertion doc")
            continue
        text = p.read_text(encoding="utf-8").lower()
        segment = _match_segment(rel, rules)
        present = {tok for tok in required_tokens if tok.lower() in text}
        token_presence_map[rel] = present
        ratio = _safe_ratio(float(len(present)), float(max(1, len(required_tokens))), default=0.0)
        rows.append(
            {
                "path": rel,
                "segment": segment,
                "required_token_coverage_ratio": ratio,
                "missing_required_token_count": float(max(0, len(required_tokens) - len(present))),
            }
        )

    rows.sort(key=lambda r: (str(r["segment"]), str(r["path"])))

    union_tokens: set[str] = set()
    intersection_tokens: set[str] | None = None
    for present in token_presence_map.values():
        union_tokens |= present
        if intersection_tokens is None:
            intersection_tokens = set(present)
        else:
            intersection_tokens &= present
    intersection_tokens = intersection_tokens or set()
    token_sync_ratio = _safe_ratio(float(len(intersection_tokens)), float(max(1, len(union_tokens))), default=1.0)

    coverage_payload = contract_coverage_jsonable(root)
    cov_summary = coverage_payload.get("summary") if isinstance(coverage_payload, dict) else {}
    if not isinstance(cov_summary, dict):
        cov_summary = {}
    must_rules = int(cov_summary.get("must_rules", 0))
    must_covered = int(cov_summary.get("must_covered", 0))
    must_coverage_ratio = _safe_ratio(float(must_covered), float(max(1, must_rules)), default=0.0)

    segments: dict[str, Any] = {}
    order = [str(rule["segment"]) for rule in rules] + ["other"]
    seen: list[str] = []
    for seg in order + [str(r["segment"]) for r in rows]:
        if seg not in seen:
            seen.append(seg)
    for seg in seen:
        seg_rows = [r for r in rows if str(r["segment"]) == seg]
        segments[seg] = _summarize_segment(
            seg_rows,
            ["required_token_coverage_ratio", "missing_required_token_count"],
        )

    total = len(rows)
    token_cov_overall = _safe_ratio(
        sum(float(r["required_token_coverage_ratio"]) for r in rows),
        float(total),
        default=0.0,
    )
    overall_ratio = (token_cov_overall + must_coverage_ratio + token_sync_ratio) / 3.0

    return {
        "version": 1,
        "summary": {
            "total_docs": total,
            "overall_contract_assertions_ratio": overall_ratio,
            "overall_required_token_coverage_ratio": token_cov_overall,
            "contract_must_coverage_ratio": must_coverage_ratio,
            "token_sync_ratio": token_sync_ratio,
        },
        "segments": segments,
        "docs": rows,
        "config": cfg,
        "errors": errors,
    }

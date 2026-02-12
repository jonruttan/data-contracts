from __future__ import annotations

import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import yaml
from spec_runner.doc_parser import iter_spec_doc_tests

_NORMATIVE_CONTRACT_DOCS = [
    "docs/spec/contract/00-design-goals.md",
    "docs/spec/contract/versioning.md",
    "docs/spec/contract/01-discovery.md",
    "docs/spec/contract/02-case-shape.md",
    "docs/spec/contract/03-assertions.md",
    "docs/spec/contract/03a-regex-portability-v1.md",
    "docs/spec/contract/04-harness.md",
    "docs/spec/contract/05-errors.md",
    "docs/spec/contract/06-conformance.md",
]
_REGEX_PROFILE_DOC = "docs/spec/contract/03a-regex-portability-v1.md"
_ASSERTION_OPERATOR_DOC_SYNC_TOKENS = ("contain", "regex")
_CONFORMANCE_MAX_BLOCK_LINES = 50
_CONFORMANCE_CASE_ID_PATTERN = re.compile(r"\bSRCONF-[A-Z0-9-]+\b")


def _read_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _normalize_sentence(s: str) -> str:
    return re.sub(r"\s+", " ", str(s).strip().lower())


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


def _lint_conformance_case_docs(cases_dir: Path) -> list[str]:
    errs: list[str] = []
    global_ids: set[str] = set()
    for p in sorted(cases_dir.glob("*.spec.md")):
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
                errs.append(
                    f"conformance style: block exceeds {_CONFORMANCE_MAX_BLOCK_LINES} lines "
                    f"in {p}:{start + 1}"
                )
            payload = yaml.safe_load("\n".join(block_lines)) if block_lines else None
            if isinstance(payload, list):
                errs.append(f"conformance style: one case per spec-test block required in {p}:{start + 1}")
            if isinstance(payload, dict):
                rid = str(payload.get("id", "")).strip()
                rationale = str(payload.get("rationale", "")).strip()
                if not rationale:
                    errs.append(f"conformance style: case must include non-empty rationale: {p}:{start + 1}")
                title = str(payload.get("title", "")).strip()
                if title and _normalize_sentence(title) == _normalize_sentence(rationale):
                    errs.append(
                        "conformance style: rationale must add context beyond title "
                        f"for case {rid or '<unknown>'}: {p}:{start + 1}"
                    )
                if rid:
                    ids_in_file.append(rid)
                    if rid in global_ids:
                        errs.append(f"duplicate conformance case id across files: {rid}")
                    global_ids.add(rid)
                    prev_idx = start - 1
                    while prev_idx >= 0 and not lines[prev_idx].strip():
                        prev_idx -= 1
                    expected_heading = f"## {rid}"
                    if prev_idx < 0 or lines[prev_idx].strip() != expected_heading:
                        errs.append(
                            f"conformance style: expected heading '{expected_heading}' immediately before block "
                            f"in {p}:{start + 1}"
                        )
            i += 1
        if ids_in_file != sorted(ids_in_file):
            errs.append(f"conformance style: case ids must be sorted within file: {p}")
    return errs


def _collect_fixture_case_ids(path: Path) -> set[str]:
    ids: set[str] = set()
    for spec in iter_spec_doc_tests(path):
        rid = str(spec.test.get("id", "")).strip()
        if rid:
            ids.add(rid)
    return ids


def _lint_conformance_case_index(cases_dir: Path, fixture_ids: set[str]) -> list[str]:
    errs: list[str] = []
    index_path = cases_dir / "README.md"
    if not fixture_ids and not index_path.exists():
        return errs
    if not index_path.exists():
        errs.append(f"conformance case index missing: {index_path}")
        return errs

    raw = index_path.read_text(encoding="utf-8")
    indexed_ids = set(_CONFORMANCE_CASE_ID_PATTERN.findall(raw))
    for rid in sorted(fixture_ids - indexed_ids):
        errs.append(f"conformance case index missing id: {rid}")
    for rid in sorted(indexed_ids - fixture_ids):
        errs.append(f"conformance case index has stale id: {rid}")
    return errs


@dataclass(frozen=True)
class RuleCoverage:
    rule_id: str
    norm: str
    lifecycle_status: str
    introduced_in: str
    deprecated_in: str | None
    removed_in: str | None
    has_traceability: bool
    has_tests: bool
    has_conformance_cases: bool
    is_covered: bool


def _exists_repo_or_runner(repo_root: Path, rel: str) -> bool:
    p = repo_root / rel
    if p.exists():
        return True
    return (repo_root / "tools/spec_runner" / rel).exists()


def _load_policy_and_trace(repo_root: Path) -> tuple[dict[str, Any], dict[str, Any], set[str]]:
    policy_path = repo_root / "tools/spec_runner/docs/spec/contract/policy-v1.yaml"
    trace_path = repo_root / "tools/spec_runner/docs/spec/contract/traceability-v1.yaml"
    cases_dir = repo_root / "tools/spec_runner/docs/spec/conformance/cases"
    policy = _read_yaml(policy_path) or {}
    trace = _read_yaml(trace_path) or {}
    conformance_ids = _collect_fixture_case_ids(cases_dir)
    return policy, trace, conformance_ids


def _parse_contract_version(label: str) -> int | None:
    s = str(label).strip().lower()
    if len(s) < 2 or not s.startswith("v"):
        return None
    n = s[1:]
    if not n.isdigit():
        return None
    return int(n)


def build_contract_coverage(repo_root: Path) -> list[RuleCoverage]:
    repo_root = repo_root.resolve()
    policy, trace, _conformance_ids = _load_policy_and_trace(repo_root)
    rules = policy.get("rules") or []
    links = trace.get("links") or []
    if not isinstance(rules, list) or not isinstance(links, list):
        return []

    links_by_rule: dict[str, dict[str, Any]] = {}
    for l in links:
        if isinstance(l, dict):
            rid = str(l.get("rule_id", "")).strip()
            if rid and rid not in links_by_rule:
                links_by_rule[rid] = l

    out: list[RuleCoverage] = []
    for r in rules:
        if not isinstance(r, dict):
            continue
        rid = str(r.get("id", "")).strip()
        if not rid:
            continue
        norm = str(r.get("norm", "")).upper()
        introduced_in = None if r.get("introduced_in") is None else str(r.get("introduced_in"))
        deprecated_in = None if r.get("deprecated_in") is None else str(r.get("deprecated_in"))
        removed_in = None if r.get("removed_in") is None else str(r.get("removed_in"))
        if removed_in:
            lifecycle_status = "removed"
        elif deprecated_in:
            lifecycle_status = "deprecated"
        else:
            lifecycle_status = "active"
        link = links_by_rule.get(rid)
        has_trace = link is not None
        conformance_case_ids = (link.get("conformance_case_ids") if isinstance(link, dict) else []) or []
        unit_test_refs = (link.get("unit_test_refs") if isinstance(link, dict) else []) or []
        has_tests = isinstance(unit_test_refs, list) and len(unit_test_refs) > 0
        has_conf = isinstance(conformance_case_ids, list) and len(conformance_case_ids) > 0
        if norm == "MUST":
            is_covered = has_trace and (has_tests or has_conf)
        else:
            is_covered = has_trace
        out.append(
            RuleCoverage(
                rule_id=rid,
                norm=norm,
                lifecycle_status=lifecycle_status,
                introduced_in="" if introduced_in is None else introduced_in,
                deprecated_in=deprecated_in,
                removed_in=removed_in,
                has_traceability=has_trace,
                has_tests=has_tests,
                has_conformance_cases=has_conf,
                is_covered=is_covered,
            )
        )
    return out


def contract_coverage_jsonable(repo_root: Path) -> dict[str, Any]:
    coverage = build_contract_coverage(repo_root)
    total = len(coverage)
    covered = sum(1 for r in coverage if r.is_covered)
    must_total = sum(1 for r in coverage if r.norm == "MUST")
    must_covered = sum(1 for r in coverage if r.norm == "MUST" and r.is_covered)
    active_total = sum(1 for r in coverage if r.lifecycle_status == "active")
    deprecated_total = sum(1 for r in coverage if r.lifecycle_status == "deprecated")
    removed_total = sum(1 for r in coverage if r.lifecycle_status == "removed")
    return {
        "version": 1,
        "summary": {
            "total_rules": total,
            "covered_rules": covered,
            "coverage_ratio": 0.0 if total == 0 else covered / total,
            "must_rules": must_total,
            "must_covered": must_covered,
            "active_rules": active_total,
            "deprecated_rules": deprecated_total,
            "removed_rules": removed_total,
        },
        "rules": [asdict(r) for r in coverage],
    }


def check_contract_governance(repo_root: Path) -> list[str]:
    errs: list[str] = []
    repo_root = repo_root.resolve()

    policy, trace, conformance_ids = _load_policy_and_trace(repo_root)
    cases_dir = repo_root / "tools/spec_runner/docs/spec/conformance/cases"
    if cases_dir.exists():
        errs.extend(_lint_conformance_case_docs(cases_dir))
        errs.extend(_lint_conformance_case_index(cases_dir, conformance_ids))
    rules = policy.get("rules") or []
    links = trace.get("links") or []
    if not isinstance(rules, list):
        return ["policy-v1.yaml rules must be a list"]
    if not isinstance(links, list):
        return ["traceability-v1.yaml links must be a list"]

    rules_by_id: dict[str, dict[str, Any]] = {}
    allowed_norms = {"MUST", "SHOULD", "MUST_NOT"}

    for r in rules:
        if not isinstance(r, dict):
            errs.append("policy rule entries must be mappings")
            continue
        rid = str(r.get("id", "")).strip()
        if not rid:
            errs.append("policy rule missing id")
            continue
        if rid in rules_by_id:
            errs.append(f"duplicate policy rule id: {rid}")
        rules_by_id[rid] = r
        norm = str(r.get("norm", "")).upper()
        if norm not in allowed_norms:
            errs.append(f"invalid norm for {rid}: {norm!r}")
        introduced = str(r.get("introduced_in", "")).strip()
        if not introduced:
            errs.append(f"policy rule missing introduced_in: {rid}")
        introduced_n = _parse_contract_version(introduced) if introduced else None
        if introduced and introduced_n is None:
            errs.append(f"invalid introduced_in for {rid}: {introduced!r}")
        deprecated = str(r.get("deprecated_in", "")).strip()
        deprecated_n = _parse_contract_version(deprecated) if deprecated else None
        if deprecated and deprecated_n is None:
            errs.append(f"invalid deprecated_in for {rid}: {deprecated!r}")
        removed = str(r.get("removed_in", "")).strip()
        removed_n = _parse_contract_version(removed) if removed else None
        if removed and removed_n is None:
            errs.append(f"invalid removed_in for {rid}: {removed!r}")
        if removed and not deprecated:
            errs.append(f"removed_in requires deprecated_in for {rid}")
        if introduced_n is not None and deprecated_n is not None and deprecated_n < introduced_n:
            errs.append(f"deprecated_in precedes introduced_in for {rid}")
        if introduced_n is not None and removed_n is not None and removed_n <= introduced_n:
            errs.append(f"removed_in must be greater than introduced_in for {rid}")
        if deprecated_n is not None and removed_n is not None and removed_n <= deprecated_n:
            errs.append(f"removed_in must be greater than deprecated_in for {rid}")
        for field in ("rationale", "risk_if_violated"):
            if not str(r.get(field, "")).strip():
                errs.append(f"policy rule missing {field}: {rid}")
        refs = r.get("references")
        if not isinstance(refs, list) or not refs:
            errs.append(f"policy rule references must be a non-empty list: {rid}")
            refs = []
        for rel in refs:
            srel = str(rel)
            if not _exists_repo_or_runner(repo_root, srel):
                errs.append(f"missing policy reference for {rid}: {srel}")

    links_by_rule: dict[str, dict[str, Any]] = {}
    referenced_contract_docs: set[str] = set()
    for l in links:
        if not isinstance(l, dict):
            errs.append("traceability link entries must be mappings")
            continue
        rid = str(l.get("rule_id", "")).strip()
        if not rid:
            errs.append("traceability link missing rule_id")
            continue
        if rid in links_by_rule:
            errs.append(f"duplicate traceability rule_id: {rid}")
        links_by_rule[rid] = l
        if rid not in rules_by_id:
            errs.append(f"traceability references unknown policy rule: {rid}")
        want_policy_ref = f"docs/spec/contract/policy-v1.yaml#{rid}"
        got_policy_ref = str(l.get("policy_ref", "")).strip()
        if got_policy_ref != want_policy_ref:
            errs.append(
                f"traceability policy_ref mismatch for {rid}: "
                f"expected {want_policy_ref}, got {got_policy_ref or '<missing>'}"
            )
        cref = l.get("contract_refs") or []
        if isinstance(cref, list):
            for rel in cref:
                referenced_contract_docs.add(str(rel))

    for rid in rules_by_id:
        if rid not in links_by_rule:
            errs.append(f"policy rule missing traceability link: {rid}")

    for rid, rule in rules_by_id.items():
        norm = str(rule.get("norm", "")).upper()
        link = links_by_rule.get(rid)
        if not link:
            continue

        conformance_case_ids = link.get("conformance_case_ids") or []
        unit_test_refs = link.get("unit_test_refs") or []
        if not isinstance(conformance_case_ids, list):
            errs.append(f"traceability conformance_case_ids must be a list: {rid}")
            conformance_case_ids = []
        if not isinstance(unit_test_refs, list):
            errs.append(f"traceability unit_test_refs must be a list: {rid}")
            unit_test_refs = []

        if norm == "MUST" and not conformance_case_ids and not unit_test_refs:
            errs.append(f"MUST rule missing test evidence (conformance_case_ids/unit_test_refs): {rid}")

        for rel in link.get("contract_refs") or []:
            if not _exists_repo_or_runner(repo_root, str(rel)):
                errs.append(f"missing contract_ref for {rid}: {rel}")
        for rel in link.get("schema_refs") or []:
            if not _exists_repo_or_runner(repo_root, str(rel)):
                errs.append(f"missing schema_ref for {rid}: {rel}")
        for rel in unit_test_refs:
            if not _exists_repo_or_runner(repo_root, str(rel)):
                errs.append(f"missing unit_test_ref for {rid}: {rel}")
        for rel in link.get("implementation_refs") or []:
            if not (repo_root / "tools/spec_runner" / str(rel)).exists():
                errs.append(f"missing implementation_ref for {rid}: {rel}")

        for cid in conformance_case_ids:
            c = str(cid)
            if c not in conformance_ids:
                errs.append(f"missing conformance case id for {rid}: {c}")

    for rel in _NORMATIVE_CONTRACT_DOCS:
        if not _exists_repo_or_runner(repo_root, rel):
            errs.append(f"missing normative contract doc: {rel}")
        elif rel not in referenced_contract_docs:
            errs.append(f"normative contract doc missing traceability coverage: {rel}")

    assertions_doc = repo_root / "tools/spec_runner/docs/spec/contract/03-assertions.md"
    schema_doc = repo_root / "tools/spec_runner/docs/spec/schema/schema-v1.md"
    policy_doc = repo_root / "tools/spec_runner/docs/spec/contract/policy-v1.yaml"
    if assertions_doc.exists() and schema_doc.exists() and policy_doc.exists():
        assertions_text = assertions_doc.read_text(encoding="utf-8")
        schema_text = schema_doc.read_text(encoding="utf-8")
        policy_text = policy_doc.read_text(encoding="utf-8")
        if _REGEX_PROFILE_DOC not in assertions_text:
            errs.append(f"assertions doc missing regex portability profile reference: {_REGEX_PROFILE_DOC}")
        if _REGEX_PROFILE_DOC not in schema_text:
            errs.append(f"schema doc missing regex portability profile reference: {_REGEX_PROFILE_DOC}")
        if _REGEX_PROFILE_DOC not in policy_text:
            errs.append(f"policy doc missing regex portability profile reference: {_REGEX_PROFILE_DOC}")
        for tok in _ASSERTION_OPERATOR_DOC_SYNC_TOKENS:
            if tok not in assertions_text:
                errs.append(f"assertions doc missing operator token: {tok}")
            if tok not in schema_text:
                errs.append(f"schema doc missing operator token: {tok}")

    return errs

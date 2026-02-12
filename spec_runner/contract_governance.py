from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def _read_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _collect_fixture_case_ids(path: Path) -> set[str]:
    ids: set[str] = set()
    for p in sorted(path.glob("*.y*ml")):
        payload = _read_yaml(p)
        if not isinstance(payload, dict):
            continue
        cases = payload.get("cases") or []
        if isinstance(cases, list):
            for c in cases:
                if isinstance(c, dict) and c.get("id"):
                    ids.add(str(c["id"]))
    return ids


def _collect_expected_ids(path: Path) -> set[str]:
    ids: set[str] = set()
    for p in sorted(path.glob("*.y*ml")):
        payload = _read_yaml(p)
        if not isinstance(payload, dict):
            continue
        results = payload.get("results") or []
        if isinstance(results, list):
            for r in results:
                if isinstance(r, dict) and r.get("id"):
                    ids.add(str(r["id"]))
    return ids


def check_contract_governance(repo_root: Path) -> list[str]:
    errs: list[str] = []
    repo_root = repo_root.resolve()

    policy_path = repo_root / "tools/spec_runner/docs/spec/contract/policy-v1.yaml"
    trace_path = repo_root / "tools/spec_runner/docs/spec/contract/traceability-v1.yaml"
    cases_dir = repo_root / "tools/spec_runner/fixtures/conformance/cases"
    expected_dir = repo_root / "tools/spec_runner/fixtures/conformance/expected"

    policy = _read_yaml(policy_path) or {}
    trace = _read_yaml(trace_path) or {}
    rules = policy.get("rules") or []
    links = trace.get("links") or []
    if not isinstance(rules, list):
        return ["policy-v1.yaml rules must be a list"]
    if not isinstance(links, list):
        return ["traceability-v1.yaml links must be a list"]

    rules_by_id: dict[str, dict[str, Any]] = {}
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

    links_by_rule: dict[str, dict[str, Any]] = {}
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

    conformance_ids = _collect_fixture_case_ids(cases_dir)
    expected_ids = _collect_expected_ids(expected_dir)

    def _exists_repo_or_runner(rel: str) -> bool:
        p = repo_root / rel
        if p.exists():
            return True
        return (repo_root / "tools/spec_runner" / rel).exists()

    for rid, rule in rules_by_id.items():
        norm = str(rule.get("norm", "")).upper()
        if norm != "MUST":
            continue
        link = links_by_rule.get(rid)
        if not link:
            errs.append(f"MUST rule missing traceability link: {rid}")
            continue

        conformance_case_ids = link.get("conformance_case_ids") or []
        unit_test_refs = link.get("unit_test_refs") or []
        if not isinstance(conformance_case_ids, list):
            errs.append(f"traceability conformance_case_ids must be a list: {rid}")
            conformance_case_ids = []
        if not isinstance(unit_test_refs, list):
            errs.append(f"traceability unit_test_refs must be a list: {rid}")
            unit_test_refs = []

        if not conformance_case_ids and not unit_test_refs:
            errs.append(f"MUST rule missing test evidence (conformance_case_ids/unit_test_refs): {rid}")

        for rel in link.get("contract_refs") or []:
            if not _exists_repo_or_runner(str(rel)):
                errs.append(f"missing contract_ref for {rid}: {rel}")
        for rel in link.get("schema_refs") or []:
            if not _exists_repo_or_runner(str(rel)):
                errs.append(f"missing schema_ref for {rid}: {rel}")
        for rel in unit_test_refs:
            if not _exists_repo_or_runner(str(rel)):
                errs.append(f"missing unit_test_ref for {rid}: {rel}")
        for rel in link.get("implementation_refs") or []:
            if not (repo_root / "tools/spec_runner" / str(rel)).exists():
                errs.append(f"missing implementation_ref for {rid}: {rel}")

        for cid in conformance_case_ids:
            c = str(cid)
            if c not in conformance_ids:
                errs.append(f"missing conformance case id for {rid}: {c}")
            if c not in expected_ids:
                errs.append(f"missing expected result id for {rid}: {c}")

    return errs

from pathlib import Path

import yaml

from spec_runner.contract_governance import (
    build_contract_coverage,
    check_contract_governance,
    contract_coverage_jsonable,
)

_NORMATIVE_DOCS = [
    "00-design-goals.md",
    "versioning.md",
    "01-discovery.md",
    "02-case-shape.md",
    "03-assertions.md",
    "03a-regex-portability-v1.md",
    "04-harness.md",
    "05-errors.md",
    "06-conformance.md",
]


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _seed_governance_repo(tmp_path: Path) -> None:
    _write_text(tmp_path / "tools/spec_runner/docs/spec/schema/schema-v1.md", "contain regex docs/spec/contract/03a-regex-portability-v1.md\n")
    for name in _NORMATIVE_DOCS:
        content = "x\n"
        if name == "03-assertions.md":
            content = "contain regex docs/spec/contract/03a-regex-portability-v1.md\n"
        _write_text(tmp_path / "tools/spec_runner/docs/spec/contract" / name, content)
    _write_text(tmp_path / "tools/spec_runner/tests/test_contract_governance_unit.py", "x\n")
    (tmp_path / "tools/spec_runner/docs/spec/conformance/cases").mkdir(parents=True, exist_ok=True)
    (tmp_path / "tools/spec_runner/docs/spec/conformance/expected").mkdir(parents=True, exist_ok=True)


def _write_min_policy_trace(tmp_path: Path, *, rule_id: str) -> None:
    policy = {
        "rules": [
            {
                "id": rule_id,
                "introduced_in": "v1",
                "norm": "SHOULD",
                "scope": "governance",
                "applies_to": "docs",
                "requirement": "x",
                "rationale": "because",
                "risk_if_violated": "risk",
                "references": ["docs/spec/contract/README.md"],
            }
        ]
    }
    trace = {
        "links": [
            {
                "rule_id": rule_id,
                "policy_ref": f"docs/spec/contract/policy-v1.yaml#{rule_id}",
                "contract_refs": [f"docs/spec/contract/{x}" for x in _NORMATIVE_DOCS],
                "schema_refs": ["docs/spec/schema/schema-v1.md"],
                "conformance_case_ids": [],
                "unit_test_refs": ["tools/spec_runner/tests/test_contract_governance_unit.py"],
                "implementation_refs": [],
            }
        ]
    }
    _write_text(
        tmp_path / "tools/spec_runner/docs/spec/contract/policy-v1.yaml",
        yaml.safe_dump(policy, sort_keys=False),
    )
    _write_text(
        tmp_path / "tools/spec_runner/docs/spec/contract/traceability-v1.yaml",
        yaml.safe_dump(trace, sort_keys=False),
    )
    _write_text(tmp_path / "tools/spec_runner/docs/spec/contract/README.md", "x\n")


def test_contract_governance_passes_on_repo_state():
    repo_root = Path(__file__).resolve().parents[3]
    errs = check_contract_governance(repo_root)
    assert errs == []


def test_contract_governance_fails_when_must_rule_has_no_evidence(tmp_path):
    (tmp_path / "tools/spec_runner/docs/spec/contract").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/conformance/cases").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/conformance/expected").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/contract/04-harness.md").write_text("x", encoding="utf-8")
    (tmp_path / "tools/spec_runner/docs/spec/schema").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/schema/schema-v1.md").write_text("x", encoding="utf-8")

    policy = {
        "rules": [
            {
                "id": "R1",
                "introduced_in": "v1",
                "norm": "MUST",
                "scope": "case",
                "applies_to": "x",
                "requirement": "y",
            }
        ]
    }
    trace = {
        "links": [
            {
                "rule_id": "R1",
                "contract_refs": ["tools/spec_runner/docs/spec/contract/04-harness.md"],
                "schema_refs": ["tools/spec_runner/docs/spec/schema/schema-v1.md"],
                "conformance_case_ids": [],
                "unit_test_refs": [],
                "implementation_refs": [],
            }
        ]
    }
    (tmp_path / "tools/spec_runner/docs/spec/contract/policy-v1.yaml").write_text(
        yaml.safe_dump(policy, sort_keys=False),
        encoding="utf-8",
    )
    (tmp_path / "tools/spec_runner/docs/spec/contract/traceability-v1.yaml").write_text(
        yaml.safe_dump(trace, sort_keys=False),
        encoding="utf-8",
    )

    errs = check_contract_governance(tmp_path)
    assert any("missing test evidence" in e for e in errs)


def test_contract_governance_fails_on_invalid_norm_and_missing_metadata(tmp_path):
    (tmp_path / "tools/spec_runner/docs/spec/contract").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/conformance/cases").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/conformance/expected").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/contract/04-harness.md").write_text("x", encoding="utf-8")
    (tmp_path / "tools/spec_runner/docs/spec/schema").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/schema/schema-v1.md").write_text("x", encoding="utf-8")

    policy = {
        "rules": [
            {
                "id": "R2",
                "introduced_in": "v1",
                "norm": "MUSTBE",
                "scope": "case",
                "applies_to": "x",
                "requirement": "y",
                "references": ["tools/spec_runner/docs/spec/contract/04-harness.md"],
            }
        ]
    }
    trace = {
        "links": [
            {
                "rule_id": "R2",
                "policy_ref": "docs/spec/contract/policy-v1.yaml#R2",
                "contract_refs": ["tools/spec_runner/docs/spec/contract/04-harness.md"],
                "schema_refs": ["tools/spec_runner/docs/spec/schema/schema-v1.md"],
                "conformance_case_ids": [],
                "unit_test_refs": [],
                "implementation_refs": [],
            }
        ]
    }
    (tmp_path / "tools/spec_runner/docs/spec/contract/policy-v1.yaml").write_text(
        yaml.safe_dump(policy, sort_keys=False),
        encoding="utf-8",
    )
    (tmp_path / "tools/spec_runner/docs/spec/contract/traceability-v1.yaml").write_text(
        yaml.safe_dump(trace, sort_keys=False),
        encoding="utf-8",
    )

    errs = check_contract_governance(tmp_path)
    assert any("invalid norm" in e for e in errs)
    assert any("missing rationale" in e for e in errs)
    assert any("missing risk_if_violated" in e for e in errs)


def test_contract_governance_fails_on_policy_ref_mismatch(tmp_path):
    (tmp_path / "tools/spec_runner/docs/spec/contract").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/conformance/cases").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/conformance/expected").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/contract/04-harness.md").write_text("x", encoding="utf-8")
    (tmp_path / "tools/spec_runner/docs/spec/schema").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/schema/schema-v1.md").write_text("x", encoding="utf-8")

    policy = {
        "rules": [
            {
                "id": "R3",
                "introduced_in": "v1",
                "norm": "SHOULD",
                "scope": "implementation",
                "applies_to": "x",
                "requirement": "y",
                "rationale": "because",
                "risk_if_violated": "risk",
                "references": ["tools/spec_runner/docs/spec/contract/04-harness.md"],
            }
        ]
    }
    trace = {
        "links": [
            {
                "rule_id": "R3",
                "policy_ref": "docs/spec/contract/policy-v1.yaml#WRONG",
                "contract_refs": ["tools/spec_runner/docs/spec/contract/04-harness.md"],
                "schema_refs": ["tools/spec_runner/docs/spec/schema/schema-v1.md"],
                "conformance_case_ids": [],
                "unit_test_refs": [],
                "implementation_refs": [],
            }
        ]
    }
    (tmp_path / "tools/spec_runner/docs/spec/contract/policy-v1.yaml").write_text(
        yaml.safe_dump(policy, sort_keys=False),
        encoding="utf-8",
    )
    (tmp_path / "tools/spec_runner/docs/spec/contract/traceability-v1.yaml").write_text(
        yaml.safe_dump(trace, sort_keys=False),
        encoding="utf-8",
    )

    errs = check_contract_governance(tmp_path)
    assert any("policy_ref mismatch" in e for e in errs)


def test_contract_coverage_marks_must_rules_covered_on_repo_state():
    repo_root = Path(__file__).resolve().parents[3]
    coverage = build_contract_coverage(repo_root)
    must_rules = [r for r in coverage if r.norm == "MUST"]
    assert must_rules
    assert all(r.is_covered for r in must_rules)
    payload = contract_coverage_jsonable(repo_root)
    summary = payload["summary"]
    assert {"active_rules", "deprecated_rules", "removed_rules"} <= set(summary.keys())


def test_contract_coverage_marks_uncovered_must(tmp_path):
    (tmp_path / "tools/spec_runner/docs/spec/contract").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/conformance/cases").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/conformance/expected").mkdir(parents=True)
    policy = {
        "rules": [
            {
                "id": "R4",
                "introduced_in": "v1",
                "norm": "MUST",
                "scope": "case",
                "applies_to": "x",
                "requirement": "y",
                "rationale": "because",
                "risk_if_violated": "risk",
                "references": [],
            }
        ]
    }
    trace = {
        "links": [
            {
                "rule_id": "R4",
                "policy_ref": "docs/spec/contract/policy-v1.yaml#R4",
                "conformance_case_ids": [],
                "unit_test_refs": [],
            }
        ]
    }
    (tmp_path / "tools/spec_runner/docs/spec/contract/policy-v1.yaml").write_text(
        yaml.safe_dump(policy, sort_keys=False),
        encoding="utf-8",
    )
    (tmp_path / "tools/spec_runner/docs/spec/contract/traceability-v1.yaml").write_text(
        yaml.safe_dump(trace, sort_keys=False),
        encoding="utf-8",
    )

    coverage = build_contract_coverage(tmp_path)
    assert len(coverage) == 1
    assert coverage[0].norm == "MUST"
    assert coverage[0].is_covered is False


def test_contract_governance_fails_on_lifecycle_ordering(tmp_path):
    (tmp_path / "tools/spec_runner/docs/spec/contract").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/conformance/cases").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/conformance/expected").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/contract/04-harness.md").write_text("x", encoding="utf-8")
    (tmp_path / "tools/spec_runner/docs/spec/schema").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/schema/schema-v1.md").write_text("x", encoding="utf-8")

    policy = {
        "rules": [
            {
                "id": "R5",
                "introduced_in": "v2",
                "deprecated_in": "v1",
                "norm": "SHOULD",
                "scope": "implementation",
                "applies_to": "x",
                "requirement": "y",
                "rationale": "because",
                "risk_if_violated": "risk",
                "references": ["tools/spec_runner/docs/spec/contract/04-harness.md"],
            },
            {
                "id": "R6",
                "introduced_in": "v1",
                "removed_in": "v2",
                "norm": "SHOULD",
                "scope": "implementation",
                "applies_to": "x",
                "requirement": "y",
                "rationale": "because",
                "risk_if_violated": "risk",
                "references": ["tools/spec_runner/docs/spec/contract/04-harness.md"],
            },
        ]
    }
    trace = {
        "links": [
            {
                "rule_id": "R5",
                "policy_ref": "docs/spec/contract/policy-v1.yaml#R5",
                "contract_refs": ["tools/spec_runner/docs/spec/contract/04-harness.md"],
                "schema_refs": ["tools/spec_runner/docs/spec/schema/schema-v1.md"],
                "conformance_case_ids": [],
                "unit_test_refs": [],
                "implementation_refs": [],
            },
            {
                "rule_id": "R6",
                "policy_ref": "docs/spec/contract/policy-v1.yaml#R6",
                "contract_refs": ["tools/spec_runner/docs/spec/contract/04-harness.md"],
                "schema_refs": ["tools/spec_runner/docs/spec/schema/schema-v1.md"],
                "conformance_case_ids": [],
                "unit_test_refs": [],
                "implementation_refs": [],
            },
        ]
    }
    (tmp_path / "tools/spec_runner/docs/spec/contract/policy-v1.yaml").write_text(
        yaml.safe_dump(policy, sort_keys=False),
        encoding="utf-8",
    )
    (tmp_path / "tools/spec_runner/docs/spec/contract/traceability-v1.yaml").write_text(
        yaml.safe_dump(trace, sort_keys=False),
        encoding="utf-8",
    )

    errs = check_contract_governance(tmp_path)
    assert any("deprecated_in precedes introduced_in" in e for e in errs)
    assert any("removed_in requires deprecated_in" in e for e in errs)


def test_contract_governance_fails_when_normative_doc_missing_traceability_coverage(tmp_path):
    _seed_governance_repo(tmp_path)
    policy = {
        "rules": [
            {
                "id": "R7",
                "introduced_in": "v1",
                "norm": "MUST",
                "scope": "governance",
                "applies_to": "docs",
                "requirement": "traceability",
                "rationale": "because",
                "risk_if_violated": "risk",
                "references": ["docs/spec/contract/README.md"],
            }
        ]
    }
    trace = {
        "links": [
            {
                "rule_id": "R7",
                "policy_ref": "docs/spec/contract/policy-v1.yaml#R7",
                "contract_refs": [f"docs/spec/contract/{x}" for x in _NORMATIVE_DOCS if x != "05-errors.md"],
                "schema_refs": ["docs/spec/schema/schema-v1.md"],
                "conformance_case_ids": [],
                "unit_test_refs": ["tools/spec_runner/tests/test_contract_governance_unit.py"],
                "implementation_refs": [],
            }
        ]
    }
    _write_text(
        tmp_path / "tools/spec_runner/docs/spec/contract/policy-v1.yaml",
        yaml.safe_dump(policy, sort_keys=False),
    )
    _write_text(
        tmp_path / "tools/spec_runner/docs/spec/contract/traceability-v1.yaml",
        yaml.safe_dump(trace, sort_keys=False),
    )
    _write_text(tmp_path / "tools/spec_runner/docs/spec/contract/README.md", "x\n")

    errs = check_contract_governance(tmp_path)
    assert any("normative contract doc missing traceability coverage: docs/spec/contract/05-errors.md" in e for e in errs)


def test_contract_governance_fails_when_regex_profile_linkage_is_missing(tmp_path):
    _seed_governance_repo(tmp_path)
    policy = {
        "rules": [
            {
                "id": "R8",
                "introduced_in": "v1",
                "norm": "MUST",
                "scope": "governance",
                "applies_to": "regex.profile",
                "requirement": "linked",
                "rationale": "because",
                "risk_if_violated": "risk",
                "references": ["docs/spec/contract/03-assertions.md"],
            }
        ]
    }
    trace = {
        "links": [
            {
                "rule_id": "R8",
                "policy_ref": "docs/spec/contract/policy-v1.yaml#R8",
                "contract_refs": [f"docs/spec/contract/{x}" for x in _NORMATIVE_DOCS],
                "schema_refs": ["docs/spec/schema/schema-v1.md"],
                "conformance_case_ids": [],
                "unit_test_refs": ["tools/spec_runner/tests/test_contract_governance_unit.py"],
                "implementation_refs": [],
            }
        ]
    }
    _write_text(
        tmp_path / "tools/spec_runner/docs/spec/contract/policy-v1.yaml",
        yaml.safe_dump(policy, sort_keys=False),
    )
    _write_text(
        tmp_path / "tools/spec_runner/docs/spec/contract/traceability-v1.yaml",
        yaml.safe_dump(trace, sort_keys=False),
    )
    _write_text(
        tmp_path / "tools/spec_runner/docs/spec/contract/03-assertions.md",
        "contain regex\n",
    )

    errs = check_contract_governance(tmp_path)
    assert any("assertions doc missing regex portability profile reference" in e for e in errs)


def test_contract_governance_fails_on_multi_case_spec_block(tmp_path):
    _seed_governance_repo(tmp_path)
    _write_min_policy_trace(tmp_path, rule_id="R9")
    _write_text(
        tmp_path / "tools/spec_runner/docs/spec/conformance/cases/bad.spec.md",
        """# Bad

## SRCONF-BAD-001

```yaml spec-test
- id: SRCONF-BAD-001
  type: text.file
  expect:
    portable: {status: pass, category: null}
- id: SRCONF-BAD-002
  type: text.file
  expect:
    portable: {status: pass, category: null}
```
""",
    )
    errs = check_contract_governance(tmp_path)
    assert any("one case per spec-test block required" in e for e in errs)


def test_contract_governance_fails_on_missing_case_heading(tmp_path):
    _seed_governance_repo(tmp_path)
    _write_min_policy_trace(tmp_path, rule_id="R10")
    _write_text(
        tmp_path / "tools/spec_runner/docs/spec/conformance/cases/bad2.spec.md",
        """# Bad

```yaml spec-test
id: SRCONF-BAD-003
why: validate heading placement rule independently
type: text.file
expect:
  portable:
    status: pass
    category: null
```
""",
    )
    errs = check_contract_governance(tmp_path)
    assert any("expected heading '## SRCONF-BAD-003'" in e for e in errs)


def test_contract_governance_fails_when_case_index_missing_fixture_id(tmp_path):
    _seed_governance_repo(tmp_path)
    _write_min_policy_trace(tmp_path, rule_id="R11")
    _write_text(
        tmp_path / "tools/spec_runner/docs/spec/conformance/cases/sample.spec.md",
        """# Sample

## SRCONF-IDX-001

```yaml spec-test
id: SRCONF-IDX-001
why: validate index coverage catches missing ids
type: text.file
expect:
  portable:
    status: pass
    category: null
```
""",
    )
    _write_text(
        tmp_path / "tools/spec_runner/docs/spec/conformance/cases/README.md",
        "# Conformance Cases\n\n- SRCONF-OTHER-999\n",
    )

    errs = check_contract_governance(tmp_path)
    assert any("conformance case index missing id: SRCONF-IDX-001" in e for e in errs)


def test_contract_governance_fails_when_case_index_has_stale_id(tmp_path):
    _seed_governance_repo(tmp_path)
    _write_min_policy_trace(tmp_path, rule_id="R12")
    _write_text(
        tmp_path / "tools/spec_runner/docs/spec/conformance/cases/sample.spec.md",
        """# Sample

## SRCONF-IDX-002

```yaml spec-test
id: SRCONF-IDX-002
why: validate index coverage catches stale ids
type: text.file
expect:
  portable:
    status: pass
    category: null
```
""",
    )
    _write_text(
        tmp_path / "tools/spec_runner/docs/spec/conformance/cases/README.md",
        "# Conformance Cases\n\n- SRCONF-IDX-002\n- SRCONF-STALE-123\n",
    )

    errs = check_contract_governance(tmp_path)
    assert any("conformance case index has stale id: SRCONF-STALE-123" in e for e in errs)


def test_contract_governance_fails_when_case_why_is_missing(tmp_path):
    _seed_governance_repo(tmp_path)
    _write_min_policy_trace(tmp_path, rule_id="R13")
    _write_text(
        tmp_path / "tools/spec_runner/docs/spec/conformance/cases/missing-why.spec.md",
        """# Sample

## SRCONF-WHY-001

```yaml spec-test
id: SRCONF-WHY-001
type: text.file
expect:
  portable:
    status: pass
    category: null
```
""",
    )
    _write_text(
        tmp_path / "tools/spec_runner/docs/spec/conformance/cases/README.md",
        "# Conformance Cases\n\n- SRCONF-WHY-001\n",
    )
    errs = check_contract_governance(tmp_path)
    assert any("case must include non-empty why" in e for e in errs)


def test_contract_governance_fails_when_case_why_is_empty(tmp_path):
    _seed_governance_repo(tmp_path)
    _write_min_policy_trace(tmp_path, rule_id="R14")
    _write_text(
        tmp_path / "tools/spec_runner/docs/spec/conformance/cases/empty-why.spec.md",
        """# Sample

## SRCONF-WHY-002

```yaml spec-test
id: SRCONF-WHY-002
why: "   "
type: text.file
expect:
  portable:
    status: pass
    category: null
```
""",
    )
    _write_text(
        tmp_path / "tools/spec_runner/docs/spec/conformance/cases/README.md",
        "# Conformance Cases\n\n- SRCONF-WHY-002\n",
    )
    errs = check_contract_governance(tmp_path)
    assert any("case must include non-empty why" in e for e in errs)

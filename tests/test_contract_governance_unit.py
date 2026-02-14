# SPEC-OPT-OUT: Exercises behavior not yet representable as stable .spec.md coverage (unit-level API/diagnostic/infrastructure checks).
from pathlib import Path

import yaml

from spec_runner.contract_governance import (
    build_contract_coverage,
    check_contract_governance,
    contract_coverage_jsonable,
)
from spec_runner.settings import case_file_name

_NORMATIVE_DOCS = [
    "00-design-goals.md",
    "versioning.md",
    "01-discovery.md",
    "02-case-shape.md",
    "03-assertions.md",
    "03a-regex-portability-v1.md",
    "03b_spec_lang_v1.md",
    "04-harness.md",
    "05_errors.md",
    "06-conformance.md",
    "07-portable-spec-authoring.md",
    "08_v1_scope.md",
    "09_internal_representation.md",
    "10_docs_quality.md",
    "11_adoption_profiles.md",
]


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _case_doc_path(root: Path, stem: str) -> Path:
    return root / "docs/spec/conformance/cases" / case_file_name(stem)


def _seed_governance_repo(tmp_path: Path) -> None:
    _write_text(tmp_path / "docs/spec/schema/schema_v1.md", "contain regex docs/spec/contract/03a_regex_portability_v1.md\n")
    for name in _NORMATIVE_DOCS:
        content = "x\n"
        if name == "03-assertions.md":
            content = "contain regex docs/spec/contract/03a_regex_portability_v1.md\n"
        _write_text(tmp_path / "docs/spec/contract" / name, content)
    _write_text(tmp_path / "tests/test_contract_governance_unit.py", "x\n")
    _write_text(
        tmp_path / "docs/spec/conformance/purpose_warning_codes.md",
        """# Purpose Warning Codes

- PUR001
- PUR002
- PUR003
- PUR004
""",
    )
    (tmp_path / "docs/spec/conformance/cases").mkdir(parents=True, exist_ok=True)
    (tmp_path / "docs/spec/conformance/expected").mkdir(parents=True, exist_ok=True)


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
                "policy_ref": f"docs/spec/contract/policy_v1.yaml#{rule_id}",
                "contract_refs": [f"docs/spec/contract/{x}" for x in _NORMATIVE_DOCS],
                "schema_refs": ["docs/spec/schema/schema_v1.md"],
                "conformance_case_ids": [],
                "unit_test_refs": ["tests/test_contract_governance_unit.py"],
                "implementation_refs": [],
            }
        ]
    }
    _write_text(
        tmp_path / "docs/spec/contract/policy_v1.yaml",
        yaml.safe_dump(policy, sort_keys=False),
    )
    _write_text(
        tmp_path / "docs/spec/contract/traceability_v1.yaml",
        yaml.safe_dump(trace, sort_keys=False),
    )
    _write_text(tmp_path / "docs/spec/contract/README.md", "x\n")


def test_contract_governance_passes_on_repo_state():
    repo_root = Path(__file__).resolve().parents[1]
    errs = check_contract_governance(repo_root)
    assert errs == []


def test_contract_governance_fails_when_must_rule_has_no_evidence(tmp_path):
    (tmp_path / "docs/spec/contract").mkdir(parents=True)
    (tmp_path / "docs/spec/conformance/cases").mkdir(parents=True)
    (tmp_path / "docs/spec/conformance/expected").mkdir(parents=True)
    (tmp_path / "docs/spec/contract/04_harness.md").write_text("x", encoding="utf-8")
    (tmp_path / "docs/spec/schema").mkdir(parents=True)
    (tmp_path / "docs/spec/schema/schema_v1.md").write_text("x", encoding="utf-8")

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
                "contract_refs": ["docs/spec/contract/04_harness.md"],
                "schema_refs": ["docs/spec/schema/schema_v1.md"],
                "conformance_case_ids": [],
                "unit_test_refs": [],
                "implementation_refs": [],
            }
        ]
    }
    (tmp_path / "docs/spec/contract/policy_v1.yaml").write_text(
        yaml.safe_dump(policy, sort_keys=False),
        encoding="utf-8",
    )
    (tmp_path / "docs/spec/contract/traceability_v1.yaml").write_text(
        yaml.safe_dump(trace, sort_keys=False),
        encoding="utf-8",
    )

    errs = check_contract_governance(tmp_path)
    assert any("missing test evidence" in e for e in errs)


def test_contract_governance_fails_on_invalid_norm_and_missing_metadata(tmp_path):
    (tmp_path / "docs/spec/contract").mkdir(parents=True)
    (tmp_path / "docs/spec/conformance/cases").mkdir(parents=True)
    (tmp_path / "docs/spec/conformance/expected").mkdir(parents=True)
    (tmp_path / "docs/spec/contract/04_harness.md").write_text("x", encoding="utf-8")
    (tmp_path / "docs/spec/schema").mkdir(parents=True)
    (tmp_path / "docs/spec/schema/schema_v1.md").write_text("x", encoding="utf-8")

    policy = {
        "rules": [
            {
                "id": "R2",
                "introduced_in": "v1",
                "norm": "MUSTBE",
                "scope": "case",
                "applies_to": "x",
                "requirement": "y",
                "references": ["docs/spec/contract/04_harness.md"],
            }
        ]
    }
    trace = {
        "links": [
            {
                "rule_id": "R2",
                "policy_ref": "docs/spec/contract/policy_v1.yaml#R2",
                "contract_refs": ["docs/spec/contract/04_harness.md"],
                "schema_refs": ["docs/spec/schema/schema_v1.md"],
                "conformance_case_ids": [],
                "unit_test_refs": [],
                "implementation_refs": [],
            }
        ]
    }
    (tmp_path / "docs/spec/contract/policy_v1.yaml").write_text(
        yaml.safe_dump(policy, sort_keys=False),
        encoding="utf-8",
    )
    (tmp_path / "docs/spec/contract/traceability_v1.yaml").write_text(
        yaml.safe_dump(trace, sort_keys=False),
        encoding="utf-8",
    )

    errs = check_contract_governance(tmp_path)
    assert any("invalid norm" in e for e in errs)
    assert any("missing rationale" in e for e in errs)
    assert any("missing risk_if_violated" in e for e in errs)


def test_contract_governance_fails_on_policy_ref_mismatch(tmp_path):
    (tmp_path / "docs/spec/contract").mkdir(parents=True)
    (tmp_path / "docs/spec/conformance/cases").mkdir(parents=True)
    (tmp_path / "docs/spec/conformance/expected").mkdir(parents=True)
    (tmp_path / "docs/spec/contract/04_harness.md").write_text("x", encoding="utf-8")
    (tmp_path / "docs/spec/schema").mkdir(parents=True)
    (tmp_path / "docs/spec/schema/schema_v1.md").write_text("x", encoding="utf-8")

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
                "references": ["docs/spec/contract/04_harness.md"],
            }
        ]
    }
    trace = {
        "links": [
            {
                "rule_id": "R3",
                "policy_ref": "docs/spec/contract/policy_v1.yaml#WRONG",
                "contract_refs": ["docs/spec/contract/04_harness.md"],
                "schema_refs": ["docs/spec/schema/schema_v1.md"],
                "conformance_case_ids": [],
                "unit_test_refs": [],
                "implementation_refs": [],
            }
        ]
    }
    (tmp_path / "docs/spec/contract/policy_v1.yaml").write_text(
        yaml.safe_dump(policy, sort_keys=False),
        encoding="utf-8",
    )
    (tmp_path / "docs/spec/contract/traceability_v1.yaml").write_text(
        yaml.safe_dump(trace, sort_keys=False),
        encoding="utf-8",
    )

    errs = check_contract_governance(tmp_path)
    assert any("policy_ref mismatch" in e for e in errs)


def test_contract_coverage_marks_must_rules_covered_on_repo_state():
    repo_root = Path(__file__).resolve().parents[1]
    coverage = build_contract_coverage(repo_root)
    must_rules = [r for r in coverage if r.norm == "MUST"]
    assert must_rules
    assert all(r.is_covered for r in must_rules)
    payload = contract_coverage_jsonable(repo_root)
    summary = payload["summary"]
    assert {"active_rules", "deprecated_rules", "removed_rules"} <= set(summary.keys())


def test_contract_coverage_marks_uncovered_must(tmp_path):
    (tmp_path / "docs/spec/contract").mkdir(parents=True)
    (tmp_path / "docs/spec/conformance/cases").mkdir(parents=True)
    (tmp_path / "docs/spec/conformance/expected").mkdir(parents=True)
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
                "policy_ref": "docs/spec/contract/policy_v1.yaml#R4",
                "conformance_case_ids": [],
                "unit_test_refs": [],
            }
        ]
    }
    (tmp_path / "docs/spec/contract/policy_v1.yaml").write_text(
        yaml.safe_dump(policy, sort_keys=False),
        encoding="utf-8",
    )
    (tmp_path / "docs/spec/contract/traceability_v1.yaml").write_text(
        yaml.safe_dump(trace, sort_keys=False),
        encoding="utf-8",
    )

    coverage = build_contract_coverage(tmp_path)
    assert len(coverage) == 1
    assert coverage[0].norm == "MUST"
    assert coverage[0].is_covered is False


def test_contract_governance_fails_on_lifecycle_ordering(tmp_path):
    (tmp_path / "docs/spec/contract").mkdir(parents=True)
    (tmp_path / "docs/spec/conformance/cases").mkdir(parents=True)
    (tmp_path / "docs/spec/conformance/expected").mkdir(parents=True)
    (tmp_path / "docs/spec/contract/04_harness.md").write_text("x", encoding="utf-8")
    (tmp_path / "docs/spec/schema").mkdir(parents=True)
    (tmp_path / "docs/spec/schema/schema_v1.md").write_text("x", encoding="utf-8")

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
                "references": ["docs/spec/contract/04_harness.md"],
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
                "references": ["docs/spec/contract/04_harness.md"],
            },
        ]
    }
    trace = {
        "links": [
            {
                "rule_id": "R5",
                "policy_ref": "docs/spec/contract/policy_v1.yaml#R5",
                "contract_refs": ["docs/spec/contract/04_harness.md"],
                "schema_refs": ["docs/spec/schema/schema_v1.md"],
                "conformance_case_ids": [],
                "unit_test_refs": [],
                "implementation_refs": [],
            },
            {
                "rule_id": "R6",
                "policy_ref": "docs/spec/contract/policy_v1.yaml#R6",
                "contract_refs": ["docs/spec/contract/04_harness.md"],
                "schema_refs": ["docs/spec/schema/schema_v1.md"],
                "conformance_case_ids": [],
                "unit_test_refs": [],
                "implementation_refs": [],
            },
        ]
    }
    (tmp_path / "docs/spec/contract/policy_v1.yaml").write_text(
        yaml.safe_dump(policy, sort_keys=False),
        encoding="utf-8",
    )
    (tmp_path / "docs/spec/contract/traceability_v1.yaml").write_text(
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
                "policy_ref": "docs/spec/contract/policy_v1.yaml#R7",
                "contract_refs": [f"docs/spec/contract/{x}" for x in _NORMATIVE_DOCS if x != "05_errors.md"],
                "schema_refs": ["docs/spec/schema/schema_v1.md"],
                "conformance_case_ids": [],
                "unit_test_refs": ["tests/test_contract_governance_unit.py"],
                "implementation_refs": [],
            }
        ]
    }
    _write_text(
        tmp_path / "docs/spec/contract/policy_v1.yaml",
        yaml.safe_dump(policy, sort_keys=False),
    )
    _write_text(
        tmp_path / "docs/spec/contract/traceability_v1.yaml",
        yaml.safe_dump(trace, sort_keys=False),
    )
    _write_text(tmp_path / "docs/spec/contract/README.md", "x\n")

    errs = check_contract_governance(tmp_path)
    assert any("normative contract doc missing traceability coverage: docs/spec/contract/05_errors.md" in e for e in errs)

from pathlib import Path

import yaml

from spec_runner.contract_governance import check_contract_governance


def test_contract_governance_passes_on_repo_state():
    repo_root = Path(__file__).resolve().parents[3]
    errs = check_contract_governance(repo_root)
    assert errs == []


def test_contract_governance_fails_when_must_rule_has_no_evidence(tmp_path):
    (tmp_path / "tools/spec_runner/docs/spec/contract").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/fixtures/conformance/cases").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/fixtures/conformance/expected").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/contract/04-harness.md").write_text("x", encoding="utf-8")
    (tmp_path / "tools/spec_runner/docs/spec/schema").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/schema/schema-v1.md").write_text("x", encoding="utf-8")

    policy = {
        "rules": [
            {
                "id": "R1",
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
    (tmp_path / "tools/spec_runner/fixtures/conformance/cases").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/fixtures/conformance/expected").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/contract/04-harness.md").write_text("x", encoding="utf-8")
    (tmp_path / "tools/spec_runner/docs/spec/schema").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/schema/schema-v1.md").write_text("x", encoding="utf-8")

    policy = {
        "rules": [
            {
                "id": "R2",
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
    (tmp_path / "tools/spec_runner/fixtures/conformance/cases").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/fixtures/conformance/expected").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/contract/04-harness.md").write_text("x", encoding="utf-8")
    (tmp_path / "tools/spec_runner/docs/spec/schema").mkdir(parents=True)
    (tmp_path / "tools/spec_runner/docs/spec/schema/schema-v1.md").write_text("x", encoding="utf-8")

    policy = {
        "rules": [
            {
                "id": "R3",
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

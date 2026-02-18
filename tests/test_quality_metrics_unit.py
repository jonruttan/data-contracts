# SPEC-OPT-OUT: Metric engine behavior and baseline-comparison logic for quality report helpers.
from __future__ import annotations

from pathlib import Path

from spec_runner.quality_metrics import compare_metric_non_regression
from spec_runner.quality_metrics import contract_assertions_report_jsonable
from spec_runner.quality_metrics import docs_operability_report_jsonable
from spec_runner.quality_metrics import python_dependency_report_jsonable
from spec_runner.quality_metrics import runner_independence_report_jsonable
from spec_runner.quality_metrics import spec_lang_adoption_report_jsonable


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_compare_metric_non_regression_directional_checks() -> None:
    current = {
        "summary": {"a": 0.6, "b": 2.0},
        "segments": {"x": {"c": 0.7}},
    }
    baseline = {
        "summary": {"a": 0.5, "b": 3.0},
        "segments": {"x": {"c": 0.7}},
    }
    violations = compare_metric_non_regression(
        current=current,
        baseline=baseline,
        summary_fields={"a": "non_decrease", "b": "non_increase"},
        segment_fields={"x": {"c": "non_decrease"}},
        epsilon=1e-12,
    )
    assert violations == []

    current_bad = {
        "summary": {"a": 0.4, "b": 4.0},
        "segments": {"x": {"c": 0.6}},
    }
    violations = compare_metric_non_regression(
        current=current_bad,
        baseline=baseline,
        summary_fields={"a": "non_decrease", "b": "non_increase"},
        segment_fields={"x": {"c": "non_decrease"}},
        epsilon=1e-12,
    )
    assert any("summary.a" in v for v in violations)
    assert any("summary.b" in v for v in violations)
    assert any("segments.x.c" in v for v in violations)


def test_spec_lang_adoption_report_basic_shape(tmp_path: Path) -> None:
    _write(
        tmp_path / "docs/spec/conformance/cases/a.spec.md",
        """# A

## C1

```yaml contract-spec
id: C1
type: text.file
assert:
  - target: text
    must:
      - std.string.contains:
        - var: subject
        - x
```
""",
    )
    payload = spec_lang_adoption_report_jsonable(
        tmp_path,
        config={
            "roots": ["docs/spec/conformance/cases"],
            "segment_rules": [{"prefix": "docs/spec/conformance/cases", "segment": "conformance"}],
            "recursive": True,
            "tests_glob": "tests/test_*_unit.py",
        },
    )
    assert payload["errors"] == []
    assert payload["summary"]["total_cases"] == 1
    assert "governance_library_backed_policy_ratio" in payload["summary"]
    assert "impl_library_backed_case_ratio" in payload["summary"]
    assert "conformance" in payload["segments"]


def test_runner_independence_report_basic_shape(tmp_path: Path) -> None:
    _write(tmp_path / "scripts/gate.sh", "SPEC_RUNNER_BIN=./scripts/runner_adapter.sh\n")
    _write(tmp_path / ".github/workflows/ci.yml", "core-gate-rust-adapter:\n  env:\n    SPEC_RUNNER_BIN: ./scripts/rust/runner_adapter.sh\n  run: ./scripts/core_gate.sh\n")
    _write(tmp_path / "scripts/rust/runner_adapter.sh", "#!/usr/bin/env bash\n")
    payload = runner_independence_report_jsonable(tmp_path)
    assert payload["errors"] == []
    assert "overall_runner_independence_ratio" in payload["summary"]
    assert "rust_subcommand_native_coverage_ratio" in payload["summary"]


def test_python_dependency_report_basic_shape(tmp_path: Path) -> None:
    _write(tmp_path / "scripts/ci_gate.sh", "SPEC_RUNNER_BIN=\"${ROOT_DIR}/scripts/rust/runner_adapter.sh\"\n")
    _write(tmp_path / "scripts/core_gate.sh", "SPEC_RUNNER_BIN=\"${ROOT_DIR}/scripts/rust/runner_adapter.sh\"\n")
    _write(tmp_path / "scripts/docs_doctor.sh", "SPEC_RUNNER_BIN=\"${ROOT_DIR}/scripts/rust/runner_adapter.sh\"\n")
    _write(tmp_path / "scripts/rust/runner_adapter.sh", "#!/usr/bin/env bash\n")
    _write(tmp_path / "scripts/rust/spec_runner_cli/src/main.rs", "fn main() {}\n")
    payload = python_dependency_report_jsonable(tmp_path)
    assert payload["errors"] == []
    assert "default_lane_python_free_ratio" in payload["summary"]


def test_docs_operability_report_basic_shape(tmp_path: Path) -> None:
    _write(
        tmp_path / "docs/book/reference_manifest.yaml",
        """version: 1
chapters:
  - path: docs/book/a.md
    summary: A
""",
    )
    _write(
        tmp_path / "docs/book/a.md",
        """# A

```yaml doc-meta
doc_id: DOC-REF-001
title: A
status: active
audience: author
owns_tokens: [\"tok.a\"]
requires_tokens: [\"tok.a\"]
commands:
  - run: \"./scripts/ci_gate.sh\"
    purpose: gate
examples:
  - id: EX-A-001
    runnable: true
sections_required: [\"Purpose\", \"Inputs\", \"Outputs\", \"Failure Modes\"]
```

## Purpose
## Inputs
## Outputs
## Failure Modes
""",
    )
    payload = docs_operability_report_jsonable(tmp_path)
    assert "overall_docs_operability_ratio" in payload["summary"]


def test_contract_assertions_report_basic_shape(tmp_path: Path) -> None:
    _write(tmp_path / "docs/spec/contract/03_assertions.md", "must can cannot contain regex evaluate\n")
    _write(tmp_path / "docs/spec/schema/schema_v1.md", "must can cannot contain regex evaluate\n")
    _write(tmp_path / "docs/book/03_assertions.md", "must can cannot contain regex evaluate\n")
    _write(tmp_path / "docs/spec/contract/03b_spec_lang_v1.md", "must can cannot contain regex evaluate\n")
    _write(
        tmp_path / "docs/spec/contract/policy_v1.yaml",
        """version: 1
title: t
rules:
  - id: X
    scope: s
    norm: MUST
    applies_to: a
    requirement: r
    description: d
    rationale: q
    risk_if_violated: z
    references: [docs/spec/contract/03_assertions.md]
""",
    )
    _write(
        tmp_path / "docs/spec/contract/traceability_v1.yaml",
        """version: 1
links:
  - rule_id: X
    policy_ref: docs/spec/contract/policy_v1.yaml#X
    contract_refs: [docs/spec/contract/03_assertions.md]
    schema_refs: [docs/spec/schema/schema_v1.md]
    conformance_case_ids: []
    unit_test_refs: []
    implementation_refs: []
""",
    )

    payload = contract_assertions_report_jsonable(tmp_path)
    assert "overall_contract_assertions_ratio" in payload["summary"]
    assert payload["summary"]["total_docs"] >= 1

# SPEC-OPT-OUT: Metric-scoring and aggregation behavior for portability reporting helper module.
from __future__ import annotations

from pathlib import Path

from spec_runner.spec_portability import spec_portability_report_jsonable


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _base_config(root_name: str = "cases") -> dict:
    return {
        "roots": [root_name],
        "core_types": ["text.file", "cli.run"],
        "segment_rules": [{"prefix": root_name, "segment": "conformance"}],
        "recursive": True,
        "runtime_capability_tokens": ["api.http"],
        "runtime_capability_prefixes": ["runtime.", "php."],
        "weights": {
            "non_evaluate_leaf_share": 0.45,
            "expect_impl_overlay": 0.25,
            "runtime_specific_capability": 0.15,
            "non_core_type": 0.15,
        },
        "report": {"top_n": 5},
        "enforce": False,
    }


def test_evaluate_only_case_scores_one(tmp_path: Path) -> None:
    _write(
        tmp_path / "cases/a.spec.md",
        """# A

## C1

```yaml spec-test
id: C1
type: text.file
assert:
  - target: text
    must:
      - std.string.contains:
        - var: subject
        - ok
```
""",
    )

    payload = spec_portability_report_jsonable(tmp_path, config=_base_config())
    assert payload["errors"] == []
    assert payload["summary"]["total_cases"] == 1
    case = payload["cases"][0]
    assert case["self_contained_ratio"] == 1.0
    assert case["implementation_reliance_ratio"] == 0.0


def test_mixed_leaf_formula_matches_weights(tmp_path: Path) -> None:
    _write(
        tmp_path / "cases/a.spec.md",
        """# A

## C2

```yaml spec-test
id: C2
type: text.file
assert:
  - target: text
    must:
      - contain: ["x"]
      - std.string.contains:
        - var: subject
        - x
```
""",
    )

    payload = spec_portability_report_jsonable(tmp_path, config=_base_config())
    case = payload["cases"][0]
    # All leaves are expression-evaluate leaves in hard-cut mode.
    assert abs(case["self_contained_ratio"] - 1.0) < 1e-9
    assert abs(case["implementation_reliance_ratio"] - 0.0) < 1e-9


def test_impl_overlay_non_core_and_runtime_capability_penalties_apply(tmp_path: Path) -> None:
    _write(
        tmp_path / "cases/a.spec.md",
        """# A

## C3

```yaml spec-test
id: C3
type: api.http
requires:
  capabilities: ["api.http", "runtime.debug"]
expect:
  portable: {status: pass, category: null}
  impl:
    php: {status: fail, category: assertion}
assert: []
```
""",
    )

    payload = spec_portability_report_jsonable(tmp_path, config=_base_config())
    case = payload["cases"][0]
    expected_penalty = 0.25 + 0.15 + 0.15
    assert abs(case["self_contained_ratio"] - (1.0 - expected_penalty)) < 1e-9
    assert "expect.impl overlay present" in case["reasons"]
    assert "runtime-specific capability declared" in case["reasons"]
    assert "non-core type api.http" in case["reasons"]


def test_no_leaf_assertions_are_neutral(tmp_path: Path) -> None:
    _write(
        tmp_path / "cases/a.spec.md",
        """# A

## C4

```yaml spec-test
id: C4
type: text.file
assert: []
```
""",
    )

    payload = spec_portability_report_jsonable(tmp_path, config=_base_config())
    case = payload["cases"][0]
    assert case["leaf_counts"]["total"] == 0
    assert case["self_contained_ratio"] == 1.0


def test_segmented_and_overall_summary_are_reported(tmp_path: Path) -> None:
    _write(
        tmp_path / "conformance/a.spec.md",
        """# C

## C5

```yaml spec-test
id: C5
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
    _write(
        tmp_path / "governance/b.spec.md",
        """# G

## C6

```yaml spec-test
id: C6
type: governance.check
assert:
  - target: text
    must:
      - contain: ["x"]
```
""",
    )

    cfg = _base_config("conformance")
    cfg["roots"] = ["conformance", "governance"]
    cfg["segment_rules"] = [
        {"prefix": "conformance", "segment": "conformance"},
        {"prefix": "governance", "segment": "governance"},
    ]
    cfg["runtime_capability_tokens"] = ["governance.check"]

    payload = spec_portability_report_jsonable(tmp_path, config=cfg)
    assert payload["summary"]["total_cases"] == 2
    assert payload["segments"]["conformance"]["case_count"] == 1
    assert payload["segments"]["governance"]["case_count"] == 1
    assert "overall_logic_self_contained_ratio" in payload["summary"]
    assert "overall_execution_portability_ratio" in payload["summary"]
    assert payload["worst_cases"]

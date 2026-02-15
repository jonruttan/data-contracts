# SPEC-OPT-OUT: Exercises governance engine error-path shaping not yet representable as stable .spec.md fixtures.
from __future__ import annotations

from spec_runner.governance_engine import normalize_policy_evaluate, run_governance_policy


def test_normalize_policy_evaluate_accepts_direct_expr() -> None:
    expr = [{"eq": [1, 1]}]
    assert normalize_policy_evaluate(expr, field="x") == ["eq", 1, 1]


def test_normalize_policy_evaluate_accepts_single_wrapped_expr() -> None:
    expr = [{"eq": [1, 1]}]
    assert normalize_policy_evaluate(expr, field="x") == ["eq", 1, 1]


def test_normalize_policy_evaluate_rejects_invalid_shape() -> None:
    try:
        normalize_policy_evaluate([], field="x")
        raise AssertionError("expected ValueError")
    except ValueError as exc:
        assert "x" in str(exc)


def test_run_governance_policy_true() -> None:
    policy = normalize_policy_evaluate([{"eq": [1, 1]}], field="harness.policy_evaluate")
    got = run_governance_policy(
        check_id="demo.check",
        case_id="CASE-1",
        policy_evaluate=policy,
        subject={},
    )
    assert got.passed is True
    assert got.diagnostics == []


def test_run_governance_policy_false() -> None:
    policy = normalize_policy_evaluate([{"eq": [1, 2]}], field="harness.policy_evaluate")
    got = run_governance_policy(
        check_id="demo.check",
        case_id="CASE-2",
        policy_evaluate=policy,
        subject={},
    )
    assert got.passed is False
    assert got.diagnostics
    assert "CASE-2" in got.diagnostics[0]


def test_run_governance_policy_runtime_error() -> None:
    policy = normalize_policy_evaluate([{"unknown_symbol": [1]}], field="harness.policy_evaluate")
    got = run_governance_policy(
        check_id="demo.check",
        case_id="CASE-3",
        policy_evaluate=policy,
        subject={},
    )
    assert got.passed is False
    assert got.diagnostics
    assert "runtime error" in got.diagnostics[0]

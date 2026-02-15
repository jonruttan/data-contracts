from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from spec_runner.spec_lang import SpecLangLimits, eval_predicate


@dataclass(frozen=True)
class GovernancePolicyResult:
    passed: bool
    diagnostics: list[str]


def normalize_policy_evaluate(raw: object, *, field: str) -> list[object]:
    if not isinstance(raw, list) or not raw:
        raise ValueError(f"{field} must be a list-based spec-lang expression")
    if isinstance(raw[0], str):
        return raw
    if len(raw) == 1 and isinstance(raw[0], list):
        inner = raw[0]
        if inner and isinstance(inner[0], str):
            return inner
    raise ValueError(f"{field} must be a list-based spec-lang expression")


def run_governance_policy(
    *,
    check_id: str,
    case_id: str,
    policy_evaluate: list[object],
    subject: Any,
    limits: SpecLangLimits | None = None,
    symbols: Mapping[str, Any] | None = None,
    policy_path: str = "harness.policy_evaluate",
) -> GovernancePolicyResult:
    cfg = limits or SpecLangLimits()
    try:
        ok = eval_predicate(policy_evaluate, subject=subject, limits=cfg, symbols=symbols)
    except Exception as exc:  # noqa: BLE001
        return GovernancePolicyResult(
            passed=False,
            diagnostics=[
                f"[case_id={case_id} check_id={check_id} policy_path={policy_path}] "
                f"policy_evaluate runtime error: {exc}"
            ],
        )

    if ok:
        return GovernancePolicyResult(passed=True, diagnostics=[])
    return GovernancePolicyResult(
        passed=False,
        diagnostics=[
            f"[case_id={case_id} check_id={check_id} policy_path={policy_path}] "
            "policy_evaluate returned false"
        ],
    )

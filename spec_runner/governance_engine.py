from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from spec_runner.spec_lang import SpecLangLimits, eval_predicate
from spec_runner.spec_lang_yaml_ast import SpecLangYamlAstError, compile_yaml_expr_list


@dataclass(frozen=True)
class GovernancePolicyResult:
    passed: bool
    diagnostics: list[str]


def normalize_policy_evaluate(raw: object, *, field: str) -> list[object]:
    if not isinstance(raw, list):
        raise ValueError(f"{field} must be a non-empty list of mapping-ast expressions")
    try:
        compiled = compile_yaml_expr_list(raw, field_path=field)
    except SpecLangYamlAstError as exc:
        raise ValueError(str(exc)) from exc
    if len(compiled) == 1:
        return compiled[0]
    return ["and", *compiled]


def run_governance_policy(
    *,
    check_id: str,
    case_id: str,
    policy_evaluate: list[object],
    subject: Any,
    limits: SpecLangLimits | None = None,
    symbols: Mapping[str, Any] | None = None,
    imports: Mapping[str, str] | None = None,
    policy_path: str = "harness.policy_evaluate",
) -> GovernancePolicyResult:
    cfg = limits or SpecLangLimits()
    try:
        ok = eval_predicate(
            policy_evaluate,
            subject=subject,
            limits=cfg,
            symbols=symbols,
            imports=imports,
        )
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

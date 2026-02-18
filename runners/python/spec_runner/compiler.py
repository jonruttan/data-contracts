from __future__ import annotations

from pathlib import Path
from typing import Any, Literal, cast

from spec_runner.internal_model import GroupNode, InternalAssertNode, InternalSpecCase, PredicateLeaf
from spec_runner.schema_validator import validate_case_shape
from spec_runner.spec_lang_yaml_ast import SpecLangYamlAstError, compile_yaml_expr_to_sexpr


def _compile_assert_expr_leaf(raw_expr: Any, *, target: str, assert_path: str) -> PredicateLeaf:
    if not isinstance(raw_expr, dict) or not raw_expr:
        raise ValueError(f"{assert_path} must be a non-empty expression mapping")
    if "evaluate" in raw_expr:
        raise ValueError(f"{assert_path} must not use evaluate wrapper; place operator mapping directly in asserts")
    try:
        expr = compile_yaml_expr_to_sexpr(raw_expr, field_path=assert_path)
    except SpecLangYamlAstError as exc:
        raise ValueError(str(exc)) from exc
    # Universal core operator contract: compile-only sugar normalizes to evaluate.
    supported = {"evaluate"}
    op = "evaluate"
    if op == "evaluate":
        pass
    if op not in supported:
        raise ValueError(f"{assert_path} unsupported operator: {op}")
    return PredicateLeaf(
        target=target,
        subject_key=target,
        op=op,
        expr=expr,
        assert_path=assert_path,
    )


def _looks_like_assert_step(item: Any) -> bool:
    return isinstance(item, dict) and "id" in item and "class" in item and "asserts" in item


def compile_assert_tree(
    raw_assert: Any,
    *,
    type_name: str,
    inherited_target: str | None = None,
    assert_path: str = "contract",
    strict_steps: bool = True,
) -> InternalAssertNode:
    if raw_assert is None:
        return GroupNode(op="MUST", target=inherited_target, children=[], assert_path=assert_path)
    if not isinstance(raw_assert, list):
        raise TypeError("contract must be a list of step mappings")

    if not raw_assert:
        return GroupNode(op="MUST", target=inherited_target, children=[], assert_path=assert_path)

    is_step_form = all(_looks_like_assert_step(x) for x in raw_assert)
    if not is_step_form:
        raise ValueError("contract must use step form entries with id/class/asserts")

    seen_ids: set[str] = set()
    step_nodes: list[InternalAssertNode] = []
    for idx, raw_step in enumerate(raw_assert):
        assert isinstance(raw_step, dict)
        step_id = str(raw_step.get("id", "")).strip()
        if not step_id:
            raise ValueError(f"{assert_path}[{idx}].id must be a non-empty string")
        if step_id in seen_ids:
            raise ValueError(f"{assert_path} has duplicate step id: {step_id}")
        seen_ids.add(step_id)
        class_name = str(raw_step.get("class", "")).strip()
        if class_name not in {"MUST", "MAY", "MUST_NOT"}:
            raise ValueError(f"{assert_path}[{idx}].class must be one of: MUST, MAY, MUST_NOT")
        step_target = str(raw_step.get("target", "")).strip() or inherited_target
        raw_checks = raw_step.get("asserts")
        if not isinstance(raw_checks, list) or not raw_checks:
            raise TypeError(f"{assert_path}[{idx}].asserts must be a non-empty list")
        children: list[InternalAssertNode] = [
            _compile_assert_expr_leaf(
                check,
                target=str(step_target or "").strip(),
                assert_path=f"{assert_path}[{idx}].asserts[{cidx}]",
            )
            for cidx, check in enumerate(raw_checks)
        ]
        step_nodes.append(
            GroupNode(
                op=cast(Literal["MUST", "MAY", "MUST_NOT"], class_name),
                target=step_target,
                children=children,
                assert_path=f"{assert_path}[{idx}]<{step_id}>",
            )
        )
    return GroupNode(op="MUST", target=inherited_target, children=step_nodes, assert_path=assert_path)


def compile_external_case(raw_case: dict[str, Any], *, doc_path: Path) -> InternalSpecCase:
    if not isinstance(raw_case, dict):
        raise TypeError("spec case must be a mapping")
    case_id = str(raw_case.get("id", "")).strip()
    type_name = str(raw_case.get("type", "")).strip()
    if not case_id:
        raise ValueError("spec case must include non-empty id")
    if not type_name:
        raise ValueError("spec case must include non-empty type")

    diagnostics = validate_case_shape(raw_case, type_name, doc_path.as_posix())
    if diagnostics:
        raise ValueError("; ".join(d.render() for d in diagnostics))

    harness = raw_case.get("harness")
    if harness is None:
        harness_map: dict[str, Any] = {}
    elif isinstance(harness, dict):
        harness_map = {str(k): v for k, v in harness.items()}
    else:
        raise TypeError("harness must be a mapping")

    assert_tree: InternalAssertNode
    producer_export_type = type_name in {"contract.export"}
    if producer_export_type:
        # Producer-only case type: exported callables are compiled from raw
        # contract step asserts via chain_engine, not from runtime assertion targets.
        assert_tree = GroupNode(op="MUST", target=None, children=[], assert_path="contract")
    else:
        assert_tree = compile_assert_tree(
            raw_case.get("contract", []) or [],
            type_name=type_name,
            strict_steps=True,
        )

    metadata = {
        "expect": raw_case.get("expect"),
        "requires": raw_case.get("requires"),
        "assert_health": raw_case.get("assert_health"),
        "source": {"doc_path": doc_path.as_posix()},
    }

    title_raw = raw_case.get("title")
    title = None if title_raw is None else str(title_raw)

    return InternalSpecCase(
        id=case_id,
        type=type_name,
        title=title,
        doc_path=doc_path,
        harness=harness_map,
        metadata=metadata,
        raw_case=dict(raw_case),
        assert_tree=assert_tree,
    )

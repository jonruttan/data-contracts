from __future__ import annotations

from pathlib import Path
from typing import Any, Literal, cast

from spec_runner.internal_model import GroupNode, InternalAssertNode, InternalSpecCase, PredicateLeaf
from spec_runner.schema_validator import validate_case_shape
from spec_runner.spec_lang_yaml_ast import SpecLangYamlAstError, compile_yaml_expr_to_sexpr


def _require_group_key(node: dict[str, Any]) -> str | None:
    keys = [k for k in ("must", "can", "cannot") if k in node]
    if not keys:
        return None
    if len(keys) > 1:
        got = ", ".join(keys)
        raise ValueError(f"assert group must include exactly one key (must/can/cannot), got: {got}")
    return keys[0]


def _compile_leaf_op(*, op: str, value: Any, target: str, type_name: str, assert_path: str) -> PredicateLeaf:
    supported = {"evaluate"}
    if op not in supported:
        raise ValueError(f"unsupported op for {type_name}.{target}: {op}")

    if op == "evaluate":
        try:
            expr = compile_yaml_expr_to_sexpr(value, field_path=f"{assert_path}.evaluate")
        except SpecLangYamlAstError as exc:
            raise ValueError(str(exc)) from exc
        subject_key = target
    else:
        raise ValueError(f"unsupported op: {op}")

    return PredicateLeaf(target=target, subject_key=subject_key, op=op, expr=expr, assert_path=assert_path)


def compile_assert_tree(
    raw_assert: Any,
    *,
    type_name: str,
    inherited_target: str | None = None,
    assert_path: str = "assert",
) -> InternalAssertNode:
    if raw_assert is None:
        return GroupNode(op="must", target=inherited_target, children=[], assert_path=assert_path)

    if isinstance(raw_assert, list):
        return GroupNode(
            op="must",
            target=inherited_target,
            children=[
                compile_assert_tree(
                    child,
                    type_name=type_name,
                    inherited_target=inherited_target,
                    assert_path=f"{assert_path}[{idx}]",
                )
                for idx, child in enumerate(raw_assert)
            ],
            assert_path=assert_path,
        )

    if not isinstance(raw_assert, dict):
        raise TypeError("assert node must be a mapping or a list")

    group_key = _require_group_key(raw_assert)
    if group_key is not None:
        group_target = str(raw_assert.get("target", "")).strip() or inherited_target
        extra = [k for k in raw_assert.keys() if k not in (group_key, "target")]
        if extra:
            bad = sorted(str(k) for k in extra)[0]
            raise ValueError(f"unknown key in assert group: {bad}")
        children = raw_assert.get(group_key)
        if not isinstance(children, list):
            raise TypeError(f"assert.{group_key} must be a list")
        if not children:
            raise ValueError(f"assert.{group_key} must not be empty")
        group_op = cast(Literal["must", "can", "cannot"], group_key)
        return GroupNode(
            op=group_op,
            target=group_target,
            children=[
                compile_assert_tree(
                    child,
                    type_name=type_name,
                    inherited_target=group_target,
                    assert_path=f"{assert_path}.{group_key}[{idx}]",
                )
                for idx, child in enumerate(children)
            ],
            assert_path=assert_path,
        )

    if "target" in raw_assert:
        raise ValueError("leaf assertion must not include key: target; move target to a parent group")
    if any(k in raw_assert for k in ("must", "can", "cannot")):
        raise ValueError("leaf assertion must not include group keys")

    target = str(inherited_target or "").strip()
    if not target:
        raise ValueError("assertion leaf requires inherited target from a parent group")

    leaves: list[InternalAssertNode] = []
    for op, raw_values in raw_assert.items():
        if not isinstance(raw_values, list):
            raise TypeError(f"assertion op '{op}' must be a list")
        for value in raw_values:
            leaves.append(
                _compile_leaf_op(
                    op=op,
                    value=value,
                    target=target,
                    type_name=type_name,
                    assert_path=assert_path,
                )
            )

    if not leaves:
        raise ValueError("assertion missing an op key (use evaluate:)")
    if len(leaves) == 1:
        return leaves[0]
    return GroupNode(op="must", target=target, children=leaves, assert_path=assert_path)


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

    assert_tree = compile_assert_tree(raw_case.get("assert", []) or [], type_name=type_name)

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

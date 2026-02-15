# SPEC-OPT-OUT: Unit checks for IR compiler normalization and schema enforcement details.
from __future__ import annotations

from pathlib import Path

import pytest

from spec_runner.compiler import compile_assert_tree, compile_external_case
from spec_runner.internal_model import GroupNode, PredicateLeaf


def test_compile_evaluate_leaf_to_spec_lang_expr() -> None:
    raw = {
        "id": "C-1",
        "type": "cli.run",
        "assert": [
            {
                "target": "stdout",
                "must": [
                    {
                        "evaluate": [{"contains": [{"var": "subject"}, "ok"]}],
                    }
                ],
            },
        ],
    }

    case = compile_external_case(raw, doc_path=Path("/tmp/case.spec.md"))
    assert isinstance(case.assert_tree, GroupNode)

    leaves: list[PredicateLeaf] = []

    def _walk(node):
        if isinstance(node, PredicateLeaf):
            leaves.append(node)
            return
        for c in node.children:
            _walk(c)

    _walk(case.assert_tree)
    assert len(leaves) == 1
    leaf = leaves[0]
    assert leaf.op == "evaluate"
    assert leaf.expr == ["contains", ["var", "subject"], "ok"]
    assert leaf.subject_key == "stdout"


def test_compile_non_evaluate_ops_are_rejected() -> None:
    with pytest.raises(ValueError, match="unsupported op for cli.run.stdout: contain"):
        compile_assert_tree(
            [{"target": "stdout", "must": [{"contain": ["x"]}]}],
            type_name="cli.run",
        )


def test_compile_evaluate_is_universal_across_targets() -> None:
    tree = compile_assert_tree(
        [{"target": "status", "must": [{"evaluate": [{"contains": [{"var": "subject"}, "200"]}]}]}],
        type_name="api.http",
    )
    assert isinstance(tree, GroupNode)


def test_compile_only_evaluate_supported_matrix() -> None:
    with pytest.raises(ValueError, match="unsupported op for cli.run.stdout: json_type"):
        compile_assert_tree(
            [{"target": "stdout", "must": [{"json_type": ["array"]}]}],
            type_name="cli.run",
        )


def test_compile_external_case_rejects_unknown_top_level_key() -> None:
    raw = {
        "id": "C-unknown",
        "type": "text.file",
        "assert": [],
        "bogus_extra": True,
    }
    with pytest.raises(ValueError, match="unknown top-level key: bogus_extra"):
        compile_external_case(raw, doc_path=Path("/tmp/case.spec.md"))

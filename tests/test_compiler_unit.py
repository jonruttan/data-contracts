# SPEC-OPT-OUT: Unit checks for IR compiler normalization and schema enforcement details.
from __future__ import annotations

from pathlib import Path

import pytest

from spec_runner.compiler import compile_assert_tree, compile_external_case
from spec_runner.internal_model import GroupNode, PredicateLeaf


def test_compile_leaf_ops_to_spec_lang_exprs() -> None:
    raw = {
        "id": "C-1",
        "type": "cli.run",
        "assert": [
            {
                "target": "stdout",
                "must": [
                    {
                        "contain": ["ok"],
                        "regex": ["^o"],
                        "json_type": ["list"],
                        "evaluate": [["contains", "ok"]],
                    }
                ],
            },
            {
                "target": "stdout_path",
                "must": [{"exists": [True]}],
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
    by_op = {leaf.op: leaf for leaf in leaves}

    assert by_op["contain"].expr == ["contains", ["subject"], "ok"]
    assert by_op["regex"].expr == ["regex_match", ["subject"], "^o"]
    assert by_op["json_type"].expr == ["json_type", ["json_parse", ["subject"]], "list"]
    assert by_op["exists"].expr == ["path_exists", ["subject"]]
    assert by_op["evaluate"].expr == ["contains", "ok"]


def test_compile_exists_enforces_stdout_path_target() -> None:
    with pytest.raises(ValueError, match="unsupported op for cli.run.stdout: exists"):
        compile_assert_tree(
            [{"target": "stdout", "must": [{"exists": [True]}]}],
            type_name="cli.run",
        )


def test_compile_json_type_enforces_supported_values() -> None:
    with pytest.raises(ValueError, match="unsupported json_type"):
        compile_assert_tree(
            [{"target": "stdout", "must": [{"json_type": ["nope"]}]}],
            type_name="cli.run",
        )

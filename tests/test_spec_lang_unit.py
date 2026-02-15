# SPEC-OPT-OUT: Exercises evaluator internals and budget semantics not yet fully representable as stable .spec.md fixtures.
from __future__ import annotations

import pytest

from spec_runner.spec_lang import (
    SpecLangLimits,
    compile_symbol_bindings,
    eval_expr,
    eval_predicate,
    limits_from_harness,
)


def test_spec_lang_basic_predicate_true() -> None:
    expr = ["and", ["contains", "hello"], ["starts_with", ["subject"], "hello"]]
    assert eval_predicate(expr, subject="hello world") is True


def test_spec_lang_unknown_symbol_is_schema_error() -> None:
    with pytest.raises(ValueError, match="unsupported spec_lang symbol"):
        eval_expr(["nope", 1], subject="x")


def test_spec_lang_bad_arity_is_schema_error() -> None:
    with pytest.raises(ValueError, match="arity error"):
        eval_expr(["not", True, False], subject="x")


def test_spec_lang_tail_recursion_is_stack_safe() -> None:
    expr = [
        "let",
        [
            [
                "loop",
                [
                    "fn",
                    ["n", "acc"],
                    [
                        "if",
                        ["eq", ["var", "n"], 0],
                        ["var", "acc"],
                        [
                            "call",
                            ["var", "loop"],
                            ["sub", ["var", "n"], 1],
                            ["add", ["var", "acc"], 1],
                        ],
                    ],
                ],
            ]
        ],
        ["call", ["var", "loop"], 2000, 0],
    ]
    got = eval_expr(expr, subject=None, limits=SpecLangLimits(max_steps=50000, timeout_ms=0))
    assert got == 2000


def test_spec_lang_non_tail_recursion_hits_budget_deterministically() -> None:
    expr = [
        "let",
        [
            [
                "sum",
                [
                    "fn",
                    ["n"],
                    [
                        "if",
                        ["eq", ["var", "n"], 0],
                        0,
                        ["add", 1, ["call", ["var", "sum"], ["sub", ["var", "n"], 1]]],
                    ],
                ],
            ]
        ],
        ["call", ["var", "sum"], 10_000],
    ]
    with pytest.raises(RuntimeError, match="budget exceeded: steps"):
        eval_expr(expr, subject=None, limits=SpecLangLimits(max_steps=200, timeout_ms=0))


def test_spec_lang_nodes_budget_exceeded() -> None:
    expr = ["and", True, True]
    with pytest.raises(RuntimeError, match="budget exceeded: nodes"):
        eval_expr(expr, subject=None, limits=SpecLangLimits(max_nodes=2, timeout_ms=0))


def test_limits_from_harness_validates_fields() -> None:
    with pytest.raises(TypeError, match="harness.spec_lang.max_steps"):
        limits_from_harness({"spec_lang": {"max_steps": "10"}})
    with pytest.raises(ValueError, match="harness.spec_lang.timeout_ms"):
        limits_from_harness({"spec_lang": {"timeout_ms": -1}})

    limits = limits_from_harness({"spec_lang": {"max_steps": 10, "timeout_ms": 0}})
    assert limits.max_steps == 10
    assert limits.timeout_ms == 0


def test_spec_lang_regex_match_builtin() -> None:
    assert eval_predicate(["regex_match", ["subject"], "^hello"], subject="hello world") is True
    assert eval_predicate(["regex_match", ["subject"], "^bye"], subject="hello world") is False


def test_spec_lang_path_exists_builtin_is_not_supported() -> None:
    with pytest.raises(ValueError, match="unsupported spec_lang symbol: path_exists"):
        eval_predicate(["path_exists", "x"], subject=None)


def test_spec_lang_collection_and_compare_builtins() -> None:
    assert eval_predicate(["lt", 1, 2], subject=None) is True
    assert eval_predicate(["lte", 2, 2], subject=None) is True
    assert eval_predicate(["gt", 3, 2], subject=None) is True
    assert eval_predicate(["gte", 3, 3], subject=None) is True
    assert eval_expr(["count", ["split", "a,b,c", ","]], subject=None) == 3
    assert eval_expr(["join", ["split", "a,b,c", ","], "-"], subject=None) == "a-b-c"
    assert eval_expr(["first", ["split", "1,2,3", ","]], subject=None) == "1"
    assert eval_expr(["rest", ["split", "1,2,3", ","]], subject=None) == ["2", "3"]
    assert eval_predicate(["all", ["split", "x y z"]], subject=None) is True
    assert eval_predicate(["any", ["split", "x  y", " "]], subject=None) is True
    assert eval_predicate(["none", ["split", "", ","]], subject=None) is True
    assert eval_expr(
        ["map", ["fn", ["x"], ["upper", ["var", "x"]]], ["split", "a,b,c", ","]],
        subject=None,
    ) == ["A", "B", "C"]
    assert eval_expr(
        ["filter", ["fn", ["x"], ["matches", ["var", "x"], "^[23]$"]], ["split", "0,1,2,3", ","]],
        subject=None,
    ) == ["2", "3"]
    assert eval_predicate(["matches", "abc-123", "^[a-z]+-[0-9]+$"], subject=None) is True


def test_spec_lang_symbol_bindings() -> None:
    symbols = compile_symbol_bindings(
        {
            "is_warn": ["fn", ["t"], ["contains", ["var", "t"], "WARN"]],
            "is_error": ["fn", ["t"], ["contains", ["var", "t"], "ERROR"]],
        }
    )
    expr = [
        "and",
        ["call", ["var", "is_warn"], ["subject"]],
        ["not", ["call", ["var", "is_error"], ["subject"]]],
    ]
    assert eval_predicate(expr, subject="WARN: hello", symbols=symbols) is True


def test_spec_lang_governance_collection_builtins() -> None:
    rows = [{"name": "c", "value": 3}, {"name": "a", "value": 1}, {"name": "b", "value": 2}]
    assert eval_expr(["sum", ["subject"]], subject=[1, 2, 3]) == 6
    assert eval_expr(["min", ["subject"]], subject=[3, 1, 2]) == 1
    assert eval_expr(["max", ["subject"]], subject=[3, 1, 2]) == 3
    assert eval_expr(["distinct", ["split", "a,a,b,a", ","]], subject=None) == ["a", "b"]
    assert eval_predicate(["is_empty", ["subject"]], subject=[]) is True
    assert eval_expr(["coalesce", None, "", "x"], subject=None) == "x"
    assert eval_expr(["pluck", ["subject"], "name"], subject=rows) == ["c", "a", "b"]
    assert eval_expr(["pluck", ["sort_by", ["subject"], "name"], "name"], subject=rows) == ["a", "b", "c"]
    assert eval_predicate(["matches_all", "abc-123", ["subject"]], subject=["^[a-z]+", "123$"]) is True


def test_spec_lang_set_algebra_and_deep_equals() -> None:
    left = ["json_parse", '[{"k":1},{"k":2},{"k":2},{"k":3}]']
    right = ["json_parse", '[{"k":2},{"k":4},{"k":1}]']
    assert eval_expr(["intersection", left, right], subject=None) == [{"k": 1}, {"k": 2}]
    assert eval_expr(["union", left, right], subject=None) == [{"k": 1}, {"k": 2}, {"k": 3}, {"k": 4}]
    assert eval_expr(["difference", left, right], subject=None) == [{"k": 3}]
    assert eval_expr(["symmetric_difference", left, right], subject=None) == [{"k": 3}, {"k": 4}]
    assert (
        eval_predicate(
            ["set_equals", left, ["json_parse", '[{"k":3},{"k":2},{"k":1}]']],
            subject=None,
        )
        is True
    )
    assert eval_predicate(["is_subset", ["json_parse", '[{"k":1},{"k":2}]'], left], subject=None) is True
    assert eval_predicate(["is_superset", left, ["json_parse", '[{"k":1},{"k":3}]']], subject=None) is True
    assert eval_predicate(["includes", left, ["json_parse", '{"k":2}']], subject=None) is True
    assert (
        eval_predicate(
            ["equals", ["json_parse", '{"a":[1,{"b":2}]}'], ["json_parse", '{"a":[1,{"b":2}]}']],
            subject=None,
        )
        is True
    )


def test_spec_lang_currying_and_collection_transforms() -> None:
    assert eval_expr(["call", ["var", "add"], 2], subject=None) != 0
    assert eval_expr(["call", ["call", ["var", "add"], 2], 3], subject=None) == 5
    assert eval_expr(
        ["map", ["call", ["var", "add"], 10], ["json_parse", "[1,2,3]"]],
        subject=None,
    ) == [11, 12, 13]
    assert eval_expr(
        ["filter", ["call", ["var", "lt"], 3], ["json_parse", "[1,2,3,4,5]"]],
        subject=None,
    ) == [4, 5]
    assert eval_expr(
        ["reduce", ["var", "add"], 0, ["json_parse", "[1,2,3,4]"]],
        subject=None,
    ) == 10
    assert eval_expr(["reject", ["call", ["var", "lt"], 2], ["json_parse", "[1,2,3,4]"]], subject=None) == [1, 2]
    assert eval_expr(["find", ["call", ["var", "lt"], 3], ["json_parse", "[1,2,3,4]"]], subject=None) == 4
    assert (
        eval_expr(["partition", ["call", ["var", "lt"], 2], ["json_parse", "[1,2,3,4]"]], subject=None)
        == [[3, 4], [1, 2]]
    )
    assert eval_expr(
        ["group_by", ["fn", ["x"], ["if", ["gt", ["var", "x"], 2], "hi", "lo"]], ["json_parse", "[1,2,3,4]"]],
        subject=None,
    ) == {"lo": [1, 2], "hi": [3, 4]}
    assert eval_expr(
        ["uniq_by", ["fn", ["x"], ["get", ["var", "x"], "k"]], ["json_parse", '[{"k":1},{"k":1},{"k":2}]']],
        subject=None,
    ) == [{"k": 1}, {"k": 2}]
    assert eval_expr(["flatten", ["json_parse", "[1,[2,[3],[]],4]"]], subject=None) == [1, 2, 3, 4]
    assert eval_expr(["concat", ["json_parse", "[1,2]"], ["json_parse", "[3]"]], subject=None) == [1, 2, 3]
    assert eval_expr(["append", 3, ["json_parse", "[1,2]"]], subject=None) == [1, 2, 3]
    assert eval_expr(["prepend", 0, ["json_parse", "[1,2]"]], subject=None) == [0, 1, 2]
    assert eval_expr(["take", 2, ["json_parse", "[1,2,3]"]], subject=None) == [1, 2]
    assert eval_expr(["drop", 2, ["json_parse", "[1,2,3]"]], subject=None) == [3]

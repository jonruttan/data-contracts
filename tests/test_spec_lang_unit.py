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
    expr = ["std.logic.and", ["std.string.contains", "hello"], ["std.string.starts_with", ["std.core.subject"], "hello"]]
    assert eval_predicate(expr, subject="hello world") is True


def test_spec_lang_unknown_symbol_is_schema_error() -> None:
    with pytest.raises(ValueError, match="unsupported spec_lang symbol"):
        eval_expr(["nope", 1], subject="x")


def test_spec_lang_bad_arity_is_schema_error() -> None:
    with pytest.raises(ValueError, match="arity error"):
        eval_expr(["std.logic.not", True, False], subject="x")


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
                        ["std.logic.eq", ["var", "n"], 0],
                        ["var", "acc"],
                        [
                            "call",
                            ["var", "loop"],
                            ["std.math.sub", ["var", "n"], 1],
                            ["std.math.add", ["var", "acc"], 1],
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
                "std.math.sum",
                [
                    "fn",
                    ["n"],
                    [
                        "if",
                        ["std.logic.eq", ["var", "n"], 0],
                        0,
                        ["std.math.add", 1, ["call", ["var", "std.math.sum"], ["std.math.sub", ["var", "n"], 1]]],
                    ],
                ],
            ]
        ],
        ["call", ["var", "std.math.sum"], 10_000],
    ]
    with pytest.raises(RuntimeError, match="budget exceeded: steps"):
        eval_expr(expr, subject=None, limits=SpecLangLimits(max_steps=200, timeout_ms=0))


def test_spec_lang_nodes_budget_exceeded() -> None:
    expr = ["std.logic.and", True, True]
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
    assert eval_predicate(["std.string.regex_match", ["std.core.subject"], "^hello"], subject="hello world") is True
    assert eval_predicate(["std.string.regex_match", ["std.core.subject"], "^bye"], subject="hello world") is False


def test_spec_lang_path_exists_builtin_is_not_supported() -> None:
    with pytest.raises(ValueError, match="unsupported spec_lang symbol: path_exists"):
        eval_predicate(["path_exists", "x"], subject=None)


def test_spec_lang_collection_and_compare_builtins() -> None:
    assert eval_predicate(["std.logic.lt", 1, 2], subject=None) is True
    assert eval_predicate(["std.logic.lte", 2, 2], subject=None) is True
    assert eval_predicate(["std.logic.gt", 3, 2], subject=None) is True
    assert eval_predicate(["std.logic.gte", 3, 3], subject=None) is True
    assert eval_expr(["std.collection.count", ["std.string.split", "a,b,c", ","]], subject=None) == 3
    assert eval_expr(["std.string.join", ["std.string.split", "a,b,c", ","], "-"], subject=None) == "a-b-c"
    assert eval_expr(["std.collection.first", ["std.string.split", "1,2,3", ","]], subject=None) == "1"
    assert eval_expr(["std.collection.rest", ["std.string.split", "1,2,3", ","]], subject=None) == ["2", "3"]
    assert eval_predicate(["std.collection.all", ["std.string.split", "x y z"]], subject=None) is True
    assert eval_predicate(["std.collection.any", ["std.string.split", "x  y", " "]], subject=None) is True
    assert eval_predicate(["std.collection.none", ["std.string.split", "", ","]], subject=None) is True
    assert eval_expr(
        ["std.collection.map", ["fn", ["x"], ["std.string.upper", ["var", "x"]]], ["std.string.split", "a,b,c", ","]],
        subject=None,
    ) == ["A", "B", "C"]
    assert eval_expr(
        ["std.collection.filter", ["fn", ["x"], ["std.string.matches", ["var", "x"], "^[23]$"]], ["std.string.split", "0,1,2,3", ","]],
        subject=None,
    ) == ["2", "3"]
    assert eval_predicate(["std.string.matches", "abc-123", "^[a-z]+-[0-9]+$"], subject=None) is True


def test_spec_lang_symbol_bindings() -> None:
    symbols = compile_symbol_bindings(
        {
            "is_warn": ["fn", ["t"], ["std.string.contains", ["var", "t"], "WARN"]],
            "is_error": ["fn", ["t"], ["std.string.contains", ["var", "t"], "ERROR"]],
        }
    )
    expr = [
        "std.logic.and",
        ["call", ["var", "is_warn"], ["std.core.subject"]],
        ["std.logic.not", ["call", ["var", "is_error"], ["std.core.subject"]]],
    ]
    assert eval_predicate(expr, subject="WARN: hello", symbols=symbols) is True


def test_spec_lang_governance_collection_builtins() -> None:
    rows = [{"name": "c", "value": 3}, {"name": "a", "value": 1}, {"name": "b", "value": 2}]
    assert eval_expr(["std.math.sum", ["std.core.subject"]], subject=[1, 2, 3]) == 6
    assert eval_expr(["std.math.min", ["std.core.subject"]], subject=[3, 1, 2]) == 1
    assert eval_expr(["std.math.max", ["std.core.subject"]], subject=[3, 1, 2]) == 3
    assert eval_expr(["std.collection.distinct", ["std.string.split", "a,a,b,a", ","]], subject=None) == ["a", "b"]
    assert eval_predicate(["std.collection.is_empty", ["std.core.subject"]], subject=[]) is True
    assert eval_expr(["std.null.coalesce", None, "", "x"], subject=None) == "x"
    assert eval_expr(["std.object.pluck", ["std.core.subject"], "name"], subject=rows) == ["c", "a", "b"]
    assert eval_expr(["std.object.pluck", ["std.collection.sort_by", ["std.core.subject"], "name"], "name"], subject=rows) == ["a", "b", "c"]
    assert eval_predicate(["std.string.matches_all", "abc-123", ["std.core.subject"]], subject=["^[a-z]+", "123$"]) is True
    assert eval_predicate(["std.type.is_null", None], subject=None) is True
    assert eval_predicate(["std.type.is_bool", True], subject=None) is True
    assert eval_predicate(["std.type.is_boolean", True], subject=None) is True
    assert eval_predicate(["std.type.is_number", 3.14], subject=None) is True
    assert eval_predicate(["std.type.is_string", "x"], subject=None) is True
    assert eval_predicate(["std.type.is_list", ["std.json.parse", "[1,2]"]], subject=None) is True
    assert eval_predicate(["std.type.is_array", ["std.json.parse", "[1,2]"]], subject=None) is True
    assert eval_predicate(["std.type.is_dict", ["std.json.parse", '{"a":1}']], subject=None) is True
    assert eval_predicate(["std.type.is_object", ["std.json.parse", '{"a":1}']], subject=None) is True
    assert eval_predicate(["std.type.json_type", ["std.json.parse", "[1,2]"], "array"], subject=None) is True
    assert eval_predicate(["std.type.json_type", ["std.json.parse", '{"a":1}'], "object"], subject=None) is True
    assert eval_predicate(["std.type.json_type", True, "boolean"], subject=None) is True


def test_spec_lang_set_algebra_and_deep_equals() -> None:
    left = ["std.json.parse", '[{"k":1},{"k":2},{"k":2},{"k":3}]']
    right = ["std.json.parse", '[{"k":2},{"k":4},{"k":1}]']
    assert eval_expr(["std.set.intersection", left, right], subject=None) == [{"k": 1}, {"k": 2}]
    assert eval_expr(["std.set.union", left, right], subject=None) == [{"k": 1}, {"k": 2}, {"k": 3}, {"k": 4}]
    assert eval_expr(["std.set.difference", left, right], subject=None) == [{"k": 3}]
    assert eval_expr(["std.set.symmetric_difference", left, right], subject=None) == [{"k": 3}, {"k": 4}]
    assert (
        eval_predicate(
            ["std.set.set_equals", left, ["std.json.parse", '[{"k":3},{"k":2},{"k":1}]']],
            subject=None,
        )
        is True
    )
    assert eval_predicate(["std.set.is_subset", ["std.json.parse", '[{"k":1},{"k":2}]'], left], subject=None) is True
    assert eval_predicate(["std.set.is_superset", left, ["std.json.parse", '[{"k":1},{"k":3}]']], subject=None) is True
    assert eval_predicate(["std.collection.includes", left, ["std.json.parse", '{"k":2}']], subject=None) is True
    assert (
        eval_predicate(
            ["std.logic.equals", ["std.json.parse", '{"a":[1,{"b":2}]}'], ["std.json.parse", '{"a":[1,{"b":2}]}']],
            subject=None,
        )
        is True
    )


def test_spec_lang_currying_and_collection_transforms() -> None:
    assert eval_expr(["call", ["var", "std.math.add"], 2], subject=None) != 0
    assert eval_expr(["call", ["call", ["var", "std.math.add"], 2], 3], subject=None) == 5
    assert eval_expr(
        ["std.collection.map", ["call", ["var", "std.math.add"], 10], ["std.json.parse", "[1,2,3]"]],
        subject=None,
    ) == [11, 12, 13]
    assert eval_expr(
        ["std.collection.filter", ["call", ["var", "std.logic.lt"], 3], ["std.json.parse", "[1,2,3,4,5]"]],
        subject=None,
    ) == [4, 5]
    assert eval_expr(
        ["std.collection.reduce", ["var", "std.math.add"], 0, ["std.json.parse", "[1,2,3,4]"]],
        subject=None,
    ) == 10
    assert eval_expr(["std.collection.reject", ["call", ["var", "std.logic.lt"], 2], ["std.json.parse", "[1,2,3,4]"]], subject=None) == [1, 2]
    assert eval_expr(["std.collection.find", ["call", ["var", "std.logic.lt"], 3], ["std.json.parse", "[1,2,3,4]"]], subject=None) == 4
    assert (
        eval_expr(["std.collection.partition", ["call", ["var", "std.logic.lt"], 2], ["std.json.parse", "[1,2,3,4]"]], subject=None)
        == [[3, 4], [1, 2]]
    )
    assert eval_expr(
        ["std.collection.group_by", ["fn", ["x"], ["if", ["std.logic.gt", ["var", "x"], 2], "hi", "lo"]], ["std.json.parse", "[1,2,3,4]"]],
        subject=None,
    ) == {"lo": [1, 2], "hi": [3, 4]}
    assert eval_expr(
        ["std.collection.uniq_by", ["fn", ["x"], ["std.object.get", ["var", "x"], "k"]], ["std.json.parse", '[{"k":1},{"k":1},{"k":2}]']],
        subject=None,
    ) == [{"k": 1}, {"k": 2}]
    assert eval_expr(["std.collection.flatten", ["std.json.parse", "[1,[2,[3],[]],4]"]], subject=None) == [1, 2, 3, 4]
    assert eval_expr(["std.collection.concat", ["std.json.parse", "[1,2]"], ["std.json.parse", "[3]"]], subject=None) == [1, 2, 3]
    assert eval_expr(["std.collection.append", 3, ["std.json.parse", "[1,2]"]], subject=None) == [1, 2, 3]
    assert eval_expr(["std.collection.prepend", 0, ["std.json.parse", "[1,2]"]], subject=None) == [0, 1, 2]
    assert eval_expr(["std.collection.take", 2, ["std.json.parse", "[1,2,3]"]], subject=None) == [1, 2]
    assert eval_expr(["std.collection.drop", 2, ["std.json.parse", "[1,2,3]"]], subject=None) == [3]


def test_spec_lang_full_suite_builtins_are_pure_and_deterministic() -> None:
    assert eval_expr(["std.math.mul", 3, 4], subject=None) == 12
    assert eval_expr(["std.math.div", 9, 2], subject=None) == 4.5
    assert eval_expr(["std.math.mod", 9, 4], subject=None) == 1
    assert eval_expr(["std.math.pow", 2, 5], subject=None) == 32
    assert eval_expr(["std.math.abs", -7], subject=None) == 7
    assert eval_expr(["std.math.negate", 3], subject=None) == -3
    assert eval_expr(["std.math.inc", 3], subject=None) == 4
    assert eval_expr(["std.math.dec", 3], subject=None) == 2
    assert eval_expr(["std.math.clamp", 1, 5, 9], subject=None) == 5
    assert eval_expr(["std.math.round", 2.5], subject=None) == 3
    assert eval_expr(["std.math.floor", 2.9], subject=None) == 2
    assert eval_expr(["std.math.ceil", 2.1], subject=None) == 3
    assert eval_expr(["std.logic.compare", 1, 2], subject=None) == -1
    assert eval_predicate(["std.logic.between", 1, 3, 2], subject=None) is True
    assert eval_predicate(["std.logic.xor", True, False], subject=None) is True
    assert eval_expr(["std.collection.slice", 1, 3, ["std.json.parse", "[0,1,2,3]"]], subject=None) == [1, 2]
    assert eval_expr(["std.collection.reverse", ["std.json.parse", "[1,2,3]"]], subject=None) == [3, 2, 1]
    assert eval_expr(["std.collection.zip", ["std.json.parse", "[1,2,3]"], ["std.json.parse", "[4,5]"]], subject=None) == [
        [1, 4],
        [2, 5],
    ]
    assert eval_expr(
        ["std.collection.zip_with", ["var", "std.math.add"], ["std.json.parse", "[1,2,3]"], ["std.json.parse", "[4,5,6]"]],
        subject=None,
    ) == [5, 7, 9]
    assert eval_expr(["std.math.range", 2, 5], subject=None) == [2, 3, 4]
    assert eval_expr(["std.collection.repeat", "x", 3], subject=None) == ["x", "x", "x"]
    assert eval_expr(["std.object.keys", ["std.json.parse", '{"a":1,"b":2}']], subject=None) == ["a", "b"]
    assert eval_expr(["std.object.values", ["std.json.parse", '{"a":1,"b":2}']], subject=None) == [1, 2]
    assert eval_expr(["std.object.entries", ["std.json.parse", '{"a":1}']], subject=None) == [["a", 1]]
    assert eval_expr(["std.object.merge", ["std.json.parse", '{"a":1}'], ["std.json.parse", '{"b":2}']], subject=None) == {
        "a": 1,
        "b": 2,
    }
    assert eval_expr(["std.object.assoc", "b", 2, ["std.json.parse", '{"a":1}']], subject=None) == {"a": 1, "b": 2}
    assert eval_expr(["std.object.dissoc", "a", ["std.json.parse", '{"a":1,"b":2}']], subject=None) == {"b": 2}
    assert eval_expr(["std.object.pick", ["std.json.parse", '["a"]'], ["std.json.parse", '{"a":1,"b":2}']], subject=None) == {"a": 1}
    assert eval_expr(["std.object.omit", ["std.json.parse", '["a"]'], ["std.json.parse", '{"a":1,"b":2}']], subject=None) == {"b": 2}
    assert eval_predicate(["std.object.prop_eq", "a", 1, ["std.json.parse", '{"a":1}']], subject=None) is True
    assert (
        eval_expr(
            ["std.object.where", ["std.json.parse", '{"a":1}'], ["std.json.parse", '{"a":1,"b":2}']],
            subject=None,
        )
        is True
    )
    assert eval_expr(["std.fn.compose", ["call", ["var", "std.math.add"], 1], ["call", ["var", "std.math.mul"], 2], 3], subject=None) == 7
    assert eval_expr(["std.fn.pipe", ["call", ["var", "std.math.mul"], 2], ["call", ["var", "std.math.add"], 1], 3], subject=None) == 7
    assert eval_expr(["std.fn.identity", "x"], subject=None) == "x"
    assert eval_expr(["call", ["call", ["var", "std.fn.always"], "k"], 999], subject=None) == "k"
    assert eval_expr(["std.string.replace", "a-b-c", "-", ":"], subject=None) == "a:b:c"
    assert eval_expr(["std.string.pad_left", "7", 3, "0"], subject=None) == "007"
    assert eval_expr(["std.string.pad_right", "7", 3, "0"], subject=None) == "700"

    with pytest.raises(ValueError, match="spec_lang mod expects integer args"):
        eval_expr(["std.math.mod", 1.5, 2], subject=None)

# SPEC-OPT-OUT: Exercises evaluator internals and budget semantics not yet fully representable as stable .spec.md fixtures.
from __future__ import annotations

import pytest

from spec_runner.spec_lang import SpecLangLimits, eval_expr, eval_predicate, limits_from_harness


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


def test_spec_lang_path_exists_builtin(tmp_path) -> None:
    p = tmp_path / "x.txt"
    p.write_text("ok", encoding="utf-8")
    assert eval_predicate(["path_exists", str(p)], subject=None) is True
    assert eval_predicate(["path_exists", str(tmp_path / "missing.txt")], subject=None) is False

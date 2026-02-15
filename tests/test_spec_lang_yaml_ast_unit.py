# SPEC-OPT-OUT: Unit checks for mapping-AST compiler edge-cases and path diagnostics.
from __future__ import annotations

import pytest

from spec_runner.spec_lang_yaml_ast import (
    SpecLangYamlAstError,
    compile_yaml_expr_list,
    compile_yaml_expr_to_sexpr,
    sexpr_to_yaml_ast,
)


def test_compile_operator_mapping_happy_path() -> None:
    expr = {"contains": [{"var": "subject"}, "ok"]}
    assert compile_yaml_expr_to_sexpr(expr, field_path="x") == ["contains", ["var", "subject"], "ok"]


def test_compile_var_subject_happy_path() -> None:
    expr = {"contains": [{"var": "subject"}, "ok"]}
    assert compile_yaml_expr_to_sexpr(expr, field_path="x") == ["contains", ["var", "subject"], "ok"]


def test_compile_subject_mapping_form() -> None:
    expr = {"contains": [{"subject": []}, "ok"]}
    assert compile_yaml_expr_to_sexpr(expr, field_path="x") == ["contains", ["subject"], "ok"]


def test_compile_bare_subject_is_literal_string() -> None:
    expr = {"eq": ["subject", "subject"]}
    assert compile_yaml_expr_to_sexpr(expr, field_path="x") == ["eq", "subject", "subject"]


def test_reverse_conversion_emits_var_subject() -> None:
    assert sexpr_to_yaml_ast(["subject"]) == {"var": "subject"}


def test_compile_lit_wrapped_list_and_map() -> None:
    assert compile_yaml_expr_to_sexpr({"lit": [1, 2, 3]}, field_path="x") == [1, 2, 3]
    assert compile_yaml_expr_to_sexpr({"lit": {"k": 1}}, field_path="x") == {"k": 1}


def test_rejects_multi_key_mapping() -> None:
    with pytest.raises(SpecLangYamlAstError, match="exactly one operator key"):
        compile_yaml_expr_to_sexpr({"contains": ["x"], "eq": [1, 1]}, field_path="x")


def test_rejects_raw_literal_list_without_lit() -> None:
    with pytest.raises(SpecLangYamlAstError, match="list expressions are not allowed"):
        compile_yaml_expr_to_sexpr(["contains", "x"], field_path="x")


def test_rejects_non_list_operator_args() -> None:
    with pytest.raises(SpecLangYamlAstError, match="operator args must be a list"):
        compile_yaml_expr_to_sexpr({"contains": None}, field_path="x")


def test_ref_and_var_list_forms_compile_without_special_rejection() -> None:
    assert compile_yaml_expr_to_sexpr({"ref": ["subject"]}, field_path="x") == ["ref", "subject"]
    with pytest.raises(SpecLangYamlAstError, match="variable name must be a non-empty string"):
        compile_yaml_expr_to_sexpr({"var": ["subject"]}, field_path="x")


def test_compile_fn_uses_plain_param_list_shape() -> None:
    expr = {
        "fn": [
            ["row"],
            {"gt": [{"count": [{"get": [{"var": "row"}, "non_evaluate_ops"]}]}, 0]},
        ]
    }
    assert compile_yaml_expr_to_sexpr(expr, field_path="x") == [
        "fn",
        ["row"],
        ["gt", ["count", ["get", ["var", "row"], "non_evaluate_ops"]], 0],
    ]


def test_reject_legacy_fn_param_node_shapes() -> None:
    with pytest.raises(SpecLangYamlAstError, match="params must be a list"):
        compile_yaml_expr_to_sexpr({"fn": [{"lit": ["row"]}, {"var": "row"}]}, field_path="x")
    with pytest.raises(SpecLangYamlAstError, match="must be a non-empty string"):
        compile_yaml_expr_to_sexpr({"fn": [[None], {"var": "row"}]}, field_path="x")


def test_rejects_empty_expression_list() -> None:
    with pytest.raises(SpecLangYamlAstError, match="must be a non-empty list"):
        compile_yaml_expr_list([], field_path="x")

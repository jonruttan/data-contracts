import pytest

from spec_runner.assertions import (
    assert_stdout_path_exists,
    eval_assert_tree,
    first_nonempty_line,
    iter_leaf_assertions,
)


def test_first_nonempty_line_empty():
    assert first_nonempty_line("") == ""
    assert first_nonempty_line("\n \n\t\n") == ""


def test_first_nonempty_line_strips():
    assert first_nonempty_line("\n  a \n b\n") == "a"


def test_assert_stdout_path_exists(tmp_path):
    p = tmp_path / "x.md"
    p.write_text("x", encoding="utf-8")
    out = f"\n{p}\n"
    assert_stdout_path_exists(out, suffix=".md")


def test_iter_leaf_assertions_requires_mapping_target_and_op_key():
    with pytest.raises(TypeError, match="assert leaf must be a mapping"):
        list(iter_leaf_assertions(["nope"]))
    with pytest.raises(ValueError, match="missing required key: target"):
        list(iter_leaf_assertions({"contains": ["x"]}))
    with pytest.raises(ValueError, match="missing an op key"):
        list(iter_leaf_assertions({"target": "stderr"}))


def test_iter_leaf_assertions_requires_list_values_and_rejects_legacy():
    with pytest.raises(TypeError, match="must be a list"):
        list(iter_leaf_assertions({"target": "stderr", "contains": "x"}))
    with pytest.raises(ValueError, match="legacy assertion shape"):
        list(iter_leaf_assertions({"target": "stderr", "op": "contains", "value": "x"}))
    with pytest.raises(ValueError, match="unsupported op"):
        list(iter_leaf_assertions({"target": "stderr", "wat": ["x"]}))
    with pytest.raises(ValueError, match="must not include 'any' or 'all'"):
        list(iter_leaf_assertions({"target": "stderr", "any": []}))


def test_iter_leaf_assertions_happy_path():
    assert list(
        iter_leaf_assertions(
            {"target": "stderr", "contains": ["ok"], "not_contains": ["ERROR:", "nope"], "regex": ["x.*"]}
        )
    ) == [
        ("stderr", "contains", "ok"),
        ("stderr", "not_contains", "ERROR:"),
        ("stderr", "not_contains", "nope"),
        ("stderr", "regex", "x.*"),
    ]


def test_eval_assert_tree_all_list_is_and():
    seen = []

    def leaf(x):
        seen.append(x["name"])
        assert x["ok"] is True

    eval_assert_tree([{"name": "a", "ok": True}, {"name": "b", "ok": True}], eval_leaf=leaf)
    assert seen == ["a", "b"]


def test_eval_assert_tree_any_is_or():
    seen = []

    def leaf(x):
        seen.append(x["name"])
        assert x["ok"] is True

    eval_assert_tree({"any": [{"name": "a", "ok": False}, {"name": "b", "ok": True}]}, eval_leaf=leaf)
    assert seen == ["a", "b"]


def test_eval_assert_tree_any_all_fail_raises_helpful_error():
    def leaf(x):
        assert False, x["msg"]

    with pytest.raises(AssertionError, match="all 'any' branches failed"):
        eval_assert_tree({"any": [{"msg": "nope1"}, {"msg": "nope2"}]}, eval_leaf=leaf)


def test_eval_assert_tree_all_and_any_can_coexist_in_one_node():
    seen = []

    def leaf(x):
        seen.append(x["name"])
        assert x["ok"] is True

    eval_assert_tree(
        {
            "all": [{"name": "a", "ok": True}],
            "any": [{"name": "b", "ok": False}, {"name": "c", "ok": True}],
        },
        eval_leaf=leaf,
    )
    assert seen == ["a", "b", "c"]


def test_eval_assert_tree_all_only_does_not_evaluate_leaf():
    seen = []

    def leaf(x):
        seen.append(x["name"])

    eval_assert_tree({"all": [{"name": "a"}]}, eval_leaf=leaf)
    assert seen == ["a"]


def test_eval_assert_tree_group_rejects_extra_keys():
    with pytest.raises(ValueError, match="unknown key in assert group"):
        eval_assert_tree({"any": [], "wat": 1}, eval_leaf=lambda _x: None)

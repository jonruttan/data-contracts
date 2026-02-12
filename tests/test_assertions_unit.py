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
    with pytest.raises(TypeError, match="key 'is' must be a bool"):
        list(iter_leaf_assertions({"target": "stderr", "contains": ["x"], "is": "yes"}))
    with pytest.raises(ValueError, match="legacy assertion shape"):
        list(iter_leaf_assertions({"target": "stderr", "op": "contains", "value": "x"}))
    with pytest.raises(ValueError, match="unsupported op"):
        list(iter_leaf_assertions({"target": "stderr", "wat": ["x"]}))
    with pytest.raises(ValueError, match="must not include group keys"):
        list(iter_leaf_assertions({"target": "stderr", "any": []}))
    with pytest.raises(ValueError, match="unsupported op: not_contains"):
        list(iter_leaf_assertions({"target": "stderr", "not_contains": ["x"]}))
    with pytest.raises(ValueError, match="unsupported op: not_regex"):
        list(iter_leaf_assertions({"target": "stderr", "not_regex": ["x"]}))


def test_iter_leaf_assertions_happy_path_with_is_false():
    assert list(
        iter_leaf_assertions(
            {
                "target": "stderr",
                "contain": ["ok"],
                "regex": ["x.*"],
                "is": False,
            }
        )
    ) == [
        ("stderr", "contain", "ok", False),
        ("stderr", "regex", "x.*", False),
    ]


def test_iter_leaf_assertions_accepts_target_override():
    assert list(iter_leaf_assertions({"contain": ["ok"]}, target_override="stderr")) == [
        ("stderr", "contain", "ok", True),
    ]


def test_iter_leaf_assertions_contains_alias_canonicalizes_to_contain():
    assert list(iter_leaf_assertions({"target": "stderr", "contains": ["ok"]})) == [
        ("stderr", "contain", "ok", True),
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

    with pytest.raises(AssertionError, match="all 'can/any' branches failed"):
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


def test_eval_assert_tree_group_target_inherited_by_children():
    seen = []

    def leaf(x, *, inherited_target=None):
        for target, op, value, is_true in iter_leaf_assertions(x, target_override=inherited_target):
            seen.append((target, op, value, is_true))

    eval_assert_tree(
        {
            "target": "stderr",
            "must": [
                {"contain": ["WARN:"]},
                {"regex": ["boom"], "is": False},
            ],
        },
        eval_leaf=leaf,
    )
    assert seen == [
        ("stderr", "contain", "WARN:", True),
        ("stderr", "regex", "boom", False),
    ]


def test_eval_assert_tree_child_target_overrides_group_target():
    seen = []

    def leaf(x, *, inherited_target=None):
        for target, op, value, is_true in iter_leaf_assertions(x, target_override=inherited_target):
            seen.append((target, op, value, is_true))

    eval_assert_tree(
        {
            "target": "stderr",
            "must": [
                {"contain": ["WARN:"]},
                {"target": "stdout", "contain": ["ok"]},
            ],
        },
        eval_leaf=leaf,
    )
    assert seen == [
        ("stderr", "contain", "WARN:", True),
        ("stdout", "contain", "ok", True),
    ]


def test_eval_assert_tree_missing_target_without_inheritance_raises():
    with pytest.raises(ValueError, match="missing required key: target"):
        eval_assert_tree(
            {"all": [{"contains": ["x"]}]},
            eval_leaf=lambda x: list(iter_leaf_assertions(x)),
        )


def test_eval_assert_tree_cannot_requires_all_children_to_fail():
    seen = []

    def leaf(x):
        seen.append(x["name"])
        assert x["ok"] is True

    eval_assert_tree(
        {"cannot": [{"name": "a", "ok": False}, {"name": "b", "ok": False}]},
        eval_leaf=leaf,
    )
    assert seen == ["a", "b"]


def test_eval_assert_tree_cannot_fails_if_any_child_passes():
    def leaf(x):
        assert x["ok"] is True

    with pytest.raises(AssertionError, match="'cannot' failed"):
        eval_assert_tree(
            {"cannot": [{"ok": False}, {"ok": True}]},
            eval_leaf=leaf,
        )

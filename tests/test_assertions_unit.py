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
    with pytest.raises(ValueError, match="requires inherited target"):
        list(iter_leaf_assertions({"contain": ["x"]}))
    with pytest.raises(ValueError, match="must not include key: target"):
        list(iter_leaf_assertions({"target": "stderr"}))


def test_iter_leaf_assertions_requires_list_values_and_rejects_legacy():
    with pytest.raises(ValueError, match="must not include key: target"):
        list(iter_leaf_assertions({"target": "stderr", "contain": ["x"]}, target_override="stderr"))
    with pytest.raises(TypeError, match="must be a list"):
        list(iter_leaf_assertions({"contain": "x"}, target_override="stderr"))
    with pytest.raises(ValueError, match="key 'is' is not supported"):
        list(iter_leaf_assertions({"contain": ["x"], "is": False}, target_override="stderr"))
    with pytest.raises(ValueError, match="legacy assertion shape"):
        list(iter_leaf_assertions({"op": "contains", "value": "x"}, target_override="stderr"))
    with pytest.raises(ValueError, match="unsupported op"):
        list(iter_leaf_assertions({"wat": ["x"]}, target_override="stderr"))
    with pytest.raises(ValueError, match="must not include group keys"):
        list(iter_leaf_assertions({"any": []}, target_override="stderr"))
    with pytest.raises(ValueError, match="unsupported op: not_contains"):
        list(iter_leaf_assertions({"not_contains": ["x"]}, target_override="stderr"))
    with pytest.raises(ValueError, match="unsupported op: not_regex"):
        list(iter_leaf_assertions({"not_regex": ["x"]}, target_override="stderr"))


def test_iter_leaf_assertions_happy_path():
    assert list(
        iter_leaf_assertions(
            {
                "contain": ["ok"],
                "regex": ["x.*"],
            },
            target_override="stderr",
        )
    ) == [
        ("stderr", "contain", "ok", True),
        ("stderr", "regex", "x.*", True),
    ]


def test_iter_leaf_assertions_accepts_target_override():
    assert list(iter_leaf_assertions({"contain": ["ok"]}, target_override="stderr")) == [
        ("stderr", "contain", "ok", True),
    ]


def test_iter_leaf_assertions_rejects_contains_alias():
    with pytest.raises(ValueError, match="unsupported op: contains"):
        list(iter_leaf_assertions({"contains": ["ok"]}, target_override="stderr"))


def test_eval_assert_tree_list_is_and():
    seen = []

    def leaf(x):
        seen.append(x["name"])
        assert x["ok"] is True

    eval_assert_tree([{"name": "a", "ok": True}, {"name": "b", "ok": True}], eval_leaf=leaf)
    assert seen == ["a", "b"]


def test_eval_assert_tree_can_is_or():
    seen = []

    def leaf(x):
        seen.append(x["name"])
        assert x["ok"] is True

    eval_assert_tree({"can": [{"name": "a", "ok": False}, {"name": "b", "ok": True}]}, eval_leaf=leaf)
    assert seen == ["a", "b"]


def test_eval_assert_tree_can_all_fail_raises_helpful_error():
    def leaf(x):
        assert False, x["msg"]

    with pytest.raises(AssertionError, match="all 'can' branches failed"):
        eval_assert_tree({"can": [{"msg": "nope1"}, {"msg": "nope2"}]}, eval_leaf=leaf)


def test_eval_assert_tree_must_and_can_can_coexist_in_one_node():
    seen = []

    def leaf(x):
        seen.append(x["name"])
        assert x["ok"] is True

    eval_assert_tree(
        {
            "must": [{"name": "a", "ok": True}],
            "can": [{"name": "b", "ok": False}, {"name": "c", "ok": True}],
        },
        eval_leaf=leaf,
    )
    assert seen == ["a", "b", "c"]


def test_eval_assert_tree_must_only_does_not_evaluate_leaf():
    seen = []

    def leaf(x):
        seen.append(x["name"])

    eval_assert_tree({"must": [{"name": "a"}]}, eval_leaf=leaf)
    assert seen == ["a"]


def test_eval_assert_tree_group_rejects_extra_keys():
    with pytest.raises(ValueError, match="unknown key in assert group"):
        eval_assert_tree({"can": [], "wat": 1}, eval_leaf=lambda _x: None)


def test_eval_assert_tree_rejects_legacy_group_aliases():
    with pytest.raises(ValueError, match="aliases 'all'/'any' are not supported"):
        eval_assert_tree({"all": []}, eval_leaf=lambda _x: None)
    with pytest.raises(ValueError, match="aliases 'all'/'any' are not supported"):
        eval_assert_tree({"any": []}, eval_leaf=lambda _x: None)


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
                {"regex": ["boom"]},
            ],
        },
        eval_leaf=leaf,
    )
    assert seen == [
        ("stderr", "contain", "WARN:", True),
        ("stderr", "regex", "boom", True),
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
                {"target": "stdout", "must": [{"contain": ["ok"]}]},
            ],
        },
        eval_leaf=leaf,
    )
    assert seen == [
        ("stderr", "contain", "WARN:", True),
        ("stdout", "contain", "ok", True),
    ]


def test_eval_assert_tree_missing_target_without_inheritance_raises():
    with pytest.raises(ValueError, match="requires inherited target"):
        eval_assert_tree(
            {"must": [{"contain": ["x"]}]},
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

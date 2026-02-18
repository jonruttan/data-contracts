# SPEC-OPT-OUT: Exercises behavior not yet representable as stable .spec.md coverage (unit-level API/diagnostic/infrastructure checks).
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
    with pytest.raises(TypeError, match="contract leaf must be a mapping"):
        list(iter_leaf_assertions(["nope"]))
    with pytest.raises(ValueError, match="requires inherited target"):
        list(iter_leaf_assertions({"std.logic.eq": [1, 1]}))
    with pytest.raises(ValueError, match="must not include key: target"):
        list(iter_leaf_assertions({"target": "stderr"}))


def test_iter_leaf_assertions_rejects_unsupported_shapes():
    with pytest.raises(ValueError, match="must not include key: target"):
        list(iter_leaf_assertions({"target": "stderr", "std.logic.eq": [1, 1]}, target_override="stderr"))
    with pytest.raises(ValueError, match="must not include group keys"):
        list(iter_leaf_assertions({"must": []}, target_override="stderr"))


def test_iter_leaf_assertions_happy_path():
    assert list(
        iter_leaf_assertions(
            {
                "std.string.contains": [{"var": "subject"}, "ok"],
            },
            target_override="stderr",
        )
    ) == [
        ("stderr", "evaluate", {"std.string.contains": [{"var": "subject"}, "ok"]}, True),
    ]


def test_iter_leaf_assertions_accepts_target_override():
    assert list(iter_leaf_assertions({"std.string.contains": [{"var": "subject"}, "ok"]}, target_override="stderr")) == [
        ("stderr", "evaluate", {"std.string.contains": [{"var": "subject"}, "ok"]}, True),
    ]


def test_iter_leaf_assertions_allows_unknown_operator_for_compiler_stage_validation():
    assert list(iter_leaf_assertions({"unknown_op": ["ok"]}, target_override="stderr")) == [
        ("stderr", "evaluate", {"unknown_op": ["ok"]}, True),
    ]


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


def test_eval_assert_tree_group_rejects_multiple_group_keys():
    with pytest.raises(ValueError, match="exactly one key"):
        eval_assert_tree(
            {
                "must": [{"name": "a", "ok": True}],
                "can": [{"name": "b", "ok": False}, {"name": "c", "ok": True}],
            },
            eval_leaf=lambda _x: None,
        )


def test_eval_assert_tree_must_only_does_not_evaluate_leaf():
    seen = []

    def leaf(x):
        seen.append(x["name"])

    eval_assert_tree({"must": [{"name": "a"}]}, eval_leaf=leaf)
    assert seen == ["a"]


def test_eval_assert_tree_group_rejects_extra_keys():
    with pytest.raises(ValueError, match="unknown key in contract group"):
        eval_assert_tree({"can": [], "wat": 1}, eval_leaf=lambda _x: None)


def test_eval_assert_tree_group_rejects_empty_children():
    with pytest.raises(ValueError, match="must not be empty"):
        eval_assert_tree({"must": []}, eval_leaf=lambda _x: None)
    with pytest.raises(ValueError, match="must not be empty"):
        eval_assert_tree({"can": []}, eval_leaf=lambda _x: None)
    with pytest.raises(ValueError, match="must not be empty"):
        eval_assert_tree({"cannot": []}, eval_leaf=lambda _x: None)


def test_eval_assert_tree_group_target_inherited_by_children():
    seen = []

    def leaf(x, *, inherited_target=None):
        for target, op, value, is_true in iter_leaf_assertions(x, target_override=inherited_target):
            seen.append((target, op, value, is_true))

    eval_assert_tree(
        {
            "target": "stderr",
            "must": [
                {"std.string.contains": [{"var": "subject"}, "WARN:"]},
                {"std.string.regex_match": [{"var": "subject"}, "boom"]},
            ],
        },
        eval_leaf=leaf,
    )
    assert seen == [
        ("stderr", "evaluate", {"std.string.contains": [{"var": "subject"}, "WARN:"]}, True),
        ("stderr", "evaluate", {"std.string.regex_match": [{"var": "subject"}, "boom"]}, True),
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
                {"std.string.contains": [{"var": "subject"}, "WARN:"]},
                {"target": "stdout", "must": [{"std.string.contains": [{"var": "subject"}, "ok"]}]},
            ],
        },
        eval_leaf=leaf,
    )
    assert seen == [
        ("stderr", "evaluate", {"std.string.contains": [{"var": "subject"}, "WARN:"]}, True),
        ("stdout", "evaluate", {"std.string.contains": [{"var": "subject"}, "ok"]}, True),
    ]


def test_eval_assert_tree_missing_target_without_inheritance_raises():
    with pytest.raises(ValueError, match="requires inherited target"):
        eval_assert_tree(
            {"must": [{"std.string.contains": [{"var": "subject"}, "x"]}]},
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

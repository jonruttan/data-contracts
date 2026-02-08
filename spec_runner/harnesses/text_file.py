from spec_runner.assertions import assert_text_op, eval_assert_tree, iter_leaf_assertions


def run(case, *, ctx) -> None:
    t = case.test
    text = case.doc_path.read_text(encoding="utf-8")

    def _eval_leaf(leaf: dict) -> None:
        for target, op, value in iter_leaf_assertions(leaf):
            if target != "text":
                raise ValueError(f"unknown assert target for text.file: {target}")
            assert_text_op(text, op, value)

    eval_assert_tree(t.get("assert", []) or [], eval_leaf=_eval_leaf)

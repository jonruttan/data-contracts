from spec_runner.assertions import assert_text_op, eval_assert_tree, iter_leaf_assertions


def run(case, *, ctx) -> None:
    t = case.test
    # By default, assert against the spec doc that contains the spec-test.
    # If `path` is provided, assert against that file (relative to the spec doc).
    p = case.doc_path
    rel = t.get("path")
    if rel is not None:
        from pathlib import Path

        rel_p = Path(str(rel))
        if rel_p.is_absolute():
            raise ValueError("text.file path must be relative")
        p = (case.doc_path.parent / rel_p).resolve()
    text = p.read_text(encoding="utf-8")

    def _eval_leaf(leaf: dict, *, inherited_target: str | None = None) -> None:
        for target, op, value, is_true in iter_leaf_assertions(leaf, target_override=inherited_target):
            if target != "text":
                raise ValueError(f"unknown assert target for text.file: {target}")
            assert_text_op(text, op, value, is_true=is_true)

    eval_assert_tree(t.get("assert", []) or [], eval_leaf=_eval_leaf)

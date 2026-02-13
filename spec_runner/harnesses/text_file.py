import os
import sys

from spec_runner.assertions import (
    _raise_with_assert_context,
    assert_text_op,
    eval_assert_tree,
    iter_leaf_assertions,
)
from spec_runner.assertion_health import (
    format_assertion_health_error,
    format_assertion_health_warning,
    lint_assert_tree,
    resolve_assert_health_mode,
)


def _runtime_env(ctx) -> dict[str, str]:
    raw_env = getattr(ctx, "env", None)
    if raw_env is None:
        return dict(os.environ)
    return {str(k): str(v) for k, v in raw_env.items()}


def _contract_root_for(doc_path):
    # Use repository/workspace root when detectable; otherwise fallback to the
    # spec document directory for safe defaults in isolated tests.
    p = doc_path.resolve()
    for cur in (p.parent, *p.parent.parents):
        if (cur / ".git").exists():
            return cur
    return p.parent


def run(case, *, ctx) -> None:
    t = case.test
    case_id = str(t.get("id", ""))
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
        root = _contract_root_for(case.doc_path)
        try:
            p.relative_to(root)
        except ValueError as e:
            raise ValueError("text.file path escapes contract root") from e
    text = p.read_text(encoding="utf-8")
    assert_spec = t.get("assert", []) or []
    mode = resolve_assert_health_mode(t, env=_runtime_env(ctx))
    diags = lint_assert_tree(assert_spec)
    if diags and mode == "error":
        raise AssertionError(format_assertion_health_error(diags))
    if diags and mode == "warn":
        for d in diags:
            print(format_assertion_health_warning(d), file=sys.stderr)

    def _eval_leaf(leaf: dict, *, inherited_target: str | None = None, assert_path: str = "assert") -> None:
        for target, op, value, is_true in iter_leaf_assertions(leaf, target_override=inherited_target):
            try:
                if target != "text":
                    raise ValueError(f"unknown assert target for text.file: {target}")
                assert_text_op(text, op, value, is_true=is_true)
            except BaseException as e:  # noqa: BLE001
                _raise_with_assert_context(
                    e,
                    case_id=case_id,
                    assert_path=assert_path,
                    target=target,
                    op=op,
                )

    eval_assert_tree(assert_spec, eval_leaf=_eval_leaf)

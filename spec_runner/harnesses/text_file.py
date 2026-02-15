import os
import sys

from spec_runner.assertions import (
    evaluate_internal_assert_tree,
)
from spec_runner.assertion_health import (
    format_assertion_health_error,
    format_assertion_health_warning,
    lint_assert_tree,
    resolve_assert_health_mode,
)
from spec_runner.compiler import compile_external_case
from spec_runner.spec_lang_libraries import load_spec_lang_symbols_for_case
from spec_runner.spec_lang import limits_from_harness


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
    if hasattr(case, "test") and hasattr(case, "doc_path"):
        case = compile_external_case(case.test, doc_path=case.doc_path)
    t = case.raw_case
    case_id = case.id
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
    spec_lang_limits = limits_from_harness(case.harness)
    spec_lang_symbols = load_spec_lang_symbols_for_case(
        doc_path=case.doc_path,
        harness=case.harness,
        limits=spec_lang_limits,
    )
    mode = resolve_assert_health_mode(t, env=_runtime_env(ctx))
    diags = lint_assert_tree(assert_spec)
    if diags and mode == "error":
        raise AssertionError(format_assertion_health_error(diags))
    if diags and mode == "warn":
        for d in diags:
            print(format_assertion_health_warning(d), file=sys.stderr)

    def _subject_for_key(subject_key: str) -> str:
        if subject_key != "text":
            raise ValueError(f"unknown assert target for text.file: {subject_key}")
        return text

    evaluate_internal_assert_tree(
        case.assert_tree,
        case_id=case_id,
        subject_for_key=_subject_for_key,
        limits=spec_lang_limits,
        symbols=spec_lang_symbols,
    )

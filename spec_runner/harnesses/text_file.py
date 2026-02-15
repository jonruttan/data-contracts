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
from spec_runner.spec_lang import limits_from_harness
from spec_runner.spec_lang_libraries import load_spec_lang_symbols_for_case
from spec_runner.virtual_paths import contract_root_for, resolve_contract_path


def _runtime_env(ctx) -> dict[str, str]:
    raw_env = getattr(ctx, "env", None)
    if raw_env is None:
        return dict(os.environ)
    return {str(k): str(v) for k, v in raw_env.items()}


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
        try:
            p = resolve_contract_path(
                contract_root_for(case.doc_path), str(rel), field="text.file path"
            )
        except ValueError as e:
            raise ValueError(str(e)) from e
    doc_path = case.doc_path.resolve()
    root = contract_root_for(doc_path)
    text = p.read_text(encoding="utf-8")
    text_subject_profile = {
        "profile_id": "text.file/v1",
        "profile_version": 1,
        "value": text,
        "meta": {
            "target": "text",
            "path": "/" + p.resolve().relative_to(root).as_posix().lstrip("/"),
        },
        "context": {
            "source_doc": "/" + doc_path.relative_to(root).as_posix().lstrip("/"),
        },
    }
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

    def _subject_for_key(subject_key: str):
        if subject_key != "text":
            if subject_key == "context_json":
                return text_subject_profile
            raise ValueError(f"unknown assert target for text.file: {subject_key}")
        return text

    evaluate_internal_assert_tree(
        case.assert_tree,
        case_id=case_id,
        subject_for_key=_subject_for_key,
        limits=spec_lang_limits,
        symbols=spec_lang_symbols,
    )

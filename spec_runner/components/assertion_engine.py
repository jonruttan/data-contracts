from __future__ import annotations

import os
import sys
from typing import Any, Callable

from spec_runner.assertion_health import (
    format_assertion_health_error,
    format_assertion_health_warning,
    lint_assert_tree,
    resolve_assert_health_mode,
)
from spec_runner.assertions import evaluate_internal_assert_tree
from spec_runner.components.contracts import HarnessExecutionContext


def runtime_env(ctx) -> dict[str, str]:
    raw_env = getattr(ctx, "env", None)
    if raw_env is None:
        return dict(os.environ)
    return {str(k): str(v) for k, v in raw_env.items()}


def run_assertions_with_context(
    *,
    assert_tree,
    raw_assert_spec: list[Any] | None,
    raw_case: dict[str, Any],
    ctx,
    execution: HarnessExecutionContext,
    subject_for_key: Callable[[str], Any],
) -> None:
    mode = resolve_assert_health_mode(raw_case, env=runtime_env(ctx))
    diags = lint_assert_tree(raw_assert_spec or [])
    if diags and mode == "error":
        raise AssertionError(format_assertion_health_error(diags))
    if diags and mode == "warn":
        for d in diags:
            print(format_assertion_health_warning(d), file=sys.stderr)

    evaluate_internal_assert_tree(
        assert_tree,
        case_id=execution.case_id,
        subject_for_key=subject_for_key,
        limits=execution.limits,
        symbols=execution.symbols,
        imports=execution.imports,
    )


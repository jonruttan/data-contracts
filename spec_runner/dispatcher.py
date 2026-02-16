from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Mapping, Protocol

from spec_runner.codecs import load_external_cases
from spec_runner.compiler import compile_external_case
from spec_runner.components.chain_engine import execute_case_chain
from spec_runner.doc_parser import SpecDocTest
from spec_runner.internal_model import InternalSpecCase


class RuntimePatcher(Protocol):
    def context(self) -> Any: ...


class RuntimeCapture(Protocol):
    def readouterr(self) -> Any: ...


TypeRunner = Callable[..., None]


@dataclass(frozen=True)
class SpecRunContext:
    tmp_path: Path
    patcher: RuntimePatcher
    capture: RuntimeCapture
    env: Mapping[str, str] | None = None
    chain_state: dict[str, Any] = field(default_factory=dict)
    chain_trace: list[dict[str, Any]] = field(default_factory=list)
    _case_target_values: dict[str, dict[str, Any]] = field(default_factory=dict)
    _case_chain_imports: dict[str, dict[str, Any]] = field(default_factory=dict)
    _case_chain_payloads: dict[str, dict[str, Any]] = field(default_factory=dict)
    _active_case_keys: set[str] = field(default_factory=set)

    def patch_context(self) -> Any:
        return self.patcher.context()

    def read_capture(self) -> Any:
        return self.capture.readouterr()

    def set_case_targets(self, *, case_key: str, targets: Mapping[str, Any]) -> None:
        self._case_target_values[case_key] = dict(targets)

    def get_case_targets(self, *, case_key: str) -> Mapping[str, Any] | None:
        return self._case_target_values.get(case_key)

    def set_case_chain_imports(self, *, case_key: str, imports: Mapping[str, Any]) -> None:
        self._case_chain_imports[case_key] = dict(imports)

    def get_case_chain_imports(self, *, case_key: str) -> Mapping[str, Any]:
        return dict(self._case_chain_imports.get(case_key, {}))

    def set_case_chain_payload(self, *, case_key: str, payload: Mapping[str, Any]) -> None:
        self._case_chain_payloads[case_key] = dict(payload)

    def get_case_chain_payload(self, *, case_key: str) -> Mapping[str, Any]:
        return dict(self._case_chain_payloads.get(case_key, {"state": {}, "trace": [], "imports": {}}))

    def push_active_case(self, case_key: str) -> None:
        if case_key in self._active_case_keys:
            raise RuntimeError(f"recursive case execution detected for {case_key}")
        self._active_case_keys.add(case_key)

    def pop_active_case(self, case_key: str) -> None:
        self._active_case_keys.discard(case_key)


def iter_cases(
    spec_dir: Path,
    *,
    file_pattern: str | None = None,
    formats: set[str] | None = None,
) -> list[SpecDocTest]:
    return [
        SpecDocTest(doc_path=doc_path, test=test)
        for doc_path, test in load_external_cases(spec_dir, formats=formats or {"md"}, md_pattern=file_pattern)
    ]


def default_type_runners() -> dict[str, TypeRunner]:
    # Lazy import to avoid circular imports during collection.
    from spec_runner.harnesses.api_http import run as run_api_http
    from spec_runner.harnesses.cli_run import run as run_cli
    from spec_runner.harnesses.docs_generate import run as run_docs_generate
    from spec_runner.harnesses.orchestration_run import run as run_orchestration
    from spec_runner.harnesses.text_file import run as run_text_file

    return {
        "api.http": run_api_http,
        "cli.run": run_cli,
        "docs.generate": run_docs_generate,
        "orchestration.run": run_orchestration,
        "text.file": run_text_file,
    }


def _to_internal_case(case: SpecDocTest | InternalSpecCase) -> InternalSpecCase:
    if isinstance(case, InternalSpecCase):
        return case
    return compile_external_case(case.test, doc_path=case.doc_path)


def run_case(
    case: SpecDocTest | InternalSpecCase,
    *,
    ctx: SpecRunContext,
    type_runners: Mapping[str, TypeRunner] | None = None,
) -> None:
    runners = default_type_runners()
    if type_runners:
        runners.update(type_runners)
    if isinstance(case, InternalSpecCase):
        type_ = case.type
    else:
        type_ = str(case.test["type"])
    fn = runners.get(type_)
    if not fn:
        doc_path = case.doc_path if isinstance(case, SpecDocTest) else case.doc_path
        raise RuntimeError(f"unknown spec-test type: {type_} (from {doc_path})")

    internal_case = _to_internal_case(case)
    case_key = f"{internal_case.doc_path.resolve().as_posix()}::{internal_case.id}"
    ctx.push_active_case(case_key)
    try:
        execute_case_chain(
            internal_case,
            ctx=ctx,
            run_case_fn=lambda chained_case: run_case(chained_case, ctx=ctx, type_runners=type_runners),
        )
        # Core runner types execute compiled internal cases. External custom runners
        # keep receiving SpecDocTest for backward compatibility.
        if type_ in {"api.http", "cli.run", "docs.generate", "orchestration.run", "text.file"}:
            fn(internal_case, ctx=ctx)
            return
        fn(case, ctx=ctx)
    finally:
        ctx.pop_active_case(case_key)

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Mapping, Protocol

from spec_runner.codecs import load_external_cases
from spec_runner.compiler import compile_external_case
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

    def patch_context(self) -> Any:
        return self.patcher.context()

    def read_capture(self) -> Any:
        return self.capture.readouterr()


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
    from spec_runner.harnesses.orchestration_run import run as run_orchestration
    from spec_runner.harnesses.text_file import run as run_text_file

    return {
        "api.http": run_api_http,
        "cli.run": run_cli,
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

    # Core runner types execute compiled internal cases. External custom runners
    # keep receiving SpecDocTest for backward compatibility.
    if type_ in {"api.http", "cli.run", "orchestration.run", "text.file"}:
        fn(_to_internal_case(case), ctx=ctx)
        return
    fn(case, ctx=ctx)

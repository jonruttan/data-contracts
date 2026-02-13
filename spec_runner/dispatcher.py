from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Mapping, Protocol

from spec_runner.doc_parser import SpecDocTest, iter_spec_doc_tests


class RuntimePatcher(Protocol):
    def context(self) -> Any: ...


class RuntimeCapture(Protocol):
    def readouterr(self) -> Any: ...


TypeRunner = Callable[..., None]


@dataclass(frozen=True)
class SpecRunContext:
    tmp_path: Path
    monkeypatch: RuntimePatcher | None = None
    capsys: RuntimeCapture | None = None
    env: Mapping[str, str] | None = None
    patcher: RuntimePatcher | None = None
    capture: RuntimeCapture | None = None

    def patch_context(self) -> Any:
        patcher = self.patcher or self.monkeypatch
        if patcher is None:
            raise RuntimeError("SpecRunContext requires patcher (or legacy monkeypatch)")
        return patcher.context()

    def read_capture(self) -> Any:
        capture = self.capture or self.capsys
        if capture is None:
            raise RuntimeError("SpecRunContext requires capture (or legacy capsys)")
        return capture.readouterr()


def iter_cases(spec_dir: Path) -> list[SpecDocTest]:
    return list(iter_spec_doc_tests(spec_dir))


def default_type_runners() -> dict[str, TypeRunner]:
    # Lazy import to avoid circular imports during collection.
    from spec_runner.harnesses.cli_run import run as run_cli
    from spec_runner.harnesses.text_file import run as run_text_file

    return {
        "cli.run": run_cli,
        "text.file": run_text_file,
    }


def run_case(case: SpecDocTest, *, ctx: SpecRunContext, type_runners: Mapping[str, TypeRunner] | None = None) -> None:
    type_ = case.test["type"]
    runners = default_type_runners()
    if type_runners:
        runners.update(type_runners)
    fn = runners.get(type_)
    if not fn:
        raise RuntimeError(f"unknown spec-test type: {type_} (from {case.doc_path})")
    fn(case, ctx=ctx)

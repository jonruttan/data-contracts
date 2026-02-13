from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

from spec_runner.doc_parser import SpecDocTest, iter_spec_doc_tests


@dataclass(frozen=True)
class SpecRunContext:
    tmp_path: Path
    monkeypatch: object
    capsys: object
    env: Mapping[str, str] | None = None


def iter_cases(spec_dir: Path) -> list[SpecDocTest]:
    return list(iter_spec_doc_tests(spec_dir))


def default_type_runners() -> dict[str, object]:
    # Lazy import to avoid circular imports during collection.
    from spec_runner.harnesses.cli_run import run as run_cli
    from spec_runner.harnesses.text_file import run as run_text_file

    return {
        "cli.run": run_cli,
        "text.file": run_text_file,
    }


def run_case(case: SpecDocTest, *, ctx: SpecRunContext, type_runners: dict[str, object] | None = None) -> None:
    type_ = case.test["type"]
    runners = default_type_runners()
    if type_runners:
        runners.update(type_runners)
    fn = runners.get(type_)
    if not fn:
        raise RuntimeError(f"unknown spec-test type: {type_} (from {case.doc_path})")
    fn(case, ctx=ctx)

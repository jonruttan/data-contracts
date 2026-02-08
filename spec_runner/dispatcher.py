from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from spec_runner.doc_parser import SpecDocTest, iter_spec_doc_tests


@dataclass(frozen=True)
class SpecRunContext:
    tmp_path: Path
    monkeypatch: object
    capsys: object


def iter_cases(spec_dir: Path) -> list[SpecDocTest]:
    return list(iter_spec_doc_tests(spec_dir))


def default_kind_runners() -> dict[str, object]:
    # Lazy import to avoid circular imports during collection.
    from spec_runner.harnesses.cli_run import run as run_cli

    return {"cli.run": run_cli}


def run_case(case: SpecDocTest, *, ctx: SpecRunContext, kind_runners: dict[str, object] | None = None) -> None:
    kind = case.test["kind"]
    runners = default_kind_runners()
    if kind_runners:
        runners.update(kind_runners)
    fn = runners.get(kind)
    if not fn:
        raise RuntimeError(f"unknown spec-test kind: {kind} (from {case.doc_path})")
    fn(case, ctx=ctx)

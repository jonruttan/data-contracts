from pathlib import Path

import pytest

from spec_runner.dispatcher import SpecRunContext, run_case
from spec_runner.doc_parser import SpecDocTest


def test_unknown_kind_raises_clear_error(tmp_path, monkeypatch, capsys):
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={"id": "CK-CLI-999", "kind": "unknown.kind", "title": "Unknown kind"},
    )

    with pytest.raises(RuntimeError, match=r"unknown spec-test kind: unknown\.kind"):
        run_case(
            case,
            ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys),
            kind_runners={"cli.run": lambda *_a, **_k: None},
        )

from __future__ import annotations

import sys
import types
from pathlib import Path

import pytest

from spec_runner.dispatcher import SpecRunContext
from spec_runner.doc_parser import SpecDocTest


def _install_sut(monkeypatch, fn) -> str:
    """
    Install a fake "system under test" module with a `main(argv)` function.

    Returns an entrypoint string suitable for `harness.entrypoint`.
    """
    mod_name = "spec_runner_test_sut"
    m = types.ModuleType(mod_name)
    m.main = fn  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, mod_name, m)
    return f"{mod_name}:main"


def test_cli_kind_accepts_string_argv_and_systemexit(tmp_path, monkeypatch, capsys):
    def fake_main(argv):
        print("[]")  # stdout
        raise SystemExit(0)

    ep = _install_sut(monkeypatch, fake_main)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-001",
            "kind": "cli.run",
            "argv": "plugins",
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert": [{"target": "stdout", "json_type": ["list"]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_kind_unsupported_stdout_json_type_raises(tmp_path, monkeypatch, capsys):
    def fake_main(argv):
        print("[]")
        return 0

    ep = _install_sut(monkeypatch, fake_main)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-002",
            "kind": "cli.run",
            "argv": ["plugins"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert": [{"target": "stdout", "json_type": ["nope"]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    with pytest.raises(ValueError, match="unsupported json_type"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_kind_stdout_json_dict(tmp_path, monkeypatch, capsys):
    def fake_main(argv):
        print("{}")
        return 0

    ep = _install_sut(monkeypatch, fake_main)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-003",
            "kind": "cli.run",
            "argv": ["plugins"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert": [{"target": "stdout", "json_type": ["dict"]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_kind_contains_and_regex_and_negation(tmp_path, monkeypatch, capsys):
    def fake_main(argv):
        print("hello world")
        print("ERR", file=sys.stderr)
        return 0

    ep = _install_sut(monkeypatch, fake_main)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-004",
            "kind": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert": [
                {"target": "stdout", "contains": ["hello"], "regex": ["world\\s*$"]},
                {"target": "stderr", "not_contains": ["ERROR:"]},
            ],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_kind_stdout_path_text(tmp_path, monkeypatch, capsys):
    note = tmp_path / "n.md"
    note.write_text("hello", encoding="utf-8")

    def fake_main(argv):
        print(str(note))
        return 0

    ep = _install_sut(monkeypatch, fake_main)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-005",
            "kind": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert": [{"target": "stdout_path_text", "contains": ["hello"]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_kind_errors_on_unknown_target(tmp_path, monkeypatch, capsys):
    def fake_main(argv):
        print("x")
        return 0

    ep = _install_sut(monkeypatch, fake_main)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-006",
            "kind": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert": [{"target": "nope", "contains": ["x"]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    with pytest.raises(ValueError, match="unknown assert target"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_kind_stdout_path_unsupported_op(tmp_path, monkeypatch, capsys):
    note = tmp_path / "n.md"
    note.write_text("hello", encoding="utf-8")

    def fake_main(argv):
        print(str(note))
        return 0

    ep = _install_sut(monkeypatch, fake_main)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-007",
            "kind": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert": [{"target": "stdout_path", "contains": ["x"]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    with pytest.raises(ValueError, match="unsupported op for stdout_path"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_kind_unsupported_op_raises(tmp_path, monkeypatch, capsys):
    ep = _install_sut(monkeypatch, lambda _argv: 0)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-008",
            "kind": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert": [{"target": "stdout", "nope": ["x"]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    with pytest.raises(ValueError, match="unsupported op"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_kind_supports_env_and_setup_files(tmp_path, monkeypatch, capsys):
    seen = {}

    def fake_main(_argv):
        import os
        from pathlib import Path as _Path

        seen["cfg"] = os.environ.get("X_CFG")
        print(_Path(seen["cfg"]).read_text(encoding="utf-8"))
        return 0

    ep = _install_sut(monkeypatch, fake_main)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-011",
            "kind": "cli.run",
            "argv": ["plugins"],
            "exit_code": 0,
            "harness": {
                "entrypoint": ep,
                "setup_files": [{"path": "cfg.txt", "text": "hello"}],
                "env": {"X_CFG": "cfg.txt"},
            },
            "assert": [{"target": "stdout", "contains": ["hello"]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))
    assert seen["cfg"] == str((tmp_path / "cfg.txt").resolve())


def test_cli_kind_can_stub_modules(tmp_path, monkeypatch, capsys):
    def fake_main(_argv):
        import openai  # noqa: F401

        print("ok")
        return 0

    ep = _install_sut(monkeypatch, fake_main)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-014",
            "kind": "cli.run",
            "argv": ["plugins"],
            "exit_code": 0,
            "harness": {"entrypoint": ep, "stub_modules": ["openai"]},
            "assert": [{"target": "stdout", "contains": ["ok"]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_kind_can_inject_stdin_text_and_isatty(tmp_path, monkeypatch, capsys):
    def fake_main(_argv):
        data = sys.stdin.read()
        print(f"stdin={data}")
        return 0

    ep = _install_sut(monkeypatch, fake_main)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-012",
            "kind": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep, "stdin_isatty": False, "stdin_text": "hello"},
            "assert": [{"target": "stdout", "contains": ["stdin=hello"]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_kind_any_group_or_semantics(tmp_path, monkeypatch, capsys):
    def fake_main(_argv):
        print("ok")
        print("WARN: something", file=sys.stderr)
        return 0

    ep = _install_sut(monkeypatch, fake_main)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-010",
            "kind": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert": [
                {"any": [{"target": "stderr", "contains": ["INFO:"]}, {"target": "stderr", "contains": ["WARN:"]}]},
                {"target": "stderr", "not_contains": ["ERROR:"]},
            ],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))

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


def _install_hook(monkeypatch, fn) -> str:
    """
    Install a fake hook module with a `hook(**kwargs)` function.
    """
    mod_name = "spec_runner_test_hook"
    m = types.ModuleType(mod_name)
    m.hook = fn  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, mod_name, m)
    return f"{mod_name}:hook"


def test_cli_type_accepts_string_argv_and_systemexit(tmp_path, monkeypatch, capsys):
    def fake_main(argv):
        print("[]")  # stdout
        raise SystemExit(0)

    ep = _install_sut(monkeypatch, fake_main)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-001",
            "type": "cli.run",
            "argv": "plugins",
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert": [{"target": "stdout", "must": [{"json_type": ["list"]}]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_unsupported_stdout_json_type_raises(tmp_path, monkeypatch, capsys):
    def fake_main(argv):
        print("[]")
        return 0

    ep = _install_sut(monkeypatch, fake_main)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-002",
            "type": "cli.run",
            "argv": ["plugins"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert": [{"target": "stdout", "must": [{"json_type": ["nope"]}]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    with pytest.raises(ValueError, match="unsupported json_type"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_stdout_json_dict(tmp_path, monkeypatch, capsys):
    def fake_main(argv):
        print("{}")
        return 0

    ep = _install_sut(monkeypatch, fake_main)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-003",
            "type": "cli.run",
            "argv": ["plugins"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert": [{"target": "stdout", "must": [{"json_type": ["dict"]}]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_contain_regex_and_cannot(tmp_path, monkeypatch, capsys):
    def fake_main(argv):
        print("hello world")
        print("ERR", file=sys.stderr)
        return 0

    ep = _install_sut(monkeypatch, fake_main)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-004",
            "type": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert": [
                {"target": "stdout", "must": [{"contain": ["hello"], "regex": ["world\\s*$"]}]},
                {"target": "stderr", "cannot": [{"contain": ["ERROR:"]}]},
            ],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_stdout_path_text(tmp_path, monkeypatch, capsys):
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
            "type": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert": [{"target": "stdout_path_text", "must": [{"contain": ["hello"]}]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_errors_on_unknown_target(tmp_path, monkeypatch, capsys):
    def fake_main(argv):
        print("x")
        return 0

    ep = _install_sut(monkeypatch, fake_main)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-006",
            "type": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert": [{"target": "nope", "must": [{"contain": ["x"]}]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    with pytest.raises(ValueError, match="unknown assert target"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_stdout_path_unsupported_op(tmp_path, monkeypatch, capsys):
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
            "type": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert": [{"target": "stdout_path", "must": [{"contain": ["x"]}]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    with pytest.raises(ValueError, match="unsupported op for stdout_path"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_unsupported_op_raises(tmp_path, monkeypatch, capsys):
    ep = _install_sut(monkeypatch, lambda _argv: 0)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-008",
            "type": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert": [{"target": "stdout", "must": [{"nope": ["x"]}]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    with pytest.raises(ValueError, match="unsupported op"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_supports_env_and_setup_files(tmp_path, monkeypatch, capsys):
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
            "type": "cli.run",
            "argv": ["plugins"],
            "exit_code": 0,
            "harness": {
                "entrypoint": ep,
                "setup_files": [{"path": "cfg.txt", "text": "hello"}],
                "env": {"X_CFG": "cfg.txt"},
            },
            "assert": [{"target": "stdout", "must": [{"contain": ["hello"]}]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))
    assert seen["cfg"] == str((tmp_path / "cfg.txt").resolve())


def test_cli_type_can_stub_modules(tmp_path, monkeypatch, capsys):
    def fake_main(_argv):
        import openai  # noqa: F401

        print("ok")
        return 0

    ep = _install_sut(monkeypatch, fake_main)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-014",
            "type": "cli.run",
            "argv": ["plugins"],
            "exit_code": 0,
            "harness": {"entrypoint": ep, "stub_modules": ["openai"]},
            "assert": [{"target": "stdout", "must": [{"contain": ["ok"]}]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_can_inject_stdin_text_and_isatty(tmp_path, monkeypatch, capsys):
    def fake_main(_argv):
        data = sys.stdin.read()
        print(f"stdin={data}")
        return 0

    ep = _install_sut(monkeypatch, fake_main)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-012",
            "type": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep, "stdin_isatty": False, "stdin_text": "hello"},
            "assert": [{"target": "stdout", "must": [{"contain": ["stdin=hello"]}]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_can_group_or_semantics(tmp_path, monkeypatch, capsys):
    def fake_main(_argv):
        print("ok")
        print("WARN: something", file=sys.stderr)
        return 0

    ep = _install_sut(monkeypatch, fake_main)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-010",
            "type": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert": [
                {"can": [{"target": "stderr", "must": [{"contain": ["INFO:"]}]}, {"target": "stderr", "must": [{"contain": ["WARN:"]}]}]},
                {"target": "stderr", "cannot": [{"contain": ["ERROR:"]}]},
            ],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_cannot_json_type(tmp_path, monkeypatch, capsys):
    def fake_main(_argv):
        print("{}")
        return 0

    ep = _install_sut(monkeypatch, fake_main)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-017",
            "type": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert": [{"target": "stdout", "cannot": [{"json_type": ["list"]}]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_hook_runs_after_command(tmp_path, monkeypatch, capsys):
    seen = {}

    def fake_main(_argv):
        print("{\"ok\": true}")
        return 0

    def hook(*, case, ctx, result, extra=None):
        assert case.test["id"] == "SR-CLI-UNIT-015"
        assert result["exit_code"] == 0
        assert "\"ok\"" in result["stdout"]
        assert isinstance(ctx.tmp_path, Path)
        seen["ran"] = True
        seen["extra"] = extra

    ep = _install_sut(monkeypatch, fake_main)
    hook_ep = _install_hook(monkeypatch, hook)

    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-015",
            "type": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep, "hook_after": hook_ep, "hook_kwargs": {"extra": "v"}},
            "assert": [{"target": "stdout", "must": [{"json_type": ["dict"]}]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))
    assert seen == {"ran": True, "extra": "v"}


def test_cli_type_hook_before_runs_before_command(tmp_path, monkeypatch, capsys):
    seen = {}

    def hook_before(*, case, ctx, harness, extra=None):
        assert case.test["id"] == "SR-CLI-UNIT-016"
        ctx.monkeypatch.setenv("X_BEFORE", "yes")
        seen["ran"] = True
        seen["extra"] = extra
        assert isinstance(harness, dict)

    def fake_main(_argv):
        import os

        print(os.environ.get("X_BEFORE", "no"))
        return 0

    ep = _install_sut(monkeypatch, fake_main)
    hook_ep = _install_hook(monkeypatch, hook_before)

    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-016",
            "type": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep, "hook_before": hook_ep, "hook_kwargs": {"extra": "v2"}},
            "assert": [{"target": "stdout", "must": [{"contain": ["yes"]}]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))
    assert seen == {"ran": True, "extra": "v2"}


def test_cli_type_stub_modules_do_not_leak_between_cases(tmp_path, monkeypatch, capsys):
    mod_name = "spec_runner_stub_mod_unique"

    def fake_main(_argv):
        try:
            __import__(mod_name)
            print("imported")
        except ModuleNotFoundError:
            print("missing")
        return 0

    ep = _install_sut(monkeypatch, fake_main)
    from spec_runner.harnesses.cli_run import run

    case_with_stub = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-018",
            "type": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep, "stub_modules": [mod_name]},
            "assert": [{"target": "stdout", "must": [{"contain": ["imported"]}]}],
        },
    )
    run(case_with_stub, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))

    case_without_stub = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-019",
            "type": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert": [{"target": "stdout", "must": [{"contain": ["missing"]}]}],
        },
    )
    run(case_without_stub, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_setup_files_rejects_absolute_path(tmp_path, monkeypatch, capsys):
    ep = _install_sut(monkeypatch, lambda _argv: 0)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-020",
            "type": "cli.run",
            "exit_code": 0,
            "harness": {
                "entrypoint": ep,
                "setup_files": [{"path": str((tmp_path / "x.txt").resolve()), "text": "x"}],
            },
        },
    )

    from spec_runner.harnesses.cli_run import run

    with pytest.raises(ValueError, match="setup_files item path must be relative"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_setup_files_rejects_path_escape(tmp_path, monkeypatch, capsys):
    ep = _install_sut(monkeypatch, lambda _argv: 0)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-021",
            "type": "cli.run",
            "exit_code": 0,
            "harness": {
                "entrypoint": ep,
                "setup_files": [{"path": "../escape.txt", "text": "x"}],
            },
        },
    )

    from spec_runner.harnesses.cli_run import run

    with pytest.raises(ValueError, match="setup_files item path escapes tmp_path"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_requires_entrypoint_or_env_fallback(tmp_path, monkeypatch, capsys):
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-022",
            "type": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {},
        },
    )

    from spec_runner.harnesses.cli_run import run

    with pytest.raises(RuntimeError, match="requires harness.entrypoint or SPEC_RUNNER_ENTRYPOINT"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_assert_health_warn_emits_warning(tmp_path, monkeypatch, capsys):
    ep = _install_sut(monkeypatch, lambda _argv: 0)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-023",
            "type": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert_health": {"mode": "warn"},
            "assert": [
                {"target": "stdout", "must": [{"contain": [""]}]},
                {"target": "stderr", "must": [{"contain": ["WARN: ASSERT_HEALTH AH001"]}]},
            ],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_assert_health_error_fails(tmp_path, monkeypatch, capsys):
    ep = _install_sut(monkeypatch, lambda _argv: 0)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-024",
            "type": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert_health": {"mode": "error"},
            "assert": [{"target": "stdout", "must": [{"contain": [""]}]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    with pytest.raises(AssertionError, match="assertion health check failed"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_failure_includes_case_and_assert_context(tmp_path, monkeypatch, capsys):
    ep = _install_sut(monkeypatch, lambda _argv: 0)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-025",
            "type": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert": [{"target": "stdout", "must": [{"contain": ["missing-value"]}]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    with pytest.raises(AssertionError) as ei:
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))
    msg = str(ei.value)
    assert "case_id=SR-CLI-UNIT-025" in msg
    assert "assert_path=assert[0].must[0]" in msg
    assert "target=stdout" in msg
    assert "op=contain" in msg


def test_cli_type_assert_health_warns_on_redundant_branches(tmp_path, monkeypatch, capsys):
    ep = _install_sut(monkeypatch, lambda _argv: 0)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-026",
            "type": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": ep},
            "assert_health": {"mode": "warn"},
            "assert": [
                {
                    "target": "stdout",
                    "can": [
                        {"contain": [""]},
                        {"contain": [""]},
                    ],
                },
                {"target": "stderr", "must": [{"contain": ["WARN: ASSERT_HEALTH AH004"]}]},
            ],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_rejects_entrypoint_without_colon(tmp_path, monkeypatch, capsys):
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-027",
            "type": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": "not-an-entrypoint"},
        },
    )

    from spec_runner.harnesses.cli_run import run

    with pytest.raises(ValueError, match="invalid entrypoint"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_rejects_missing_entrypoint_module(tmp_path, monkeypatch, capsys):
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-028",
            "type": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": "missing_module_xyz:main"},
        },
    )

    from spec_runner.harnesses.cli_run import run

    with pytest.raises(ModuleNotFoundError, match="entrypoint module not found"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_rejects_missing_entrypoint_attribute(tmp_path, monkeypatch, capsys):
    m = types.ModuleType("spec_runner_test_missing_attr")
    monkeypatch.setitem(sys.modules, "spec_runner_test_missing_attr", m)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-029",
            "type": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {"entrypoint": "spec_runner_test_missing_attr:main"},
        },
    )

    from spec_runner.harnesses.cli_run import run

    with pytest.raises(AttributeError, match="entrypoint attribute not found"):
        run(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))


def test_cli_type_can_use_entrypoint_from_context_env(tmp_path, monkeypatch, capsys):
    def fake_main(_argv):
        print("ok")
        return 0

    ep = _install_sut(monkeypatch, fake_main)
    case = SpecDocTest(
        doc_path=Path("docs/spec/cli.md"),
        test={
            "id": "SR-CLI-UNIT-030",
            "type": "cli.run",
            "argv": ["x"],
            "exit_code": 0,
            "harness": {},
            "assert": [{"target": "stdout", "must": [{"contain": ["ok"]}]}],
        },
    )

    from spec_runner.harnesses.cli_run import run

    run(
        case,
        ctx=SpecRunContext(
            tmp_path=tmp_path,
            monkeypatch=monkeypatch,
            capsys=capsys,
            env={"SPEC_RUNNER_ENTRYPOINT": ep},
        ),
    )

import builtins
import io
import os
import sys
import types
import importlib

from spec_runner.assertions import (
    assert_stdout_path_exists,
    assert_text_op,
    eval_assert_tree,
    is_text_op,
    iter_leaf_assertions,
    parse_json,
)

def _load_entrypoint(ep: str):
    """
    Load a call target from an entrypoint-like string: "module.sub:func".
    """
    if ":" not in ep:
        raise ValueError(f"invalid entrypoint (expected module:attr): {ep}")
    mod_name, attr = ep.split(":", 1)
    mod = importlib.import_module(mod_name)
    fn = getattr(mod, attr, None)
    if not callable(fn):
        raise TypeError(f"entrypoint is not callable: {ep}")
    return fn


def run(case, *, ctx) -> None:
    t = case.test
    h = t.get("harness") or {}
    if not isinstance(h, dict):
        raise TypeError("harness must be a mapping")

    supported_harness_keys = {
        "entrypoint",
        "env",
        "stdin_isatty",
        "stdin_text",
        "block_imports",
        "stub_modules",
        "setup_files",
        "hook_before",
        "hook_after",
        "hook_kwargs",
    }
    unknown = sorted(str(k) for k in h.keys() if k not in supported_harness_keys)
    if unknown:
        raise ValueError(f"unsupported harness key(s): {', '.join(unknown)}")

    legacy_keys = {
        "stub_modules",
        "setup_files",
        "stdin_text",
        "stdin_isatty",
        "block_imports",
    }
    found_legacy = sorted(k for k in legacy_keys if k in t)
    if found_legacy:
        raise ValueError(f"move harness-only keys under 'harness:': {', '.join(found_legacy)}")

    argv = t.get("argv", [])
    if isinstance(argv, str):
        argv = [argv]
    argv = [str(a) for a in (argv or [])]

    # Runner-provided setup features. These are deliberately small and generic
    # to avoid hook proliferation for common cases.
    stub_modules = h.get("stub_modules") or []
    if isinstance(stub_modules, str):
        stub_modules = [stub_modules]
    for name in [str(x).strip() for x in stub_modules if str(x).strip()]:
        if name == "openai":
            sys.modules.setdefault("openai", types.SimpleNamespace(OpenAI=object))
        else:
            sys.modules.setdefault(name, types.SimpleNamespace())

    setup_files = h.get("setup_files") or []
    if isinstance(setup_files, dict):
        setup_files = [setup_files]
    if setup_files:
        if not isinstance(setup_files, list):
            raise TypeError("setup_files must be a list (or mapping for a single file)")
        for item in setup_files:
            if not isinstance(item, dict):
                raise TypeError("setup_files item must be a mapping")
            rel = item.get("path")
            if not rel:
                raise ValueError("setup_files item missing required key: path")
            text = item.get("text", "")
            p = ctx.tmp_path / str(rel)
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(str(text), encoding="utf-8")

    env = h.get("env") or {}
    if env:
        if not isinstance(env, dict):
            raise TypeError("harness.env must be a mapping")
        for k, v in env.items():
            k = str(k)
            if v is None:
                ctx.monkeypatch.delenv(k, raising=False)
            else:
                sv = str(v)
                # Convenience: if an env value looks like a relative path and a
                # file exists under the runner temp dir, pass the absolute path.
                try:
                    from pathlib import Path

                    pv = Path(sv).expanduser()
                    if not pv.is_absolute() and (ctx.tmp_path / pv).exists():
                        sv = str((ctx.tmp_path / pv).resolve())
                except Exception:
                    pass
                ctx.monkeypatch.setenv(k, sv)

    stdin_text = h.get("stdin_text")
    stdin_isatty = h.get("stdin_isatty")
    if stdin_text is not None or stdin_isatty is not None:
        class _FakeStdin(io.StringIO):
            def __init__(self, text: str, isatty: bool):
                super().__init__(text)
                self._isatty = bool(isatty)

            def isatty(self) -> bool:  # type: ignore[override]
                return self._isatty

        fake = _FakeStdin("" if stdin_text is None else str(stdin_text), bool(stdin_isatty))
        ctx.monkeypatch.setattr(sys, "stdin", fake)

    # Test-only affordance: allow docs-embedded spec-tests to simulate missing
    # optional dependencies in a deterministic way.
    block_imports = h.get("block_imports") or []
    if isinstance(block_imports, str):
        block_imports = [block_imports]
    block_imports = {str(x) for x in block_imports if str(x).strip()}

    real_import = builtins.__import__

    def _blocked_import(name, globals=None, locals=None, fromlist=(), level=0):
        if name in block_imports or any(name.startswith(m + ".") for m in block_imports):
            raise ModuleNotFoundError(name)
        return real_import(name, globals, locals, fromlist, level)

    if block_imports:
        ctx.monkeypatch.setattr(builtins, "__import__", _blocked_import)

    # Optional hooks for complex setup/assertions.
    hook_kwargs = h.get("hook_kwargs") or {}
    if not isinstance(hook_kwargs, dict):
        raise TypeError("harness.hook_kwargs must be a mapping")

    hook_before_ep = h.get("hook_before")
    hook_after_ep = h.get("hook_after")

    if hook_before_ep is not None and not str(hook_before_ep).strip():
        hook_before_ep = None
    if hook_after_ep is not None and not str(hook_after_ep).strip():
        hook_after_ep = None

    if hook_before_ep:
        hook_before_fn = _load_entrypoint(str(hook_before_ep))
        hook_before_fn(case=case, ctx=ctx, harness=h, **{str(k): v for k, v in hook_kwargs.items()})

    entrypoint = str(h.get("entrypoint") or os.environ.get("SPEC_RUNNER_ENTRYPOINT") or "").strip()
    if not entrypoint:
        raise RuntimeError("cli.run requires harness.entrypoint or SPEC_RUNNER_ENTRYPOINT")
    cli_main = _load_entrypoint(entrypoint)

    try:
        code = cli_main(argv)
    except SystemExit as e:
        ec = getattr(e, "code", 1)
        code = 1 if ec is None else int(ec)

    captured = ctx.capsys.readouterr()
    assert int(code) == int(t.get("exit_code", 0))

    # Optional hook_after for complex assertions/setup that don't fit the declarative DSL.
    if hook_after_ep:
        # Best-effort derive stdout_path for convenience.
        stdout_path = None
        try:
            stdout_path = assert_stdout_path_exists(captured.out)
        except Exception:
            stdout_path = None
        hook_after_fn = _load_entrypoint(str(hook_after_ep))
        hook_after_fn(
            case=case,
            ctx=ctx,
            result={
                "exit_code": int(code),
                "stdout": captured.out,
                "stderr": captured.err,
                "stdout_path": stdout_path,
            },
            **{str(k): v for k, v in hook_kwargs.items()},
        )

    def _eval_leaf(leaf: dict) -> None:
        for target, op, value in iter_leaf_assertions(leaf):
            if target == "stdout":
                subject = captured.out
            elif target == "stderr":
                subject = captured.err
            elif target == "stdout_path":
                p = assert_stdout_path_exists(captured.out)
                if op != "exists":
                    raise ValueError(f"unsupported op for stdout_path: {op}")
                if value not in (None, True):
                    raise ValueError("stdout_path.exists only supports value: true (or null)")
                assert p.exists()
                continue
            elif target == "stdout_path_text":
                p = assert_stdout_path_exists(captured.out)
                subject = p.read_text(encoding="utf-8")
            else:
                raise ValueError(f"unknown assert target: {target}")

            if is_text_op(op):
                assert_text_op(subject, op, value)
            elif op == "json_type":
                parsed = parse_json(subject)
                want = str(value).lower()
                if want == "list":
                    assert isinstance(parsed, list)
                elif want == "dict":
                    assert isinstance(parsed, dict)
                else:
                    raise ValueError(f"unsupported json_type: {value}")
            else:
                raise ValueError(f"unsupported op: {op}")

    eval_assert_tree(t.get("assert", []) or [], eval_leaf=_eval_leaf)

# Spec Runner

`spec_runner` is a small **executable-spec runner**: it scans Markdown
documents for fenced blocks tagged `yaml spec-test`, parses them, and executes
them via pluggable harnesses keyed by `type`.

It is designed to be publishable and reusable across projects; each project
can provide its own `type` adapters.

## Install

```sh
python -m pip install spec-runner
```

For development:

```sh
python -m pip install -e '.[dev]'
```

## Quickstart

1. Create a spec doc with a fenced `yaml spec-test` block:

```yaml
id: EX-CLI-001
type: cli.run
argv: ["--help"]
exit_code: 0
harness:
  entrypoint: "myproj.cli:main"
assert:
  - target: stdout
    contain: ["usage:", "options:"]
  - target: stderr
    must:
      - contain: ["WARN:"]
    cannot:
      - contain: ["ERROR:"]
```

2. In your test suite, run the collected cases:

```python
from pathlib import Path

from spec_runner.dispatcher import SpecRunContext, iter_cases, run_case

def test_specs_from_docs(tmp_path, monkeypatch, capsys):
    cases = iter_cases(Path("docs/spec"))
    monkeypatch.setenv("SPEC_RUNNER_ENTRYPOINT", "myproj.cli:main")
    for case in cases:
        run_case(case, ctx=SpecRunContext(tmp_path=tmp_path, monkeypatch=monkeypatch, capsys=capsys))
```

## Layout

- `spec_runner/`: runner implementation (parser, dispatcher, harnesses)
- `tests/`: unit tests for the runner

## Schema (v1)

Each `yaml spec-test` test case is a mapping with:

- `id` (required)
- `type` (required)
- `title` (optional)
- type-specific keys (e.g. `argv`, `exit_code`, `assert` for `cli.run`)
- `harness` (optional): runner-only setup inputs (fixture files, stubs, stdin)

Runner-only keys MUST live under `harness:` to keep the spec format clean.

Canonical boolean groups are `must`, `can`, and `cannot` (legacy aliases
`all`/`any` are still accepted). Text assertions use `contain` (legacy
`contains` is accepted).

Legacy leaf-level negation remains available via `is: false`:

```yaml
- target: stderr
  contain: ["ERROR:"]
  is: false
```

Assertion groups can carry a shared `target`, which child
leaves inherit unless overridden.

Canonical schema doc: `tools/spec_runner/docs/spec/schema.md`.

Discovery note: `iter_cases(Path(...))` currently scans only `*.md` files in
that directory (non-recursive).

## Reuse / Publishing Notes

The runner core is generic, but individual `type` harnesses may be specific to
the system under test. Keep `spec_runner` focused on stable parsing,
dispatching, and assertions; treat adapters as project-owned code.

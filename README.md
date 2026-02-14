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
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[dev]'
```

If system Python is externally managed (PEP 668), use the venv flow above.

Contract governance check:

```sh
python scripts/check_contract_governance.py
```

Lint and static syntax checks:

```sh
python -m ruff check .
python scripts/evaluate_style.py --check docs/spec
python -m mypy spec_runner
python -m compileall -q spec_runner scripts tests
```

Conformance reference test:

```sh
python -m pytest tests/test_conformance_runner_unit.py
```

CI merge gate (GitHub Actions `spec_runner` job) runs:

- `python scripts/check_contract_governance.py`
- `python -m ruff check .`
- `python scripts/evaluate_style.py --check docs/spec`
- `python -m mypy spec_runner`
- `python -m compileall -q spec_runner scripts tests`
- `python scripts/contract_coverage_report.py --out .artifacts/contract-coverage.json`
- `python -m pytest`

## Quickstart

Deterministic first-run walkthrough:

- `docs/book/00_first_10_minutes.md`

Trust/safety model (read before running specs from outside your repo):

- `spec_runner` is not a sandbox.
- Spec files are trusted inputs; `cli.run` and hooks execute project code with
  runner process privileges.
- Running untrusted spec documents is unsafe and out of scope for v1.

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
    must:
      - contain: ["usage:", "options:"]
  - target: stderr
    must:
      - contain: ["WARN:"]
  - target: stderr
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
        run_case(case, ctx=SpecRunContext(tmp_path=tmp_path, patcher=monkeypatch, capture=capsys))
```

## Layout

- `spec_runner/`: runner implementation (parser, dispatcher, harnesses)
- `tests/`: unit tests for runner internals
- `docs/design_philosophy.md`: project design principles and change bar
- `docs/spec/contract/`: language-neutral contract docs
- `docs/spec/schema/`: schema docs (syntax/shape)
- `docs/spec/impl/`: implementation-specific notes (Python/PHP)
- `docs/spec/conformance/`: cross-language conformance contract docs
- `docs/spec/conformance/cases/`: cross-language conformance case specs

## Schema (v1)

Each `yaml spec-test` test case is a mapping with:

- `id` (required)
- `type` (required)
- `title` (optional)
- type-specific keys (e.g. `argv`, `exit_code`, `assert` for `cli.run`)
- `harness` (optional): runner-only setup inputs (fixture files, stubs, stdin)

Runner-only keys MUST live under `harness:` to keep the spec format clean.

Canonical boolean groups are `must`, `can`, and `cannot`.
Text assertions use `contain` and `regex`.
Expression assertions use `evaluate` (spec-lang list S-expressions).
Each assertion group uses exactly one of `must` / `can` / `cannot`, and group
lists must be non-empty.

Write assertions in canonical form:
- use `must` (AND), `can` (OR), `cannot` (negation)
- use `contain` / `regex` as leaf operators
- put all operator values in lists

Assertion groups can carry a shared `target`, which child
leaves inherit unless overridden.
Leaf assertions do not carry `target` directly.

Canonical schema doc: `docs/spec/schema/schema_v1.md`.
Portable contract docs: `docs/spec/contract/`.
Machine-readable policy:
`docs/spec/contract/policy_v1.yaml`.
Traceability mapping:
`docs/spec/contract/traceability_v1.yaml`.
V1 scope/non-goals/compatibility commitments:
`docs/spec/contract/08_v1_scope.md`.

Discovery note: `iter_cases(Path(...))` scans files matching the configured
default case-file pattern in that directory (non-recursive). You can pass a
custom pattern with `iter_cases(Path(...), file_pattern="*.md")`.

## Reuse / Publishing Notes

The runner core is generic, but individual `type` harnesses may be specific to
the system under test. Keep `spec_runner` focused on stable parsing,
dispatching, and assertions; treat adapters as project-owned code.

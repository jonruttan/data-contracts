# First 10 Minutes (Deterministic Walkthrough)

```yaml doc-meta
doc_id: DOC-REF-001
title: First 10 Minutes (Deterministic Walkthrough)
status: active
audience: author
owns_tokens: ["first_run_walkthrough", "trusted_inputs_required"]
requires_tokens: ["quickstart_minimal_case"]
commands:
  - run: "python -m pip install -e '.[dev]'"
    purpose: Install editable package with dev dependencies.
  - run: "./scripts/ci_gate.sh"
    purpose: Execute canonical local gate.
examples:
  - id: EX-FIRST10-001
    runnable: true
sections_required:
  - "## Purpose"
  - "## Inputs"
  - "## Outputs"
  - "## Failure Modes"
```

This walkthrough gives a deterministic first success with `spec_runner` from a
clean clone.

## Purpose

Establish a deterministic first successful run from a clean clone.

## Inputs

- local repo checkout
- Python toolchain for virtualenv and package install

## Outputs

- one passing executable case
- successful local gate execution

## Failure Modes

- missing virtualenv/python tooling
- invalid fenced `yaml spec-test` syntax
- failing local gate checks

## Safety First (Required)

- `spec_runner` is not a sandbox.
- Spec files are trusted inputs; `cli.run` and hook entrypoints execute project
  code with runner process privileges.
- Do not run untrusted spec documents.

## 1) Create And Activate A Virtual Environment

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[dev]'
```

Expected result:

- Install completes without errors.
- `spec_runner` is importable from the local checkout.

## 2) Create A Minimal Executable Spec

```sh
mkdir -p .artifacts/first10
cat > .artifacts/first10/hello.spec.md <<'MD'
# First 10 Minutes Example

```yaml spec-test
id: FIRST10-001
type: text.file
assert:
  - target: text
    must:
      - contain: ["FIRST10-001"]
```
MD
```

Expected result:

- File `.artifacts/first10/hello.spec.md` exists.
- It contains one `yaml spec-test` case with `id` and `type`.

## 3) Execute The Case Through The Library API

```sh
python - <<'PY'
from pathlib import Path
from tempfile import TemporaryDirectory
from spec_runner.dispatcher import SpecRunContext, iter_cases, run_case
from spec_runner.runtime_context import MiniCapsys, MiniMonkeyPatch

cases = iter_cases(Path(".artifacts/first10"), file_pattern="*.spec.md")
with TemporaryDirectory(prefix="spec-runner-first10-") as td:
    for case in cases:
        patcher = MiniMonkeyPatch()
        capture = MiniCapsys()
        ctx = SpecRunContext(tmp_path=Path(td), patcher=patcher, capture=capture)
        with capture.capture():
            run_case(case, ctx=ctx)

print(f"PASS cases={len(cases)}")
PY
```

Expected result:

- Command exits `0`.
- Output includes exactly:

```text
PASS cases=1
```

## 4) Run The Full Local Gate

```sh
./scripts/ci_gate.sh
```

Expected result:

- Gate exits `0`.
- Contract checks, parity checks, and tests all pass.

## Troubleshooting

- `externally-managed-environment`:
  use the virtualenv flow in Step 1.
- `ModuleNotFoundError: spec_runner`:
  rerun `python -m pip install -e '.[dev]'` in the active venv.
- `PASS cases=0`:
  confirm the file is named `*.spec.md` and fence tag is `yaml spec-test`.

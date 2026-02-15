# Python Implementation Notes

This document captures Python-specific implementation details that are not
part of the language-neutral contract.

Current implementation locations:

- parser: `spec_runner/doc_parser.py`
- assertion engine: `spec_runner/assertions.py`
- dispatch: `spec_runner/dispatcher.py`
- harnesses: `spec_runner/harnesses/`

## Supported Flags

Python conformance runner script:

- `scripts/python/conformance_runner.py`
- `spec-runner-conformance`

Public flags:

- `--cases` (required): case file or directory path.
- `--out` (required): JSON report output path.
- `--case-file-pattern` (default: `*.spec.md`): directory-mode case glob.
- `--case-formats` (default: `md`): comma-separated formats (`md,yaml,json`).

## Default Behavior

- discovery default is Markdown-only (`md`) with case pattern `*.spec.md`.
- report is always written when invocation succeeds.
- exit code is `0` only when all case statuses are `pass` or `skip`.
- assertion runtime is universal `evaluate` core:
  - external sugar (`contain`, `regex`, `json_type`, `exists`) compiles to
    spec-lang expressions
  - pass/fail decisions run through compiled spec-lang predicates
  - target applicability is subject-driven by harness-provided subjects

## Opt-In Behavior

- external formats (`yaml`, `json`) require explicit `--case-formats`.
- `SPEC_RUNNER_SAFE_MODE=1` disables hook entrypoints.

## Failure Mode Notes

- CLI usage/argument errors return exit code `2` (for example empty
  `--case-file-pattern`, empty `--case-formats`, missing paths).
- runtime execution or unexpected runner failures return exit code `1`.
- `harness.entrypoint` is required for `cli.run`.

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

Public flags:

- `--cases` (required): case file or directory path.
- `--out` (required): JSON report output path.
- `--case-file-pattern` (default: `*.spec.md`): directory-mode case glob.
- `--case-formats` (default: `md`): comma-separated formats (`md,yaml,json`).

## Default Behavior

- discovery default is Markdown-only (`md`) with case pattern `*.spec.md`.
- report is always written when invocation succeeds.
- exit code is `0` only when all case statuses are `pass` or `skip`.

## Opt-In Behavior

- external formats (`yaml`, `json`) require explicit `--case-formats`.
- `cli.run` may use `SPEC_RUNNER_ENTRYPOINT` fallback if `harness.entrypoint`
  is omitted.
- `SPEC_RUNNER_SAFE_MODE=1` disables hook entrypoints and env fallback.

## Failure Mode Notes

- CLI usage/argument errors return exit code `2` (for example empty
  `--case-file-pattern`, empty `--case-formats`, missing paths).
- runtime execution or unexpected runner failures return exit code `1`.
- portable fixtures should still set `harness.entrypoint` explicitly to avoid
  environment coupling.

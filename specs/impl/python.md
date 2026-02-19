# Python Implementation Notes

This document captures Python-specific implementation details that are not
part of the language-neutral contract.

Current implementation locations:

- parser: `dc-runner-python/spec_runner/doc_parser.py`
- assertion engine: `dc-runner-python/spec_runner/assertions.py`
- dispatch: `dc-runner-python/spec_runner/dispatcher.py`
- harnesses: `dc-runner-python/spec_runner/harnesses/`

Implementation-owned executable cases:

- `specs/impl/python/cases/contract_coverage_report.spec.md`
- `specs/impl/python/cases/docs_lint.spec.md`
- `specs/impl/python/cases/schema_registry_report.spec.md`
- `specs/impl/python/cases/spec_lang_stdlib_report.spec.md`
- `specs/impl/python/cases/validate_conformance_report.spec.md`

## Supported Flags

Python conformance runner command:

- `python -m spec_runner.python_conformance_runner`
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

# Spec Runner (Tooling Subproject)

`spec_runner` is a small **executable-spec runner**: it scans Markdown
documents for fenced blocks tagged `yaml spec-test`, parses them, and executes
them via pluggable `kind` harnesses.

In this repository it is used to run `capturekit`'s specs under `docs/spec/`,
but the runner itself is intended to be publishable as a standalone project.

## Layout

- `spec_runner/`: runner implementation (parser, dispatcher, harnesses)
- `tests/`: unit tests for the runner

## Schema (v1)

Each `yaml spec-test` test case is a mapping with:

- `id` (required)
- `kind` (required)
- `title` (optional)
- kind-specific keys (e.g. `argv`, `exit_code`, `assert` for `cli.run`)
- `harness` (optional): runner-only setup inputs (fixture files, stubs, stdin)

Runner-only keys MUST live under `harness:` to keep the spec format clean.

## Running

This repository runs the runner's own unit tests via pytest `testpaths`, and
also runs the doc-embedded spec-tests via `tests/specs/test_specs_from_docs.py`.

## Reuse / Publishing Notes

The runner core is generic, but individual `kind` harnesses may be specific to
the system under test (e.g. a `cli.run` harness that imports that project's
CLI entrypoint). When publishing, keep the core (`doc_parser`, `dispatcher`,
`assertions`) stable and treat harnesses as optional adapters.

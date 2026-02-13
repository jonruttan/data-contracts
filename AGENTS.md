# AGENTS.md

Project-specific instructions for AI agents working in `tools/spec_runner/`.

## What This Subproject Is

- `spec_runner` is a small Python library for running executable spec tests
  embedded in Markdown documents as fenced blocks tagged `yaml spec-test`.
- It parses spec-test blocks and dispatches each case to a harness based on
  `type`.
- The core library is intended to be reusable and publishable. Project-specific
  harnesses/adapters should live with the system under test.

## Configuration / Schema

- The spec-test schema is documented in `docs/spec/schema/schema-v1.md`.
- Runner-only setup inputs MUST live under `harness:` (never as arbitrary
  top-level keys).
- Executable spec cases MUST live in Markdown files (`*.spec.md`) with fenced
  `yaml spec-test` blocks.

## Local Commands

- Install editable:
  - `python -m pip install -e .`
- Install editable with dev deps:
  - `python -m pip install -e '.[dev]'`
- Run tests:
  - `python -m pytest`
- Build:
  - `python -m build`

## Engineering Rules

- Keep `spec_runner` dependency-minimal:
  - stdlib preferred
  - small, stable dependencies only when justified (e.g. `PyYAML`)
- Keep the core stable:
  - prefer extending via adapters/harnesses rather than growing a large DSL
  - avoid test-runner-specific “magic” unless it is clearly schema’d and
    versioned
- Error messages should be direct and actionable (schema violations should
  explain what to change).

## Change Hygiene

- Keep diffs focused.
- Prefer small, composable changes to schema and harness behavior.

## Commits

- Never run `git commit`, `git rebase`, or any history-editing command unless
  the user explicitly requests it for that specific change.
- If a commit is desired, propose the commit message and wait for explicit
  approval (e.g. "commit it", "approved").

### Approval Semantics

- When the user replies with `approved` (or `commit it`) in response to a
  proposed commit, treat that as approval to:
  - stage the described changes (if not already staged)
  - run a single `git commit` using the proposed message
- `approved` does not approve rebases, hard resets, force-pushes, or other
  history edits.

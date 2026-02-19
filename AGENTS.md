# AGENTS.md

Project-specific instructions for AI agents working in `data-contracts`.

## What This Subproject Is

- `data-contracts` is the canonical contracts/specs/governance repository.
- Executable spec cases remain Markdown files with fenced `yaml contract-spec`
  blocks.
- Runner implementations are externalized to:
  - `dc-runner-rust` (required lane)
  - `dc-runner-python` (compatibility lane)
  - `dc-runner-php` (compatibility lane)
- This repo must not vendor runner implementation logic.

## Configuration / Schema

- The contract-spec schema is documented in `specs/schema/schema_v1.md`.
- Runner-only setup inputs MUST live under `harness:` (never as arbitrary
  top-level keys).
- Executable spec cases MUST live in Markdown files (`*.spec.md`) with fenced
  `yaml contract-spec` blocks.

## Local Commands

- Required lane checks:
  - `./scripts/runner_bin.sh critical-gate`
  - `./scripts/runner_bin.sh governance`
  - `./scripts/runner_bin.sh docs-generate-check`

## Engineering Rules

- Keep Data Contracts runner-agnostic and rust-first for required lane checks.
- Do not add local `runners/rust`, `runners/python`, or `runners/php`
  implementation code back into this repo.
- Keep command boundary stable at `scripts/runner_bin.sh`.
- Error messages should be direct and actionable (schema violations should
  explain what to change).
- Test authoring policy:
  - New behavior tests SHOULD be authored as executable `.spec.md` cases.
  - Runtime implementation tests belong in the owning `dc-runner-*` repo.

## Change Hygiene

- Keep diffs focused.
- Prefer small, composable changes to schema and harness behavior.
- Filename convention:
  - Use lowercase filenames.
  - Use `_` to replace spaces in words.
  - Use `-` to separate major sections (for example date prefixes or section
    tokens).

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

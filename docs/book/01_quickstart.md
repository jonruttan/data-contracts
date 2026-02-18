# Chapter 1: Quickstart

```yaml doc-meta
doc_id: DOC-REF-002
title: Chapter 1 Quickstart
status: active
audience: author
owns_tokens:
- quickstart_minimal_case
- quickstart_gate
requires_tokens:
- core_case_model
commands:
- run: ./scripts/ci_gate.sh
  purpose: Run full local quality gate.
examples:
- id: EX-QUICKSTART-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

This chapter gets you from zero to a passing executable spec in minutes.

## Purpose

Provide the shortest path from no case to passing case execution.

## Inputs

- a writable `.spec.md` file
- repository root shell

## Outputs

- runnable `text.file` and `cli.run` examples
- first sugar and `evaluate` assertion examples

## Failure Modes

- misplaced runner-only keys outside `harness:`
- invalid assertion tree structure

## 1) Write A Minimal Case

Create a Markdown file with a fenced `yaml contract-spec` block:

```yaml
id: BK-QS-001
type: text.file
contract:
- target: text
  MUST:
  - contain:
    - BK-QS-001
```

Why this passes:

- `type: text.file` reads the containing spec file by default.
- The file contains the case id string, so the `contain` assertion succeeds.

## 2) Run The Repo Gate

From repo root:

```sh
./scripts/ci_gate.sh
```

This runs governance checks, conformance reports, parity checks, and tests.

## 3) Add A CLI Case

```yaml
id: BK-QS-002
type: cli.run
argv:
- hello
exit_code: 0
harness:
  entrypoint: /bin/echo
contract:
- target: stdout
  MUST:
  - contain:
    - hello
```

## 4) Add A First `evaluate` Assertion

```yaml
id: BK-QS-002B
type: text.file
contract:
- target: text
  MUST:
  - evaluate:
    - std.logic.and:
      - std.string.contains:
        - BK-QS-002B
      - std.string.starts_with:
        - var: subject
        - 'id:'
```

Use `evaluate` when simple text checks are not enough and you need portable
boolean/value logic in the spec itself.

Authoring default:

- prefer sugar operators (`contain`, `regex`, `json_type`, `exists`) unless
  `evaluate` is required for case intent.

## 5) Common Authoring Mistakes

Invalid:

```yaml
id: BK-QS-003
type: cli.run
entrypoint: /bin/echo
assert: []
```

Problem:

- `entrypoint` is a runner-only key and must be under `harness:`.

Expected fix:

```yaml
id: BK-QS-003
type: cli.run
harness:
  entrypoint: /bin/echo
assert: []
```

## 6) Checklist

- Case has `id` and `type`.
- Runner-only config lives under `harness:`.
- `assert` uses canonical groups/operators.
- Case is small and focused.
- `./scripts/ci_gate.sh` passes locally.

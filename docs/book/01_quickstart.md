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

- runnable `contract.check` examples
- first canonical `evaluate` assertion examples

## Failure Modes

- misplaced runner-only keys outside `harness:`
- invalid assertion tree structure

## 1) Write A Minimal Case

Create a Markdown file with a fenced `yaml contract-spec` block:

```yaml
id: BK-QS-001
type: contract.check
harness:
  check:
    profile: text.file
    config: {}
contract:
- id: contains_case_id
  class: MUST
  target: text
  asserts:
  - evaluate:
      std.string.contains:
      - var: subject
      - BK-QS-001
```

Why this passes:

- `harness.check.profile: text.file` reads the containing spec file by default.
- The file contains the case id string, so the evaluate expression succeeds.

## 2) Run The Repo Gate

From repo root:

```sh
./scripts/ci_gate.sh
```

This runs governance checks, conformance reports, parity checks, and tests.

## 3) Add A CLI Case

```yaml
id: BK-QS-002
type: contract.check
harness:
  check:
    profile: cli.run
    config:
      argv:
      - hello
      exit_code: 0
      harness:
        entrypoint: /bin/echo
contract:
- id: stdout_has_hello
  class: MUST
  target: stdout
  asserts:
  - evaluate:
      std.string.contains:
      - var: subject
      - hello
```

## 4) Add A First `evaluate` Assertion

```yaml
id: BK-QS-002B
type: contract.check
harness:
  check:
    profile: text.file
    config: {}
contract:
- id: text_shape_check
  class: MUST
  target: text
  asserts:
  - evaluate:
      std.logic.and:
      - std.string.contains:
        - BK-QS-002B
      - std.string.starts_with:
        - var: subject
        - 'id:'
```

Use `evaluate` when simple text checks are not enough and you need portable
boolean/value logic in the spec itself.

Authoring default:

- use `evaluate` expressions only.

## 5) Common Authoring Mistakes

Invalid:

```yaml
id: BK-QS-003
type: contract.check
entrypoint: /bin/echo
contract: []
```

Problem:

- `entrypoint` is a runner-only key and must be under `harness:`.

Expected fix:

```yaml
id: BK-QS-003
type: contract.check
harness:
  check:
    profile: cli.run
    config:
      harness:
        entrypoint: /bin/echo
contract: []
```

## 6) Checklist

- Case has `id` and `type`.
- Runner-only config lives under `harness:`.
- `contract` uses `class` + `asserts` with `evaluate`.
- Case is small and focused.
- `./scripts/ci_gate.sh` passes locally.

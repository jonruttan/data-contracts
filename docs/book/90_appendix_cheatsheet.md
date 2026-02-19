# Appendix: Cheatsheet

```yaml doc-meta
doc_id: DOC-REF-006
title: Appendix Cheatsheet
status: active
audience: author
owns_tokens:
- cheatsheet
- minimal_examples
requires_tokens:
- first_run_walkthrough
commands:
- run: ./runners/public/runner_adapter.sh --impl rust spec-lang-format --check --cases specs
  purpose: Verify canonical evaluate style.
examples:
- id: EX-CHEATSHEET-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Provide a compact, copyable set of minimal valid case patterns.

## Inputs

- an author creating or reviewing new `yaml contract-spec` cases

## Outputs

- minimal templates for core types and assertion forms

## Failure Modes

- missing required keys
- operators not list-valued
- misplaced runner-only configuration

## Minimal `text.file`

```yaml
id: CHEAT-001
type: contract.check
harness:
  check:
    profile: text.file
    config: {}
contract:
- id: assert_1
  class: MUST
  target: text
  asserts:
  -       std.string.contains:
      - var: subject
      - hello
```

## Minimal `cli.run`

```yaml
id: CHEAT-002
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
- id: assert_1
  class: MUST
  target: stdout
  asserts:
  -       std.string.contains:
      - var: subject
      - hello
```

## Minimal `evaluate`

```yaml
id: CHEAT-003
type: contract.check
harness:
  check:
    profile: text.file
    config: {}
contract:
- id: assert_1
  class: MUST
  target: text
  asserts:
  -       std.string.contains:
      - var: subject
      - CHEAT-003
```

## Group Semantics

- `MUST`: AND
- `MAY`: OR
- `MUST_NOT`: NONE

## Frequent Schema Rules

- `id` and `type` required
- runner-only keys must be under `harness:`
- operator values are lists
- leaf nodes do not carry `target`
- `evaluate` expression roots are operator-keyed mapping AST nodes

## Common Error -> Fix

- `unsupported harness key(s)` -> move/rename unsupported keys
- `text.file path must be relative` -> remove absolute path
- `text.file path escapes contract root` -> use safe in-root relative path
- `unsupported op` -> use canonical operators
- `assert_health.mode must be one of` -> use `ignore`, `warn`, or `error`

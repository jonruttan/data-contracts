# Chapter 30: Assertion Model

```yaml doc-meta
doc_id: DOC-REF-130
title: Chapter 30 Assertion Model
status: active
audience: author
owns_tokens:
- explicit_assert_imports_v1
requires_tokens:
- case_topology_v1
commands:
- run: ./scripts/control_plane.sh spec-lang-lint --cases specs
  purpose: Enforce canonical assertion/import authoring.
- run: ./scripts/control_plane.sh spec-lang-format --check --cases specs
  purpose: Enforce canonical formatting and safe rewrites.
examples:
- id: EX-ASSERTION-MODEL-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Define canonical assertion semantics and explicit import binding rules.

## Inputs

- `specs/02_contracts/03_assertions.md`
- assertion expressions in mapping-AST form

## Outputs

- deterministic MUST/MAY/MUST_NOT evaluation
- explicit symbol scope per step

## Failure Modes

- missing imports for referenced variables
- canonical assertion shapes
- incompatible class semantics assumptions

## Canonical Contract Shape

```yaml
contract:
  defaults: {}
  imports:
  - from: artifact
    names: [summary_json]
  steps:
  - id: assert_passed
    assert:
      std.logic.eq:
      - std.object.get:
        - {var: summary_json}
        - passed
      - true
```

## Imports and Precedence

- `contract.imports`: default bindings.
- `contract.steps[].imports`: per-step overrides.
- Effective step bindings are merge(contract imports, step imports), with step override precedence.

Assertion imports use list form:

- `from` (canonical: `artifact`)
- `names` (non-empty list)
- `as` (optional alias map)

## Forbidden canonical Forms

- `contract: [ ... ]`
- `steps[].asserts`
- `steps[].target`
- `steps[].on`
- `evaluate` wrapper leaves
- group aliases `can`/`cannot`

## Class Semantics

- `MUST`: all assertions in step pass.
- `MAY`: at least one assertion in step passes.
- `MUST_NOT`: no assertions in step pass.

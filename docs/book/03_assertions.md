# Chapter 3: Assertions

```yaml doc-meta
doc_id: DOC-REF-004
title: Chapter 3 Assertions
status: active
audience: author
owns_tokens:
- must
- can
- cannot
- evaluate
requires_tokens:
- spec-lang
commands:
- run: python scripts/evaluate_style.py --check docs/spec
  purpose: Validate canonical evaluate formatting.
examples:
- id: EX-ASSERTIONS-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

Assertions are step-oriented with explicit class semantics.

## Purpose

Define assertion-step semantics and canonical evaluate usage.

## Inputs

- `assert` step lists with `id`, `class`, `target`, and `checks`

## Outputs

- deterministic assertion evaluation semantics across runners

## Failure Modes

- leaf `target` misuse
- non-list operator values
- invalid `evaluate` expression roots

## Step Shape

`assert` uses one canonical shape:

- list of steps
- each step declares:
  - `id`
  - `class` (`must`, `can`, `cannot`)
  - optional `target`
  - `checks` (non-empty list of assertion nodes)

## Group Semantics

- `must`: all children must pass
- `can`: at least one child must pass
- `cannot`: no child may pass

## Targets

Target is set on an assertion step and inherited by checks/leaves.

Valid:

```yaml
assert:
- id: assert_1
  class: must
  target: stdout
  checks:
  - evaluate:
    - std.string.contains:
      - var: subject
      - ok
```

Invalid:

```yaml
assert:
- id: assert_1
  class: must
  checks:
  - target: stdout
    evaluate:
    - std.string.contains:
      - var: subject
      - ok
```

Why invalid:

- leaf nodes must not include `target`.
- chain-aware cases can assert chain execution state via `target: chain_json`.

## Operators

Canonical operator:

- `evaluate`

All operator values are lists.

`evaluate` uses spec-lang v1 operator-keyed mapping AST nodes:

```yaml
assert:
- target: text
  must:
  - evaluate:
    - std.logic.and:
      - std.string.contains:
        - version
      - std.string.starts_with:
        - var: subject
        - '#'
```

Reference:

- `docs/book/07_spec_lang_reference.md`
- `docs/spec/contract/03b_spec_lang_v1.md`

Tail-recursive example:

```yaml
assert:
- target: text
  must:
  - evaluate:
    - let:
      - lit:
        - - loop
          - - fn
            - - n
              - acc
            - - if
              - - eq
                - - var
                  - n
                - 0
              - - var
                - acc
              - - call
                - - var
                  - loop
                - - sub
                  - - var
                    - n
                  - 1
                - - add
                  - - var
                    - acc
                  - 1
      - eq:
        - call:
          - var:
            - loop
          - 100
          - 0
        - 100
```

## Example: Mixed Assertions

```yaml
assert:
- target: stderr
  cannot:
  - contain:
    - 'ERROR:'
- target: stdout
  can:
  - json_type:
    - list
  - contain:
    - '[]'
- target: chain_json
  must:
  - evaluate:
    - std.object.has_key:
      - var: subject
      - state
```

## Markdown Assertions Cookbook

Prefer library-backed markdown predicates over raw token checks.

```yaml
assert:
- target: context_json
  must:
  - evaluate:
    - call:
      - {var: domain.markdown.required_sections_present}
      - {var: subject}
      - lit:
        - Purpose
        - Inputs
        - Outputs
    - call:
      - {var: domain.markdown.link_targets_all_resolve}
      - {var: subject}
    - call:
      - {var: domain.markdown.has_yaml_spec_test_fence}
      - {var: subject}
```

Use `target: text` only for literal obligations where structure is not the
goal:

```yaml
assert:
- target: text
  must:
  - contain:
    - "Spec-Version: 1"
```

Anti-pattern:

- broad `std.string.contains` checks for headings/links/tokens when
  `domain.markdown.*` / `domain.markdown.*` helpers exist.

## `stdout_path` / `stdout_path_text`

For `cli.run`:

- `stdout_path` uses first non-empty line of stdout as a path.
- Adapter code resolves existence; spec-lang receives a normalized boolean.
- `stdout_path.exists` only supports `true` (or `null`) values.
- `stdout_path_text` reads that file content and applies text assertions.

## Assertion Health

`assert_health.mode` controls diagnostics:

- `ignore`
- `warn`
- `error`

Common diagnostic examples:

- `AH001`: empty `contain` (always true)
- `AH002`: always-true regex
- `AH003`: duplicate operator values
- `AH004`: redundant sibling branches
- `AH005`: non-portable regex constructs

## Troubleshooting Patterns

Symptom: `unsupported op: ...`

- Cause: non-canonical operator key.
- Fix: use one of the supported operators.

Symptom: `assertion leaf requires inherited target`

- Cause: leaf exists without parent target.
- Fix: move `target` to the containing group node.

Symptom: `assert group must include exactly one key`

- Cause: multiple group keys in one node.
- Fix: split into separate group nodes.

## Checklist

- Every leaf has an inherited target.
- Every operator value is a list.
- Group nodes use exactly one of `must/can/cannot`.
- Sugar is the default authoring form unless `evaluate` is required.
- Portable regex subset is used when cross-runtime parity matters.

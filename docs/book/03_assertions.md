# Chapter 3: Assertions

```yaml doc-meta
doc_id: DOC-REF-004
title: Chapter 3 Assertions
status: active
audience: author
owns_tokens:
- must
- may
- must_not
- evaluate
requires_tokens:
- spec-lang
commands:
- run: python -m spec_runner.spec_lang_commands spec-lang-format --check docs/spec
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

- `contract` step lists with `id`, `class`, `target`, and `asserts`

## Outputs

- deterministic assertion evaluation semantics across runners

## Failure Modes

- leaf `target` misuse
- non-list operator values
- invalid `evaluate` expression roots

## Step Shape

`contract` uses one canonical shape:

- list of steps
- each step declares:
  - `id`
  - `class` (`MUST`, `MAY`, `MUST_NOT`)
  - optional `target`
  - `asserts` (non-empty list of assertion nodes)

## Group Semantics

- `MUST`: all children must pass
- `MAY`: at least one child must pass
- `MUST_NOT`: no child may pass
- Legacy wording synonyms:
  - `can` corresponds to `MAY`
  - `cannot` corresponds to `MUST_NOT`

## Targets

Target is set on an assertion step and inherited by checks/leaves.

Valid:

```yaml
contract:
- id: assert_1
  class: MUST
  target: stdout
  asserts:
  - evaluate:
      std.string.contains:
      - var: subject
      - ok
```

Invalid:

```yaml
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      std.string.contains:
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
contract:
- id: assert_1
  class: MUST
  target: text
  asserts:
  - evaluate:
      std.logic.and:
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
contract:
- id: assert_1
  class: MUST
  target: text
  asserts:
  - evaluate:
      let:
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
contract:
- id: assert_1
  class: MUST_NOT
  target: stderr
  asserts:
  - evaluate:
      std.string.contains:
      - var: subject
      - 'ERROR:'
- id: assert_2
  class: MAY
  target: stdout
  asserts:
  - evaluate:
      std.type.json_type:
      - var: subject
      - list
  - evaluate:
      std.string.contains:
      - var: subject
      - '[]'
- id: assert_3
  class: MUST
  target: chain_json
  asserts:
  - evaluate:
      std.object.has_key:
      - var: subject
      - state
```

## Markdown Assertions Cookbook

Prefer library-backed markdown predicates over raw token checks.

```yaml
contract:
- id: assert_1
  class: MUST
  target: context_json
  asserts:
  - evaluate:
      call:
      - {var: domain.markdown.required_sections_present}
      - {var: subject}
      - lit:
        - Purpose
        - Inputs
        - Outputs
  - evaluate:
      call:
      - {var: domain.markdown.link_targets_all_resolve}
      - {var: subject}
  - evaluate:
      call:
      - {var: domain.markdown.has_yaml_contract_spec_fence}
      - {var: subject}
```

Use `target: text` only for literal obligations where structure is not the
goal:

```yaml
contract:
- id: assert_1
  class: MUST
  target: text
  asserts:
  - evaluate:
      std.string.contains:
      - var: subject
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

- duplicate operator values
- redundant sibling branches
- non-portable expression patterns

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
- Every operator value is valid mapping-AST.
- Steps use `class: MUST|MAY|MUST_NOT`.
- Author with `evaluate` expressions.

## Chain Export Migration

Legacy per-symbol export blocks are no longer canonical:

```yaml
exports:
- as: domain.markdown.has_heading
  from: assert.function
  path: /domain.markdown.has_heading
  required: true
- as: domain.markdown.required_sections_present
  from: assert.function
  path: /domain.markdown.required_sections_present
  required: true
```

Use compact symbol-batch export form:

```yaml
exports:
- from: assert.function
  required: true
  symbols:
  - domain.markdown.has_heading
  - domain.markdown.required_sections_present
```

# Chapter 7: Spec-Lang Reference (`evaluate`)

```yaml doc-meta
doc_id: DOC-REF-007
title: Chapter 7 Spec-Lang Reference
status: active
audience: reviewer
owns_tokens:
- spec-lang
- tail-call-optimization
- spec_lang_forms
requires_tokens:
- minimal_examples
commands:
- run: ./runners/public/runner_adapter.sh --impl rust spec-lang-format --check --cases specs
  purpose: Enforce canonical evaluate formatting in specs.
examples:
- id: EX-SPECLANG-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

This chapter is the strict semantic reference for the `evaluate` assertion leaf.

Normative profile references:

- `/specs/schema/spec_lang_stdlib_profile_v1.yaml`
- `/specs/contract/19_spec_lang_stdlib_profile_v1.md`

Authoring note:

- Authoring is evaluate-first in contract-critical surfaces.

## Purpose

Provide a complete, deterministic reference for spec-lang `evaluate`.

## Inputs

- assertion leaf expressions encoded as operator-keyed mapping AST nodes

## Outputs

- portable predicate behavior and consistent evaluator diagnostics

## Failure Modes

- malformed expression shape
- unsupported symbols/arity/type mismatches
- evaluator budget exhaustion

## 1) What `evaluate` Is

`evaluate` runs a spec-lang expression against the assertion target subject.
The expression must be operator-keyed mapping AST form.

Example:

```yaml
contract:
- id: assert_1
  class: MUST
  target: text
  asserts:
  -       std.string.contains:
      - var: subject
      - hello
```

Each `evaluate` item is one expression. The expression result is coerced to
boolean for assertion pass/fail.

## 2) Expression Shape

Valid form:

```yaml
contains:
- hello
```

Invalid forms:

- list-root expressions (`["contains", ...]`)
- raw list/map literal nodes without `lit`
- multi-key expression mappings
- non-list operator argument values

## 3) Core Forms

Boolean:

- `std.logic.and`
- `std.logic.or`
- `std.logic.not`

Value/text:

- `std.string.contains`
- `std.string.starts_with`
- `std.string.ends_with`
- `std.logic.eq`
- `std.logic.neq`

JSON/value:

- `std.type.json_type`
- `std.object.has_key`
- `std.object.get`

Utility:

- `len`
- `count`
- `first`
- `rest`
- `trim`
- `lower`
- `upper`
- `split`
- `join`
- `map`
- `filter`
- `reject`
- `find`
- `reduce`
- `partition`
- `group_by`
- `uniq_by`
- `flatten`
- `concat`
- `append`
- `prepend`
- `take`
- `drop`
- `any`
- `all`
- `none`
- `var`
- `add`
- `sub`
- `lt`
- `lte`
- `gt`
- `gte`
- `matches`
- `equals`
- `includes`
- `union`
- `intersection`
- `difference`
- `symmetric_difference`
- `is_subset`
- `is_superset`
- `set_equals`

Control/recursion:

- `if`
- `let`
- `fn`
- `call`

## 4) Common Patterns

Text + boolean composition:

```yaml
-     std.logic.and:
    - std.string.contains:
      - WARN
    - std.logic.not:
      - std.string.contains:
        - ERROR
```

JSON field check (for `target: body_json`):

```yaml
-     std.logic.and:
    - std.object.has_key:
      - items
    - std.logic.eq:
      - std.type.json_type:
        - std.object.get:
          - var: subject
          - items
      - true
```

Tail recursion (stack-safe by contract):

```yaml
-     let:
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
        - 1000
        - 0
      - 1000
```

Set algebra + deep equality:

```yaml
-     std.set.intersection:
    - std.json.parse:
      - '[{"k":1},{"k":2},{"k":2}]'
    - std.json.parse:
      - '[{"k":2},{"k":3}]'
```

Currying with collection forms:

```yaml
-     map:
    - call:
      - var:
        - add
      - 10
    - std.json.parse:
      - '[1,2,3]'
```

## 4.5) Domain Helper Preference For FS Workflows

In executable specs, prefer domain helpers over raw filesystem primitives.

| Primitive family | Preferred helper family |
| --- | --- |
| path normalization/ordering | `domain.path.*` |
| file metadata predicates | `domain.file.*` |
| json text path lookups | `domain.fs.json_*` |
| glob filtering/matching | `domain.fs.glob_*` |

Use raw `ops.fs.*` directly only in stdlib primitive conformance and domain-library implementation specs.

## 5) Budgets (`harness.spec_lang`)

Optional per-case evaluator limits:

```yaml
harness:
  spec_lang:
    max_steps: 20000
    max_nodes: 20000
    max_literal_bytes: 262144
    timeout_ms: 200
```

Rules:

- all values are integers
- `max_steps`, `max_nodes`, `max_literal_bytes` must be `>= 1`
- `timeout_ms` must be `>= 0` (`0` disables timeout)

## 6) Error Categories

- malformed form / unknown symbol / arity/type issues: `schema`
- expression returns false in `must`: `assertion`
- budget/timeout/execution faults: `runtime`

Typical diagnostics include:

- `case_id=...`
- `assert_path=...`
- `target=...`
- `op=evaluate`

## 7) Evaluate-Only Guidance

Use `evaluate` for all contract assertions. Use standard library operators
inside the expression when you need:

- composable boolean logic
- value/JSON-aware checks
- deterministic recursive logic in the spec itself

## 8) Cross-References

- `specs/schema/schema_v1.md`
- `specs/contract/03_assertions.md`
- `specs/contract/03b_spec_lang_v1.md`
- `specs/contract/14_spec_lang_libraries.md`
- `specs/conformance/cases/core/spec_lang.spec.md`

## 9) Lint + Format

Use the repo tool to keep `evaluate` layout canonical:

```sh
./runners/public/runner_adapter.sh --impl rust spec-lang-format --check --cases specs
./runners/public/runner_adapter.sh --impl rust spec-lang-format --write --cases specs
```

# Assertion Contract (v1)

## Tree Model

`clauses` uses mapping form:

- `defaults` (optional mapping)
- `predicates` (required non-empty list)

Each predicate has:

- `id` (string)
- `purpose` (optional string)
- `required` (optional bool, default `true`)
- `priority` (optional int, default `1`; must be `>=1`)
- `severity` (optional int, default `1`; must be `>=1`)
- `imports` (optional list of import items)
- `assert` (non-empty expression mapping or list)

prior forms are forbidden:

- top-level list `clauses: [...]`
- predicate key `asserts`
- predicate keys `target` / `on`

## Explicit Import Bindings

Assertions must consume explicitly imported values.

Import binding shape:

- `imports` is a list of mapping items
- each item must be `{from, names, as?}`
- assertion imports are artifact-only in canonical v1 (`from: artifact`)
- `names` is a non-empty list of artifact keys
- `as` is optional mapping of `source_name -> local_name`
- when `as` is omitted, local symbol defaults to each `names[]` entry

Import merge semantics:

- effective imports = `clauses.imports` + `clauses.predicates[].imports`
- predicate imports override same-name defaults

`{var: subject}` is valid only when `subject` is imported explicitly.

## Step Semantics

- `required: true` (or omitted): predicate failure fails the case.
- `required: false`: predicate still evaluates; failure is recorded but does not fail
  overall case verdict.
- `priority` and `severity` are metadata-only for reporting/triage and do not
  affect execution order or pass/fail computation.
- prohibition assertions are authored explicitly with negation operators
  (for example `std.logic.not`).

## Governance Artifact Keys

For `type: contract.check` with governance profile, common artifact imports include:

- `text`
- `summary_json`
- `violation_count`
- `meta_json`

Example:

```yaml
clauses:
  defaults: {}
  imports:
  - from: artifact
    names: [violation_count]
    as:
      violation_count: subject
  predicates:
  - id: assert_1
    purpose: Ensures no governance violations are reported.
    required: true
    priority: 1
    severity: 1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
```

## Leaf Operators

Runtime decision semantics are evaluate-only through spec-lang mapping AST expressions.

Normative references:

- `specs/contract/03b_spec_lang_v1.md`
- `specs/contract/09_internal_representation.md`

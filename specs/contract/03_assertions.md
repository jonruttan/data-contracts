# Assertion Contract (v1)

## Tree Model

`asserts` uses mapping form:

- `defaults` (optional mapping)
- `checks` (required non-empty list)

Each check has:

- `id` (required string)
- `purpose` (optional string)
- `required` (optional bool, default `true`)
- `priority` (optional int, default `1`; must be `>=1`)
- `severity` (optional int, default `1`; must be `>=1`)
- `imports` (optional list of import items)
- `assert` (non-empty expression mapping or list)

Check id uniqueness:

- predicate ids must be unique within each predicate list
- missing predicate ids are schema hard-fail

prior forms are forbidden:

- top-level list `asserts: [...]`
- predicate key `asserts`
- predicate keys `target` / `on`

## Explicit Import Bindings

Assertions must consume explicitly imported values.

Scope separation:

- assertion import bindings are declared only under `asserts.imports` and
  `asserts.checks[].imports`.
- suite-root `artifacts[]` are external
  reference declarations and do not implicitly bind assertion symbols.
- `contracts.clauses[].bindings.rows[]` materializes service-produced symbols into predicate
  contexts using artifact-id I/O mappings.
- binding I/O rows accept canonical mappings and compact string aliases; compact
  rows are endpoint-only (`to` for outputs, `from` for inputs).
- service locator values consumed by bindings/imports must be declared in
  `artifacts[]`; assertion/runtime surfaces must not rely on direct
  service config locators.
- suite/contract/artifact/function documentation metadata is declared through
  `docs[]` entries and is not part of assertion symbol binding.

Import binding shape:

- `imports` is a list of canonical mapping rows
- canonical row form is `{from, names, service?, as?}`
- compact/short alias rows are invalid in v2
- canonical sources are `artifact` and `service`
- for `from: artifact`, imported names MUST be explicitly declared at suite
  root (`artifacts[].id`)
- runtime-produced artifact symbols MUST be explicitly wired through
  `contracts.clauses[].bindings.rows[].outputs` before predicate import use
- when any item uses `from: service`, suite-root `services` MUST be present and
  valid
- when `from: service`, `service` key is required and must reference suite `services[].operations[].id`
- referenced service actions must use integration-only catalog types (`io.*`);
  legacy orchestration service types are invalid in v2
- `names` is a non-empty list of imported symbol keys
- `as` is optional mapping of `source_name -> local_name`
- when `as` is omitted, local symbol defaults to each `names[]` entry
- requiredness terminology:
  - explicit-required: key must be authored
  - optional: key may be omitted
  - effective-required: key may be inherited but must exist after merge

Uniform terminology:

- accepted input forms: parser-supported canonical row shape
- preferred authoring form: canonical rows
- canonical normalized form: canonical row shape before validation/evaluation

Import merge semantics:

- effective imports = `asserts.imports` + `asserts.checks[].imports`
- predicate imports override same-name defaults
- `asserts.defaults` may provide inherited assertion-level defaults; explicit row
  values always override inherited defaults
- binding-piped symbols from `contracts.clauses[].bindings.rows[]` are applied after import merge:
  - `mode: merge` preserves explicit import values on collisions
  - `mode: override` replaces explicit import values on collisions
- implicit harness/service symbol injection is forbidden

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

For `harness: check` governance profiles (for example
`clauses.profile: governance.scan`), common artifact imports include:

- `text`
- `summary_json`
- `violation_count`
- `meta_json`

Example:

```yaml
asserts:
  defaults: {}
  imports:
  - from: artifact
    names: [violation_count]
    as:
      violation_count: subject
  checks:
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

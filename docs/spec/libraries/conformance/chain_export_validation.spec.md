# Chain Export Validation Fixtures

This file is intentionally non-executable as a standalone conformance surface.
It provides producer cases referenced by conformance negative tests.

## BAD-EXPORT-PATH

```yaml spec-test
id: BAD-EXPORT-PATH
type: spec.export
assert:
- id: valid_step
  class: must
  checks:
  - std.logic.eq:
    - var: subject
    - var: subject
harness:
  chain:
    exports:
    - as: bad.path.symbol
      from: assert.function
      path: /missing_step
      params:
      - subject
      required: true
```

## BAD-EXPORT-CLASS

```yaml spec-test
id: BAD-EXPORT-CLASS
type: spec.export
assert:
- id: non_must_step
  class: can
  checks:
  - std.logic.eq:
    - var: subject
    - var: subject
harness:
  chain:
    exports:
    - as: bad.class.symbol
      from: assert.function
      path: /non_must_step
      params:
      - subject
      required: true
```

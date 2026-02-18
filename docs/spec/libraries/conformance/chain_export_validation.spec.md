# Chain Export Validation Fixtures

This file is intentionally non-executable as a standalone conformance surface.
It provides producer cases referenced by conformance negative tests.

## BAD-EXPORT-PATH

```yaml contract-spec
id: BAD-EXPORT-PATH
type: spec.export
contract:
- id: valid_step
  class: must
  asserts:
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

```yaml contract-spec
id: BAD-EXPORT-CLASS
type: spec.export
contract:
- id: non_must_step
  class: can
  asserts:
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

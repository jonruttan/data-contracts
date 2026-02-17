# Spec-Lang Python Domain Library

## LIB-DOMAIN-PY-001

```yaml spec-test
id: LIB-DOMAIN-PY-001
title: python projection helper functions
type: spec.export
assert:
- id: __export__py.is_tuple_projection
  class: must
  checks:
  - std.logic.eq:
    - std.object.get:
      - std.object.get:
        - var: subject
        - meta
      - native_kind
    - python.tuple
harness:
  chain:
    exports:
    - as: py.is_tuple_projection
      from: assert.function
      path: /__export__py.is_tuple_projection
      params:
      - subject
      required: true
```

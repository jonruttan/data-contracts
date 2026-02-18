# Spec-Lang Python Domain Library

## LIB-DOMAIN-PY-001

```yaml contract-spec
id: LIB-DOMAIN-PY-001
title: python projection helper functions
type: contract.export
contract:
- id: __export__py.is_tuple_projection
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            std.logic.eq:
            - std.object.get:
              - std.object.get:
                - {var: subject}
                - meta
              - native_kind
            - python.tuple
harness:
  exports:
  - as: py.is_tuple_projection
    from: assert.function
    path: /__export__py.is_tuple_projection
    params:
    - subject
    required: true
```

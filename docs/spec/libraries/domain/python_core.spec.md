# Spec-Lang Python Domain Library

## LIB-DOMAIN-PY-001

```yaml spec-test
id: LIB-DOMAIN-PY-001
title: python projection helper functions
type: spec_lang.library
defines:
  public:
    py.is_tuple_projection:
      fn:
      - [subject]
      - std.logic.eq:
        - std.object.get:
          - std.object.get:
            - {var: subject}
            - meta
          - native_kind
        - python.tuple
harness:
  chain:
    exports:
    - as: py.is_tuple_projection
      from: assert.function
      path: /py.is_tuple_projection
      required: true
```

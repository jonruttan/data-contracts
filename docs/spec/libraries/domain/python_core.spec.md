# Spec-Lang Python Domain Library

## LIB-DOMAIN-PY-001

```yaml spec-test
id: LIB-DOMAIN-PY-001
title: python projection helper functions
type: spec_lang.library
definitions:
  public:
    py.is_tuple_projection:
      fn:
      - [subject]
      - eq:
        - get:
          - get:
            - {var: subject}
            - meta
          - native_kind
        - python.tuple
```

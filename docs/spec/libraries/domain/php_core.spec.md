# Spec-Lang PHP Domain Library

## LIB-DOMAIN-PHP-001

```yaml contract-spec
id: LIB-DOMAIN-PHP-001
title: php projection helper functions
type: spec.export
contract:
- id: __export__php.is_assoc_projection
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - std.object.get:
        - var: subject
        - meta
      - php_array_kind
    - assoc
harness:
  exports:
  - as: php.is_assoc_projection
    from: assert.function
    path: /__export__php.is_assoc_projection
    params:
    - subject
    required: true
```

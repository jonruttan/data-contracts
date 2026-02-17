# Spec-Lang PHP Domain Library

## LIB-DOMAIN-PHP-001

```yaml spec-test
id: LIB-DOMAIN-PHP-001
title: php projection helper functions
type: spec.export
assert:
- id: __export__php.is_assoc_projection
  class: must
  checks:
  - std.logic.eq:
    - std.object.get:
      - std.object.get:
        - var: subject
        - meta
      - php_array_kind
    - assoc
harness:
  chain:
    exports:
    - as: php.is_assoc_projection
      from: assert.function
      path: /__export__php.is_assoc_projection
      params:
      - subject
      required: true
```

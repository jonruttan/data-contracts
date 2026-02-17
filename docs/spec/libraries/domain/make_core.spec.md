# Spec-Lang Makefile Domain Library

## LIB-DOMAIN-MAKE-001

```yaml spec-test
id: LIB-DOMAIN-MAKE-001
title: makefile projection helper functions
type: spec.export
assert:
- id: __export__make.has_target
  class: must
  checks:
  - std.string.contains:
    - std.object.get:
      - var: subject
      - value
    - var: target
harness:
  chain:
    exports:
    - as: make.has_target
      from: assert.function
      path: /__export__make.has_target
      params:
      - subject
      - target
      required: true
```

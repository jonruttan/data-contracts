# Spec-Lang Makefile Domain Library

## LIB-DOMAIN-MAKE-001

```yaml contract-spec
id: LIB-DOMAIN-MAKE-001
title: makefile projection helper functions
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__make.has_target
    assert:
      std.string.contains:
      - std.object.get:
        - {var: subject}
        - value
      - {var: target}
harness:
  exports:
  - as: make.has_target
    from: assert.function
    path: /__export__make.has_target
    params:
    - subject
    - target
    required: true
```

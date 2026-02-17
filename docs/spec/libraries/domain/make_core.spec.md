# Spec-Lang Makefile Domain Library

## LIB-DOMAIN-MAKE-001

```yaml spec-test
id: LIB-DOMAIN-MAKE-001
title: makefile projection helper functions
type: spec_lang.library
defines:
  public:
    make.has_target:
      fn:
      - [subject, target]
      - std.string.contains:
        - std.object.get:
          - {var: subject}
          - value
        - {var: target}
harness:
  chain:
    exports:
    - as: make.has_target
      from: assert.function
      path: /make.has_target
      required: true
```

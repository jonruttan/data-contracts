# PHP Spec Runner Library Export References

## SRPHP-RUN-LIB-001

```yaml spec-test
id: SRPHP-RUN-LIB-001
title: impl assertion library exports are referenced by impl fixtures
purpose: References impl assertion library exports for governance usage tracking.
type: text.file
harness:
  chain:
    steps:
    - id: lib_assertion_core_spec
      class: must
      ref: /docs/spec/libraries/impl/assertion_core.spec.md
      exports:
      - as: impl.assert.contains
        from: library.symbol
        required: true
        path: /impl.assert.contains
      - as: impl.assert.regex
        from: library.symbol
        required: true
        path: /impl.assert.regex
      - as: impl.assert.json_type
        from: library.symbol
        required: true
        path: /impl.assert.json_type
    imports:
    - from: lib_assertion_core_spec
      names:
      - impl.assert.contains
      - impl.assert.regex
      - impl.assert.json_type
expect:
  portable:
    status: pass
    category: null
assert:
- id: assert_1
  class: must
  checks:
  - std.string.contains:
    - var: subject
    - '# PHP Spec Runner Library Export References'
  target: text
```

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
        impl.assert.contains:
          from: library.symbol
          path: /impl.assert.contains
          required: true
        impl.assert.regex:
          from: library.symbol
          path: /impl.assert.regex
          required: true
        impl.assert.json_type:
          from: library.symbol
          path: /impl.assert.json_type
          required: true
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
- target: text
  must:
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - '# PHP Spec Runner Library Export References'
```

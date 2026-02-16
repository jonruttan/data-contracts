# PHP Spec Runner Library Export References

## SRPHP-RUN-LIB-001

```yaml spec-test
id: SRPHP-RUN-LIB-001
title: impl assertion library exports are referenced by impl fixtures
purpose: References impl assertion library exports for governance usage tracking.
type: text.file
harness:
  spec_lang:
    includes:
    - /docs/spec/libraries/impl/assertion_core.spec.md
    exports:
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
    - contains:
      - {var: subject}
      - '# PHP Spec Runner Library Export References'
```

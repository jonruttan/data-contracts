# PHP Spec Runner Library Export References

## SRPHP-RUN-LIB-001

```yaml contract-spec
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
    imports:
    - from: lib_assertion_core_spec
      names:
      - impl.assert.contains
      - impl.assert.json_type
      - impl.assert.regex
expect:
  portable:
    status: pass
    category: null
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.string.contains:
    - var: subject
    - '# PHP Spec Runner Library Export References'
  target: text
```

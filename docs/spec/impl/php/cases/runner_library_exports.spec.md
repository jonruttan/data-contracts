# PHP Spec Runner Library Export References

## SRPHP-RUN-LIB-001

```yaml contract-spec
id: SRPHP-RUN-LIB-001
title: impl assertion library exports are referenced by impl fixtures
purpose: References impl assertion library exports for governance usage tracking.
type: contract.check
harness:
  chain:
    steps:
    - id: lib_assertion_core_spec
      class: MUST
      ref: /docs/spec/libraries/impl/assertion_core.spec.md
    imports:
    - from: lib_assertion_core_spec
      names:
      - impl.assert.contains
      - impl.assert.json_type
      - impl.assert.regex
  check:
    profile: text.file
    config: {}
expect:
  portable:
    status: pass
    category: null
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.string.contains:
          - {var: subject}
          - '# PHP Spec Runner Library Export References'
  target: text
```

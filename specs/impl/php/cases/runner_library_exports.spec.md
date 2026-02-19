# PHP Spec Runner Library Export References

## SRPHP-RUN-LIB-001

```yaml contract-spec
id: SRPHP-RUN-LIB-001
title: impl assertion library exports are referenced by impl fixtures
purpose: References impl assertion library exports for governance usage tracking.
type: contract.check
harness:
  check:
    profile: text.file
    config: {}
  use:
  - ref: /specs/libraries/impl/assertion_core.spec.md
    as: lib_assertion_core_spec
    symbols:
    - impl.assert.contains
    - impl.assert.json_type
    - impl.assert.regex
expect:
  portable:
    status: pass
    category: null
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    assert:
      std.string.contains:
      - {var: subject}
      - '# PHP Spec Runner Library Export References'
    imports:
      subject:
        from: artifact
        key: text
```

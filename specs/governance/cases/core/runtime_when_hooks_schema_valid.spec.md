# Governance Cases

## SRGOV-RUNTIME-HOOKS-001

```yaml contract-spec
id: SRGOV-RUNTIME-HOOKS-001
title: when hooks schema must be valid
purpose: Enforces when shape and hook expression list requirements.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.when_hooks_schema_valid
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    target: violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
```

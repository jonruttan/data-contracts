# Governance Cases

## DCGOV-RUNTIME-HOOKS-001

```yaml contract-spec
id: DCGOV-RUNTIME-HOOKS-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
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
  defaults: {}
  imports:
  - from: artifact
    names:
    - violation_count
  steps:
  - id: assert_1
    assert:
      call:
      - {var: policy.assert.no_violations}
      - std.object.assoc:
        - violation_count
        - {var: violation_count}
        - lit: {}
```

# Governance Cases

## DCGOV-RUNTIME-CONTRACT-SPEC-001

```yaml contract-spec
id: DCGOV-RUNTIME-CONTRACT-SPEC-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: executable case fences must use contract-spec
purpose: Enforces hard-cut fence rename to contract-spec across specs cases.
type: contract.check
contract:
  defaults:
    class: MUST
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
harness:
  check:
    profile: governance.scan
    config:
      check: runtime.contract_spec_fence_required
```

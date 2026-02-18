# Governance Cases

## SRGOV-RUNTIME-CONTRACT-SPEC-001

```yaml contract-spec
id: SRGOV-RUNTIME-CONTRACT-SPEC-001
title: executable case fences must use contract-spec
purpose: Enforces hard-cut fence rename to contract-spec across docs/spec cases.
type: contract.check
contract:
- id: assert_1
  class: MUST
  target: violation_count
  asserts:
  - evaluate:
    - lit:
        std.logic.eq:
        - {var: subject}
        - 0
harness:
  check:
    profile: governance.scan
    config:
      check: runtime.contract_spec_fence_required
```

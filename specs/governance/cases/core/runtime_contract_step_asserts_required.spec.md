# Governance Cases

## SRGOV-RUNTIME-CONTRACT-STEP-001

```yaml contract-spec
id: SRGOV-RUNTIME-CONTRACT-STEP-001
title: contract steps must declare asserts
purpose: Enforces step-form contract nodes to use asserts list and non-empty children.
type: contract.check
contract:
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: violation_count
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
harness:
  check:
    profile: governance.scan
    config:
      check: runtime.contract_step_asserts_required
```

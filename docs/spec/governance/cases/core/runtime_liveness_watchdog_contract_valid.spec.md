# Governance Cases

## SRGOV-LIVENESS-CONTRACT-001

```yaml contract-spec
id: SRGOV-LIVENESS-CONTRACT-001
title: runtime liveness watchdog contract docs and schema are synchronized
purpose: Ensures liveness controls and reason tokens are declared in runtime profiling contract
  and schema artifacts.
type: governance.check
check: runtime.liveness_watchdog_contract_valid
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```

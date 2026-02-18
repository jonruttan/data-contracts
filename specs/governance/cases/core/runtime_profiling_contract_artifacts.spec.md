# Governance Cases

## SRGOV-PROFILE-CONTRACT-001

```yaml contract-spec
id: SRGOV-PROFILE-CONTRACT-001
title: runtime profiling contract artifacts exist and are discoverable
purpose: Ensures run trace schema and profiling contract docs are present and linked in current
  snapshot notes.
type: contract.check
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /specs/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: runtime.profiling_contract_artifacts
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
```


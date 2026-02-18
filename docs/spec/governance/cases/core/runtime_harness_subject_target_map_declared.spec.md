# Governance Cases

## SRGOV-ARCH-COMPONENTS-005

```yaml contract-spec
id: SRGOV-ARCH-COMPONENTS-005
title: harnesses declare target subject maps
purpose: Enforces explicit target-to-subject mapping declarations so assertion targets remain
  deterministic and reviewable.
type: contract.check
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: runtime.harness_subject_target_map_declared
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
```


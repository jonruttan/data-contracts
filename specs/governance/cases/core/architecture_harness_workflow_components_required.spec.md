# Governance Cases

## SRGOV-ARCH-COMPONENTS-001

```yaml contract-spec
id: SRGOV-ARCH-COMPONENTS-001
title: harnesses must use shared workflow components
purpose: Enforces hard-cut architecture by requiring shared execution context, assertion engine,
  and subject router wiring in all harnesses.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: architecture.harness_workflow_components_required
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    'on': violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
```


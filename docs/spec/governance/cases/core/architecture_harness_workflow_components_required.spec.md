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
      check: architecture.harness_workflow_components_required
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.logic.eq:
          - {var: subject}
          - 0
  target: violation_count
```


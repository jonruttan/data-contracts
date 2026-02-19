# Governance Cases

## SRGOV-ARCH-COMPONENTS-002

```yaml contract-spec
id: SRGOV-ARCH-COMPONENTS-002
title: non-canonical harness workflow duplication is forbidden
purpose: Prevents harness modules from reintroducing local spec-lang setup and direct assertion-evaluation
  glue after component hard cut.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: architecture.harness_local_workflow_duplication_forbidden
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


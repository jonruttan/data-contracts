# Governance Cases

## SRGOV-ARCH-COMPONENTS-002

```yaml spec-test
id: SRGOV-ARCH-COMPONENTS-002
title: legacy harness workflow duplication is forbidden
purpose: Prevents harness modules from reintroducing local spec-lang setup and direct assertion-evaluation
  glue after component hard cut.
type: governance.check
check: architecture.harness_local_workflow_duplication_forbidden
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
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```


# Governance Cases

## SRGOV-ARCH-COMPONENTS-001

```yaml spec-test
id: SRGOV-ARCH-COMPONENTS-001
title: harnesses must use shared workflow components
purpose: Enforces hard-cut architecture by requiring shared execution context, assertion engine,
  and subject router wiring in all harnesses.
type: governance.check
check: architecture.harness_workflow_components_required
harness:
  root: .
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
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


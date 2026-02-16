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
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
```


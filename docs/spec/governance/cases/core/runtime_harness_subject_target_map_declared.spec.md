# Governance Cases

## SRGOV-ARCH-COMPONENTS-005

```yaml spec-test
id: SRGOV-ARCH-COMPONENTS-005
title: harnesses declare target subject maps
purpose: Enforces explicit target-to-subject mapping declarations so assertion targets remain
  deterministic and reviewable.
type: governance.check
check: runtime.harness_subject_target_map_declared
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


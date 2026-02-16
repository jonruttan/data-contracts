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


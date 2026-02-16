# Governance Cases

## SRGOV-ARCH-COMPONENTS-003

```yaml spec-test
id: SRGOV-ARCH-COMPONENTS-003
title: harness type overlays are complete
purpose: Ensures behavior-heavy harness types publish non-empty schema overlays for machine
  validation and drift prevention.
type: governance.check
check: schema.harness_type_overlay_complete
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


# Governance Cases

## SRGOV-ARCH-COMPONENTS-003

```yaml contract-spec
id: SRGOV-ARCH-COMPONENTS-003
title: harness type overlays are complete
purpose: Ensures behavior-heavy harness types publish non-empty schema overlays for machine
  validation and drift prevention.
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
      check: schema.harness_type_overlay_complete
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            std.logic.eq:
            - {var: subject}
            - 0
  target: violation_count
```


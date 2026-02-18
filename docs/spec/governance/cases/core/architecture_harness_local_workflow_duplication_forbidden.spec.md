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
      check: architecture.harness_local_workflow_duplication_forbidden
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


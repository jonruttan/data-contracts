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


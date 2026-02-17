# Governance Cases

## SRGOV-LIVENESS-DEPRECATION-001

```yaml spec-test
id: SRGOV-LIVENESS-DEPRECATION-001
title: governance legacy timeout envs are marked deprecated
purpose: Ensures legacy governance timeout environment variables remain documented as deprecated
  and mapped to liveness hard-cap behavior.
type: governance.check
check: runtime.legacy_timeout_envs_deprecated
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

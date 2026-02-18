# Governance Cases

## SRGOV-RUNTIME-TRIAGE-006

```yaml spec-test
id: SRGOV-RUNTIME-TRIAGE-006
title: emergency bypass remains explicit and logged
purpose: Ensures pre-push bypass remains explicit and emits deterministic warning output.
type: governance.check
check: runtime.triage_bypass_logged_required
harness:
  root: .
  triage_bypass_logging:
    path: /.githooks/pre-push
    required_tokens:
    - SPEC_PREPUSH_BYPASS
    - 'WARNING: bypass enabled'
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

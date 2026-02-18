# Governance Cases

## SRGOV-RUNTIME-PREPUSH-002

```yaml spec-test
id: SRGOV-RUNTIME-PREPUSH-002
title: python parity lane is not optional by default in prepush
purpose: Ensures local parity script does not use optional parity env toggles as default behavior.
type: governance.check
check: runtime.prepush_python_parity_not_optional_by_default
harness:
  root: .
  prepush_python_parity:
    path: /scripts/local_ci_parity.sh
    required_tokens:
    - lane_python_parity
    - MODE="${SPEC_PREPUSH_MODE:-parity}"
    forbidden_tokens:
    - SPEC_PREPUSH_PYTHON_PARITY
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

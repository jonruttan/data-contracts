# Governance Cases

## SRGOV-RUNTIME-PREPUSH-001

```yaml spec-test
id: SRGOV-RUNTIME-PREPUSH-001
title: local ci parity script is rust-only
purpose: Ensures local prepush parity flow contains no python parity lane hooks.
type: governance.check
check: runtime.local_ci_parity_python_lane_forbidden
harness:
  root: .
  local_ci_parity_python_lane:
    path: /scripts/local_ci_parity.sh
    required_tokens:
    - MODE="${SPEC_PREPUSH_MODE:-critical}"
    - 'mode=critical: rust-only critical path'
    - expected critical|fast
    forbidden_tokens:
    - lane_python_parity
    - --impl python
    - SPEC_PREPUSH_MODE:-parity
    - python-governance-triage
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

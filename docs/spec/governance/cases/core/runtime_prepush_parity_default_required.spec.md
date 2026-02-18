# Governance Cases

## SRGOV-RUNTIME-PREPUSH-001

```yaml spec-test
id: SRGOV-RUNTIME-PREPUSH-001
title: prepush defaults to parity lane execution
purpose: Ensures prepush default route runs both rust-core and python parity lanes.
type: governance.check
check: runtime.prepush_parity_default_required
harness:
  root: .
  prepush_parity_default:
    files:
    - /scripts/local_ci_parity.sh
    required_tokens:
    - MODE="${SPEC_PREPUSH_MODE:-parity}"
    - lane_rust_core
    - lane_python_parity
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

# Governance Cases

## DCGOV-RUNTIME-PREPUSH-001

```yaml contract-spec
id: DCGOV-RUNTIME-PREPUSH-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: local ci parity script is rust-only
purpose: Ensures local prepush parity flow contains no python parity lane hooks.
type: contract.check
harness:
  root: .
  local_ci_parity_python_lane:
    path: /scripts/ci_gate.sh
    required_tokens:
    - MODE="${SPEC_PREPUSH_MODE:-critical}"
    - 'mode=critical: rust-only critical path'
    - expected critical|fast
    forbidden_tokens:
    - lane_python_parity
    - --impl python
    - SPEC_PREPUSH_MODE:-parity
    - python-governance-triage
  check:
    profile: governance.scan
    config:
      check: runtime.local_ci_parity_python_lane_forbidden
  use:
  - ref: /specs/libraries/policy/policy_assertions.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.assert.no_violations
    - policy.assert.summary_passed
    - policy.assert.summary_check_id
    - policy.assert.scan_pass
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - violation_count
  steps:
  - id: assert_1
    assert:
      call:
      - {var: policy.assert.no_violations}
      - std.object.assoc:
        - violation_count
        - {var: violation_count}
        - lit: {}
```

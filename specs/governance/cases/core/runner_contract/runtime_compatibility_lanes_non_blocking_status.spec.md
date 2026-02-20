# Governance Cases

## DCGOV-RUNTIME-CONFIG-007

```yaml contract-spec
id: DCGOV-RUNTIME-CONFIG-007
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: compatibility lanes remain non-blocking
purpose: Ensures compatibility runtime lanes are present in CI and explicitly non-blocking.
type: contract.check
harness:
  root: .
  compatibility_lanes:
    workflow: /.github/workflows/ci.yml
    required_tokens:
    - compatibility-python-lane: null
    - compatibility-php-lane: null
    - compatibility-node-lane: null
    - compatibility-c-lane: null
    - continue-on-error: true
  check:
    profile: governance.scan
    config:
      check: runtime.compatibility_lanes_non_blocking_status
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

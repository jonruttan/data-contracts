# Governance Cases

## DCGOV-RUNTIME-TRIAGE-006

```yaml contract-spec
id: DCGOV-RUNTIME-TRIAGE-006
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: emergency bypass remains explicit and logged
purpose: Ensures pre-push bypass remains explicit and emits deterministic warning output.
type: contract.check
harness:
  root: .
  triage_bypass_logging:
    path: /.githooks/pre-push
    required_tokens:
    - SPEC_PREPUSH_BYPASS
    - 'WARNING: bypass enabled'
  check:
    profile: governance.scan
    config:
      check: runtime.triage_bypass_logged_required
  use:
  - ref: /specs/libraries/policy/policy_assertions.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.assert.no_violations
    - policy.assert.summary_passed
    - policy.assert.summary_check_id
    - policy.assert.scan_pass
contract:
  defaults: {}
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

# Governance Cases

## DCGOV-RUNTIME-APIHTTP-003

```yaml contract-spec
id: DCGOV-RUNTIME-APIHTTP-003
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: api.http network oauth/request flows require explicit live mode
purpose: Ensures network token/request URLs are only used when harness.api_http.mode is explicitly
  live.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.api_http_live_mode_explicit
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
  - id: assert_2
    assert:
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
    - call:
      - {var: policy.assert.summary_check_id}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
      - runtime.api_http_live_mode_explicit
    imports:
    - from: artifact
      names:
      - summary_json
```

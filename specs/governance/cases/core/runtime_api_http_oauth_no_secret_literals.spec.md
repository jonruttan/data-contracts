# Governance Cases

## DCGOV-RUNTIME-APIHTTP-002

```yaml contract-spec
id: DCGOV-RUNTIME-APIHTTP-002
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: api.http oauth specs contain no secret literals
purpose: Ensures api.http fixtures avoid inline bearer tokens and secret literal OAuth fields.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.api_http_oauth_no_secret_literals
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
      - runtime.api_http_oauth_no_secret_literals
    imports:
    - from: artifact
      names:
      - summary_json
```

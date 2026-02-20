# Governance Cases

## DCGOV-DOCS-APIHTTP-001

```yaml contract-spec
id: DCGOV-DOCS-APIHTTP-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: api.http tutorials remain present in howto and troubleshooting docs
purpose: Ensures contributor docs cover practical REST verbs, CORS preflight, and round-trip
  scenario guidance.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.api_http_tutorial_sync
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
  - id: assert_2
    assert:
      call:
      - {var: policy.assert.summary_check_id}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
      - docs.api_http_tutorial_sync
    imports:
    - from: artifact
      names:
      - summary_json
```

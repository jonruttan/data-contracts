# Governance Cases

## SRGOV-CONF-API-001

```yaml spec-test
id: SRGOV-CONF-API-001
title: api.http portable conformance cases use canonical shape
purpose: Ensures api.http portable fixtures keep setup under harness and use only canonical
  behavior assertion targets.
type: governance.check
check: conformance.api_http_portable_shape
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  api_http:
    allowed_top_level_keys:
    - id
    - type
    - title
    - purpose
    - request
    - assert
    - expect
    - requires
    - assert_health
    - harness
    allowed_assert_targets:
    - status
    - headers
    - body_text
    - body_json
    required_request_fields:
    - method
    - url
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
    - eq:
      - get:
        - {var: subject}
        - check_id
      - conformance.api_http_portable_shape
```

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
  api_http:
    allowed_top_level_keys:
    - id
    - type
    - title
    - purpose
    - request
    - requests
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
    - cors_json
    - steps_json
    - context_json
    required_request_fields:
    - method
    - url
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
      - as: policy.pass_when_no_violations
        from: library.symbol
        required: true
        path: /policy.pass_when_no_violations
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
- id: assert_2
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - conformance.api_http_portable_shape
  target: summary_json
```

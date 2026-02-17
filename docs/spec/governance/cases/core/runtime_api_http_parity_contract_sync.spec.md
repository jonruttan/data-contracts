# Governance Cases

## SRGOV-RUNTIME-APIHTTP-008

```yaml spec-test
id: SRGOV-RUNTIME-APIHTTP-008
title: api.http python/php parity contract surfaces remain synchronized
purpose: Ensures python/php api.http implementations and contracts expose shared v2 tokens.
type: governance.check
check: runtime.api_http_parity_contract_sync
harness:
  root: .
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
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - check_id
    - runtime.api_http_parity_contract_sync
  target: summary_json
```

# Governance Cases

## SRGOV-RUNTIME-APIHTTP-006

```yaml contract-spec
id: SRGOV-RUNTIME-APIHTTP-006
title: api.http CORS support surfaces remain synchronized
purpose: Ensures CORS preflight and normalized cors_json projection are documented
  and implemented.
type: governance.check
check: runtime.api_http_cors_support
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - check_id
    - runtime.api_http_cors_support
  target: summary_json
```

# Governance Cases

## SRGOV-RUNTIME-APIHTTP-006

```yaml spec-test
id: SRGOV-RUNTIME-APIHTTP-006
title: api.http CORS support surfaces remain synchronized
purpose: Ensures CORS preflight and normalized cors_json projection are documented and implemented.
type: governance.check
check: runtime.api_http_cors_support
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - runtime.api_http_cors_support
```

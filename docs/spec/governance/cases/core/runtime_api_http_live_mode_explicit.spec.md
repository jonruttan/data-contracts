# Governance Cases

## SRGOV-RUNTIME-APIHTTP-003

```yaml spec-test
id: SRGOV-RUNTIME-APIHTTP-003
title: api.http network oauth/request flows require explicit live mode
purpose: Ensures network token/request URLs are only used when harness.api_http.mode is explicitly
  live.
type: governance.check
check: runtime.api_http_live_mode_explicit
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
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - runtime.api_http_live_mode_explicit
```

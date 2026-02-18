# Governance Cases

## SRGOV-RUNTIME-APIHTTP-003

```yaml contract-spec
id: SRGOV-RUNTIME-APIHTTP-003
title: api.http network oauth/request flows require explicit live mode
purpose: Ensures network token/request URLs are only used when harness.api_http.mode is explicitly
  live.
type: governance.check
check: runtime.api_http_live_mode_explicit
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
  class: must
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: must
  asserts:
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
      - runtime.api_http_live_mode_explicit
  target: summary_json
```

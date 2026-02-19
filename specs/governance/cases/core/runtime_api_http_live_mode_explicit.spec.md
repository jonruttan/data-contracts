# Governance Cases

## SRGOV-RUNTIME-APIHTTP-003

```yaml contract-spec
id: SRGOV-RUNTIME-APIHTTP-003
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
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - violation_count
    as:
      violation_count: subject
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    assert:
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
    imports:
    - from: artifact
      names:
      - summary_json
      as:
        summary_json: subject
```

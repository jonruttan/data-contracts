# Governance Cases

## SRGOV-RUNTIME-APIHTTP-006

```yaml contract-spec
id: SRGOV-RUNTIME-APIHTTP-006
title: api.http CORS support surfaces remain synchronized
purpose: Ensures CORS preflight and normalized cors_json projection are documented and implemented.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.api_http_cors_support
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
    imports:
      subject:
        from: artifact
        key: violation_count
  - id: assert_2
    assert:
      std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - runtime.api_http_cors_support
    imports:
      subject:
        from: artifact
        key: summary_json
```

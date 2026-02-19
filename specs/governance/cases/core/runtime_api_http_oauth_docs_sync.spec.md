# Governance Cases

## SRGOV-RUNTIME-APIHTTP-004

```yaml contract-spec
id: SRGOV-RUNTIME-APIHTTP-004
title: api.http oauth contract docs remain synchronized
purpose: Ensures schema and contract docs contain the required api.http OAuth profile tokens.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.api_http_oauth_docs_sync
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
    'on': violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    'on': summary_json
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
      - runtime.api_http_oauth_docs_sync
```

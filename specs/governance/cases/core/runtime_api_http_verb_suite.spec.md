# Governance Cases

## SRGOV-RUNTIME-APIHTTP-005

```yaml contract-spec
id: SRGOV-RUNTIME-APIHTTP-005
title: api.http practical verb suite remains covered and validated
purpose: Ensures api.http fixtures cover GET/POST/PUT/PATCH/DELETE/HEAD/OPTIONS and reject
  unsupported methods.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.api_http_verb_suite
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
      std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - runtime.api_http_verb_suite
```

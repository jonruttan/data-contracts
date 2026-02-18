# Governance Cases

## SRGOV-RUNTIME-APIHTTP-002

```yaml contract-spec
id: SRGOV-RUNTIME-APIHTTP-002
title: api.http oauth specs contain no secret literals
purpose: Ensures api.http fixtures avoid inline bearer tokens and secret literal OAuth fields.
type: contract.check
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: runtime.api_http_oauth_no_secret_literals
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            std.logic.eq:
            - {var: subject}
            - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            MUST:
            - std.logic.eq:
              - std.object.get:
                - {var: subject}
                - passed
              - true
            - std.logic.eq:
              - std.object.get:
                - {var: subject}
                - check_id
              - runtime.api_http_oauth_no_secret_literals
  target: summary_json
```

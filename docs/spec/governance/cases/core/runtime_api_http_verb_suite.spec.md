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
      check: runtime.api_http_verb_suite
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
            std.logic.eq:
            - std.object.get:
              - {var: subject}
              - check_id
            - runtime.api_http_verb_suite
  target: summary_json
```

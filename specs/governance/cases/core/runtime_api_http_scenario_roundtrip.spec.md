# Governance Cases

## SRGOV-RUNTIME-APIHTTP-007

```yaml contract-spec
id: SRGOV-RUNTIME-APIHTTP-007
title: api.http scenario roundtrip support remains present
purpose: Ensures requests-list roundtrip support, step templating, and steps_json targeting
  remain implemented.
type: contract.check
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /specs/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: runtime.api_http_scenario_roundtrip
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - check_id
    - runtime.api_http_scenario_roundtrip
  target: summary_json
```

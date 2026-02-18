# Governance Cases

## SRGOV-RUNTIME-APIHTTP-001

```yaml contract-spec
id: SRGOV-RUNTIME-APIHTTP-001
title: api.http oauth credentials use env references only
purpose: Ensures api.http OAuth credential fields are env-reference based and forbid inline
  credential literals.
type: governance.check
check: runtime.api_http_oauth_env_only
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
      - runtime.api_http_oauth_env_only
  target: summary_json
```

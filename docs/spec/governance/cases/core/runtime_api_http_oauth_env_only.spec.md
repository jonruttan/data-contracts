# Governance Cases

## SRGOV-RUNTIME-APIHTTP-001

```yaml spec-test
id: SRGOV-RUNTIME-APIHTTP-001
title: api.http oauth credentials use env references only
purpose: Ensures api.http OAuth credential fields are env-reference based and forbid inline
  credential literals.
type: governance.check
check: runtime.api_http_oauth_env_only
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
      - runtime.api_http_oauth_env_only
```

# Governance Cases

## SRGOV-RUNTIME-APIHTTP-008

```yaml contract-spec
id: SRGOV-RUNTIME-APIHTTP-008
title: api.http python/php parity contract surfaces remain synchronized
purpose: Ensures python/php api.http implementations and contracts expose shared v1 tokens.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.api_http_parity_contract_sync
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
      - runtime.api_http_parity_contract_sync
```

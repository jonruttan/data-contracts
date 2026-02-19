# Governance Cases

## SRGOV-NORM-003

```yaml contract-spec
id: SRGOV-NORM-003
title: normalization docs token sync is enforced
purpose: Ensures schema contract and book docs maintain required mapping-AST wording and forbid
  stale expression-shape tokens.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: normalization.docs_token_sync
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
      - normalization.docs_token_sync
```

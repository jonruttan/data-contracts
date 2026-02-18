# Governance Cases

## SRGOV-NORM-003

```yaml contract-spec
id: SRGOV-NORM-003
title: normalization docs token sync is enforced
purpose: Ensures schema contract and book docs maintain required mapping-AST wording
  and forbid stale expression-shape tokens.
type: governance.check
check: normalization.docs_token_sync
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
  class: MUST
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - MUST:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - normalization.docs_token_sync
  target: summary_json
```

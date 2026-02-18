# Governance Cases

## SRGOV-RUNTIME-ASSERT-AUTH-001

```yaml contract-spec
id: SRGOV-RUNTIME-ASSERT-AUTH-001
title: governance verdict authority lives in assert blocks
purpose: Ensures governance runtime no longer uses policy_evaluate verdict
  branching and enforces assert-driven obligations.
type: governance.check
check: runtime.assert_block_decision_authority_required
harness:
  root: .
  assert_decision_authority:
    path: /scripts/run_governance_specs.py
    required_tokens:
    - governance.check forbids harness.policy_evaluate
    - eval_assert_tree(assert_spec, eval_leaf=_eval_leaf)
    forbidden_tokens:
    - run_governance_policy(
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```

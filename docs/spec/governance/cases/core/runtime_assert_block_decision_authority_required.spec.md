# Governance Cases

## SRGOV-RUNTIME-ASSERT-AUTH-001

```yaml contract-spec
id: SRGOV-RUNTIME-ASSERT-AUTH-001
title: governance verdict authority lives in assert blocks
purpose: Ensures governance runtime no longer uses evaluate verdict branching and enforces
  assert-driven obligations.
type: contract.check
harness:
  root: .
  assert_decision_authority:
    path: /scripts/run_governance_specs.py
    required_tokens:
    - governance.check forbids harness.evaluate
    - eval_assert_tree(assert_spec, eval_leaf=_eval_leaf)
    forbidden_tokens:
    - run_governance_policy(
  check:
    profile: governance.scan
    config:
      check: runtime.assert_block_decision_authority_required
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.logic.eq:
          - {var: subject}
          - 0
  target: violation_count
```

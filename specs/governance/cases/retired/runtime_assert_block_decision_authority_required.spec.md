```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-ASSERT-AUTH-001
  title: governance verdict authority lives in assert blocks
  purpose: Ensures governance runtime no longer uses evaluate verdict branching and enforces assert-driven obligations.
  harness:
    root: "."
    assert_decision_authority:
      path: "/dc-runner-python"
      required_tokens:
      - governance.scan forbids harness.evaluate
      - eval_assert_tree(assert_spec, eval_leaf=_eval_leaf)
      forbidden_tokens:
      - run_governance_policy(
    check:
      profile: governance.scan
      config:
        check: runtime.assert_block_decision_authority_required
  clauses:
    imports:
    - from: artifact
      names:
      - violation_count
    predicates:
    - id: assert_1
      assert:
        std.logic.eq:
        - var: violation_count
        - 0
```

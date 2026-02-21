```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-POLICY-SRC-001
    title: policy source is spec-lang
    purpose: Ensures control-plane policy source contract states spec-lang as the policy verdict authority.
    harness:
      root: .
      policy_source_contract:
        path: /specs/contract/28_spec_lang_policy_execution.md
        required_tokens:
          - Policy verdict logic MUST be encoded
          - Shell scripts MUST NOT be the source of final policy verdict semantics
      check:
        profile: governance.scan
        config:
          check: governance.policy_source_spec_lang_required
    clauses:
      imports:
        - from: artifact
          names:
            - violation_count
      predicates:
        - id: assert_1
          assert:
            call:
          - {var: policy.assert.no_violations}
          - std.object.assoc:
            - violation_count
            - {var: violation_count}
            - lit: {}
```

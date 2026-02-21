```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-REF-TOKENS-001
    title: configured token anchors exist
    purpose: Ensures configured token anchors resolve to existing files and token matches.
    harness:
      root: .
      token_anchors:
        files:
        - path: /specs/contract/03b_spec_lang_v1.md
          tokens:
          - operator-keyed mapping AST
      check:
        profile: governance.scan
        config:
          check: reference.token_anchors_exist
      use:
      - ref: /specs/libraries/policy/policy_assertions.spec.md
        as: lib_policy_core_spec
        symbols:
        - policy.assert.no_violations
        - policy.assert.summary_passed
        - policy.assert.summary_check_id
        - policy.assert.scan_pass
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - summary_json
      predicates:
      - id: assert_1
        assert:
          call:
          - {var: policy.assert.summary_check_id}
          - std.object.assoc:
            - summary_json
            - {var: summary_json}
            - lit: {}
          - reference.token_anchors_exist
```

```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-CHAIN-FROM-004
    title: executable cases forbid spec_lang includes
    purpose: Ensures executable case types do not use harness.spec_lang.includes and load symbols
      through harness.chain.
    harness:
      root: .
      check:
        profile: governance.scan
        config:
          check: runtime.executable_spec_lang_includes_forbidden
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
          - {var: policy.assert.summary_passed}
          - std.object.assoc:
            - summary_json
            - {var: summary_json}
            - lit: {}
```

```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-LIB-SINGLE-001
    title: library cases use single public symbol granularity
    purpose: Ensures each spec_lang.export case defines exactly one symbol under defines.public.
    harness:
      root: .
      check:
        profile: governance.scan
        config:
          check: library.single_public_symbol_per_case_required
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

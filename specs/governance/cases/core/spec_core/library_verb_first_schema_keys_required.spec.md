```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-LIB-VERB-001
    title: library schema uses verb-first key names
    purpose: Ensures spec_lang.export authoring uses defines.public/defines.private and rejects
      non-canonical definitions keys.
    harness:
      root: .
      check:
        profile: governance.scan
        config:
          check: library.verb_first_schema_keys_required
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
          - library.verb_first_schema_keys_required
```

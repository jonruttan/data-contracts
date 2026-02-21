```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-HARNESS-EXPORTS-001
    title: producer exports are declared at harness.exports
    purpose: Ensures producer symbol declarations are declared at harness.exports and non-canonical
      harness.chain.exports is rejected.
    harness:
      root: .
      check:
        profile: governance.scan
        config:
          check: runtime.harness_exports_location_required
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

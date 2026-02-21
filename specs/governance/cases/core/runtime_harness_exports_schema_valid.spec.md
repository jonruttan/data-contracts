```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-HARNESS-EXPORTS-003
    title: harness exports schema is valid
    purpose: Ensures harness.exports entries enforce as/from/path/params/required schema requirements.
    harness:
      root: .
      check:
        profile: governance.scan
        config:
          check: runtime.harness_exports_schema_valid
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

```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-SCHEMA-PIN-003
    title: schema_ref resolves in schema catalog
    purpose: Ensures schema pin validator rejects unknown schema_ref values.
    harness:
      root: .
      schema_pin_validator:
        path: /scripts/spec_schema_pin_validate.sh
        required_tokens:
        - unknown_schema_ref_count
      check:
        profile: governance.scan
        config:
          check: schema.spec_case_schema_ref_known
    clauses:
      defaults: {}
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

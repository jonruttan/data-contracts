```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-SCHEMA-PIN-004
    title: spec_version matches schema_ref major
    purpose: Ensures schema pin validator rejects mismatched spec_version and schema_ref major values.
    harness:
      root: .
      schema_pin_validator:
        path: /scripts/spec_schema_pin_validate.sh
        required_tokens:
        - mismatched_version_count
      check:
        profile: governance.scan
        config:
          check: schema.spec_case_version_matches_schema_ref
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

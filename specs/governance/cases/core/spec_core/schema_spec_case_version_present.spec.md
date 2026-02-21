```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-SCHEMA-PIN-001
  title: spec cases include spec_version
  purpose: Ensures schema pin validator enforces presence of spec_version for all executable contract-spec blocks.
  harness:
    root: "."
    schema_pin_validator:
      path: "/scripts/spec_schema_pin_validate.sh"
      required_tokens:
      - missing_spec_version_count
    check:
      profile: governance.scan
      config:
        check: schema.spec_case_version_present
  clauses:
    imports:
    - from: artifact
      names:
      - violation_count
    predicates:
    - id: assert_1
      assert:
        call:
        - var: policy.assert.no_violations
        - std.object.assoc:
          - violation_count
          - var: violation_count
          - lit: {}
```

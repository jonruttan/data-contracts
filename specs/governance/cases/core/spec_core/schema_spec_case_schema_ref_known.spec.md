# Governance Cases

## DCGOV-SCHEMA-PIN-003

```yaml contract-spec
id: DCGOV-SCHEMA-PIN-003
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: schema_ref resolves in schema catalog
purpose: Ensures schema pin validator rejects unknown schema_ref values.
type: contract.check
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
contract:
  defaults: {}
  imports:
  - from: artifact
    names:
    - violation_count
  steps:
  - id: assert_1
    assert:
      call:
      - {var: policy.assert.no_violations}
      - std.object.assoc:
        - violation_count
        - {var: violation_count}
        - lit: {}
```

```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'schema_pin_validator': {'path': '/scripts/spec_schema_pin_validate.sh', 'required_tokens': ['unknown_schema_ref_count']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'schema.spec_case_schema_ref_known'}}}"
services:
  entries:
  - id: svc.root_schema_pin_validator_path_scripts_spec_schema_pin_validate_sh_required_tokens_unknown_schema_ref_count_check_profile_governance_scan_config_check_schema_spec_case_schema_ref_known.default.1
    type: legacy.root_schema_pin_validator_path_scripts_spec_schema_pin_validate_sh_required_tokens_unknown_schema_ref_count_check_profile_governance_scan_config_check_schema_spec_case_schema_ref_known
    io: io
    profile: default
    config: {}
contracts:
- id: DCGOV-SCHEMA-PIN-003
  title: schema_ref resolves in schema catalog
  purpose: Ensures schema pin validator rejects unknown schema_ref values.
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

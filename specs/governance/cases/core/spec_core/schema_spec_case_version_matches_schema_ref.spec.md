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
    - "{'root': '.', 'schema_pin_validator': {'path': '/scripts/spec_schema_pin_validate.sh', 'required_tokens': ['mismatched_version_count']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'schema.spec_case_version_matches_schema_ref'}}}"
services:
  actions:
  - id: svc.root_schema_pin_validator_path_scripts_spec_schema_pin_validate_sh_required_tokens_mismatched_version_count_check_profile_governance_scan_config_check_schema_spec_case_version_matches_schema_ref.default.1
    type: legacy.root_schema_pin_validator_path_scripts_spec_schema_pin_validate_sh_required_tokens_mismatched_version_count_check_profile_governance_scan_config_check_schema_spec_case_version_matches_schema_ref
    io: io
    profile: default
contracts:
- id: DCGOV-SCHEMA-PIN-004
  title: spec_version matches schema_ref major
  purpose: Ensures schema pin validator rejects mismatched spec_version and schema_ref major values.
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

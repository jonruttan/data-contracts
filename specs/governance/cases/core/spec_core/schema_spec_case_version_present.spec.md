```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'schema_pin_validator': {'path': '/scripts/spec_schema_pin_validate.sh',
      'required_tokens': ['missing_spec_version_count']}, 'check': {'profile': 'governance.scan',
      'config': {'check': 'schema.spec_case_version_present'}}}"
services:
- type: legacy.root_schema_pin_validator_path_scripts_spec_schema_pin_validate_sh_required_tokens_missing_spec_version_count_check_profile_governance_scan_config_check_schema_spec_case_version_present
  operations:
  - id: svc.root_schema_pin_validator_path_scripts_spec_schema_pin_validate_sh_required_tokens_missing_spec_version_count_check_profile_governance_scan_config_check_schema_spec_case_version_present.default.1
    mode: default
    direction: bidirectional
contracts:
  defaults:
    type: contract.check
  clauses:
  - id: DCGOV-SCHEMA-PIN-001
    title: spec cases include spec_version
    purpose: Ensures schema pin validator enforces presence of spec_version for all
      executable contract-spec blocks.
    asserts:
      imports:
      - from: artifact
        names:
        - violation_count
      checks:
      - id: assert_1
        assert:
          call:
          - var: policy.assert.no_violations
          - std.object.assoc:
            - violation_count
            - var: violation_count
            - lit: {}
```

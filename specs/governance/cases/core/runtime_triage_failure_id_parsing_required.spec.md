```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'triage_failure_parser': {'path': '/scripts/governance_triage.sh',
      'required_tokens': ['^ERROR: ([A-Z0-9-]+):', 'parse_error_ids_from_output',
      'build_prefixes_from_ids', 'specs/governance/check_prefix_map_v1.yaml']}, 'check':
      {'profile': 'governance.scan', 'config': {'check': 'runtime.triage_failure_id_parsing_required'}},
      'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id',
      'policy.assert.scan_pass']}]}"
services:
- type: legacy.root_triage_failure_parser_path_scripts_governance_triage_sh_required_tokens_error_a_z0_9_parse_error_ids_from_output_build_prefixes_from_ids_specs_governance_check_prefix_map_v1_yaml_check_profile_governance_scan_config_check_runtime_triage_failure_id_parsing_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  operations:
  - id: svc.root_triage_failure_parser_path_scripts_governance_triage_sh_required_tokens_error_a_z0_9_parse_error_ids_from_output_build_prefixes_from_ids_specs_governance_check_prefix_map_v1_yaml_check_profile_governance_scan_config_check_runtime_triage_failure_id_parsing_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    mode: default
    direction: bidirectional
contracts:
  defaults:
    type: contract.check
  clauses:
  - id: DCGOV-RUNTIME-TRIAGE-005
    title: triage parser derives failing check ids and prefixes
    purpose: Ensures triage script parses governance ERROR lines and maps check ids
      to check-prefix retries.
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

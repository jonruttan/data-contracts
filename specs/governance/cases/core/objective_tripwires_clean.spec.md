```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-OBJECTIVE-003
  title: objective tripwires are clean
  purpose: Ensures objective manifest tripwire checks map to valid governance 
    checks and currently pass.
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
    - id: assert_2
      assert:
      - call:
        - var: policy.assert.summary_passed
        - std.object.assoc:
          - summary_json
          - var: summary_json
          - lit: {}
      - call:
        - var: policy.assert.summary_check_id
        - std.object.assoc:
          - summary_json
          - var: summary_json
          - lit: {}
        - objective.tripwires_clean
      imports:
      - from: artifact
        names:
        - summary_json
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'objective_tripwires': {'manifest_path': '/specs/governance/metrics/objective_manifest.yaml',
      'cases_path': '/specs/governance/cases', 'case_file_pattern': '*.spec.md'},
      'check': {'profile': 'governance.scan', 'config': {'check': 'objective.tripwires_clean'}},
      'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id',
      'policy.assert.scan_pass']}]}"
services:
  entries:
  - id: 
      svc.root_objective_tripwires_manifest_path_specs_governance_metrics_objective_manifest_yaml_cases_path_specs_governance_cases_case_file_pattern_spec_md_check_profile_governance_scan_config_check_objective_tripwires_clean_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: 
      legacy.root_objective_tripwires_manifest_path_specs_governance_metrics_objective_manifest_yaml_cases_path_specs_governance_cases_case_file_pattern_spec_md_check_profile_governance_scan_config_check_objective_tripwires_clean_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
    config: {}
    default: true
```

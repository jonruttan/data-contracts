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
    - "{'root': '.', 'structured_assertions': {'cases_path': '/specs/governance/cases', 'case_file_pattern': '*.spec.md', 'ignore_checks': ['governance.structured_assertions_required']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'governance.structured_assertions_required'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
services:
  entries:
  - id: svc.root_structured_assertions_cases_path_specs_governance_cases_case_file_pattern_spec_md_ignore_checks_governance_structured_assertions_required_check_profile_governance_scan_config_check_governance_structured_assertions_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_structured_assertions_cases_path_specs_governance_cases_case_file_pattern_spec_md_ignore_checks_governance_structured_assertions_required_check_profile_governance_scan_config_check_governance_structured_assertions_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
    config: {}
contracts:
- id: DCGOV-POLICY-REQ-003
  title: governance checks require structured assertion targets
  purpose: Ensures governance cases validate deterministic structured result targets instead of relying on PASS text markers as primary contract truth.
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
        - governance.structured_assertions_required
      imports:
      - from: artifact
        names:
        - summary_json
```

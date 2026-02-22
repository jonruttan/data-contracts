```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'check': {'profile': 'text.file', 'config': {}}, 'use': [{'ref': '#LIB-POLICY-ASSERT-001',
      'as': 'lib_policy_assertions', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed',
      'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
    - "{'exports': [{'as': 'policy.assert.no_violations', 'from': 'assert.function',
      'path': '/__export__policy.assert.no_violations', 'params': ['subject'], 'required':
      True}, {'as': 'policy.assert.summary_passed', 'from': 'assert.function', 'path':
      '/__export__policy.assert.summary_passed', 'params': ['subject'], 'required':
      True}, {'as': 'policy.assert.summary_check_id', 'from': 'assert.function', 'path':
      '/__export__policy.assert.summary_check_id', 'params': ['subject', 'expected_check_id'],
      'required': True}, {'as': 'policy.assert.scan_pass', 'from': 'assert.function',
      'path': '/__export__policy.assert.scan_pass', 'params': ['subject', 'expected_check_id'],
      'required': True}]}"
services:
- type: legacy.exports_as_policy_assert_no_violations_from_assert_function_path_export_policy_assert_no_violations_params_subject_required_true_as_policy_assert_summary_passed_from_assert_function_path_export_policy_assert_summary_passed_params_subject_required_true_as_policy_assert_summary_check_id_from_assert_function_path_export_policy_assert_summary_check_id_params_subject_expected_check_id_required_true_as_policy_assert_scan_pass_from_assert_function_path_export_policy_assert_scan_pass_params_subject_expected_check_id_required_true
  operations:
  - id: svc.exports_as_policy_assert_no_violations_from_assert_function_path_export_policy_assert_no_violations_params_subject_required_true_as_policy_assert_summary_passed_from_assert_function_path_export_policy_assert_summary_passed_params_subject_required_true_as_policy_assert_summary_check_id_from_assert_function_path_export_policy_assert_summary_check_id_params_subject_expected_check_id_required_true_as_policy_assert_scan_pass_from_assert_function_path_export_policy_assert_scan_pass_params_subject_expected_check_id_required_true.default.1
    mode: default
- type: legacy.check_profile_text_file_config_use_ref_lib_policy_assert_001_as_lib_policy_assertions_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  operations:
  - id: svc.check_profile_text_file_config_use_ref_lib_policy_assert_001_as_lib_policy_assertions_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    mode: default
contracts:
  asserts:
  - id: LIB-POLICY-ASSERT-001
    title: reusable scan envelope assertions
    library:
      id: policy.assertions
      module: policy
      stability: alpha
      owner: data-contracts
      tags:
      - policy
      - assertions
    type: contract.export
    asserts:
      checks:
      - id: __export__policy.assert.no_violations
        assert:
          std.logic.eq:
          - std.object.get:
            - var: subject
            - violation_count
          - 0
      - id: __export__policy.assert.summary_passed
        assert:
          std.logic.eq:
          - std.object.get:
            - std.object.get:
              - var: subject
              - summary_json
            - passed
          - true
      - id: __export__policy.assert.summary_check_id
        assert:
          std.logic.eq:
          - std.object.get:
            - std.object.get:
              - var: subject
              - summary_json
            - check_id
          - var: expected_check_id
      - id: __export__policy.assert.scan_pass
        assert:
          std.logic.and:
          - call:
            - var: policy.assert.no_violations
            - var: subject
          - call:
            - var: policy.assert.summary_passed
            - var: subject
          - call:
            - var: policy.assert.summary_check_id
            - var: subject
            - var: expected_check_id
  - id: LIB-POLICY-ASSERT-900
    title: assertions policy library smoke
    type: contract.check
    asserts:
      imports:
      - from: artifact
        names:
        - text
      checks:
      - id: assert_1
        assert:
        - call:
          - var: policy.assert.no_violations
          - lit:
              violation_count: 0
        - std.logic.not:
          - call:
            - var: policy.assert.no_violations
            - lit:
                violation_count: 2
        - call:
          - var: policy.assert.summary_passed
          - lit:
              summary_json:
                passed: true
        - std.logic.not:
          - call:
            - var: policy.assert.summary_passed
            - lit:
                summary_json:
                  passed: false
        - call:
          - var: policy.assert.summary_check_id
          - lit:
              summary_json:
                check_id: docs.reference_manifest_sync
          - docs.reference_manifest_sync
        - std.logic.not:
          - call:
            - var: policy.assert.summary_check_id
            - lit:
                summary_json:
                  check_id: docs.reference_manifest_sync
            - docs.reference_index_sync
        - call:
          - var: policy.assert.scan_pass
          - lit:
              violation_count: 0
              summary_json:
                passed: true
                check_id: docs.reference_manifest_sync
          - docs.reference_manifest_sync
        - std.logic.not:
          - call:
            - var: policy.assert.scan_pass
            - lit:
                violation_count: 1
                summary_json:
                  passed: true
                  check_id: docs.reference_manifest_sync
            - docs.reference_manifest_sync
```



```yaml contract-spec
spec_version: 2
schema_ref: "/specs/01_schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'check': {'profile': 'text.file', 'config': {}}, 'use': [{'ref': '#LIB-POLICY-CI-001', 'as': 'lib_policy_ci', 'symbols': ['policy.ci.required_profiles_pass', 'policy.ci.optional_profile_report_only', 'policy.ci.artifacts_present']}]}"
    - "{'exports': [{'as': 'policy.ci.required_profiles_pass', 'from': 'assert.function', 'path': '/__export__policy.ci.required_profiles_pass', 'params': ['subject'], 'required': True}, {'as': 'policy.ci.optional_profile_report_only', 'from': 'assert.function', 'path': '/__export__policy.ci.optional_profile_report_only', 'params': ['subject'], 'required': True}, {'as': 'policy.ci.artifacts_present', 'from': 'assert.function', 'path': '/__export__policy.ci.artifacts_present', 'params': ['subject'], 'required': True}]}"
contracts:
  asserts:
  - id: LIB-POLICY-CI-001
    title: ci gate predicates
    library:
      id: policy.ci.gate
      module: policy
      stability: alpha
      owner: data-contracts
      tags:
      - policy
      - ci
    type: contract.export
    asserts:
      checks:
      - id: __export__policy.ci.required_profiles_pass
        assert:
          std.logic.eq:
          - std.object.get:
            - std.object.get:
              - var: subject
              - gate_summary
            - status
          - pass
      - id: __export__policy.ci.optional_profile_report_only
        assert:
          std.logic.eq:
          - std.object.get:
            - std.object.get:
              - var: subject
              - optional_report
            - status
          - report-only
      - id: __export__policy.ci.artifacts_present
        assert:
          std.logic.and:
          - std.object.has:
            - var: subject
            - gate_summary
          - std.object.has:
            - var: subject
            - optional_report
  - id: LIB-POLICY-CI-900
    title: ci gate policy library smoke
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
          - var: policy.ci.required_profiles_pass
          - lit:
              gate_summary:
                status: pass
        - call:
          - var: policy.ci.optional_profile_report_only
          - lit:
              optional_report:
                status: report-only
        - call:
          - var: policy.ci.artifacts_present
          - lit:
              gate_summary: {}
              optional_report: {}
adapters:
- type: legacy.exports_as_policy_ci_required_profiles_pass_from_assert_function_path_export_policy_ci_required_profiles_pass_params_subject_required_true_as_policy_ci_optional_profile_report_only_from_assert_function_path_export_policy_ci_optional_profile_report_only_params_subject_required_true_as_policy_ci_artifacts_present_from_assert_function_path_export_policy_ci_artifacts_present_params_subject_required_true
  actions:
  - id: svc.exports_as_policy_ci_required_profiles_pass_from_assert_function_path_export_policy_ci_required_profiles_pass_params_subject_required_true_as_policy_ci_optional_profile_report_only_from_assert_function_path_export_policy_ci_optional_profile_report_only_params_subject_required_true_as_policy_ci_artifacts_present_from_assert_function_path_export_policy_ci_artifacts_present_params_subject_required_true.default.1
    profile: default
- type: legacy.check_profile_text_file_config_use_ref_lib_policy_ci_001_as_lib_policy_ci_symbols_policy_ci_required_profiles_pass_policy_ci_optional_profile_report_only_policy_ci_artifacts_present
  actions:
  - id: svc.check_profile_text_file_config_use_ref_lib_policy_ci_001_as_lib_policy_ci_symbols_policy_ci_required_profiles_pass_policy_ci_optional_profile_report_only_policy_ci_artifacts_present.default.1
    profile: default
services:
- id: svc.exports_as_policy_ci_required_profiles_pass_from_assert_function_path_export_policy_ci_required_profiles_pass_params_subject_required_true_as_policy_ci_optional_profile_report_only_from_assert_function_path_export_policy_ci_optional_profile_report_only_params_subject_required_true_as_policy_ci_artifacts_present_from_assert_function_path_export_policy_ci_artifacts_present_params_subject_required_true.default.1
  consumes:
  - svc.exports_as_policy_ci_required_profiles_pass_from_assert_function_path_export_policy_ci_required_profiles_pass_params_subject_required_true_as_policy_ci_optional_profile_report_only_from_assert_function_path_export_policy_ci_optional_profile_report_only_params_subject_required_true_as_policy_ci_artifacts_present_from_assert_function_path_export_policy_ci_artifacts_present_params_subject_required_true.default.1
- id: svc.check_profile_text_file_config_use_ref_lib_policy_ci_001_as_lib_policy_ci_symbols_policy_ci_required_profiles_pass_policy_ci_optional_profile_report_only_policy_ci_artifacts_present.default.1
  consumes:
  - svc.check_profile_text_file_config_use_ref_lib_policy_ci_001_as_lib_policy_ci_symbols_policy_ci_required_profiles_pass_policy_ci_optional_profile_report_only_policy_ci_artifacts_present.default.1
```



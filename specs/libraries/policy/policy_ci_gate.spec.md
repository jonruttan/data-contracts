```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
contracts:
- id: LIB-POLICY-CI-001
  type: contract.export
  title: ci gate predicates
  clauses:
    predicates:
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
  library:
    id: policy.ci.gate
    module: policy
    stability: alpha
    owner: data-contracts
    tags:
    - policy
    - ci
- id: LIB-POLICY-CI-900
  type: contract.check
  title: ci gate policy library smoke
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
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
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'check': {'profile': 'text.file', 'config': {}}, 'use': [{'ref': '#LIB-POLICY-CI-001',
      'as': 'lib_policy_ci', 'symbols': ['policy.ci.required_profiles_pass', 'policy.ci.optional_profile_report_only',
      'policy.ci.artifacts_present']}]}"
    - "{'exports': [{'as': 'policy.ci.required_profiles_pass', 'from': 'assert.function',
      'path': '/__export__policy.ci.required_profiles_pass', 'params': ['subject'],
      'required': True}, {'as': 'policy.ci.optional_profile_report_only', 'from':
      'assert.function', 'path': '/__export__policy.ci.optional_profile_report_only',
      'params': ['subject'], 'required': True}, {'as': 'policy.ci.artifacts_present',
      'from': 'assert.function', 'path': '/__export__policy.ci.artifacts_present',
      'params': ['subject'], 'required': True}]}"
services:
  defaults:
    io: io
    profile: default
    config: {}
  entries:
  - id: 
      svc.exports_as_policy_ci_required_profiles_pass_from_assert_function_path_export_policy_ci_required_profiles_pass_params_subject_required_true_as_policy_ci_optional_profile_report_only_from_assert_function_path_export_policy_ci_optional_profile_report_only_params_subject_required_true_as_policy_ci_artifacts_present_from_assert_function_path_export_policy_ci_artifacts_present_params_subject_required_true.default.1
    type: 
      legacy.exports_as_policy_ci_required_profiles_pass_from_assert_function_path_export_policy_ci_required_profiles_pass_params_subject_required_true_as_policy_ci_optional_profile_report_only_from_assert_function_path_export_policy_ci_optional_profile_report_only_params_subject_required_true_as_policy_ci_artifacts_present_from_assert_function_path_export_policy_ci_artifacts_present_params_subject_required_true
    default: true
  - id: 
      svc.check_profile_text_file_config_use_ref_lib_policy_ci_001_as_lib_policy_ci_symbols_policy_ci_required_profiles_pass_policy_ci_optional_profile_report_only_policy_ci_artifacts_present.default.1
    type: 
      legacy.check_profile_text_file_config_use_ref_lib_policy_ci_001_as_lib_policy_ci_symbols_policy_ci_required_profiles_pass_policy_ci_optional_profile_report_only_policy_ci_artifacts_present
```



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
    - "{'root': '.', 'ci_python_lane_non_blocking': {'workflow': '/.github/workflows/ci.yml',
      'required_tokens': [{'compatibility-python-lane': None}, {'continue-on-error':
      True}, 'Run Python compatibility lane (non-blocking)'], 'forbidden_tokens':
      [{'python-parity-lane': None}]}, 'check': {'profile': 'governance.scan', 'config':
      {'check': 'runtime.ci_python_lane_non_blocking_required'}}, 'use': [{'ref':
      '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id',
      'policy.assert.scan_pass']}]}"
services:
  actions:
  - id: svc.root_ci_python_lane_non_blocking_workflow_github_workflows_ci_yml_required_tokens_compatibility_python_lane_none_continue_on_error_true_run_python_compatibility_lane_non_blocking_forbidden_tokens_python_parity_lane_none_check_profile_governance_scan_config_check_runtime_ci_python_lane_non_blocking_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_ci_python_lane_non_blocking_workflow_github_workflows_ci_yml_required_tokens_compatibility_python_lane_none_continue_on_error_true_run_python_compatibility_lane_non_blocking_forbidden_tokens_python_parity_lane_none_check_profile_governance_scan_config_check_runtime_ci_python_lane_non_blocking_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-CONFIG-005
  title: python compatibility lane remains non-blocking
  purpose: Ensures Python compatibility lane exists in CI and is configured as non-blocking.
  clauses:
    imports:
    - artifact:
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

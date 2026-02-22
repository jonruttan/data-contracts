```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-CONFIG-007
  title: compatibility lanes remain non-blocking
  purpose: Ensures compatibility runtime lanes are present in CI and explicitly 
    non-blocking.
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
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'compatibility_lanes': {'workflow': '/.github/workflows/ci.yml',
      'required_tokens': [{'compatibility-python-lane': None}, {'compatibility-php-lane':
      None}, {'compatibility-node-lane': None}, {'compatibility-c-lane': None}, {'continue-on-error':
      True}]}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.compatibility_lanes_non_blocking_status'}},
      'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id',
      'policy.assert.scan_pass']}]}"
services:
  entries:
  - id: 
      svc.root_compatibility_lanes_workflow_github_workflows_ci_yml_required_tokens_compatibility_python_lane_none_compatibility_php_lane_none_compatibility_node_lane_none_compatibility_c_lane_none_continue_on_error_true_check_profile_governance_scan_config_check_runtime_compatibility_lanes_non_blocking_status_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: 
      legacy.root_compatibility_lanes_workflow_github_workflows_ci_yml_required_tokens_compatibility_python_lane_none_compatibility_php_lane_none_compatibility_node_lane_none_compatibility_c_lane_none_continue_on_error_true_check_profile_governance_scan_config_check_runtime_compatibility_lanes_non_blocking_status_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
    config: {}
```

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
    - "{'root': '.', 'runner_independence_non_regression': {'baseline_path': '/specs/governance/metrics/runner_independence_baseline.json', 'summary_fields': {'overall_runner_independence_ratio': 'non_decrease', 'direct_runtime_invocation_count': 'non_increase'}, 'segment_fields': {'gate_scripts': {'mean_runner_interface_usage_ratio': 'non_decrease'}}, 'epsilon': 1e-12, 'runner_independence': {'segment_files': {'gate_scripts': ['scripts/ci_gate.sh', 'scripts/ci_gate.sh', 'scripts/control_plane.sh'], 'ci_workflows': ['.github/workflows/*.yml'], 'adapter_interfaces': ['scripts/runner_bin.sh', 'dc-runner-rust', 'dc-runner-rust']}, 'direct_runtime_token_segments': ['gate_scripts', 'ci_workflows']}}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.runner_independence_non_regression'}}, 'use': [{'ref': '/specs/libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.pass_when_no_violations']}]}"
services:
  entries:
  - id: svc.root_runner_independence_non_regression_baseline_path_specs_governance_metrics_runner_independence_baseline_json_summary_fields_overall_runner_independence_ratio_non_decrease_direct_runtime_invocation_count_non_increase_segment_fields_gate_scripts_mean_runner_interface_usage_ratio_non_decrease_epsilon_1e_12_runner_independence_segment_files_gate_scripts_scripts_ci_gate_sh_scripts_ci_gate_sh_scripts_control_plane_sh_ci_workflows_github_workflows_yml_adapter_interfaces_scripts_runner_bin_sh_dc_runner_rust_dc_runner_rust_direct_runtime_token_segments_gate_scripts_ci_workflows_check_profile_governance_scan_config_check_runtime_runner_independence_non_regression_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: legacy.root_runner_independence_non_regression_baseline_path_specs_governance_metrics_runner_independence_baseline_json_summary_fields_overall_runner_independence_ratio_non_decrease_direct_runtime_invocation_count_non_increase_segment_fields_gate_scripts_mean_runner_interface_usage_ratio_non_decrease_epsilon_1e_12_runner_independence_segment_files_gate_scripts_scripts_ci_gate_sh_scripts_ci_gate_sh_scripts_control_plane_sh_ci_workflows_github_workflows_yml_adapter_interfaces_scripts_runner_bin_sh_dc_runner_rust_dc_runner_rust_direct_runtime_token_segments_gate_scripts_ci_workflows_check_profile_governance_scan_config_check_runtime_runner_independence_non_regression_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
    config: {}
contracts:
- id: DCGOV-RUNTIME-INDEP-002
  title: runner independence metric is non-regressing
  purpose: Enforces monotonic non-regression for runner independence metrics against checked-in baseline.
  clauses:
    imports:
    - from: artifact
      names:
      - violation_count
    predicates:
    - id: assert_1
      assert:
        std.logic.eq:
        - var: violation_count
        - 0
    - id: assert_2
      assert:
      - std.logic.eq:
        - std.object.get:
          - var: summary_json
          - passed
        - true
      - std.logic.eq:
        - std.object.get:
          - var: summary_json
          - check_id
        - runtime.runner_independence_non_regression
      imports:
      - from: artifact
        names:
        - summary_json
```

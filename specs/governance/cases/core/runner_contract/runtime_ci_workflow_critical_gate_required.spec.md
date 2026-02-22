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
    - "{'root': '.', 'ci_workflow_critical_gate': {'path': '/.github/workflows/ci.yml', 'required_tokens': ['control-plane-critical-gate:', 'Run control-plane critical gate', './scripts/control_plane.sh critical-gate', 'needs: control-plane-critical-gate', 'continue-on-error: true']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.ci_workflow_critical_gate_required'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
services:
  actions:
  - id: svc.root_ci_workflow_critical_gate_path_github_workflows_ci_yml_required_tokens_control_plane_critical_gate_run_control_plane_critical_gate_scripts_control_plane_sh_critical_gate_needs_control_plane_critical_gate_continue_on_error_true_check_profile_governance_scan_config_check_runtime_ci_workflow_critical_gate_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_ci_workflow_critical_gate_path_github_workflows_ci_yml_required_tokens_control_plane_critical_gate_run_control_plane_critical_gate_scripts_control_plane_sh_critical_gate_needs_control_plane_critical_gate_continue_on_error_true_check_profile_governance_scan_config_check_runtime_ci_workflow_critical_gate_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-TRIAGE-014
  title: ci workflow defines rust critical gate as first-class lane
  purpose: Ensures CI has a dedicated rust critical gate job and diagnostic ci-gate depends on it.
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
```

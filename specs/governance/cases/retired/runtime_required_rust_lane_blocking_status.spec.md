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
    - "{'root': '.', 'required_rust_lane': {'workflow': '/.github/workflows/ci.yml', 'required_tokens': [{'ci-gate': None}, 'Run CI gate (required lane)', {'run': './scripts/ci_gate.sh'}], 'forbidden_tokens': ['Run CI gate (diagnostic lane)', 'continue-on-error: true\\n        run: ./scripts/ci_gate.sh']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.required_rust_lane_blocking_status'}}, 'use': [{'ref': '/specs/libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.pass_when_no_violations']}]}"
services:
  entries:
  - id: svc.root_required_rust_lane_workflow_github_workflows_ci_yml_required_tokens_ci_gate_none_run_ci_gate_required_lane_run_scripts_ci_gate_sh_forbidden_tokens_run_ci_gate_diagnostic_lane_continue_on_error_true_n_run_scripts_ci_gate_sh_check_profile_governance_scan_config_check_runtime_required_rust_lane_blocking_status_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: legacy.root_required_rust_lane_workflow_github_workflows_ci_yml_required_tokens_ci_gate_none_run_ci_gate_required_lane_run_scripts_ci_gate_sh_forbidden_tokens_run_ci_gate_diagnostic_lane_continue_on_error_true_n_run_scripts_ci_gate_sh_check_profile_governance_scan_config_check_runtime_required_rust_lane_blocking_status_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-CONFIG-006
  title: required lane remains blocking
  purpose: Ensures the required CI gate lane is implementation-agnostic and not configured as non-blocking.
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
```

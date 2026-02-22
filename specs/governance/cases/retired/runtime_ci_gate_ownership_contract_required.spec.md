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
    - "{'root': '.', 'ci_gate_ownership_contract': {'gate_path': '/scripts/ci_gate.sh', 'gate_required_tokens': ['critical-gate', 'ci-gate-summary'], 'gate_ordered_tokens': ['critical-gate', 'ci-gate-summary'], 'summary_files': ['/dc-runner-python', '/dc-runner-rust'], 'summary_required_tokens': ['governance_broad', 'triage_phase', 'broad_required'], 'summary_forbidden_tokens': ['governance_critical', 'SPEC_CI_GATE_INCLUDE_CRITICAL', 'SPEC_CI_GATE_SKIP_CRITICAL', '--include-critical']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.ci_gate_ownership_contract_required'}}, 'use': [{'ref': '/specs/libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.pass_when_no_violations']}]}"
services:
  actions:
  - id: svc.root_ci_gate_ownership_contract_gate_path_scripts_ci_gate_sh_gate_required_tokens_critical_gate_ci_gate_summary_gate_ordered_tokens_critical_gate_ci_gate_summary_summary_files_dc_runner_python_dc_runner_rust_summary_required_tokens_governance_broad_triage_phase_broad_required_summary_forbidden_tokens_governance_critical_spec_ci_gate_include_critical_spec_ci_gate_skip_critical_include_critical_check_profile_governance_scan_config_check_runtime_ci_gate_ownership_contract_required_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: legacy.root_ci_gate_ownership_contract_gate_path_scripts_ci_gate_sh_gate_required_tokens_critical_gate_ci_gate_summary_gate_ordered_tokens_critical_gate_ci_gate_summary_summary_files_dc_runner_python_dc_runner_rust_summary_required_tokens_governance_broad_triage_phase_broad_required_summary_forbidden_tokens_governance_critical_spec_ci_gate_include_critical_spec_ci_gate_skip_critical_include_critical_check_profile_governance_scan_config_check_runtime_ci_gate_ownership_contract_required_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-TRIAGE-019
  title: ci gate ownership contract is single-source and broad-only in summary
  purpose: Ensures ci_gate.sh owns critical execution ordering and ci-gate-summary owns broad governance only.
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

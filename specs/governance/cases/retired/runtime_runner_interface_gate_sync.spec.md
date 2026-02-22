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
    - "{'root': '.', 'runner_interface': {'required_paths': ['/scripts/runner_bin.sh', '/dc-runner-python', '/dc-runner-rust'], 'files': ['scripts/ci_gate.sh', 'scripts/control_plane.sh', 'scripts/ci_gate.sh'], 'required_tokens': ['SPEC_RUNNER_BIN', 'scripts/runner_bin.sh'], 'forbidden_tokens': ['spec_lang_commands run-governance-specs', 'dc-runner-python', 'spec_lang_commands spec-lang-format --check specs', 'scripts/conformance_purpose_report.py', 'spec_lang_commands compare-conformance-parity']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.runner_interface_gate_sync'}}, 'use': [{'ref': '/specs/libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.pass_when_no_violations']}]}"
services:
  entries:
  - id: svc.root_runner_interface_required_paths_scripts_runner_bin_sh_dc_runner_python_dc_runner_rust_files_scripts_ci_gate_sh_scripts_control_plane_sh_scripts_ci_gate_sh_required_tokens_spec_runner_bin_scripts_runner_bin_sh_forbidden_tokens_spec_lang_commands_run_governance_specs_dc_runner_python_spec_lang_commands_spec_lang_format_check_specs_scripts_conformance_purpose_report_py_spec_lang_commands_compare_conformance_parity_check_profile_governance_scan_config_check_runtime_runner_interface_gate_sync_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: legacy.root_runner_interface_required_paths_scripts_runner_bin_sh_dc_runner_python_dc_runner_rust_files_scripts_ci_gate_sh_scripts_control_plane_sh_scripts_ci_gate_sh_required_tokens_spec_runner_bin_scripts_runner_bin_sh_forbidden_tokens_spec_lang_commands_run_governance_specs_dc_runner_python_spec_lang_commands_spec_lang_format_check_specs_scripts_conformance_purpose_report_py_spec_lang_commands_compare_conformance_parity_check_profile_governance_scan_config_check_runtime_runner_interface_gate_sync_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
    config: {}
contracts:
- id: DCGOV-RUNTIME-CONFIG-003
  title: gate scripts call runner interface boundary
  purpose: Ensures gate scripts call a runner command boundary instead of hardcoding Python implementation entrypoints.
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
        - runtime.runner_interface_gate_sync
      imports:
      - from: artifact
        names:
        - summary_json
```

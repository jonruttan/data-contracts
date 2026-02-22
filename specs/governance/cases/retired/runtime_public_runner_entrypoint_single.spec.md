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
    - "{'root': '.', 'public_runner_entrypoint': {'required_entrypoint': 'scripts/runner_bin.sh', 'gate_files': ['scripts/ci_gate.sh', 'scripts/ci_gate.sh', 'scripts/control_plane.sh']}, 'forbidden_tokens': ['dc-runner-rust', 'dc-runner-python'], 'forbidden_paths': ['scripts/runner_adapter.sh', 'scripts/rust/runner_adapter.sh', 'scripts/python/runner_adapter.sh', 'scripts/php/conformance_runner.php', 'scripts/php/spec_runner.php'], 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.public_runner_entrypoint_single'}}, 'use': [{'ref': '/specs/libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.pass_when_no_violations']}]}"
services:
  actions:
  - id: svc.root_public_runner_entrypoint_required_entrypoint_scripts_runner_bin_sh_gate_files_scripts_ci_gate_sh_scripts_ci_gate_sh_scripts_control_plane_sh_forbidden_tokens_dc_runner_rust_dc_runner_python_forbidden_paths_scripts_runner_adapter_sh_scripts_rust_runner_adapter_sh_scripts_python_runner_adapter_sh_scripts_php_conformance_runner_php_scripts_php_spec_runner_php_check_profile_governance_scan_config_check_runtime_public_runner_entrypoint_single_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: legacy.root_public_runner_entrypoint_required_entrypoint_scripts_runner_bin_sh_gate_files_scripts_ci_gate_sh_scripts_ci_gate_sh_scripts_control_plane_sh_forbidden_tokens_dc_runner_rust_dc_runner_python_forbidden_paths_scripts_runner_adapter_sh_scripts_rust_runner_adapter_sh_scripts_python_runner_adapter_sh_scripts_php_conformance_runner_php_scripts_php_spec_runner_php_check_profile_governance_scan_config_check_runtime_public_runner_entrypoint_single_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-ENTRY-001
  title: gate scripts use a single public runner entrypoint
  purpose: Ensures gate scripts reference only the canonical public runner entrypoint.
  clauses:
    imports:
    - artifact:
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
          - check_id
        - runtime.public_runner_entrypoint_single
      - std.logic.eq:
        - std.object.get:
          - var: summary_json
          - passed
        - true
      imports:
      - artifact:
        - summary_json
```

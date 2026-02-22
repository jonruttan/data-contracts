```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUST-PRIMARY-008
  title: rust runner interface avoids direct python execution tokens
  purpose: Ensures the Rust runner interface implementation does not hardcode 
    direct python executable invocation.
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
        - runtime.required_lane_adapter_no_python_exec
      imports:
      - from: artifact
        names:
        - summary_json
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'rust_no_python_exec': {'path': '/dc-runner-rust', 'forbidden_tokens':
      ['spec_runner.spec_lang_commands', 'PYTHONPATH', 'python', 'python3', 'PYTHON_BIN',
      'resolve_python_bin', 'scripts/run_governance_specs.py']}, 'check': {'profile':
      'governance.scan', 'config': {'check': 'runtime.required_lane_adapter_no_python_exec'}},
      'use': [{'ref': '/specs/libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.pass_when_no_violations']}]}"
services:
  entries:
  - id: 
      svc.root_rust_no_python_exec_path_dc_runner_rust_forbidden_tokens_spec_runner_spec_lang_commands_pythonpath_python_python3_python_bin_resolve_python_bin_scripts_run_governance_specs_py_check_profile_governance_scan_config_check_runtime_required_lane_adapter_no_python_exec_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: 
      legacy.root_rust_no_python_exec_path_dc_runner_rust_forbidden_tokens_spec_runner_spec_lang_commands_pythonpath_python_python3_python_bin_resolve_python_bin_scripts_run_governance_specs_py_check_profile_governance_scan_config_check_runtime_required_lane_adapter_no_python_exec_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
    config: {}
```

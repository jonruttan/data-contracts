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
    - "{'root': '.', 'rust_transitive_no_python': {'files': ['dc-runner-rust', 'dc-runner-rust'], 'forbidden_tokens': ['scripts/runner_bin.sh', 'spec_runner.spec_lang_commands', 'PYTHONPATH', 'python', 'scripts/run_governance_specs.py']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.required_lane_adapter_transitive_no_python'}}, 'use': [{'ref': '/specs/libraries/policy/policy_core.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.pass_when_no_violations']}]}"
services:
  actions:
  - id: svc.root_rust_transitive_no_python_files_dc_runner_rust_dc_runner_rust_forbidden_tokens_scripts_runner_bin_sh_spec_runner_spec_lang_commands_pythonpath_python_scripts_run_governance_specs_py_check_profile_governance_scan_config_check_runtime_required_lane_adapter_transitive_no_python_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: legacy.root_rust_transitive_no_python_files_dc_runner_rust_dc_runner_rust_forbidden_tokens_scripts_runner_bin_sh_spec_runner_spec_lang_commands_pythonpath_python_scripts_run_governance_specs_py_check_profile_governance_scan_config_check_runtime_required_lane_adapter_transitive_no_python_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-PYDEP-004
  title: rust adapter boundary avoids transitive python delegation tokens
  purpose: Ensures rust adapter boundary files do not delegate to python adapter entrypoints or direct python execution tokens.
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
        - runtime.required_lane_adapter_transitive_no_python
      imports:
      - from: artifact
        names:
        - summary_json
```

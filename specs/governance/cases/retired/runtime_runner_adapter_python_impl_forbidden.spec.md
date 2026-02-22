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
    - '{''root'': ''.'', ''runner_adapter_python_impl'': {''path'': ''/scripts/runner_bin.sh'', ''required_tokens'': [''python runner impl is no longer supported on the runtime path'', ''Use rust impl instead''], ''forbidden_tokens'': [''exec "${ROOT_DIR}/dc-runner-python" "$@"'']}, ''check'': {''profile'': ''governance.scan'', ''config'': {''check'': ''runtime.runner_adapter_python_impl_forbidden''}}, ''use'': [{''ref'': ''/specs/libraries/policy/policy_core.spec.md'', ''as'': ''lib_policy_core_spec'', ''symbols'': [''policy.pass_when_no_violations'']}]}'
services:
  entries:
  - id: svc.root_runner_adapter_python_impl_path_scripts_runner_bin_sh_required_tokens_python_runner_impl_is_no_longer_supported_on_the_runtime_path_use_rust_impl_instead_forbidden_tokens_exec_root_dir_dc_runner_python_check_profile_governance_scan_config_check_runtime_runner_adapter_python_impl_forbidden_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations.default.1
    type: legacy.root_runner_adapter_python_impl_path_scripts_runner_bin_sh_required_tokens_python_runner_impl_is_no_longer_supported_on_the_runtime_path_use_rust_impl_instead_forbidden_tokens_exec_root_dir_dc_runner_python_check_profile_governance_scan_config_check_runtime_runner_adapter_python_impl_forbidden_use_ref_specs_libraries_policy_policy_core_spec_md_as_lib_policy_core_spec_symbols_policy_pass_when_no_violations
    io: io
    profile: default
    config: {}
contracts:
- id: DCGOV-RUNTIME-ENTRY-003
  title: runner adapter hard-fails python impl selection
  purpose: Ensures `scripts/runner_bin.sh` rejects `--impl python` with migration guidance.
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

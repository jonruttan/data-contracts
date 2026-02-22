```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'rust_only_prepush': {'file_token_sets': [{'path': '/scripts/ci_gate.sh', 'required_tokens': ['mode=critical: rust-only critical path'], 'forbidden_tokens': ['lane_python_parity', '--impl python', 'expected critical|parity|fast']}, {'path': '/.githooks/pre-push', 'required_tokens': ['make prepush'], 'forbidden_tokens': ['--impl python', 'SPEC_PREPUSH_MODE=parity']}, {'path': '/Makefile', 'required_tokens': ['SPEC_PREPUSH_MODE=critical ./scripts/ci_gate.sh'], 'forbidden_tokens': ['python-parity:', 'SPEC_PREPUSH_MODE=parity ./scripts/ci_gate.sh']}]}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.required_lane_only_prepush_required'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
services:
- type: legacy.root_rust_only_prepush_file_token_sets_path_scripts_ci_gate_sh_required_tokens_mode_critical_rust_only_critical_path_forbidden_tokens_lane_python_parity_impl_python_expected_critical_parity_fast_path_githooks_pre_push_required_tokens_make_prepush_forbidden_tokens_impl_python_spec_prepush_mode_parity_path_makefile_required_tokens_spec_prepush_mode_critical_scripts_ci_gate_sh_forbidden_tokens_python_parity_spec_prepush_mode_parity_scripts_ci_gate_sh_check_profile_governance_scan_config_check_runtime_required_lane_only_prepush_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  operations:
  - id: svc.root_rust_only_prepush_file_token_sets_path_scripts_ci_gate_sh_required_tokens_mode_critical_rust_only_critical_path_forbidden_tokens_lane_python_parity_impl_python_expected_critical_parity_fast_path_githooks_pre_push_required_tokens_make_prepush_forbidden_tokens_impl_python_spec_prepush_mode_parity_path_makefile_required_tokens_spec_prepush_mode_critical_scripts_ci_gate_sh_forbidden_tokens_python_parity_spec_prepush_mode_parity_scripts_ci_gate_sh_check_profile_governance_scan_config_check_runtime_required_lane_only_prepush_required_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    mode: default
    direction: bidirectional
contracts:
  clauses:
  - id: DCGOV-RUNTIME-PREPUSH-006
    title: prepush path is rust-only
    purpose: Ensures prepush entrypoints and hook routing remain rust-only.
    asserts:
      imports:
      - from: artifact
        names:
        - violation_count
      checks:
      - id: assert_1
        assert:
          call:
          - var: policy.assert.no_violations
          - std.object.assoc:
            - violation_count
            - var: violation_count
            - lit: {}
```

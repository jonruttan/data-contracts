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
    - "{'root': '.', 'make_python_parity': {'path': '/Makefile', 'required_tokens': ['prepush: ## Required local pre-push gate (default rust critical-gate path)', 'SPEC_PREPUSH_MODE=critical ./scripts/ci_gate.sh', 'prepush-fast: ## Rust-only critical pre-push mode'], 'forbidden_tokens': ['python-parity:', '--impl python', 'SPEC_PREPUSH_MODE=parity']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.make_python_parity_targets_forbidden'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
services:
  entries:
  - id: svc.root_make_python_parity_path_makefile_required_tokens_prepush_required_local_pre_push_gate_default_rust_critical_gate_path_spec_prepush_mode_critical_scripts_ci_gate_sh_prepush_fast_rust_only_critical_pre_push_mode_forbidden_tokens_python_parity_impl_python_spec_prepush_mode_parity_check_profile_governance_scan_config_check_runtime_make_python_parity_targets_forbidden_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_make_python_parity_path_makefile_required_tokens_prepush_required_local_pre_push_gate_default_rust_critical_gate_path_spec_prepush_mode_critical_scripts_ci_gate_sh_prepush_fast_rust_only_critical_pre_push_mode_forbidden_tokens_python_parity_impl_python_spec_prepush_mode_parity_check_profile_governance_scan_config_check_runtime_make_python_parity_targets_forbidden_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-PREPUSH-002
  title: makefile contains no python parity prepush targets
  purpose: Ensures contributor-facing make targets do not expose python runner lane execution.
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

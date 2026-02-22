```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-PREPUSH-003
  title: managed pre-push hook enforces local parity gate
  purpose: Ensures repository-managed pre-push hook exists and is installable 
    via canonical script.
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
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'git_hook_prepush': {'hook_path': '/.githooks/pre-push', 'install_script':
      '/scripts/ci_gate.sh', 'makefile_path': '/Makefile'}, 'check': {'profile': 'governance.scan',
      'config': {'check': 'runtime.git_hook_prepush_enforced'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md',
      'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed',
      'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
services:
  entries:
  - id: 
      svc.root_git_hook_prepush_hook_path_githooks_pre_push_install_script_scripts_ci_gate_sh_makefile_path_makefile_check_profile_governance_scan_config_check_runtime_git_hook_prepush_enforced_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: 
      legacy.root_git_hook_prepush_hook_path_githooks_pre_push_install_script_scripts_ci_gate_sh_makefile_path_makefile_check_profile_governance_scan_config_check_runtime_git_hook_prepush_enforced_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
    config: {}
    default: true
```

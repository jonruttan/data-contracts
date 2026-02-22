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
    - "{'root': '.', 'python_bin_resolver': {'helper': 'scripts/lib/python_bin.sh',
      'files': ['scripts/lib/python_bin.sh'], 'required_tokens': ['resolve_python_bin()
      {', '${root_dir}/.venv/bin/python', '${root_dir}/../../.venv/bin/python', 'python3'],
      'forbidden_tokens': []}, 'check': {'profile': 'governance.scan', 'config': {'check':
      'runtime.compatibility_python_lane_bin_resolver_sync'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md',
      'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed',
      'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
services:
  actions:
  - id: svc.root_python_bin_resolver_helper_scripts_lib_python_bin_sh_files_scripts_lib_python_bin_sh_required_tokens_resolve_python_bin_root_dir_venv_bin_python_root_dir_venv_bin_python_python3_forbidden_tokens_check_profile_governance_scan_config_check_runtime_compatibility_python_lane_bin_resolver_sync_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_python_bin_resolver_helper_scripts_lib_python_bin_sh_files_scripts_lib_python_bin_sh_required_tokens_resolve_python_bin_root_dir_venv_bin_python_root_dir_venv_bin_python_python3_forbidden_tokens_check_profile_governance_scan_config_check_runtime_compatibility_python_lane_bin_resolver_sync_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-CONFIG-002
  title: python-invoking adapter scripts use shared python-bin resolver helper
  purpose: Keeps shared Python resolver helper contract stable for remaining tooling
    paths.
  clauses:
    imports:
    - artifact:
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
    - id: assert_2
      assert:
      - call:
        - var: policy.assert.summary_passed
        - std.object.assoc:
          - summary_json
          - var: summary_json
          - lit: {}
      - call:
        - var: policy.assert.summary_check_id
        - std.object.assoc:
          - summary_json
          - var: summary_json
          - lit: {}
        - runtime.compatibility_python_lane_bin_resolver_sync
      imports:
      - artifact:
        - summary_json
```

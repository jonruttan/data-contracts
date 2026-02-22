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
    - "{'root': '.', 'runtime_scope': {'files': ['specs/contract/08_v1_scope.md',
      'specs/contract/13_runtime_scope.md', 'specs/contract/12_runner_interface.md'],
      'required_tokens': ['Python runner', 'PHP runner', 'required support targets',
      'contract/governance expansion'], 'forbidden_tokens': ['Node.js runner', 'Ruby
      runner', 'Java runner']}, 'check': {'profile': 'governance.scan', 'config':
      {'check': 'runtime.scope_sync'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md',
      'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed',
      'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
services:
  actions:
  - id: svc.root_runtime_scope_files_specs_contract_08_v1_scope_md_specs_contract_13_runtime_scope_md_specs_contract_12_runner_interface_md_required_tokens_python_runner_php_runner_required_support_targets_contract_governance_expansion_forbidden_tokens_node_js_runner_ruby_runner_java_runner_check_profile_governance_scan_config_check_runtime_scope_sync_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_runtime_scope_files_specs_contract_08_v1_scope_md_specs_contract_13_runtime_scope_md_specs_contract_12_runner_interface_md_required_tokens_python_runner_php_runner_required_support_targets_contract_governance_expansion_forbidden_tokens_node_js_runner_ruby_runner_java_runner_check_profile_governance_scan_config_check_runtime_scope_sync_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-SCOPE-001
  title: runtime support scope remains bounded for v1
  purpose: Prevents uncontrolled cross-runtime expansion by enforcing explicit v1
    runtime scope tokens in contract docs.
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
        - runtime.scope_sync
      imports:
      - artifact:
        - summary_json
```

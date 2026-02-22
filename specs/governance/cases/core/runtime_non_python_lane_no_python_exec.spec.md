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
    - "{'root': '.', 'python_dependency': {}, 'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.non_python_lane_no_python_exec'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
services:
  actions:
  - id: svc.root_python_dependency_check_profile_governance_scan_config_check_runtime_non_python_lane_no_python_exec_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_python_dependency_check_profile_governance_scan_config_check_runtime_non_python_lane_no_python_exec_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-PYDEP-003
  title: non-python lanes avoid direct python execution tokens
  purpose: Ensures default gate/orchestration and rust adapter lane files do not contain python execution tokens.
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
        - runtime.non_python_lane_no_python_exec
      imports:
      - from: artifact
        names:
        - summary_json
```

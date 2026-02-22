```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'assert.sugar_compile_only_sync'}},
      'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id',
      'policy.assert.scan_pass']}]}"
services:
- type: legacy.root_check_profile_governance_scan_config_check_assert_sugar_compile_only_sync_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  operations:
  - id: svc.root_check_profile_governance_scan_config_check_assert_sugar_compile_only_sync_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    mode: default
    direction: bidirectional
contracts:
  defaults:
    type: contract.check
  clauses:
  - id: DCGOV-ASSERT-COMPILE-001
    title: compiler keeps sugar operators compile-only
    purpose: Ensures compiler and runtime assertion path keep non-evaluate operators
      as compile-only sugar with spec-lang execution.
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
          - assert.sugar_compile_only_sync
        imports:
        - from: artifact
          names:
          - summary_json
```

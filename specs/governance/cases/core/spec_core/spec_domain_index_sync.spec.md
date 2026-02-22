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
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'spec.domain_index_sync'}},
      'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id',
      'policy.assert.scan_pass']}]}"
services:
- id: svc.root_check_profile_governance_scan_config_check_spec_domain_index_sync_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
  type: legacy.root_check_profile_governance_scan_config_check_spec_domain_index_sync_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  mode: default
  direction: bidirectional
contracts:
- id: DCGOV-SPECLAYOUT-INDEX-001
  title: spec domain indexes are synchronized
  purpose: Ensures each domain index tracks all spec files in its subtree and has
    no stale paths.
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
        call:
        - var: policy.assert.summary_check_id
        - std.object.assoc:
          - summary_json
          - var: summary_json
          - lit: {}
        - spec.domain_index_sync
```

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
    - "{'root': '.', 'stdlib_conformance': {'required_paths': ['/specs/conformance/cases/core/spec_lang_stdlib.spec.md',
      '/specs/conformance/cases/core/spec_lang_schema.spec.md']}, 'check': {'profile':
      'governance.scan', 'config': {'check': 'spec_lang.stdlib_conformance_coverage'}},
      'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id',
      'policy.assert.scan_pass']}]}"
services:
  actions:
  - id: svc.root_stdlib_conformance_required_paths_specs_conformance_cases_core_spec_lang_stdlib_spec_md_specs_conformance_cases_core_spec_lang_schema_spec_md_check_profile_governance_scan_config_check_spec_lang_stdlib_conformance_coverage_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_stdlib_conformance_required_paths_specs_conformance_cases_core_spec_lang_stdlib_spec_md_specs_conformance_cases_core_spec_lang_schema_spec_md_check_profile_governance_scan_config_check_spec_lang_stdlib_conformance_coverage_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
contracts:
- id: DCGOV-STDLIB-004
  title: stdlib conformance coverage files are present
  purpose: Ensures canonical stdlib conformance fixtures are present and discoverable.
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
```

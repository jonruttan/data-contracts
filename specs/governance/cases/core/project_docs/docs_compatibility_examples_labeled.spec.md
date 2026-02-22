```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'compatibility_docs': {'files': ['/README.md', '/docs/development.md', '/specs/contract/12_runner_interface.md'], 'required_tokens': ['implementation-agnostic', 'compatibility lanes', 'non-blocking'], 'forbidden_tokens': ['./scripts/ci_gate.sh']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'docs.compatibility_examples_labeled'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
services:
- type: legacy.root_compatibility_docs_files_readme_md_docs_development_md_specs_contract_12_runner_interface_md_required_tokens_implementation_agnostic_compatibility_lanes_non_blocking_forbidden_tokens_scripts_ci_gate_sh_check_profile_governance_scan_config_check_docs_compatibility_examples_labeled_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  operations:
  - id: svc.root_compatibility_docs_files_readme_md_docs_development_md_specs_contract_12_runner_interface_md_required_tokens_implementation_agnostic_compatibility_lanes_non_blocking_forbidden_tokens_scripts_ci_gate_sh_check_profile_governance_scan_config_check_docs_compatibility_examples_labeled_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    mode: default
    direction: bidirectional
contracts:
  clauses:
  - id: DCGOV-DOCS-REF-008
    title: compatibility examples are explicitly labeled
    purpose: Ensures active documentation keeps Rust as canonical and labels Python/PHP examples as non-blocking compatibility lanes.
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

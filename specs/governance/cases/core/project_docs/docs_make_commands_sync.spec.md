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
    - "{'root': '.', 'make_commands': {'files': ['README.md', 'docs/development.md', '.github/pull_request_template.md'], 'required_tokens': ['make verify-docs', 'make core-check', 'make check', 'make prepush', 'make prepush-fast', 'make ci-cleanroom'], 'forbidden_tokens': ['make prepush-parity']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'docs.make_commands_sync'}}, 'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec', 'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id', 'policy.assert.scan_pass']}]}"
services:
  entries:
  - id: svc.root_make_commands_files_readme_md_docs_development_md_github_pull_request_template_md_required_tokens_make_verify_docs_make_core_check_make_check_make_prepush_make_prepush_fast_make_ci_cleanroom_forbidden_tokens_make_prepush_parity_check_profile_governance_scan_config_check_docs_make_commands_sync_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    type: legacy.root_make_commands_files_readme_md_docs_development_md_github_pull_request_template_md_required_tokens_make_verify_docs_make_core_check_make_check_make_prepush_make_prepush_fast_make_ci_cleanroom_forbidden_tokens_make_prepush_parity_check_profile_governance_scan_config_check_docs_make_commands_sync_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
    io: io
    profile: default
contracts:
- id: DCGOV-DOCS-REF-007
  title: docs use canonical make command entrypoints
  purpose: Keeps contributor docs aligned on the canonical make-based command entrypoints for verification and gate execution.
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
        - docs.make_commands_sync
      imports:
      - from: artifact
        names:
        - summary_json
```

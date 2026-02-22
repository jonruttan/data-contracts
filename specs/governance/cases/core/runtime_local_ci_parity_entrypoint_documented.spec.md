```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'local_ci_parity_docs': {'files': ['/README.md', '/docs/development.md',
      '/docs/book/60_runner_and_gates.md', '/docs/book/80_troubleshooting.md'], 'required_tokens':
      ['make prepush', 'make prepush-fast', 'make hooks-install', 'SPEC_PREPUSH_BYPASS=1']},
      'check': {'profile': 'governance.scan', 'config': {'check': 'runtime.local_ci_parity_entrypoint_documented'}},
      'use': [{'ref': '/specs/libraries/policy/policy_assertions.spec.md', 'as': 'lib_policy_core_spec',
      'symbols': ['policy.assert.no_violations', 'policy.assert.summary_passed', 'policy.assert.summary_check_id',
      'policy.assert.scan_pass']}]}"
services:
- type: legacy.root_local_ci_parity_docs_files_readme_md_docs_development_md_docs_book_60_runner_and_gates_md_docs_book_80_troubleshooting_md_required_tokens_make_prepush_make_prepush_fast_make_hooks_install_spec_prepush_bypass_1_check_profile_governance_scan_config_check_runtime_local_ci_parity_entrypoint_documented_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass
  operations:
  - id: svc.root_local_ci_parity_docs_files_readme_md_docs_development_md_docs_book_60_runner_and_gates_md_docs_book_80_troubleshooting_md_required_tokens_make_prepush_make_prepush_fast_make_hooks_install_spec_prepush_bypass_1_check_profile_governance_scan_config_check_runtime_local_ci_parity_entrypoint_documented_use_ref_specs_libraries_policy_policy_assertions_spec_md_as_lib_policy_core_spec_symbols_policy_assert_no_violations_policy_assert_summary_passed_policy_assert_summary_check_id_policy_assert_scan_pass.default.1
    mode: default
    direction: bidirectional
contracts:
  defaults:
    type: contract.check
  clauses:
  - id: DCGOV-RUNTIME-PREPUSH-005
    title: local ci parity entrypoint is documented for contributors
    purpose: Ensures contributor docs cover parity-default prepush, fast opt-out,
      and hook installation.
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

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
    - "{'root': '.', 'docs_language': {'files': ['/README.md', '/docs/development.md',
      '/docs/book/index.md', '/docs/book/60_runner_and_gates.md'], 'required_tokens':
      ['implementation-agnostic control plane', 'runtime execution ownership lives
      in runner repositories']}, 'check': {'profile': 'governance.scan', 'config':
      {'check': 'runtime.docs_no_required_lane_language'}}}"
services:
  actions:
  - id: svc.root_docs_language_files_readme_md_docs_development_md_docs_book_index_md_docs_book_60_runner_and_gates_md_required_tokens_implementation_agnostic_control_plane_runtime_execution_ownership_lives_in_runner_repositories_check_profile_governance_scan_config_check_runtime_docs_no_required_lane_language.default.1
    type: legacy.root_docs_language_files_readme_md_docs_development_md_docs_book_index_md_docs_book_60_runner_and_gates_md_required_tokens_implementation_agnostic_control_plane_runtime_execution_ownership_lives_in_runner_repositories_check_profile_governance_scan_config_check_runtime_docs_no_required_lane_language
    io: io
    profile: default
contracts:
- id: DCGOV-RUNTIME-DOCS-001
  title: docs use control-plane language
  purpose: Ensures active docs describe this repository as implementation-agnostic
    control-plane.
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

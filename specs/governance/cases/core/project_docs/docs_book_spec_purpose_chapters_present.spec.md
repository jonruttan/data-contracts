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
    - "{'root': '.', 'docs_manifest': {'path': '/docs/book/reference_manifest.yaml', 'required_paths': ['/docs/book/05_what_is_data_contracts.md', '/docs/book/15_spec_lifecycle.md', '/docs/book/25_system_topology.md', '/docs/book/35_usage_guides_index.md']}, 'check': {'profile': 'governance.scan', 'config': {'check': 'docs.book_spec_purpose_chapters_present'}}}"
services:
  entries:
  - id: svc.root_docs_manifest_path_docs_book_reference_manifest_yaml_required_paths_docs_book_05_what_is_data_contracts_md_docs_book_15_spec_lifecycle_md_docs_book_25_system_topology_md_docs_book_35_usage_guides_index_md_check_profile_governance_scan_config_check_docs_book_spec_purpose_chapters_present.default.1
    type: legacy.root_docs_manifest_path_docs_book_reference_manifest_yaml_required_paths_docs_book_05_what_is_data_contracts_md_docs_book_15_spec_lifecycle_md_docs_book_25_system_topology_md_docs_book_35_usage_guides_index_md_check_profile_governance_scan_config_check_docs_book_spec_purpose_chapters_present
    io: io
    profile: default
contracts:
- id: DCGOV-DOCS-REF-019
  title: spec purpose narrative chapters are present
  purpose: Ensures the core spec-purpose chapters are present in the reference manifest.
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
```

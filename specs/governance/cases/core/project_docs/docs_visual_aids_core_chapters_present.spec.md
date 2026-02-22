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
    - "{'root': '.', 'docs_quality_contract': {'path': '/specs/contract/10_docs_quality.md',
      'required_tokens': ['05_what_is_data_contracts.md', '15_spec_lifecycle.md',
      '25_system_topology.md', 'Mermaid diagram block']}, 'check': {'profile': 'governance.scan',
      'config': {'check': 'docs.visual_aids_core_chapters_present'}}}"
services:
  actions:
  - id: svc.root_docs_quality_contract_path_specs_contract_10_docs_quality_md_required_tokens_05_what_is_data_contracts_md_15_spec_lifecycle_md_25_system_topology_md_mermaid_diagram_block_check_profile_governance_scan_config_check_docs_visual_aids_core_chapters_present.default.1
    type: legacy.root_docs_quality_contract_path_specs_contract_10_docs_quality_md_required_tokens_05_what_is_data_contracts_md_15_spec_lifecycle_md_25_system_topology_md_mermaid_diagram_block_check_profile_governance_scan_config_check_docs_visual_aids_core_chapters_present
    io: io
    profile: default
contracts:
- id: DCGOV-DOCS-REF-022
  title: visual aids required in core chapters
  purpose: Ensures docs quality contract enforces Mermaid visual aid requirements
    for core narrative chapters.
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

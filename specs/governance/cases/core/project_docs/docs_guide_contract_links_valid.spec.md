```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'reference_guide': {'path': '/docs/book/90_reference_guide.md',
      'required_tokens': ['Guide To Contract Map', 'guide_01_onboarding.md', 'guide_10_reference_navigation_patterns.md',
      'specs/contract/10_docs_quality.md', 'specs/contract/27_runner_status_exchange.md']},
      'check': {'profile': 'governance.scan', 'config': {'check': 'docs.guide_contract_links_valid'}}}"
services:
- type: legacy.root_reference_guide_path_docs_book_90_reference_guide_md_required_tokens_guide_to_contract_map_guide_01_onboarding_md_guide_10_reference_navigation_patterns_md_specs_contract_10_docs_quality_md_specs_contract_27_runner_status_exchange_md_check_profile_governance_scan_config_check_docs_guide_contract_links_valid
  operations:
  - id: svc.root_reference_guide_path_docs_book_90_reference_guide_md_required_tokens_guide_to_contract_map_guide_01_onboarding_md_guide_10_reference_navigation_patterns_md_specs_contract_10_docs_quality_md_specs_contract_27_runner_status_exchange_md_check_profile_governance_scan_config_check_docs_guide_contract_links_valid.default.1
    mode: default
    direction: bidirectional
contracts:
  defaults:
    type: contract.check
  clauses:
  - id: DCGOV-DOCS-REF-024
    title: guide to contract links are valid
    purpose: Ensures chapter 90 includes guide-to-contract mapping for the canonical
      guide set.
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

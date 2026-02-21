```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-DOCS-REF-024
    title: guide to contract links are valid
    purpose: Ensures chapter 90 includes guide-to-contract mapping for the canonical guide set.
    harness:
      root: .
      reference_guide:
        path: /docs/book/90_reference_guide.md
        required_tokens:
        - Guide To Contract Map
        - guide_01_onboarding.md
        - guide_10_reference_navigation_patterns.md
        - specs/contract/10_docs_quality.md
        - specs/contract/27_runner_status_exchange.md
      check:
        profile: governance.scan
        config:
          check: docs.guide_contract_links_valid
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - violation_count
      predicates:
      - id: assert_1
        assert:
          call:
          - {var: policy.assert.no_violations}
          - std.object.assoc:
            - violation_count
            - {var: violation_count}
            - lit: {}
```

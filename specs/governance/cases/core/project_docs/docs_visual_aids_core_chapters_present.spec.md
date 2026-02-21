```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-DOCS-REF-022
  title: visual aids required in core chapters
  purpose: Ensures docs quality contract enforces Mermaid visual aid requirements for core narrative chapters.
  harness:
    root: "."
    docs_quality_contract:
      path: "/specs/contract/10_docs_quality.md"
      required_tokens:
      - 05_what_is_data_contracts.md
      - 15_spec_lifecycle.md
      - 25_system_topology.md
      - Mermaid diagram block
    check:
      profile: governance.scan
      config:
        check: docs.visual_aids_core_chapters_present
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

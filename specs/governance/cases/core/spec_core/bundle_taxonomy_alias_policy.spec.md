```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-BUNDLE-TAXONOMY-001
    title: bundle taxonomy contract defines canonical metadata names
    purpose: Ensures canonical naming guidance prefers bundle_version and maintainers.
    harness:
      check:
        profile: text.file
        config:
          path: /specs/contract/32_contract_bundle_taxonomy.md
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - text
      predicates:
      - id: assert_1
        assert:
        - std.string.contains:
          - {var: text}
          - bundle_version
        - std.string.contains:
          - {var: text}
          - maintainers
        - std.string.contains:
          - {var: text}
          - contract_set
        - std.string.contains:
          - {var: text}
          - pack
  - id: DCGOV-BUNDLE-TAXONOMY-002
    title: schema v2 docs mark version and author as prose aliases only
    purpose: Ensures schema_v2 narrative preserves canonical key policy for bundle metadata.
    harness:
      check:
        profile: text.file
        config:
          path: /specs/schema/schema_v2.md
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - text
      predicates:
      - id: assert_1
        assert:
        - std.string.contains:
          - {var: text}
          - Canonical metadata names are `bundle_version` and `maintainers`.
        - std.string.contains:
          - {var: text}
          - "`version` and `author` are migration aliases in prose only"
```

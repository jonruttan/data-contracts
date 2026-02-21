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
    title: schema v2 docs keep bundle semantics outside contract-spec suite shape
    purpose: Ensures schema_v2 does not define top-level bundle metadata and points to package-level contracts.
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
          std.logic.and:
          - std.logic.not:
            - std.string.contains:
              - {var: text}
              - - `bundle` (mapping, optional)
          - std.string.contains:
            - {var: text}
            - Bundle/package management is not part of `contract-spec` suite shape in v2.
```

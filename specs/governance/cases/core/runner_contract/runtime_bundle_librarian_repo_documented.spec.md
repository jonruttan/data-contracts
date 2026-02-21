```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-BUNDLE-004
    title: canonical bundle librarian repository is documented
    purpose: Ensures canonical bundle source points to data-contracts-bundles and not local specs/bundles manifests.
    harness:
      check:
        profile: text.file
        config:
          path: /README.md
    clauses:
      defaults: {}
      imports:
        - from: artifact
          names: [text]
      predicates:
        - id: assert_1
          assert:
            std.string.contains:
              - {var: text}
              - data-contracts-bundles
        - id: assert_2
          assert:
            std.logic.not:
              std.string.contains:
                - {var: text}
                - /specs/bundles/index.md
```

```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCCONF-BTOOL-002
    title: runner build tool contract defines required sync tasks
    purpose: Portable build tool contract must define spec-sync and spec-sync-check required tasks.
    harness:
      check:
        profile: text.file
        config: {}
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
              - spec-sync
        - id: assert_2
          assert:
            std.string.contains:
              - {var: text}
              - spec-sync-check
```

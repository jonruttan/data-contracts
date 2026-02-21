```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-BUNDLE-001
    title: runner bundle package management contract is defined
    purpose: Ensures bundle package management contract describes release-asset and checksum requirements.
    harness:
      check:
        profile: text.file
        config:
          path: /specs/contract/33_bundle_package_management.md
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
              - bundle-sync
        - id: assert_2
          assert:
            std.string.contains:
              - {var: text}
              - bundle-sync-check
        - id: assert_3
          assert:
            std.string.contains:
              - {var: text}
              - release-asset
        - id: assert_4
          assert:
            std.string.contains:
              - {var: text}
              - checksum
        - id: assert_5
          assert:
            std.string.contains:
              - {var: text}
              - bundles.lock.yaml
        - id: assert_6
          assert:
            std.string.contains:
              - {var: text}
              - data-contracts-bundles
  - id: DCGOV-RUNTIME-BUNDLE-003
    title: runner build tool schema declares bundle sync tasks
    purpose: Ensures runner build tool schema uses bundle-sync task ids and does not include legacy spec-sync task ids.
    harness:
      check:
        profile: text.file
        config:
          path: /specs/schema/runner_build_tool_contract_v1.yaml
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
              - bundle-sync
        - id: assert_2
          assert:
            std.string.contains:
              - {var: text}
              - bundle-sync-check
        - id: assert_3
          assert:
            std.logic.not:
              std.string.contains:
                - {var: text}
                - spec-sync
```

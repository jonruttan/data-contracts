```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCCONF-BTOOL-002
  title: runner build tool contract defines required bundle sync tasks
  purpose: Portable build tool contract must define bundle-sync and bundle-sync-check required tasks.
  harness:
    check:
      profile: text.file
      config:
        path: "/specs/contract/30_build_tool_command_set.md"
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
    - id: assert_1
      assert:
        std.string.contains:
        - var: text
        - bundle-sync
    - id: assert_2
      assert:
        std.string.contains:
        - var: text
        - bundle-sync-check
    - id: assert_3
      assert:
        std.logic.not:
          std.string.contains:
          - var: text
          - "`spec-sync`"
    - id: assert_4
      assert:
        std.logic.not:
          std.string.contains:
          - var: text
          - "`spec-sync-check`"
```

```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCCONF-BTOOL-001
  title: runner build tool contract defines required core tasks
  purpose: Portable build tool contract must define build, test, and verify required tasks.
  harness:
    check:
      profile: text.file
      config: {}
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
        - build
    - id: assert_2
      assert:
        std.string.contains:
        - var: text
        - test
    - id: assert_3
      assert:
        std.string.contains:
        - var: text
        - verify
```

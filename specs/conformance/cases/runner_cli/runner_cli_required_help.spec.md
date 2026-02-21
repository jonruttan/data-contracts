```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCCONF-RCLI-001
  title: runner cli exposes help command
  purpose: Portable CLI contract requires help surface.
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
        - runner --help
```

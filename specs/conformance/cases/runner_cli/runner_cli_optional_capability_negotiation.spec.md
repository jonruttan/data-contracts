```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCCONF-RCLI-005
    title: runner cli supports optional capability negotiation
    purpose: Portable CLI contract allows optional capability flags such as structured output mode.
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
          required: false
          assert:
            std.string.contains:
              - {var: text}
              - --json
```

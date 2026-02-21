```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCCONF-BTOOL-005
    title: runner build tool contract declares manifest path requirement
    purpose: Build tool command contract must require each runner repository to publish a task map manifest path.
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
              - /specs/impl/<runner>/runner_build_tool_contract_v1.yaml
```

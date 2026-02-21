```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-BTOOL-002
  title: runner build tool contract schema is defined
  purpose: Ensures tool-agnostic build tool schema is present in schema index.
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
        - "/specs/schema/runner_build_tool_contract_v1.yaml"
```

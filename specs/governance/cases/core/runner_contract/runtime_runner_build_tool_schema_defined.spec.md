# Governance Cases

## DCGOV-RUNTIME-BTOOL-002

```yaml contract-spec
id: DCGOV-RUNTIME-BTOOL-002
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: runner build tool contract schema is defined
purpose: Ensures tool-agnostic build tool schema is present in schema index.
type: contract.check
harness:
  check:
    profile: text.file
    config: {}
contract:
  defaults: {}
  imports:
    - from: artifact
      names: [text]
  steps:
    - id: assert_1
      assert:
        std.string.contains:
          - {var: text}
          - /specs/schema/runner_build_tool_contract_v1.yaml
```

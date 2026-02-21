# Governance Cases

## DCGOV-RUNTIME-BTOOL-001

```yaml contract-spec
id: DCGOV-RUNTIME-BTOOL-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: runner build tool contract document is defined
purpose: Ensures tool-agnostic build tool contract document is present in the portable contract index.
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
          - /specs/contract/30_build_tool_command_set.md
```

# runtime_chain_exports_legacy_forbidden

```yaml contract-spec
id: SRGOV-HARNESS-EXPORTS-002
title: legacy harness.chain.exports is forbidden
purpose: Ensures legacy producer export declarations at harness.chain.exports are rejected.
type: governance.check
check: runtime.chain_exports_legacy_forbidden
harness:
  root: .
contract:
- id: assert_1
  class: must
  target: summary_json
  asserts:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - passed
    - true
```

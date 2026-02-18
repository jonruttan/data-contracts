# runtime_harness_exports_location_required

```yaml contract-spec
id: SRGOV-HARNESS-EXPORTS-001
title: producer exports are declared at harness.exports
purpose: Ensures producer symbol declarations are declared at harness.exports and
  legacy harness.chain.exports is rejected.
type: governance.check
check: runtime.harness_exports_location_required
harness:
  root: .
contract:
- id: assert_1
  class: MUST
  target: summary_json
  asserts:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - passed
    - true
```

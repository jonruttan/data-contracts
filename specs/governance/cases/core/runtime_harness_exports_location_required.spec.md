# runtime_harness_exports_location_required

```yaml contract-spec
id: SRGOV-HARNESS-EXPORTS-001
title: producer exports are declared at harness.exports
purpose: Ensures producer symbol declarations are declared at harness.exports and non-canonical
  harness.chain.exports is rejected.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.harness_exports_location_required
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - summary_json
    as:
      summary_json: subject
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```

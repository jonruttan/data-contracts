# runtime_harness_exports_schema_valid

```yaml contract-spec
id: SRGOV-HARNESS-EXPORTS-003
title: harness exports schema is valid
purpose: Ensures harness.exports entries enforce as/from/path/params/required schema requirements.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: runtime.harness_exports_schema_valid
contract:
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: summary_json
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```

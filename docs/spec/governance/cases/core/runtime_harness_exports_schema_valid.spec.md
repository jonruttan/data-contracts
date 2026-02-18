# runtime_harness_exports_schema_valid

```yaml contract-spec
id: SRGOV-HARNESS-EXPORTS-003
title: harness exports schema is valid
purpose: Ensures harness.exports entries enforce as/from/path/params/required
  schema requirements.
type: governance.check
check: runtime.harness_exports_schema_valid
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

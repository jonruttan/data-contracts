# Governance Cases

## SRGOV-RUNTIME-SPECLANG-EXPORT-001

```yaml contract-spec
id: SRGOV-RUNTIME-SPECLANG-EXPORT-001
title: legacy spec_lang.export type is forbidden after hard cut
purpose: Ensures executable spec surfaces reject type spec_lang.export and require
  spec.export producer cases.
type: governance.check
check: runtime.spec_lang_export_type_forbidden
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - MUST:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - runtime.spec_lang_export_type_forbidden
  target: summary_json
```

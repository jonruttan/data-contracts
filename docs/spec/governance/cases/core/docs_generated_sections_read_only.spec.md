# Governance Cases

## SRGOV-DOCS-GEN-003

```yaml contract-spec
id: SRGOV-DOCS-GEN-003
title: generated markdown sections are read-only blocks
purpose: Ensures configured generated markdown outputs contain valid generated section
  markers.
type: governance.check
check: docs.generated_sections_read_only
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
  - MUST:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - docs.generated_sections_read_only
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```

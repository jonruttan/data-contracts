# Governance Cases

## SRGOV-DOCS-GEN-001

```yaml contract-spec
id: SRGOV-DOCS-GEN-001
title: docs generator registry is valid and complete
purpose: Ensures docs generator registry exists, validates, and includes required surfaces.
type: governance.check
check: docs.generator_registry_valid
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
  class: must
  asserts:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - docs.generator_registry_valid
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```

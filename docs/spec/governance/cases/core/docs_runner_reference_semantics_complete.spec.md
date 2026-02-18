# Governance Cases

## SRGOV-DOCS-GEN-024

```yaml contract-spec
id: SRGOV-DOCS-GEN-024
title: runner reference includes semantic sections
purpose: Ensures generated runner API reference includes summary/defaults/failure
  modes/examples per command.
type: governance.check
check: docs.runner_reference_semantics_complete
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
      - docs.runner_reference_semantics_complete
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```

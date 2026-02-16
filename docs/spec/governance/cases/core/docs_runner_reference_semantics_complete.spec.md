# Governance Cases

## SRGOV-DOCS-GEN-024

```yaml spec-test
id: SRGOV-DOCS-GEN-024
title: runner reference includes semantic sections
purpose: Ensures generated runner API reference includes summary/defaults/failure modes/examples
  per command.
type: governance.check
check: docs.runner_reference_semantics_complete
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - docs.runner_reference_semantics_complete
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```

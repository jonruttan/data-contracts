# Governance Cases

## SRGOV-DOCS-GEN-002

```yaml spec-test
id: SRGOV-DOCS-GEN-002
title: docs generator outputs are synchronized
purpose: Ensures all registry-backed docs generator outputs are up-to-date in check mode.
type: governance.check
check: docs.generator_outputs_sync
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
    - eq:
      - get:
        - {var: subject}
        - check_id
      - docs.generator_outputs_sync
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
```

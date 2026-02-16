# Governance Cases

## SRGOV-DOCS-GEN-003

```yaml spec-test
id: SRGOV-DOCS-GEN-003
title: generated markdown sections are read-only blocks
purpose: Ensures configured generated markdown outputs contain valid generated section markers.
type: governance.check
check: docs.generated_sections_read_only
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
      - docs.generated_sections_read_only
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```

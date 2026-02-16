# Governance Cases

## SRGOV-SPEC-MD-001

```yaml spec-test
id: SRGOV-SPEC-MD-001
title: executable spec surfaces are markdown only
purpose: Ensures all canonical executable case trees are authored as .spec.md and do not use
  runnable yaml/json case files.
type: governance.check
check: spec.executable_surface_markdown_only
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
      - spec.executable_surface_markdown_only
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```

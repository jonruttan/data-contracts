# Governance Cases

## SRGOV-DOCS-LAYOUT-002

```yaml spec-test
id: SRGOV-DOCS-LAYOUT-002
title: docs use index.md as canonical directory index filename
purpose: Enforces index.md-only docs directory index policy.
type: governance.check
check: docs.index_filename_policy
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
      - docs.index_filename_policy
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```

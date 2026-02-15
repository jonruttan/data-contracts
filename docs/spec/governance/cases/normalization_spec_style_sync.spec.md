# Governance Cases

## SRGOV-NORM-004

```yaml spec-test
id: SRGOV-NORM-004
title: normalization spec style policy stays profile-driven
purpose: Ensures conformance style limits and wording remain synchronized with the normalization profile and governance scanner constants.
type: governance.check
check: normalization.spec_style_sync
harness:
  root: .
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: text
  must:
  - contain:
    - 'PASS: normalization.spec_style_sync'
```

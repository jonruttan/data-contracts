# Governance Cases

## SRGOV-DOCS-REF-009

```yaml spec-test
id: SRGOV-DOCS-REF-009
title: core and full adoption profile docs stay synchronized
purpose: Keeps contributor-facing docs aligned on core-check and full-check adoption profile wording.
type: governance.check
check: docs.adoption_profiles_sync
harness:
  root: .
  adoption_profiles:
    files:
    - README.md
    - docs/development.md
    required_tokens:
    - Core profile
    - Full profile
    - make core-check
    - make check
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: text
  must:
  - contain:
    - 'PASS: docs.adoption_profiles_sync'
```

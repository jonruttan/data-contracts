# Governance Cases

## SRGOV-DOCS-QUAL-003

```yaml spec-test
id: SRGOV-DOCS-QUAL-003
title: doc token ownership is unique
purpose: Ensures canonical documentation tokens have a single owner page.
type: governance.check
check: docs.token_ownership_unique
harness:
  root: .
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  docs_quality:
    manifest: docs/book/reference_manifest.yaml
  policy_evaluate:
  - {call: [{var: [policy.pass_when_no_violations]}, {ref: subject}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{ref: subject}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{ref: subject}, passed]}
      - true
    - eq:
      - {get: [{ref: subject}, check_id]}
      - docs.token_ownership_unique
```

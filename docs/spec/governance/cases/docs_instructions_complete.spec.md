# Governance Cases

## SRGOV-DOCS-QUAL-005

```yaml spec-test
id: SRGOV-DOCS-QUAL-005
title: instruction pages contain required operational sections
purpose: Ensures docs metadata required sections are present in canonical chapter content.
type: governance.check
check: docs.instructions_complete
harness:
  root: .
  docs_quality:
    manifest: docs/book/reference_manifest.yaml
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: text
  must:
  - contain:
    - 'PASS: docs.instructions_complete'
```

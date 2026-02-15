# Governance Cases

## SRGOV-DOC-REGEX-001

```yaml spec-test
id: SRGOV-DOC-REGEX-001
title: regex profile and operator tokens are synchronized across core docs
purpose: Ensures regex portability linkage and core assertion operator tokens remain aligned in contract/schema/policy docs.
type: governance.check
check: docs.regex_doc_sync
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
    - 'PASS: docs.regex_doc_sync'
```

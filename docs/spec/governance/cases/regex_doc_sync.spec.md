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
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - {call: [{var: [policy.pass_when_no_violations]}, {subject: []}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{subject: []}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{subject: []}, passed]}
      - true
    - eq:
      - {get: [{subject: []}, check_id]}
      - docs.regex_doc_sync
```

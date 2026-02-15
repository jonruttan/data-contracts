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
      - docs.instructions_complete
```

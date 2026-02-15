# Governance Cases

## SRGOV-DOCS-QUAL-002

```yaml spec-test
id: SRGOV-DOCS-QUAL-002
title: reference index is generated from manifest
purpose: Ensures reference index markdown remains synchronized with the manifest source of truth.
type: governance.check
check: docs.reference_manifest_sync
harness:
  root: .
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  docs_quality:
    manifest: docs/book/reference_manifest.yaml
    index_out: docs/book/reference_index.md
  policy_evaluate:
  - {call: [{var: policy.pass_when_no_violations}, {var: subject}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{var: subject}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{var: subject}, passed]}
      - true
    - eq:
      - {get: [{var: subject}, check_id]}
      - docs.reference_manifest_sync
```

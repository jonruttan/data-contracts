# Governance Cases

## SRGOV-DOCS-QUAL-007

```yaml spec-test
id: SRGOV-DOCS-QUAL-007
title: docs example ids are unique
purpose: Ensures example identifiers are unique across canonical docs metadata.
type: governance.check
check: docs.example_id_uniqueness
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
      - docs.example_id_uniqueness
```

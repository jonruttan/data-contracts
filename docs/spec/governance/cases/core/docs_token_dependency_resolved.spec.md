# Governance Cases

## SRGOV-DOCS-QUAL-004

```yaml spec-test
id: SRGOV-DOCS-QUAL-004
title: doc token dependencies resolve to owner docs
purpose: Ensures required tokens in doc metadata are owned and present in owner docs.
type: governance.check
check: docs.token_dependency_resolved
harness:
  root: .
  spec_lang:
    library_paths:
    - /docs/spec/libraries/policy/policy_core.spec.md
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
      - docs.token_dependency_resolved
```

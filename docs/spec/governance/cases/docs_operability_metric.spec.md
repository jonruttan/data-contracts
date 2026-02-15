# Governance Cases

## SRGOV-DOCS-OPER-001

```yaml spec-test
id: SRGOV-DOCS-OPER-001
title: docs operability metric report generation is valid
purpose: Ensures docs operability report generation and shape are valid.
type: governance.check
check: docs.operability_metric
harness:
  root: .
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  docs_operability:
    reference_manifest: docs/book/reference_manifest.yaml
    policy_evaluate:
    - and:
      - {has_key: [{subject: []}, summary]}
      - {has_key: [{subject: []}, segments]}
      - has_key:
        - {get: [{subject: []}, summary]}
        - overall_docs_operability_ratio
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
      - docs.operability_metric
```

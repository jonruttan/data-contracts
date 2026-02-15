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
  docs_operability:
    reference_manifest: docs/book/reference_manifest.yaml
    policy_evaluate:
    - and:
      - has_key:
        - subject: []
        - summary
      - has_key:
        - subject: []
        - segments
      - has_key:
        - get:
          - subject: []
          - summary
        - overall_docs_operability_ratio
assert:
- target: text
  must:
  - contain:
    - 'PASS: docs.operability_metric'
```

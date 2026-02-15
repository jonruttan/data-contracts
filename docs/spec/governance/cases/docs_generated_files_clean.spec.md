# Governance Cases

## SRGOV-DOCS-QUAL-008

```yaml spec-test
id: SRGOV-DOCS-QUAL-008
title: generated docs artifacts are up-to-date
purpose: Ensures generated reference index, coverage, and docs graph artifacts are kept fresh.
type: governance.check
check: docs.generated_files_clean
harness:
  root: .
  docs_quality:
    manifest: docs/book/reference_manifest.yaml
    index_out: docs/book/reference_index.md
    coverage_out: docs/book/reference_coverage.md
    graph_out: docs/book/docs_graph.json
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: text
  must:
  - contain:
    - 'PASS: docs.generated_files_clean'
```

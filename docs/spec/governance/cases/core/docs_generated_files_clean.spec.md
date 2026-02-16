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
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  docs_quality:
    manifest: docs/book/reference_manifest.yaml
    index_out: /docs/book/reference_index.md
    coverage_out: /docs/book/reference_coverage.md
    graph_out: /docs/book/docs_graph.json
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
    - eq:
      - get:
        - {var: subject}
        - check_id
      - docs.generated_files_clean
```

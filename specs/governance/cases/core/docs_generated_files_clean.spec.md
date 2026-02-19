# Governance Cases

## SRGOV-DOCS-QUAL-008

```yaml contract-spec
id: SRGOV-DOCS-QUAL-008
title: generated docs artifacts are up-to-date
purpose: Ensures generated reference index, coverage, and docs graph artifacts are kept fresh.
type: contract.check
harness:
  root: .
  docs_quality:
    manifest: docs/book/reference_manifest.yaml
    index_out: /docs/book/reference_index.md
    coverage_out: /docs/book/reference_coverage.md
    graph_out: /docs/book/docs_graph.json
  check:
    profile: governance.scan
    config:
      check: docs.generated_files_clean
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    'on': violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    'on': summary_json
    assert:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - docs.generated_files_clean
```

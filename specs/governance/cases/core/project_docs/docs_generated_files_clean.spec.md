```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-DOCS-QUAL-008
    title: generated docs artifacts are up-to-date
    purpose: Ensures generated reference index, coverage, and docs graph artifacts are kept fresh.
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
      - ref: /specs/libraries/policy/policy_assertions.spec.md
        as: lib_policy_core_spec
        symbols:
        - policy.assert.no_violations
        - policy.assert.summary_passed
        - policy.assert.summary_check_id
        - policy.assert.scan_pass
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - violation_count
      predicates:
      - id: assert_1
        assert:
          call:
          - {var: policy.assert.no_violations}
          - std.object.assoc:
            - violation_count
            - {var: violation_count}
            - lit: {}
      - id: assert_2
        assert:
        - call:
          - {var: policy.assert.summary_passed}
          - std.object.assoc:
            - summary_json
            - {var: summary_json}
            - lit: {}
        - call:
          - {var: policy.assert.summary_check_id}
          - std.object.assoc:
            - summary_json
            - {var: summary_json}
            - lit: {}
          - docs.generated_files_clean
        imports:
        - from: artifact
          names:
          - summary_json
```

```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-DOCS-CANON-001
    title: specs index links all canonical spec entrypoints
    purpose: Ensures /specs/index.md links every canonical spec subtree and current snapshot.
    harness:
      root: .
      check:
        profile: governance.scan
        config:
          check: docs.spec_index_reachability
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
```

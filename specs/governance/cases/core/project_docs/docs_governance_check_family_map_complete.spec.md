```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-DOCS-CANON-002
    title: governance check family map covers all registered checks
    purpose: Ensures each governance check id is mapped to a canonical check family prefix.
    harness:
      root: .
      check:
        profile: governance.scan
        config:
          check: docs.governance_check_family_map_complete
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

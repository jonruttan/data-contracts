```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-CONTRACT-BLOCK-001
    title: cases must use contract block
    purpose: Enforces top-level contract block requirement for executable cases.
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
    harness:
      check:
        profile: governance.scan
        config:
          check: runtime.case_contract_block_required
```

```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-SPEC-TOPO-001
    title: specs taxonomy hard-cut layout is canonical
    purpose: Ensures governance utility domains are folded under `/specs/governance/*` and prior root shim paths are removed.
    harness:
      root: .
      taxonomy_layout:
        required_paths:
        - /specs/governance/metrics
        - /specs/governance/tools
        - /specs/governance
        - /specs/current.md
        - /specs/schema/index.md
        - /specs/contract/index.md
        forbidden_paths:
        - /specs/metrics
        - /specs/tools
        - /specs/pending
        - /specs/schema.md
        - /specs/portable_contract.md
      check:
        profile: governance.scan
        config:
          check: spec.taxonomy_hard_cut_required
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
```

```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-CONTRACT-SPEC-001
    title: executable case fences must use contract-spec
    purpose: Enforces hard-cut fence rename to contract-spec across specs cases.
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
          check: runtime.contract_spec_fence_required
```

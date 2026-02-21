```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-CONTRACT-STEP-001
    title: contract steps must declare asserts
    purpose: Enforces step-form contract nodes to use asserts list and non-empty children.
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
          check: runtime.contract_step_asserts_required
```

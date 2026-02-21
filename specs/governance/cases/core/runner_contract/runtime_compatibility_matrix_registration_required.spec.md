```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-CONFIG-008
    title: compatibility matrix registration is explicit
    purpose: Ensures runtime lanes are registered in the compatibility matrix contract before
      use.
    harness:
      root: .
      compatibility_matrix:
        path: /specs/contract/25_compatibility_matrix.md
        required_tokens:
        - '- `required`:'
        - '- `compatibility_non_blocking`:'
        - '- `rust`'
        - '- `python`'
        - '- `php`'
        - '- `node`'
        - '- `c`'
      check:
        profile: governance.scan
        config:
          check: runtime.compatibility_matrix_registration_required
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

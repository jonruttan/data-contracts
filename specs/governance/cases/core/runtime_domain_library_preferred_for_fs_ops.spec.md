```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-DOMAIN-LIB-OPS-FS-001
    title: executable specs prefer domain library helpers over raw ops fs symbols
    purpose: Enforces domain.path/domain.fs usage in executable specs and allows raw ops.fs usage
      only in stdlib primitive conformance coverage.
    harness:
      root: .
      check:
        profile: governance.scan
        config:
          check: runtime.domain_library_preferred_for_fs_ops
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
        - summary_json
      predicates:
      - id: assert_1
        assert:
          call:
          - {var: policy.assert.summary_passed}
          - std.object.assoc:
            - summary_json
            - {var: summary_json}
            - lit: {}
```

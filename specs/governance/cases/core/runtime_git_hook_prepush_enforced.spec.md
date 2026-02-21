```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-PREPUSH-003
    title: managed pre-push hook enforces local parity gate
    purpose: Ensures repository-managed pre-push hook exists and is installable via canonical
      script.
    harness:
      root: .
      git_hook_prepush:
        hook_path: /.githooks/pre-push
        install_script: /scripts/ci_gate.sh
        makefile_path: /Makefile
      check:
        profile: governance.scan
        config:
          check: runtime.git_hook_prepush_enforced
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

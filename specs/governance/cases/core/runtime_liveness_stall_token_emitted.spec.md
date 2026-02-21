```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-LIVENESS-STALL-001
    title: run trace contains liveness stall reason tokens
    purpose: Ensures watchdog reason tokens for runner/subprocess stall semantics are observable
      in run trace artifacts.
    harness:
      root: .
      liveness_trace_tokens:
        trace_path: specs/governance/cases/fixtures/run_trace_liveness_sample.json
        required_tokens:
        - stall.runner.no_progress
        - stall.subprocess.no_output_no_event
      check:
        profile: governance.scan
        config:
          check: runtime.liveness_stall_token_emitted
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

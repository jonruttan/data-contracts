```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
contracts:
  clauses:
  - id: DCGOV-RUNTIME-CORE-003
    title: non-core scripts absent from active policy and traceability
    purpose: Ensures policy and traceability surfaces do not reference retired script entrypoints.
    harness:
      root: "."
      policy_traceability_paths:
      - "/specs/contract/policy_v1.yaml"
      - "/specs/contract/traceability_v1.yaml"
      forbidden_tokens:
      - scripts/core_gate.sh
      - scripts/local_ci_parity.sh
      - scripts/docs_doctor.sh
      - scripts/install_git_hooks.sh
      - scripts/prepush_gate.sh
      check:
        profile: governance.scan
        config:
          check: runtime.non_core_scripts_not_in_active_policy_traceability
    asserts:
      imports:
      - from: artifact
        names:
        - violation_count
      checks:
      - id: assert_1
        assert:
          call:
          - var: policy.assert.no_violations
          - std.object.assoc:
            - violation_count
            - var: violation_count
            - lit: {}
```

```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-CI-001
    title: control-plane ci forbids runtime runner execution
    purpose: Ensures this repository CI does not execute runtime lanes directly.
    harness:
      root: .
      ci_runtime_exec:
        files:
        - /.github/workflows/ci.yml
        - /scripts/ci_gate.sh
        - /scripts/ci_gate.sh
        - /scripts/ci_gate.sh
        forbidden_tokens:
        - scripts/runner_bin.sh
      check:
        profile: governance.scan
        config:
          check: runtime.control_plane_ci_runner_execution_forbidden
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

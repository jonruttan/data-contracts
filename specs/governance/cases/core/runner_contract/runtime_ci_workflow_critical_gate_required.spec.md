```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-TRIAGE-014
  title: ci workflow defines rust critical gate as first-class lane
  purpose: Ensures CI has a dedicated rust critical gate job and diagnostic ci-gate depends on it.
  harness:
    root: "."
    ci_workflow_critical_gate:
      path: "/.github/workflows/ci.yml"
      required_tokens:
      - 'control-plane-critical-gate:'
      - Run control-plane critical gate
      - "./scripts/control_plane.sh critical-gate"
      - 'needs: control-plane-critical-gate'
      - 'continue-on-error: true'
    check:
      profile: governance.scan
      config:
        check: runtime.ci_workflow_critical_gate_required
    use:
    - ref: "/specs/libraries/policy/policy_assertions.spec.md"
      as: lib_policy_core_spec
      symbols:
      - policy.assert.no_violations
      - policy.assert.summary_passed
      - policy.assert.summary_check_id
      - policy.assert.scan_pass
  clauses:
    imports:
    - from: artifact
      names:
      - violation_count
    predicates:
    - id: assert_1
      assert:
        call:
        - var: policy.assert.no_violations
        - std.object.assoc:
          - violation_count
          - var: violation_count
          - lit: {}
```

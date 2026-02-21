```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-TRIAGE-002
  title: prepush lane uses governance triage entrypoint
  purpose: Ensures prepush parity lane calls governance triage instead of direct broad governance.
  harness:
    root: "."
    prepush_governance_triage:
      path: "/scripts/ci_gate.sh"
      required_tokens:
      - governance-triage
      - "./scripts/governance_triage.sh"
      forbidden_tokens:
      - run_step governance "${SPEC_RUNNER_BIN}" governance
    check:
      profile: governance.scan
      config:
        check: runtime.prepush_uses_governance_triage_required
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

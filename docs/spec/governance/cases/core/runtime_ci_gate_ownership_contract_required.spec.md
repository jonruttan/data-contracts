# Governance Cases

## SRGOV-RUNTIME-TRIAGE-019

```yaml contract-spec
id: SRGOV-RUNTIME-TRIAGE-019
title: ci gate ownership contract is single-source and broad-only in summary
purpose: Ensures ci_gate.sh owns critical execution ordering and ci-gate-summary owns
  broad governance only.
type: governance.check
check: runtime.ci_gate_ownership_contract_required
harness:
  root: .
  ci_gate_ownership_contract:
    gate_path: /scripts/ci_gate.sh
    gate_required_tokens:
    - critical-gate
    - ci-gate-summary
    gate_ordered_tokens:
    - critical-gate
    - ci-gate-summary
    summary_files:
    - /scripts/ci_gate_summary.py
    - /scripts/rust/spec_runner_cli/src/main.rs
    summary_required_tokens:
    - governance_broad
    - triage_phase
    - broad_required
    summary_forbidden_tokens:
    - governance_critical
    - SPEC_CI_GATE_INCLUDE_CRITICAL
    - SPEC_CI_GATE_SKIP_CRITICAL
    - --include-critical
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```

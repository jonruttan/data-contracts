# Governance Cases

## SRGOV-RUNTIME-TRIAGE-014

```yaml contract-spec
id: SRGOV-RUNTIME-TRIAGE-014
title: ci workflow defines rust critical gate as first-class lane
purpose: Ensures CI has a dedicated rust critical gate job and diagnostic ci-gate
  depends on it.
type: governance.check
check: runtime.ci_workflow_critical_gate_required
harness:
  root: .
  ci_workflow_critical_gate:
    path: /.github/workflows/ci.yml
    required_tokens:
    - 'rust-critical-gate:'
    - Run rust critical gate
    - ./scripts/runner_adapter.sh --impl rust critical-gate
    - 'needs: rust-critical-gate'
    - 'continue-on-error: true'
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
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

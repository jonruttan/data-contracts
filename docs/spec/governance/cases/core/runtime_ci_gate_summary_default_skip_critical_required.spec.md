# Governance Cases

## SRGOV-RUNTIME-TRIAGE-018

```yaml spec-test
id: SRGOV-RUNTIME-TRIAGE-018
title: ci gate summary skips critical by default unless explicitly included
purpose: Ensures ci-gate-summary defaults to broad-only flow and only includes governance_critical
  when explicitly opted in.
type: governance.check
check: runtime.ci_gate_summary_default_skip_critical_required
harness:
  root: .
  ci_gate_summary_default_skip_critical:
    files:
    - /scripts/ci_gate_summary.py
    - /scripts/rust/spec_runner_cli/src/main.rs
    required_tokens:
    - SPEC_CI_GATE_INCLUDE_CRITICAL
    - SPEC_CI_GATE_SKIP_CRITICAL
    - --include-critical
    forbidden_tokens:
    - SPEC_CI_GATE_SKIP_CRITICAL\", false
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```

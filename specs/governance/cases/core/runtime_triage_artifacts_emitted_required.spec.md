# Governance Cases

## SRGOV-RUNTIME-TRIAGE-004

```yaml contract-spec
id: SRGOV-RUNTIME-TRIAGE-004
title: triage artifacts are emitted by triage and gate flows
purpose: Ensures triage artifacts are produced and referenced by governance-triage and ci-gate-summary.
type: contract.check
harness:
  root: .
  triage_artifacts:
    files:
    - /scripts/governance_triage.sh
    - /runners/python/spec_runner/script_runtime_commands.py
    required_tokens:
    - failing_check_ids
    - failing_check_prefixes
  check:
    profile: governance.scan
    config:
      check: runtime.triage_artifacts_emitted_required
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
    imports:
      subject:
        from: artifact
        key: violation_count
```

# Governance Cases

## SRGOV-RUNTIME-TRIAGE-012

```yaml contract-spec
id: SRGOV-RUNTIME-TRIAGE-012
title: triage artifact includes selection metadata
type: contract.check
purpose: Ensures governance triage artifacts include selection_source and selected_prefixes
  metadata.
harness:
  root: .
  triage_artifact_selection_metadata:
    path: /scripts/governance_triage.sh
    required_tokens:
    - selection_source
    - selected_prefixes
    - broad_required
    - governance-triage-summary.md
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: runtime.governance_triage_artifact_contains_selection_metadata
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            std.logic.eq:
            - {var: subject}
            - 0
  target: violation_count
```

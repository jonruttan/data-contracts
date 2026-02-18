# Governance Cases

## SRGOV-RUNTIME-TRIAGE-005

```yaml spec-test
id: SRGOV-RUNTIME-TRIAGE-005
title: triage parser derives failing check ids and prefixes
purpose: Ensures triage script parses governance ERROR lines and maps check ids to check-prefix
  retries.
type: governance.check
check: runtime.triage_failure_id_parsing_required
harness:
  root: .
  triage_failure_parser:
    path: /scripts/governance_triage.sh
    required_tokens:
    - '^ERROR: ([A-Z0-9-]+):'
    - parse_error_ids_from_output
    - build_prefixes_from_ids
    - docs/spec/governance/check_prefix_map_v1.yaml
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

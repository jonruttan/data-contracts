# Governance Cases

## SRGOV-RUNTIME-TRIAGE-005

```yaml contract-spec
id: SRGOV-RUNTIME-TRIAGE-005
title: triage parser derives failing check ids and prefixes
purpose: Ensures triage script parses governance ERROR lines and maps check ids to check-prefix
  retries.
type: contract.check
harness:
  root: .
  triage_failure_parser:
    path: /scripts/governance_triage.sh
    required_tokens:
    - '^ERROR: ([A-Z0-9-]+):'
    - parse_error_ids_from_output
    - build_prefixes_from_ids
    - docs/spec/governance/check_prefix_map_v1.yaml
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
      check: runtime.triage_failure_id_parsing_required
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.logic.eq:
          - {var: subject}
          - 0
  target: violation_count
```

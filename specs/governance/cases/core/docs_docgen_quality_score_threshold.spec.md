# Governance Cases

## SRGOV-DOCS-GEN-026

```yaml contract-spec
id: SRGOV-DOCS-GEN-026
title: docgen quality score meets minimum threshold
purpose: Ensures generated runner/harness/stdlib catalogs meet minimum semantic quality score.
type: contract.check
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /specs/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: docs.docgen_quality_score_threshold
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - check_id
    - docs.docgen_quality_score_threshold
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - passed
    - true
  target: summary_json
```

# Governance Cases

## SRGOV-DOCS-GEN-026

```yaml contract-spec
id: SRGOV-DOCS-GEN-026
title: docgen quality score meets minimum threshold
purpose: Ensures generated runner/harness/stdlib catalogs meet minimum semantic quality score.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.docgen_quality_score_threshold
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: summary_json
  steps:
  - id: assert_1
    assert:
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
```

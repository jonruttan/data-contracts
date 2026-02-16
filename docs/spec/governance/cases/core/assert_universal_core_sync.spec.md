# Governance Cases

## SRGOV-ASSERT-CORE-001

```yaml spec-test
id: SRGOV-ASSERT-CORE-001
title: assertion docs define universal evaluate core
purpose: Ensures schema and contract docs consistently define evaluate as the universal assertion
  core and classify other operators as authoring sugar.
type: governance.check
check: assert.universal_core_sync
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - assert.universal_core_sync
```

# Governance Cases

## SRGOV-CONF-PORT-002

```yaml spec-test
id: SRGOV-CONF-PORT-002
title: conformance cases avoid non-deterministic ambient tokens
purpose: Ensures portable conformance fixtures avoid direct time/random expressions that break
  cross-run determinism.
type: governance.check
check: conformance.portable_determinism_guard
harness:
  root: .
  determinism:
    exclude_case_keys:
    - id
    - title
    - purpose
    - expect
    - requires
    - assert_health
    patterns:
    - \bdatetime\.now\s*\(
    - \bdatetime\.utcnow\s*\(
    - \btime\.time\s*\(
    - \bdate\.today\s*\(
    - \bDate\.now\s*\(
    - \bnew\s+Date\s*\(
    - \brandom\.
    - \brand(?:int|range)?\s*\(
    - \bMath\.random\s*\(
    policy_evaluate:
    - std.collection.is_empty:
      - std.object.get:
        - {var: subject}
        - violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
      - as: policy.pass_when_no_violations
        from: library.symbol
        required: true
        path: /policy.pass_when_no_violations
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
- id: assert_2
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - conformance.portable_determinism_guard
  target: summary_json
```

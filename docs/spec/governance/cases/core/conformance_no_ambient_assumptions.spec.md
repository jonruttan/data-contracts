# Governance Cases

## SRGOV-CONF-PORT-003

```yaml spec-test
id: SRGOV-CONF-PORT-003
title: conformance cases avoid ambient env/time/random assumptions
purpose: Ensures portable conformance fixtures do not embed ambient environment, clock, or
  random-source assumptions.
type: governance.check
check: conformance.no_ambient_assumptions
harness:
  root: .
  ambient_assumptions:
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
    - \bos\.environ\b
    - \bos\.getenv\s*\(
    - \bgetenv\s*\(
    - \bprocess\.env\b
    - \$_ENV\b
    - \bSystem\.getenv\s*\(
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
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from_step: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
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
      - conformance.no_ambient_assumptions
```

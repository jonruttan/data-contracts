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
  spec_lang:
    library_paths:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
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
    - is_empty:
      - get:
        - {var: subject}
        - violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
    - eq:
      - get:
        - {var: subject}
        - check_id
      - conformance.no_ambient_assumptions
```

# Governance Cases

## SRGOV-CONF-PORT-002

```yaml spec-test
id: SRGOV-CONF-PORT-002
title: conformance cases avoid non-deterministic ambient tokens
purpose: Ensures portable conformance fixtures avoid direct time/random expressions that break cross-run determinism.
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
    - eq:
      - count:
        - filter:
          - fn:
            - {row: []}
            - gt:
              - count:
                - filter:
                  - fn:
                    - {s: []}
                    - any:
                      - map:
                        - fn:
                          - {p: []}
                          - {matches: [{var: [s]}, {var: [p]}]}
                        - {var: [patterns]}
                  - {get: [{var: [row]}, strings]}
              - 0
          - {subject: []}
      - 0
  policy_evaluate:
  - is_empty:
    - {get: [{subject: []}, violations]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{subject: []}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{subject: []}, passed]}
      - true
    - eq:
      - {get: [{subject: []}, check_id]}
      - conformance.portable_determinism_guard
```

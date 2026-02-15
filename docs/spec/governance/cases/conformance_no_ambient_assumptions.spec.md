# Governance Cases

## SRGOV-CONF-PORT-003

```yaml spec-test
id: SRGOV-CONF-PORT-003
title: conformance cases avoid ambient env/time/random assumptions
purpose: Ensures portable conformance fixtures do not embed ambient environment, clock, or random-source assumptions.
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
    - eq:
      - count:
        - filter:
          - fn:
            - row: []
            - gt:
              - count:
                - filter:
                  - fn:
                    - s: []
                    - any:
                      - map:
                        - fn:
                          - p: []
                          - matches:
                            - var:
                              - s
                            - var:
                              - p
                        - var:
                          - patterns
                  - get:
                    - var:
                      - row
                    - strings
              - 0
          - subject: []
      - 0
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: text
  must:
  - contain:
    - 'PASS: conformance.no_ambient_assumptions'
```

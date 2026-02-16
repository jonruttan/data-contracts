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
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
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
    - std.logic.eq:
      - std.collection.count:
        - std.collection.filter:
          - fn:
            - [row]
            - std.logic.gt:
              - std.collection.count:
                - std.collection.filter:
                  - fn:
                    - [s]
                    - std.collection.any:
                      - std.collection.map:
                        - fn:
                          - [p]
                          - std.string.matches:
                            - {var: s}
                            - {var: p}
                        - {var: patterns}
                  - std.object.get:
                    - {var: row}
                    - strings
              - 0
          - {var: subject}
      - 0
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
      - conformance.portable_determinism_guard
```

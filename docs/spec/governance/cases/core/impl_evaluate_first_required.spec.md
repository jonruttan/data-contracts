# Governance Cases

## SRGOV-IMPL-SPECLANG-001

```yaml spec-test
id: SRGOV-IMPL-SPECLANG-001
title: impl fixtures require evaluate-first assertions
purpose: Enforces evaluate-first assertion authoring in impl fixture surfaces.
type: governance.check
check: impl.evaluate_first_required
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  impl_evaluate_first:
    roots:
    - /docs/spec/impl
    allow_sugar_case_ids:
    - SRPHP-AH-001
    - SRPHP-AH-002
    - SRPHP-AH-003
    - SRPHP-AH-004
    - SRPHP-AH-005
    - SRPHP-RUN-007
    - SRPHP-RUN-F004
    - SRPHP-RUN-F008
    policy_evaluate:
    - std.logic.eq:
      - std.collection.count:
        - std.collection.filter:
          - fn:
            - [row]
            - std.logic.and:
              - std.logic.gt:
                - std.collection.count:
                  - std.object.get:
                    - {var: row}
                    - non_evaluate_ops
                - 0
              - std.logic.not:
                - std.object.get:
                  - {var: row}
                  - allowlisted
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
      - impl.evaluate_first_required
```

# Spec-Lang Conformance Domain Library

## LIB-DOMAIN-CONFORMANCE-001

```yaml spec-test
id: LIB-DOMAIN-CONFORMANCE-001-001-DOMAIN-CONFORMANCE-VALIDATE-REPORT-ERRORS
type: spec.export
assert:
- id: __export__domain.conformance.validate_report_errors
  class: must
  checks:
  - std.collection.concat:
    - if:
      - std.logic.eq:
        - std.object.get:
          - var: report
          - version
        - 1
      - lit: []
      - lit:
        - report.version must equal 1
    - if:
      - std.type.is_list:
        - std.object.get:
          - var: report
          - results
      - lit: []
      - lit:
        - report.results must be a list
harness:
  chain:
    exports:
    - as: domain.conformance.validate_report_errors
      from: assert.function
      path: /__export__domain.conformance.validate_report_errors
      params:
      - report
      required: true
```

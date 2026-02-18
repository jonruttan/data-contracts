# Spec-Lang Conformance Domain Library

## LIB-DOMAIN-CONFORMANCE-001

```yaml contract-spec
id: LIB-DOMAIN-CONFORMANCE-001-000-DOMAIN-CONFORMANCE-ERROR-WHEN-FALSE
type: contract.export
contract:
- id: __export__domain.conformance.error_when_false
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            if:
            - {var: condition}
            - lit: []
            - lit:
              - {var: message}
harness:
  exports:
  - as: domain.conformance.error_when_false
    from: assert.function
    path: /__export__domain.conformance.error_when_false
    params:
    - condition
    - message
    required: true
```

```yaml contract-spec
id: LIB-DOMAIN-CONFORMANCE-001-000A-DOMAIN-CONFORMANCE-REPORT-VERSION-IS-V1
type: contract.export
contract:
- id: __export__domain.conformance.report_version_is_v1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            std.logic.eq:
            - std.object.get:
              - {var: report}
              - version
            - 1
harness:
  exports:
  - as: domain.conformance.report_version_is_v1
    from: assert.function
    path: /__export__domain.conformance.report_version_is_v1
    params:
    - report
    required: true
```

```yaml contract-spec
id: LIB-DOMAIN-CONFORMANCE-001-000B-DOMAIN-CONFORMANCE-REPORT-RESULTS-IS-LIST
type: contract.export
contract:
- id: __export__domain.conformance.report_results_is_list
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            std.type.is_list:
            - std.object.get:
              - {var: report}
              - results
harness:
  exports:
  - as: domain.conformance.report_results_is_list
    from: assert.function
    path: /__export__domain.conformance.report_results_is_list
    params:
    - report
    required: true
```

```yaml contract-spec
id: LIB-DOMAIN-CONFORMANCE-001-000C-DOMAIN-CONFORMANCE-VALIDATE-REPORT-ERRORS
type: contract.export
contract:
- id: __export__domain.conformance.validate_report_errors
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            std.collection.concat:
            - if:
              - std.logic.eq:
                - std.object.get:
                  - {var: report}
                  - version
                - 1
              - lit: []
              - lit:
                - report.version must equal 1
            - if:
              - std.type.is_list:
                - std.object.get:
                  - {var: report}
                  - results
              - lit: []
              - lit:
                - report.results must be a list
harness:
  exports:
  - as: domain.conformance.validate_report_errors
    from: assert.function
    path: /__export__domain.conformance.validate_report_errors
    params:
    - report
    required: true
```

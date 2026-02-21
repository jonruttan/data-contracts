```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.export
contracts:
- id: LIB-DOMAIN-CONFORMANCE-001-000-DOMAIN-CONFORMANCE-ERROR-WHEN-FALSE
  clauses:
    predicates:
    - id: __export__domain.conformance.error_when_false
      assert:
        lit:
          if:
          - var: condition
          - lit: []
          - lit:
            - var: message
  harness:
    exports:
    - as: domain.conformance.error_when_false
      from: assert.function
      path: "/__export__domain.conformance.error_when_false"
      params:
      - condition
      - message
      required: true
      doc:
        summary: Contract export for `domain.conformance.error_when_false`.
        description: Auto-generated metadata stub. Replace with authored reference text.
        params:
        - name: condition
          type: any
          required: true
          description: Input parameter `condition`.
        - name: message
          type: any
          required: true
          description: Input parameter `message`.
        returns:
          type: any
          description: Result payload for this symbol.
        errors:
        - code: SCHEMA_ERROR
          when: Input payload does not satisfy contract shape requirements.
          category: schema
        examples:
        - title: Basic usage
          input:
            condition: "<condition>"
            message: "<message>"
          expected: "<result>"
          notes: Replace with a concrete scenario.
        portability:
          python: true
          php: true
          rust: true
          notes: Confirm per-runtime behavior and caveats.
        see_also: []
        since: v1
  library:
    id: domain.conformance.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  doc:
    summary: Case `LIB-DOMAIN-CONFORMANCE-001-000-DOMAIN-CONFORMANCE-ERROR-WHEN-FALSE` for `contract.export`.
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    audience: spec-authors
    since: v1
    tags:
    - contract.export
    see_also: []
- id: LIB-DOMAIN-CONFORMANCE-001-000A-DOMAIN-CONFORMANCE-REPORT-VERSION-IS-V1
  clauses:
    predicates:
    - id: __export__domain.conformance.report_version_is_v1
      assert:
        std.logic.eq:
        - std.object.get:
          - var: report
          - version
        - 1
  harness:
    exports:
    - as: domain.conformance.report_version_is_v1
      from: assert.function
      path: "/__export__domain.conformance.report_version_is_v1"
      params:
      - report
      required: true
      doc:
        summary: Contract export for `domain.conformance.report_version_is_v1`.
        description: Auto-generated metadata stub. Replace with authored reference text.
        params:
        - name: report
          type: any
          required: true
          description: Input parameter `report`.
        returns:
          type: any
          description: Result payload for this symbol.
        errors:
        - code: SCHEMA_ERROR
          when: Input payload does not satisfy contract shape requirements.
          category: schema
        examples:
        - title: Basic usage
          input:
            report: "<report>"
          expected: "<result>"
          notes: Replace with a concrete scenario.
        portability:
          python: true
          php: true
          rust: true
          notes: Confirm per-runtime behavior and caveats.
        see_also: []
        since: v1
  library:
    id: domain.conformance.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  doc:
    summary: Case `LIB-DOMAIN-CONFORMANCE-001-000A-DOMAIN-CONFORMANCE-REPORT-VERSION-IS-V1` for `contract.export`.
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    audience: spec-authors
    since: v1
    tags:
    - contract.export
    see_also: []
- id: LIB-DOMAIN-CONFORMANCE-001-000B-DOMAIN-CONFORMANCE-REPORT-RESULTS-IS-LIST
  clauses:
    predicates:
    - id: __export__domain.conformance.report_results_is_list
      assert:
        std.type.is_list:
        - std.object.get:
          - var: report
          - results
  harness:
    exports:
    - as: domain.conformance.report_results_is_list
      from: assert.function
      path: "/__export__domain.conformance.report_results_is_list"
      params:
      - report
      required: true
      doc:
        summary: Contract export for `domain.conformance.report_results_is_list`.
        description: Auto-generated metadata stub. Replace with authored reference text.
        params:
        - name: report
          type: any
          required: true
          description: Input parameter `report`.
        returns:
          type: any
          description: Result payload for this symbol.
        errors:
        - code: SCHEMA_ERROR
          when: Input payload does not satisfy contract shape requirements.
          category: schema
        examples:
        - title: Basic usage
          input:
            report: "<report>"
          expected: "<result>"
          notes: Replace with a concrete scenario.
        portability:
          python: true
          php: true
          rust: true
          notes: Confirm per-runtime behavior and caveats.
        see_also: []
        since: v1
  library:
    id: domain.conformance.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  doc:
    summary: Case `LIB-DOMAIN-CONFORMANCE-001-000B-DOMAIN-CONFORMANCE-REPORT-RESULTS-IS-LIST` for `contract.export`.
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    audience: spec-authors
    since: v1
    tags:
    - contract.export
    see_also: []
- id: LIB-DOMAIN-CONFORMANCE-001-000C-DOMAIN-CONFORMANCE-VALIDATE-REPORT-ERRORS
  clauses:
    predicates:
    - id: __export__domain.conformance.validate_report_errors
      assert:
        std.collection.concat:
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
    exports:
    - as: domain.conformance.validate_report_errors
      from: assert.function
      path: "/__export__domain.conformance.validate_report_errors"
      params:
      - report
      required: true
      doc:
        summary: Contract export for `domain.conformance.validate_report_errors`.
        description: Auto-generated metadata stub. Replace with authored reference text.
        params:
        - name: report
          type: any
          required: true
          description: Input parameter `report`.
        returns:
          type: any
          description: Result payload for this symbol.
        errors:
        - code: SCHEMA_ERROR
          when: Input payload does not satisfy contract shape requirements.
          category: schema
        examples:
        - title: Basic usage
          input:
            report: "<report>"
          expected: "<result>"
          notes: Replace with a concrete scenario.
        portability:
          python: true
          php: true
          rust: true
          notes: Confirm per-runtime behavior and caveats.
        see_also: []
        since: v1
  library:
    id: domain.conformance.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  doc:
    summary: Case `LIB-DOMAIN-CONFORMANCE-001-000C-DOMAIN-CONFORMANCE-VALIDATE-REPORT-ERRORS` for `contract.export`.
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    audience: spec-authors
    since: v1
    tags:
    - contract.export
    see_also: []
```




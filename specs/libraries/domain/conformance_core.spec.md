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
      docs:
      - id: domain.conformance.error_when_false.doc.1
        summary: Contract export for `domain.conformance.error_when_false`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  condition: \"<condition>\"\n  message: \"<message>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: condition\n  type: any\n  required: true\n  description: Input parameter `condition`.\n- name: message\n  type: any\n  required: true\n  description: Input parameter `message`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.conformance.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-CONFORMANCE-001-000-DOMAIN-CONFORMANCE-ERROR-WHEN-FALSE.doc.1
    summary: Case `LIB-DOMAIN-CONFORMANCE-001-000-DOMAIN-CONFORMANCE-ERROR-WHEN-FALSE` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
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
      docs:
      - id: domain.conformance.report_version_is_v1.doc.1
        summary: Contract export for `domain.conformance.report_version_is_v1`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  report: \"<report>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: report\n  type: any\n  required: true\n  description: Input parameter `report`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.conformance.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-CONFORMANCE-001-000A-DOMAIN-CONFORMANCE-REPORT-VERSION-IS-V1.doc.1
    summary: Case `LIB-DOMAIN-CONFORMANCE-001-000A-DOMAIN-CONFORMANCE-REPORT-VERSION-IS-V1` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
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
      docs:
      - id: domain.conformance.report_results_is_list.doc.1
        summary: Contract export for `domain.conformance.report_results_is_list`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  report: \"<report>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: report\n  type: any\n  required: true\n  description: Input parameter `report`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.conformance.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-CONFORMANCE-001-000B-DOMAIN-CONFORMANCE-REPORT-RESULTS-IS-LIST.doc.1
    summary: Case `LIB-DOMAIN-CONFORMANCE-001-000B-DOMAIN-CONFORMANCE-REPORT-RESULTS-IS-LIST` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
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
      docs:
      - id: domain.conformance.validate_report_errors.doc.1
        summary: Contract export for `domain.conformance.validate_report_errors`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  report: \"<report>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: report\n  type: any\n  required: true\n  description: Input parameter `report`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.conformance.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-CONFORMANCE-001-000C-DOMAIN-CONFORMANCE-VALIDATE-REPORT-ERRORS.doc.1
    summary: Case `LIB-DOMAIN-CONFORMANCE-001-000C-DOMAIN-CONFORMANCE-VALIDATE-REPORT-ERRORS` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
```




```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.export
contracts:
- id: LIB-CONF-ASSERT-001
  title: reusable conformance assertion helper functions
  clauses:
    predicates:
    - id: __export__conf.pass_when_text_contains
      assert:
        std.string.contains:
        - var: subject
        - var: token
    - id: __export__conf.pass_when_text_regex
      assert:
        std.string.regex_match:
        - var: subject
        - var: pattern
    - id: __export__conf.eq
      assert:
        std.logic.eq:
        - var: subject
        - var: value
    - id: __export__conf.has_error_category
      assert:
        std.string.contains:
        - var: subject
        - var: category
    - id: __export__conf.json_type_is
      assert:
        std.type.json_type:
        - var: subject
        - var: type_name
  harness:
    exports:
    - as: conf.pass_when_text_contains
      from: assert.function
      path: "/__export__conf.pass_when_text_contains"
      params:
      - subject
      - token
      required: true
      doc:
        summary: Contract export for `conf.pass_when_text_contains`.
        description: Auto-generated metadata stub. Replace with authored reference text.
        params:
        - name: subject
          type: any
          required: true
          description: Input parameter `subject`.
        - name: token
          type: any
          required: true
          description: Input parameter `token`.
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
            subject: "<subject>"
            token: "<token>"
          expected: "<result>"
          notes: Replace with a concrete scenario.
        portability:
          python: true
          php: true
          rust: true
          notes: Confirm per-runtime behavior and caveats.
        see_also: []
        since: v1
    - as: conf.pass_when_text_regex
      from: assert.function
      path: "/__export__conf.pass_when_text_regex"
      params:
      - subject
      - pattern
      required: true
      doc:
        summary: Contract export for `conf.pass_when_text_regex`.
        description: Auto-generated metadata stub. Replace with authored reference text.
        params:
        - name: subject
          type: any
          required: true
          description: Input parameter `subject`.
        - name: pattern
          type: any
          required: true
          description: Input parameter `pattern`.
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
            subject: "<subject>"
            pattern: "<pattern>"
          expected: "<result>"
          notes: Replace with a concrete scenario.
        portability:
          python: true
          php: true
          rust: true
          notes: Confirm per-runtime behavior and caveats.
        see_also: []
        since: v1
    - as: conf.eq
      from: assert.function
      path: "/__export__conf.eq"
      params:
      - subject
      - value
      required: true
      doc:
        summary: Contract export for `conf.eq`.
        description: Auto-generated metadata stub. Replace with authored reference text.
        params:
        - name: subject
          type: any
          required: true
          description: Input parameter `subject`.
        - name: value
          type: any
          required: true
          description: Input parameter `value`.
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
            subject: "<subject>"
            value: "<value>"
          expected: "<result>"
          notes: Replace with a concrete scenario.
        portability:
          python: true
          php: true
          rust: true
          notes: Confirm per-runtime behavior and caveats.
        see_also: []
        since: v1
    - as: conf.has_error_category
      from: assert.function
      path: "/__export__conf.has_error_category"
      params:
      - subject
      - category
      required: true
      doc:
        summary: Contract export for `conf.has_error_category`.
        description: Auto-generated metadata stub. Replace with authored reference text.
        params:
        - name: subject
          type: any
          required: true
          description: Input parameter `subject`.
        - name: category
          type: any
          required: true
          description: Input parameter `category`.
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
            subject: "<subject>"
            category: "<category>"
          expected: "<result>"
          notes: Replace with a concrete scenario.
        portability:
          python: true
          php: true
          rust: true
          notes: Confirm per-runtime behavior and caveats.
        see_also: []
        since: v1
    - as: conf.json_type_is
      from: assert.function
      path: "/__export__conf.json_type_is"
      params:
      - subject
      - type_name
      required: true
      doc:
        summary: Contract export for `conf.json_type_is`.
        description: Auto-generated metadata stub. Replace with authored reference text.
        params:
        - name: subject
          type: any
          required: true
          description: Input parameter `subject`.
        - name: type_name
          type: any
          required: true
          description: Input parameter `type_name`.
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
            subject: "<subject>"
            type_name: "<type_name>"
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
    id: conformance.assertion.core
    module: conformance
    stability: alpha
    owner: data-contracts
    tags:
    - conformance
  doc:
    summary: Case `LIB-CONF-ASSERT-001` for `contract.export`.
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    audience: spec-authors
    since: v1
    tags:
    - contract.export
    see_also: []
```

```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.export
contracts:
  - id: LIB-DOMAIN-FS-001-001-DOMAIN-FS-IS-DOCS-SPEC-FILE
    clauses:
      defaults: {}
      predicates:
      - id: __export__domain.fs.is_docs_spec_file
        assert:
          std.logic.and:
          - ops.fs.path.within:
            - /docs
            - ops.fs.path.normalize:
              - {var: path}
          - std.string.ends_with:
            - ops.fs.path.normalize:
              - {var: path}
            - .spec.md
    harness:
      exports:
      - as: domain.fs.is_docs_spec_file
        from: assert.function
        path: /__export__domain.fs.is_docs_spec_file
        params:
        - path
        required: true
        doc:
          summary: Contract export for `domain.fs.is_docs_spec_file`.
          description: Auto-generated metadata stub. Replace with authored reference text.
          params:
          - name: path
            type: any
            required: true
            description: Input parameter `path`.
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
              path: <path>
            expected: <result>
            notes: Replace with a concrete scenario.
          portability:
            python: true
            php: true
            rust: true
            notes: Confirm per-runtime behavior and caveats.
          see_also: []
          since: v1
    library:
      id: domain.fs.core
      module: domain
      stability: alpha
      owner: data-contracts
      tags:
      - domain
    doc:
      summary: Case `LIB-DOMAIN-FS-001-001-DOMAIN-FS-IS-DOCS-SPEC-FILE` for `contract.export`.
      description: Auto-generated root doc metadata stub. Replace with authored reference text.
      audience: spec-authors
      since: v1
      tags:
      - contract.export
      see_also: []
  - id: LIB-DOMAIN-FS-001-002-DOMAIN-FS-SORT-SPEC-FILES
    clauses:
      defaults: {}
      predicates:
      - id: __export__domain.fs.sort_spec_files
        assert:
          ops.fs.path.sort:
          - ops.fs.glob.filter:
            - {var: paths}
            - '*.spec.md'
    harness:
      exports:
      - as: domain.fs.sort_spec_files
        from: assert.function
        path: /__export__domain.fs.sort_spec_files
        params:
        - paths
        required: true
        doc:
          summary: Contract export for `domain.fs.sort_spec_files`.
          description: Auto-generated metadata stub. Replace with authored reference text.
          params:
          - name: paths
            type: any
            required: true
            description: Input parameter `paths`.
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
              paths: <paths>
            expected: <result>
            notes: Replace with a concrete scenario.
          portability:
            python: true
            php: true
            rust: true
            notes: Confirm per-runtime behavior and caveats.
          see_also: []
          since: v1
    library:
      id: domain.fs.core
      module: domain
      stability: alpha
      owner: data-contracts
      tags:
      - domain
    doc:
      summary: Case `LIB-DOMAIN-FS-001-002-DOMAIN-FS-SORT-SPEC-FILES` for `contract.export`.
      description: Auto-generated root doc metadata stub. Replace with authored reference text.
      audience: spec-authors
      since: v1
      tags:
      - contract.export
      see_also: []
  - id: LIB-DOMAIN-FS-001-003-DOMAIN-FS-JSON-GET-OR-TEXT
    clauses:
      defaults: {}
      predicates:
      - id: __export__domain.fs.json_get_or_text
        assert:
          ops.fs.json.get_or:
          - ops.fs.json.parse:
            - {var: json_text}
          - {var: path_segments}
          - {var: fallback}
    harness:
      exports:
      - as: domain.fs.json_get_or_text
        from: assert.function
        path: /__export__domain.fs.json_get_or_text
        params:
        - json_text
        - path_segments
        - fallback
        required: true
        doc:
          summary: Contract export for `domain.fs.json_get_or_text`.
          description: Auto-generated metadata stub. Replace with authored reference text.
          params:
          - name: json_text
            type: any
            required: true
            description: Input parameter `json_text`.
          - name: path_segments
            type: any
            required: true
            description: Input parameter `path_segments`.
          - name: fallback
            type: any
            required: true
            description: Input parameter `fallback`.
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
              json_text: <json_text>
              path_segments: <path_segments>
              fallback: <fallback>
            expected: <result>
            notes: Replace with a concrete scenario.
          portability:
            python: true
            php: true
            rust: true
            notes: Confirm per-runtime behavior and caveats.
          see_also: []
          since: v1
    library:
      id: domain.fs.core
      module: domain
      stability: alpha
      owner: data-contracts
      tags:
      - domain
    doc:
      summary: Case `LIB-DOMAIN-FS-001-003-DOMAIN-FS-JSON-GET-OR-TEXT` for `contract.export`.
      description: Auto-generated root doc metadata stub. Replace with authored reference text.
      audience: spec-authors
      since: v1
      tags:
      - contract.export
      see_also: []
  - id: LIB-DOMAIN-FS-001-004-DOMAIN-FS-JSON-HAS-PATH-TEXT
    clauses:
      defaults: {}
      predicates:
      - id: __export__domain.fs.json_has_path_text
        assert:
          ops.fs.json.has_path:
          - ops.fs.json.parse:
            - {var: json_text}
          - {var: path_segments}
    harness:
      exports:
      - as: domain.fs.json_has_path_text
        from: assert.function
        path: /__export__domain.fs.json_has_path_text
        params:
        - json_text
        - path_segments
        required: true
        doc:
          summary: Contract export for `domain.fs.json_has_path_text`.
          description: Auto-generated metadata stub. Replace with authored reference text.
          params:
          - name: json_text
            type: any
            required: true
            description: Input parameter `json_text`.
          - name: path_segments
            type: any
            required: true
            description: Input parameter `path_segments`.
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
              json_text: <json_text>
              path_segments: <path_segments>
            expected: <result>
            notes: Replace with a concrete scenario.
          portability:
            python: true
            php: true
            rust: true
            notes: Confirm per-runtime behavior and caveats.
          see_also: []
          since: v1
    library:
      id: domain.fs.core
      module: domain
      stability: alpha
      owner: data-contracts
      tags:
      - domain
    doc:
      summary: Case `LIB-DOMAIN-FS-001-004-DOMAIN-FS-JSON-HAS-PATH-TEXT` for `contract.export`.
      description: Auto-generated root doc metadata stub. Replace with authored reference text.
      audience: spec-authors
      since: v1
      tags:
      - contract.export
      see_also: []
  - id: LIB-DOMAIN-FS-001-005-DOMAIN-FS-GLOB-ANY-SPEC-FILES
    clauses:
      defaults: {}
      predicates:
      - id: __export__domain.fs.glob_any_spec_files
        assert:
          ops.fs.glob.any:
          - {var: paths}
          - '*.spec.md'
    harness:
      exports:
      - as: domain.fs.glob_any_spec_files
        from: assert.function
        path: /__export__domain.fs.glob_any_spec_files
        params:
        - paths
        required: true
        doc:
          summary: Contract export for `domain.fs.glob_any_spec_files`.
          description: Auto-generated metadata stub. Replace with authored reference text.
          params:
          - name: paths
            type: any
            required: true
            description: Input parameter `paths`.
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
              paths: <paths>
            expected: <result>
            notes: Replace with a concrete scenario.
          portability:
            python: true
            php: true
            rust: true
            notes: Confirm per-runtime behavior and caveats.
          see_also: []
          since: v1
    library:
      id: domain.fs.core
      module: domain
      stability: alpha
      owner: data-contracts
      tags:
      - domain
    doc:
      summary: Case `LIB-DOMAIN-FS-001-005-DOMAIN-FS-GLOB-ANY-SPEC-FILES` for `contract.export`.
      description: Auto-generated root doc metadata stub. Replace with authored reference text.
      audience: spec-authors
      since: v1
      tags:
      - contract.export
      see_also: []
  - id: LIB-DOMAIN-FS-001-006-DOMAIN-FS-FILE-EXT-EQ
    clauses:
      defaults: {}
      predicates:
      - id: __export__domain.fs.file_ext_eq
        assert:
          ops.fs.path.has_ext:
          - ops.fs.file.path:
            - {var: meta}
          - {var: ext}
    harness:
      exports:
      - as: domain.fs.file_ext_eq
        from: assert.function
        path: /__export__domain.fs.file_ext_eq
        params:
        - meta
        - ext
        required: true
        doc:
          summary: Contract export for `domain.fs.file_ext_eq`.
          description: Auto-generated metadata stub. Replace with authored reference text.
          params:
          - name: meta
            type: any
            required: true
            description: Input parameter `meta`.
          - name: ext
            type: any
            required: true
            description: Input parameter `ext`.
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
              meta: <meta>
              ext: <ext>
            expected: <result>
            notes: Replace with a concrete scenario.
          portability:
            python: true
            php: true
            rust: true
            notes: Confirm per-runtime behavior and caveats.
          see_also: []
          since: v1
    library:
      id: domain.fs.core
      module: domain
      stability: alpha
      owner: data-contracts
      tags:
      - domain
    doc:
      summary: Case `LIB-DOMAIN-FS-001-006-DOMAIN-FS-FILE-EXT-EQ` for `contract.export`.
      description: Auto-generated root doc metadata stub. Replace with authored reference text.
      audience: spec-authors
      since: v1
      tags:
      - contract.export
      see_also: []
  - id: LIB-DOMAIN-FS-001-007-DOMAIN-FS-JSON-GET-TEXT
    clauses:
      defaults: {}
      predicates:
      - id: __export__domain.fs.json_get_text
        assert:
          ops.fs.json.get:
          - ops.fs.json.parse:
            - {var: json_text}
          - {var: path_segments}
    harness:
      exports:
      - as: domain.fs.json_get_text
        from: assert.function
        path: /__export__domain.fs.json_get_text
        params:
        - json_text
        - path_segments
        required: true
        doc:
          summary: Contract export for `domain.fs.json_get_text`.
          description: Auto-generated metadata stub. Replace with authored reference text.
          params:
          - name: json_text
            type: any
            required: true
            description: Input parameter `json_text`.
          - name: path_segments
            type: any
            required: true
            description: Input parameter `path_segments`.
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
              json_text: <json_text>
              path_segments: <path_segments>
            expected: <result>
            notes: Replace with a concrete scenario.
          portability:
            python: true
            php: true
            rust: true
            notes: Confirm per-runtime behavior and caveats.
          see_also: []
          since: v1
    library:
      id: domain.fs.core
      module: domain
      stability: alpha
      owner: data-contracts
      tags:
      - domain
    doc:
      summary: Case `LIB-DOMAIN-FS-001-007-DOMAIN-FS-JSON-GET-TEXT` for `contract.export`.
      description: Auto-generated root doc metadata stub. Replace with authored reference text.
      audience: spec-authors
      since: v1
      tags:
      - contract.export
      see_also: []
  - id: LIB-DOMAIN-FS-001-008-DOMAIN-FS-JSON-PATH-EQ-TEXT
    clauses:
      defaults: {}
      predicates:
      - id: __export__domain.fs.json_path_eq_text
        assert:
          std.logic.eq:
          - call:
            - {var: domain.fs.json_get_or_text}
            - {var: json_text}
            - {var: path_segments}
            - null
          - {var: expected}
    harness:
      exports:
      - as: domain.fs.json_path_eq_text
        from: assert.function
        path: /__export__domain.fs.json_path_eq_text
        params:
        - json_text
        - path_segments
        - expected
        required: true
        doc:
          summary: Contract export for `domain.fs.json_path_eq_text`.
          description: Auto-generated metadata stub. Replace with authored reference text.
          params:
          - name: json_text
            type: any
            required: true
            description: Input parameter `json_text`.
          - name: path_segments
            type: any
            required: true
            description: Input parameter `path_segments`.
          - name: expected
            type: any
            required: true
            description: Input parameter `expected`.
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
              json_text: <json_text>
              path_segments: <path_segments>
              expected: <expected>
            expected: <result>
            notes: Replace with a concrete scenario.
          portability:
            python: true
            php: true
            rust: true
            notes: Confirm per-runtime behavior and caveats.
          see_also: []
          since: v1
    library:
      id: domain.fs.core
      module: domain
      stability: alpha
      owner: data-contracts
      tags:
      - domain
    doc:
      summary: Case `LIB-DOMAIN-FS-001-008-DOMAIN-FS-JSON-PATH-EQ-TEXT` for `contract.export`.
      description: Auto-generated root doc metadata stub. Replace with authored reference text.
      audience: spec-authors
      since: v1
      tags:
      - contract.export
      see_also: []
  - id: LIB-DOMAIN-FS-001-009-DOMAIN-FS-GLOB-FILTER
    clauses:
      defaults: {}
      predicates:
      - id: __export__domain.fs.glob_filter
        assert:
          ops.fs.glob.filter:
          - {var: paths}
          - {var: pattern}
    harness:
      exports:
      - as: domain.fs.glob_filter
        from: assert.function
        path: /__export__domain.fs.glob_filter
        params:
        - paths
        - pattern
        required: true
        doc:
          summary: Contract export for `domain.fs.glob_filter`.
          description: Auto-generated metadata stub. Replace with authored reference text.
          params:
          - name: paths
            type: any
            required: true
            description: Input parameter `paths`.
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
              paths: <paths>
              pattern: <pattern>
            expected: <result>
            notes: Replace with a concrete scenario.
          portability:
            python: true
            php: true
            rust: true
            notes: Confirm per-runtime behavior and caveats.
          see_also: []
          since: v1
    library:
      id: domain.fs.core
      module: domain
      stability: alpha
      owner: data-contracts
      tags:
      - domain
    doc:
      summary: Case `LIB-DOMAIN-FS-001-009-DOMAIN-FS-GLOB-FILTER` for `contract.export`.
      description: Auto-generated root doc metadata stub. Replace with authored reference text.
      audience: spec-authors
      since: v1
      tags:
      - contract.export
      see_also: []
  - id: LIB-DOMAIN-FS-001-010-DOMAIN-FS-GLOB-ALL
    clauses:
      defaults: {}
      predicates:
      - id: __export__domain.fs.glob_all
        assert:
          ops.fs.glob.all:
          - {var: paths}
          - {var: pattern}
    harness:
      exports:
      - as: domain.fs.glob_all
        from: assert.function
        path: /__export__domain.fs.glob_all
        params:
        - paths
        - pattern
        required: true
        doc:
          summary: Contract export for `domain.fs.glob_all`.
          description: Auto-generated metadata stub. Replace with authored reference text.
          params:
          - name: paths
            type: any
            required: true
            description: Input parameter `paths`.
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
              paths: <paths>
              pattern: <pattern>
            expected: <result>
            notes: Replace with a concrete scenario.
          portability:
            python: true
            php: true
            rust: true
            notes: Confirm per-runtime behavior and caveats.
          see_also: []
          since: v1
    library:
      id: domain.fs.core
      module: domain
      stability: alpha
      owner: data-contracts
      tags:
      - domain
    doc:
      summary: Case `LIB-DOMAIN-FS-001-010-DOMAIN-FS-GLOB-ALL` for `contract.export`.
      description: Auto-generated root doc metadata stub. Replace with authored reference text.
      audience: spec-authors
      since: v1
      tags:
      - contract.export
      see_also: []
```










```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.export
contracts:
- id: LIB-DOMAIN-FS-001-001-DOMAIN-FS-IS-DOCS-SPEC-FILE
  clauses:
    predicates:
    - id: __export__domain.fs.is_docs_spec_file
      assert:
        std.logic.and:
        - ops.fs.path.within:
          - "/docs"
          - ops.fs.path.normalize:
            - var: path
        - std.string.ends_with:
          - ops.fs.path.normalize:
            - var: path
          - ".spec.md"
  harness:
    exports:
    - as: domain.fs.is_docs_spec_file
      from: assert.function
      path: "/__export__domain.fs.is_docs_spec_file"
      params:
      - path
      required: true
      docs:
      - id: domain.fs.is_docs_spec_file.doc.1
        summary: Contract export for `domain.fs.is_docs_spec_file`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.fs.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-FS-001-001-DOMAIN-FS-IS-DOCS-SPEC-FILE.doc.1
    summary: Case `LIB-DOMAIN-FS-001-001-DOMAIN-FS-IS-DOCS-SPEC-FILE` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-FS-001-002-DOMAIN-FS-SORT-SPEC-FILES
  clauses:
    predicates:
    - id: __export__domain.fs.sort_spec_files
      assert:
        ops.fs.path.sort:
        - ops.fs.glob.filter:
          - var: paths
          - "*.spec.md"
  harness:
    exports:
    - as: domain.fs.sort_spec_files
      from: assert.function
      path: "/__export__domain.fs.sort_spec_files"
      params:
      - paths
      required: true
      docs:
      - id: domain.fs.sort_spec_files.doc.1
        summary: Contract export for `domain.fs.sort_spec_files`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  paths: \"<paths>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: paths\n  type: any\n  required: true\n  description: Input parameter `paths`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.fs.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-FS-001-002-DOMAIN-FS-SORT-SPEC-FILES.doc.1
    summary: Case `LIB-DOMAIN-FS-001-002-DOMAIN-FS-SORT-SPEC-FILES` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-FS-001-003-DOMAIN-FS-JSON-GET-OR-TEXT
  clauses:
    predicates:
    - id: __export__domain.fs.json_get_or_text
      assert:
        ops.fs.json.get_or:
        - ops.fs.json.parse:
          - var: json_text
        - var: path_segments
        - var: fallback
  harness:
    exports:
    - as: domain.fs.json_get_or_text
      from: assert.function
      path: "/__export__domain.fs.json_get_or_text"
      params:
      - json_text
      - path_segments
      - fallback
      required: true
      docs:
      - id: domain.fs.json_get_or_text.doc.1
        summary: Contract export for `domain.fs.json_get_or_text`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  json_text: \"<json_text>\"\n  path_segments: \"<path_segments>\"\n  fallback: \"<fallback>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: json_text\n  type: any\n  required: true\n  description: Input parameter `json_text`.\n- name: path_segments\n  type: any\n  required: true\n  description: Input parameter `path_segments`.\n- name: fallback\n  type: any\n  required: true\n  description: Input parameter `fallback`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.fs.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-FS-001-003-DOMAIN-FS-JSON-GET-OR-TEXT.doc.1
    summary: Case `LIB-DOMAIN-FS-001-003-DOMAIN-FS-JSON-GET-OR-TEXT` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-FS-001-004-DOMAIN-FS-JSON-HAS-PATH-TEXT
  clauses:
    predicates:
    - id: __export__domain.fs.json_has_path_text
      assert:
        ops.fs.json.has_path:
        - ops.fs.json.parse:
          - var: json_text
        - var: path_segments
  harness:
    exports:
    - as: domain.fs.json_has_path_text
      from: assert.function
      path: "/__export__domain.fs.json_has_path_text"
      params:
      - json_text
      - path_segments
      required: true
      docs:
      - id: domain.fs.json_has_path_text.doc.1
        summary: Contract export for `domain.fs.json_has_path_text`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  json_text: \"<json_text>\"\n  path_segments: \"<path_segments>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: json_text\n  type: any\n  required: true\n  description: Input parameter `json_text`.\n- name: path_segments\n  type: any\n  required: true\n  description: Input parameter `path_segments`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.fs.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-FS-001-004-DOMAIN-FS-JSON-HAS-PATH-TEXT.doc.1
    summary: Case `LIB-DOMAIN-FS-001-004-DOMAIN-FS-JSON-HAS-PATH-TEXT` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-FS-001-005-DOMAIN-FS-GLOB-ANY-SPEC-FILES
  clauses:
    predicates:
    - id: __export__domain.fs.glob_any_spec_files
      assert:
        ops.fs.glob.any:
        - var: paths
        - "*.spec.md"
  harness:
    exports:
    - as: domain.fs.glob_any_spec_files
      from: assert.function
      path: "/__export__domain.fs.glob_any_spec_files"
      params:
      - paths
      required: true
      docs:
      - id: domain.fs.glob_any_spec_files.doc.1
        summary: Contract export for `domain.fs.glob_any_spec_files`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  paths: \"<paths>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: paths\n  type: any\n  required: true\n  description: Input parameter `paths`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.fs.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-FS-001-005-DOMAIN-FS-GLOB-ANY-SPEC-FILES.doc.1
    summary: Case `LIB-DOMAIN-FS-001-005-DOMAIN-FS-GLOB-ANY-SPEC-FILES` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-FS-001-006-DOMAIN-FS-FILE-EXT-EQ
  clauses:
    predicates:
    - id: __export__domain.fs.file_ext_eq
      assert:
        ops.fs.path.has_ext:
        - ops.fs.file.path:
          - var: meta
        - var: ext
  harness:
    exports:
    - as: domain.fs.file_ext_eq
      from: assert.function
      path: "/__export__domain.fs.file_ext_eq"
      params:
      - meta
      - ext
      required: true
      docs:
      - id: domain.fs.file_ext_eq.doc.1
        summary: Contract export for `domain.fs.file_ext_eq`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  meta: \"<meta>\"\n  ext: \"<ext>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: meta\n  type: any\n  required: true\n  description: Input parameter `meta`.\n- name: ext\n  type: any\n  required: true\n  description: Input parameter `ext`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.fs.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-FS-001-006-DOMAIN-FS-FILE-EXT-EQ.doc.1
    summary: Case `LIB-DOMAIN-FS-001-006-DOMAIN-FS-FILE-EXT-EQ` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-FS-001-007-DOMAIN-FS-JSON-GET-TEXT
  clauses:
    predicates:
    - id: __export__domain.fs.json_get_text
      assert:
        ops.fs.json.get:
        - ops.fs.json.parse:
          - var: json_text
        - var: path_segments
  harness:
    exports:
    - as: domain.fs.json_get_text
      from: assert.function
      path: "/__export__domain.fs.json_get_text"
      params:
      - json_text
      - path_segments
      required: true
      docs:
      - id: domain.fs.json_get_text.doc.1
        summary: Contract export for `domain.fs.json_get_text`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  json_text: \"<json_text>\"\n  path_segments: \"<path_segments>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: json_text\n  type: any\n  required: true\n  description: Input parameter `json_text`.\n- name: path_segments\n  type: any\n  required: true\n  description: Input parameter `path_segments`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.fs.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-FS-001-007-DOMAIN-FS-JSON-GET-TEXT.doc.1
    summary: Case `LIB-DOMAIN-FS-001-007-DOMAIN-FS-JSON-GET-TEXT` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-FS-001-008-DOMAIN-FS-JSON-PATH-EQ-TEXT
  clauses:
    predicates:
    - id: __export__domain.fs.json_path_eq_text
      assert:
        std.logic.eq:
        - call:
          - var: domain.fs.json_get_or_text
          - var: json_text
          - var: path_segments
          - 
        - var: expected
  harness:
    exports:
    - as: domain.fs.json_path_eq_text
      from: assert.function
      path: "/__export__domain.fs.json_path_eq_text"
      params:
      - json_text
      - path_segments
      - expected
      required: true
      docs:
      - id: domain.fs.json_path_eq_text.doc.1
        summary: Contract export for `domain.fs.json_path_eq_text`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  json_text: \"<json_text>\"\n  path_segments: \"<path_segments>\"\n  expected: \"<expected>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: json_text\n  type: any\n  required: true\n  description: Input parameter `json_text`.\n- name: path_segments\n  type: any\n  required: true\n  description: Input parameter `path_segments`.\n- name: expected\n  type: any\n  required: true\n  description: Input parameter `expected`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.fs.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-FS-001-008-DOMAIN-FS-JSON-PATH-EQ-TEXT.doc.1
    summary: Case `LIB-DOMAIN-FS-001-008-DOMAIN-FS-JSON-PATH-EQ-TEXT` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-FS-001-009-DOMAIN-FS-GLOB-FILTER
  clauses:
    predicates:
    - id: __export__domain.fs.glob_filter
      assert:
        ops.fs.glob.filter:
        - var: paths
        - var: pattern
  harness:
    exports:
    - as: domain.fs.glob_filter
      from: assert.function
      path: "/__export__domain.fs.glob_filter"
      params:
      - paths
      - pattern
      required: true
      docs:
      - id: domain.fs.glob_filter.doc.1
        summary: Contract export for `domain.fs.glob_filter`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  paths: \"<paths>\"\n  pattern: \"<pattern>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: paths\n  type: any\n  required: true\n  description: Input parameter `paths`.\n- name: pattern\n  type: any\n  required: true\n  description: Input parameter `pattern`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.fs.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-FS-001-009-DOMAIN-FS-GLOB-FILTER.doc.1
    summary: Case `LIB-DOMAIN-FS-001-009-DOMAIN-FS-GLOB-FILTER` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-FS-001-010-DOMAIN-FS-GLOB-ALL
  clauses:
    predicates:
    - id: __export__domain.fs.glob_all
      assert:
        ops.fs.glob.all:
        - var: paths
        - var: pattern
  harness:
    exports:
    - as: domain.fs.glob_all
      from: assert.function
      path: "/__export__domain.fs.glob_all"
      params:
      - paths
      - pattern
      required: true
      docs:
      - id: domain.fs.glob_all.doc.1
        summary: Contract export for `domain.fs.glob_all`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  paths: \"<paths>\"\n  pattern: \"<pattern>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: paths\n  type: any\n  required: true\n  description: Input parameter `paths`.\n- name: pattern\n  type: any\n  required: true\n  description: Input parameter `pattern`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.fs.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-FS-001-010-DOMAIN-FS-GLOB-ALL.doc.1
    summary: Case `LIB-DOMAIN-FS-001-010-DOMAIN-FS-GLOB-ALL` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
```










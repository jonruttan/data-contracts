```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.export
contracts:
- id: LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE
  clauses:
    predicates:
    - id: __export__domain.path.normalize
      assert:
        ops.fs.path.normalize:
        - var: path
  harness:
    exports:
    - as: domain.path.normalize
      from: assert.function
      path: "/__export__domain.path.normalize"
      params:
      - path
      required: true
      docs:
      - id: domain.path.normalize.doc.1
        summary: Contract export for `domain.path.normalize`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.path.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE.doc.1
    summary: Case `LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-PATH-001-002-DOMAIN-PATH-EQ
  clauses:
    predicates:
    - id: __export__domain.path.eq
      assert:
        std.logic.eq:
        - ops.fs.path.normalize:
          - var: left
        - ops.fs.path.normalize:
          - var: right
  harness:
    exports:
    - as: domain.path.eq
      from: assert.function
      path: "/__export__domain.path.eq"
      params:
      - left
      - right
      required: true
      docs:
      - id: domain.path.eq.doc.1
        summary: Contract export for `domain.path.eq`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  left: \"<left>\"\n  right: \"<right>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: left\n  type: any\n  required: true\n  description: Input parameter `left`.\n- name: right\n  type: any\n  required: true\n  description: Input parameter `right`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.path.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-PATH-001-002-DOMAIN-PATH-EQ.doc.1
    summary: Case `LIB-DOMAIN-PATH-001-002-DOMAIN-PATH-EQ` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-PATH-001-003-DOMAIN-PATH-IS-SPEC-MD
  clauses:
    predicates:
    - id: __export__domain.path.is_spec_md
      assert:
        std.string.ends_with:
        - ops.fs.path.normalize:
          - var: path
        - ".spec.md"
  harness:
    exports:
    - as: domain.path.is_spec_md
      from: assert.function
      path: "/__export__domain.path.is_spec_md"
      params:
      - path
      required: true
      docs:
      - id: domain.path.is_spec_md.doc.1
        summary: Contract export for `domain.path.is_spec_md`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.path.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-PATH-001-003-DOMAIN-PATH-IS-SPEC-MD.doc.1
    summary: Case `LIB-DOMAIN-PATH-001-003-DOMAIN-PATH-IS-SPEC-MD` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-PATH-001-004-DOMAIN-PATH-IS-IN-DOCS
  clauses:
    predicates:
    - id: __export__domain.path.is_in_docs
      assert:
        ops.fs.path.within:
        - "/docs"
        - ops.fs.path.normalize:
          - var: path
  harness:
    exports:
    - as: domain.path.is_in_docs
      from: assert.function
      path: "/__export__domain.path.is_in_docs"
      params:
      - path
      required: true
      docs:
      - id: domain.path.is_in_docs.doc.1
        summary: Contract export for `domain.path.is_in_docs`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.path.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-PATH-001-004-DOMAIN-PATH-IS-IN-DOCS.doc.1
    summary: Case `LIB-DOMAIN-PATH-001-004-DOMAIN-PATH-IS-IN-DOCS` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-PATH-001-005-DOMAIN-PATH-SORTED
  clauses:
    predicates:
    - id: __export__domain.path.sorted
      assert:
        ops.fs.path.sort:
        - var: paths
  harness:
    exports:
    - as: domain.path.sorted
      from: assert.function
      path: "/__export__domain.path.sorted"
      params:
      - paths
      required: true
      docs:
      - id: domain.path.sorted.doc.1
        summary: Contract export for `domain.path.sorted`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  paths: \"<paths>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: paths\n  type: any\n  required: true\n  description: Input parameter `paths`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.path.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-PATH-001-005-DOMAIN-PATH-SORTED.doc.1
    summary: Case `LIB-DOMAIN-PATH-001-005-DOMAIN-PATH-SORTED` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-PATH-001-006-DOMAIN-FILE-IS-EXISTING-FILE
  clauses:
    predicates:
    - id: __export__domain.file.is_existing_file
      assert:
        std.logic.and:
        - ops.fs.file.exists:
          - var: meta
        - ops.fs.file.is_file:
          - var: meta
  harness:
    exports:
    - as: domain.file.is_existing_file
      from: assert.function
      path: "/__export__domain.file.is_existing_file"
      params:
      - meta
      required: true
      docs:
      - id: domain.file.is_existing_file.doc.1
        summary: Contract export for `domain.file.is_existing_file`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  meta: \"<meta>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: meta\n  type: any\n  required: true\n  description: Input parameter `meta`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.path.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-PATH-001-006-DOMAIN-FILE-IS-EXISTING-FILE.doc.1
    summary: Case `LIB-DOMAIN-PATH-001-006-DOMAIN-FILE-IS-EXISTING-FILE` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-PATH-001-007-DOMAIN-FILE-IS-EXISTING-DIR
  clauses:
    predicates:
    - id: __export__domain.file.is_existing_dir
      assert:
        std.logic.and:
        - ops.fs.file.exists:
          - var: meta
        - ops.fs.file.is_dir:
          - var: meta
  harness:
    exports:
    - as: domain.file.is_existing_dir
      from: assert.function
      path: "/__export__domain.file.is_existing_dir"
      params:
      - meta
      required: true
      docs:
      - id: domain.file.is_existing_dir.doc.1
        summary: Contract export for `domain.file.is_existing_dir`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  meta: \"<meta>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: meta\n  type: any\n  required: true\n  description: Input parameter `meta`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.path.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-PATH-001-007-DOMAIN-FILE-IS-EXISTING-DIR.doc.1
    summary: Case `LIB-DOMAIN-PATH-001-007-DOMAIN-FILE-IS-EXISTING-DIR` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-PATH-001-008-DOMAIN-FILE-HAS-EXT
  clauses:
    predicates:
    - id: __export__domain.file.has_ext
      assert:
        ops.fs.path.has_ext:
        - ops.fs.file.path:
          - var: meta
        - var: ext
  harness:
    exports:
    - as: domain.file.has_ext
      from: assert.function
      path: "/__export__domain.file.has_ext"
      params:
      - meta
      - ext
      required: true
      docs:
      - id: domain.file.has_ext.doc.1
        summary: Contract export for `domain.file.has_ext`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  meta: \"<meta>\"\n  ext: \"<ext>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: meta\n  type: any\n  required: true\n  description: Input parameter `meta`.\n- name: ext\n  type: any\n  required: true\n  description: Input parameter `ext`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.path.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-PATH-001-008-DOMAIN-FILE-HAS-EXT.doc.1
    summary: Case `LIB-DOMAIN-PATH-001-008-DOMAIN-FILE-HAS-EXT` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-PATH-001-009-DOMAIN-FILE-NAME
  clauses:
    predicates:
    - id: __export__domain.file.name
      assert:
        ops.fs.file.name:
        - var: meta
  harness:
    exports:
    - as: domain.file.name
      from: assert.function
      path: "/__export__domain.file.name"
      params:
      - meta
      required: true
      docs:
      - id: domain.file.name.doc.1
        summary: Contract export for `domain.file.name`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  meta: \"<meta>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: meta\n  type: any\n  required: true\n  description: Input parameter `meta`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.path.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-PATH-001-009-DOMAIN-FILE-NAME.doc.1
    summary: Case `LIB-DOMAIN-PATH-001-009-DOMAIN-FILE-NAME` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
```









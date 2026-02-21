```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
contracts:
- id: LIB-PATH-001-001-PATH-NORMALIZE-SLASHES
  type: contract.export
  clauses:
    predicates:
    - id: __export__path.normalize_slashes
      assert:
        std.string.replace:
        - var: path
        - "\\"
        - "/"
    - id: __export__path.trim_dot
      assert:
        std.string.replace:
        - var: path
        - "./"
        - ''
    - id: __export__path.dirname
      assert:
        lit:
          let:
          - lit:
            - - segs
              - call:
                - var: path.segments
                - var: path
          - if:
            - std.logic.lte:
              - std.collection.len:
                - var: segs
              - 1
            - ''
            - std.string.join:
              - std.collection.slice:
                - 0
                - std.math.sub:
                  - std.collection.len:
                    - var: segs
                  - 1
                - var: segs
              - "/"
    - id: __export__path.has_extension
      assert:
        std.logic.eq:
        - call:
          - var: path.extension
          - var: path
        - var: ext
    - id: __export__path.is_under
      assert:
        std.string.starts_with:
        - call:
          - var: path.normalize_slashes
          - var: path
        - call:
          - var: path.normalize_slashes
          - var: prefix
    - id: __export__path.matches
      assert:
        std.string.regex_match:
        - call:
          - var: path.normalize_slashes
          - var: path
        - var: pattern
  harness:
    exports:
    - as: path.normalize_slashes
      from: assert.function
      path: "/__export__path.normalize_slashes"
      params:
      - path
      docs:
      - id: path.normalize_slashes.doc.1
        summary: Contract export for `path.normalize_slashes`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: path.trim_dot
      from: assert.function
      path: "/__export__path.trim_dot"
      params:
      - path
      docs:
      - id: path.trim_dot.doc.1
        summary: Contract export for `path.trim_dot`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: path.dirname
      from: assert.function
      path: "/__export__path.dirname"
      params:
      - path
      docs:
      - id: path.dirname.doc.1
        summary: Contract export for `path.dirname`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: path.has_extension
      from: assert.function
      path: "/__export__path.has_extension"
      params:
      - path
      - ext
      docs:
      - id: path.has_extension.doc.1
        summary: Contract export for `path.has_extension`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\n  ext: \"<ext>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- name: ext\n  type: any\n  required: true\n  description: Input parameter `ext`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: path.is_under
      from: assert.function
      path: "/__export__path.is_under"
      params:
      - path
      - prefix
      docs:
      - id: path.is_under.doc.1
        summary: Contract export for `path.is_under`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\n  prefix: \"<prefix>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- name: prefix\n  type: any\n  required: true\n  description: Input parameter `prefix`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: path.matches
      from: assert.function
      path: "/__export__path.matches"
      params:
      - path
      - pattern
      docs:
      - id: path.matches.doc.1
        summary: Contract export for `path.matches`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\n  pattern: \"<pattern>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- name: pattern\n  type: any\n  required: true\n  description: Input parameter `pattern`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: path.path.core
    module: path
    stability: alpha
    owner: data-contracts
    tags:
    - path
  docs:
  - id: LIB-PATH-001-001-PATH-NORMALIZE-SLASHES.doc.1
    summary: Case `LIB-PATH-001-001-PATH-NORMALIZE-SLASHES` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-PATH-001-002-PATH-SEGMENTS
  type: contract.export
  clauses:
    predicates:
    - id: __export__path.segments
      assert:
        std.string.split:
        - call:
          - var: path.normalize_slashes
          - var: path
        - "/"
    - id: __export__path.trim_dot
      assert:
        std.string.replace:
        - var: path
        - "./"
        - ''
    - id: __export__path.dirname
      assert:
        lit:
          let:
          - lit:
            - - segs
              - call:
                - var: path.segments
                - var: path
          - if:
            - std.logic.lte:
              - std.collection.len:
                - var: segs
              - 1
            - ''
            - std.string.join:
              - std.collection.slice:
                - 0
                - std.math.sub:
                  - std.collection.len:
                    - var: segs
                  - 1
                - var: segs
              - "/"
    - id: __export__path.has_extension
      assert:
        std.logic.eq:
        - call:
          - var: path.extension
          - var: path
        - var: ext
    - id: __export__path.is_under
      assert:
        std.string.starts_with:
        - call:
          - var: path.normalize_slashes
          - var: path
        - call:
          - var: path.normalize_slashes
          - var: prefix
    - id: __export__path.matches
      assert:
        std.string.regex_match:
        - call:
          - var: path.normalize_slashes
          - var: path
        - var: pattern
  harness:
    exports:
    - as: path.segments
      from: assert.function
      path: "/__export__path.segments"
      params:
      - path
      docs:
      - id: path.segments.doc.1
        summary: Contract export for `path.segments`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: path.trim_dot
      from: assert.function
      path: "/__export__path.trim_dot"
      params:
      - path
      docs:
      - id: path.trim_dot.doc.1
        summary: Contract export for `path.trim_dot`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: path.dirname
      from: assert.function
      path: "/__export__path.dirname"
      params:
      - path
      docs:
      - id: path.dirname.doc.1
        summary: Contract export for `path.dirname`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: path.has_extension
      from: assert.function
      path: "/__export__path.has_extension"
      params:
      - path
      - ext
      docs:
      - id: path.has_extension.doc.1
        summary: Contract export for `path.has_extension`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\n  ext: \"<ext>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- name: ext\n  type: any\n  required: true\n  description: Input parameter `ext`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: path.is_under
      from: assert.function
      path: "/__export__path.is_under"
      params:
      - path
      - prefix
      docs:
      - id: path.is_under.doc.1
        summary: Contract export for `path.is_under`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\n  prefix: \"<prefix>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- name: prefix\n  type: any\n  required: true\n  description: Input parameter `prefix`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: path.matches
      from: assert.function
      path: "/__export__path.matches"
      params:
      - path
      - pattern
      docs:
      - id: path.matches.doc.1
        summary: Contract export for `path.matches`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\n  pattern: \"<pattern>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- name: pattern\n  type: any\n  required: true\n  description: Input parameter `pattern`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: path.path.core
    module: path
    stability: alpha
    owner: data-contracts
    tags:
    - path
  docs:
  - id: LIB-PATH-001-002-PATH-SEGMENTS.doc.1
    summary: Case `LIB-PATH-001-002-PATH-SEGMENTS` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-PATH-001-003-PATH-BASENAME
  type: contract.export
  clauses:
    predicates:
    - id: __export__path.basename
      assert:
        lit:
          let:
          - lit:
            - - segs
              - call:
                - var: path.segments
                - var: path
          - if:
            - std.collection.is_empty:
              - var: segs
            - ''
            - std.object.get:
              - var: segs
              - std.math.sub:
                - std.collection.len:
                  - var: segs
                - 1
    - id: __export__path.trim_dot
      assert:
        std.string.replace:
        - var: path
        - "./"
        - ''
    - id: __export__path.dirname
      assert:
        lit:
          let:
          - lit:
            - - segs
              - call:
                - var: path.segments
                - var: path
          - if:
            - std.logic.lte:
              - std.collection.len:
                - var: segs
              - 1
            - ''
            - std.string.join:
              - std.collection.slice:
                - 0
                - std.math.sub:
                  - std.collection.len:
                    - var: segs
                  - 1
                - var: segs
              - "/"
    - id: __export__path.has_extension
      assert:
        std.logic.eq:
        - call:
          - var: path.extension
          - var: path
        - var: ext
    - id: __export__path.is_under
      assert:
        std.string.starts_with:
        - call:
          - var: path.normalize_slashes
          - var: path
        - call:
          - var: path.normalize_slashes
          - var: prefix
    - id: __export__path.matches
      assert:
        std.string.regex_match:
        - call:
          - var: path.normalize_slashes
          - var: path
        - var: pattern
  harness:
    exports:
    - as: path.basename
      from: assert.function
      path: "/__export__path.basename"
      params:
      - path
      docs:
      - id: path.basename.doc.1
        summary: Contract export for `path.basename`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: path.trim_dot
      from: assert.function
      path: "/__export__path.trim_dot"
      params:
      - path
      docs:
      - id: path.trim_dot.doc.1
        summary: Contract export for `path.trim_dot`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: path.dirname
      from: assert.function
      path: "/__export__path.dirname"
      params:
      - path
      docs:
      - id: path.dirname.doc.1
        summary: Contract export for `path.dirname`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: path.has_extension
      from: assert.function
      path: "/__export__path.has_extension"
      params:
      - path
      - ext
      docs:
      - id: path.has_extension.doc.1
        summary: Contract export for `path.has_extension`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\n  ext: \"<ext>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- name: ext\n  type: any\n  required: true\n  description: Input parameter `ext`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: path.is_under
      from: assert.function
      path: "/__export__path.is_under"
      params:
      - path
      - prefix
      docs:
      - id: path.is_under.doc.1
        summary: Contract export for `path.is_under`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\n  prefix: \"<prefix>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- name: prefix\n  type: any\n  required: true\n  description: Input parameter `prefix`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: path.matches
      from: assert.function
      path: "/__export__path.matches"
      params:
      - path
      - pattern
      docs:
      - id: path.matches.doc.1
        summary: Contract export for `path.matches`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\n  pattern: \"<pattern>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- name: pattern\n  type: any\n  required: true\n  description: Input parameter `pattern`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: path.path.core
    module: path
    stability: alpha
    owner: data-contracts
    tags:
    - path
  docs:
  - id: LIB-PATH-001-003-PATH-BASENAME.doc.1
    summary: Case `LIB-PATH-001-003-PATH-BASENAME` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-PATH-001-004-PATH-EXTENSION
  type: contract.export
  clauses:
    predicates:
    - id: __export__path.extension
      assert:
        lit:
          let:
          - lit:
            - - base
              - call:
                - var: path.basename
                - var: path
          - let:
            - lit:
              - - parts
                - split:
                  - var: base
                  - "."
            - if:
              - std.logic.lte:
                - std.collection.len:
                  - var: parts
                - 1
              - ''
              - std.object.get:
                - var: parts
                - std.math.sub:
                  - std.collection.len:
                    - var: parts
                  - 1
    - id: __export__path.trim_dot
      assert:
        std.string.replace:
        - var: path
        - "./"
        - ''
    - id: __export__path.dirname
      assert:
        lit:
          let:
          - lit:
            - - segs
              - call:
                - var: path.segments
                - var: path
          - if:
            - std.logic.lte:
              - std.collection.len:
                - var: segs
              - 1
            - ''
            - std.string.join:
              - std.collection.slice:
                - 0
                - std.math.sub:
                  - std.collection.len:
                    - var: segs
                  - 1
                - var: segs
              - "/"
    - id: __export__path.has_extension
      assert:
        std.logic.eq:
        - call:
          - var: path.extension
          - var: path
        - var: ext
    - id: __export__path.is_under
      assert:
        std.string.starts_with:
        - call:
          - var: path.normalize_slashes
          - var: path
        - call:
          - var: path.normalize_slashes
          - var: prefix
    - id: __export__path.matches
      assert:
        std.string.regex_match:
        - call:
          - var: path.normalize_slashes
          - var: path
        - var: pattern
  harness:
    exports:
    - as: path.extension
      from: assert.function
      path: "/__export__path.extension"
      params:
      - path
      docs:
      - id: path.extension.doc.1
        summary: Contract export for `path.extension`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: path.trim_dot
      from: assert.function
      path: "/__export__path.trim_dot"
      params:
      - path
      docs:
      - id: path.trim_dot.doc.1
        summary: Contract export for `path.trim_dot`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: path.dirname
      from: assert.function
      path: "/__export__path.dirname"
      params:
      - path
      docs:
      - id: path.dirname.doc.1
        summary: Contract export for `path.dirname`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: path.has_extension
      from: assert.function
      path: "/__export__path.has_extension"
      params:
      - path
      - ext
      docs:
      - id: path.has_extension.doc.1
        summary: Contract export for `path.has_extension`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\n  ext: \"<ext>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- name: ext\n  type: any\n  required: true\n  description: Input parameter `ext`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: path.is_under
      from: assert.function
      path: "/__export__path.is_under"
      params:
      - path
      - prefix
      docs:
      - id: path.is_under.doc.1
        summary: Contract export for `path.is_under`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\n  prefix: \"<prefix>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- name: prefix\n  type: any\n  required: true\n  description: Input parameter `prefix`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: path.matches
      from: assert.function
      path: "/__export__path.matches"
      params:
      - path
      - pattern
      docs:
      - id: path.matches.doc.1
        summary: Contract export for `path.matches`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  path: \"<path>\"\n  pattern: \"<pattern>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: path\n  type: any\n  required: true\n  description: Input parameter `path`.\n- name: pattern\n  type: any\n  required: true\n  description: Input parameter `pattern`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: path.path.core
    module: path
    stability: alpha
    owner: data-contracts
    tags:
    - path
  docs:
  - id: LIB-PATH-001-004-PATH-EXTENSION.doc.1
    summary: Case `LIB-PATH-001-004-PATH-EXTENSION` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-PATH-001-900-PATH-SMOKE
  type: contract.check
  harness:
    check:
      profile: text.file
      config: {}
    use:
    - ref: "#LIB-PATH-001-001-PATH-NORMALIZE-SLASHES"
      as: lib_path_normalize
      symbols:
      - path.normalize_slashes
  clauses:
    imports:
    - from: artifact
      names:
      - text
    predicates:
    - id: assert_1
      assert:
        std.logic.eq:
        - call:
          - var: path.normalize_slashes
          - a\\b\\c.txt
        - a/b/c.txt
```





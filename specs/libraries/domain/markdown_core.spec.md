```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.export
contracts:
- id: LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING
  title: 'markdown projection helper functions: domain.markdown.has_heading'
  clauses:
    predicates:
    - id: __export__domain.markdown.has_heading
      assert:
        std.logic.or:
        - std.collection.any:
          - std.collection.map:
            - fn:
              - - row
              - std.logic.eq:
                - std.string.lower:
                  - std.object.get:
                    - var: row
                    - text
                - std.string.lower:
                  - var: heading
            - call:
              - var: markdown._headings
              - var: subject
        - std.logic.or:
          - std.string.contains:
            - call:
              - var: markdown._text
              - var: subject
            - std.string.join:
              - std.collection.append:
                - var: heading
                - lit:
                  - "# "
              - ''
          - std.logic.or:
            - std.string.contains:
              - call:
                - var: markdown._text
                - var: subject
              - std.string.join:
                - std.collection.append:
                  - var: heading
                  - lit:
                    - "## "
                - ''
            - std.logic.or:
              - std.string.contains:
                - call:
                  - var: markdown._text
                  - var: subject
                - std.string.join:
                  - std.collection.append:
                    - var: heading
                    - lit:
                      - "### "
                  - ''
              - std.logic.or:
                - std.string.contains:
                  - call:
                    - var: markdown._text
                    - var: subject
                  - std.string.join:
                    - std.collection.append:
                      - var: heading
                      - lit:
                        - "#### "
                    - ''
                - std.logic.or:
                  - std.string.contains:
                    - call:
                      - var: markdown._text
                      - var: subject
                    - std.string.join:
                      - std.collection.append:
                        - var: heading
                        - lit:
                          - "##### "
                      - ''
                  - std.string.contains:
                    - call:
                      - var: markdown._text
                      - var: subject
                    - std.string.join:
                      - std.collection.append:
                        - var: heading
                        - lit:
                          - "###### "
                      - ''
    - id: __export__markdown._text
      assert:
        lit:
          if:
          - std.type.is_string:
            - var: subject
          - var: subject
          - std.null.default_to:
            - ''
            - std.object.get:
              - var: subject
              - value
    - id: __export__markdown._context
      assert:
        lit:
          if:
          - std.type.is_dict:
            - var: subject
          - std.null.default_to:
            - lit: {}
            - std.object.get:
              - var: subject
              - context
          - lit: {}
    - id: __export__markdown._headings
      assert:
        std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - var: markdown._context
            - var: subject
          - headings
    - id: __export__markdown._links
      assert:
        std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - var: markdown._context
            - var: subject
          - links
    - id: __export__markdown._tokens_map
      assert:
        std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - var: markdown._context
            - var: subject
          - tokens
    - id: __export__markdown._token_owners
      assert:
        std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - var: markdown._context
            - var: subject
          - token_owners
    - id: __export__markdown._token_dependencies
      assert:
        std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - var: markdown._context
            - var: subject
          - token_dependencies
  harness:
    exports:
    - as: domain.markdown.has_heading
      from: assert.function
      path: "/__export__domain.markdown.has_heading"
      params:
      - subject
      - heading
      required: true
      docs:
      - id: domain.markdown.has_heading.doc.1
        summary: Contract export for `domain.markdown.has_heading`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\n  heading: \"<heading>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: heading\n  type: any\n  required: true\n  description: Input parameter `heading`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: markdown._text
      from: assert.function
      path: "/__export__markdown._text"
      params:
      - subject
      required: true
      docs:
      - id: markdown._text.doc.1
        summary: Contract export for `markdown._text`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: markdown._context
      from: assert.function
      path: "/__export__markdown._context"
      params:
      - subject
      required: true
      docs:
      - id: markdown._context.doc.1
        summary: Contract export for `markdown._context`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: markdown._headings
      from: assert.function
      path: "/__export__markdown._headings"
      params:
      - subject
      required: true
      docs:
      - id: markdown._headings.doc.1
        summary: Contract export for `markdown._headings`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: markdown._links
      from: assert.function
      path: "/__export__markdown._links"
      params:
      - subject
      required: true
      docs:
      - id: markdown._links.doc.1
        summary: Contract export for `markdown._links`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: markdown._tokens_map
      from: assert.function
      path: "/__export__markdown._tokens_map"
      params:
      - subject
      required: true
      docs:
      - id: markdown._tokens_map.doc.1
        summary: Contract export for `markdown._tokens_map`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: markdown._token_owners
      from: assert.function
      path: "/__export__markdown._token_owners"
      params:
      - subject
      required: true
      docs:
      - id: markdown._token_owners.doc.1
        summary: Contract export for `markdown._token_owners`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
    - as: markdown._token_dependencies
      from: assert.function
      path: "/__export__markdown._token_dependencies"
      params:
      - subject
      required: true
      docs:
      - id: markdown._token_dependencies.doc.1
        summary: Contract export for `markdown._token_dependencies`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.markdown.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING.doc.1
    summary: Case `LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-MD-001-003-DOMAIN-MARKDOWN-HEADING-LEVEL-EXISTS
  title: 'markdown projection helper functions: domain.markdown.heading_level_exists'
  clauses:
    predicates:
    - id: __export__domain.markdown.heading_level_exists
      assert:
        std.logic.or:
        - std.collection.any:
          - std.collection.map:
            - fn:
              - - row
              - std.logic.eq:
                - std.object.get:
                  - var: row
                  - level
                - var: level
            - call:
              - var: markdown._headings
              - var: subject
        - if:
          - std.logic.eq:
            - var: level
            - 1
          - std.string.regex_match:
            - call:
              - var: markdown._text
              - var: subject
            - "(?m)^#\\s+"
          - if:
            - std.logic.eq:
              - var: level
              - 2
            - std.string.regex_match:
              - call:
                - var: markdown._text
                - var: subject
              - "(?m)^##\\s+"
            - if:
              - std.logic.eq:
                - var: level
                - 3
              - std.string.regex_match:
                - call:
                  - var: markdown._text
                  - var: subject
                - "(?m)^###\\s+"
              - if:
                - std.logic.eq:
                  - var: level
                  - 4
                - std.string.regex_match:
                  - call:
                    - var: markdown._text
                    - var: subject
                  - "(?m)^####\\s+"
                - if:
                  - std.logic.eq:
                    - var: level
                    - 5
                  - std.string.regex_match:
                    - call:
                      - var: markdown._text
                      - var: subject
                    - "(?m)^#####\\s+"
                  - if:
                    - std.logic.eq:
                      - var: level
                      - 6
                    - std.string.regex_match:
                      - call:
                        - var: markdown._text
                        - var: subject
                      - "(?m)^######\\s+"
                    - false
  harness:
    exports:
    - as: domain.markdown.heading_level_exists
      from: assert.function
      path: "/__export__domain.markdown.heading_level_exists"
      params:
      - subject
      - level
      required: true
      docs:
      - id: domain.markdown.heading_level_exists.doc.1
        summary: Contract export for `domain.markdown.heading_level_exists`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\n  level: \"<level>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: level\n  type: any\n  required: true\n  description: Input parameter `level`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.markdown.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-MD-001-003-DOMAIN-MARKDOWN-HEADING-LEVEL-EXISTS.doc.1
    summary: Case `LIB-DOMAIN-MD-001-003-DOMAIN-MARKDOWN-HEADING-LEVEL-EXISTS` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-MD-001-005-DOMAIN-MARKDOWN-SECTION-ORDER-VALID
  title: 'markdown projection helper functions: domain.markdown.section_order_valid'
  clauses:
    predicates:
    - id: __export__domain.markdown.section_order_valid
      assert:
        std.logic.and:
        - call:
          - var: domain.markdown.required_sections_present
          - var: subject
          - var: headings
        - if:
          - std.logic.lte:
            - std.collection.len:
              - var: headings
            - 1
          - true
          - std.logic.and:
            - std.logic.neq:
              - std.object.get:
                - std.object.get:
                  - call:
                    - var: markdown._context
                    - var: subject
                  - heading_positions
                - std.object.get:
                  - var: headings
                  - 0
              - 
            - std.logic.gt:
              - std.object.get:
                - std.object.get:
                  - call:
                    - var: markdown._context
                    - var: subject
                  - heading_positions
                - std.object.get:
                  - var: headings
                  - 1
              - std.object.get:
                - std.object.get:
                  - call:
                    - var: markdown._context
                    - var: subject
                  - heading_positions
                - std.object.get:
                  - var: headings
                  - 0
  harness:
    exports:
    - as: domain.markdown.section_order_valid
      from: assert.function
      path: "/__export__domain.markdown.section_order_valid"
      params:
      - subject
      - headings
      required: true
      docs:
      - id: domain.markdown.section_order_valid.doc.1
        summary: Contract export for `domain.markdown.section_order_valid`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\n  headings: \"<headings>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: headings\n  type: any\n  required: true\n  description: Input parameter `headings`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.markdown.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-MD-001-005-DOMAIN-MARKDOWN-SECTION-ORDER-VALID.doc.1
    summary: Case `LIB-DOMAIN-MD-001-005-DOMAIN-MARKDOWN-SECTION-ORDER-VALID` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-MD-001-007-DOMAIN-MARKDOWN-REQUIRED-SECTIONS-PRESENT
  title: 'markdown projection helper functions: domain.markdown.required_sections_present'
  clauses:
    predicates:
    - id: __export__domain.markdown.required_sections_present
      assert:
        std.collection.all:
        - std.collection.map:
          - fn:
            - - heading
            - call:
              - var: domain.markdown.has_heading
              - var: subject
              - var: heading
          - var: headings
  harness:
    exports:
    - as: domain.markdown.required_sections_present
      from: assert.function
      path: "/__export__domain.markdown.required_sections_present"
      params:
      - subject
      - headings
      required: true
      docs:
      - id: domain.markdown.required_sections_present.doc.1
        summary: Contract export for `domain.markdown.required_sections_present`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\n  headings: \"<headings>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: headings\n  type: any\n  required: true\n  description: Input parameter `headings`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.markdown.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-MD-001-007-DOMAIN-MARKDOWN-REQUIRED-SECTIONS-PRESENT.doc.1
    summary: Case `LIB-DOMAIN-MD-001-007-DOMAIN-MARKDOWN-REQUIRED-SECTIONS-PRESENT` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-MD-001-009-DOMAIN-MARKDOWN-LINK-TARGETS-ALL-RESOLVE
  title: 'markdown projection helper functions: domain.markdown.link_targets_all_resolve'
  clauses:
    predicates:
    - id: __export__domain.markdown.link_targets_all_resolve
      assert:
        std.collection.all:
        - std.collection.map:
          - fn:
            - - row
            - std.logic.eq:
              - std.object.get:
                - var: row
                - resolved
              - true
          - call:
            - var: markdown._links
            - var: subject
  harness:
    exports:
    - as: domain.markdown.link_targets_all_resolve
      from: assert.function
      path: "/__export__domain.markdown.link_targets_all_resolve"
      params:
      - subject
      required: true
      docs:
      - id: domain.markdown.link_targets_all_resolve.doc.1
        summary: Contract export for `domain.markdown.link_targets_all_resolve`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.markdown.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-MD-001-009-DOMAIN-MARKDOWN-LINK-TARGETS-ALL-RESOLVE.doc.1
    summary: Case `LIB-DOMAIN-MD-001-009-DOMAIN-MARKDOWN-LINK-TARGETS-ALL-RESOLVE` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-MD-001-011-DOMAIN-MARKDOWN-HAS-BROKEN-LINKS
  title: 'markdown projection helper functions: domain.markdown.has_broken_links'
  clauses:
    predicates:
    - id: __export__domain.markdown.has_broken_links
      assert:
        std.logic.not:
        - call:
          - var: domain.markdown.link_targets_all_resolve
          - var: subject
  harness:
    exports:
    - as: domain.markdown.has_broken_links
      from: assert.function
      path: "/__export__domain.markdown.has_broken_links"
      params:
      - subject
      required: true
      docs:
      - id: domain.markdown.has_broken_links.doc.1
        summary: Contract export for `domain.markdown.has_broken_links`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.markdown.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-MD-001-011-DOMAIN-MARKDOWN-HAS-BROKEN-LINKS.doc.1
    summary: Case `LIB-DOMAIN-MD-001-011-DOMAIN-MARKDOWN-HAS-BROKEN-LINKS` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-MD-001-013-DOMAIN-MARKDOWN-HAS-YAML-SPEC-TEST-FENCE
  title: 'markdown projection helper functions: domain.markdown.has_yaml_spec_test_fence'
  clauses:
    predicates:
    - id: __export__domain.markdown.has_yaml_spec_test_fence
      assert:
        std.logic.or:
        - std.string.contains:
          - call:
            - var: markdown._text
            - var: subject
          - "```yaml contract-spec"
        - std.string.contains:
          - call:
            - var: markdown._text
            - var: subject
          - "~~~yaml contract-spec"
  harness:
    exports:
    - as: domain.markdown.has_yaml_spec_test_fence
      from: assert.function
      path: "/__export__domain.markdown.has_yaml_spec_test_fence"
      params:
      - subject
      required: true
      docs:
      - id: domain.markdown.has_yaml_spec_test_fence.doc.1
        summary: Contract export for `domain.markdown.has_yaml_spec_test_fence`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.markdown.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-MD-001-013-DOMAIN-MARKDOWN-HAS-YAML-SPEC-TEST-FENCE.doc.1
    summary: Case `LIB-DOMAIN-MD-001-013-DOMAIN-MARKDOWN-HAS-YAML-SPEC-TEST-FENCE` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-MD-001-015-DOMAIN-MARKDOWN-CODE-FENCE-LANGUAGE-EXISTS
  title: 'markdown projection helper functions: domain.markdown.code_fence_language_exists'
  clauses:
    predicates:
    - id: __export__domain.markdown.code_fence_language_exists
      assert:
        std.logic.or:
        - std.string.contains:
          - call:
            - var: markdown._text
            - var: subject
          - std.string.join:
            - std.collection.append:
              - var: language
              - lit:
                - "```"
            - ''
        - std.string.contains:
          - call:
            - var: markdown._text
            - var: subject
          - std.string.join:
            - std.collection.append:
              - var: language
              - lit:
                - "~~~"
            - ''
  harness:
    exports:
    - as: domain.markdown.code_fence_language_exists
      from: assert.function
      path: "/__export__domain.markdown.code_fence_language_exists"
      params:
      - subject
      - language
      required: true
      docs:
      - id: domain.markdown.code_fence_language_exists.doc.1
        summary: Contract export for `domain.markdown.code_fence_language_exists`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\n  language: \"<language>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: language\n  type: any\n  required: true\n  description: Input parameter `language`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.markdown.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-MD-001-015-DOMAIN-MARKDOWN-CODE-FENCE-LANGUAGE-EXISTS.doc.1
    summary: Case `LIB-DOMAIN-MD-001-015-DOMAIN-MARKDOWN-CODE-FENCE-LANGUAGE-EXISTS` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-MD-001-017-DOMAIN-MARKDOWN-TOKEN-PRESENT
  title: 'markdown projection helper functions: domain.markdown.token_present'
  clauses:
    predicates:
    - id: __export__domain.markdown.token_present
      assert:
        std.logic.or:
        - std.object.has_key:
          - call:
            - var: markdown._tokens_map
            - var: subject
          - var: token
        - std.string.contains:
          - call:
            - var: markdown._text
            - var: subject
          - var: token
  harness:
    exports:
    - as: domain.markdown.token_present
      from: assert.function
      path: "/__export__domain.markdown.token_present"
      params:
      - subject
      - token
      required: true
      docs:
      - id: domain.markdown.token_present.doc.1
        summary: Contract export for `domain.markdown.token_present`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\n  token: \"<token>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: token\n  type: any\n  required: true\n  description: Input parameter `token`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.markdown.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-MD-001-017-DOMAIN-MARKDOWN-TOKEN-PRESENT.doc.1
    summary: Case `LIB-DOMAIN-MD-001-017-DOMAIN-MARKDOWN-TOKEN-PRESENT` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-MD-001-019-DOMAIN-MARKDOWN-TOKENS-ALL-PRESENT
  title: 'markdown projection helper functions: domain.markdown.tokens_all_present'
  clauses:
    predicates:
    - id: __export__domain.markdown.tokens_all_present
      assert:
        std.collection.all:
        - std.collection.map:
          - fn:
            - - token
            - call:
              - var: domain.markdown.token_present
              - var: subject
              - var: token
          - var: tokens
  harness:
    exports:
    - as: domain.markdown.tokens_all_present
      from: assert.function
      path: "/__export__domain.markdown.tokens_all_present"
      params:
      - subject
      - tokens
      required: true
      docs:
      - id: domain.markdown.tokens_all_present.doc.1
        summary: Contract export for `domain.markdown.tokens_all_present`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\n  tokens: \"<tokens>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- name: tokens\n  type: any\n  required: true\n  description: Input parameter `tokens`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.markdown.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-MD-001-019-DOMAIN-MARKDOWN-TOKENS-ALL-PRESENT.doc.1
    summary: Case `LIB-DOMAIN-MD-001-019-DOMAIN-MARKDOWN-TOKENS-ALL-PRESENT` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-MD-001-021-DOMAIN-MARKDOWN-TOKEN-OWNERSHIP-UNIQUE
  title: 'markdown projection helper functions: domain.markdown.token_ownership_unique'
  clauses:
    predicates:
    - id: __export__domain.markdown.token_ownership_unique
      assert:
        std.collection.all:
        - std.collection.map:
          - fn:
            - - owners
            - std.logic.eq:
              - std.collection.len:
                - var: owners
              - 1
          - std.object.values:
            - call:
              - var: markdown._token_owners
              - var: subject
  harness:
    exports:
    - as: domain.markdown.token_ownership_unique
      from: assert.function
      path: "/__export__domain.markdown.token_ownership_unique"
      params:
      - subject
      required: true
      docs:
      - id: domain.markdown.token_ownership_unique.doc.1
        summary: Contract export for `domain.markdown.token_ownership_unique`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.markdown.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-MD-001-021-DOMAIN-MARKDOWN-TOKEN-OWNERSHIP-UNIQUE.doc.1
    summary: Case `LIB-DOMAIN-MD-001-021-DOMAIN-MARKDOWN-TOKEN-OWNERSHIP-UNIQUE` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
- id: LIB-DOMAIN-MD-001-023-DOMAIN-MARKDOWN-TOKEN-DEPENDENCIES-RESOLVED
  title: 'markdown projection helper functions: domain.markdown.token_dependencies_resolved'
  clauses:
    predicates:
    - id: __export__domain.markdown.token_dependencies_resolved
      assert:
        std.collection.all:
        - std.collection.map:
          - fn:
            - - dep
            - std.logic.eq:
              - std.object.get:
                - var: dep
                - resolved
              - true
          - call:
            - var: markdown._token_dependencies
            - var: subject
  harness:
    exports:
    - as: domain.markdown.token_dependencies_resolved
      from: assert.function
      path: "/__export__domain.markdown.token_dependencies_resolved"
      params:
      - subject
      required: true
      docs:
      - id: domain.markdown.token_dependencies_resolved.doc.1
        summary: Contract export for `domain.markdown.token_dependencies_resolved`.
        audience: spec-authors
        status: active
        description: "Auto-generated metadata stub. Replace with authored reference text.\n\nLegacy doc fields migrated to description:\n- examples[]: title: Basic usage\ninput:\n  subject: \"<subject>\"\nexpected: \"<result>\"\nnotes: Replace with a concrete scenario.\n- params: - name: subject\n  type: any\n  required: true\n  description: Input parameter `subject`.\n- returns: type: any\ndescription: Result payload for this symbol.\n- errors: - code: SCHEMA_ERROR\n  when: Input payload does not satisfy contract shape requirements.\n  category: schema\n- portability: python: true\nphp: true\nrust: true\nnotes: Confirm per-runtime behavior and caveats."
        since: v1
  library:
    id: domain.markdown.core
    module: domain
    stability: alpha
    owner: data-contracts
    tags:
    - domain
  docs:
  - id: LIB-DOMAIN-MD-001-023-DOMAIN-MARKDOWN-TOKEN-DEPENDENCIES-RESOLVED.doc.1
    summary: Case `LIB-DOMAIN-MD-001-023-DOMAIN-MARKDOWN-TOKEN-DEPENDENCIES-RESOLVED` for `contract.export`.
    audience: spec-authors
    status: active
    description: Auto-generated root doc metadata stub. Replace with authored reference text.
    since: v1
    tags:
    - contract.export
```




































# Spec-Lang Markdown Domain Library

## LIB-DOMAIN-MD-001

```yaml spec-test
id: LIB-DOMAIN-MD-001-001-DOMAIN-MARKDOWN-HAS-HEADING
title: 'markdown projection helper functions: domain.markdown.has_heading'
type: spec_lang.export
defines:
  public:
    domain.markdown.has_heading:
      fn:
      - [subject, heading]
      - std.logic.or:
        - std.collection.any:
          - std.collection.map:
            - fn:
              - [row]
              - std.logic.eq:
                - std.string.lower:
                  - std.object.get:
                    - {var: row}
                    - text
                - std.string.lower:
                  - {var: heading}
            - call:
              - {var: markdown._headings}
              - {var: subject}
        - std.logic.or:
          - std.string.contains:
            - call:
              - {var: markdown._text}
              - {var: subject}
            - std.string.join:
              - std.collection.append:
                - {var: heading}
                - lit:
                  - '# '
              - ''
          - std.logic.or:
            - std.string.contains:
              - call:
                - {var: markdown._text}
                - {var: subject}
              - std.string.join:
                - std.collection.append:
                  - {var: heading}
                  - lit:
                    - '## '
                - ''
            - std.logic.or:
              - std.string.contains:
                - call:
                  - {var: markdown._text}
                  - {var: subject}
                - std.string.join:
                  - std.collection.append:
                    - {var: heading}
                    - lit:
                      - '### '
                  - ''
              - std.logic.or:
                - std.string.contains:
                  - call:
                    - {var: markdown._text}
                    - {var: subject}
                  - std.string.join:
                    - std.collection.append:
                      - {var: heading}
                      - lit:
                        - '#### '
                    - ''
                - std.logic.or:
                  - std.string.contains:
                    - call:
                      - {var: markdown._text}
                      - {var: subject}
                    - std.string.join:
                      - std.collection.append:
                        - {var: heading}
                        - lit:
                          - '##### '
                      - ''
                  - std.string.contains:
                    - call:
                      - {var: markdown._text}
                      - {var: subject}
                    - std.string.join:
                      - std.collection.append:
                        - {var: heading}
                        - lit:
                          - '###### '
                      - ''
  private:
    markdown._text:
      fn:
      - [subject]
      - if:
        - std.type.is_string:
          - {var: subject}
        - {var: subject}
        - std.null.default_to:
          - ''
          - std.object.get:
            - {var: subject}
            - value
    markdown._context:
      fn:
      - [subject]
      - if:
        - std.type.is_dict:
          - {var: subject}
        - std.null.default_to:
          - lit: {}
          - std.object.get:
            - {var: subject}
            - context
        - lit: {}
    markdown._headings:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - headings
    markdown._links:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - links
    markdown._tokens_map:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - tokens
    markdown._token_owners:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_owners
    markdown._token_dependencies:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_dependencies
harness:
  chain:
    exports:
    - as: domain.markdown.has_heading
      from: assert.function
      path: /domain.markdown.has_heading
      required: true
    - as: domain.markdown.heading_level_exists
      from: assert.function
      path: /domain.markdown.heading_level_exists
      required: true
    - as: domain.markdown.section_order_valid
      from: assert.function
      path: /domain.markdown.section_order_valid
      required: true
    - as: domain.markdown.required_sections_present
      from: assert.function
      path: /domain.markdown.required_sections_present
      required: true
    - as: domain.markdown.link_targets_all_resolve
      from: assert.function
      path: /domain.markdown.link_targets_all_resolve
      required: true
    - as: domain.markdown.has_broken_links
      from: assert.function
      path: /domain.markdown.has_broken_links
      required: true
    - as: domain.markdown.has_yaml_spec_test_fence
      from: assert.function
      path: /domain.markdown.has_yaml_spec_test_fence
      required: true
    - as: domain.markdown.code_fence_language_exists
      from: assert.function
      path: /domain.markdown.code_fence_language_exists
      required: true
    - as: domain.markdown.token_present
      from: assert.function
      path: /domain.markdown.token_present
      required: true
    - as: domain.markdown.tokens_all_present
      from: assert.function
      path: /domain.markdown.tokens_all_present
      required: true
    - as: domain.markdown.token_ownership_unique
      from: assert.function
      path: /domain.markdown.token_ownership_unique
      required: true
    - as: domain.markdown.token_dependencies_resolved
      from: assert.function
      path: /domain.markdown.token_dependencies_resolved
      required: true
```



```yaml spec-test
id: LIB-DOMAIN-MD-001-003-DOMAIN-MARKDOWN-HEADING-LEVEL-EXISTS
title: 'markdown projection helper functions: domain.markdown.heading_level_exists'
type: spec_lang.export
defines:
  public:
    domain.markdown.heading_level_exists:
      fn:
      - [subject, level]
      - std.logic.or:
        - std.collection.any:
          - std.collection.map:
            - fn:
              - [row]
              - std.logic.eq:
                - std.object.get:
                  - {var: row}
                  - level
                - {var: level}
            - call:
              - {var: markdown._headings}
              - {var: subject}
        - if:
          - std.logic.eq:
            - {var: level}
            - 1
          - std.string.regex_match:
            - call:
              - {var: markdown._text}
              - {var: subject}
            - (?m)^#\s+
          - if:
            - std.logic.eq:
              - {var: level}
              - 2
            - std.string.regex_match:
              - call:
                - {var: markdown._text}
                - {var: subject}
              - (?m)^##\s+
            - if:
              - std.logic.eq:
                - {var: level}
                - 3
              - std.string.regex_match:
                - call:
                  - {var: markdown._text}
                  - {var: subject}
                - (?m)^###\s+
              - if:
                - std.logic.eq:
                  - {var: level}
                  - 4
                - std.string.regex_match:
                  - call:
                    - {var: markdown._text}
                    - {var: subject}
                  - (?m)^####\s+
                - if:
                  - std.logic.eq:
                    - {var: level}
                    - 5
                  - std.string.regex_match:
                    - call:
                      - {var: markdown._text}
                      - {var: subject}
                    - (?m)^#####\s+
                  - if:
                    - std.logic.eq:
                      - {var: level}
                      - 6
                    - std.string.regex_match:
                      - call:
                        - {var: markdown._text}
                        - {var: subject}
                      - (?m)^######\s+
                    - false
  private:
    markdown._text:
      fn:
      - [subject]
      - if:
        - std.type.is_string:
          - {var: subject}
        - {var: subject}
        - std.null.default_to:
          - ''
          - std.object.get:
            - {var: subject}
            - value
    markdown._context:
      fn:
      - [subject]
      - if:
        - std.type.is_dict:
          - {var: subject}
        - std.null.default_to:
          - lit: {}
          - std.object.get:
            - {var: subject}
            - context
        - lit: {}
    markdown._headings:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - headings
    markdown._links:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - links
    markdown._tokens_map:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - tokens
    markdown._token_owners:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_owners
    markdown._token_dependencies:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_dependencies
harness:
  chain:
    exports:
    - as: domain.markdown.has_heading
      from: assert.function
      path: /domain.markdown.has_heading
      required: true
    - as: domain.markdown.heading_level_exists
      from: assert.function
      path: /domain.markdown.heading_level_exists
      required: true
    - as: domain.markdown.section_order_valid
      from: assert.function
      path: /domain.markdown.section_order_valid
      required: true
    - as: domain.markdown.required_sections_present
      from: assert.function
      path: /domain.markdown.required_sections_present
      required: true
    - as: domain.markdown.link_targets_all_resolve
      from: assert.function
      path: /domain.markdown.link_targets_all_resolve
      required: true
    - as: domain.markdown.has_broken_links
      from: assert.function
      path: /domain.markdown.has_broken_links
      required: true
    - as: domain.markdown.has_yaml_spec_test_fence
      from: assert.function
      path: /domain.markdown.has_yaml_spec_test_fence
      required: true
    - as: domain.markdown.code_fence_language_exists
      from: assert.function
      path: /domain.markdown.code_fence_language_exists
      required: true
    - as: domain.markdown.token_present
      from: assert.function
      path: /domain.markdown.token_present
      required: true
    - as: domain.markdown.tokens_all_present
      from: assert.function
      path: /domain.markdown.tokens_all_present
      required: true
    - as: domain.markdown.token_ownership_unique
      from: assert.function
      path: /domain.markdown.token_ownership_unique
      required: true
    - as: domain.markdown.token_dependencies_resolved
      from: assert.function
      path: /domain.markdown.token_dependencies_resolved
      required: true
```



```yaml spec-test
id: LIB-DOMAIN-MD-001-005-DOMAIN-MARKDOWN-SECTION-ORDER-VALID
title: 'markdown projection helper functions: domain.markdown.section_order_valid'
type: spec_lang.export
defines:
  public:
    domain.markdown.section_order_valid:
      fn:
      - [subject, headings]
      - std.logic.and:
        - call:
          - {var: domain.markdown.required_sections_present}
          - {var: subject}
          - {var: headings}
        - if:
          - std.logic.lte:
            - std.collection.len:
              - {var: headings}
            - 1
          - true
          - std.logic.and:
            - std.logic.neq:
              - std.object.get:
                - std.object.get:
                  - call:
                    - {var: markdown._context}
                    - {var: subject}
                  - heading_positions
                - std.object.get:
                  - {var: headings}
                  - 0
              - null
            - std.logic.gt:
              - std.object.get:
                - std.object.get:
                  - call:
                    - {var: markdown._context}
                    - {var: subject}
                  - heading_positions
                - std.object.get:
                  - {var: headings}
                  - 1
              - std.object.get:
                - std.object.get:
                  - call:
                    - {var: markdown._context}
                    - {var: subject}
                  - heading_positions
                - std.object.get:
                  - {var: headings}
                  - 0
  private:
    markdown._text:
      fn:
      - [subject]
      - if:
        - std.type.is_string:
          - {var: subject}
        - {var: subject}
        - std.null.default_to:
          - ''
          - std.object.get:
            - {var: subject}
            - value
    markdown._context:
      fn:
      - [subject]
      - if:
        - std.type.is_dict:
          - {var: subject}
        - std.null.default_to:
          - lit: {}
          - std.object.get:
            - {var: subject}
            - context
        - lit: {}
    markdown._headings:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - headings
    markdown._links:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - links
    markdown._tokens_map:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - tokens
    markdown._token_owners:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_owners
    markdown._token_dependencies:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_dependencies
harness:
  chain:
    exports:
    - as: domain.markdown.has_heading
      from: assert.function
      path: /domain.markdown.has_heading
      required: true
    - as: domain.markdown.heading_level_exists
      from: assert.function
      path: /domain.markdown.heading_level_exists
      required: true
    - as: domain.markdown.section_order_valid
      from: assert.function
      path: /domain.markdown.section_order_valid
      required: true
    - as: domain.markdown.required_sections_present
      from: assert.function
      path: /domain.markdown.required_sections_present
      required: true
    - as: domain.markdown.link_targets_all_resolve
      from: assert.function
      path: /domain.markdown.link_targets_all_resolve
      required: true
    - as: domain.markdown.has_broken_links
      from: assert.function
      path: /domain.markdown.has_broken_links
      required: true
    - as: domain.markdown.has_yaml_spec_test_fence
      from: assert.function
      path: /domain.markdown.has_yaml_spec_test_fence
      required: true
    - as: domain.markdown.code_fence_language_exists
      from: assert.function
      path: /domain.markdown.code_fence_language_exists
      required: true
    - as: domain.markdown.token_present
      from: assert.function
      path: /domain.markdown.token_present
      required: true
    - as: domain.markdown.tokens_all_present
      from: assert.function
      path: /domain.markdown.tokens_all_present
      required: true
    - as: domain.markdown.token_ownership_unique
      from: assert.function
      path: /domain.markdown.token_ownership_unique
      required: true
    - as: domain.markdown.token_dependencies_resolved
      from: assert.function
      path: /domain.markdown.token_dependencies_resolved
      required: true
```



```yaml spec-test
id: LIB-DOMAIN-MD-001-007-DOMAIN-MARKDOWN-REQUIRED-SECTIONS-PRESENT
title: 'markdown projection helper functions: domain.markdown.required_sections_present'
type: spec_lang.export
defines:
  public:
    domain.markdown.required_sections_present:
      fn:
      - [subject, headings]
      - std.collection.all:
        - std.collection.map:
          - fn:
            - [heading]
            - call:
              - {var: domain.markdown.has_heading}
              - {var: subject}
              - {var: heading}
          - {var: headings}
  private:
    markdown._text:
      fn:
      - [subject]
      - if:
        - std.type.is_string:
          - {var: subject}
        - {var: subject}
        - std.null.default_to:
          - ''
          - std.object.get:
            - {var: subject}
            - value
    markdown._context:
      fn:
      - [subject]
      - if:
        - std.type.is_dict:
          - {var: subject}
        - std.null.default_to:
          - lit: {}
          - std.object.get:
            - {var: subject}
            - context
        - lit: {}
    markdown._headings:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - headings
    markdown._links:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - links
    markdown._tokens_map:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - tokens
    markdown._token_owners:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_owners
    markdown._token_dependencies:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_dependencies
harness:
  chain:
    exports:
    - as: domain.markdown.has_heading
      from: assert.function
      path: /domain.markdown.has_heading
      required: true
    - as: domain.markdown.heading_level_exists
      from: assert.function
      path: /domain.markdown.heading_level_exists
      required: true
    - as: domain.markdown.section_order_valid
      from: assert.function
      path: /domain.markdown.section_order_valid
      required: true
    - as: domain.markdown.required_sections_present
      from: assert.function
      path: /domain.markdown.required_sections_present
      required: true
    - as: domain.markdown.link_targets_all_resolve
      from: assert.function
      path: /domain.markdown.link_targets_all_resolve
      required: true
    - as: domain.markdown.has_broken_links
      from: assert.function
      path: /domain.markdown.has_broken_links
      required: true
    - as: domain.markdown.has_yaml_spec_test_fence
      from: assert.function
      path: /domain.markdown.has_yaml_spec_test_fence
      required: true
    - as: domain.markdown.code_fence_language_exists
      from: assert.function
      path: /domain.markdown.code_fence_language_exists
      required: true
    - as: domain.markdown.token_present
      from: assert.function
      path: /domain.markdown.token_present
      required: true
    - as: domain.markdown.tokens_all_present
      from: assert.function
      path: /domain.markdown.tokens_all_present
      required: true
    - as: domain.markdown.token_ownership_unique
      from: assert.function
      path: /domain.markdown.token_ownership_unique
      required: true
    - as: domain.markdown.token_dependencies_resolved
      from: assert.function
      path: /domain.markdown.token_dependencies_resolved
      required: true
```



```yaml spec-test
id: LIB-DOMAIN-MD-001-009-DOMAIN-MARKDOWN-LINK-TARGETS-ALL-RESOLVE
title: 'markdown projection helper functions: domain.markdown.link_targets_all_resolve'
type: spec_lang.export
defines:
  public:
    domain.markdown.link_targets_all_resolve:
      fn:
      - [subject]
      - std.collection.all:
        - std.collection.map:
          - fn:
            - [row]
            - std.logic.eq:
              - std.object.get:
                - {var: row}
                - resolved
              - true
          - call:
            - {var: markdown._links}
            - {var: subject}
  private:
    markdown._text:
      fn:
      - [subject]
      - if:
        - std.type.is_string:
          - {var: subject}
        - {var: subject}
        - std.null.default_to:
          - ''
          - std.object.get:
            - {var: subject}
            - value
    markdown._context:
      fn:
      - [subject]
      - if:
        - std.type.is_dict:
          - {var: subject}
        - std.null.default_to:
          - lit: {}
          - std.object.get:
            - {var: subject}
            - context
        - lit: {}
    markdown._headings:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - headings
    markdown._links:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - links
    markdown._tokens_map:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - tokens
    markdown._token_owners:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_owners
    markdown._token_dependencies:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_dependencies
harness:
  chain:
    exports:
    - as: domain.markdown.has_heading
      from: assert.function
      path: /domain.markdown.has_heading
      required: true
    - as: domain.markdown.heading_level_exists
      from: assert.function
      path: /domain.markdown.heading_level_exists
      required: true
    - as: domain.markdown.section_order_valid
      from: assert.function
      path: /domain.markdown.section_order_valid
      required: true
    - as: domain.markdown.required_sections_present
      from: assert.function
      path: /domain.markdown.required_sections_present
      required: true
    - as: domain.markdown.link_targets_all_resolve
      from: assert.function
      path: /domain.markdown.link_targets_all_resolve
      required: true
    - as: domain.markdown.has_broken_links
      from: assert.function
      path: /domain.markdown.has_broken_links
      required: true
    - as: domain.markdown.has_yaml_spec_test_fence
      from: assert.function
      path: /domain.markdown.has_yaml_spec_test_fence
      required: true
    - as: domain.markdown.code_fence_language_exists
      from: assert.function
      path: /domain.markdown.code_fence_language_exists
      required: true
    - as: domain.markdown.token_present
      from: assert.function
      path: /domain.markdown.token_present
      required: true
    - as: domain.markdown.tokens_all_present
      from: assert.function
      path: /domain.markdown.tokens_all_present
      required: true
    - as: domain.markdown.token_ownership_unique
      from: assert.function
      path: /domain.markdown.token_ownership_unique
      required: true
    - as: domain.markdown.token_dependencies_resolved
      from: assert.function
      path: /domain.markdown.token_dependencies_resolved
      required: true
```



```yaml spec-test
id: LIB-DOMAIN-MD-001-011-DOMAIN-MARKDOWN-HAS-BROKEN-LINKS
title: 'markdown projection helper functions: domain.markdown.has_broken_links'
type: spec_lang.export
defines:
  public:
    domain.markdown.has_broken_links:
      fn:
      - [subject]
      - std.logic.not:
        - call:
          - {var: domain.markdown.link_targets_all_resolve}
          - {var: subject}
  private:
    markdown._text:
      fn:
      - [subject]
      - if:
        - std.type.is_string:
          - {var: subject}
        - {var: subject}
        - std.null.default_to:
          - ''
          - std.object.get:
            - {var: subject}
            - value
    markdown._context:
      fn:
      - [subject]
      - if:
        - std.type.is_dict:
          - {var: subject}
        - std.null.default_to:
          - lit: {}
          - std.object.get:
            - {var: subject}
            - context
        - lit: {}
    markdown._headings:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - headings
    markdown._links:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - links
    markdown._tokens_map:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - tokens
    markdown._token_owners:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_owners
    markdown._token_dependencies:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_dependencies
harness:
  chain:
    exports:
    - as: domain.markdown.has_heading
      from: assert.function
      path: /domain.markdown.has_heading
      required: true
    - as: domain.markdown.heading_level_exists
      from: assert.function
      path: /domain.markdown.heading_level_exists
      required: true
    - as: domain.markdown.section_order_valid
      from: assert.function
      path: /domain.markdown.section_order_valid
      required: true
    - as: domain.markdown.required_sections_present
      from: assert.function
      path: /domain.markdown.required_sections_present
      required: true
    - as: domain.markdown.link_targets_all_resolve
      from: assert.function
      path: /domain.markdown.link_targets_all_resolve
      required: true
    - as: domain.markdown.has_broken_links
      from: assert.function
      path: /domain.markdown.has_broken_links
      required: true
    - as: domain.markdown.has_yaml_spec_test_fence
      from: assert.function
      path: /domain.markdown.has_yaml_spec_test_fence
      required: true
    - as: domain.markdown.code_fence_language_exists
      from: assert.function
      path: /domain.markdown.code_fence_language_exists
      required: true
    - as: domain.markdown.token_present
      from: assert.function
      path: /domain.markdown.token_present
      required: true
    - as: domain.markdown.tokens_all_present
      from: assert.function
      path: /domain.markdown.tokens_all_present
      required: true
    - as: domain.markdown.token_ownership_unique
      from: assert.function
      path: /domain.markdown.token_ownership_unique
      required: true
    - as: domain.markdown.token_dependencies_resolved
      from: assert.function
      path: /domain.markdown.token_dependencies_resolved
      required: true
```



```yaml spec-test
id: LIB-DOMAIN-MD-001-013-DOMAIN-MARKDOWN-HAS-YAML-SPEC-TEST-FENCE
title: 'markdown projection helper functions: domain.markdown.has_yaml_spec_test_fence'
type: spec_lang.export
defines:
  public:
    domain.markdown.has_yaml_spec_test_fence:
      fn:
      - [subject]
      - std.logic.or:
        - std.string.contains:
          - call:
            - {var: markdown._text}
            - {var: subject}
          - '```yaml spec-test'
        - std.string.contains:
          - call:
            - {var: markdown._text}
            - {var: subject}
          - ~~~yaml spec-test
  private:
    markdown._text:
      fn:
      - [subject]
      - if:
        - std.type.is_string:
          - {var: subject}
        - {var: subject}
        - std.null.default_to:
          - ''
          - std.object.get:
            - {var: subject}
            - value
    markdown._context:
      fn:
      - [subject]
      - if:
        - std.type.is_dict:
          - {var: subject}
        - std.null.default_to:
          - lit: {}
          - std.object.get:
            - {var: subject}
            - context
        - lit: {}
    markdown._headings:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - headings
    markdown._links:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - links
    markdown._tokens_map:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - tokens
    markdown._token_owners:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_owners
    markdown._token_dependencies:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_dependencies
harness:
  chain:
    exports:
    - as: domain.markdown.has_heading
      from: assert.function
      path: /domain.markdown.has_heading
      required: true
    - as: domain.markdown.heading_level_exists
      from: assert.function
      path: /domain.markdown.heading_level_exists
      required: true
    - as: domain.markdown.section_order_valid
      from: assert.function
      path: /domain.markdown.section_order_valid
      required: true
    - as: domain.markdown.required_sections_present
      from: assert.function
      path: /domain.markdown.required_sections_present
      required: true
    - as: domain.markdown.link_targets_all_resolve
      from: assert.function
      path: /domain.markdown.link_targets_all_resolve
      required: true
    - as: domain.markdown.has_broken_links
      from: assert.function
      path: /domain.markdown.has_broken_links
      required: true
    - as: domain.markdown.has_yaml_spec_test_fence
      from: assert.function
      path: /domain.markdown.has_yaml_spec_test_fence
      required: true
    - as: domain.markdown.code_fence_language_exists
      from: assert.function
      path: /domain.markdown.code_fence_language_exists
      required: true
    - as: domain.markdown.token_present
      from: assert.function
      path: /domain.markdown.token_present
      required: true
    - as: domain.markdown.tokens_all_present
      from: assert.function
      path: /domain.markdown.tokens_all_present
      required: true
    - as: domain.markdown.token_ownership_unique
      from: assert.function
      path: /domain.markdown.token_ownership_unique
      required: true
    - as: domain.markdown.token_dependencies_resolved
      from: assert.function
      path: /domain.markdown.token_dependencies_resolved
      required: true
```



```yaml spec-test
id: LIB-DOMAIN-MD-001-015-DOMAIN-MARKDOWN-CODE-FENCE-LANGUAGE-EXISTS
title: 'markdown projection helper functions: domain.markdown.code_fence_language_exists'
type: spec_lang.export
defines:
  public:
    domain.markdown.code_fence_language_exists:
      fn:
      - [subject, language]
      - std.logic.or:
        - std.string.contains:
          - call:
            - {var: markdown._text}
            - {var: subject}
          - std.string.join:
            - std.collection.append:
              - {var: language}
              - lit:
                - '```'
            - ''
        - std.string.contains:
          - call:
            - {var: markdown._text}
            - {var: subject}
          - std.string.join:
            - std.collection.append:
              - {var: language}
              - lit:
                - ~~~
            - ''
  private:
    markdown._text:
      fn:
      - [subject]
      - if:
        - std.type.is_string:
          - {var: subject}
        - {var: subject}
        - std.null.default_to:
          - ''
          - std.object.get:
            - {var: subject}
            - value
    markdown._context:
      fn:
      - [subject]
      - if:
        - std.type.is_dict:
          - {var: subject}
        - std.null.default_to:
          - lit: {}
          - std.object.get:
            - {var: subject}
            - context
        - lit: {}
    markdown._headings:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - headings
    markdown._links:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - links
    markdown._tokens_map:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - tokens
    markdown._token_owners:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_owners
    markdown._token_dependencies:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_dependencies
harness:
  chain:
    exports:
    - as: domain.markdown.has_heading
      from: assert.function
      path: /domain.markdown.has_heading
      required: true
    - as: domain.markdown.heading_level_exists
      from: assert.function
      path: /domain.markdown.heading_level_exists
      required: true
    - as: domain.markdown.section_order_valid
      from: assert.function
      path: /domain.markdown.section_order_valid
      required: true
    - as: domain.markdown.required_sections_present
      from: assert.function
      path: /domain.markdown.required_sections_present
      required: true
    - as: domain.markdown.link_targets_all_resolve
      from: assert.function
      path: /domain.markdown.link_targets_all_resolve
      required: true
    - as: domain.markdown.has_broken_links
      from: assert.function
      path: /domain.markdown.has_broken_links
      required: true
    - as: domain.markdown.has_yaml_spec_test_fence
      from: assert.function
      path: /domain.markdown.has_yaml_spec_test_fence
      required: true
    - as: domain.markdown.code_fence_language_exists
      from: assert.function
      path: /domain.markdown.code_fence_language_exists
      required: true
    - as: domain.markdown.token_present
      from: assert.function
      path: /domain.markdown.token_present
      required: true
    - as: domain.markdown.tokens_all_present
      from: assert.function
      path: /domain.markdown.tokens_all_present
      required: true
    - as: domain.markdown.token_ownership_unique
      from: assert.function
      path: /domain.markdown.token_ownership_unique
      required: true
    - as: domain.markdown.token_dependencies_resolved
      from: assert.function
      path: /domain.markdown.token_dependencies_resolved
      required: true
```



```yaml spec-test
id: LIB-DOMAIN-MD-001-017-DOMAIN-MARKDOWN-TOKEN-PRESENT
title: 'markdown projection helper functions: domain.markdown.token_present'
type: spec_lang.export
defines:
  public:
    domain.markdown.token_present:
      fn:
      - [subject, token]
      - std.logic.or:
        - std.object.has_key:
          - call:
            - {var: markdown._tokens_map}
            - {var: subject}
          - {var: token}
        - std.string.contains:
          - call:
            - {var: markdown._text}
            - {var: subject}
          - {var: token}
  private:
    markdown._text:
      fn:
      - [subject]
      - if:
        - std.type.is_string:
          - {var: subject}
        - {var: subject}
        - std.null.default_to:
          - ''
          - std.object.get:
            - {var: subject}
            - value
    markdown._context:
      fn:
      - [subject]
      - if:
        - std.type.is_dict:
          - {var: subject}
        - std.null.default_to:
          - lit: {}
          - std.object.get:
            - {var: subject}
            - context
        - lit: {}
    markdown._headings:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - headings
    markdown._links:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - links
    markdown._tokens_map:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - tokens
    markdown._token_owners:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_owners
    markdown._token_dependencies:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_dependencies
harness:
  chain:
    exports:
    - as: domain.markdown.has_heading
      from: assert.function
      path: /domain.markdown.has_heading
      required: true
    - as: domain.markdown.heading_level_exists
      from: assert.function
      path: /domain.markdown.heading_level_exists
      required: true
    - as: domain.markdown.section_order_valid
      from: assert.function
      path: /domain.markdown.section_order_valid
      required: true
    - as: domain.markdown.required_sections_present
      from: assert.function
      path: /domain.markdown.required_sections_present
      required: true
    - as: domain.markdown.link_targets_all_resolve
      from: assert.function
      path: /domain.markdown.link_targets_all_resolve
      required: true
    - as: domain.markdown.has_broken_links
      from: assert.function
      path: /domain.markdown.has_broken_links
      required: true
    - as: domain.markdown.has_yaml_spec_test_fence
      from: assert.function
      path: /domain.markdown.has_yaml_spec_test_fence
      required: true
    - as: domain.markdown.code_fence_language_exists
      from: assert.function
      path: /domain.markdown.code_fence_language_exists
      required: true
    - as: domain.markdown.token_present
      from: assert.function
      path: /domain.markdown.token_present
      required: true
    - as: domain.markdown.tokens_all_present
      from: assert.function
      path: /domain.markdown.tokens_all_present
      required: true
    - as: domain.markdown.token_ownership_unique
      from: assert.function
      path: /domain.markdown.token_ownership_unique
      required: true
    - as: domain.markdown.token_dependencies_resolved
      from: assert.function
      path: /domain.markdown.token_dependencies_resolved
      required: true
```



```yaml spec-test
id: LIB-DOMAIN-MD-001-019-DOMAIN-MARKDOWN-TOKENS-ALL-PRESENT
title: 'markdown projection helper functions: domain.markdown.tokens_all_present'
type: spec_lang.export
defines:
  public:
    domain.markdown.tokens_all_present:
      fn:
      - [subject, tokens]
      - std.collection.all:
        - std.collection.map:
          - fn:
            - [token]
            - call:
              - {var: domain.markdown.token_present}
              - {var: subject}
              - {var: token}
          - {var: tokens}
  private:
    markdown._text:
      fn:
      - [subject]
      - if:
        - std.type.is_string:
          - {var: subject}
        - {var: subject}
        - std.null.default_to:
          - ''
          - std.object.get:
            - {var: subject}
            - value
    markdown._context:
      fn:
      - [subject]
      - if:
        - std.type.is_dict:
          - {var: subject}
        - std.null.default_to:
          - lit: {}
          - std.object.get:
            - {var: subject}
            - context
        - lit: {}
    markdown._headings:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - headings
    markdown._links:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - links
    markdown._tokens_map:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - tokens
    markdown._token_owners:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_owners
    markdown._token_dependencies:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_dependencies
harness:
  chain:
    exports:
    - as: domain.markdown.has_heading
      from: assert.function
      path: /domain.markdown.has_heading
      required: true
    - as: domain.markdown.heading_level_exists
      from: assert.function
      path: /domain.markdown.heading_level_exists
      required: true
    - as: domain.markdown.section_order_valid
      from: assert.function
      path: /domain.markdown.section_order_valid
      required: true
    - as: domain.markdown.required_sections_present
      from: assert.function
      path: /domain.markdown.required_sections_present
      required: true
    - as: domain.markdown.link_targets_all_resolve
      from: assert.function
      path: /domain.markdown.link_targets_all_resolve
      required: true
    - as: domain.markdown.has_broken_links
      from: assert.function
      path: /domain.markdown.has_broken_links
      required: true
    - as: domain.markdown.has_yaml_spec_test_fence
      from: assert.function
      path: /domain.markdown.has_yaml_spec_test_fence
      required: true
    - as: domain.markdown.code_fence_language_exists
      from: assert.function
      path: /domain.markdown.code_fence_language_exists
      required: true
    - as: domain.markdown.token_present
      from: assert.function
      path: /domain.markdown.token_present
      required: true
    - as: domain.markdown.tokens_all_present
      from: assert.function
      path: /domain.markdown.tokens_all_present
      required: true
    - as: domain.markdown.token_ownership_unique
      from: assert.function
      path: /domain.markdown.token_ownership_unique
      required: true
    - as: domain.markdown.token_dependencies_resolved
      from: assert.function
      path: /domain.markdown.token_dependencies_resolved
      required: true
```



```yaml spec-test
id: LIB-DOMAIN-MD-001-021-DOMAIN-MARKDOWN-TOKEN-OWNERSHIP-UNIQUE
title: 'markdown projection helper functions: domain.markdown.token_ownership_unique'
type: spec_lang.export
defines:
  public:
    domain.markdown.token_ownership_unique:
      fn:
      - [subject]
      - std.collection.all:
        - std.collection.map:
          - fn:
            - [owners]
            - std.logic.eq:
              - std.collection.len:
                - {var: owners}
              - 1
          - std.object.values:
            - call:
              - {var: markdown._token_owners}
              - {var: subject}
  private:
    markdown._text:
      fn:
      - [subject]
      - if:
        - std.type.is_string:
          - {var: subject}
        - {var: subject}
        - std.null.default_to:
          - ''
          - std.object.get:
            - {var: subject}
            - value
    markdown._context:
      fn:
      - [subject]
      - if:
        - std.type.is_dict:
          - {var: subject}
        - std.null.default_to:
          - lit: {}
          - std.object.get:
            - {var: subject}
            - context
        - lit: {}
    markdown._headings:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - headings
    markdown._links:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - links
    markdown._tokens_map:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - tokens
    markdown._token_owners:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_owners
    markdown._token_dependencies:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_dependencies
harness:
  chain:
    exports:
    - as: domain.markdown.has_heading
      from: assert.function
      path: /domain.markdown.has_heading
      required: true
    - as: domain.markdown.heading_level_exists
      from: assert.function
      path: /domain.markdown.heading_level_exists
      required: true
    - as: domain.markdown.section_order_valid
      from: assert.function
      path: /domain.markdown.section_order_valid
      required: true
    - as: domain.markdown.required_sections_present
      from: assert.function
      path: /domain.markdown.required_sections_present
      required: true
    - as: domain.markdown.link_targets_all_resolve
      from: assert.function
      path: /domain.markdown.link_targets_all_resolve
      required: true
    - as: domain.markdown.has_broken_links
      from: assert.function
      path: /domain.markdown.has_broken_links
      required: true
    - as: domain.markdown.has_yaml_spec_test_fence
      from: assert.function
      path: /domain.markdown.has_yaml_spec_test_fence
      required: true
    - as: domain.markdown.code_fence_language_exists
      from: assert.function
      path: /domain.markdown.code_fence_language_exists
      required: true
    - as: domain.markdown.token_present
      from: assert.function
      path: /domain.markdown.token_present
      required: true
    - as: domain.markdown.tokens_all_present
      from: assert.function
      path: /domain.markdown.tokens_all_present
      required: true
    - as: domain.markdown.token_ownership_unique
      from: assert.function
      path: /domain.markdown.token_ownership_unique
      required: true
    - as: domain.markdown.token_dependencies_resolved
      from: assert.function
      path: /domain.markdown.token_dependencies_resolved
      required: true
```



```yaml spec-test
id: LIB-DOMAIN-MD-001-023-DOMAIN-MARKDOWN-TOKEN-DEPENDENCIES-RESOLVED
title: 'markdown projection helper functions: domain.markdown.token_dependencies_resolved'
type: spec_lang.export
defines:
  public:
    domain.markdown.token_dependencies_resolved:
      fn:
      - [subject]
      - std.collection.all:
        - std.collection.map:
          - fn:
            - [dep]
            - std.logic.eq:
              - std.object.get:
                - {var: dep}
                - resolved
              - true
          - call:
            - {var: markdown._token_dependencies}
            - {var: subject}
  private:
    markdown._text:
      fn:
      - [subject]
      - if:
        - std.type.is_string:
          - {var: subject}
        - {var: subject}
        - std.null.default_to:
          - ''
          - std.object.get:
            - {var: subject}
            - value
    markdown._context:
      fn:
      - [subject]
      - if:
        - std.type.is_dict:
          - {var: subject}
        - std.null.default_to:
          - lit: {}
          - std.object.get:
            - {var: subject}
            - context
        - lit: {}
    markdown._headings:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - headings
    markdown._links:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - links
    markdown._tokens_map:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - tokens
    markdown._token_owners:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: {}
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_owners
    markdown._token_dependencies:
      fn:
      - [subject]
      - std.null.default_to:
        - lit: []
        - std.object.get:
          - call:
            - {var: markdown._context}
            - {var: subject}
          - token_dependencies
harness:
  chain:
    exports:
    - as: domain.markdown.has_heading
      from: assert.function
      path: /domain.markdown.has_heading
      required: true
    - as: domain.markdown.heading_level_exists
      from: assert.function
      path: /domain.markdown.heading_level_exists
      required: true
    - as: domain.markdown.section_order_valid
      from: assert.function
      path: /domain.markdown.section_order_valid
      required: true
    - as: domain.markdown.required_sections_present
      from: assert.function
      path: /domain.markdown.required_sections_present
      required: true
    - as: domain.markdown.link_targets_all_resolve
      from: assert.function
      path: /domain.markdown.link_targets_all_resolve
      required: true
    - as: domain.markdown.has_broken_links
      from: assert.function
      path: /domain.markdown.has_broken_links
      required: true
    - as: domain.markdown.has_yaml_spec_test_fence
      from: assert.function
      path: /domain.markdown.has_yaml_spec_test_fence
      required: true
    - as: domain.markdown.code_fence_language_exists
      from: assert.function
      path: /domain.markdown.code_fence_language_exists
      required: true
    - as: domain.markdown.token_present
      from: assert.function
      path: /domain.markdown.token_present
      required: true
    - as: domain.markdown.tokens_all_present
      from: assert.function
      path: /domain.markdown.tokens_all_present
      required: true
    - as: domain.markdown.token_ownership_unique
      from: assert.function
      path: /domain.markdown.token_ownership_unique
      required: true
    - as: domain.markdown.token_dependencies_resolved
      from: assert.function
      path: /domain.markdown.token_dependencies_resolved
      required: true
```



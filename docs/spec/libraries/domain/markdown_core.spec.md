# Spec-Lang Markdown Domain Library

## LIB-DOMAIN-MD-001

```yaml spec-test
id: LIB-DOMAIN-MD-001
title: markdown projection helper functions
type: spec_lang.library
definitions:
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
    md.has_heading:
      fn:
      - [subject, heading]
      - call:
        - {var: domain.markdown.has_heading}
        - {var: subject}
        - {var: heading}
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
    md.heading_level_exists:
      fn:
      - [subject, level]
      - call:
        - {var: domain.markdown.heading_level_exists}
        - {var: subject}
        - {var: level}
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
    md.section_order_valid:
      fn:
      - [subject, headings]
      - call:
        - {var: domain.markdown.section_order_valid}
        - {var: subject}
        - {var: headings}
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
    md.required_sections_present:
      fn:
      - [subject, headings]
      - call:
        - {var: domain.markdown.required_sections_present}
        - {var: subject}
        - {var: headings}
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
    md.link_targets_all_resolve:
      fn:
      - [subject]
      - call:
        - {var: domain.markdown.link_targets_all_resolve}
        - {var: subject}
    domain.markdown.has_broken_links:
      fn:
      - [subject]
      - std.logic.not:
        - call:
          - {var: domain.markdown.link_targets_all_resolve}
          - {var: subject}
    md.has_broken_links:
      fn:
      - [subject]
      - call:
        - {var: domain.markdown.has_broken_links}
        - {var: subject}
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
    md.has_yaml_spec_test_fence:
      fn:
      - [subject]
      - call:
        - {var: domain.markdown.has_yaml_spec_test_fence}
        - {var: subject}
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
    md.code_fence_language_exists:
      fn:
      - [subject, language]
      - call:
        - {var: domain.markdown.code_fence_language_exists}
        - {var: subject}
        - {var: language}
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
    md.token_present:
      fn:
      - [subject, token]
      - call:
        - {var: domain.markdown.token_present}
        - {var: subject}
        - {var: token}
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
    md.tokens_all_present:
      fn:
      - [subject, tokens]
      - call:
        - {var: domain.markdown.tokens_all_present}
        - {var: subject}
        - {var: tokens}
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
    md.token_ownership_unique:
      fn:
      - [subject]
      - call:
        - {var: domain.markdown.token_ownership_unique}
        - {var: subject}
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
    md.token_dependencies_resolved:
      fn:
      - [subject]
      - call:
        - {var: domain.markdown.token_dependencies_resolved}
        - {var: subject}
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
```

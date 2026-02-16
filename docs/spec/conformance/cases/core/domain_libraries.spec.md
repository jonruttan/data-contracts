# Domain Library Conformance Cases

## SRCONF-DOMAIN-LIB-001

```yaml spec-test
id: SRCONF-DOMAIN-LIB-001
title: domain http library defines status helper
purpose: Ensures domain HTTP library exports reusable status-based assertion helper.
type: text.file
path: /docs/spec/libraries/domain/http_core.spec.md
harness:
  spec_lang:
    includes:
    - /docs/spec/libraries/domain/http_core.spec.md
    exports:
    - domain.http.auth_is_oauth
    - domain.http.body_json
    - domain.http.body_json_has_key
    - domain.http.body_json_type_is
    - domain.http.body_text
    - domain.http.has_bearer_header
    - domain.http.header_contains
    - domain.http.header_get
    - domain.http.oauth_scope_requested
    - domain.http.ok_2xx
    - domain.http.status
    - domain.http.status_is
    - domain.http.status_is_forbidden
    - domain.http.status_is_unauthorized
    - domain.http.status_in
expect:
  portable:
    status: pass
assert:
- target: text
  must:
  - evaluate:
    - std.logic.eq:
      - call:
        - {var: domain.http.status}
        - lit:
            value:
              status: 200
              headers:
                Authorization: Bearer abc
                content-type: application/json
              body_text: ok
              body_json:
                ok: true
            meta:
              auth_mode: oauth
            context:
              oauth:
                scope_requested: read:items
      - 200
    - call:
      - {var: domain.http.status_is}
      - lit:
          value:
            status: 200
          meta: {}
      - 200
    - call:
      - {var: domain.http.status_is_unauthorized}
      - lit:
          value:
            status: 401
          meta: {}
    - call:
      - {var: domain.http.status_is_forbidden}
      - lit:
          value:
            status: 403
          meta: {}
    - call:
      - {var: domain.http.ok_2xx}
      - lit:
          value:
            status: 204
          meta: {}
    - call:
      - {var: domain.http.status_in}
      - lit:
          value:
            status: 200
            headers:
              Authorization: Bearer abc
              content-type: application/json
            body_text: ok
            body_json:
              ok: true
          meta:
            auth_mode: oauth
          context:
            oauth:
              scope_requested: read:items
      - lit:
        - 200
        - 201
    - std.logic.eq:
      - call:
        - {var: domain.http.header_get}
        - lit:
            value:
              headers:
                Authorization: Bearer abc
            meta: {}
        - Authorization
      - Bearer abc
    - call:
      - {var: domain.http.header_contains}
      - lit:
          value:
            headers:
              Authorization: Bearer abc
          meta: {}
      - Authorization
      - Bearer
    - std.logic.eq:
      - call:
        - {var: domain.http.body_text}
        - lit:
            value:
              body_text: ok
            meta: {}
      - ok
    - call:
      - {var: domain.http.body_json}
      - lit:
          value:
            body_json:
              ok: true
          meta: {}
    - call:
      - {var: domain.http.body_json_type_is}
      - lit:
          value:
            body_json:
              ok: true
          meta: {}
      - object
    - call:
      - {var: domain.http.body_json_has_key}
      - lit:
          value:
            body_json:
              ok: true
          meta: {}
      - ok
    - call:
      - {var: domain.http.auth_is_oauth}
      - lit:
          value: {}
          meta:
            auth_mode: oauth
    - call:
      - {var: domain.http.has_bearer_header}
      - lit:
          value:
            headers:
              Authorization: Bearer abc
          meta: {}
    - call:
      - {var: domain.http.oauth_scope_requested}
      - lit:
          value: {}
          meta: {}
          context:
            oauth:
              scope_requested: read:items
    - std.string.contains:
      - {var: subject}
      - domain.http.status_in
    - std.string.contains:
      - {var: subject}
      - domain.http.auth_is_oauth
    - std.string.contains:
      - {var: subject}
      - 'type: spec_lang.library'
```

## SRCONF-DOMAIN-LIB-002

```yaml spec-test
id: SRCONF-DOMAIN-LIB-002
title: domain library index references all domain library files
purpose: Ensures domain index remains synchronized with all domain library spec files.
type: text.file
path: /docs/spec/libraries/domain/index.md
harness:
  spec_lang:
    includes:
    - /docs/spec/libraries/domain/make_core.spec.md
    - /docs/spec/libraries/domain/markdown_core.spec.md
    - /docs/spec/libraries/domain/python_core.spec.md
    - /docs/spec/libraries/domain/php_core.spec.md
    exports:
    - make.has_target
    - domain.markdown.code_fence_language_exists
    - domain.markdown.has_broken_links
    - domain.markdown.has_heading
    - domain.markdown.has_yaml_spec_test_fence
    - domain.markdown.heading_level_exists
    - domain.markdown.link_targets_all_resolve
    - domain.markdown.required_sections_present
    - domain.markdown.section_order_valid
    - domain.markdown.token_dependencies_resolved
    - domain.markdown.token_ownership_unique
    - domain.markdown.token_present
    - domain.markdown.tokens_all_present
    - md.code_fence_language_exists
    - md.has_broken_links
    - md.has_heading
    - md.has_yaml_spec_test_fence
    - md.heading_level_exists
    - md.link_targets_all_resolve
    - md.required_sections_present
    - md.section_order_valid
    - md.token_dependencies_resolved
    - md.token_ownership_unique
    - md.token_present
    - md.tokens_all_present
    - py.is_tuple_projection
    - php.is_assoc_projection
expect:
  portable:
    status: pass
assert:
- target: text
  must:
  - evaluate:
    - call:
      - {var: make.has_target}
      - lit:
          value: "ci-gate:\n\t@echo ok\n"
          meta: {}
      - ci-gate
    - call:
      - {var: md.has_heading}
      - lit:
          value: '# Contract


            ## Usage


            ~~~yaml spec-test

            id: SAMPLE

            type: text.file

            ~~~

            '
          meta: {}
          context:
            headings:
            - text: Contract
              level: 1
            - text: Usage
              level: 2
            heading_positions:
              Contract: 1
              Usage: 2
            links:
            - target: /docs/spec/current.md
              resolved: true
            tokens:
              DOCS_ONE: true
            token_owners:
              DOCS_ONE:
              - /docs/book/index.md
            token_dependencies:
            - token: DOCS_ONE
              depends_on: DOCS_BASE
              resolved: true
      - Contract
    - call:
      - {var: domain.markdown.has_heading}
      - lit:
          value: '# Contract


            ## Usage

            '
          meta: {}
      - Usage
    - call:
      - {var: md.heading_level_exists}
      - lit:
          value: '# Contract


            ## Usage

            '
          meta: {}
          context:
            headings:
            - text: Contract
              level: 1
            - text: Usage
              level: 2
      - 2
    - call:
      - {var: md.required_sections_present}
      - lit:
          value: '# Contract


            ## Usage

            '
          meta: {}
      - lit:
        - Contract
        - Usage
    - call:
      - {var: md.section_order_valid}
      - lit:
          value: '# Contract


            ## Usage

            '
          meta: {}
          context:
            heading_positions:
              Contract: 1
              Usage: 2
      - lit:
        - Contract
        - Usage
    - call:
      - {var: md.link_targets_all_resolve}
      - lit:
          value: '# doc

            '
          meta: {}
          context:
            links:
            - target: /docs/spec/current.md
              resolved: true
    - call:
      - {var: md.has_broken_links}
      - lit:
          value: '# doc

            '
          meta: {}
          context:
            links:
            - target: /missing
              resolved: false
    - call:
      - {var: md.has_yaml_spec_test_fence}
      - lit:
          value: '~~~yaml spec-test

            id: A

            ~~~

            '
          meta: {}
    - call:
      - {var: md.code_fence_language_exists}
      - lit:
          value: '~~~yaml spec-test

            id: A

            ~~~

            '
          meta: {}
      - yaml
    - call:
      - {var: md.token_present}
      - lit:
          value: '# docs

            '
          meta: {}
          context:
            tokens:
              DOCS_ONE: true
      - DOCS_ONE
    - call:
      - {var: md.tokens_all_present}
      - lit:
          value: '# docs

            '
          meta: {}
          context:
            tokens:
              DOCS_ONE: true
              DOCS_TWO: true
      - lit:
        - DOCS_ONE
        - DOCS_TWO
    - call:
      - {var: md.token_ownership_unique}
      - lit:
          value: '# docs

            '
          meta: {}
          context:
            token_owners:
              DOCS_ONE:
              - /docs/book/index.md
    - call:
      - {var: md.token_dependencies_resolved}
      - lit:
          value: '# docs

            '
          meta: {}
          context:
            token_dependencies:
            - token: DOCS_ONE
              depends_on: DOCS_BASE
              resolved: true
    - call:
      - {var: py.is_tuple_projection}
      - lit:
          value:
          - 1
          - 2
          meta:
            native_kind: python.tuple
    - call:
      - {var: php.is_assoc_projection}
      - lit:
          value:
            k: v
          meta:
            php_array_kind: assoc
    - std.string.contains:
      - {var: subject}
      - /docs/spec/libraries/domain/http_core.spec.md
    - std.string.contains:
      - {var: subject}
      - /docs/spec/libraries/domain/make_core.spec.md
    - std.string.contains:
      - {var: subject}
      - /docs/spec/libraries/domain/markdown_core.spec.md
    - std.string.contains:
      - {var: subject}
      - /docs/spec/libraries/domain/php_core.spec.md
    - std.string.contains:
      - {var: subject}
      - /docs/spec/libraries/domain/python_core.spec.md
```

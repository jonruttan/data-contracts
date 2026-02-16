# Domain Library Conformance Cases

## SRCONF-DOMAIN-LIB-001

```yaml spec-test
id: SRCONF-DOMAIN-LIB-001
title: domain http library defines status helper
purpose: Ensures domain HTTP library exports reusable status-based assertion helper.
type: text.file
path: /docs/spec/libraries/domain/http_core.spec.md
harness:
  chain:
    steps:
    - id: lib_http_core_spec
      class: must
      ref: /docs/spec/libraries/domain/http_core.spec.md
      exports:
        domain.http.status:
          from: library.symbol
          path: /domain.http.status
          required: true
        domain.http.status_in:
          from: library.symbol
          path: /domain.http.status_in
          required: true
        domain.http.status_is:
          from: library.symbol
          path: /domain.http.status_is
          required: true
        domain.http.status_is_unauthorized:
          from: library.symbol
          path: /domain.http.status_is_unauthorized
          required: true
        domain.http.status_is_forbidden:
          from: library.symbol
          path: /domain.http.status_is_forbidden
          required: true
        domain.http.ok_2xx:
          from: library.symbol
          path: /domain.http.ok_2xx
          required: true
        domain.http.header_get:
          from: library.symbol
          path: /domain.http.header_get
          required: true
        domain.http.header_contains:
          from: library.symbol
          path: /domain.http.header_contains
          required: true
        domain.http.body_text:
          from: library.symbol
          path: /domain.http.body_text
          required: true
        domain.http.body_json:
          from: library.symbol
          path: /domain.http.body_json
          required: true
        domain.http.body_json_type_is:
          from: library.symbol
          path: /domain.http.body_json_type_is
          required: true
        domain.http.body_json_has_key:
          from: library.symbol
          path: /domain.http.body_json_has_key
          required: true
        domain.http.auth_is_oauth:
          from: library.symbol
          path: /domain.http.auth_is_oauth
          required: true
        domain.http.has_bearer_header:
          from: library.symbol
          path: /domain.http.has_bearer_header
          required: true
        domain.http.oauth_scope_requested:
          from: library.symbol
          path: /domain.http.oauth_scope_requested
          required: true
    imports:
    - from: lib_http_core_spec
      names:
      - domain.http.status
      - domain.http.status_in
      - domain.http.status_is
      - domain.http.status_is_unauthorized
      - domain.http.status_is_forbidden
      - domain.http.ok_2xx
      - domain.http.header_get
      - domain.http.header_contains
      - domain.http.body_text
      - domain.http.body_json
      - domain.http.body_json_type_is
      - domain.http.body_json_has_key
      - domain.http.auth_is_oauth
      - domain.http.has_bearer_header
      - domain.http.oauth_scope_requested
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
  chain:
    steps:
    - id: lib_make_core_spec
      class: must
      ref: /docs/spec/libraries/domain/make_core.spec.md
      exports:
        make.has_target:
          from: library.symbol
          path: /make.has_target
          required: true
    - id: lib_markdown_core_spec
      class: must
      ref: /docs/spec/libraries/domain/markdown_core.spec.md
      exports:
        md.has_heading:
          from: library.symbol
          path: /md.has_heading
          required: true
        md.heading_level_exists:
          from: library.symbol
          path: /md.heading_level_exists
          required: true
        md.section_order_valid:
          from: library.symbol
          path: /md.section_order_valid
          required: true
        md.required_sections_present:
          from: library.symbol
          path: /md.required_sections_present
          required: true
        md.link_targets_all_resolve:
          from: library.symbol
          path: /md.link_targets_all_resolve
          required: true
        md.has_broken_links:
          from: library.symbol
          path: /md.has_broken_links
          required: true
        md.has_yaml_spec_test_fence:
          from: library.symbol
          path: /md.has_yaml_spec_test_fence
          required: true
        md.code_fence_language_exists:
          from: library.symbol
          path: /md.code_fence_language_exists
          required: true
        md.token_present:
          from: library.symbol
          path: /md.token_present
          required: true
        md.tokens_all_present:
          from: library.symbol
          path: /md.tokens_all_present
          required: true
        md.token_ownership_unique:
          from: library.symbol
          path: /md.token_ownership_unique
          required: true
        md.token_dependencies_resolved:
          from: library.symbol
          path: /md.token_dependencies_resolved
          required: true
    - id: lib_python_core_spec
      class: must
      ref: /docs/spec/libraries/domain/python_core.spec.md
      exports:
        py.is_tuple_projection:
          from: library.symbol
          path: /py.is_tuple_projection
          required: true
    - id: lib_php_core_spec
      class: must
      ref: /docs/spec/libraries/domain/php_core.spec.md
      exports:
        php.is_assoc_projection:
          from: library.symbol
          path: /php.is_assoc_projection
          required: true
    imports:
    - from: lib_make_core_spec
      names:
      - make.has_target
    - from: lib_markdown_core_spec
      names:
      - md.has_heading
      - md.heading_level_exists
      - md.section_order_valid
      - md.required_sections_present
      - md.link_targets_all_resolve
      - md.has_broken_links
      - md.has_yaml_spec_test_fence
      - md.code_fence_language_exists
      - md.token_present
      - md.tokens_all_present
      - md.token_ownership_unique
      - md.token_dependencies_resolved
    - from: lib_python_core_spec
      names:
      - py.is_tuple_projection
    - from: lib_php_core_spec
      names:
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

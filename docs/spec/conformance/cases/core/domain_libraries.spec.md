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
    imports:
    - from: lib_http_core_spec
      names:
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
      - domain.http.status_in
      - domain.http.status_is
      - domain.http.status_is_forbidden
      - domain.http.status_is_unauthorized
expect:
  portable:
    status: pass
assert:
- id: assert_1
  class: must
  checks:
  - must:
    - std.logic.eq:
      - call:
        - var: domain.http.status
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
      - var: domain.http.status_is
      - lit:
          value:
            status: 200
          meta: {}
      - 200
    - call:
      - var: domain.http.status_is_unauthorized
      - lit:
          value:
            status: 401
          meta: {}
    - call:
      - var: domain.http.status_is_forbidden
      - lit:
          value:
            status: 403
          meta: {}
    - call:
      - var: domain.http.ok_2xx
      - lit:
          value:
            status: 204
          meta: {}
    - call:
      - var: domain.http.status_in
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
        - var: domain.http.header_get
        - lit:
            value:
              headers:
                Authorization: Bearer abc
            meta: {}
        - Authorization
      - Bearer abc
    - call:
      - var: domain.http.header_contains
      - lit:
          value:
            headers:
              Authorization: Bearer abc
          meta: {}
      - Authorization
      - Bearer
    - std.logic.eq:
      - call:
        - var: domain.http.body_text
        - lit:
            value:
              body_text: ok
            meta: {}
      - ok
    - call:
      - var: domain.http.body_json
      - lit:
          value:
            body_json:
              ok: true
          meta: {}
    - call:
      - var: domain.http.body_json_type_is
      - lit:
          value:
            body_json:
              ok: true
          meta: {}
      - object
    - call:
      - var: domain.http.body_json_has_key
      - lit:
          value:
            body_json:
              ok: true
          meta: {}
      - ok
    - call:
      - var: domain.http.auth_is_oauth
      - lit:
          value: {}
          meta:
            auth_mode: oauth
    - call:
      - var: domain.http.has_bearer_header
      - lit:
          value:
            headers:
              Authorization: Bearer abc
          meta: {}
    - call:
      - var: domain.http.oauth_scope_requested
      - lit:
          value: {}
          meta: {}
          context:
            oauth:
              scope_requested: read:items
    - std.string.contains:
      - var: subject
      - domain.http.status_in
    - std.string.contains:
      - var: subject
      - domain.http.auth_is_oauth
    - std.string.contains:
      - var: subject
      - 'type: spec.export'
  target: text
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
    - id: lib_markdown_core_spec
      class: must
      ref: /docs/spec/libraries/domain/markdown_core.spec.md
    - id: lib_path_core_spec
      class: must
      ref: /docs/spec/libraries/domain/path_core.spec.md
    - id: lib_python_core_spec
      class: must
      ref: /docs/spec/libraries/domain/python_core.spec.md
    - id: lib_php_core_spec
      class: must
      ref: /docs/spec/libraries/domain/php_core.spec.md
    imports:
    - from: lib_make_core_spec
      names:
      - make.has_target
    - from: lib_markdown_core_spec
      names:
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
    - from: lib_path_core_spec
      names:
      - domain.path.normalize
      - domain.path.eq
      - domain.path.is_spec_md
      - domain.path.is_in_docs
      - domain.path.sorted
      - domain.file.is_existing_file
      - domain.file.is_existing_dir
      - domain.file.has_ext
      - domain.file.name
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
- id: assert_1
  class: must
  checks:
  - must:
    - call:
      - var: make.has_target
      - lit:
          value: "ci-gate:\n\t@echo ok\n"
          meta: {}
      - ci-gate
    - call:
      - var: py.is_tuple_projection
      - lit:
          value:
          - 1
          - 2
          meta:
            native_kind: python.tuple
    - call:
      - var: php.is_assoc_projection
      - lit:
          value:
            k: v
          meta:
            php_array_kind: assoc
    - std.logic.eq:
      - call:
        - var: domain.path.normalize
        - /docs//spec/./libraries/domain/http_core.spec.md
      - /docs/spec/libraries/domain/http_core.spec.md
    - call:
      - var: domain.path.eq
      - /docs/spec/libraries/domain/http_core.spec.md
      - /docs/spec/libraries/domain//http_core.spec.md
    - call:
      - var: domain.path.is_spec_md
      - /docs/spec/libraries/domain/http_core.spec.md
    - call:
      - var: domain.path.is_in_docs
      - /docs/spec/libraries/domain/http_core.spec.md
    - std.logic.eq:
      - call:
        - var: domain.path.sorted
        - lit:
          - /docs/b
          - /docs/a
      - lit:
        - /docs/a
        - /docs/b
    - call:
      - var: domain.file.is_existing_file
      - lit:
          path: /docs/spec/libraries/domain/http_core.spec.md
          exists: true
          type: file
    - call:
      - var: domain.file.is_existing_dir
      - lit:
          path: /docs/spec/libraries/domain
          exists: true
          type: dir
    - call:
      - var: domain.file.has_ext
      - lit:
          path: /docs/spec/libraries/domain/http_core.spec.md
      - .md
    - std.logic.eq:
      - call:
        - var: domain.file.name
        - lit:
            path: /docs/spec/libraries/domain/http_core.spec.md
      - http_core.spec.md
    - std.string.contains:
      - var: subject
      - /docs/spec/libraries/domain/http_core.spec.md
    - std.string.contains:
      - var: subject
      - /docs/spec/libraries/domain/make_core.spec.md
    - std.string.contains:
      - var: subject
      - /docs/spec/libraries/domain/markdown_core.spec.md
    - std.string.contains:
      - var: subject
      - /docs/spec/libraries/domain/path_core.spec.md
    - std.string.contains:
      - var: subject
      - /docs/spec/libraries/domain/php_core.spec.md
    - std.string.contains:
      - var: subject
      - /docs/spec/libraries/domain/python_core.spec.md
  target: text
```

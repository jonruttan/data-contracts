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
    - md.has_heading
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


            Text'
          meta: {}
      - Contract
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

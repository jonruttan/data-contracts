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
    library_paths:
    - /docs/spec/libraries/domain/http_core.spec.md
    exports:
    - http.status_in
expect:
  portable:
    status: pass
assert:
- target: text
  must:
  - evaluate:
    - call:
      - {var: http.status_in}
      - {lit: {value: {status: 200}, meta: {}}}
      - {lit: [200, 201]}
    - {contains: [{var: subject}, http.status_in]}
    - {contains: [{var: subject}, 'type: spec_lang.library']}
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
    library_paths:
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
      - {lit: {value: "ci-gate:\n\t@echo ok\n", meta: {}}}
      - ci-gate
    - call:
      - {var: md.has_heading}
      - {lit: {value: '# Contract


            Text', meta: {}}}
      - Contract
    - call:
      - {var: py.is_tuple_projection}
      - {lit: {value: [1, 2], meta: {native_kind: python.tuple}}}
    - call:
      - {var: php.is_assoc_projection}
      - {lit: {value: {k: v}, meta: {php_array_kind: assoc}}}
    - {contains: [{var: subject}, /docs/spec/libraries/domain/http_core.spec.md]}
    - {contains: [{var: subject}, /docs/spec/libraries/domain/make_core.spec.md]}
    - {contains: [{var: subject}, /docs/spec/libraries/domain/markdown_core.spec.md]}
    - {contains: [{var: subject}, /docs/spec/libraries/domain/php_core.spec.md]}
    - {contains: [{var: subject}, /docs/spec/libraries/domain/python_core.spec.md]}
```

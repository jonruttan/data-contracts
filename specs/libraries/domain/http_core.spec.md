# Spec-Lang HTTP Domain Library

## LIB-DOMAIN-HTTP-001

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-001-DOMAIN-HTTP-STATUS
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.status
    assert:
      std.object.get:
      - std.object.get:
        - {var: subject}
        - value
      - status
harness:
  exports:
  - as: domain.http.status
    from: assert.function
    path: /__export__domain.http.status
    params:
    - subject
    doc:
      summary: Contract export for `domain.http.status`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-001-DOMAIN-HTTP-STATUS` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-002-DOMAIN-HTTP-STATUS-IN
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.status_in
    assert:
      std.collection.in:
      - std.object.get:
        - std.object.get:
          - {var: subject}
          - value
        - status
      - {var: allowed}
harness:
  exports:
  - as: domain.http.status_in
    from: assert.function
    path: /__export__domain.http.status_in
    params:
    - subject
    - allowed
    doc:
      summary: Contract export for `domain.http.status_in`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      - name: allowed
        type: any
        required: true
        description: Input parameter `allowed`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
          allowed: <allowed>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-002-DOMAIN-HTTP-STATUS-IN` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-003-DOMAIN-HTTP-STATUS-IS
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.status_is
    assert:
      std.logic.eq:
      - std.object.get:
        - std.object.get:
          - {var: subject}
          - value
        - status
      - {var: expected}
harness:
  exports:
  - as: domain.http.status_is
    from: assert.function
    path: /__export__domain.http.status_is
    params:
    - subject
    - expected
    doc:
      summary: Contract export for `domain.http.status_is`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      - name: expected
        type: any
        required: true
        description: Input parameter `expected`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
          expected: <expected>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-003-DOMAIN-HTTP-STATUS-IS` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-004-DOMAIN-HTTP-STATUS-IS-UNAUTHORIZED
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.status_is_unauthorized
    assert:
      lit:
        call:
        - var: domain.http.status_is
        - var: subject
        - 401
harness:
  exports:
  - as: domain.http.status_is_unauthorized
    from: assert.function
    path: /__export__domain.http.status_is_unauthorized
    params:
    - subject
    doc:
      summary: Contract export for `domain.http.status_is_unauthorized`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-004-DOMAIN-HTTP-STATUS-IS-UNAUTHORIZED` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-005-DOMAIN-HTTP-STATUS-IS-FORBIDDEN
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.status_is_forbidden
    assert:
      lit:
        call:
        - var: domain.http.status_is
        - var: subject
        - 403
harness:
  exports:
  - as: domain.http.status_is_forbidden
    from: assert.function
    path: /__export__domain.http.status_is_forbidden
    params:
    - subject
    doc:
      summary: Contract export for `domain.http.status_is_forbidden`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-005-DOMAIN-HTTP-STATUS-IS-FORBIDDEN` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-006-DOMAIN-HTTP-OK-2XX
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.ok_2xx
    assert:
      std.logic.and:
      - std.logic.gte:
        - std.object.get:
          - std.object.get:
            - {var: subject}
            - value
          - status
        - 200
      - std.logic.lt:
        - std.object.get:
          - std.object.get:
            - {var: subject}
            - value
          - status
        - 300
harness:
  exports:
  - as: domain.http.ok_2xx
    from: assert.function
    path: /__export__domain.http.ok_2xx
    params:
    - subject
    doc:
      summary: Contract export for `domain.http.ok_2xx`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-006-DOMAIN-HTTP-OK-2XX` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-007-DOMAIN-HTTP-HEADER-GET
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.header_get
    assert:
      std.object.get:
      - std.object.get:
        - std.object.get:
          - {var: subject}
          - value
        - headers
      - {var: key}
harness:
  exports:
  - as: domain.http.header_get
    from: assert.function
    path: /__export__domain.http.header_get
    params:
    - subject
    - key
    doc:
      summary: Contract export for `domain.http.header_get`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      - name: key
        type: any
        required: true
        description: Input parameter `key`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
          key: <key>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-007-DOMAIN-HTTP-HEADER-GET` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-008-DOMAIN-HTTP-HEADER-CONTAINS
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.header_contains
    assert:
      std.string.contains:
      - std.object.get:
        - std.object.get:
          - std.object.get:
            - {var: subject}
            - value
          - headers
        - {var: key}
      - {var: token}
harness:
  exports:
  - as: domain.http.header_contains
    from: assert.function
    path: /__export__domain.http.header_contains
    params:
    - subject
    - key
    - token
    doc:
      summary: Contract export for `domain.http.header_contains`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      - name: key
        type: any
        required: true
        description: Input parameter `key`.
      - name: token
        type: any
        required: true
        description: Input parameter `token`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
          key: <key>
          token: <token>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-008-DOMAIN-HTTP-HEADER-CONTAINS` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-009-DOMAIN-HTTP-BODY-TEXT
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.body_text
    assert:
      std.object.get:
      - std.object.get:
        - {var: subject}
        - value
      - body_text
harness:
  exports:
  - as: domain.http.body_text
    from: assert.function
    path: /__export__domain.http.body_text
    params:
    - subject
    doc:
      summary: Contract export for `domain.http.body_text`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-009-DOMAIN-HTTP-BODY-TEXT` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-010-DOMAIN-HTTP-BODY-JSON
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.body_json
    assert:
      std.object.get:
      - std.object.get:
        - {var: subject}
        - value
      - body_json
harness:
  exports:
  - as: domain.http.body_json
    from: assert.function
    path: /__export__domain.http.body_json
    params:
    - subject
    doc:
      summary: Contract export for `domain.http.body_json`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-010-DOMAIN-HTTP-BODY-JSON` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-011-DOMAIN-HTTP-BODY-JSON-TYPE-IS
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.body_json_type_is
    assert:
      std.type.json_type:
      - std.object.get:
        - std.object.get:
          - {var: subject}
          - value
        - body_json
      - {var: expected_type}
harness:
  exports:
  - as: domain.http.body_json_type_is
    from: assert.function
    path: /__export__domain.http.body_json_type_is
    params:
    - subject
    - expected_type
    doc:
      summary: Contract export for `domain.http.body_json_type_is`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      - name: expected_type
        type: any
        required: true
        description: Input parameter `expected_type`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
          expected_type: <expected_type>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-011-DOMAIN-HTTP-BODY-JSON-TYPE-IS` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-012-DOMAIN-HTTP-BODY-JSON-HAS-KEY
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.body_json_has_key
    assert:
      std.object.has_key:
      - std.object.get:
        - std.object.get:
          - {var: subject}
          - value
        - body_json
      - {var: key}
harness:
  exports:
  - as: domain.http.body_json_has_key
    from: assert.function
    path: /__export__domain.http.body_json_has_key
    params:
    - subject
    - key
    doc:
      summary: Contract export for `domain.http.body_json_has_key`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      - name: key
        type: any
        required: true
        description: Input parameter `key`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
          key: <key>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-012-DOMAIN-HTTP-BODY-JSON-HAS-KEY` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-013-DOMAIN-HTTP-AUTH-IS-OAUTH
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.auth_is_oauth
    assert:
      std.logic.eq:
      - std.object.get:
        - std.object.get:
          - {var: subject}
          - meta
        - auth_mode
      - oauth
harness:
  exports:
  - as: domain.http.auth_is_oauth
    from: assert.function
    path: /__export__domain.http.auth_is_oauth
    params:
    - subject
    doc:
      summary: Contract export for `domain.http.auth_is_oauth`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-013-DOMAIN-HTTP-AUTH-IS-OAUTH` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-014-DOMAIN-HTTP-OAUTH-TOKEN-SOURCE-IS
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.oauth_token_source_is
    assert:
      std.logic.eq:
      - std.object.get:
        - std.object.get:
          - {var: subject}
          - meta
        - oauth_token_source
      - {var: expected}
harness:
  exports:
  - as: domain.http.oauth_token_source_is
    from: assert.function
    path: /__export__domain.http.oauth_token_source_is
    params:
    - subject
    - expected
    doc:
      summary: Contract export for `domain.http.oauth_token_source_is`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      - name: expected
        type: any
        required: true
        description: Input parameter `expected`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
          expected: <expected>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-014-DOMAIN-HTTP-OAUTH-TOKEN-SOURCE-IS` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-015-DOMAIN-HTTP-HAS-BEARER-HEADER
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.has_bearer_header
    assert:
      std.string.starts_with:
      - std.object.get:
        - std.object.get:
          - std.object.get:
            - {var: subject}
            - value
          - headers
        - Authorization
      - 'Bearer '
harness:
  exports:
  - as: domain.http.has_bearer_header
    from: assert.function
    path: /__export__domain.http.has_bearer_header
    params:
    - subject
    doc:
      summary: Contract export for `domain.http.has_bearer_header`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-015-DOMAIN-HTTP-HAS-BEARER-HEADER` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-015-DOMAIN-HTTP-OAUTH-SCOPE-REQUESTED
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.oauth_scope_requested
    assert:
      std.logic.neq:
      - std.object.get:
        - std.object.get:
          - std.object.get:
            - {var: subject}
            - context
          - oauth
        - scope_requested
      - null
harness:
  exports:
  - as: domain.http.oauth_scope_requested
    from: assert.function
    path: /__export__domain.http.oauth_scope_requested
    params:
    - subject
    doc:
      summary: Contract export for `domain.http.oauth_scope_requested`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-015-DOMAIN-HTTP-OAUTH-SCOPE-REQUESTED` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-016-DOMAIN-HTTP-CORS-ALLOW-ORIGIN
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.cors_allow_origin
    assert:
      std.object.get:
      - std.object.get:
        - std.object.get:
          - {var: subject}
          - value
        - cors
      - allow_origin
harness:
  exports:
  - as: domain.http.cors_allow_origin
    from: assert.function
    path: /__export__domain.http.cors_allow_origin
    params:
    - subject
    doc:
      summary: Contract export for `domain.http.cors_allow_origin`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-016-DOMAIN-HTTP-CORS-ALLOW-ORIGIN` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-017-DOMAIN-HTTP-CORS-ALLOWS-METHOD
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.cors_allows_method
    assert:
      std.collection.includes:
      - std.object.get:
        - std.object.get:
          - std.object.get:
            - {var: subject}
            - value
          - cors
        - allow_methods
      - {var: method_name}
harness:
  exports:
  - as: domain.http.cors_allows_method
    from: assert.function
    path: /__export__domain.http.cors_allows_method
    params:
    - subject
    - method_name
    doc:
      summary: Contract export for `domain.http.cors_allows_method`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      - name: method_name
        type: any
        required: true
        description: Input parameter `method_name`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
          method_name: <method_name>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-017-DOMAIN-HTTP-CORS-ALLOWS-METHOD` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-018-DOMAIN-HTTP-CORS-ALLOWS-HEADER
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.cors_allows_header
    assert:
      std.collection.includes:
      - std.object.get:
        - std.object.get:
          - std.object.get:
            - {var: subject}
            - value
          - cors
        - allow_headers
      - {var: header_name}
harness:
  exports:
  - as: domain.http.cors_allows_header
    from: assert.function
    path: /__export__domain.http.cors_allows_header
    params:
    - subject
    - header_name
    doc:
      summary: Contract export for `domain.http.cors_allows_header`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      - name: header_name
        type: any
        required: true
        description: Input parameter `header_name`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
          header_name: <header_name>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-018-DOMAIN-HTTP-CORS-ALLOWS-HEADER` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-019-DOMAIN-HTTP-CORS-CREDENTIALS-ENABLED
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.cors_credentials_enabled
    assert:
      std.logic.eq:
      - std.object.get:
        - std.object.get:
          - std.object.get:
            - {var: subject}
            - value
          - cors
        - allow_credentials
      - true
harness:
  exports:
  - as: domain.http.cors_credentials_enabled
    from: assert.function
    path: /__export__domain.http.cors_credentials_enabled
    params:
    - subject
    doc:
      summary: Contract export for `domain.http.cors_credentials_enabled`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-019-DOMAIN-HTTP-CORS-CREDENTIALS-ENABLED` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-020-DOMAIN-HTTP-CORS-MAX-AGE-GTE
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.cors_max_age_gte
    assert:
      std.logic.gte:
      - std.object.get:
        - std.object.get:
          - std.object.get:
            - {var: subject}
            - value
          - cors
        - max_age
      - {var: min_age}
harness:
  exports:
  - as: domain.http.cors_max_age_gte
    from: assert.function
    path: /__export__domain.http.cors_max_age_gte
    params:
    - subject
    - min_age
    doc:
      summary: Contract export for `domain.http.cors_max_age_gte`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: subject
        type: any
        required: true
        description: Input parameter `subject`.
      - name: min_age
        type: any
        required: true
        description: Input parameter `min_age`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          subject: <subject>
          min_age: <min_age>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-020-DOMAIN-HTTP-CORS-MAX-AGE-GTE` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-021-DOMAIN-HTTP-IS-PREFLIGHT-STEP
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.is_preflight_step
    assert:
      std.logic.eq:
      - std.object.get:
        - {var: step}
        - method
      - OPTIONS
harness:
  exports:
  - as: domain.http.is_preflight_step
    from: assert.function
    path: /__export__domain.http.is_preflight_step
    params:
    - step
    doc:
      summary: Contract export for `domain.http.is_preflight_step`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: step
        type: any
        required: true
        description: Input parameter `step`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          step: <step>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-021-DOMAIN-HTTP-IS-PREFLIGHT-STEP` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-022-DOMAIN-HTTP-STEP-BY-ID
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.step_by_id
    assert:
      std.collection.find:
      - fn:
        - [row]
        - std.logic.eq:
          - std.object.get:
            - {var: row}
            - id
          - {var: step_id}
      - {var: steps}
harness:
  exports:
  - as: domain.http.step_by_id
    from: assert.function
    path: /__export__domain.http.step_by_id
    params:
    - steps
    - step_id
    doc:
      summary: Contract export for `domain.http.step_by_id`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: steps
        type: any
        required: true
        description: Input parameter `steps`.
      - name: step_id
        type: any
        required: true
        description: Input parameter `step_id`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          steps: <steps>
          step_id: <step_id>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-022-DOMAIN-HTTP-STEP-BY-ID` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-023-DOMAIN-HTTP-STEP-STATUS-IS
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.step_status_is
    assert:
      std.logic.eq:
      - std.object.get:
        - call:
          - {var: domain.http.step_by_id}
          - {var: steps}
          - {var: step_id}
        - status
      - {var: expected}
harness:
  exports:
  - as: domain.http.step_status_is
    from: assert.function
    path: /__export__domain.http.step_status_is
    params:
    - steps
    - step_id
    - expected
    doc:
      summary: Contract export for `domain.http.step_status_is`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: steps
        type: any
        required: true
        description: Input parameter `steps`.
      - name: step_id
        type: any
        required: true
        description: Input parameter `step_id`.
      - name: expected
        type: any
        required: true
        description: Input parameter `expected`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          steps: <steps>
          step_id: <step_id>
          expected: <expected>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-023-DOMAIN-HTTP-STEP-STATUS-IS` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-HTTP-001-024-DOMAIN-HTTP-STEP-BODY-JSON-GET
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.http.step_body_json_get
    assert:
      std.object.get:
      - std.object.get:
        - call:
          - {var: domain.http.step_by_id}
          - {var: steps}
          - {var: step_id}
        - body_json
      - {var: field}
harness:
  exports:
  - as: domain.http.step_body_json_get
    from: assert.function
    path: /__export__domain.http.step_body_json_get
    params:
    - steps
    - step_id
    - field
    doc:
      summary: Contract export for `domain.http.step_body_json_get`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: steps
        type: any
        required: true
        description: Input parameter `steps`.
      - name: step_id
        type: any
        required: true
        description: Input parameter `step_id`.
      - name: field
        type: any
        required: true
        description: Input parameter `field`.
      returns:
        type: any
        description: Result payload for this symbol.
      errors:
      - code: SCHEMA_ERROR
        when: Input payload does not satisfy contract shape requirements.
        category: schema
      examples:
      - title: Basic usage
        input:
          steps: <steps>
          step_id: <step_id>
          field: <field>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
library:
  id: domain.http.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-HTTP-001-024-DOMAIN-HTTP-STEP-BODY-JSON-GET` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

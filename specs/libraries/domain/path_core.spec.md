# Spec-Lang Path/File Domain Library

## LIB-DOMAIN-PATH-001

```yaml contract-spec
id: LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__domain.path.normalize
    assert:
      ops.fs.path.normalize:
      - {var: path}
harness:
  exports:
  - as: domain.path.normalize
    from: assert.function
    path: /__export__domain.path.normalize
    params:
    - path
    required: true
    doc:
      summary: Contract export for `domain.path.normalize`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: path
        type: any
        required: true
        description: Input parameter `path`.
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
          path: <path>
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
  id: domain.path.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-PATH-001-001-DOMAIN-PATH-NORMALIZE` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-PATH-001-002-DOMAIN-PATH-EQ
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__domain.path.eq
    assert:
      std.logic.eq:
      - ops.fs.path.normalize:
        - {var: left}
      - ops.fs.path.normalize:
        - {var: right}
harness:
  exports:
  - as: domain.path.eq
    from: assert.function
    path: /__export__domain.path.eq
    params:
    - left
    - right
    required: true
    doc:
      summary: Contract export for `domain.path.eq`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: left
        type: any
        required: true
        description: Input parameter `left`.
      - name: right
        type: any
        required: true
        description: Input parameter `right`.
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
          left: <left>
          right: <right>
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
  id: domain.path.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-PATH-001-002-DOMAIN-PATH-EQ` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-PATH-001-003-DOMAIN-PATH-IS-SPEC-MD
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__domain.path.is_spec_md
    assert:
      std.string.ends_with:
      - ops.fs.path.normalize:
        - {var: path}
      - .spec.md
harness:
  exports:
  - as: domain.path.is_spec_md
    from: assert.function
    path: /__export__domain.path.is_spec_md
    params:
    - path
    required: true
    doc:
      summary: Contract export for `domain.path.is_spec_md`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: path
        type: any
        required: true
        description: Input parameter `path`.
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
          path: <path>
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
  id: domain.path.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-PATH-001-003-DOMAIN-PATH-IS-SPEC-MD` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-PATH-001-004-DOMAIN-PATH-IS-IN-DOCS
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__domain.path.is_in_docs
    assert:
      ops.fs.path.within:
      - /docs
      - ops.fs.path.normalize:
        - {var: path}
harness:
  exports:
  - as: domain.path.is_in_docs
    from: assert.function
    path: /__export__domain.path.is_in_docs
    params:
    - path
    required: true
    doc:
      summary: Contract export for `domain.path.is_in_docs`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: path
        type: any
        required: true
        description: Input parameter `path`.
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
          path: <path>
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
  id: domain.path.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-PATH-001-004-DOMAIN-PATH-IS-IN-DOCS` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-PATH-001-005-DOMAIN-PATH-SORTED
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__domain.path.sorted
    assert:
      ops.fs.path.sort:
      - {var: paths}
harness:
  exports:
  - as: domain.path.sorted
    from: assert.function
    path: /__export__domain.path.sorted
    params:
    - paths
    required: true
    doc:
      summary: Contract export for `domain.path.sorted`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: paths
        type: any
        required: true
        description: Input parameter `paths`.
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
          paths: <paths>
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
  id: domain.path.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-PATH-001-005-DOMAIN-PATH-SORTED` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-PATH-001-006-DOMAIN-FILE-IS-EXISTING-FILE
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__domain.file.is_existing_file
    assert:
      std.logic.and:
      - ops.fs.file.exists:
        - {var: meta}
      - ops.fs.file.is_file:
        - {var: meta}
harness:
  exports:
  - as: domain.file.is_existing_file
    from: assert.function
    path: /__export__domain.file.is_existing_file
    params:
    - meta
    required: true
    doc:
      summary: Contract export for `domain.file.is_existing_file`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: meta
        type: any
        required: true
        description: Input parameter `meta`.
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
          meta: <meta>
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
  id: domain.path.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-PATH-001-006-DOMAIN-FILE-IS-EXISTING-FILE` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-PATH-001-007-DOMAIN-FILE-IS-EXISTING-DIR
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__domain.file.is_existing_dir
    assert:
      std.logic.and:
      - ops.fs.file.exists:
        - {var: meta}
      - ops.fs.file.is_dir:
        - {var: meta}
harness:
  exports:
  - as: domain.file.is_existing_dir
    from: assert.function
    path: /__export__domain.file.is_existing_dir
    params:
    - meta
    required: true
    doc:
      summary: Contract export for `domain.file.is_existing_dir`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: meta
        type: any
        required: true
        description: Input parameter `meta`.
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
          meta: <meta>
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
  id: domain.path.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-PATH-001-007-DOMAIN-FILE-IS-EXISTING-DIR` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-PATH-001-008-DOMAIN-FILE-HAS-EXT
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__domain.file.has_ext
    assert:
      ops.fs.path.has_ext:
      - ops.fs.file.path:
        - {var: meta}
      - {var: ext}
harness:
  exports:
  - as: domain.file.has_ext
    from: assert.function
    path: /__export__domain.file.has_ext
    params:
    - meta
    - ext
    required: true
    doc:
      summary: Contract export for `domain.file.has_ext`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: meta
        type: any
        required: true
        description: Input parameter `meta`.
      - name: ext
        type: any
        required: true
        description: Input parameter `ext`.
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
          meta: <meta>
          ext: <ext>
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
  id: domain.path.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-PATH-001-008-DOMAIN-FILE-HAS-EXT` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

```yaml contract-spec
id: LIB-DOMAIN-PATH-001-009-DOMAIN-FILE-NAME
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__domain.file.name
    assert:
      ops.fs.file.name:
      - {var: meta}
harness:
  exports:
  - as: domain.file.name
    from: assert.function
    path: /__export__domain.file.name
    params:
    - meta
    required: true
    doc:
      summary: Contract export for `domain.file.name`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: meta
        type: any
        required: true
        description: Input parameter `meta`.
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
          meta: <meta>
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
  id: domain.path.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-PATH-001-009-DOMAIN-FILE-NAME` for `contract.export`.
  description: Auto-generated root doc metadata stub. Replace with authored reference text.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

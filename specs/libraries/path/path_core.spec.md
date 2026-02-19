# Spec-Lang Path Core Library

## LIB-PATH-001

```yaml contract-spec
id: LIB-PATH-001-001-PATH-NORMALIZE-SLASHES
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__path.normalize_slashes
    assert:
      std.string.replace:
      - {var: path}
      - \
      - /
  - id: __export__path.trim_dot
    assert:
      std.string.replace:
      - {var: path}
      - ./
      - ''
  - id: __export__path.dirname
    assert:
      lit:
        let:
        - lit:
          - - segs
            - call:
              - var: path.segments
              - var: path
        - if:
          - std.logic.lte:
            - std.collection.len:
              - var: segs
            - 1
          - ''
          - std.string.join:
            - std.collection.slice:
              - 0
              - std.math.sub:
                - std.collection.len:
                  - var: segs
                - 1
              - var: segs
            - /
  - id: __export__path.has_extension
    assert:
      std.logic.eq:
      - call:
        - {var: path.extension}
        - {var: path}
      - {var: ext}
  - id: __export__path.is_under
    assert:
      std.string.starts_with:
      - call:
        - {var: path.normalize_slashes}
        - {var: path}
      - call:
        - {var: path.normalize_slashes}
        - {var: prefix}
  - id: __export__path.matches
    assert:
      std.string.regex_match:
      - call:
        - {var: path.normalize_slashes}
        - {var: path}
      - {var: pattern}
harness:
  exports:
  - as: path.normalize_slashes
    from: assert.function
    path: /__export__path.normalize_slashes
    params:
    - path
    doc:
      summary: Contract export for `path.normalize_slashes`.
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
  - as: path.trim_dot
    from: assert.function
    path: /__export__path.trim_dot
    params:
    - path
    doc:
      summary: Contract export for `path.trim_dot`.
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
  - as: path.dirname
    from: assert.function
    path: /__export__path.dirname
    params:
    - path
    doc:
      summary: Contract export for `path.dirname`.
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
  - as: path.has_extension
    from: assert.function
    path: /__export__path.has_extension
    params:
    - path
    - ext
    doc:
      summary: Contract export for `path.has_extension`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: path
        type: any
        required: true
        description: Input parameter `path`.
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
          path: <path>
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
  - as: path.is_under
    from: assert.function
    path: /__export__path.is_under
    params:
    - path
    - prefix
    doc:
      summary: Contract export for `path.is_under`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: path
        type: any
        required: true
        description: Input parameter `path`.
      - name: prefix
        type: any
        required: true
        description: Input parameter `prefix`.
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
          prefix: <prefix>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
  - as: path.matches
    from: assert.function
    path: /__export__path.matches
    params:
    - path
    - pattern
    doc:
      summary: Contract export for `path.matches`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: path
        type: any
        required: true
        description: Input parameter `path`.
      - name: pattern
        type: any
        required: true
        description: Input parameter `pattern`.
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
          pattern: <pattern>
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
  id: path.path.core
  module: path
  stability: alpha
  owner: spec_runner
  tags:
  - path
```

```yaml contract-spec
id: LIB-PATH-001-002-PATH-SEGMENTS
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__path.segments
    assert:
      std.string.split:
      - call:
        - {var: path.normalize_slashes}
        - {var: path}
      - /
  - id: __export__path.trim_dot
    assert:
      std.string.replace:
      - {var: path}
      - ./
      - ''
  - id: __export__path.dirname
    assert:
      lit:
        let:
        - lit:
          - - segs
            - call:
              - var: path.segments
              - var: path
        - if:
          - std.logic.lte:
            - std.collection.len:
              - var: segs
            - 1
          - ''
          - std.string.join:
            - std.collection.slice:
              - 0
              - std.math.sub:
                - std.collection.len:
                  - var: segs
                - 1
              - var: segs
            - /
  - id: __export__path.has_extension
    assert:
      std.logic.eq:
      - call:
        - {var: path.extension}
        - {var: path}
      - {var: ext}
  - id: __export__path.is_under
    assert:
      std.string.starts_with:
      - call:
        - {var: path.normalize_slashes}
        - {var: path}
      - call:
        - {var: path.normalize_slashes}
        - {var: prefix}
  - id: __export__path.matches
    assert:
      std.string.regex_match:
      - call:
        - {var: path.normalize_slashes}
        - {var: path}
      - {var: pattern}
harness:
  exports:
  - as: path.segments
    from: assert.function
    path: /__export__path.segments
    params:
    - path
    doc:
      summary: Contract export for `path.segments`.
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
  - as: path.trim_dot
    from: assert.function
    path: /__export__path.trim_dot
    params:
    - path
    doc:
      summary: Contract export for `path.trim_dot`.
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
  - as: path.dirname
    from: assert.function
    path: /__export__path.dirname
    params:
    - path
    doc:
      summary: Contract export for `path.dirname`.
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
  - as: path.has_extension
    from: assert.function
    path: /__export__path.has_extension
    params:
    - path
    - ext
    doc:
      summary: Contract export for `path.has_extension`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: path
        type: any
        required: true
        description: Input parameter `path`.
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
          path: <path>
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
  - as: path.is_under
    from: assert.function
    path: /__export__path.is_under
    params:
    - path
    - prefix
    doc:
      summary: Contract export for `path.is_under`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: path
        type: any
        required: true
        description: Input parameter `path`.
      - name: prefix
        type: any
        required: true
        description: Input parameter `prefix`.
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
          prefix: <prefix>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
  - as: path.matches
    from: assert.function
    path: /__export__path.matches
    params:
    - path
    - pattern
    doc:
      summary: Contract export for `path.matches`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: path
        type: any
        required: true
        description: Input parameter `path`.
      - name: pattern
        type: any
        required: true
        description: Input parameter `pattern`.
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
          pattern: <pattern>
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
  id: path.path.core
  module: path
  stability: alpha
  owner: spec_runner
  tags:
  - path
```

```yaml contract-spec
id: LIB-PATH-001-003-PATH-BASENAME
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__path.basename
    assert:
      lit:
        let:
        - lit:
          - - segs
            - call:
              - var: path.segments
              - var: path
        - if:
          - std.collection.is_empty:
            - var: segs
          - ''
          - std.object.get:
            - var: segs
            - std.math.sub:
              - std.collection.len:
                - var: segs
              - 1
  - id: __export__path.trim_dot
    assert:
      std.string.replace:
      - {var: path}
      - ./
      - ''
  - id: __export__path.dirname
    assert:
      lit:
        let:
        - lit:
          - - segs
            - call:
              - var: path.segments
              - var: path
        - if:
          - std.logic.lte:
            - std.collection.len:
              - var: segs
            - 1
          - ''
          - std.string.join:
            - std.collection.slice:
              - 0
              - std.math.sub:
                - std.collection.len:
                  - var: segs
                - 1
              - var: segs
            - /
  - id: __export__path.has_extension
    assert:
      std.logic.eq:
      - call:
        - {var: path.extension}
        - {var: path}
      - {var: ext}
  - id: __export__path.is_under
    assert:
      std.string.starts_with:
      - call:
        - {var: path.normalize_slashes}
        - {var: path}
      - call:
        - {var: path.normalize_slashes}
        - {var: prefix}
  - id: __export__path.matches
    assert:
      std.string.regex_match:
      - call:
        - {var: path.normalize_slashes}
        - {var: path}
      - {var: pattern}
harness:
  exports:
  - as: path.basename
    from: assert.function
    path: /__export__path.basename
    params:
    - path
    doc:
      summary: Contract export for `path.basename`.
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
  - as: path.trim_dot
    from: assert.function
    path: /__export__path.trim_dot
    params:
    - path
    doc:
      summary: Contract export for `path.trim_dot`.
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
  - as: path.dirname
    from: assert.function
    path: /__export__path.dirname
    params:
    - path
    doc:
      summary: Contract export for `path.dirname`.
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
  - as: path.has_extension
    from: assert.function
    path: /__export__path.has_extension
    params:
    - path
    - ext
    doc:
      summary: Contract export for `path.has_extension`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: path
        type: any
        required: true
        description: Input parameter `path`.
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
          path: <path>
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
  - as: path.is_under
    from: assert.function
    path: /__export__path.is_under
    params:
    - path
    - prefix
    doc:
      summary: Contract export for `path.is_under`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: path
        type: any
        required: true
        description: Input parameter `path`.
      - name: prefix
        type: any
        required: true
        description: Input parameter `prefix`.
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
          prefix: <prefix>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
  - as: path.matches
    from: assert.function
    path: /__export__path.matches
    params:
    - path
    - pattern
    doc:
      summary: Contract export for `path.matches`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: path
        type: any
        required: true
        description: Input parameter `path`.
      - name: pattern
        type: any
        required: true
        description: Input parameter `pattern`.
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
          pattern: <pattern>
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
  id: path.path.core
  module: path
  stability: alpha
  owner: spec_runner
  tags:
  - path
```

```yaml contract-spec
id: LIB-PATH-001-004-PATH-EXTENSION
type: contract.export
contract:
  defaults:
    class: MUST
  steps:
  - id: __export__path.extension
    assert:
      lit:
        let:
        - lit:
          - - base
            - call:
              - var: path.basename
              - var: path
        - let:
          - lit:
            - - parts
              - split:
                - var: base
                - .
          - if:
            - std.logic.lte:
              - std.collection.len:
                - var: parts
              - 1
            - ''
            - std.object.get:
              - var: parts
              - std.math.sub:
                - std.collection.len:
                  - var: parts
                - 1
  - id: __export__path.trim_dot
    assert:
      std.string.replace:
      - {var: path}
      - ./
      - ''
  - id: __export__path.dirname
    assert:
      lit:
        let:
        - lit:
          - - segs
            - call:
              - var: path.segments
              - var: path
        - if:
          - std.logic.lte:
            - std.collection.len:
              - var: segs
            - 1
          - ''
          - std.string.join:
            - std.collection.slice:
              - 0
              - std.math.sub:
                - std.collection.len:
                  - var: segs
                - 1
              - var: segs
            - /
  - id: __export__path.has_extension
    assert:
      std.logic.eq:
      - call:
        - {var: path.extension}
        - {var: path}
      - {var: ext}
  - id: __export__path.is_under
    assert:
      std.string.starts_with:
      - call:
        - {var: path.normalize_slashes}
        - {var: path}
      - call:
        - {var: path.normalize_slashes}
        - {var: prefix}
  - id: __export__path.matches
    assert:
      std.string.regex_match:
      - call:
        - {var: path.normalize_slashes}
        - {var: path}
      - {var: pattern}
harness:
  exports:
  - as: path.extension
    from: assert.function
    path: /__export__path.extension
    params:
    - path
    doc:
      summary: Contract export for `path.extension`.
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
  - as: path.trim_dot
    from: assert.function
    path: /__export__path.trim_dot
    params:
    - path
    doc:
      summary: Contract export for `path.trim_dot`.
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
  - as: path.dirname
    from: assert.function
    path: /__export__path.dirname
    params:
    - path
    doc:
      summary: Contract export for `path.dirname`.
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
  - as: path.has_extension
    from: assert.function
    path: /__export__path.has_extension
    params:
    - path
    - ext
    doc:
      summary: Contract export for `path.has_extension`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: path
        type: any
        required: true
        description: Input parameter `path`.
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
          path: <path>
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
  - as: path.is_under
    from: assert.function
    path: /__export__path.is_under
    params:
    - path
    - prefix
    doc:
      summary: Contract export for `path.is_under`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: path
        type: any
        required: true
        description: Input parameter `path`.
      - name: prefix
        type: any
        required: true
        description: Input parameter `prefix`.
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
          prefix: <prefix>
        expected: <result>
        notes: Replace with a concrete scenario.
      portability:
        python: true
        php: true
        rust: true
        notes: Confirm per-runtime behavior and caveats.
      see_also: []
      since: v1
  - as: path.matches
    from: assert.function
    path: /__export__path.matches
    params:
    - path
    - pattern
    doc:
      summary: Contract export for `path.matches`.
      description: Auto-generated metadata stub. Replace with authored reference text.
      params:
      - name: path
        type: any
        required: true
        description: Input parameter `path`.
      - name: pattern
        type: any
        required: true
        description: Input parameter `pattern`.
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
          pattern: <pattern>
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
  id: path.path.core
  module: path
  stability: alpha
  owner: spec_runner
  tags:
  - path
```

```yaml contract-spec
id: LIB-PATH-001-900-PATH-SMOKE
type: contract.check
harness:
  check:
    profile: text.file
    config: {}
  use:
  - ref: '#LIB-PATH-001-001-PATH-NORMALIZE-SLASHES'
    as: lib_path_normalize
    symbols:
    - path.normalize_slashes
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    'on': text
    assert:
      std.logic.eq:
      - call:
        - {var: path.normalize_slashes}
        - a\\b\\c.txt
      - a/b/c.txt
```

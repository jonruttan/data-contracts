# Spec-Lang Library Contract Conformance Cases

## SRCONF-LIB-CONTRACT-001

```yaml contract-spec
id: SRCONF-LIB-CONTRACT-001
title: policy library uses producer harness exports
purpose: Ensures policy library authoring uses producer-owned harness.exports with assert.function
  source mappings.
type: contract.check
expect:
  portable:
    status: pass
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.string.contains:
    - {var: subject}
    - 'type: spec.export'
  - std.string.contains:
    - {var: subject}
    - 'harness:'
  - std.string.contains:
    - {var: subject}
    - 'exports:'
  - std.string.contains:
    - {var: subject}
    - 'from: assert.function'
  - std.logic.not:
    - std.string.contains:
      - {var: subject}
      - 'defines:'
  target: text
harness:
  check:
    profile: text.file
    config:
      path: /docs/spec/libraries/policy/policy_core.spec.md
```

## SRCONF-LIB-CONTRACT-002

```yaml contract-spec
id: SRCONF-LIB-CONTRACT-002
title: path library uses producer harness exports
purpose: Ensures path library authoring uses producer-owned harness.exports with assert.function
  source mappings.
type: contract.check
expect:
  portable:
    status: pass
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.string.contains:
    - {var: subject}
    - 'type: spec.export'
  - std.string.contains:
    - {var: subject}
    - 'harness:'
  - std.string.contains:
    - {var: subject}
    - 'exports:'
  - std.string.contains:
    - {var: subject}
    - 'from: assert.function'
  - std.logic.not:
    - std.string.contains:
      - {var: subject}
      - 'defines:'
  target: text
harness:
  check:
    profile: text.file
    config:
      path: /docs/spec/libraries/path/path_core.spec.md
```

## SRCONF-LIB-CONTRACT-003

```yaml contract-spec
id: SRCONF-LIB-CONTRACT-003
title: policy library index tracks canonical files
purpose: Ensures generated policy library index includes canonical file references.
type: contract.check
expect:
  portable:
    status: pass
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.string.contains:
    - {var: subject}
    - /docs/spec/libraries/policy/policy_core.spec.md
  - std.string.contains:
    - {var: subject}
    - /docs/spec/libraries/policy/policy_metrics.spec.md
  target: text
harness:
  check:
    profile: text.file
    config:
      path: /docs/spec/libraries/policy/index.md
```

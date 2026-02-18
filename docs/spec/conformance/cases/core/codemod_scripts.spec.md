# Codemod Script Conformance Cases

These fixtures verify key codemod scripts through executable `.spec.md` cases.

## SRCONF-CODEMOD-001

```yaml contract-spec
id: SRCONF-CODEMOD-001
title: chain export codemod rewrites legacy export key to from
purpose: Verifies convert_chain_export_from_key check fails on legacy input and write
  mode rewrites to canonical from key.
type: cli.run
requires:
  capabilities:
  - cli.run
  when_missing: skip
expect:
  portable:
    status: pass
    category: null
  impl:
    php:
      status: skip
      category: null
argv:
- chain_export
exit_code: 0
harness:
  entrypoint: spec_runner.conformance_fixtures:codemod_smoke
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.string.contains:
    - var: subject
    - ok_chain_export
  target: stdout
```

## SRCONF-CODEMOD-002

```yaml contract-spec
id: SRCONF-CODEMOD-002
title: chain ref codemod rewrites mapping refs to scalar form
purpose: Verifies convert_chain_ref_format rewrites legacy mapping refs and passes
  check after write.
type: cli.run
requires:
  capabilities:
  - cli.run
  when_missing: skip
expect:
  portable:
    status: pass
    category: null
  impl:
    php:
      status: skip
      category: null
argv:
- chain_ref
exit_code: 0
harness:
  entrypoint: spec_runner.conformance_fixtures:codemod_smoke
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.string.contains:
    - var: subject
    - ok_chain_ref
  target: stdout
```

## SRCONF-CODEMOD-003

```yaml contract-spec
id: SRCONF-CODEMOD-003
title: definitions codemod rewrites to defines and passes check
purpose: Verifies convert_definitions_to_defines rewrites legacy library key names
  and check mode passes after rewrite.
type: cli.run
requires:
  capabilities:
  - cli.run
  when_missing: skip
expect:
  portable:
    status: pass
    category: null
  impl:
    php:
      status: skip
      category: null
argv:
- defines
exit_code: 0
harness:
  entrypoint: spec_runner.conformance_fixtures:codemod_smoke
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.string.contains:
    - var: subject
    - ok_defines
  target: stdout
```

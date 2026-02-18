# Spec-Lang Repo Domain Library

## LIB-DOMAIN-REPO-001

```yaml contract-spec
id: LIB-DOMAIN-REPO-001-001-DOMAIN-REPO-WALK-MATCHING
type: contract.export
harness:
  exports:
  - as: domain.repo.walk_matching
    from: assert.function
    path: /__export__domain.repo.walk_matching
    params:
    - root
    - pattern
    required: true
contract:
- id: __export__domain.repo.walk_matching
  class: MUST
  asserts:
  - ops.fs.walk:
    - {var: root}
    - lit:
        pattern:
          var: pattern
        include_dirs: false
        relative: true
```

# Governance Cases

## SRGOV-DOCS-CANON-001

```yaml contract-spec
id: SRGOV-DOCS-CANON-001
title: docs/spec index links all canonical spec entrypoints
purpose: Ensures /docs/spec/index.md links every canonical spec subtree and current snapshot.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.spec_index_reachability
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          std.logic.eq:
          - {var: subject}
          - 0
  target: violation_count
```

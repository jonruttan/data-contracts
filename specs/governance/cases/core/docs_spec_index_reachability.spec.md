# Governance Cases

## SRGOV-DOCS-CANON-001

```yaml contract-spec
id: SRGOV-DOCS-CANON-001
title: specs index links all canonical spec entrypoints
purpose: Ensures /specs/index.md links every canonical spec subtree and current snapshot.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.spec_index_reachability
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    'on': violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
```

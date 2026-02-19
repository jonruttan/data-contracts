# Governance Cases

## SRGOV-DOCS-CANON-002

```yaml contract-spec
id: SRGOV-DOCS-CANON-002
title: governance check family map covers all registered checks
purpose: Ensures each governance check id is mapped to a canonical check family prefix.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.governance_check_family_map_complete
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
    imports:
      subject:
        from: artifact
        key: violation_count
```

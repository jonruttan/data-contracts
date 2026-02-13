# Governance Cases

## SRGOV-CONF-PORT-001

```yaml spec-test
id: SRGOV-CONF-PORT-001
title: conformance cases keep runner logic under harness
purpose: Ensures portable conformance fixtures do not place runner/setup keys at top level.
type: governance.check
check: conformance.no_runner_logic_outside_harness
harness:
  root: .
assert:
  - target: text
    must:
      - contain: ["PASS: conformance.no_runner_logic_outside_harness"]
```

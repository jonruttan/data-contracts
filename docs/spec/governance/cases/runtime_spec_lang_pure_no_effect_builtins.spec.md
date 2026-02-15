# Governance Cases

## SRGOV-RUNTIME-SPECLANG-PURE-001

```yaml spec-test
id: SRGOV-RUNTIME-SPECLANG-PURE-001
title: spec-lang evaluators avoid side-effectful builtins
purpose: Enforces pure evaluation semantics by forbidding side-effectful probes in spec-lang implementations.
type: governance.check
check: runtime.spec_lang_pure_no_effect_builtins
harness:
  root: .
  spec_lang_purity:
    files:
      - spec_runner/spec_lang.py
      - scripts/php/spec_runner.php
      - scripts/php/conformance_runner.php
    forbidden_tokens:
      - "path_exists"
assert:
  - target: text
    must:
      - contain: ["PASS: runtime.spec_lang_pure_no_effect_builtins"]
```

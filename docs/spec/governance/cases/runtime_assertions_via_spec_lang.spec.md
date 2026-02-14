# Governance Cases

## SRGOV-RUNTIME-ASSERT-001

```yaml spec-test
id: SRGOV-RUNTIME-ASSERT-001
title: runtime assertion paths compile and evaluate through spec-lang
purpose: Enforces that runner assertion semantics route through spec-lang expression evaluation and avoid direct ad-hoc contain or regex execution paths.
type: governance.check
check: runtime.assertions_via_spec_lang
harness:
  root: .
  assert_engine:
    files:
      - path: scripts/php/conformance_runner.php
        required_tokens:
          - "compileLeafExpr("
          - "assertLeafPredicate("
          - "specLangEvalPredicate("
        forbidden_tokens:
          - "strpos($subject, $v)"
          - "preg_match('/' . str_replace('/', '\\/', $v) . '/u', $subject)"
      - path: scripts/php/spec_runner.php
        required_tokens:
          - "compileLeafExpr("
          - "assertLeafPredicate("
          - "specLangEvalPredicate("
        forbidden_tokens:
          - "strpos($subject, $v)"
          - "preg_match('/' . str_replace('/', '\\/', $v) . '/u', $subject)"
      - path: scripts/run_governance_specs.py
        required_tokens:
          - "eval_predicate("
        forbidden_tokens:
          - "assert_text_op("
      - path: spec_runner/assertions.py
        required_tokens:
          - "evaluate_internal_assert_tree("
          - "eval_predicate("
        forbidden_tokens:
          - "def assert_text_op("
      - path: spec_runner/harnesses/text_file.py
        required_tokens:
          - "evaluate_internal_assert_tree("
        forbidden_tokens:
          - "contain assertion failed"
      - path: spec_runner/harnesses/cli_run.py
        required_tokens:
          - "evaluate_internal_assert_tree("
        forbidden_tokens:
          - "contain assertion failed"
      - path: spec_runner/harnesses/api_http.py
        required_tokens:
          - "evaluate_internal_assert_tree("
        forbidden_tokens:
          - "contain assertion failed"
assert:
  - target: text
    must:
      - contain: ["PASS: runtime.assertions_via_spec_lang"]
```

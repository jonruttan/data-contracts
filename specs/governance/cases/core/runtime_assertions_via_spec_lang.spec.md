# Governance Cases

## SRGOV-RUNTIME-ASSERT-001

```yaml contract-spec
id: SRGOV-RUNTIME-ASSERT-001
title: runtime assertion paths compile and evaluate through spec-lang
purpose: Enforces that runner assertion semantics route through spec-lang expression evaluation
  and avoid direct ad-hoc contain or regex execution paths.
type: contract.check
harness:
  root: .
  assert_engine:
    files:
    - path: /runners/php/conformance_runner.php
      required_tokens:
      - compileAssertionLeafExpr(
      - assertLeafPredicate(
      - specLangEvalPredicate(
      forbidden_tokens:
      - strpos($subject, $v)
      - preg_match('/' . str_replace('/', '\/', $v) . '/u', $subject)
    - path: /runners/php/spec_runner.php
      required_tokens:
      - compileAssertionLeafExpr(
      - assertLeafPredicate(
      - specLangEvalPredicate(
      forbidden_tokens:
      - strpos($subject, $v)
      - preg_match('/' . str_replace('/', '\/', $v) . '/u', $subject)
    - path: /spec_runner/governance_runtime.py
      required_tokens:
      - eval_predicate(
      forbidden_tokens:
      - assert_text_op(
    - path: /spec_runner/assertions.py
      required_tokens:
      - evaluate_internal_assert_tree(
      - eval_predicate(
      forbidden_tokens:
      - def assert_text_op(
    - path: /spec_runner/harnesses/text_file.py
      required_tokens:
      - run_assertions_with_context(
      forbidden_tokens:
      - contain assertion failed
    - path: /spec_runner/harnesses/cli_run.py
      required_tokens:
      - run_assertions_with_context(
      forbidden_tokens:
      - contain assertion failed
    - path: /spec_runner/harnesses/api_http.py
      required_tokens:
      - run_assertions_with_context(
      forbidden_tokens:
      - contain assertion failed
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /specs/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: runtime.assertions_via_spec_lang
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - passed
    - true
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - check_id
    - runtime.assertions_via_spec_lang
  target: summary_json
```

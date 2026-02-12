---
id: SR-PORT-001
title: Portable Runner Contract and Cross-Language Conformance
priority: P1
---

# Portable Runner Contract and Cross-Language Conformance

## Problem

`spec_runner` is currently implemented in Python, but the project goal is to
port the runner to other languages (first target: PHP + PHPUnit/Laravel test
harnesses). Without a language-agnostic contract and shared conformance
fixtures, ports can drift in behavior even when they appear schema-compatible.

## Proposal

`spec_runner` SHOULD define a portable runner contract that is independent of
Python implementation details. The contract MUST specify:

- Markdown fenced-block discovery rules for `yaml spec-test`.
- YAML payload shapes and validation behavior.
- Assertion semantics for `must` / `can` / `cannot`, including inherited
  `target`.
- Error classes/messages at the contract level (schema vs assertion failure).
- Harness invocation contract (inputs and expected outputs).

The project SHOULD provide shared conformance fixtures and expected outcomes
that can be executed by multiple implementations (Python and PHP).

## Slices

Implement in small slices:

1. Portable contract doc:
   extract a language-neutral contract from current schema behavior.
2. Conformance fixtures:
   add canonical pass/fail fixtures for parser, assertion semantics, and error
   cases.
3. Python conformance reporter:
   add machine-readable output by case id/status/error to serve as reference.
4. PHP parser + assertion engine:
   implement contract-compatible parsing and assertion evaluation in PHP.
5. PHP harness dispatch + PHPUnit integration:
   support equivalent harness behavior and run fixtures in Laravel test flow.
6. Cross-language parity gate:
   compare Python and PHP conformance results by case id in CI.

## Examples

- Fixture case: `assert` with `target: stderr` + `cannot` around `contain`.
  Expected behavior must match exactly in Python and PHP runs.
- Fixture case: leaf assertion containing `target` must fail with a schema
  error in both implementations.

## Compatibility

No immediate end-user behavior change. This codifies current behavior and adds
a path for validating compatible alternative implementations.

## Test Plan

- Add conformance fixtures under `tools/spec_runner/fixtures/conformance/`.
- Add Python tests that execute all conformance fixtures and emit normalized
  results.
- Add a parity test plan for PHP implementation to compare against Python
  fixture outcomes.

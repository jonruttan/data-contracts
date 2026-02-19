# Spec Case Templates Reference

```yaml doc-meta
doc_id: DOC-REF-945
title: Spec Case Templates Reference
status: active
audience: author
owns_tokens:
- spec_case_templates_reference
requires_tokens:
- generated_reference_gateway
commands:
- run: PYTHONPATH=runners/python .venv/bin/python -m spec_runner.spec_lang_commands generate-spec-case-templates --check
  purpose: Verify generated spec case templates reference content is in sync.
examples:
- id: EX-REF-TEMPLATE-001
  runnable: false
  opt_out_reason: Generated reference page intentionally contains non-runnable template examples.
sections_required:
- '## Generated Spec Case Templates'
- '## Canonical Full Templates'
```

Generated canonical full templates for `contract.check`, `contract.job`, and
`contract.export` authoring.

<!-- GENERATED:START spec_case_templates_reference -->

## Generated Spec Case Templates

- version: `1`
- generated_at: `2026-02-19T03:56:43+00:00`

## Canonical Full Templates

### contract.check

```yaml contract-spec
id: EX-TEMPLATE-CHECK-001
title: canonical full contract.check template
purpose: Replace harness profile/config and assertions for your surface.
type: contract.check
doc:
  summary: Canonical full contract.check template.
  description: Author-facing baseline shape for check cases.
  audience: author
  since: v1
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.make_commands_sync
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - violation_count
  - from: artifact
    names:
    - summary_json
  steps:
  - id: assert_violation_count_zero
    assert:
      std.logic.eq:
      - {var: violation_count}
      - 0
  - id: assert_summary_shape
    assert:
    - std.logic.eq:
      - std.object.get:
        - {var: summary_json}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: summary_json}
        - check_id
      - docs.make_commands_sync
```

### contract.job

```yaml contract-spec
id: EX-TEMPLATE-JOB-001
title: canonical full contract.job template
type: contract.job
doc:
  summary: Canonical full contract.job template.
  description: Author-facing baseline shape for job-dispatch cases.
  audience: author
  since: v1
harness:
  spec_lang:
    capabilities:
    - ops.job
  jobs:
    main:
      helper: helper.docs.generate_all
      mode: custom
      inputs: {}
    on_fail:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/EX-TEMPLATE-JOB-001.fail.json
        format: json
        report_name: EX-TEMPLATE-JOB-001.fail
    on_complete:
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/EX-TEMPLATE-JOB-001.complete.json
        format: json
        report_name: EX-TEMPLATE-JOB-001.complete
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - summary_json
  steps:
  - id: dispatch_main
    assert:
    - ops.job.dispatch:
      - main
    - std.logic.eq:
      - std.object.get:
        - {var: summary_json}
        - ok
      - true
when:
  fail:
  - ops.job.dispatch:
    - on_fail
  complete:
  - ops.job.dispatch:
    - on_complete
```

### contract.export

```yaml contract-spec
id: EX-TEMPLATE-EXPORT-001
title: canonical full contract.export template
type: contract.export
domain: example
doc:
  summary: Canonical full contract.export template.
  description: Author-facing baseline shape for exported assertion functions.
  audience: author
  since: v1
library:
  id: example.core
  module: example
  stability: alpha
  owner: spec_runner
harness:
  exports:
  - as: example.symbol
    from: assert.function
    path: /assert_symbol
    params:
    - subject
    doc:
      summary: One-sentence symbol summary.
      description: Concise symbol description and intended usage.
      params:
      - name: subject
        type: any
        required: true
        description: Input under evaluation.
      returns:
        type: bool
        description: True when assertion passes.
      errors:
      - code: ASSERT_SYMBOL_ERROR
        when: Evaluation fails or payload is malformed.
        category: assertion
      examples:
      - title: subject contains required token
        input: '{"subject": "hello"}'
        expected: true
      portability:
        python: true
        php: true
        rust: true
      since: v1
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - subject
  steps:
  - id: assert_symbol
    assert:
      std.string.contains:
      - {var: subject}
      - hello
```

## Notes

- These are canonical authoring templates for v1 shape.
- Use explicit `contract.imports` and `steps[].assert`.
- Keep Rust lane examples canonical in active docs.
<!-- GENERATED:END spec_case_templates_reference -->

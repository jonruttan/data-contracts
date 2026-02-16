# Docs Generate Surfaces

## SRDOCGEN-001

```yaml spec-test
id: SRDOCGEN-001
type: docs.generate
title: reference index surface generation
harness:
  docs_generate:
    surface_id: reference_book
    mode: write
    output_mode: full_file
    template_path: /docs/book/templates/passthrough_text.md
    output_path: /docs/book/reference_index.md
    data_sources:
    - id: content
      source_type: generated_artifact
      path: /docs/book/reference_index.md
assert:
- target: context_json
  must:
  - evaluate:
    - std.logic.eq:
      - true
      - true
```

## SRDOCGEN-002

```yaml spec-test
id: SRDOCGEN-002
type: docs.generate
title: reference coverage surface generation
harness:
  docs_generate:
    surface_id: reference_book
    mode: write
    output_mode: full_file
    template_path: /docs/book/templates/passthrough_text.md
    output_path: /docs/book/reference_coverage.md
    data_sources:
    - id: content
      source_type: generated_artifact
      path: /docs/book/reference_coverage.md
assert:
- target: context_json
  must:
  - evaluate:
    - std.logic.eq:
      - true
      - true
```

## SRDOCGEN-003

```yaml spec-test
id: SRDOCGEN-003
type: docs.generate
title: docs graph surface generation
harness:
  docs_generate:
    surface_id: docs_graph
    mode: write
    output_mode: full_file
    template_path: /docs/book/templates/passthrough_text.md
    output_path: /docs/book/docs_graph.json
    data_sources:
    - id: content
      source_type: command_output
      command:
      - cat
      - docs/book/docs_graph.json
assert:
- target: context_json
  must:
  - evaluate:
    - std.logic.eq:
      - true
      - true
```

## SRDOCGEN-004

```yaml spec-test
id: SRDOCGEN-004
type: docs.generate
title: schema docs surface generation
harness:
  docs_generate:
    surface_id: schema_docs
    mode: write
    output_mode: full_file
    template_path: /docs/book/templates/passthrough_text.md
    output_path: /docs/spec/schema/schema_v1.md
    data_sources:
    - id: content
      source_type: generated_artifact
      path: /docs/spec/schema/schema_v1.md
assert:
- target: context_json
  must:
  - evaluate:
    - std.logic.eq:
      - true
      - true
```

## SRDOCGEN-005

```yaml spec-test
id: SRDOCGEN-005
type: docs.generate
title: runner api catalog surface generation
harness:
  docs_generate:
    surface_id: runner_api_catalog
    mode: write
    output_mode: markers
    template_path: /docs/book/templates/runner_api_catalog_template.md
    output_path: /docs/book/91_appendix_runner_api_reference.md
    marker_surface_id: runner_api_catalog
    data_sources:
    - id: runner
      source_type: generated_artifact
      path: /.artifacts/runner-api-catalog.json
assert:
- target: context_json
  must:
  - evaluate:
    - std.logic.eq:
      - true
      - true
```

## SRDOCGEN-006

```yaml spec-test
id: SRDOCGEN-006
type: docs.generate
title: harness type catalog surface generation
harness:
  docs_generate:
    surface_id: harness_type_catalog
    mode: write
    output_mode: markers
    template_path: /docs/book/templates/harness_type_catalog_template.md
    output_path: /docs/book/92_appendix_harness_type_reference.md
    marker_surface_id: harness_type_catalog
    data_sources:
    - id: harness
      source_type: generated_artifact
      path: /.artifacts/harness-type-catalog.json
assert:
- target: context_json
  must:
  - evaluate:
    - std.logic.eq:
      - true
      - true
```

## SRDOCGEN-007

```yaml spec-test
id: SRDOCGEN-007
type: docs.generate
title: spec lang builtin catalog surface generation
harness:
  docs_generate:
    surface_id: spec_lang_builtin_catalog
    mode: write
    output_mode: markers
    template_path: /docs/book/templates/spec_lang_builtin_catalog_template.md
    output_path: /docs/book/93_appendix_spec_lang_builtin_catalog.md
    marker_surface_id: spec_lang_builtin_catalog
    data_sources:
    - id: stdlib
      source_type: generated_artifact
      path: /.artifacts/spec-lang-builtin-catalog.json
assert:
- target: context_json
  must:
  - evaluate:
    - std.logic.eq:
      - true
      - true
```

## SRDOCGEN-008

```yaml spec-test
id: SRDOCGEN-008
type: docs.generate
title: policy rule catalog surface generation
harness:
  docs_generate:
    surface_id: policy_rule_catalog
    mode: write
    output_mode: markers
    template_path: /docs/book/templates/policy_rule_catalog_template.md
    output_path: /docs/book/94_appendix_contract_policy_reference.md
    marker_surface_id: policy_rule_catalog
    data_sources:
    - id: policy
      source_type: generated_artifact
      path: /.artifacts/policy-rule-catalog.json
assert:
- target: context_json
  must:
  - evaluate:
    - std.logic.eq:
      - true
      - true
```

## SRDOCGEN-009

```yaml spec-test
id: SRDOCGEN-009
type: docs.generate
title: traceability catalog surface generation
harness:
  docs_generate:
    surface_id: traceability_catalog
    mode: write
    output_mode: markers
    template_path: /docs/book/templates/traceability_catalog_template.md
    output_path: /docs/book/95_appendix_traceability_reference.md
    marker_surface_id: traceability_catalog
    data_sources:
    - id: trace
      source_type: generated_artifact
      path: /.artifacts/traceability-catalog.json
assert:
- target: context_json
  must:
  - evaluate:
    - std.logic.eq:
      - true
      - true
```

## SRDOCGEN-010

```yaml spec-test
id: SRDOCGEN-010
type: docs.generate
title: governance check catalog surface generation
harness:
  docs_generate:
    surface_id: governance_check_catalog
    mode: write
    output_mode: markers
    template_path: /docs/book/templates/governance_check_catalog_template.md
    output_path: /docs/book/96_appendix_governance_checks_reference.md
    marker_surface_id: governance_check_catalog
    data_sources:
    - id: checks
      source_type: generated_artifact
      path: /.artifacts/governance-check-catalog.json
assert:
- target: context_json
  must:
  - evaluate:
    - std.logic.eq:
      - true
      - true
```

## SRDOCGEN-011

```yaml spec-test
id: SRDOCGEN-011
type: docs.generate
title: metrics field catalog surface generation
harness:
  docs_generate:
    surface_id: metrics_field_catalog
    mode: write
    output_mode: markers
    template_path: /docs/book/templates/metrics_field_catalog_template.md
    output_path: /docs/book/97_appendix_metrics_reference.md
    marker_surface_id: metrics_field_catalog
    data_sources:
    - id: metrics
      source_type: generated_artifact
      path: /.artifacts/metrics-field-catalog.json
assert:
- target: context_json
  must:
  - evaluate:
    - std.logic.eq:
      - true
      - true
```

## SRDOCGEN-012

```yaml spec-test
id: SRDOCGEN-012
type: docs.generate
title: spec schema field catalog surface generation for appendix
harness:
  docs_generate:
    surface_id: spec_schema_field_catalog
    mode: write
    output_mode: full_file
    template_path: /docs/book/templates/passthrough_text.md
    output_path: /docs/book/98_appendix_spec_case_shape_reference.md
    data_sources:
    - id: content
      source_type: generated_artifact
      path: /docs/book/98_appendix_spec_case_shape_reference.md
assert:
- target: context_json
  must:
  - evaluate:
    - std.logic.eq:
      - true
      - true
```

## SRDOCGEN-013

```yaml spec-test
id: SRDOCGEN-013
type: docs.generate
title: spec schema field catalog surface generation for schema docs
harness:
  docs_generate:
    surface_id: spec_schema_field_catalog
    mode: write
    output_mode: full_file
    template_path: /docs/book/templates/passthrough_text.md
    output_path: /docs/spec/schema/schema_v1.md
    data_sources:
    - id: content
      source_type: generated_artifact
      path: /docs/spec/schema/schema_v1.md
assert:
- target: context_json
  must:
  - evaluate:
    - std.logic.eq:
      - true
      - true
```

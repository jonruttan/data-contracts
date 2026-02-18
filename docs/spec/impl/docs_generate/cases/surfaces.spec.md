# Docs Generate Surfaces

## SRDOCGEN-001

```yaml contract-spec
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
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

## SRDOCGEN-002

```yaml contract-spec
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
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

## SRDOCGEN-003

```yaml contract-spec
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
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

## SRDOCGEN-004

```yaml contract-spec
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
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

## SRDOCGEN-005

```yaml contract-spec
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
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

## SRDOCGEN-006

```yaml contract-spec
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
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

## SRDOCGEN-007

```yaml contract-spec
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
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

## SRDOCGEN-008

```yaml contract-spec
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
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

## SRDOCGEN-009

```yaml contract-spec
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
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

## SRDOCGEN-010

```yaml contract-spec
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
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

## SRDOCGEN-011

```yaml contract-spec
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
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

## SRDOCGEN-012

```yaml contract-spec
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
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

## SRDOCGEN-013

```yaml contract-spec
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
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

## SRDOCGEN-014

```yaml contract-spec
id: SRDOCGEN-014
type: docs.generate
title: spec lang core namespace chapter generation
harness:
  docs_generate:
    surface_id: spec_lang_namespace_core
    mode: write
    output_mode: markers
    template_path: /docs/book/templates/spec_lang_namespace_core_template.md
    output_path: /docs/book/93a_std_core.md
    marker_surface_id: spec_lang_namespace_core
    data_sources:
    - id: stdlib
      source_type: generated_artifact
      path: /.artifacts/spec-lang-builtin-catalog.json
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

## SRDOCGEN-015

```yaml contract-spec
id: SRDOCGEN-015
type: docs.generate
title: spec lang logic namespace chapter generation
harness:
  docs_generate:
    surface_id: spec_lang_namespace_logic
    mode: write
    output_mode: markers
    template_path: /docs/book/templates/spec_lang_namespace_logic_template.md
    output_path: /docs/book/93b_std_logic.md
    marker_surface_id: spec_lang_namespace_logic
    data_sources:
    - id: stdlib
      source_type: generated_artifact
      path: /.artifacts/spec-lang-builtin-catalog.json
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

## SRDOCGEN-016

```yaml contract-spec
id: SRDOCGEN-016
type: docs.generate
title: spec lang math namespace chapter generation
harness:
  docs_generate:
    surface_id: spec_lang_namespace_math
    mode: write
    output_mode: markers
    template_path: /docs/book/templates/spec_lang_namespace_math_template.md
    output_path: /docs/book/93c_std_math.md
    marker_surface_id: spec_lang_namespace_math
    data_sources:
    - id: stdlib
      source_type: generated_artifact
      path: /.artifacts/spec-lang-builtin-catalog.json
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

## SRDOCGEN-017

```yaml contract-spec
id: SRDOCGEN-017
type: docs.generate
title: spec lang string namespace chapter generation
harness:
  docs_generate:
    surface_id: spec_lang_namespace_string
    mode: write
    output_mode: markers
    template_path: /docs/book/templates/spec_lang_namespace_string_template.md
    output_path: /docs/book/93d_std_string.md
    marker_surface_id: spec_lang_namespace_string
    data_sources:
    - id: stdlib
      source_type: generated_artifact
      path: /.artifacts/spec-lang-builtin-catalog.json
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

## SRDOCGEN-018

```yaml contract-spec
id: SRDOCGEN-018
type: docs.generate
title: spec lang collection namespace chapter generation
harness:
  docs_generate:
    surface_id: spec_lang_namespace_collection
    mode: write
    output_mode: markers
    template_path: /docs/book/templates/spec_lang_namespace_collection_template.md
    output_path: /docs/book/93e_std_collection.md
    marker_surface_id: spec_lang_namespace_collection
    data_sources:
    - id: stdlib
      source_type: generated_artifact
      path: /.artifacts/spec-lang-builtin-catalog.json
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

## SRDOCGEN-019

```yaml contract-spec
id: SRDOCGEN-019
type: docs.generate
title: spec lang object namespace chapter generation
harness:
  docs_generate:
    surface_id: spec_lang_namespace_object
    mode: write
    output_mode: markers
    template_path: /docs/book/templates/spec_lang_namespace_object_template.md
    output_path: /docs/book/93f_std_object.md
    marker_surface_id: spec_lang_namespace_object
    data_sources:
    - id: stdlib
      source_type: generated_artifact
      path: /.artifacts/spec-lang-builtin-catalog.json
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

## SRDOCGEN-020

```yaml contract-spec
id: SRDOCGEN-020
type: docs.generate
title: spec lang type namespace chapter generation
harness:
  docs_generate:
    surface_id: spec_lang_namespace_type
    mode: write
    output_mode: markers
    template_path: /docs/book/templates/spec_lang_namespace_type_template.md
    output_path: /docs/book/93g_std_type.md
    marker_surface_id: spec_lang_namespace_type
    data_sources:
    - id: stdlib
      source_type: generated_artifact
      path: /.artifacts/spec-lang-builtin-catalog.json
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

## SRDOCGEN-021

```yaml contract-spec
id: SRDOCGEN-021
type: docs.generate
title: spec lang set namespace chapter generation
harness:
  docs_generate:
    surface_id: spec_lang_namespace_set
    mode: write
    output_mode: markers
    template_path: /docs/book/templates/spec_lang_namespace_set_template.md
    output_path: /docs/book/93h_std_set.md
    marker_surface_id: spec_lang_namespace_set
    data_sources:
    - id: stdlib
      source_type: generated_artifact
      path: /.artifacts/spec-lang-builtin-catalog.json
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

## SRDOCGEN-022

```yaml contract-spec
id: SRDOCGEN-022
type: docs.generate
title: spec lang json schema fn null namespace chapter generation
harness:
  docs_generate:
    surface_id: spec_lang_namespace_json_schema_fn_null
    mode: write
    output_mode: markers
    template_path: /docs/book/templates/spec_lang_namespace_json_schema_fn_null_template.md
    output_path: /docs/book/93i_std_json_schema_fn_null.md
    marker_surface_id: spec_lang_namespace_json_schema_fn_null
    data_sources:
    - id: stdlib
      source_type: generated_artifact
      path: /.artifacts/spec-lang-builtin-catalog.json
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - true
    - true
  target: context_json
```

# Spec-Lang Contract-Set Domain Library

## LIB-DOMAIN-CONTRACT-SET-001

```yaml contract-spec
id: LIB-DOMAIN-CONTRACT-SET-001
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: contract-set manifest projection helper functions
type: contract.export
contract:
  defaults: {}
  steps:
  - id: __export__domain.contract_set.id
    assert:
      std.object.get:
      - {var: manifest}
      - contract_set_id
  - id: __export__domain.contract_set.depends_on
    assert:
      std.object.get:
      - {var: manifest}
      - depends_on
  - id: __export__domain.contract_set.include_paths
    assert:
      std.object.get:
      - {var: manifest}
      - include_paths
  - id: __export__domain.contract_set.applies_to_runners
    assert:
      std.object.get:
      - {var: manifest}
      - applies_to_runners
harness:
  exports:
  - as: domain.contract_set.id
    from: assert.function
    path: /__export__domain.contract_set.id
    params:
    - manifest
    required: true
    doc:
      summary: Contract export for `domain.contract_set.id`.
      description: Returns manifest `contract_set_id`.
      params:
      - name: manifest
        type: any
        required: true
        description: Contract-set manifest object projection.
      returns:
        type: string
        description: Manifest contract-set identifier.
      errors:
      - code: SCHEMA_ERROR
        when: Manifest does not contain the required field.
        category: schema
      examples:
      - title: Read id
        input:
          manifest:
            contract_set_id: python_runner_contract_set
        expected: python_runner_contract_set
      portability:
        python: true
        php: true
        rust: true
        notes: Portable stdlib projection.
      see_also: []
      since: v1
  - as: domain.contract_set.depends_on
    from: assert.function
    path: /__export__domain.contract_set.depends_on
    params:
    - manifest
    required: true
    doc:
      summary: Contract export for `domain.contract_set.depends_on`.
      description: Returns declared dependency list from manifest.
      params:
      - name: manifest
        type: any
        required: true
        description: Contract-set manifest object projection.
      returns:
        type: list
        description: Manifest dependency contract set ids.
      errors:
      - code: SCHEMA_ERROR
        when: Manifest does not contain the required field.
        category: schema
      examples:
      - title: Read dependencies
        input:
          manifest:
            depends_on: [shared_makefile_help_contract_set]
        expected: [shared_makefile_help_contract_set]
      portability:
        python: true
        php: true
        rust: true
        notes: Portable stdlib projection.
      see_also: []
      since: v1
  - as: domain.contract_set.include_paths
    from: assert.function
    path: /__export__domain.contract_set.include_paths
    params:
    - manifest
    required: true
    doc:
      summary: Contract export for `domain.contract_set.include_paths`.
      description: Returns include path/glob list from manifest.
      params:
      - name: manifest
        type: any
        required: true
        description: Contract-set manifest object projection.
      returns:
        type: list
        description: Include path/glob list.
      errors:
      - code: SCHEMA_ERROR
        when: Manifest does not contain the required field.
        category: schema
      examples:
      - title: Read include paths
        input:
          manifest:
            include_paths: [specs/impl/python/**]
        expected: [specs/impl/python/**]
      portability:
        python: true
        php: true
        rust: true
        notes: Portable stdlib projection.
      see_also: []
      since: v1
  - as: domain.contract_set.applies_to_runners
    from: assert.function
    path: /__export__domain.contract_set.applies_to_runners
    params:
    - manifest
    required: true
    doc:
      summary: Contract export for `domain.contract_set.applies_to_runners`.
      description: Returns optional runner applicability list.
      params:
      - name: manifest
        type: any
        required: true
        description: Contract-set manifest object projection.
      returns:
        type: list
        description: Runner ids list or null/empty list per manifest authoring.
      errors:
      - code: SCHEMA_ERROR
        when: Manifest does not contain expected structure.
        category: schema
      examples:
      - title: Read runner filter
        input:
          manifest:
            applies_to_runners: [python, php]
        expected: [python, php]
      portability:
        python: true
        php: true
        rust: true
        notes: Portable stdlib projection.
      see_also: []
      since: v1
library:
  id: domain.contract_set.core
  module: domain
  stability: alpha
  owner: data-contracts
  tags:
  - domain
doc:
  summary: Case `LIB-DOMAIN-CONTRACT-SET-001` for `contract.export`.
  description: Contract-set manifest projection exports for resolver policy and validation checks.
  audience: spec-authors
  since: v1
  tags:
  - contract.export
  see_also: []
```

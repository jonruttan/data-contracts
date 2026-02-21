```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-DOCS-REF-011
    title: generated docs command metadata avoids python execution
    purpose: Ensures generated docs `doc-meta.commands` use canonical rust adapter commands and do not reintroduce python execution tokens.
    harness:
      root: .
      generated_command_meta:
        files:
        - /docs/book/93j_library_symbol_reference.md
        - /docs/book/93k_library_symbol_index.md
        - /docs/book/93l_spec_case_reference.md
        - /docs/book/93m_spec_case_index.md
        - /docs/book/93n_spec_case_templates_reference.md
        required_tokens:
        - ./scripts/control_plane.sh docs-generate-check
        forbidden_tokens:
        - PYTHONPATH=runners/python
        - .venv/bin/python
        - spec_runner.spec_lang_commands
      check:
        profile: governance.scan
        config:
          check: docs.generated_command_meta_no_python_exec
      use:
      - ref: /specs/libraries/policy/policy_assertions.spec.md
        as: lib_policy_core_spec
        symbols:
        - policy.assert.no_violations
        - policy.assert.summary_passed
        - policy.assert.summary_check_id
        - policy.assert.scan_pass
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - violation_count
      predicates:
      - id: assert_1
        assert:
          call:
          - {var: policy.assert.no_violations}
          - std.object.assoc:
            - violation_count
            - {var: violation_count}
            - lit: {}
```

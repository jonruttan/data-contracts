```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.job
contracts:
- id: DCCONF-JOB-004
  title: schema registry build via contract.job
  purpose: Ensures script command contracts dispatch and return deterministic success state.
  harness:
    use:
    - ref: /specs/libraries/policy/policy_job.spec.md
      as: lib_policy_job
      symbols:
      - policy.job.dispatch_ok
      - policy.job.written_path_contains
    spec_lang:
      capabilities:
      - ops.helper
      - ops.job
    jobs:
    - id: main
      mode: build
      helper: helper.schema.registry_report
      inputs:
        format: json
        out: .artifacts/schema_registry_report.json
        check: false
    - id: on_fail
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/DCCONF-JOB-004.fail.json
        format: json
        report_name: DCCONF-JOB-004.fail
    - id: on_complete
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/DCCONF-JOB-004.complete.json
        format: json
        report_name: DCCONF-JOB-004.complete
  clauses:
    defaults: {}
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-005
  title: schema registry check via contract.job
  purpose: Ensures script command contracts dispatch and return deterministic success state.
  harness:
    use:
    - ref: /specs/libraries/policy/policy_job.spec.md
      as: lib_policy_job
      symbols:
      - policy.job.dispatch_ok
      - policy.job.written_path_contains
    spec_lang:
      capabilities:
      - ops.helper
      - ops.job
    jobs:
    - id: main
      mode: check
      helper: helper.schema.registry_report
      inputs:
        format: json
        out: .artifacts/schema_registry_report.json
        check: true
    - id: on_fail
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/DCCONF-JOB-005.fail.json
        format: json
        report_name: DCCONF-JOB-005.fail
    - id: on_complete
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/DCCONF-JOB-005.complete.json
        format: json
        report_name: DCCONF-JOB-005.complete
  clauses:
    defaults: {}
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-006
  title: docs lint via contract.job
  purpose: Ensures script command contracts dispatch and return deterministic success state.
  harness:
    use:
    - ref: /specs/libraries/policy/policy_job.spec.md
      as: lib_policy_job
      symbols:
      - policy.job.dispatch_ok
      - policy.job.written_path_contains
    spec_lang:
      capabilities:
      - ops.helper
      - ops.job
    jobs:
    - id: main
      mode: lint
      helper: helper.docs.lint
      inputs: {}
    - id: on_fail
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/DCCONF-JOB-006.fail.json
        format: json
        report_name: DCCONF-JOB-006.fail
    - id: on_complete
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/DCCONF-JOB-006.complete.json
        format: json
        report_name: DCCONF-JOB-006.complete
  clauses:
    defaults: {}
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-007
  title: docs generate build via contract.job
  purpose: Ensures script command contracts dispatch and return deterministic success state.
  harness:
    use:
    - ref: /specs/libraries/policy/policy_job.spec.md
      as: lib_policy_job
      symbols:
      - policy.job.dispatch_ok
      - policy.job.written_path_contains
    spec_lang:
      capabilities:
      - ops.helper
      - ops.job
    jobs:
    - id: main
      mode: build
      helper: helper.docs.generate_all
      inputs:
        action: build
    - id: on_fail
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/DCCONF-JOB-007.fail.json
        format: json
        report_name: DCCONF-JOB-007.fail
    - id: on_complete
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/DCCONF-JOB-007.complete.json
        format: json
        report_name: DCCONF-JOB-007.complete
  clauses:
    defaults: {}
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-008
  title: docs generate check via contract.job
  purpose: Ensures script command contracts dispatch and return deterministic success state.
  harness:
    use:
    - ref: /specs/libraries/policy/policy_job.spec.md
      as: lib_policy_job
      symbols:
      - policy.job.dispatch_ok
      - policy.job.written_path_contains
    spec_lang:
      capabilities:
      - ops.helper
      - ops.job
    jobs:
    - id: main
      mode: check
      helper: helper.docs.generate_all
      inputs:
        action: check
    - id: on_fail
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/DCCONF-JOB-008.fail.json
        format: json
        report_name: DCCONF-JOB-008.fail
    - id: on_complete
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/DCCONF-JOB-008.complete.json
        format: json
        report_name: DCCONF-JOB-008.complete
  clauses:
    defaults: {}
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-009
  title: docs build reference book via contract.job
  purpose: Ensures script command contracts dispatch and return deterministic success state.
  harness:
    use:
    - ref: /specs/libraries/policy/policy_job.spec.md
      as: lib_policy_job
      symbols:
      - policy.job.dispatch_ok
      - policy.job.written_path_contains
    spec_lang:
      capabilities:
      - ops.helper
      - ops.job
    jobs:
    - id: main
      mode: build
      helper: helper.docs.generate_all
      inputs:
        action: build
        surface: reference_book
    - id: on_fail
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/DCCONF-JOB-009.fail.json
        format: json
        report_name: DCCONF-JOB-009.fail
    - id: on_complete
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/DCCONF-JOB-009.complete.json
        format: json
        report_name: DCCONF-JOB-009.complete
  clauses:
    defaults: {}
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-010
  title: docs build check reference book via contract.job
  purpose: Ensures script command contracts dispatch and return deterministic success state.
  harness:
    use:
    - ref: /specs/libraries/policy/policy_job.spec.md
      as: lib_policy_job
      symbols:
      - policy.job.dispatch_ok
      - policy.job.written_path_contains
    spec_lang:
      capabilities:
      - ops.helper
      - ops.job
    jobs:
    - id: main
      mode: check
      helper: helper.docs.generate_all
      inputs:
        action: check
        surface: reference_book
    - id: on_fail
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/DCCONF-JOB-010.fail.json
        format: json
        report_name: DCCONF-JOB-010.fail
    - id: on_complete
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/DCCONF-JOB-010.complete.json
        format: json
        report_name: DCCONF-JOB-010.complete
  clauses:
    defaults: {}
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
- id: DCCONF-JOB-011
  title: docs graph export via contract.job
  purpose: Ensures script command contracts dispatch and return deterministic success state.
  harness:
    use:
    - ref: /specs/libraries/policy/policy_job.spec.md
      as: lib_policy_job
      symbols:
      - policy.job.dispatch_ok
      - policy.job.written_path_contains
    spec_lang:
      capabilities:
      - ops.helper
      - ops.job
    jobs:
    - id: main
      mode: build
      helper: helper.docs.generate_all
      inputs:
        action: build
        surface: docs_graph
    - id: on_fail
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/DCCONF-JOB-011.fail.json
        format: json
        report_name: DCCONF-JOB-011.fail
    - id: on_complete
      helper: helper.report.emit
      mode: report
      inputs:
        out: .artifacts/job-hooks/DCCONF-JOB-011.complete.json
        format: json
        report_name: DCCONF-JOB-011.complete
  clauses:
    defaults: {}
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
      - ops.job.dispatch:
        - main
      - call:
        - var: policy.job.dispatch_ok
        - var: summary_json
  when:
    fail:
    - ops.job.dispatch:
      - on_fail
    complete:
    - ops.job.dispatch:
      - on_complete
```















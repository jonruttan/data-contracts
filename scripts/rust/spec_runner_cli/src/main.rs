use std::env;
use std::path::{Path, PathBuf};
use std::process::{self, Command};

fn find_repo_root() -> Result<PathBuf, String> {
    let mut cur = env::current_dir().map_err(|e| format!("failed to read cwd: {e}"))?;
    loop {
        if cur.join(".git").exists() {
            return Ok(cur);
        }
        match cur.parent() {
            Some(parent) => cur = parent.to_path_buf(),
            None => return Err("unable to find repository root (.git)".to_string()),
        }
    }
}

fn run_cmd(program: &str, args: &[String], root: &Path) -> i32 {
    let mut cmd = Command::new(program);
    cmd.args(args)
        .current_dir(root)
        .stdin(process::Stdio::inherit())
        .stdout(process::Stdio::inherit())
        .stderr(process::Stdio::inherit());

    match cmd.status() {
        Ok(status) => status.code().unwrap_or(1),
        Err(e) => {
            eprintln!("ERROR: failed to run command '{program}': {e}");
            1
        }
    }
}

fn with_forwarded(base: Vec<String>, forwarded: &[String]) -> Vec<String> {
    base.into_iter().chain(forwarded.iter().cloned()).collect::<Vec<_>>()
}

fn tool_path(root: &Path, name: &str) -> String {
    let local = root.join(".venv").join("bin").join(name);
    if local.exists() {
        return local.to_string_lossy().to_string();
    }
    name.to_string()
}

fn python_path(root: &Path) -> String {
    let local = root.join(".venv").join("bin").join("python");
    if local.exists() {
        return local.to_string_lossy().to_string();
    }
    let parent = root.join("..").join("..").join(".venv").join("bin").join("python");
    if parent.exists() {
        return parent.to_string_lossy().to_string();
    }
    "python".to_string()
}

fn script(root: &Path, file: &str) -> String {
    root.join("scripts").join(file).to_string_lossy().to_string()
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        eprintln!("ERROR: missing runner adapter subcommand");
        process::exit(2);
    }

    let subcommand = args[1].clone();
    let forwarded: Vec<String> = args[2..].to_vec();

    let root = match find_repo_root() {
        Ok(p) => p,
        Err(msg) => {
            eprintln!("ERROR: {msg}");
            process::exit(1);
        }
    };

    let py = python_path(&root);
    let ruff = tool_path(&root, "ruff");
    let mypy = tool_path(&root, "mypy");
    let pytest = tool_path(&root, "pytest");

    let code = match subcommand.as_str() {
        "governance" => run_cmd(&py, &with_forwarded(vec![script(&root, "run_governance_specs.py")], &forwarded), &root),
        "style-check" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "evaluate_style.py"),
                    "--check".to_string(),
                    "docs/spec".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "normalize-check" => run_cmd(
            &py,
            &with_forwarded(vec![script(&root, "normalize_repo.py"), "--check".to_string()], &forwarded),
            &root,
        ),
        "normalize-fix" => run_cmd(
            &py,
            &with_forwarded(vec![script(&root, "normalize_repo.py"), "--write".to_string()], &forwarded),
            &root,
        ),
        "schema-registry-check" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "schema_registry_report.py"),
                    "--format".to_string(),
                    "json".to_string(),
                    "--out".to_string(),
                    ".artifacts/schema_registry_report.json".to_string(),
                    "--check".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "schema-registry-build" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "schema_registry_report.py"),
                    "--format".to_string(),
                    "json".to_string(),
                    "--out".to_string(),
                    ".artifacts/schema_registry_report.json".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "schema-docs-check" => run_cmd(
            &py,
            &with_forwarded(vec![script(&root, "generate_schema_docs.py"), "--check".to_string()], &forwarded),
            &root,
        ),
        "schema-docs-build" => run_cmd(
            &py,
            &with_forwarded(vec![script(&root, "generate_schema_docs.py")], &forwarded),
            &root,
        ),
        "lint" => run_cmd(&ruff, &with_forwarded(vec!["check".to_string(), ".".to_string()], &forwarded), &root),
        "typecheck" => run_cmd(&mypy, &with_forwarded(vec!["spec_runner".to_string()], &forwarded), &root),
        "compilecheck" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    "-m".to_string(),
                    "compileall".to_string(),
                    "-q".to_string(),
                    "spec_runner".to_string(),
                    "scripts".to_string(),
                    "tests".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "conformance-purpose-json" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "conformance_purpose_report.py"),
                    "--out".to_string(),
                    ".artifacts/conformance-purpose.json".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "conformance-purpose-md" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "conformance_purpose_report.py"),
                    "--format".to_string(),
                    "md".to_string(),
                    "--out".to_string(),
                    ".artifacts/conformance-purpose-summary.md".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "spec-portability-json" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "spec_portability_report.py"),
                    "--out".to_string(),
                    ".artifacts/spec-portability.json".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "spec-portability-md" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "spec_portability_report.py"),
                    "--format".to_string(),
                    "md".to_string(),
                    "--out".to_string(),
                    ".artifacts/spec-portability-summary.md".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "spec-lang-adoption-json" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "spec_lang_adoption_report.py"),
                    "--out".to_string(),
                    ".artifacts/spec-lang-adoption.json".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "spec-lang-adoption-md" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "spec_lang_adoption_report.py"),
                    "--format".to_string(),
                    "md".to_string(),
                    "--out".to_string(),
                    ".artifacts/spec-lang-adoption-summary.md".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "runner-independence-json" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "runner_independence_report.py"),
                    "--out".to_string(),
                    ".artifacts/runner-independence.json".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "runner-independence-md" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "runner_independence_report.py"),
                    "--format".to_string(),
                    "md".to_string(),
                    "--out".to_string(),
                    ".artifacts/runner-independence-summary.md".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "python-dependency-json" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "python_dependency_report.py"),
                    "--out".to_string(),
                    ".artifacts/python-dependency.json".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "python-dependency-md" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "python_dependency_report.py"),
                    "--format".to_string(),
                    "md".to_string(),
                    "--out".to_string(),
                    ".artifacts/python-dependency-summary.md".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "docs-operability-json" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "docs_operability_report.py"),
                    "--out".to_string(),
                    ".artifacts/docs-operability.json".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "docs-operability-md" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "docs_operability_report.py"),
                    "--format".to_string(),
                    "md".to_string(),
                    "--out".to_string(),
                    ".artifacts/docs-operability-summary.md".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "contract-assertions-json" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "contract_assertions_report.py"),
                    "--out".to_string(),
                    ".artifacts/contract-assertions.json".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "contract-assertions-md" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "contract_assertions_report.py"),
                    "--format".to_string(),
                    "md".to_string(),
                    "--out".to_string(),
                    ".artifacts/contract-assertions-summary.md".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "objective-scorecard-json" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "objective_scorecard_report.py"),
                    "--out".to_string(),
                    ".artifacts/objective-scorecard.json".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "objective-scorecard-md" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "objective_scorecard_report.py"),
                    "--format".to_string(),
                    "md".to_string(),
                    "--out".to_string(),
                    ".artifacts/objective-scorecard-summary.md".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "spec-lang-stdlib-json" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "spec_lang_stdlib_report.py"),
                    "--out".to_string(),
                    ".artifacts/spec-lang-stdlib.json".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "spec-lang-stdlib-md" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "spec_lang_stdlib_report.py"),
                    "--format".to_string(),
                    "md".to_string(),
                    "--out".to_string(),
                    ".artifacts/spec-lang-stdlib-summary.md".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "ci-gate-summary" => run_cmd(&py, &with_forwarded(vec![script(&root, "ci_gate_summary.py")], &forwarded), &root),
        "ci-cleanroom" => run_cmd(
            &script(&root, "ci_cleanroom.sh"),
            &with_forwarded(vec![], &forwarded),
            &root,
        ),
        "perf-smoke" => run_cmd(
            &py,
            &with_forwarded(vec![script(&root, "perf_smoke.py")], &forwarded),
            &root,
        ),
        "docs-generate" => run_cmd(
            &py,
            &with_forwarded(vec![script(&root, "docs_generate_all.py"), "--build".to_string()], &forwarded),
            &root,
        ),
        "docs-generate-check" => run_cmd(
            &py,
            &with_forwarded(vec![script(&root, "docs_generate_all.py"), "--check".to_string()], &forwarded),
            &root,
        ),
        "docs-build" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "docs_generate_all.py"),
                    "--build".to_string(),
                    "--surface".to_string(),
                    "reference_book".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "docs-build-check" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "docs_generate_all.py"),
                    "--check".to_string(),
                    "--surface".to_string(),
                    "reference_book".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "docs-lint" => run_cmd(&py, &with_forwarded(vec![script(&root, "docs_lint.py")], &forwarded), &root),
        "docs-graph" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "docs_generate_all.py"),
                    "--build".to_string(),
                    "--surface".to_string(),
                    "docs_graph".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "conformance-parity" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "compare_conformance_parity.py"),
                    "--cases".to_string(),
                    "docs/spec/conformance/cases".to_string(),
                    "--php-runner".to_string(),
                    "scripts/php/conformance_runner.php".to_string(),
                    "--out".to_string(),
                    ".artifacts/conformance-parity.json".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "test-core" => run_cmd(
            &pytest,
            &with_forwarded(
                vec![
                    "-q".to_string(),
                    "tests/test_doc_parser_unit.py".to_string(),
                    "tests/test_dispatcher_unit.py".to_string(),
                    "tests/test_assertions_unit.py".to_string(),
                    "tests/test_conformance_runner_unit.py".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "test-full" => run_cmd(&pytest, &with_forwarded(vec![], &forwarded), &root),
        _ => {
            eprintln!("ERROR: unsupported runner adapter subcommand: {subcommand}");
            2
        }
    };

    process::exit(code);
}

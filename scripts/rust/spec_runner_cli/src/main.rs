use std::env;
use std::fs;
use std::path::{Path, PathBuf};
use std::process::{self, Command};
use std::time::{Instant, SystemTime, UNIX_EPOCH};

use serde_json::{json, Value};

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

fn now_iso_utc_fallback() -> String {
    match SystemTime::now().duration_since(UNIX_EPOCH) {
        Ok(d) => format!("{}", d.as_secs()),
        Err(_) => "0".to_string(),
    }
}

fn runner_command(runner_bin: &str, runner_impl: &str, subcommand: &str) -> Vec<String> {
    let normalized = runner_bin.replace('\\', "/");
    let adapter_rel = format!("{}/{}", "scripts", "runner_adapter.sh");
    let adapter_prefixed = format!("./{}", adapter_rel);
    let adapter_suffix = format!("/{}", adapter_rel);
    if normalized.ends_with(&adapter_suffix)
        || normalized == adapter_rel
        || normalized == adapter_prefixed
    {
        return vec![
            runner_bin.to_string(),
            "--impl".to_string(),
            runner_impl.to_string(),
            subcommand.to_string(),
        ];
    }
    vec![runner_bin.to_string(), subcommand.to_string()]
}

fn run_command_capture_code(command: &[String], root: &Path) -> i32 {
    if command.is_empty() {
        return 1;
    }
    let mut cmd = Command::new(&command[0]);
    cmd.args(&command[1..])
        .current_dir(root)
        .stdin(process::Stdio::inherit())
        .stdout(process::Stdio::inherit())
        .stderr(process::Stdio::inherit());
    match cmd.status() {
        Ok(status) => status.code().unwrap_or(1),
        Err(e) => {
            eprintln!("ERROR: failed to run command '{}': {e}", command[0]);
            1
        }
    }
}

fn collect_unit_test_opt_out(root: &Path) -> Value {
    let tests_root = root.join("tests");
    let baseline_path = root.join("docs/spec/metrics/unit_test_opt_out_baseline.json");
    let mut total = 0_i64;
    let mut opted_out = 0_i64;
    let prefix = "# SPEC-OPT-OUT:";

    if tests_root.exists() {
        if let Ok(entries) = fs::read_dir(&tests_root) {
            let mut files = entries
                .filter_map(|e| e.ok())
                .map(|e| e.path())
                .filter(|p| p.is_file())
                .filter(|p| {
                    p.file_name()
                        .and_then(|n| n.to_str())
                        .map(|n| n.starts_with("test_") && n.ends_with("_unit.py"))
                        .unwrap_or(false)
                })
                .collect::<Vec<_>>();
            files.sort();
            for path in files {
                total += 1;
                let first_non_empty = fs::read_to_string(&path)
                    .ok()
                    .and_then(|txt| {
                        txt.lines()
                            .map(|l| l.trim())
                            .find(|l| !l.is_empty())
                            .map(|s| s.to_string())
                    })
                    .unwrap_or_default();
                if first_non_empty.starts_with(prefix) {
                    opted_out += 1;
                }
            }
        }
    }

    let mut baseline_max = 0_i64;
    if let Ok(text) = fs::read_to_string(&baseline_path) {
        if let Ok(v) = serde_json::from_str::<Value>(&text) {
            if let Some(x) = v
                .as_object()
                .and_then(|m| m.get("max_opt_out_file_count"))
                .and_then(|n| n.as_i64())
            {
                baseline_max = x;
            }
        }
    }

    json!({
        "total_unit_test_files": total,
        "opt_out_file_count": opted_out,
        "baseline_max_opt_out_file_count": baseline_max,
    })
}

fn run_ci_gate_summary_native(root: &Path, forwarded: &[String]) -> i32 {
    let mut out = ".artifacts/gate-summary.json".to_string();
    let mut runner_bin = format!("./{}/{}", "scripts", "runner_adapter.sh");
    let mut runner_impl = env::var("SPEC_RUNNER_IMPL").unwrap_or_else(|_| "rust".to_string());
    let mut trace_out = env::var("SPEC_RUNNER_TRACE_OUT").unwrap_or_default();

    let mut i = 0usize;
    while i < forwarded.len() {
        let arg = forwarded[i].as_str();
        if arg == "--out" {
            if i + 1 >= forwarded.len() {
                eprintln!("ERROR: --out requires value");
                return 2;
            }
            out = forwarded[i + 1].clone();
            i += 2;
            continue;
        }
        if arg == "--runner-bin" {
            if i + 1 >= forwarded.len() {
                eprintln!("ERROR: --runner-bin requires value");
                return 2;
            }
            runner_bin = forwarded[i + 1].clone();
            i += 2;
            continue;
        }
        if arg == "--runner-impl" {
            if i + 1 >= forwarded.len() {
                eprintln!("ERROR: --runner-impl requires value");
                return 2;
            }
            runner_impl = forwarded[i + 1].clone();
            i += 2;
            continue;
        }
        if arg == "--trace-out" {
            if i + 1 >= forwarded.len() {
                eprintln!("ERROR: --trace-out requires value");
                return 2;
            }
            trace_out = forwarded[i + 1].clone();
            i += 2;
            continue;
        }
        if arg == "--policy-case" {
            // Reserved for compatibility; policy is currently "all steps must pass".
            if i + 1 >= forwarded.len() {
                eprintln!("ERROR: --policy-case requires value");
                return 2;
            }
            i += 2;
            continue;
        }
        eprintln!("ERROR: unsupported ci-gate-summary arg: {arg}");
        return 2;
    }

    let default_steps = vec![
        ("governance", runner_command(&runner_bin, &runner_impl, "governance")),
        (
            "governance_heavy",
            runner_command(&runner_bin, &runner_impl, "governance-heavy"),
        ),
        (
            "docs_generate_check",
            runner_command(&runner_bin, &runner_impl, "docs-generate-check"),
        ),
        (
            "perf_smoke",
            {
                let mut c = runner_command(&runner_bin, &runner_impl, "perf-smoke");
                c.push("--mode".to_string());
                c.push("strict".to_string());
                c
            },
        ),
        ("docs_lint", runner_command(&runner_bin, &runner_impl, "docs-lint")),
        (
            "normalize_check",
            runner_command(&runner_bin, &runner_impl, "normalize-check"),
        ),
        (
            "schema_registry_build",
            runner_command(&runner_bin, &runner_impl, "schema-registry-build"),
        ),
        (
            "schema_registry_check",
            runner_command(&runner_bin, &runner_impl, "schema-registry-check"),
        ),
        (
            "schema_docs_check",
            runner_command(&runner_bin, &runner_impl, "schema-docs-check"),
        ),
        (
            "spec_portability_json",
            runner_command(&runner_bin, &runner_impl, "spec-portability-json"),
        ),
        (
            "spec_portability_md",
            runner_command(&runner_bin, &runner_impl, "spec-portability-md"),
        ),
        (
            "spec_lang_adoption_json",
            runner_command(&runner_bin, &runner_impl, "spec-lang-adoption-json"),
        ),
        (
            "spec_lang_adoption_md",
            runner_command(&runner_bin, &runner_impl, "spec-lang-adoption-md"),
        ),
        (
            "runner_independence_json",
            runner_command(&runner_bin, &runner_impl, "runner-independence-json"),
        ),
        (
            "runner_independence_md",
            runner_command(&runner_bin, &runner_impl, "runner-independence-md"),
        ),
        (
            "python_dependency_json",
            runner_command(&runner_bin, &runner_impl, "python-dependency-json"),
        ),
        (
            "python_dependency_md",
            runner_command(&runner_bin, &runner_impl, "python-dependency-md"),
        ),
        (
            "docs_operability_json",
            runner_command(&runner_bin, &runner_impl, "docs-operability-json"),
        ),
        (
            "docs_operability_md",
            runner_command(&runner_bin, &runner_impl, "docs-operability-md"),
        ),
        (
            "contract_assertions_json",
            runner_command(&runner_bin, &runner_impl, "contract-assertions-json"),
        ),
        (
            "contract_assertions_md",
            runner_command(&runner_bin, &runner_impl, "contract-assertions-md"),
        ),
        (
            "objective_scorecard_json",
            runner_command(&runner_bin, &runner_impl, "objective-scorecard-json"),
        ),
        (
            "objective_scorecard_md",
            runner_command(&runner_bin, &runner_impl, "objective-scorecard-md"),
        ),
        (
            "spec_lang_stdlib_json",
            runner_command(&runner_bin, &runner_impl, "spec-lang-stdlib-json"),
        ),
        (
            "spec_lang_stdlib_md",
            runner_command(&runner_bin, &runner_impl, "spec-lang-stdlib-md"),
        ),
        (
            "evaluate_style",
            runner_command(&runner_bin, &runner_impl, "style-check"),
        ),
        ("ruff", runner_command(&runner_bin, &runner_impl, "lint")),
        ("mypy", runner_command(&runner_bin, &runner_impl, "typecheck")),
        ("compileall", runner_command(&runner_bin, &runner_impl, "compilecheck")),
        (
            "conformance_purpose_json",
            runner_command(&runner_bin, &runner_impl, "conformance-purpose-json"),
        ),
        (
            "conformance_purpose_md",
            runner_command(&runner_bin, &runner_impl, "conformance-purpose-md"),
        ),
        (
            "conformance_parity",
            runner_command(&runner_bin, &runner_impl, "conformance-parity"),
        ),
        ("pytest", runner_command(&runner_bin, &runner_impl, "test-full")),
    ];

    let started = now_iso_utc_fallback();
    let t0 = Instant::now();
    let mut steps = Vec::<Value>::new();
    for (name, command) in default_steps {
        println!("[gate] {name}: {}", command.join(" "));
        let step_start = Instant::now();
        let code = run_command_capture_code(&command, root);
        let duration_ms = step_start.elapsed().as_millis() as i64;
        let status = if code == 0 { "pass" } else { "fail" };
        steps.push(json!({
            "name": name,
            "command": command,
            "status": status,
            "exit_code": code,
            "duration_ms": duration_ms,
        }));
    }

    let verdict = steps
        .iter()
        .all(|s| s.get("status").and_then(Value::as_str) == Some("pass"));
    let first_failure = steps
        .iter()
        .find_map(|s| s.get("exit_code").and_then(Value::as_i64).filter(|c| *c != 0))
        .unwrap_or(1) as i32;
    let exit_code = if verdict { 0 } else { first_failure };

    let finished = now_iso_utc_fallback();
    let total_duration_ms = t0.elapsed().as_millis() as i64;
    let payload = json!({
        "version": 1,
        "status": if verdict { "pass" } else { "fail" },
        "policy_verdict": if verdict { "pass" } else { "fail" },
        "policy_case": "docs/spec/governance/cases/core/runtime_orchestration_policy_via_spec_lang.spec.md",
        "policy_expr": [{"std.logic.eq":[{"std.collection.count":[{"std.collection.filter":[{"fn":[["step"],{"std.logic.neq":[{"std.object.get":[{"var":"step"},"status"]},"pass"]}]},{"var":"subject"}]}]},0]}],
        "started_at": started,
        "finished_at": finished,
        "total_duration_ms": total_duration_ms,
        "steps": steps,
        "runner_bin": runner_bin,
        "runner_impl": runner_impl,
        "unit_test_opt_out": collect_unit_test_opt_out(root),
    });

    let out_path = root.join(out.trim_start_matches('/'));
    if let Some(parent) = out_path.parent() {
        if let Err(e) = fs::create_dir_all(parent) {
            eprintln!("ERROR: failed to create output directory for {}: {e}", out_path.display());
            return 1;
        }
    }
    if let Err(e) = fs::write(&out_path, format!("{}\n", serde_json::to_string_pretty(&payload).unwrap_or_else(|_| "{}".to_string()))) {
        eprintln!("ERROR: failed to write gate summary {}: {e}", out_path.display());
        return 1;
    }
    if !trace_out.trim().is_empty() {
        let trace_path = root.join(trace_out.trim_start_matches('/'));
        if let Some(parent) = trace_path.parent() {
            if let Err(e) = fs::create_dir_all(parent) {
                eprintln!("ERROR: failed to create trace directory for {}: {e}", trace_path.display());
                return 1;
            }
        }
        let trace_payload = json!({
            "version": 1,
            "runner_bin": payload.get("runner_bin").cloned().unwrap_or(Value::Null),
            "runner_impl": payload.get("runner_impl").cloned().unwrap_or(Value::Null),
            "steps": payload.get("steps").cloned().unwrap_or(Value::Array(vec![])),
        });
        if let Err(e) = fs::write(&trace_path, format!("{}\n", serde_json::to_string_pretty(&trace_payload).unwrap_or_else(|_| "{}".to_string()))) {
            eprintln!("ERROR: failed to write gate trace {}: {e}", trace_path.display());
            return 1;
        }
        println!("[gate] trace: {}", trace_path.display());
    }
    println!("[gate] summary: {}", out_path.display());
    exit_code
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
        "governance-heavy" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    script(&root, "run_governance_specs.py"),
                    "--check-prefix".to_string(),
                    "runtime.chain".to_string(),
                    "--check-prefix".to_string(),
                    "library.".to_string(),
                    "--check-prefix".to_string(),
                    "normalization.mapping_ast_only".to_string(),
                    "--check-prefix".to_string(),
                    "normalization.virtual_root_paths_only".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
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
        "ci-gate-summary" => run_ci_gate_summary_native(&root, &forwarded),
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

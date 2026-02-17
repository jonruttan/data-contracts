mod spec_lang;
mod profiler;

use std::env;
use std::fs;
use std::path::{Path, PathBuf};
use std::process::{self, Command};
use std::sync::{Mutex, OnceLock};
use std::time::{Instant, SystemTime, UNIX_EPOCH};

use serde_json::{json, Value};
use serde_yaml::Value as YamlValue;
use spec_lang::{eval_mapping_ast, EvalLimits};
use profiler::{profile_options_from_env, RunProfiler};

static ACTIVE_PROFILER: OnceLock<Mutex<Option<RunProfiler>>> = OnceLock::new();

fn profiler_cell() -> &'static Mutex<Option<RunProfiler>> {
    ACTIVE_PROFILER.get_or_init(|| Mutex::new(None))
}

fn profiler_start_span(
    name: &str,
    kind: &str,
    phase: &str,
    parent_span_id: Option<String>,
    attrs: Value,
) -> Option<String> {
    if let Ok(mut guard) = profiler_cell().lock() {
        if let Some(prof) = guard.as_mut() {
            return prof.start_span(name, kind, phase, parent_span_id, attrs);
        }
    }
    None
}

fn profiler_finish_span(span_id: Option<&str>, status: &str, error: Option<Value>) {
    let Some(sid) = span_id else { return };
    if let Ok(mut guard) = profiler_cell().lock() {
        if let Some(prof) = guard.as_mut() {
            prof.finish_span(sid, status, error);
        }
    }
}

fn profiler_event(kind: &str, span_id: Option<&str>, attrs: Value) {
    if let Ok(mut guard) = profiler_cell().lock() {
        if let Some(prof) = guard.as_mut() {
            prof.event(kind, span_id, attrs);
        }
    }
}

fn debug_enabled() -> bool {
    matches!(std::env::var("SPEC_RUNNER_DEBUG").ok().as_deref(), Some("1") | Some("true") | Some("yes"))
}

fn debug_level() -> u8 {
    if let Ok(raw) = std::env::var("SPEC_RUNNER_DEBUG_LEVEL") {
        if let Ok(parsed) = raw.parse::<u8>() {
            return parsed;
        }
    }
    if debug_enabled() {
        1
    } else {
        0
    }
}

fn debug_log(msg: &str) {
    if debug_level() >= 1 {
        eprintln!("[spec_runner_cli debug] {msg}");
    }
}

fn debug_log_at(level: u8, msg: &str) {
    if debug_level() >= level {
        eprintln!("[spec_runner_cli debug:{level}] {msg}");
    }
}

fn find_repo_root() -> Result<PathBuf, String> {
    let mut cur = env::current_dir().map_err(|e| format!("failed to read cwd: {e}"))?;
    debug_log(&format!("find_repo_root:start cwd={}", cur.display()));
    loop {
        debug_log_at(3, &format!("find_repo_root:check {}", cur.display()));
        if cur.join(".git").exists() {
            debug_log(&format!("find_repo_root:found {}", cur.display()));
            return Ok(cur);
        }
        match cur.parent() {
            Some(parent) => {
                let next = parent.to_path_buf();
                if next == cur {
                    debug_log("find_repo_root:stuck-at-root");
                    return Err("unable to find repository root (.git)".to_string());
                }
                cur = next;
            }
            None => return Err("unable to find repository root (.git)".to_string()),
        }
    }
}

fn run_cmd(program: &str, args: &[String], root: &Path) -> i32 {
    let span_id = profiler_start_span(
        "subprocess.exec",
        "subprocess",
        "subprocess.exec",
        None,
        json!({
            "argv_preview": format!("{} {}", program, args.join(" ")),
            "cwd": root.display().to_string()
        }),
    );
    let mut cmd = Command::new(program);
    cmd.args(args)
        .current_dir(root)
        .stdin(process::Stdio::inherit())
        .stdout(process::Stdio::inherit())
        .stderr(process::Stdio::inherit());
    match cmd.spawn() {
        Ok(mut child) => {
            let pid = child.id();
            profiler_event("subprocess_state", span_id.as_deref(), json!({"state":"spawned","pid":pid}));
            let code = match child.wait() {
                Ok(status) => status.code().unwrap_or(1),
                Err(e) => {
                    profiler_event("subprocess_state", span_id.as_deref(), json!({"state":"wait_error","message":e.to_string()}));
                    eprintln!("ERROR: failed waiting command '{program}': {e}");
                    1
                }
            };
            profiler_event("subprocess_state", span_id.as_deref(), json!({"state":"exit","pid":pid,"returncode":code}));
            profiler_finish_span(
                span_id.as_deref(),
                if code == 0 { "ok" } else { "error" },
                if code == 0 {
                    None
                } else {
                    Some(json!({"category":"runtime","message":format!("non-zero exit: {code}")}))
                },
            );
            code
        }
        Err(e) => {
            eprintln!("ERROR: failed to run command '{program}': {e}");
            profiler_finish_span(
                span_id.as_deref(),
                "error",
                Some(json!({"category":"runtime","message":e.to_string()})),
            );
            1
        }
    }
}

fn with_forwarded(base: Vec<String>, forwarded: &[String]) -> Vec<String> {
    base.into_iter()
        .chain(forwarded.iter().cloned())
        .collect::<Vec<_>>()
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
    let parent = root
        .join("..")
        .join("..")
        .join(".venv")
        .join("bin")
        .join("python");
    if parent.exists() {
        return parent.to_string_lossy().to_string();
    }
    "python".to_string()
}

fn script(root: &Path, file: &str) -> String {
    root.join("scripts")
        .join(file)
        .to_string_lossy()
        .to_string()
}

fn now_iso_utc_fallback() -> String {
    match SystemTime::now().duration_since(UNIX_EPOCH) {
        Ok(d) => format!("{}", d.as_secs()),
        Err(_) => "0".to_string(),
    }
}

fn command_spec_ref(subcommand: &str) -> Option<&'static str> {
    match subcommand {
        "validate-report" => Some(
            "/docs/spec/libraries/domain/conformance_core.spec.md#LIB-DOMAIN-CONFORMANCE-001-000C-DOMAIN-CONFORMANCE-VALIDATE-REPORT-ERRORS",
        ),
        "docs-lint" => Some("/docs/spec/impl/python/cases/docs_lint.spec.md#SRPY-DOCSLINT-001"),
        "schema-registry-build" => Some(
            "/docs/spec/impl/python/cases/schema_registry_report.spec.md#SRPY-SCHEMA-REG-001",
        ),
        "schema-registry-check" => Some(
            "/docs/spec/impl/python/cases/schema_registry_report.spec.md#SRPY-SCHEMA-REG-002",
        ),
        "spec-lang-stdlib-json" => Some(
            "/docs/spec/impl/python/cases/spec_lang_stdlib_report.spec.md#SRPY-STDLIB-REP-001",
        ),
        "spec-lang-stdlib-md" => Some(
            "/docs/spec/impl/python/cases/spec_lang_stdlib_report.spec.md#SRPY-STDLIB-REP-002",
        ),
        "contract-assertions-json" => Some(
            "/docs/spec/impl/python/cases/contract_coverage_report.spec.md#SRPY-CONTRACT-REP-001",
        ),
        "contract-assertions-md" => Some(
            "/docs/spec/impl/python/cases/contract_coverage_report.spec.md#SRPY-CONTRACT-REP-002",
        ),
        _ => None,
    }
}

fn parse_spec_ref(spec_ref: &str) -> Result<(String, Option<String>), String> {
    let raw = spec_ref.trim();
    if raw.is_empty() {
        return Err("spec ref must not be empty".to_string());
    }
    let mut parts = raw.splitn(2, '#');
    let path = parts.next().unwrap_or("").trim().to_string();
    let frag = parts.next().map(|s| s.trim().to_string());
    if path.is_empty() {
        return Err(format!("spec ref must include path: {spec_ref}"));
    }
    if let Some(f) = &frag {
        if f.is_empty() {
            return Err(format!("spec ref has empty case id fragment: {spec_ref}"));
        }
    }
    Ok((path, frag))
}

fn extract_spec_test_blocks(markdown: &str) -> Vec<String> {
    let mut blocks = Vec::<String>::new();
    let mut in_block = false;
    let mut cur = String::new();
    for line in markdown.lines() {
        let trimmed = line.trim_end();
        if !in_block && trimmed == "```yaml spec-test" {
            in_block = true;
            cur.clear();
            continue;
        }
        if in_block && trimmed == "```" {
            blocks.push(cur.clone());
            in_block = false;
            cur.clear();
            continue;
        }
        if in_block {
            cur.push_str(line);
            cur.push('\n');
        }
    }
    blocks
}

fn block_id(block: &str) -> Option<String> {
    for line in block.lines() {
        let t = line.trim();
        if let Some(rest) = t.strip_prefix("id:") {
            let v = rest.trim();
            if !v.is_empty() {
                return Some(v.to_string());
            }
        }
    }
    None
}

fn load_case_block_from_spec_ref(root: &Path, spec_ref: &str) -> Result<String, String> {
    let (path_raw, case_id) = parse_spec_ref(spec_ref)?;
    let rel = path_raw.trim_start_matches('/');
    let path = root.join(rel);
    let text = fs::read_to_string(&path)
        .map_err(|e| format!("failed to read producer spec {}: {e}", path.display()))?;
    let blocks = extract_spec_test_blocks(&text);
    if blocks.is_empty() {
        return Err(format!("no `yaml spec-test` blocks in {}", path.display()));
    }
    for block in blocks {
        if let Some(want) = &case_id {
            if block_id(&block).as_deref() != Some(want.as_str()) {
                continue;
            }
        }
        return Ok(block);
    }
    Err(format!("case not found via spec ref: {}", spec_ref))
}

fn ensure_validate_report_export_contract(case_block: &str, spec_ref: &str) -> Result<(), String> {
    let required_tokens = [
        "type: spec.export",
        "as: domain.conformance.validate_report_errors",
        "from: assert.function",
        "path: /__export__domain.conformance.validate_report_errors",
        "params:",
        "- report",
        "report.version must equal 1",
        "report.results must be a list",
    ];
    for token in required_tokens {
        if !case_block.contains(token) {
            return Err(format!(
                "producer contract drift for {spec_ref}: missing token `{token}`"
            ));
        }
    }
    Ok(())
}

fn yaml_to_json(value: &YamlValue) -> Value {
    match value {
        YamlValue::Null => Value::Null,
        YamlValue::Bool(b) => Value::Bool(*b),
        YamlValue::Number(n) => {
            if let Some(i) = n.as_i64() {
                Value::Number(i.into())
            } else if let Some(f) = n.as_f64() {
                serde_json::Number::from_f64(f)
                    .map(Value::Number)
                    .unwrap_or(Value::Null)
            } else {
                Value::Null
            }
        }
        YamlValue::String(s) => Value::String(s.clone()),
        YamlValue::Sequence(seq) => Value::Array(seq.iter().map(yaml_to_json).collect()),
        YamlValue::Mapping(map) => {
            let mut out = serde_json::Map::new();
            for (k, v) in map {
                if let YamlValue::String(key) = k {
                    out.insert(key.clone(), yaml_to_json(v));
                }
            }
            Value::Object(out)
        }
        _ => Value::Null,
    }
}

fn parse_validate_report_expr_from_case(case_block: &str, spec_ref: &str) -> Result<Value, String> {
    let doc: YamlValue = serde_yaml::from_str(case_block)
        .map_err(|e| format!("failed to parse producer yaml for {spec_ref}: {e}"))?;
    let root = match doc {
        YamlValue::Mapping(m) => m,
        _ => return Err(format!("invalid producer case shape for {spec_ref}: expected mapping")),
    };
    let assert_node = root
        .get(&YamlValue::String("assert".to_string()))
        .ok_or_else(|| format!("missing assert in producer case: {spec_ref}"))?;
    let assert_seq = match assert_node {
        YamlValue::Sequence(seq) => seq,
        _ => return Err(format!("producer assert must be sequence: {spec_ref}")),
    };
    let target_step_id = "__export__domain.conformance.validate_report_errors";
    for step in assert_seq {
        let step_map = match step {
            YamlValue::Mapping(m) => m,
            _ => continue,
        };
        let sid = step_map
            .get(&YamlValue::String("id".to_string()))
            .and_then(|v| match v {
                YamlValue::String(s) => Some(s.as_str()),
                _ => None,
            })
            .unwrap_or("");
        if sid != target_step_id {
            continue;
        }
        let checks = step_map
            .get(&YamlValue::String("checks".to_string()))
            .ok_or_else(|| format!("producer step missing checks: {target_step_id}"))?;
        let check_seq = match checks {
            YamlValue::Sequence(seq) => seq,
            _ => return Err(format!("producer checks must be sequence: {target_step_id}")),
        };
        if check_seq.len() != 1 {
            return Err(format!(
                "producer checks must contain exactly one expression: {target_step_id}"
            ));
        }
        return Ok(yaml_to_json(&check_seq[0]));
    }
    Err(format!(
        "producer step not found in {spec_ref}: {target_step_id}"
    ))
}

fn validate_report_payload(payload: &Value, expr: &Value) -> Vec<String> {
    match eval_mapping_ast(
        expr,
        payload.clone(),
        std::collections::HashMap::new(),
        EvalLimits::default(),
    ) {
        Ok(Value::Array(items)) => items
            .into_iter()
            .filter_map(|v| v.as_str().map(|s| s.to_string()))
            .collect::<Vec<_>>(),
        Ok(_) => vec!["validate_report expression must return list".to_string()],
        Err(e) => vec![format!("spec_lang error: {}", e.message)],
    }
}

fn run_validate_report_native(root: &Path, forwarded: &[String]) -> i32 {
    debug_log("validate-report:start");
    if forwarded.len() != 1 {
        eprintln!("usage: validate-report <report-json-path>");
        return 2;
    }
    let report_path = {
        let p = PathBuf::from(&forwarded[0]);
        if p.is_absolute() {
            p
        } else {
            root.join(p)
        }
    };
    let report_text = match fs::read_to_string(&report_path) {
        Ok(s) => s,
        Err(e) => {
            eprintln!(
                "ERROR: failed to read report {}: {e}",
                report_path.display()
            );
            return 1;
        }
    };
    debug_log(&format!("validate-report:report-bytes={}", report_text.len()));
    let payload: Value = match serde_json::from_str(&report_text) {
        Ok(v) => v,
        Err(e) => {
            eprintln!("ERROR: invalid report json {}: {e}", report_path.display());
            return 1;
        }
    };
    let spec_ref = match command_spec_ref("validate-report") {
        Some(v) => v,
        None => {
            eprintln!("ERROR: missing spec ref registration for validate-report");
            return 1;
        }
    };
    debug_log(&format!("validate-report:spec-ref={spec_ref}"));
    let case_block = match load_case_block_from_spec_ref(root, spec_ref) {
        Ok(v) => v,
        Err(e) => {
            eprintln!("ERROR: {e}");
            return 1;
        }
    };
    debug_log(&format!(
        "validate-report:producer-case-bytes={}",
        case_block.len()
    ));
    if let Err(e) = ensure_validate_report_export_contract(&case_block, spec_ref) {
        eprintln!("ERROR: {e}");
        return 1;
    }
    let expr = match parse_validate_report_expr_from_case(&case_block, spec_ref) {
        Ok(v) => v,
        Err(e) => {
            eprintln!("ERROR: {e}");
            return 1;
        }
    };
    debug_log_at(2, "validate-report:loaded expression from producer export");
    let errors = validate_report_payload(&payload, &expr);
    debug_log(&format!("validate-report:error-count={}", errors.len()));
    if errors.is_empty() {
        println!("OK: valid conformance report ({})", report_path.display());
        0
    } else {
        for err in errors {
            eprintln!("ERROR: {err}");
        }
        1
    }
}

fn run_spec_ref_print(subcommand: &str) -> i32 {
    debug_log(&format!("spec-ref:lookup subcommand={subcommand}"));
    let Some(spec_ref) = command_spec_ref(subcommand) else {
        eprintln!("ERROR: no registered spec ref for command: {subcommand}");
        return 1;
    };
    debug_log(&format!("spec-ref:resolved {spec_ref}"));
    println!("{spec_ref}");
    0
}

fn run_spec_eval_native(root: &Path, forwarded: &[String]) -> i32 {
    debug_log(&format!(
        "spec-eval:start cwd={} args={}",
        root.display(),
        forwarded.len()
    ));
    let mut expr_json: Option<String> = None;
    let mut expr_file: Option<String> = None;
    let mut subject_json: Option<String> = None;
    let mut subject_file: Option<String> = None;

    let mut i = 0usize;
    while i < forwarded.len() {
        let arg = forwarded[i].as_str();
        match arg {
            "--expr-json" => {
                if i + 1 >= forwarded.len() {
                    eprintln!("ERROR: --expr-json requires value");
                    return 2;
                }
                expr_json = Some(forwarded[i + 1].clone());
                i += 2;
            }
            "--expr-file" => {
                if i + 1 >= forwarded.len() {
                    eprintln!("ERROR: --expr-file requires value");
                    return 2;
                }
                expr_file = Some(forwarded[i + 1].clone());
                i += 2;
            }
            "--subject-json" => {
                if i + 1 >= forwarded.len() {
                    eprintln!("ERROR: --subject-json requires value");
                    return 2;
                }
                subject_json = Some(forwarded[i + 1].clone());
                i += 2;
            }
            "--subject-file" => {
                if i + 1 >= forwarded.len() {
                    eprintln!("ERROR: --subject-file requires value");
                    return 2;
                }
                subject_file = Some(forwarded[i + 1].clone());
                i += 2;
            }
            _ => {
                eprintln!("ERROR: unsupported spec-eval arg: {arg}");
                return 2;
            }
        }
    }

    let expr_val: Value = match (expr_json, expr_file) {
        (Some(raw), None) => match serde_json::from_str(&raw) {
            Ok(v) => v,
            Err(e) => {
                eprintln!("ERROR: invalid --expr-json: {e}");
                return 2;
            }
        },
        (None, Some(path)) => {
            let p = root.join(path.trim_start_matches('/'));
            let raw = match fs::read_to_string(&p) {
                Ok(s) => s,
                Err(e) => {
                    eprintln!("ERROR: failed to read --expr-file {}: {e}", p.display());
                    return 2;
                }
            };
            match serde_json::from_str(&raw) {
                Ok(v) => v,
                Err(e) => {
                    eprintln!("ERROR: invalid JSON in --expr-file {}: {e}", p.display());
                    return 2;
                }
            }
        }
        _ => {
            eprintln!("ERROR: provide exactly one of --expr-json or --expr-file");
            return 2;
        }
    };

    let subject_val: Value = match (subject_json, subject_file) {
        (Some(raw), None) => match serde_json::from_str(&raw) {
            Ok(v) => v,
            Err(e) => {
                eprintln!("ERROR: invalid --subject-json: {e}");
                return 2;
            }
        },
        (None, Some(path)) => {
            let p = root.join(path.trim_start_matches('/'));
            let raw = match fs::read_to_string(&p) {
                Ok(s) => s,
                Err(e) => {
                    eprintln!("ERROR: failed to read --subject-file {}: {e}", p.display());
                    return 2;
                }
            };
            match serde_json::from_str(&raw) {
                Ok(v) => v,
                Err(e) => {
                    eprintln!("ERROR: invalid JSON in --subject-file {}: {e}", p.display());
                    return 2;
                }
            }
        }
        (None, None) => Value::Null,
        _ => {
            eprintln!("ERROR: provide at most one of --subject-json or --subject-file");
            return 2;
        }
    };

    match eval_mapping_ast(
        &expr_val,
        subject_val,
        std::collections::HashMap::new(),
        EvalLimits::default(),
    ) {
        Ok(v) => {
            debug_log("spec-eval:success");
            println!(
                "{}",
                serde_json::to_string_pretty(&v).unwrap_or_else(|_| "null".to_string())
            );
            0
        }
        Err(e) => {
            debug_log(&format!("spec-eval:error {}", e.message));
            eprintln!("ERROR: {}", e.message);
            1
        }
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
    let span_id = profiler_start_span(
        "subprocess.exec",
        "subprocess",
        "subprocess.exec",
        None,
        json!({
            "argv_preview": command.join(" "),
            "cwd": root.display().to_string()
        }),
    );
    let mut cmd = Command::new(&command[0]);
    cmd.args(&command[1..])
        .current_dir(root)
        .stdin(process::Stdio::inherit())
        .stdout(process::Stdio::inherit())
        .stderr(process::Stdio::inherit());
    match cmd.spawn() {
        Ok(mut child) => {
            let pid = child.id();
            profiler_event("subprocess_state", span_id.as_deref(), json!({"state":"spawned","pid":pid}));
            let code = match child.wait() {
                Ok(status) => status.code().unwrap_or(1),
                Err(e) => {
                    profiler_event("subprocess_state", span_id.as_deref(), json!({"state":"wait_error","message":e.to_string()}));
                    eprintln!("ERROR: failed waiting command '{}': {e}", command[0]);
                    1
                }
            };
            profiler_event("subprocess_state", span_id.as_deref(), json!({"state":"exit","pid":pid,"returncode":code}));
            profiler_finish_span(
                span_id.as_deref(),
                if code == 0 { "ok" } else { "error" },
                if code == 0 {
                    None
                } else {
                    Some(json!({"category":"runtime","message":format!("non-zero exit: {code}")}))
                },
            );
            code
        }
        Err(e) => {
            eprintln!("ERROR: failed to run command '{}': {e}", command[0]);
            profiler_finish_span(
                span_id.as_deref(),
                "error",
                Some(json!({"category":"runtime","message":e.to_string()})),
            );
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
        (
            "governance",
            runner_command(&runner_bin, &runner_impl, "governance"),
        ),
        (
            "governance_heavy",
            runner_command(&runner_bin, &runner_impl, "governance-heavy"),
        ),
        (
            "docs_generate_check",
            runner_command(&runner_bin, &runner_impl, "docs-generate-check"),
        ),
        ("perf_smoke", {
            let mut c = runner_command(&runner_bin, &runner_impl, "perf-smoke");
            c.push("--mode".to_string());
            c.push("strict".to_string());
            c
        }),
        (
            "docs_lint",
            runner_command(&runner_bin, &runner_impl, "docs-lint"),
        ),
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
        (
            "mypy",
            runner_command(&runner_bin, &runner_impl, "typecheck"),
        ),
        (
            "compileall",
            runner_command(&runner_bin, &runner_impl, "compilecheck"),
        ),
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
        (
            "pytest",
            runner_command(&runner_bin, &runner_impl, "test-full"),
        ),
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
        .find_map(|s| {
            s.get("exit_code")
                .and_then(Value::as_i64)
                .filter(|c| *c != 0)
        })
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
            eprintln!(
                "ERROR: failed to create output directory for {}: {e}",
                out_path.display()
            );
            return 1;
        }
    }
    if let Err(e) = fs::write(
        &out_path,
        format!(
            "{}\n",
            serde_json::to_string_pretty(&payload).unwrap_or_else(|_| "{}".to_string())
        ),
    ) {
        eprintln!(
            "ERROR: failed to write gate summary {}: {e}",
            out_path.display()
        );
        return 1;
    }
    if !trace_out.trim().is_empty() {
        let trace_path = root.join(trace_out.trim_start_matches('/'));
        if let Some(parent) = trace_path.parent() {
            if let Err(e) = fs::create_dir_all(parent) {
                eprintln!(
                    "ERROR: failed to create trace directory for {}: {e}",
                    trace_path.display()
                );
                return 1;
            }
        }
        let trace_payload = json!({
            "version": 1,
            "runner_bin": payload.get("runner_bin").cloned().unwrap_or(Value::Null),
            "runner_impl": payload.get("runner_impl").cloned().unwrap_or(Value::Null),
            "steps": payload.get("steps").cloned().unwrap_or(Value::Array(vec![])),
        });
        if let Err(e) = fs::write(
            &trace_path,
            format!(
                "{}\n",
                serde_json::to_string_pretty(&trace_payload).unwrap_or_else(|_| "{}".to_string())
            ),
        ) {
            eprintln!(
                "ERROR: failed to write gate trace {}: {e}",
                trace_path.display()
            );
            return 1;
        }
        println!("[gate] trace: {}", trace_path.display());
    }
    println!("[gate] summary: {}", out_path.display());
    exit_code
}

fn main() {
    debug_log("main:start");
    let args: Vec<String> = env::args().collect();
    debug_log("main:args_collected");
    let mut arg_index = 1usize;
    while arg_index < args.len() {
        let flag = args[arg_index].as_str();
        match flag {
            "--verbose" | "-v" => {
                std::env::set_var("SPEC_RUNNER_DEBUG", "1");
                std::env::set_var("SPEC_RUNNER_DEBUG_LEVEL", "1");
                arg_index += 1;
            }
            "-vv" => {
                std::env::set_var("SPEC_RUNNER_DEBUG", "1");
                std::env::set_var("SPEC_RUNNER_DEBUG_LEVEL", "2");
                arg_index += 1;
            }
            "-vvv" => {
                std::env::set_var("SPEC_RUNNER_DEBUG", "1");
                std::env::set_var("SPEC_RUNNER_DEBUG_LEVEL", "3");
                arg_index += 1;
            }
            "--profile-level" => {
                if arg_index + 1 >= args.len() {
                    eprintln!("ERROR: --profile-level requires value");
                    process::exit(2);
                }
                std::env::set_var("SPEC_RUNNER_PROFILE_LEVEL", args[arg_index + 1].clone());
                arg_index += 2;
            }
            "--profile-out" => {
                if arg_index + 1 >= args.len() {
                    eprintln!("ERROR: --profile-out requires value");
                    process::exit(2);
                }
                std::env::set_var("SPEC_RUNNER_PROFILE_OUT", args[arg_index + 1].clone());
                arg_index += 2;
            }
            "--profile-summary-out" => {
                if arg_index + 1 >= args.len() {
                    eprintln!("ERROR: --profile-summary-out requires value");
                    process::exit(2);
                }
                std::env::set_var("SPEC_RUNNER_PROFILE_SUMMARY_OUT", args[arg_index + 1].clone());
                arg_index += 2;
            }
            "--profile-heartbeat-ms" => {
                if arg_index + 1 >= args.len() {
                    eprintln!("ERROR: --profile-heartbeat-ms requires value");
                    process::exit(2);
                }
                std::env::set_var("SPEC_RUNNER_PROFILE_HEARTBEAT_MS", args[arg_index + 1].clone());
                arg_index += 2;
            }
            "--profile-stall-threshold-ms" => {
                if arg_index + 1 >= args.len() {
                    eprintln!("ERROR: --profile-stall-threshold-ms requires value");
                    process::exit(2);
                }
                std::env::set_var("SPEC_RUNNER_PROFILE_STALL_THRESHOLD_MS", args[arg_index + 1].clone());
                arg_index += 2;
            }
            "--liveness-level" => {
                if arg_index + 1 >= args.len() {
                    eprintln!("ERROR: --liveness-level requires value");
                    process::exit(2);
                }
                std::env::set_var("SPEC_RUNNER_LIVENESS_LEVEL", args[arg_index + 1].clone());
                arg_index += 2;
            }
            "--liveness-stall-ms" => {
                if arg_index + 1 >= args.len() {
                    eprintln!("ERROR: --liveness-stall-ms requires value");
                    process::exit(2);
                }
                std::env::set_var("SPEC_RUNNER_LIVENESS_STALL_MS", args[arg_index + 1].clone());
                arg_index += 2;
            }
            "--liveness-min-events" => {
                if arg_index + 1 >= args.len() {
                    eprintln!("ERROR: --liveness-min-events requires value");
                    process::exit(2);
                }
                std::env::set_var("SPEC_RUNNER_LIVENESS_MIN_EVENTS", args[arg_index + 1].clone());
                arg_index += 2;
            }
            "--liveness-hard-cap-ms" => {
                if arg_index + 1 >= args.len() {
                    eprintln!("ERROR: --liveness-hard-cap-ms requires value");
                    process::exit(2);
                }
                std::env::set_var("SPEC_RUNNER_LIVENESS_HARD_CAP_MS", args[arg_index + 1].clone());
                arg_index += 2;
            }
            "--liveness-kill-grace-ms" => {
                if arg_index + 1 >= args.len() {
                    eprintln!("ERROR: --liveness-kill-grace-ms requires value");
                    process::exit(2);
                }
                std::env::set_var("SPEC_RUNNER_LIVENESS_KILL_GRACE_MS", args[arg_index + 1].clone());
                arg_index += 2;
            }
            _ => break,
        }
    }
    debug_log_at(2, &format!("main:debug-level={}", debug_level()));
    if args.len() <= arg_index {
        eprintln!("ERROR: missing runner adapter subcommand");
        process::exit(2);
    }

    let subcommand = args[arg_index].clone();
    let forwarded: Vec<String> = args[(arg_index + 1)..].to_vec();
    debug_log(&format!(
        "main:subcommand_parsed subcommand={} forwarded={}",
        subcommand,
        forwarded.len()
    ));

    let root = match find_repo_root() {
        Ok(p) => p,
        Err(msg) => {
            eprintln!("ERROR: {msg}");
            process::exit(1);
        }
    };
    debug_log("main:repo_root_resolved");
    if let Ok(mut guard) = profiler_cell().lock() {
        let opts = profile_options_from_env(&subcommand, &forwarded);
        *guard = Some(RunProfiler::from_options(&opts));
    }
    let dispatch_span = profiler_start_span(
        "runner.dispatch",
        "runner",
        "runner.dispatch",
        None,
        json!({"subcommand": subcommand, "forwarded_count": forwarded.len()}),
    );

    let py = python_path(&root);
    let ruff = tool_path(&root, "ruff");
    let mypy = tool_path(&root, "mypy");
    let pytest = tool_path(&root, "pytest");
    debug_log_at(2, &format!(
        "main:tool-paths py={} ruff={} mypy={} pytest={}",
        py, ruff, mypy, pytest
    ));

    let code = match subcommand.as_str() {
        "spec-eval" => run_spec_eval_native(&root, &forwarded),
        "spec-ref" => {
            if forwarded.len() != 1 {
                eprintln!("usage: spec-ref <subcommand>");
                2
            } else {
                run_spec_ref_print(&forwarded[0])
            }
        }
        "validate-report" => run_validate_report_native(&root, &forwarded),
        "governance" => run_cmd(
            &py,
            &with_forwarded(vec![script(&root, "run_governance_specs.py")], &forwarded),
            &root,
        ),
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
            &with_forwarded(
                vec![script(&root, "normalize_repo.py"), "--check".to_string()],
                &forwarded,
            ),
            &root,
        ),
        "normalize-fix" => run_cmd(
            &py,
            &with_forwarded(
                vec![script(&root, "normalize_repo.py"), "--write".to_string()],
                &forwarded,
            ),
            &root,
        ),
        "schema-registry-check" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    "-m".to_string(),
                    "spec_runner.spec_lang_commands".to_string(),
                    "schema-registry-report".to_string(),
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
                    "-m".to_string(),
                    "spec_runner.spec_lang_commands".to_string(),
                    "schema-registry-report".to_string(),
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
            &with_forwarded(
                vec![
                    script(&root, "generate_schema_docs.py"),
                    "--check".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "schema-docs-build" => run_cmd(
            &py,
            &with_forwarded(vec![script(&root, "generate_schema_docs.py")], &forwarded),
            &root,
        ),
        "lint" => run_cmd(
            &ruff,
            &with_forwarded(vec!["check".to_string(), ".".to_string()], &forwarded),
            &root,
        ),
        "typecheck" => run_cmd(
            &mypy,
            &with_forwarded(vec!["spec_runner".to_string()], &forwarded),
            &root,
        ),
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
                    "-m".to_string(),
                    "spec_runner.spec_lang_commands".to_string(),
                    "spec-lang-stdlib-report".to_string(),
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
                    "-m".to_string(),
                    "spec_runner.spec_lang_commands".to_string(),
                    "spec-lang-stdlib-report".to_string(),
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
            &with_forwarded(
                vec![script(&root, "docs_generate_all.py"), "--build".to_string()],
                &forwarded,
            ),
            &root,
        ),
        "docs-generate-check" => run_cmd(
            &py,
            &with_forwarded(
                vec![script(&root, "docs_generate_all.py"), "--check".to_string()],
                &forwarded,
            ),
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
        "docs-lint" => run_cmd(
            &py,
            &with_forwarded(
                vec![
                    "-m".to_string(),
                    "spec_runner.spec_lang_commands".to_string(),
                    "docs-lint".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
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
    profiler_finish_span(
        dispatch_span.as_deref(),
        if code == 0 { "ok" } else { "error" },
        if code == 0 {
            None
        } else {
            Some(json!({"category":"runtime","message":format!("subcommand {} failed with {}", subcommand, code)}))
        },
    );
    if let Ok(mut guard) = profiler_cell().lock() {
        if let Some(prof) = guard.as_mut() {
            let out_path = std::env::var("SPEC_RUNNER_PROFILE_OUT")
                .unwrap_or_else(|_| "/.artifacts/run-trace.json".to_string());
            let summary_out = std::env::var("SPEC_RUNNER_PROFILE_SUMMARY_OUT")
                .unwrap_or_else(|_| "/.artifacts/run-trace-summary.md".to_string());
            prof.close(
                if code == 0 { "pass" } else { "fail" },
                code,
                &root,
                &out_path,
                &summary_out,
            );
        }
    }

    process::exit(code);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn parse_spec_ref_accepts_path_and_fragment() {
        let got = parse_spec_ref("/docs/spec/example.spec.md#CASE-1").expect("parse");
        assert_eq!(got.0, "/docs/spec/example.spec.md");
        assert_eq!(got.1.as_deref(), Some("CASE-1"));
    }

    #[test]
    fn parse_spec_ref_accepts_path_only() {
        let got = parse_spec_ref("/docs/spec/example.spec.md").expect("parse");
        assert_eq!(got.0, "/docs/spec/example.spec.md");
        assert!(got.1.is_none());
    }

    #[test]
    fn parse_spec_ref_rejects_empty_fragment() {
        let err = parse_spec_ref("/docs/spec/example.spec.md#").expect_err("expected error");
        assert!(err.contains("empty case id fragment"));
    }

    #[test]
    fn parse_spec_ref_rejects_empty_path() {
        let err = parse_spec_ref("#CASE-1").expect_err("expected error");
        assert!(err.contains("must include path"));
    }

    #[test]
    fn extract_spec_test_blocks_finds_tagged_yaml_blocks() {
        let md = r#"
before
```yaml spec-test
id: CASE-1
type: governance.check
```
middle
```yaml
id: NOT-A-SPEC
```
```yaml spec-test
id: CASE-2
```
after
"#;
        let blocks = extract_spec_test_blocks(md);
        assert_eq!(blocks.len(), 2);
        assert!(blocks[0].contains("id: CASE-1"));
        assert!(blocks[1].contains("id: CASE-2"));
    }

    #[test]
    fn block_id_extracts_id() {
        let block = "id: SRTEST-001\ncheck: runtime.foo\n";
        assert_eq!(block_id(block).as_deref(), Some("SRTEST-001"));
    }

    #[test]
    fn command_spec_ref_has_validate_report_mapping() {
        let got = command_spec_ref("validate-report");
        assert!(got.is_some());
        assert!(got.expect("mapping").contains("#"));
    }

    #[test]
    fn run_spec_ref_print_returns_nonzero_for_unknown() {
        let code = run_spec_ref_print("unknown-command");
        assert_ne!(code, 0);
    }
}

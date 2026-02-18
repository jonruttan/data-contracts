mod spec_lang;
mod profiler;
mod governance;

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
use governance::{run_critical_gate_native, run_governance_broad_native};

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

fn env_bool(name: &str, default_value: bool) -> bool {
    let raw = std::env::var(name).unwrap_or_default();
    let normalized = raw.trim().to_ascii_lowercase();
    if normalized.is_empty() {
        return default_value;
    }
    if matches!(normalized.as_str(), "1" | "true" | "yes" | "on") {
        return true;
    }
    if matches!(normalized.as_str(), "0" | "false" | "no" | "off") {
        return false;
    }
    default_value
}

fn profile_level_or_off(raw: &str) -> String {
    let lvl = raw.trim().to_ascii_lowercase();
    if matches!(lvl.as_str(), "off" | "basic" | "detailed" | "debug") {
        lvl
    } else {
        "off".to_string()
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

fn runner_command_with_liveness(
    runner_bin: &str,
    runner_impl: &str,
    subcommand: &str,
    level: &str,
    stall_ms: &str,
    kill_grace_ms: &str,
    hard_cap_ms: &str,
) -> Vec<String> {
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
            "--liveness-level".to_string(),
            level.to_string(),
            "--liveness-stall-ms".to_string(),
            stall_ms.to_string(),
            "--liveness-kill-grace-ms".to_string(),
            kill_grace_ms.to_string(),
            "--liveness-hard-cap-ms".to_string(),
            hard_cap_ms.to_string(),
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
    let mut fail_fast = env_bool("SPEC_RUNNER_FAIL_FAST", true);
    let mut include_critical = false;
    let mut profile_on_fail = profile_level_or_off(
        env::var("SPEC_RUNNER_PROFILE_ON_FAIL")
            .unwrap_or_else(|_| "basic".to_string())
            .as_str(),
    );

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
        if arg == "--fail-fast" {
            fail_fast = true;
            i += 1;
            continue;
        }
        if arg == "--continue-on-fail" {
            fail_fast = false;
            i += 1;
            continue;
        }
        if arg == "--profile-on-fail" {
            if i + 1 >= forwarded.len() {
                eprintln!("ERROR: --profile-on-fail requires value");
                return 2;
            }
            profile_on_fail = profile_level_or_off(&forwarded[i + 1]);
            i += 2;
            continue;
        }
        if arg == "--include-critical" {
            include_critical = true;
            i += 1;
            continue;
        }
        eprintln!("ERROR: unsupported ci-gate-summary arg: {arg}");
        return 2;
    }

    let broad_liveness_level =
        env::var("SPEC_CI_GOV_BROAD_LIVENESS_LEVEL").unwrap_or_else(|_| "strict".to_string());
    let broad_liveness_stall_ms =
        env::var("SPEC_CI_GOV_BROAD_LIVENESS_STALL_MS").unwrap_or_else(|_| "5000".to_string());
    let broad_liveness_kill_grace_ms = env::var("SPEC_CI_GOV_BROAD_LIVENESS_KILL_GRACE_MS")
        .unwrap_or_else(|_| "1000".to_string());
    let broad_liveness_hard_cap_ms =
        env::var("SPEC_CI_GOV_BROAD_LIVENESS_HARD_CAP_MS").unwrap_or_else(|_| "120000".to_string());
    let include_critical = include_critical || env_bool("SPEC_CI_GATE_INCLUDE_CRITICAL", false);
    let skip_critical = env_bool("SPEC_CI_GATE_SKIP_CRITICAL", !include_critical);

    let mut default_steps: Vec<(&str, Vec<String>)> = Vec::new();
    if include_critical && !skip_critical {
        default_steps.push((
            "governance_critical",
            runner_command(&runner_bin, &runner_impl, "critical-gate"),
        ));
    }
    default_steps.extend(vec![
        (
            "governance_broad",
            runner_command_with_liveness(
                &runner_bin,
                &runner_impl,
                "governance-broad-native",
                &broad_liveness_level,
                &broad_liveness_stall_ms,
                &broad_liveness_kill_grace_ms,
                &broad_liveness_hard_cap_ms,
            ),
        ),
        (
            "docs_generate_check",
            runner_command(&runner_bin, &runner_impl, "docs-generate-check"),
        ),
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
            "conformance_parity",
            runner_command(&runner_bin, &runner_impl, "conformance-parity"),
        ),
        (
            "pytest",
            runner_command(&runner_bin, &runner_impl, "test-full"),
        ),
    ]);

    let started = now_iso_utc_fallback();
    let t0 = Instant::now();
    let mut steps = Vec::<Value>::new();
    let mut events = Vec::<Value>::new();
    let mut first_failure_step: Option<String> = None;
    let mut aborted = false;
    for (name, command) in default_steps {
        if aborted {
            steps.push(json!({
                "name": name,
                "command": command,
                "status": "skipped",
                "exit_code": Value::Null,
                "duration_ms": 0,
                "skip_reason": "fail_fast.after_failure",
                "blocked_by": first_failure_step.clone(),
            }));
            events.push(json!({
                "ts_ns": t0.elapsed().as_nanos() as i64,
                "kind": "checkpoint",
                "span_id": "run.total",
                "attrs": {"event":"gate.step.skipped","step":name,"blocked_by":first_failure_step.clone()}
            }));
            continue;
        }
        events.push(json!({
            "ts_ns": t0.elapsed().as_nanos() as i64,
            "kind": "checkpoint",
            "span_id": "run.total",
            "attrs": {"event":"gate.step.start","step":name}
        }));
        println!("[gate] {name}: {}", command.join(" "));
        let step_start = Instant::now();
        let code = run_command_capture_code(&command, root);
        let duration_ms = step_start.elapsed().as_millis() as i64;
        let status = if code == 0 { "pass" } else { "fail" };
        let mut step_row = json!({
            "name": name,
            "command": command,
            "status": status,
            "exit_code": code,
            "duration_ms": duration_ms,
        });
        if name == "governance_critical" {
            if let Some(dst) = step_row.as_object_mut() {
                dst.insert("triage_phase".to_string(), Value::String("critical".to_string()));
            }
        } else if name == "governance_broad" {
            if let Some(dst) = step_row.as_object_mut() {
                dst.insert("triage_phase".to_string(), Value::String("broad".to_string()));
                dst.insert("broad_required".to_string(), Value::Bool(true));
            }
        }
        steps.push(step_row);
        events.push(json!({
            "ts_ns": t0.elapsed().as_nanos() as i64,
            "kind": "checkpoint",
            "span_id": "run.total",
            "attrs": {"event":format!("gate.step.{}", status),"step":name,"exit_code":code}
        }));
        if status == "fail" && first_failure_step.is_none() {
            first_failure_step = Some(name.to_string());
            if fail_fast {
                aborted = true;
                events.push(json!({
                    "ts_ns": t0.elapsed().as_nanos() as i64,
                    "kind": "checkpoint",
                    "span_id": "run.total",
                    "attrs": {"event":"gate.fail_fast.abort","after_step":name}
                }));
            }
        }
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
    let skipped_step_count = steps
        .iter()
        .filter(|x| x.get("status").and_then(Value::as_str) == Some("skipped"))
        .count();
    let first_failure_for_payload = first_failure_step.clone();
    let aborted_after_for_payload = if fail_fast {
        first_failure_step.clone()
    } else {
        None
    };
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
        "events": events,
        "fail_fast_enabled": fail_fast,
        "first_failure_step": first_failure_for_payload,
        "aborted_after_step": aborted_after_for_payload,
        "skipped_step_count": skipped_step_count,
        "runner_bin": runner_bin,
        "runner_impl": runner_impl,
        "unit_test_opt_out": collect_unit_test_opt_out(root),
    });
    let mut payload = payload;
    let governance_step_value = payload
        .get("steps")
        .and_then(Value::as_array)
        .and_then(|steps_arr| {
            steps_arr
                .iter()
                .find(|s| s.get("name").and_then(Value::as_str) == Some("governance_broad"))
                .cloned()
        });
    if let Some(governance_step) = governance_step_value {
        if let Some(obj) = payload.as_object_mut() {
            obj.insert(
                "triage_attempted".to_string(),
                governance_step
                    .get("triage_attempted")
                    .cloned()
                    .unwrap_or(Value::Bool(false)),
            );
            obj.insert(
                "triage_mode".to_string(),
                governance_step
                    .get("triage_mode")
                    .cloned()
                    .unwrap_or(Value::String("not_run".to_string())),
            );
            obj.insert(
                "triage_result".to_string(),
                governance_step
                    .get("triage_result")
                    .cloned()
                    .unwrap_or(Value::String("not_run".to_string())),
            );
            obj.insert(
                "failing_check_ids".to_string(),
                governance_step
                    .get("failing_check_ids")
                    .cloned()
                    .unwrap_or(Value::Array(vec![])),
            );
            obj.insert(
                "failing_check_prefixes".to_string(),
                governance_step
                    .get("failing_check_prefixes")
                    .cloned()
                    .unwrap_or(Value::Array(vec![])),
            );
            obj.insert(
                "stall_detected".to_string(),
                governance_step
                    .get("stall_detected")
                    .cloned()
                    .unwrap_or(Value::Bool(false)),
            );
            obj.insert(
                "stall_phase".to_string(),
                governance_step.get("stall_phase").cloned().unwrap_or(Value::Null),
            );
        }
    }

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
            "events": payload.get("events").cloned().unwrap_or(Value::Array(vec![])),
            "fail_fast_enabled": payload.get("fail_fast_enabled").cloned().unwrap_or(Value::Bool(false)),
            "first_failure_step": payload.get("first_failure_step").cloned().unwrap_or(Value::Null),
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
    if exit_code != 0 && profile_on_fail != "off" {
        let run_trace_path = root.join(".artifacts/run-trace.json");
        let run_summary_path = root.join(".artifacts/run-trace-summary.md");
        if let Some(parent) = run_trace_path.parent() {
            let _ = fs::create_dir_all(parent);
        }
        if let Some(parent) = run_summary_path.parent() {
            let _ = fs::create_dir_all(parent);
        }
        let fail_profile_payload = json!({
            "version": 1,
            "run_id": format!("gate-{}", SystemTime::now().duration_since(UNIX_EPOCH).map(|d| d.as_millis()).unwrap_or(0)),
            "runner_impl": payload.get("runner_impl").cloned().unwrap_or(Value::Null),
            "started_at": payload.get("started_at").cloned().unwrap_or(Value::Null),
            "ended_at": payload.get("finished_at").cloned().unwrap_or(Value::Null),
            "status": payload.get("status").cloned().unwrap_or(Value::Null),
            "command": "ci-gate-summary",
            "args": [],
            "env_profile": {},
            "spans": [{
                "span_id":"s1",
                "parent_span_id": Value::Null,
                "kind":"run",
                "name":"run.total",
                "phase":"run.total",
                "start_ns":0,
                "end_ns": payload.get("total_duration_ms").and_then(Value::as_i64).unwrap_or(0) * 1_000_000,
                "duration_ms": payload.get("total_duration_ms").and_then(Value::as_i64).unwrap_or(0),
                "status": if exit_code == 0 { "ok" } else { "error" },
                "attrs": {"source":"ci-gate-summary"},
                "error": Value::Null
            }],
            "events": payload.get("events").cloned().unwrap_or(Value::Array(vec![])),
            "summary": {
                "step_count": payload.get("steps").and_then(Value::as_array).map(|x| x.len()).unwrap_or(0),
                "failed_step": payload.get("first_failure_step").cloned().unwrap_or(Value::Null)
            }
        });
        let _ = fs::write(
            &run_trace_path,
            format!(
                "{}\n",
                serde_json::to_string_pretty(&fail_profile_payload).unwrap_or_else(|_| "{}".to_string())
            ),
        );
        let mut summary_md = String::new();
        summary_md.push_str("# Run Trace Summary\n\n");
        summary_md.push_str(&format!(
            "- status: `{}`\n",
            payload.get("status").and_then(Value::as_str).unwrap_or("unknown")
        ));
        summary_md.push_str(&format!(
            "- first_failure_step: `{}`\n",
            payload.get("first_failure_step").and_then(Value::as_str).unwrap_or("")
        ));
        summary_md.push_str(&format!(
            "- skipped_step_count: `{}`\n\n",
            payload.get("skipped_step_count").and_then(Value::as_u64).unwrap_or(0)
        ));
        summary_md.push_str("## Suggested Next Command\n\n");
        summary_md.push_str("- `spec_runner_cli --profile-level detailed ci-gate-summary`\n");
        let _ = fs::write(&run_summary_path, summary_md);
        println!("[gate] profile: {}", run_trace_path.display());
        println!("[gate] profile-summary: {}", run_summary_path.display());
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
        "critical-gate" => run_critical_gate_native(&root, &forwarded),
        "governance-broad-native" => run_governance_broad_native(&root, &forwarded),
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

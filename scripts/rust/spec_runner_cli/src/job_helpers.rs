use serde_json::{json, Map, Value};
use std::fs;
use std::path::{Path, PathBuf};

fn as_str<'a>(v: &'a Value, key: &str) -> Result<&'a str, String> {
    v.get(key)
        .and_then(|x| x.as_str())
        .ok_or_else(|| format!("helper payload missing string key: {key}"))
}

fn as_bool(v: &Value, key: &str, default_value: bool) -> bool {
    v.get(key).and_then(|x| x.as_bool()).unwrap_or(default_value)
}

fn resolve(root: &Path, raw: &str) -> PathBuf {
    let trimmed = raw.trim();
    if trimmed.starts_with('/') {
        root.join(trimmed.trim_start_matches('/'))
    } else {
        root.join(trimmed)
    }
}

fn helper_docs_render_template(payload: &Value) -> Result<Value, String> {
    let template = as_str(payload, "template")?;
    let values = payload
        .get("values")
        .and_then(|v| v.as_object())
        .ok_or_else(|| "helper.docs.render_template requires object key `values`".to_string())?;
    let mut out = template.to_string();
    for (k, v) in values {
        let token = format!("{{{{{}}}}}", k);
        let repl = if let Some(s) = v.as_str() {
            s.to_string()
        } else {
            v.to_string()
        };
        out = out.replace(&token, &repl);
    }
    Ok(json!({"rendered": out}))
}

fn helper_docs_catalog_generate(payload: &Value) -> Result<Value, String> {
    let title = payload
        .get("title")
        .and_then(|v| v.as_str())
        .unwrap_or("Catalog");
    let headers = payload
        .get("headers")
        .and_then(|v| v.as_array())
        .ok_or_else(|| "helper.docs.catalog_generate requires list key `headers`".to_string())?;
    let rows = payload
        .get("rows")
        .and_then(|v| v.as_array())
        .ok_or_else(|| "helper.docs.catalog_generate requires list key `rows`".to_string())?;

    let mut md = String::new();
    md.push_str("# ");
    md.push_str(title);
    md.push_str("\n\n");
    md.push('|');
    for h in headers {
        md.push(' ');
        md.push_str(h.as_str().unwrap_or(""));
        md.push(' ');
        md.push('|');
    }
    md.push('\n');
    md.push('|');
    for _ in headers {
        md.push_str("---|");
    }
    md.push('\n');
    for row in rows {
        md.push('|');
        if let Some(cols) = row.as_array() {
            for c in cols {
                let val = c
                    .as_str()
                    .map(|s| s.to_string())
                    .unwrap_or_else(|| c.to_string());
                md.push(' ');
                md.push_str(&val.replace('|', "\\|"));
                md.push(' ');
                md.push('|');
            }
        }
        md.push('\n');
    }
    Ok(json!({"markdown": md}))
}

fn helper_schema_compile_registry(root: &Path, payload: &Value) -> Result<Value, String> {
    let rel = payload
        .get("path")
        .and_then(|v| v.as_str())
        .unwrap_or("/docs/spec/schema/registry/v1");
    let base = resolve(root, rel);
    if !base.exists() {
        return Err(format!("schema registry path does not exist: {}", base.display()));
    }
    let mut files = Vec::<String>::new();
    let mut yaml_file_count = 0_i64;
    let entries = fs::read_dir(&base).map_err(|e| format!("failed to read {}: {e}", base.display()))?;
    for entry in entries.flatten() {
        let p = entry.path();
        if !p.is_file() {
            continue;
        }
        let ext = p.extension().and_then(|s| s.to_str()).unwrap_or("");
        if ext == "yaml" || ext == "yml" {
            yaml_file_count += 1;
        }
        files.push(p.to_string_lossy().to_string());
    }
    files.sort();
    Ok(json!({
        "path": base.to_string_lossy().to_string(),
        "yaml_file_count": yaml_file_count,
        "files": files,
    }))
}

fn helper_parity_compare_conformance(root: &Path, payload: &Value) -> Result<Value, String> {
    let left_path = resolve(root, as_str(payload, "left")?);
    let right_path = resolve(root, as_str(payload, "right")?);
    let left_raw =
        fs::read_to_string(&left_path).map_err(|e| format!("failed to read {}: {e}", left_path.display()))?;
    let right_raw =
        fs::read_to_string(&right_path).map_err(|e| format!("failed to read {}: {e}", right_path.display()))?;
    let left_json: Value = serde_json::from_str(&left_raw)
        .map_err(|e| format!("failed to parse {} as json: {e}", left_path.display()))?;
    let right_json: Value = serde_json::from_str(&right_raw)
        .map_err(|e| format!("failed to parse {} as json: {e}", right_path.display()))?;
    Ok(json!({
        "equal": left_json == right_json,
        "left_path": left_path.to_string_lossy().to_string(),
        "right_path": right_path.to_string_lossy().to_string()
    }))
}

fn helper_normalize_apply_edits(root: &Path, payload: &Value) -> Result<Value, String> {
    let rel = as_str(payload, "path")?;
    let write = as_bool(payload, "write", false);
    let path = resolve(root, rel);
    let mut text =
        fs::read_to_string(&path).map_err(|e| format!("failed to read {}: {e}", path.display()))?;
    let mut applied = 0_i64;
    let edits = payload
        .get("edits")
        .and_then(|v| v.as_array())
        .ok_or_else(|| "helper.normalize.apply_edits requires list key `edits`".to_string())?;
    for edit in edits {
        let from = edit
            .get("from")
            .and_then(|v| v.as_str())
            .ok_or_else(|| "edit requires string key `from`".to_string())?;
        let to = edit
            .get("to")
            .and_then(|v| v.as_str())
            .ok_or_else(|| "edit requires string key `to`".to_string())?;
        if text.contains(from) {
            text = text.replace(from, to);
            applied += 1;
        }
    }
    if write {
        fs::write(&path, &text).map_err(|e| format!("failed to write {}: {e}", path.display()))?;
    }
    Ok(json!({
        "path": path.to_string_lossy().to_string(),
        "write": write,
        "applied_count": applied,
        "text": text,
    }))
}

fn helper_governance_scan_bundle(root: &Path, payload: &Value) -> Result<Value, String> {
    let rel = payload
        .get("path")
        .and_then(|v| v.as_str())
        .unwrap_or("/docs/spec");
    let patterns = payload
        .get("patterns")
        .and_then(|v| v.as_array())
        .ok_or_else(|| "helper.governance.scan_bundle requires list key `patterns`".to_string())?;
    let base = resolve(root, rel);
    if !base.exists() {
        return Err(format!("scan path does not exist: {}", base.display()));
    }

    let mut counts = Map::<String, Value>::new();
    for pat in patterns {
        if let Some(p) = pat.as_str() {
            counts.insert(p.to_string(), Value::Number(0_i64.into()));
        }
    }
    let mut scanned_files = 0_i64;
    let mut stack = vec![base];
    while let Some(cur) = stack.pop() {
        let rd = match fs::read_dir(&cur) {
            Ok(x) => x,
            Err(_) => continue,
        };
        for entry in rd.flatten() {
            let p = entry.path();
            if p.is_dir() {
                stack.push(p);
                continue;
            }
            if !p.is_file() {
                continue;
            }
            scanned_files += 1;
            let text = fs::read_to_string(&p).unwrap_or_default();
            for pat in patterns {
                if let Some(key) = pat.as_str() {
                    if text.contains(key) {
                        let cur_n = counts.get(key).and_then(|v| v.as_i64()).unwrap_or(0);
                        counts.insert(key.to_string(), Value::Number((cur_n + 1).into()));
                    }
                }
            }
        }
    }
    Ok(json!({
        "scanned_files": scanned_files,
        "counts": counts,
    }))
}

fn helper_report_emit(root: &Path, payload: &Value) -> Result<Value, String> {
    let report = payload
        .get("report_name")
        .and_then(|v| v.as_str())
        .unwrap_or("report");
    let format = payload
        .get("format")
        .and_then(|v| v.as_str())
        .unwrap_or("json");
    let out = payload
        .get("out")
        .and_then(|v| v.as_str())
        .ok_or_else(|| "helper.report.emit requires string key `out`".to_string())?;
    let out_path = resolve(root, out);
    if let Some(parent) = out_path.parent() {
        let _ = fs::create_dir_all(parent);
    }
    let now = std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .map(|d| d.as_secs().to_string())
        .unwrap_or_else(|_| "0".to_string());
    if format == "md" {
        let mut body = String::new();
        body.push_str("# ");
        body.push_str(report);
        body.push_str(" summary\n\n");
        body.push_str("- status: `ok`\n");
        body.push_str("- generated_by: `rust.job`\n");
        body.push_str("- generated_at: `");
        body.push_str(&now);
        body.push_str("`\n");
        fs::write(&out_path, body)
            .map_err(|e| format!("failed writing {}: {e}", out_path.display()))?;
    } else {
        let payload = json!({
            "version": 1,
            "report": report,
            "status": "ok",
            "generated_by": "rust.job",
            "generated_at": now,
        });
        fs::write(
            &out_path,
            format!(
                "{}\n",
                serde_json::to_string_pretty(&payload).unwrap_or_else(|_| "{}".to_string())
            ),
        )
        .map_err(|e| format!("failed writing {}: {e}", out_path.display()))?;
    }
    Ok(json!({
        "written_path": out_path.to_string_lossy().to_string(),
        "format": format,
        "report_name": report,
        "ok": true
    }))
}

pub fn run_helper(root: &Path, helper_id: &str, payload: &Value) -> Result<Value, String> {
    match helper_id {
        "helper.docs.render_template" => helper_docs_render_template(payload),
        "helper.docs.catalog_generate" => helper_docs_catalog_generate(payload),
        "helper.schema.compile_registry" => helper_schema_compile_registry(root, payload),
        "helper.parity.compare_conformance" => helper_parity_compare_conformance(root, payload),
        "helper.normalize.apply_edits" => helper_normalize_apply_edits(root, payload),
        "helper.governance.scan_bundle" => helper_governance_scan_bundle(root, payload),
        "helper.report.emit" => helper_report_emit(root, payload),
        _ => Err(format!("unsupported helper id: {helper_id}")),
    }
}

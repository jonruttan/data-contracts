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

fn is_executable(path: &Path) -> bool {
    path.exists() && path.is_file()
}

fn resolve_python_bin(root: &Path) -> String {
    if let Ok(v) = env::var("PYTHON_BIN") {
        let s = v.trim();
        if !s.is_empty() {
            return s.to_string();
        }
    }

    let local = root.join(".venv/bin/python");
    if is_executable(&local) {
        return local.to_string_lossy().to_string();
    }

    let parent_local = root.join("../../.venv/bin/python");
    if is_executable(&parent_local) {
        return parent_local.to_string_lossy().to_string();
    }

    "python3".to_string()
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

fn rust_unimplemented(subcommand: &str) -> i32 {
    eprintln!(
        "ERROR: rust runner adapter subcommand not yet implemented in spec_runner_cli: {subcommand}"
    );
    2
}

fn with_forwarded(base: Vec<String>, forwarded: &[String]) -> Vec<String> {
    base.into_iter()
        .chain(forwarded.iter().cloned())
        .collect::<Vec<_>>()
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

    let python_bin = resolve_python_bin(&root);

    let code = match subcommand.as_str() {
        "governance" => run_cmd(
            &python_bin,
            &with_forwarded(vec!["scripts/run_governance_specs.py".to_string()], &forwarded),
            &root,
        ),
        "style-check" => run_cmd(
            &python_bin,
            &with_forwarded(
                vec![
                    "scripts/evaluate_style.py".to_string(),
                    "--check".to_string(),
                    "docs/spec".to_string(),
                ],
                &forwarded,
            ),
            &root,
        ),
        "test-core" => run_cmd(
            &python_bin,
            &with_forwarded(
                vec![
                    "-m".to_string(),
                    "pytest".to_string(),
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
        "lint"
        | "typecheck"
        | "compilecheck"
        | "conformance-purpose-json"
        | "conformance-purpose-md"
        | "spec-portability-json"
        | "spec-portability-md"
        | "docs-build"
        | "docs-build-check"
        | "docs-lint"
        | "docs-graph"
        | "conformance-parity"
        | "test-full" => rust_unimplemented(&subcommand),
        _ => {
            eprintln!("ERROR: unsupported runner adapter subcommand: {subcommand}");
            2
        }
    };

    process::exit(code);
}

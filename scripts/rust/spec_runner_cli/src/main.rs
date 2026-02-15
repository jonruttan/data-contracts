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

    let shell_adapter = root.join("scripts/runner_adapter.sh");
    let shell_adapter_str = shell_adapter.to_string_lossy().to_string();

    let code = match subcommand.as_str() {
        "governance"
        | "style-check"
        | "lint"
        | "typecheck"
        | "compilecheck"
        | "conformance-purpose-json"
        | "conformance-purpose-md"
        | "spec-portability-json"
        | "spec-portability-md"
        | "spec-lang-adoption-json"
        | "spec-lang-adoption-md"
        | "runner-independence-json"
        | "runner-independence-md"
        | "docs-operability-json"
        | "docs-operability-md"
        | "contract-assertions-json"
        | "contract-assertions-md"
        | "objective-scorecard-json"
        | "objective-scorecard-md"
        | "ci-gate-summary"
        | "docs-build"
        | "docs-build-check"
        | "docs-lint"
        | "docs-graph"
        | "conformance-parity"
        | "test-core"
        | "test-full" => run_cmd(
            &shell_adapter_str,
            &with_forwarded(vec![subcommand.clone()], &forwarded),
            &root,
        ),
        _ => {
            eprintln!("ERROR: unsupported runner adapter subcommand: {subcommand}");
            2
        }
    };

    process::exit(code);
}

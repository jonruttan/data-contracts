use std::collections::HashMap;
use std::env as std_env;
use std::process::Command;
use std::thread;
use std::time::Duration;

use serde_json::{Map, Number, Value};

#[derive(Clone, Debug)]
pub enum Expr {
    Lit(Value),
    Var(String),
    Op { name: String, args: Vec<Expr> },
}

#[derive(Clone, Debug)]
enum RuntimeValue {
    Json(Value),
    Closure(Closure),
}

#[derive(Clone, Debug)]
struct Closure {
    params: Vec<String>,
    body: Box<Expr>,
    env: Env,
}

#[derive(Clone, Debug, Default)]
struct RuntimeContext {
    capabilities: std::collections::HashSet<String>,
    last_exit_code: Option<i64>,
}

#[derive(Clone, Debug, Default)]
struct Env {
    vars: HashMap<String, RuntimeValue>,
}

impl Env {
    fn with_parent(&self, bindings: HashMap<String, RuntimeValue>) -> Self {
        let mut out = self.clone();
        for (k, v) in bindings {
            out.vars.insert(k, v);
        }
        out
    }

    fn lookup(&self, key: &str) -> Option<RuntimeValue> {
        self.vars.get(key).cloned()
    }
}

#[derive(Clone, Debug)]
pub struct EvalLimits {
    pub max_steps: usize,
}

impl Default for EvalLimits {
    fn default() -> Self {
        Self { max_steps: 20_000 }
    }
}

#[derive(Debug)]
pub struct EvalError {
    pub message: String,
}

impl EvalError {
    fn new(message: impl Into<String>) -> Self {
        Self {
            message: message.into(),
        }
    }
}

type EvalResult<T> = Result<T, EvalError>;

pub fn compile_mapping_ast(node: &Value) -> EvalResult<Expr> {
    match node {
        Value::Null | Value::Bool(_) | Value::Number(_) | Value::String(_) => {
            Ok(Expr::Lit(node.clone()))
        }
        Value::Array(_) => Err(EvalError::new(
            "list expressions are not allowed; use mapping-AST and wrap literal lists with lit",
        )),
        Value::Object(map) => compile_mapping_expr(map),
    }
}

fn compile_mapping_expr(map: &Map<String, Value>) -> EvalResult<Expr> {
    if map.is_empty() {
        return Err(EvalError::new("expression mapping must not be empty"));
    }
    if map.contains_key("lit") {
        if map.len() != 1 {
            return Err(EvalError::new(
                "lit wrapper must be the only key in a mapping",
            ));
        }
        return Ok(Expr::Lit(map.get("lit").cloned().unwrap_or(Value::Null)));
    }
    if map.len() != 1 {
        return Err(EvalError::new(
            "expression mapping must have exactly one operator key",
        ));
    }
    let (name, raw_args) = map
        .iter()
        .next()
        .ok_or_else(|| EvalError::new("expression mapping must not be empty"))?;
    if name == "var" {
        let symbol = raw_args
            .as_str()
            .ok_or_else(|| EvalError::new("var requires non-empty string variable name"))?
            .trim()
            .to_string();
        if symbol.is_empty() {
            return Err(EvalError::new(
                "var requires non-empty string variable name",
            ));
        }
        return Ok(Expr::Var(symbol));
    }
    let args = raw_args
        .as_array()
        .ok_or_else(|| EvalError::new(format!("{name} args must be a list")))?;
    let mut compiled = Vec::<Expr>::with_capacity(args.len());
    for arg in args {
        compiled.push(compile_mapping_ast(arg)?);
    }
    Ok(Expr::Op {
        name: name.clone(),
        args: compiled,
    })
}

pub fn eval_mapping_ast(
    node: &Value,
    subject: Value,
    symbols: HashMap<String, Value>,
    limits: EvalLimits,
) -> EvalResult<Value> {
    let expr = compile_mapping_ast(node)?;
    eval_expr(&expr, subject, symbols, limits)
}

pub fn eval_expr(
    expr: &Expr,
    subject: Value,
    symbols: HashMap<String, Value>,
    limits: EvalLimits,
) -> EvalResult<Value> {
    let mut runtime = RuntimeContext::default();
    runtime.capabilities = std_env::var("SPEC_RUNNER_SPEC_LANG_CAPABILITIES")
        .ok()
        .map(|raw| {
            raw.split(',')
                .map(str::trim)
                .filter(|s| !s.is_empty())
                .map(ToOwned::to_owned)
                .collect()
        })
        .unwrap_or_default();
    let mut env = Env::default();
    env.vars
        .insert("subject".to_string(), RuntimeValue::Json(subject.clone()));
    for (name, value) in symbols {
        let compiled = compile_mapping_ast(&value)?;
        let rv = match compiled {
            Expr::Op { name: op, args } if op == "fn" => compile_fn_expr(&args, &env)?,
            other => RuntimeValue::Json(eval_runtime(&other, &env, &limits, &mut 0, &mut runtime)?),
        };
        env.vars.insert(name, rv);
    }
    eval_runtime(expr, &env, &limits, &mut 0, &mut runtime)
}

fn eval_runtime(
    expr: &Expr,
    env: &Env,
    limits: &EvalLimits,
    steps: &mut usize,
    runtime: &mut RuntimeContext,
) -> EvalResult<Value> {
    *steps += 1;
    if *steps > limits.max_steps {
        return Err(EvalError::new("spec_lang budget exceeded: steps"));
    }
    match expr {
        Expr::Lit(v) => Ok(v.clone()),
        Expr::Var(name) => match env.lookup(name) {
            Some(RuntimeValue::Json(v)) => Ok(v),
            Some(RuntimeValue::Closure(_)) => Err(EvalError::new(format!(
                "variable {name} resolves to function; use call"
            ))),
            None => Err(EvalError::new(format!("undefined variable: {name}"))),
        },
        Expr::Op { name, args } => eval_op(name, args, env, limits, steps, runtime),
    }
}

fn eval_op(
    name: &str,
    args: &[Expr],
    env: &Env,
    limits: &EvalLimits,
    steps: &mut usize,
    runtime: &mut RuntimeContext,
) -> EvalResult<Value> {
    match name {
        "if" => {
            require_arity(name, args, 3)?;
            let cond = eval_runtime(&args[0], env, limits, steps, runtime)?;
            if truthy(&cond) {
                eval_runtime(&args[1], env, limits, steps, runtime)
            } else {
                eval_runtime(&args[2], env, limits, steps, runtime)
            }
        }
        "fn" => {
            let closure = compile_fn_expr(args, env)?;
            let RuntimeValue::Closure(c) = closure else {
                return Err(EvalError::new("fn compile produced non-closure"));
            };
            let mut obj = Map::new();
            obj.insert("__fn__".to_string(), Value::Bool(true));
            obj.insert(
                "__params__".to_string(),
                Value::Array(c.params.iter().cloned().map(Value::String).collect()),
            );
            Ok(Value::Object(obj))
        }
        "call" => {
            require_min_arity(name, args, 1)?;
            let target = eval_callable(&args[0], env, limits, steps, runtime)?;
            let mut values = Vec::<RuntimeValue>::new();
            for arg in &args[1..] {
                values.push(RuntimeValue::Json(eval_runtime(arg, env, limits, steps, runtime)?));
            }
            apply_callable(target, values, limits, steps, runtime)
        }
        "std.logic.eq" | "eq" => {
            require_arity(name, args, 2)?;
            let left = eval_runtime(&args[0], env, limits, steps, runtime)?;
            let right = eval_runtime(&args[1], env, limits, steps, runtime)?;
            Ok(Value::Bool(left == right))
        }
        "std.logic.neq" | "neq" => {
            require_arity(name, args, 2)?;
            let left = eval_runtime(&args[0], env, limits, steps, runtime)?;
            let right = eval_runtime(&args[1], env, limits, steps, runtime)?;
            Ok(Value::Bool(left != right))
        }
        "std.logic.and" | "and" => {
            require_min_arity(name, args, 1)?;
            for arg in args {
                let v = eval_runtime(arg, env, limits, steps, runtime)?;
                if !truthy(&v) {
                    return Ok(Value::Bool(false));
                }
            }
            Ok(Value::Bool(true))
        }
        "std.logic.or" | "or" => {
            require_min_arity(name, args, 1)?;
            for arg in args {
                let v = eval_runtime(arg, env, limits, steps, runtime)?;
                if truthy(&v) {
                    return Ok(Value::Bool(true));
                }
            }
            Ok(Value::Bool(false))
        }
        "std.logic.not" | "not" => {
            require_arity(name, args, 1)?;
            Ok(Value::Bool(!truthy(&eval_runtime(
                &args[0], env, limits, steps, runtime,
            )?)))
        }
        "std.object.get" | "get" => {
            require_arity(name, args, 2)?;
            let obj = eval_runtime(&args[0], env, limits, steps, runtime)?;
            let key = eval_runtime(&args[1], env, limits, steps, runtime)?;
            let Some(key_s) = key.as_str() else {
                return Err(EvalError::new("std.object.get key must be string"));
            };
            match obj {
                Value::Object(m) => Ok(m.get(key_s).cloned().unwrap_or(Value::Null)),
                _ => Ok(Value::Null),
            }
        }
        "std.type.is_list" | "is_list" => {
            require_arity(name, args, 1)?;
            let v = eval_runtime(&args[0], env, limits, steps, runtime)?;
            Ok(Value::Bool(v.is_array()))
        }
        "std.type.is_dict" | "is_dict" | "std.type.is_object" | "is_object" => {
            require_arity(name, args, 1)?;
            let v = eval_runtime(&args[0], env, limits, steps, runtime)?;
            Ok(Value::Bool(v.is_object()))
        }
        "std.type.is_string" | "is_string" => {
            require_arity(name, args, 1)?;
            let v = eval_runtime(&args[0], env, limits, steps, runtime)?;
            Ok(Value::Bool(v.is_string()))
        }
        "std.type.is_number" | "is_number" => {
            require_arity(name, args, 1)?;
            let v = eval_runtime(&args[0], env, limits, steps, runtime)?;
            Ok(Value::Bool(v.is_number()))
        }
        "std.type.is_bool" | "is_bool" | "std.type.is_boolean" | "is_boolean" => {
            require_arity(name, args, 1)?;
            let v = eval_runtime(&args[0], env, limits, steps, runtime)?;
            Ok(Value::Bool(v.is_boolean()))
        }
        "std.type.is_null" | "is_null" => {
            require_arity(name, args, 1)?;
            let v = eval_runtime(&args[0], env, limits, steps, runtime)?;
            Ok(Value::Bool(v.is_null()))
        }
        "std.string.contains" | "contains" => {
            require_arity(name, args, 2)?;
            let hay = eval_runtime(&args[0], env, limits, steps, runtime)?;
            let needle = eval_runtime(&args[1], env, limits, steps, runtime)?;
            let Some(hay_s) = hay.as_str() else {
                return Err(EvalError::new(
                    "std.string.contains haystack must be string",
                ));
            };
            let Some(needle_s) = needle.as_str() else {
                return Err(EvalError::new("std.string.contains needle must be string"));
            };
            Ok(Value::Bool(hay_s.contains(needle_s)))
        }
        "std.string.lower" | "lower" => {
            require_arity(name, args, 1)?;
            let v = eval_runtime(&args[0], env, limits, steps, runtime)?;
            let Some(s) = v.as_str() else {
                return Err(EvalError::new("std.string.lower expects string"));
            };
            Ok(Value::String(s.to_lowercase()))
        }
        "std.string.upper" | "upper" => {
            require_arity(name, args, 1)?;
            let v = eval_runtime(&args[0], env, limits, steps, runtime)?;
            let Some(s) = v.as_str() else {
                return Err(EvalError::new("std.string.upper expects string"));
            };
            Ok(Value::String(s.to_uppercase()))
        }
        "std.string.trim" | "trim" => {
            require_arity(name, args, 1)?;
            let v = eval_runtime(&args[0], env, limits, steps, runtime)?;
            let Some(s) = v.as_str() else {
                return Err(EvalError::new("std.string.trim expects string"));
            };
            Ok(Value::String(s.trim().to_string()))
        }
        "std.collection.count" | "count" | "len" => {
            require_arity(name, args, 1)?;
            let v = eval_runtime(&args[0], env, limits, steps, runtime)?;
            let n = match v {
                Value::Array(a) => a.len() as i64,
                Value::Object(o) => o.len() as i64,
                Value::String(s) => s.chars().count() as i64,
                _ => 0_i64,
            };
            Ok(Value::Number(Number::from(n)))
        }
        "std.collection.concat" | "concat" => {
            require_min_arity(name, args, 1)?;
            let mut out = Vec::<Value>::new();
            for arg in args {
                let v = eval_runtime(arg, env, limits, steps, runtime)?;
                let Value::Array(items) = v else {
                    return Err(EvalError::new("std.collection.concat expects list args"));
                };
                out.extend(items);
            }
            Ok(Value::Array(out))
        }
        "std.math.add" | "add" => numeric_fold(name, args, env, limits, steps, runtime, 0.0, |a, b| a + b),
        "std.math.sub" | "sub" => numeric_sub(name, args, env, limits, steps, runtime),
        "std.math.mul" | "mul" => numeric_fold(name, args, env, limits, steps, runtime, 1.0, |a, b| a * b),
        "std.math.div" | "div" => numeric_div(name, args, env, limits, steps, runtime),
        "ops.os.exec" => {
            require_arity(name, args, 2)?;
            require_ops_os(runtime, name)?;
            let cmd = eval_runtime(&args[0], env, limits, steps, runtime)?;
            let timeout_ms = eval_runtime(&args[1], env, limits, steps, runtime)?;
            let command = coerce_command(name, &cmd)?;
            let timeout = timeout_ms
                .as_i64()
                .ok_or_else(|| EvalError::new("spec_lang ops.os.exec expects integer timeout_ms"))?;
            if timeout < 0 {
                return Err(EvalError::new("spec_lang ops.os.exec expects non-negative timeout_ms"));
            }
            let mut proc = Command::new(&command[0]);
            if command.len() > 1 {
                proc.args(&command[1..]);
            }
            let status = proc.status().map_err(|e| EvalError::new(format!("ops.os.exec error: {e}")))?;
            let code = status.code().unwrap_or(-1) as i64;
            runtime.last_exit_code = Some(code);
            Ok(Value::Number(Number::from(code)))
        }
        "ops.os.exec_capture" => {
            require_arity(name, args, 2)?;
            require_ops_os(runtime, name)?;
            let cmd = eval_runtime(&args[0], env, limits, steps, runtime)?;
            let _timeout_ms = eval_runtime(&args[1], env, limits, steps, runtime)?;
            let command = coerce_command(name, &cmd)?;
            let mut proc = Command::new(&command[0]);
            if command.len() > 1 {
                proc.args(&command[1..]);
            }
            let out = proc.output().map_err(|e| EvalError::new(format!("ops.os.exec_capture error: {e}")))?;
            let code = out.status.code().unwrap_or(-1) as i64;
            runtime.last_exit_code = Some(code);
            let mut obj = Map::new();
            obj.insert("code".to_string(), Value::Number(Number::from(code)));
            obj.insert(
                "stdout".to_string(),
                Value::String(String::from_utf8_lossy(&out.stdout).to_string()),
            );
            obj.insert(
                "stderr".to_string(),
                Value::String(String::from_utf8_lossy(&out.stderr).to_string()),
            );
            obj.insert("duration_ms".to_string(), Value::Number(Number::from(0)));
            obj.insert("timed_out".to_string(), Value::Bool(false));
            Ok(Value::Object(obj))
        }
        "ops.os.env_get" => {
            require_arity(name, args, 2)?;
            require_ops_os(runtime, name)?;
            let key = eval_runtime(&args[0], env, limits, steps, runtime)?;
            let fallback = eval_runtime(&args[1], env, limits, steps, runtime)?;
            let Some(k) = key.as_str() else {
                return Err(EvalError::new("spec_lang ops.os.env_get expects string key"));
            };
            Ok(std_env::var(k).map(Value::String).unwrap_or(fallback))
        }
        "ops.os.env_has" => {
            require_arity(name, args, 1)?;
            require_ops_os(runtime, name)?;
            let key = eval_runtime(&args[0], env, limits, steps, runtime)?;
            let Some(k) = key.as_str() else {
                return Err(EvalError::new("spec_lang ops.os.env_has expects string key"));
            };
            Ok(Value::Bool(std_env::var(k).is_ok()))
        }
        "ops.os.cwd" => {
            require_arity(name, args, 0)?;
            require_ops_os(runtime, name)?;
            let cwd = std_env::current_dir().map_err(|e| EvalError::new(format!("ops.os.cwd error: {e}")))?;
            Ok(Value::String(cwd.to_string_lossy().to_string()))
        }
        "ops.os.pid" => {
            require_arity(name, args, 0)?;
            require_ops_os(runtime, name)?;
            Ok(Value::Number(Number::from(std::process::id() as i64)))
        }
        "ops.os.sleep_ms" => {
            require_arity(name, args, 1)?;
            require_ops_os(runtime, name)?;
            let ms = eval_runtime(&args[0], env, limits, steps, runtime)?
                .as_i64()
                .ok_or_else(|| EvalError::new("spec_lang ops.os.sleep_ms expects integer delay"))?;
            if ms < 0 {
                return Err(EvalError::new("spec_lang ops.os.sleep_ms expects non-negative delay"));
            }
            thread::sleep(Duration::from_millis(ms as u64));
            Ok(Value::Bool(true))
        }
        "ops.os.exit_code" => {
            require_arity(name, args, 0)?;
            require_ops_os(runtime, name)?;
            match runtime.last_exit_code {
                Some(code) => Ok(Value::Number(Number::from(code))),
                None => Ok(Value::Null),
            }
        }
        other => Err(EvalError::new(format!("unsupported spec op: {other}"))),
    }
}

fn compile_fn_expr(args: &[Expr], env: &Env) -> EvalResult<RuntimeValue> {
    if args.len() != 2 {
        return Err(EvalError::new("fn args must be [params, body]"));
    }
    let params = match &args[0] {
        Expr::Lit(Value::Array(items)) => {
            let mut out = Vec::<String>::new();
            for v in items {
                let Some(s) = v.as_str() else {
                    return Err(EvalError::new("fn params must be list[string]"));
                };
                let t = s.trim();
                if t.is_empty() {
                    return Err(EvalError::new("fn param name must be non-empty"));
                }
                out.push(t.to_string());
            }
            out
        }
        _ => return Err(EvalError::new("fn params must be list literal")),
    };
    Ok(RuntimeValue::Closure(Closure {
        params,
        body: Box::new(args[1].clone()),
        env: env.clone(),
    }))
}

fn eval_callable(
    expr: &Expr,
    env: &Env,
    limits: &EvalLimits,
    steps: &mut usize,
    runtime: &mut RuntimeContext,
) -> EvalResult<RuntimeValue> {
    match expr {
        Expr::Var(name) => match env.lookup(name) {
            Some(rv @ RuntimeValue::Closure(_)) => Ok(rv),
            Some(RuntimeValue::Json(_)) => {
                Err(EvalError::new(format!("variable {name} is not callable")))
            }
            None => Err(EvalError::new(format!("undefined variable: {name}"))),
        },
        Expr::Op { name, args } if name == "fn" => compile_fn_expr(args, env),
        _ => {
            let v = eval_runtime(expr, env, limits, steps, runtime)?;
            Err(EvalError::new(format!(
                "call target is not callable: {}",
                json_type_name(&v)
            )))
        }
    }
}

fn apply_callable(
    callable: RuntimeValue,
    args: Vec<RuntimeValue>,
    limits: &EvalLimits,
    steps: &mut usize,
    runtime: &mut RuntimeContext,
) -> EvalResult<Value> {
    let RuntimeValue::Closure(c) = callable else {
        return Err(EvalError::new("call target is not callable"));
    };
    if c.params.len() != args.len() {
        return Err(EvalError::new(format!(
            "call arity mismatch: expected {} got {}",
            c.params.len(),
            args.len()
        )));
    }
    let mut bindings = HashMap::<String, RuntimeValue>::new();
    for (name, value) in c.params.iter().zip(args) {
        bindings.insert(name.clone(), value);
    }
    let env = c.env.with_parent(bindings);
    eval_runtime(&c.body, &env, limits, steps, runtime)
}

fn truthy(v: &Value) -> bool {
    match v {
        Value::Null => false,
        Value::Bool(b) => *b,
        Value::Number(n) => n.as_f64().map(|x| x != 0.0).unwrap_or(true),
        Value::String(s) => !s.is_empty(),
        Value::Array(a) => !a.is_empty(),
        Value::Object(o) => !o.is_empty(),
    }
}

fn require_arity(op: &str, args: &[Expr], n: usize) -> EvalResult<()> {
    if args.len() == n {
        Ok(())
    } else {
        Err(EvalError::new(format!(
            "spec_lang arity error for {op}: expected {n} got {}",
            args.len()
        )))
    }
}

fn require_min_arity(op: &str, args: &[Expr], n: usize) -> EvalResult<()> {
    if args.len() >= n {
        Ok(())
    } else {
        Err(EvalError::new(format!(
            "spec_lang arity error for {op}: expected at least {n} got {}",
            args.len()
        )))
    }
}

fn numeric_arg(v: Value, op: &str) -> EvalResult<f64> {
    v.as_f64()
        .ok_or_else(|| EvalError::new(format!("spec_lang {op} expects number args")))
}

fn numeric_to_json(x: f64) -> Value {
    Number::from_f64(x)
        .map(Value::Number)
        .unwrap_or_else(|| Value::Number(Number::from(0)))
}

fn numeric_fold(
    op: &str,
    args: &[Expr],
    env: &Env,
    limits: &EvalLimits,
    steps: &mut usize,
    runtime: &mut RuntimeContext,
    init: f64,
    f: impl Fn(f64, f64) -> f64,
) -> EvalResult<Value> {
    require_min_arity(op, args, 1)?;
    let mut acc = init;
    for arg in args {
        acc = f(
            acc,
            numeric_arg(eval_runtime(arg, env, limits, steps, runtime)?, op)?,
        );
    }
    Ok(numeric_to_json(acc))
}

fn numeric_sub(
    op: &str,
    args: &[Expr],
    env: &Env,
    limits: &EvalLimits,
    steps: &mut usize,
    runtime: &mut RuntimeContext,
) -> EvalResult<Value> {
    require_min_arity(op, args, 1)?;
    let first = numeric_arg(eval_runtime(&args[0], env, limits, steps, runtime)?, op)?;
    if args.len() == 1 {
        return Ok(numeric_to_json(-first));
    }
    let mut acc = first;
    for arg in &args[1..] {
        acc -= numeric_arg(eval_runtime(arg, env, limits, steps, runtime)?, op)?;
    }
    Ok(numeric_to_json(acc))
}

fn numeric_div(
    op: &str,
    args: &[Expr],
    env: &Env,
    limits: &EvalLimits,
    steps: &mut usize,
    runtime: &mut RuntimeContext,
) -> EvalResult<Value> {
    require_min_arity(op, args, 1)?;
    let first = numeric_arg(eval_runtime(&args[0], env, limits, steps, runtime)?, op)?;
    if args.len() == 1 {
        if first == 0.0 {
            return Err(EvalError::new("division by zero"));
        }
        return Ok(numeric_to_json(1.0 / first));
    }
    let mut acc = first;
    for arg in &args[1..] {
        let rhs = numeric_arg(eval_runtime(arg, env, limits, steps, runtime)?, op)?;
        if rhs == 0.0 {
            return Err(EvalError::new("division by zero"));
        }
        acc /= rhs;
    }
    Ok(numeric_to_json(acc))
}

fn json_type_name(v: &Value) -> &'static str {
    match v {
        Value::Null => "null",
        Value::Bool(_) => "bool",
        Value::Number(_) => "number",
        Value::String(_) => "string",
        Value::Array(_) => "list",
        Value::Object(_) => "dict",
    }
}

fn require_ops_os(runtime: &RuntimeContext, op: &str) -> EvalResult<()> {
    if runtime.capabilities.contains("ops.os") {
        Ok(())
    } else {
        Err(EvalError::new(format!("capability.ops_os.required: {op}")))
    }
}

fn coerce_command(op: &str, value: &Value) -> EvalResult<Vec<String>> {
    let Value::Array(items) = value else {
        return Err(EvalError::new(format!("spec_lang {op} expects non-empty list command")));
    };
    if items.is_empty() {
        return Err(EvalError::new(format!("spec_lang {op} expects non-empty list command")));
    }
    let mut out = Vec::<String>::with_capacity(items.len());
    for item in items {
        let Some(token) = item.as_str() else {
            return Err(EvalError::new(format!("spec_lang {op} command entries must be strings")));
        };
        let t = token.trim();
        if t.is_empty() {
            return Err(EvalError::new(format!("spec_lang {op} command entries must be non-empty strings")));
        }
        out.push(t.to_string());
    }
    Ok(out)
}

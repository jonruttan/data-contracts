use std::collections::HashMap;

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
    let mut env = Env::default();
    env.vars
        .insert("subject".to_string(), RuntimeValue::Json(subject.clone()));
    for (name, value) in symbols {
        let compiled = compile_mapping_ast(&value)?;
        let rv = match compiled {
            Expr::Op { name: op, args } if op == "fn" => compile_fn_expr(&args, &env)?,
            other => RuntimeValue::Json(eval_runtime(&other, &env, &limits, &mut 0)?),
        };
        env.vars.insert(name, rv);
    }
    eval_runtime(expr, &env, &limits, &mut 0)
}

fn eval_runtime(
    expr: &Expr,
    env: &Env,
    limits: &EvalLimits,
    steps: &mut usize,
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
        Expr::Op { name, args } => eval_op(name, args, env, limits, steps),
    }
}

fn eval_op(
    name: &str,
    args: &[Expr],
    env: &Env,
    limits: &EvalLimits,
    steps: &mut usize,
) -> EvalResult<Value> {
    match name {
        "if" => {
            require_arity(name, args, 3)?;
            let cond = eval_runtime(&args[0], env, limits, steps)?;
            if truthy(&cond) {
                eval_runtime(&args[1], env, limits, steps)
            } else {
                eval_runtime(&args[2], env, limits, steps)
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
            let target = eval_callable(&args[0], env, limits, steps)?;
            let mut values = Vec::<RuntimeValue>::new();
            for arg in &args[1..] {
                values.push(RuntimeValue::Json(eval_runtime(arg, env, limits, steps)?));
            }
            apply_callable(target, values, limits, steps)
        }
        "std.logic.eq" | "eq" => {
            require_arity(name, args, 2)?;
            let left = eval_runtime(&args[0], env, limits, steps)?;
            let right = eval_runtime(&args[1], env, limits, steps)?;
            Ok(Value::Bool(left == right))
        }
        "std.logic.neq" | "neq" => {
            require_arity(name, args, 2)?;
            let left = eval_runtime(&args[0], env, limits, steps)?;
            let right = eval_runtime(&args[1], env, limits, steps)?;
            Ok(Value::Bool(left != right))
        }
        "std.logic.and" | "and" => {
            require_min_arity(name, args, 1)?;
            for arg in args {
                let v = eval_runtime(arg, env, limits, steps)?;
                if !truthy(&v) {
                    return Ok(Value::Bool(false));
                }
            }
            Ok(Value::Bool(true))
        }
        "std.logic.or" | "or" => {
            require_min_arity(name, args, 1)?;
            for arg in args {
                let v = eval_runtime(arg, env, limits, steps)?;
                if truthy(&v) {
                    return Ok(Value::Bool(true));
                }
            }
            Ok(Value::Bool(false))
        }
        "std.logic.not" | "not" => {
            require_arity(name, args, 1)?;
            Ok(Value::Bool(!truthy(&eval_runtime(
                &args[0], env, limits, steps,
            )?)))
        }
        "std.object.get" | "get" => {
            require_arity(name, args, 2)?;
            let obj = eval_runtime(&args[0], env, limits, steps)?;
            let key = eval_runtime(&args[1], env, limits, steps)?;
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
            let v = eval_runtime(&args[0], env, limits, steps)?;
            Ok(Value::Bool(v.is_array()))
        }
        "std.type.is_dict" | "is_dict" | "std.type.is_object" | "is_object" => {
            require_arity(name, args, 1)?;
            let v = eval_runtime(&args[0], env, limits, steps)?;
            Ok(Value::Bool(v.is_object()))
        }
        "std.type.is_string" | "is_string" => {
            require_arity(name, args, 1)?;
            let v = eval_runtime(&args[0], env, limits, steps)?;
            Ok(Value::Bool(v.is_string()))
        }
        "std.type.is_number" | "is_number" => {
            require_arity(name, args, 1)?;
            let v = eval_runtime(&args[0], env, limits, steps)?;
            Ok(Value::Bool(v.is_number()))
        }
        "std.type.is_bool" | "is_bool" | "std.type.is_boolean" | "is_boolean" => {
            require_arity(name, args, 1)?;
            let v = eval_runtime(&args[0], env, limits, steps)?;
            Ok(Value::Bool(v.is_boolean()))
        }
        "std.type.is_null" | "is_null" => {
            require_arity(name, args, 1)?;
            let v = eval_runtime(&args[0], env, limits, steps)?;
            Ok(Value::Bool(v.is_null()))
        }
        "std.string.contains" | "contains" => {
            require_arity(name, args, 2)?;
            let hay = eval_runtime(&args[0], env, limits, steps)?;
            let needle = eval_runtime(&args[1], env, limits, steps)?;
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
            let v = eval_runtime(&args[0], env, limits, steps)?;
            let Some(s) = v.as_str() else {
                return Err(EvalError::new("std.string.lower expects string"));
            };
            Ok(Value::String(s.to_lowercase()))
        }
        "std.string.upper" | "upper" => {
            require_arity(name, args, 1)?;
            let v = eval_runtime(&args[0], env, limits, steps)?;
            let Some(s) = v.as_str() else {
                return Err(EvalError::new("std.string.upper expects string"));
            };
            Ok(Value::String(s.to_uppercase()))
        }
        "std.string.trim" | "trim" => {
            require_arity(name, args, 1)?;
            let v = eval_runtime(&args[0], env, limits, steps)?;
            let Some(s) = v.as_str() else {
                return Err(EvalError::new("std.string.trim expects string"));
            };
            Ok(Value::String(s.trim().to_string()))
        }
        "std.collection.count" | "count" | "len" => {
            require_arity(name, args, 1)?;
            let v = eval_runtime(&args[0], env, limits, steps)?;
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
                let v = eval_runtime(arg, env, limits, steps)?;
                let Value::Array(items) = v else {
                    return Err(EvalError::new("std.collection.concat expects list args"));
                };
                out.extend(items);
            }
            Ok(Value::Array(out))
        }
        "std.math.add" | "add" => numeric_fold(name, args, env, limits, steps, 0.0, |a, b| a + b),
        "std.math.sub" | "sub" => numeric_sub(name, args, env, limits, steps),
        "std.math.mul" | "mul" => numeric_fold(name, args, env, limits, steps, 1.0, |a, b| a * b),
        "std.math.div" | "div" => numeric_div(name, args, env, limits, steps),
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
            let v = eval_runtime(expr, env, limits, steps)?;
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
    eval_runtime(&c.body, &env, limits, steps)
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
    init: f64,
    f: impl Fn(f64, f64) -> f64,
) -> EvalResult<Value> {
    require_min_arity(op, args, 1)?;
    let mut acc = init;
    for arg in args {
        acc = f(
            acc,
            numeric_arg(eval_runtime(arg, env, limits, steps)?, op)?,
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
) -> EvalResult<Value> {
    require_min_arity(op, args, 1)?;
    let first = numeric_arg(eval_runtime(&args[0], env, limits, steps)?, op)?;
    if args.len() == 1 {
        return Ok(numeric_to_json(-first));
    }
    let mut acc = first;
    for arg in &args[1..] {
        acc -= numeric_arg(eval_runtime(arg, env, limits, steps)?, op)?;
    }
    Ok(numeric_to_json(acc))
}

fn numeric_div(
    op: &str,
    args: &[Expr],
    env: &Env,
    limits: &EvalLimits,
    steps: &mut usize,
) -> EvalResult<Value> {
    require_min_arity(op, args, 1)?;
    let first = numeric_arg(eval_runtime(&args[0], env, limits, steps)?, op)?;
    if args.len() == 1 {
        if first == 0.0 {
            return Err(EvalError::new("division by zero"));
        }
        return Ok(numeric_to_json(1.0 / first));
    }
    let mut acc = first;
    for arg in &args[1..] {
        let rhs = numeric_arg(eval_runtime(arg, env, limits, steps)?, op)?;
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

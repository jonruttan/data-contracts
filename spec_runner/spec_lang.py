from __future__ import annotations

import time
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class SpecLangLimits:
    max_steps: int = 20000
    max_nodes: int = 20000
    max_literal_bytes: int = 262144
    timeout_ms: int = 200


@dataclass(frozen=True)
class _Closure:
    params: tuple[str, ...]
    body: Any
    env: "_Env"


@dataclass(frozen=True)
class _Env:
    vars: dict[str, Any]
    parent: "_Env | None"

    def lookup(self, name: str) -> Any:
        cur: _Env | None = self
        while cur is not None:
            if name in cur.vars:
                value = cur.vars[name]
                if value is _UNSET:
                    raise ValueError(f"uninitialized variable: {name}")
                return value
            cur = cur.parent
        raise ValueError(f"undefined variable: {name}")


@dataclass
class _EvalState:
    subject: Any
    limits: SpecLangLimits
    steps: int = 0
    started: float = 0.0

    def tick(self) -> None:
        self.steps += 1
        if self.steps > self.limits.max_steps:
            raise RuntimeError("spec_lang budget exceeded: steps")
        if self.limits.timeout_ms > 0:
            elapsed_ms = (time.perf_counter() - self.started) * 1000.0
            if elapsed_ms > float(self.limits.timeout_ms):
                raise RuntimeError("spec_lang budget exceeded: timeout")


_UNSET = object()


def _literal_size(v: Any) -> int:
    if isinstance(v, str):
        return len(v.encode("utf-8"))
    if isinstance(v, (bytes, bytearray)):
        return len(v)
    return 0


def validate_expr_shape(expr: Any, *, limits: SpecLangLimits) -> None:
    stack = [expr]
    nodes = 0
    literal_bytes = 0
    while stack:
        cur = stack.pop()
        nodes += 1
        if nodes > limits.max_nodes:
            raise RuntimeError("spec_lang budget exceeded: nodes")
        literal_bytes += _literal_size(cur)
        if literal_bytes > limits.max_literal_bytes:
            raise RuntimeError("spec_lang budget exceeded: literal_size")
        if isinstance(cur, list):
            for child in cur:
                stack.append(child)


def _require_arity(op: str, args: list[Any], n: int) -> None:
    if len(args) != n:
        raise ValueError(f"spec_lang arity error for {op}: expected {n} got {len(args)}")


def _require_min_arity(op: str, args: list[Any], n: int) -> None:
    if len(args) < n:
        raise ValueError(f"spec_lang arity error for {op}: expected at least {n} got {len(args)}")


def _is_list_like(v: Any) -> bool:
    return isinstance(v, list)


def _is_dict_like(v: Any) -> bool:
    return isinstance(v, dict)


def _json_type_name(v: Any) -> str:
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "bool"
    if isinstance(v, (int, float)):
        return "number"
    if isinstance(v, str):
        return "string"
    if _is_list_like(v):
        return "list"
    if _is_dict_like(v):
        return "dict"
    return "unknown"


def _truthy(v: Any) -> bool:
    return bool(v)


def _eval_non_tail(expr: Any, env: _Env, st: _EvalState) -> Any:
    return _eval_tail(expr, env, st)


def _eval_builtin(op: str, args: list[Any], env: _Env, st: _EvalState) -> Any:
    if op == "subject":
        _require_arity(op, args, 0)
        return st.subject
    if op == "var":
        _require_arity(op, args, 1)
        name = args[0]
        if not isinstance(name, str) or not name.strip():
            raise ValueError("spec_lang var requires non-empty string name")
        return env.lookup(name)
    if op == "and":
        _require_min_arity(op, args, 1)
        for a in args:
            if not _truthy(_eval_non_tail(a, env, st)):
                return False
        return True
    if op == "or":
        _require_min_arity(op, args, 1)
        for a in args:
            if _truthy(_eval_non_tail(a, env, st)):
                return True
        return False
    if op == "not":
        _require_arity(op, args, 1)
        return not _truthy(_eval_non_tail(args[0], env, st))
    if op == "contains":
        if len(args) == 1:
            hay = st.subject
            needle = _eval_non_tail(args[0], env, st)
        elif len(args) == 2:
            hay = _eval_non_tail(args[0], env, st)
            needle = _eval_non_tail(args[1], env, st)
        else:
            raise ValueError("spec_lang arity error for contains")
        return str(needle) in str(hay)
    if op == "starts_with":
        if len(args) == 1:
            hay = st.subject
            prefix = _eval_non_tail(args[0], env, st)
        elif len(args) == 2:
            hay = _eval_non_tail(args[0], env, st)
            prefix = _eval_non_tail(args[1], env, st)
        else:
            raise ValueError("spec_lang arity error for starts_with")
        return str(hay).startswith(str(prefix))
    if op == "ends_with":
        if len(args) == 1:
            hay = st.subject
            suffix = _eval_non_tail(args[0], env, st)
        elif len(args) == 2:
            hay = _eval_non_tail(args[0], env, st)
            suffix = _eval_non_tail(args[1], env, st)
        else:
            raise ValueError("spec_lang arity error for ends_with")
        return str(hay).endswith(str(suffix))
    if op == "eq":
        _require_arity(op, args, 2)
        return _eval_non_tail(args[0], env, st) == _eval_non_tail(args[1], env, st)
    if op == "neq":
        _require_arity(op, args, 2)
        return _eval_non_tail(args[0], env, st) != _eval_non_tail(args[1], env, st)
    if op == "in":
        _require_arity(op, args, 2)
        member = _eval_non_tail(args[0], env, st)
        container = _eval_non_tail(args[1], env, st)
        if _is_list_like(container):
            return member in container
        if _is_dict_like(container):
            return str(member) in container
        if isinstance(container, str):
            return str(member) in container
        raise ValueError("spec_lang in expects list/dict/string container")
    if op == "add":
        _require_arity(op, args, 2)
        left = _eval_non_tail(args[0], env, st)
        right = _eval_non_tail(args[1], env, st)
        if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
            raise ValueError("spec_lang add expects numeric args")
        return left + right
    if op == "sub":
        _require_arity(op, args, 2)
        left = _eval_non_tail(args[0], env, st)
        right = _eval_non_tail(args[1], env, st)
        if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
            raise ValueError("spec_lang sub expects numeric args")
        return left - right
    if op == "json_type":
        if len(args) == 1:
            value = st.subject
            want = _eval_non_tail(args[0], env, st)
        elif len(args) == 2:
            value = _eval_non_tail(args[0], env, st)
            want = _eval_non_tail(args[1], env, st)
        else:
            raise ValueError("spec_lang arity error for json_type")
        want_s = str(want).strip().lower()
        return _json_type_name(value) == want_s
    if op == "has_key":
        if len(args) == 1:
            obj = st.subject
            key = _eval_non_tail(args[0], env, st)
        elif len(args) == 2:
            obj = _eval_non_tail(args[0], env, st)
            key = _eval_non_tail(args[1], env, st)
        else:
            raise ValueError("spec_lang arity error for has_key")
        if not _is_dict_like(obj):
            return False
        return str(key) in obj
    if op == "get":
        _require_arity(op, args, 2)
        obj = _eval_non_tail(args[0], env, st)
        key = _eval_non_tail(args[1], env, st)
        if _is_dict_like(obj):
            return obj.get(str(key))
        if _is_list_like(obj):
            if not isinstance(key, int):
                raise ValueError("spec_lang get list index must be int")
            if key < 0 or key >= len(obj):
                return None
            return obj[key]
        raise ValueError("spec_lang get expects dict or list")
    if op == "len":
        _require_arity(op, args, 1)
        v = _eval_non_tail(args[0], env, st)
        if isinstance(v, (str, list, dict)):
            return len(v)
        raise ValueError("spec_lang len expects string/list/dict")
    if op == "trim":
        _require_arity(op, args, 1)
        return str(_eval_non_tail(args[0], env, st)).strip()
    if op == "lower":
        _require_arity(op, args, 1)
        return str(_eval_non_tail(args[0], env, st)).lower()
    if op == "upper":
        _require_arity(op, args, 1)
        return str(_eval_non_tail(args[0], env, st)).upper()
    raise ValueError(f"unsupported spec_lang symbol: {op}")


def _eval_tail(expr: Any, env: _Env, st: _EvalState) -> Any:
    current_expr = expr
    current_env = env
    while True:
        st.tick()
        if isinstance(current_expr, (str, int, float, bool)) or current_expr is None:
            return current_expr
        if not isinstance(current_expr, list):
            raise ValueError("spec_lang expression must be list-based s-expr or scalar literal")
        if len(current_expr) == 0:
            raise ValueError("spec_lang expression list must not be empty")
        head = current_expr[0]
        if not isinstance(head, str) or not head:
            raise ValueError("spec_lang expression head must be non-empty string symbol")
        op = head
        args = list(current_expr[1:])

        if op == "if":
            _require_arity(op, args, 3)
            cond = _eval_non_tail(args[0], current_env, st)
            current_expr = args[1] if _truthy(cond) else args[2]
            continue

        if op == "let":
            _require_arity(op, args, 2)
            raw_bindings = args[0]
            body = args[1]
            if not isinstance(raw_bindings, list):
                raise ValueError("spec_lang let bindings must be a list")
            slots: dict[str, Any] = {}
            next_env = _Env(vars=slots, parent=current_env)
            pairs: list[tuple[str, Any]] = []
            for b in raw_bindings:
                if not isinstance(b, list) or len(b) != 2:
                    raise ValueError("spec_lang let binding must be [name, expr]")
                name = b[0]
                if not isinstance(name, str) or not name.strip():
                    raise ValueError("spec_lang let binding name must be non-empty string")
                key = name.strip()
                if key in slots:
                    raise ValueError(f"duplicate let binding: {key}")
                slots[key] = _UNSET
                pairs.append((key, b[1]))
            for key, rhs in pairs:
                slots[key] = _eval_non_tail(rhs, next_env, st)
            current_expr = body
            current_env = next_env
            continue

        if op == "fn":
            _require_arity(op, args, 2)
            raw_params = args[0]
            body = args[1]
            if not isinstance(raw_params, list):
                raise ValueError("spec_lang fn params must be a list")
            params: list[str] = []
            seen: set[str] = set()
            for p in raw_params:
                if not isinstance(p, str) or not p.strip():
                    raise ValueError("spec_lang fn param must be non-empty string")
                key = p.strip()
                if key in seen:
                    raise ValueError(f"duplicate fn param: {key}")
                seen.add(key)
                params.append(key)
            return _Closure(params=tuple(params), body=body, env=current_env)

        if op == "call":
            _require_min_arity(op, args, 1)
            fn_val = _eval_non_tail(args[0], current_env, st)
            eval_args = [_eval_non_tail(a, current_env, st) for a in args[1:]]
            if not isinstance(fn_val, _Closure):
                raise ValueError("spec_lang call expects fn closure")
            if len(eval_args) != len(fn_val.params):
                raise ValueError("spec_lang call argument count mismatch")
            current_env = _Env(
                vars={k: v for k, v in zip(fn_val.params, eval_args)},
                parent=fn_val.env,
            )
            current_expr = fn_val.body
            continue

        return _eval_builtin(op, args, current_env, st)


def eval_expr(expr: Any, *, subject: Any, limits: SpecLangLimits | None = None) -> Any:
    cfg = limits or SpecLangLimits()
    validate_expr_shape(expr, limits=cfg)
    st = _EvalState(subject=subject, limits=cfg, started=time.perf_counter())
    return _eval_tail(expr, _Env(vars={}, parent=None), st)


def eval_predicate(expr: Any, *, subject: Any, limits: SpecLangLimits | None = None) -> bool:
    got = eval_expr(expr, subject=subject, limits=limits)
    return bool(got)


def limits_from_harness(harness: Mapping[str, Any] | None) -> SpecLangLimits:
    cfg = dict((harness or {}).get("spec_lang") or {})
    if not cfg:
        return SpecLangLimits()
    if not isinstance(cfg, dict):
        raise TypeError("harness.spec_lang must be a mapping")

    def _int_field(name: str, *, min_value: int) -> int:
        raw = cfg.get(name)
        if raw is None:
            return getattr(SpecLangLimits(), name)
        if isinstance(raw, bool) or not isinstance(raw, int):
            raise TypeError(f"harness.spec_lang.{name} must be an integer")
        if raw < min_value:
            raise ValueError(f"harness.spec_lang.{name} must be >= {min_value}")
        return raw

    return SpecLangLimits(
        max_steps=_int_field("max_steps", min_value=1),
        max_nodes=_int_field("max_nodes", min_value=1),
        max_literal_bytes=_int_field("max_literal_bytes", min_value=1),
        timeout_ms=_int_field("timeout_ms", min_value=0),
    )

#!/usr/bin/env php
<?php
declare(strict_types=1);

/*
 * PHP spec runner.
 *
 * Executes Markdown-embedded `yaml spec-test` cases and emits a normalized
 * JSON report.
 *
 * Usage:
 *   php scripts/php/spec_runner.php --cases <dir-or-file> --out <file>
 */

function usage(): void {
    fwrite(STDOUT, "usage: spec_runner.php --cases <dir-or-file> --out <file> [--case-file-pattern <glob>] [--case-formats <csv>]\n");
}

const DEFAULT_CASE_FILE_PATTERN = '*.spec.md';
const PHP_CAPABILITIES = [
    'api.http',
    'assert.op.contain',
    'assert.op.regex',
    'assert.op.evaluate',
    'assert.group.must',
    'assert.group.can',
    'assert.group.cannot',
    'assert_health.ah001',
    'assert_health.ah002',
    'assert_health.ah003',
    'assert_health.ah004',
    'assert_health.ah005',
    'evaluate.spec_lang.v1',
    'requires.capabilities',
];

function parseArgs(array $argv): array {
    $out = null;
    $cases = null;
    $casePattern = DEFAULT_CASE_FILE_PATTERN;
    $caseFormatsRaw = 'md';
    for ($i = 1; $i < count($argv); $i++) {
        $arg = $argv[$i];
        if ($arg === '--help' || $arg === '-h') {
            usage();
            exit(0);
        }
        if ($arg === '--out' && $i + 1 < count($argv)) {
            $out = $argv[++$i];
            continue;
        }
        if ($arg === '--cases' && $i + 1 < count($argv)) {
            $cases = $argv[++$i];
            continue;
        }
        if ($arg === '--case-file-pattern') {
            if ($i + 1 >= count($argv)) {
                fwrite(STDERR, "error: --case-file-pattern requires a non-empty value\n");
                usage();
                exit(2);
            }
            $casePattern = trim((string)$argv[++$i]);
            if ($casePattern === '') {
                fwrite(STDERR, "error: --case-file-pattern requires a non-empty value\n");
                usage();
                exit(2);
            }
            continue;
        }
        if ($arg === '--case-formats') {
            if ($i + 1 >= count($argv)) {
                fwrite(STDERR, "error: --case-formats requires a non-empty value\n");
                usage();
                exit(2);
            }
            $caseFormatsRaw = trim((string)$argv[++$i]);
            if ($caseFormatsRaw === '') {
                fwrite(STDERR, "error: --case-formats requires a non-empty value\n");
                usage();
                exit(2);
            }
            continue;
        }
    }
    if ($out === null || $cases === null) {
        usage();
        exit(2);
    }
    $parts = preg_split('/\s*,\s*/', strtolower($caseFormatsRaw)) ?: [];
    $formats = [];
    foreach ($parts as $p) {
        $v = trim((string)$p);
        if ($v === '') {
            continue;
        }
        if ($v !== 'md' && $v !== 'yaml' && $v !== 'json') {
            fwrite(STDERR, "error: unsupported case format: {$v}\n");
            usage();
            exit(2);
        }
        $formats[$v] = true;
    }
    if (count($formats) === 0) {
        fwrite(STDERR, "error: --case-formats requires at least one format\n");
        usage();
        exit(2);
    }
    return [
        'out' => $out,
        'cases' => $cases,
        'case_pattern' => $casePattern,
        'case_formats' => array_keys($formats),
    ];
}

function matchesCasePattern(string $name, string $pattern): bool {
    $regex = '/^' . str_replace(
        ['\*', '\?'],
        ['.*', '.'],
        preg_quote($pattern, '/')
    ) . '$/i';
    return preg_match($regex, $name) === 1;
}

function _pathMatchesFormat(string $name, array $formats, string $pattern): bool {
    $lower = strtolower($name);
    foreach ($formats as $fmt) {
        if ($fmt === 'md') {
            if (matchesCasePattern($name, $pattern)) {
                return true;
            }
            continue;
        }
        if ($fmt === 'yaml') {
            if (str_ends_with($lower, '.spec.yaml') || str_ends_with($lower, '.spec.yml')) {
                return true;
            }
            continue;
        }
        if ($fmt === 'json') {
            if (str_ends_with($lower, '.spec.json')) {
                return true;
            }
        }
    }
    return false;
}

function listCaseFiles(string $path, string $pattern, array $formats): array {
    if (is_file($path)) {
        if (_pathMatchesFormat(basename($path), $formats, $pattern)) {
            return [$path];
        }
        throw new RuntimeException("cases path is a file but does not match enabled formats/pattern: {$path}");
    }
    $files = [];
    $items = scandir($path);
    if ($items === false) {
        throw new RuntimeException("cannot read cases path: {$path}");
    }
    foreach ($items as $item) {
        if ($item === '.' || $item === '..') {
            continue;
        }
        $itemPath = rtrim($path, DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR . $item;
        if (!is_file($itemPath)) {
            continue;
        }
        if (_pathMatchesFormat($item, $formats, $pattern)) {
            $files[] = $itemPath;
        }
    }
    sort($files, SORT_STRING);
    return $files;
}

class SchemaError extends RuntimeException {}
class AssertionFailure extends RuntimeException {}

const ALWAYS_TRUE_REGEX = ['.*', '^.*$', '\\A.*\\Z'];

function isListArray(mixed $value): bool {
    if (!is_array($value)) {
        return false;
    }
    if ($value === []) {
        return true;
    }
    return array_keys($value) === range(0, count($value) - 1);
}

function isSpecTestOpeningFence(string $line): ?array {
    $trimmed = ltrim($line, " \t");
    if ($trimmed === '') {
        return null;
    }
    $first = $trimmed[0];
    if ($first !== '`' && $first !== '~') {
        return null;
    }
    $i = 0;
    $n = strlen($trimmed);
    while ($i < $n && $trimmed[$i] === $first) {
        $i++;
    }
    if ($i < 3) {
        return null;
    }
    $info = trim(substr($trimmed, $i));
    if ($info === '') {
        return null;
    }
    $tokens = preg_split('/\s+/', strtolower($info)) ?: [];
    $set = array_fill_keys($tokens, true);
    if (!isset($set['spec-test']) || (!isset($set['yaml']) && !isset($set['yml']))) {
        return null;
    }
    return [$first, $i];
}

function isClosingFence(string $line, string $char, int $minLen): bool {
    $trimmed = rtrim(ltrim($line, " \t"));
    if ($trimmed === '' || $trimmed[0] !== $char) {
        return false;
    }
    $i = 0;
    $n = strlen($trimmed);
    while ($i < $n && $trimmed[$i] === $char) {
        $i++;
    }
    return $i >= $minLen && $i === $n;
}

function parseMarkdownCases(string $path): array {
    if (!function_exists('yaml_parse')) {
        throw new RuntimeException('yaml_parse extension is required for PHP spec runner');
    }
    $raw = file_get_contents($path);
    if ($raw === false) {
        throw new RuntimeException("cannot read fixture file: {$path}");
    }
    $lines = preg_split('/\R/', $raw) ?: [];
    $i = 0;
    $cases = [];
    while ($i < count($lines)) {
        $open = isSpecTestOpeningFence($lines[$i]);
        if ($open === null) {
            $i++;
            continue;
        }
        [$fenceChar, $fenceLen] = $open;
        $i++;
        $blockLines = [];
        while ($i < count($lines) && !isClosingFence($lines[$i], $fenceChar, $fenceLen)) {
            $blockLines[] = $lines[$i];
            $i++;
        }
        if ($i >= count($lines)) {
            break;
        }
        $payload = @yaml_parse(implode("\n", $blockLines));
        if (is_array($payload) && isListArray($payload)) {
            foreach ($payload as $test) {
                if (!is_array($test)) {
                    throw new RuntimeException("spec-test block in {$path} contains a non-mapping test");
                }
                if (!array_key_exists('id', $test) || !array_key_exists('type', $test)) {
                    throw new RuntimeException("spec-test in {$path} must include 'id' and 'type'");
                }
                $cases[] = $test;
            }
        } elseif (is_array($payload)) {
            if (!array_key_exists('id', $payload) || !array_key_exists('type', $payload)) {
                throw new RuntimeException("spec-test in {$path} must include 'id' and 'type'");
            }
            $cases[] = $payload;
        } else {
            throw new RuntimeException("spec-test block in {$path} must be a mapping or a list of mappings");
        }
        $i++;
    }
    return $cases;
}

function _validateParsedCasePayload(mixed $payload, string $path): array {
    if (is_array($payload) && isListArray($payload)) {
        $cases = [];
        foreach ($payload as $test) {
            if (!is_array($test)) {
                throw new RuntimeException("spec payload in {$path} contains a non-mapping test");
            }
            if (!array_key_exists('id', $test) || !array_key_exists('type', $test)) {
                throw new RuntimeException("spec in {$path} must include 'id' and 'type'");
            }
            $cases[] = $test;
        }
        return $cases;
    }
    if (is_array($payload)) {
        if (!array_key_exists('id', $payload) || !array_key_exists('type', $payload)) {
            throw new RuntimeException("spec in {$path} must include 'id' and 'type'");
        }
        return [$payload];
    }
    throw new RuntimeException("spec payload in {$path} must be a mapping or a list of mappings");
}

function parseYamlCases(string $path): array {
    if (!function_exists('yaml_parse')) {
        throw new RuntimeException('yaml_parse extension is required for YAML spec cases');
    }
    $raw = file_get_contents($path);
    if ($raw === false) {
        throw new RuntimeException("cannot read fixture file: {$path}");
    }
    $payload = @yaml_parse($raw);
    return _validateParsedCasePayload($payload, $path);
}

function parseJsonCases(string $path): array {
    $raw = file_get_contents($path);
    if ($raw === false) {
        throw new RuntimeException("cannot read fixture file: {$path}");
    }
    try {
        $payload = json_decode($raw, true, 512, JSON_THROW_ON_ERROR);
    } catch (JsonException $e) {
        throw new RuntimeException("invalid JSON in {$path}: " . $e->getMessage());
    }
    return _validateParsedCasePayload($payload, $path);
}

function parseCases(string $path): array {
    $lower = strtolower($path);
    if (str_ends_with($lower, '.spec.yaml') || str_ends_with($lower, '.spec.yml')) {
        return parseYamlCases($path);
    }
    if (str_ends_with($lower, '.spec.json')) {
        return parseJsonCases($path);
    }
    return parseMarkdownCases($path);
}

function isAbsolutePath(string $path): bool {
    if ($path === '') {
        return false;
    }
    if ($path[0] === '/' || $path[0] === '\\') {
        return true;
    }
    return preg_match('/^[A-Za-z]:[\/\\\\]/', $path) === 1;
}

function normalizePath(string $path): string {
    $path = str_replace('\\', '/', $path);
    $isAbs = strlen($path) > 0 && $path[0] === '/';
    $parts = preg_split('~/+~', $path) ?: [];
    $stack = [];
    foreach ($parts as $part) {
        if ($part === '' || $part === '.') {
            continue;
        }
        if ($part === '..') {
            if (count($stack) > 0) {
                array_pop($stack);
            }
            continue;
        }
        $stack[] = $part;
    }
    $joined = implode('/', $stack);
    if ($isAbs) {
        return '/' . $joined;
    }
    return $joined;
}

function contractRootFor(string $docPath): string {
    $docAbs = normalizePath((string)realpath($docPath));
    $cur = dirname($docAbs);
    while (true) {
        if (is_dir($cur . '/.git')) {
            return $cur;
        }
        $parent = dirname($cur);
        if ($parent === $cur) {
            break;
        }
        $cur = $parent;
    }
    return dirname($docAbs);
}

function pathWithinRoot(string $targetPath, string $rootPath): bool {
    $target = rtrim(normalizePath($targetPath), '/');
    $root = rtrim(normalizePath($rootPath), '/');
    if ($target === $root) {
        return true;
    }
    return str_starts_with($target . '/', $root . '/');
}

function resolveContractPath(string $anchorPath, string $rawPath, string $field): string {
    $raw = trim($rawPath);
    if ($raw === '') {
        throw new SchemaError("{$field} must be non-empty");
    }
    if (str_starts_with($raw, 'external://')) {
        throw new SchemaError("{$field}: external refs are denied by default");
    }
    if (preg_match('/^[A-Za-z]:[\/\\\\]/', $raw) === 1) {
        throw new SchemaError("{$field} must not be OS-absolute");
    }
    $root = contractRootFor($anchorPath);
    if (str_starts_with($raw, '/')) {
        $joined = $root . '/' . ltrim($raw, '/');
    } else {
        $joined = $root . '/' . $raw;
    }
    $candidate = normalizePath($joined);
    if (!pathWithinRoot($candidate, $root)) {
        throw new SchemaError("{$field} escapes contract root");
    }
    return $candidate;
}

function resolveTextFilePath(string $fixturePath, array $case): string {
    $docAbs = (string)realpath($fixturePath);
    if ($docAbs === '') {
        throw new RuntimeException("cannot resolve fixture path: {$fixturePath}");
    }
    if (!array_key_exists('path', $case)) {
        return $docAbs;
    }
    return resolveContractPath($docAbs, (string)$case['path'], 'text.file path');
}

function lintAssertionHealth(mixed $node, string $path = 'assert', ?string $groupCtx = null): array {
    $diags = [];
    if (is_array($node) && isListArray($node)) {
        foreach ($node as $i => $child) {
            $diags = array_merge($diags, lintAssertionHealth($child, "{$path}[{$i}]", $groupCtx));
        }
        return $diags;
    }
    if (!is_array($node)) {
        return $diags;
    }
    foreach (['must', 'can', 'cannot'] as $group) {
        if (array_key_exists($group, $node)) {
            $children = $node[$group];
            if (is_array($children) && isListArray($children)) {
                $seen = [];
                foreach ($children as $child) {
                    $key = @json_encode($child, JSON_UNESCAPED_SLASHES);
                    if (!is_string($key) || $key === '') {
                        $key = serialize($child);
                    }
                    if (array_key_exists($key, $seen)) {
                        $diags[] = [
                            'code' => 'AH004',
                            'path' => "{$path}.{$group}",
                            'message' => "redundant sibling assertion branch in '{$group}'",
                        ];
                        break;
                    }
                    $seen[$key] = true;
                }
            }
            return array_merge($diags, lintAssertionHealth($children, "{$path}.{$group}", $group));
        }
    }
    foreach (['contain', 'regex'] as $op) {
        if (!array_key_exists($op, $node)) {
            continue;
        }
        $raw = $node[$op];
        if (!is_array($raw) || !isListArray($raw)) {
            continue;
        }
        $vals = array_map(static fn($x) => (string)$x, $raw);
        if (count($vals) !== count(array_unique($vals))) {
            $diags[] = [
                'code' => 'AH003',
                'path' => "{$path}.{$op}",
                'message' => "duplicate values in '{$op}' list can hide intent drift",
            ];
        }
        if ($op === 'contain' && in_array('', $vals, true)) {
            $msg = 'contain with empty string is always true';
            if ($groupCtx === 'cannot') {
                $msg = "cannot(contain:'') is always false";
            }
            $diags[] = ['code' => 'AH001', 'path' => "{$path}.contain", 'message' => $msg];
        }
        if ($op !== 'regex') {
            continue;
        }
        foreach ($vals as $v) {
            if (in_array($v, ALWAYS_TRUE_REGEX, true)) {
                $msg = 'regex pattern is trivially always true';
                if ($groupCtx === 'cannot') {
                    $msg = 'cannot(regex always-true) is always false';
                }
                $diags[] = ['code' => 'AH002', 'path' => "{$path}.regex", 'message' => $msg];
            }
            if (
                str_contains($v, '(?<=') ||
                str_contains($v, '(?<!') ||
                str_contains($v, '(?P<') ||
                preg_match('/\(\?<([A-Za-z_][A-Za-z0-9_]*)>/', $v) === 1 ||
                str_contains($v, '\\k<') ||
                str_contains($v, '(?(') ||
                str_contains($v, '(?>') ||
                preg_match('/\(\?[aiLmsux-]+(?::|\))/', $v) === 1 ||
                preg_match('/(?<!\\\\)(?:\\\\\\\\)*[+*?]\+/', $v) === 1
            ) {
                $diags[] = [
                    'code' => 'AH005',
                    'path' => "{$path}.regex",
                    'message' => 'regex uses non-portable construct',
                ];
                break;
            }
        }
    }
    return $diags;
}

function formatAssertionHealthWarning(array $d): string {
    return "WARN: ASSERT_HEALTH {$d['code']} at {$d['path']}: {$d['message']}";
}

function formatAssertionHealthError(array $diags): string {
    $parts = [];
    foreach ($diags as $d) {
        $parts[] = "{$d['code']}@{$d['path']}";
    }
    return "assertion health check failed (" . count($diags) . " issue(s)): " . implode('; ', $parts);
}

function resolveAssertHealthMode(array $case): string {
    $mode = strtolower(trim((string)(getenv('SPEC_RUNNER_ASSERT_HEALTH') ?: 'ignore')));
    if ($mode === '') {
        $mode = 'ignore';
    }
    if (isset($case['assert_health'])) {
        if (!is_array($case['assert_health'])) {
            throw new SchemaError('assert_health must be a mapping when provided');
        }
        if (array_key_exists('mode', $case['assert_health'])) {
            $mode = strtolower(trim((string)$case['assert_health']['mode']));
        }
    }
    if (!in_array($mode, ['ignore', 'warn', 'error'], true)) {
        throw new SchemaError('assert_health.mode must be one of: ignore, warn, error');
    }
    return $mode;
}

final class SpecLangEnv {
    public array $vars;
    public ?SpecLangEnv $parent;

    public function __construct(array $vars, ?SpecLangEnv $parent) {
        $this->vars = $vars;
        $this->parent = $parent;
    }
}

function specLangDefaultLimits(): array {
    return [
        'max_steps' => 20000,
        'max_nodes' => 20000,
        'max_literal_bytes' => 262144,
        'timeout_ms' => 200,
    ];
}

function specLangLimitsFromHarness(array $case): array {
    $defaults = specLangDefaultLimits();
    $harness = $case['harness'] ?? [];
    if (!is_array($harness)) {
        throw new SchemaError('harness must be a mapping');
    }
    $cfg = $harness['spec_lang'] ?? [];
    if ($cfg === null || $cfg === []) {
        return $defaults;
    }
    if (!is_array($cfg)) {
        throw new SchemaError('harness.spec_lang must be a mapping');
    }
    foreach ($defaults as $field => $default) {
        if (!array_key_exists($field, $cfg)) {
            continue;
        }
        $raw = $cfg[$field];
        if (!is_int($raw)) {
            throw new SchemaError("harness.spec_lang.{$field} must be an integer");
        }
        $min = $field === 'timeout_ms' ? 0 : 1;
        if ($raw < $min) {
            throw new SchemaError("harness.spec_lang.{$field} must be >= {$min}");
        }
        $defaults[$field] = $raw;
    }
    return $defaults;
}

function specLangUnsetSentinel(): object {
    static $sentinel = null;
    if ($sentinel === null) {
        $sentinel = new stdClass();
    }
    return $sentinel;
}

function specLangTick(array &$state): void {
    $state['steps'] += 1;
    if ($state['steps'] > $state['limits']['max_steps']) {
        throw new RuntimeException('spec_lang budget exceeded: steps');
    }
    $timeout = (int)$state['limits']['timeout_ms'];
    if ($timeout > 0) {
        $elapsedMs = (int)floor((microtime(true) - (float)$state['started']) * 1000.0);
        if ($elapsedMs > $timeout) {
            throw new RuntimeException('spec_lang budget exceeded: timeout');
        }
    }
}

function specLangValidateExprShape(mixed $expr, array $limits): void {
    $stack = [$expr];
    $nodes = 0;
    $literalBytes = 0;
    while (count($stack) > 0) {
        $cur = array_pop($stack);
        $nodes += 1;
        if ($nodes > $limits['max_nodes']) {
            throw new RuntimeException('spec_lang budget exceeded: nodes');
        }
        if (is_string($cur)) {
            $literalBytes += strlen($cur);
        }
        if ($literalBytes > $limits['max_literal_bytes']) {
            throw new RuntimeException('spec_lang budget exceeded: literal_size');
        }
        if (is_array($cur) && isListArray($cur)) {
            foreach ($cur as $child) {
                $stack[] = $child;
            }
        }
    }
}

function specLangLookup(SpecLangEnv $env, string $name): mixed {
    $cur = $env;
    $unset = specLangUnsetSentinel();
    while ($cur !== null) {
        if (array_key_exists($name, $cur->vars)) {
            $value = $cur->vars[$name];
            if ($value === $unset) {
                throw new SchemaError("uninitialized variable: {$name}");
            }
            return $value;
        }
        $cur = $cur->parent;
    }
    throw new SchemaError("undefined variable: {$name}");
}

function specLangJsonTypeName(mixed $value): string {
    if ($value === null) {
        return 'null';
    }
    if (is_bool($value)) {
        return 'bool';
    }
    if (is_int($value) || is_float($value)) {
        return 'number';
    }
    if (is_string($value)) {
        return 'string';
    }
    if (is_array($value)) {
        return isListArray($value) ? 'list' : 'dict';
    }
    return 'unknown';
}

function specLangNormalizeJsonTypeToken(mixed $value): string {
    $token = strtolower(trim((string)$value));
    if ($token === 'boolean') {
        return 'bool';
    }
    if ($token === 'array') {
        return 'list';
    }
    if ($token === 'object') {
        return 'dict';
    }
    return $token;
}

function specLangDeepEquals(mixed $left, mixed $right): bool {
    if (gettype($left) !== gettype($right)) {
        return false;
    }
    if (is_array($left) && is_array($right)) {
        if (isListArray($left) !== isListArray($right)) {
            return false;
        }
        if (isListArray($left)) {
            if (count($left) !== count($right)) {
                return false;
            }
            for ($i = 0; $i < count($left); $i++) {
                if (!specLangDeepEquals($left[$i], $right[$i])) {
                    return false;
                }
            }
            return true;
        }
        $lKeys = array_keys($left);
        $rKeys = array_keys($right);
        sort($lKeys, SORT_STRING);
        sort($rKeys, SORT_STRING);
        if ($lKeys !== $rKeys) {
            return false;
        }
        foreach ($lKeys as $k) {
            if (!specLangDeepEquals($left[$k], $right[$k])) {
                return false;
            }
        }
        return true;
    }
    return $left === $right;
}

function specLangRequireListArg(string $op, mixed $value): array {
    if (!is_array($value) || !isListArray($value)) {
        throw new SchemaError("spec_lang {$op} expects list");
    }
    return $value;
}

function specLangRequireDictArg(string $op, mixed $value): array {
    if (!is_array($value) || isListArray($value)) {
        throw new SchemaError("spec_lang {$op} expects dict");
    }
    return $value;
}

function specLangRequireNumericArg(string $op, mixed $value): int|float {
    if (!is_int($value) && !is_float($value)) {
        throw new SchemaError("spec_lang {$op} expects numeric args");
    }
    return $value;
}

function specLangRequireIntArg(string $op, mixed $value): int {
    if (!is_int($value)) {
        throw new SchemaError("spec_lang {$op} expects integer args");
    }
    return $value;
}

function specLangRoundHalfAwayFromZero(int|float $v): int {
    if ($v >= 0) {
        return (int)floor($v + 0.5);
    }
    return (int)ceil($v - 0.5);
}

function specLangIsClosure(mixed $value): bool {
    return is_array($value) && ($value['__type'] ?? null) === 'closure' && ($value['env'] ?? null) instanceof SpecLangEnv;
}

function specLangRequireArity(string $op, array $args, int $n): void {
    if (count($args) !== $n) {
        throw new SchemaError("spec_lang arity error for {$op}: expected {$n} got " . count($args));
    }
}

function specLangRequireMinArity(string $op, array $args, int $n): void {
    if (count($args) < $n) {
        throw new SchemaError("spec_lang arity error for {$op}: expected at least {$n} got " . count($args));
    }
}

function specLangEvalNonTail(mixed $expr, SpecLangEnv $env, mixed $subject, array $limits, array &$state): mixed {
    return specLangEvalTail($expr, $env, $subject, $limits, $state);
}

function specLangEvalBuiltin(string $op, array $args, SpecLangEnv $env, mixed $subject, array $limits, array &$state): mixed {
    if ($op === 'subject') {
        specLangRequireArity($op, $args, 0);
        return $subject;
    }
    if ($op === 'var') {
        specLangRequireArity($op, $args, 1);
        $name = $args[0];
        if (!is_string($name) || trim($name) === '') {
            throw new SchemaError('spec_lang var requires non-empty string name');
        }
        return specLangLookup($env, trim($name));
    }
    if ($op === 'and') {
        specLangRequireMinArity($op, $args, 1);
        foreach ($args as $arg) {
            if (!((bool)specLangEvalNonTail($arg, $env, $subject, $limits, $state))) {
                return false;
            }
        }
        return true;
    }
    if ($op === 'or') {
        specLangRequireMinArity($op, $args, 1);
        foreach ($args as $arg) {
            if ((bool)specLangEvalNonTail($arg, $env, $subject, $limits, $state)) {
                return true;
            }
        }
        return false;
    }
    if ($op === 'not') {
        specLangRequireArity($op, $args, 1);
        return !((bool)specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
    }
    if ($op === 'contains' || $op === 'starts_with' || $op === 'ends_with' || $op === 'json_type' || $op === 'has_key') {
        if (count($args) === 1) {
            $left = $subject;
            $right = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        } elseif (count($args) === 2) {
            $left = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
            $right = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        } else {
            throw new SchemaError("spec_lang arity error for {$op}");
        }
        if ($op === 'contains') {
            return str_contains((string)$left, (string)$right);
        }
        if ($op === 'starts_with') {
            return str_starts_with((string)$left, (string)$right);
        }
        if ($op === 'ends_with') {
            return str_ends_with((string)$left, (string)$right);
        }
        if ($op === 'json_type') {
            return specLangJsonTypeName($left) === specLangNormalizeJsonTypeToken($right);
        }
        if (!is_array($left) || isListArray($left)) {
            return false;
        }
        return array_key_exists((string)$right, $left);
    }
    if (
        $op === 'is_null'
        || $op === 'is_bool'
        || $op === 'is_boolean'
        || $op === 'is_number'
        || $op === 'is_string'
        || $op === 'is_list'
        || $op === 'is_array'
        || $op === 'is_dict'
        || $op === 'is_object'
    ) {
        specLangRequireArity($op, $args, 1);
        $jsonType = specLangJsonTypeName(specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        if ($op === 'is_null') {
            return $jsonType === 'null';
        }
        if ($op === 'is_bool') {
            return $jsonType === 'bool';
        }
        if ($op === 'is_boolean') {
            return $jsonType === 'bool';
        }
        if ($op === 'is_number') {
            return $jsonType === 'number';
        }
        if ($op === 'is_string') {
            return $jsonType === 'string';
        }
        if ($op === 'is_list') {
            return $jsonType === 'list';
        }
        if ($op === 'is_array') {
            return $jsonType === 'list';
        }
        if ($op === 'is_object') {
            return $jsonType === 'dict';
        }
        return $jsonType === 'dict';
    }
    if ($op === 'regex_match') {
        specLangRequireArity($op, $args, 2);
        $subjectText = (string)specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $pattern = (string)specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        $ok = @preg_match('/' . str_replace('/', '\\/', $pattern) . '/u', $subjectText);
        if ($ok === false) {
            throw new SchemaError("invalid regex pattern: {$pattern}");
        }
        return $ok === 1;
    }
    if ($op === 'eq') {
        specLangRequireArity($op, $args, 2);
        return specLangEvalNonTail($args[0], $env, $subject, $limits, $state) === specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
    }
    if ($op === 'neq') {
        specLangRequireArity($op, $args, 2);
        return specLangEvalNonTail($args[0], $env, $subject, $limits, $state) !== specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
    }
    if ($op === 'equals') {
        specLangRequireArity($op, $args, 2);
        return specLangDeepEquals(
            specLangEvalNonTail($args[0], $env, $subject, $limits, $state),
            specLangEvalNonTail($args[1], $env, $subject, $limits, $state),
        );
    }
    if ($op === 'lt' || $op === 'lte' || $op === 'gt' || $op === 'gte') {
        specLangRequireArity($op, $args, 2);
        $left = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $right = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        if (!((is_int($left) || is_float($left)) && (is_int($right) || is_float($right)))) {
            throw new SchemaError("spec_lang {$op} expects numeric args");
        }
        if ($op === 'lt') {
            return $left < $right;
        }
        if ($op === 'lte') {
            return $left <= $right;
        }
        if ($op === 'gt') {
            return $left > $right;
        }
        return $left >= $right;
    }
    if ($op === 'xor') {
        specLangRequireArity($op, $args, 2);
        return ((bool)specLangEvalNonTail($args[0], $env, $subject, $limits, $state))
            xor ((bool)specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
    }
    if ($op === 'in') {
        specLangRequireArity($op, $args, 2);
        $member = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $container = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        if (is_array($container)) {
            if (isListArray($container)) {
                return in_array($member, $container, true);
            }
            return array_key_exists((string)$member, $container);
        }
        if (is_string($container)) {
            return str_contains($container, (string)$member);
        }
        throw new SchemaError('spec_lang in expects list/dict/string container');
    }
    if ($op === 'includes') {
        specLangRequireArity($op, $args, 2);
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $needle = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        foreach ($seq as $item) {
            if (specLangDeepEquals($item, $needle)) {
                return true;
            }
        }
        return false;
    }
    if ($op === 'get') {
        specLangRequireArity($op, $args, 2);
        $obj = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $key = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        if (is_array($obj) && !isListArray($obj)) {
            return $obj[(string)$key] ?? null;
        }
        if (is_array($obj) && isListArray($obj)) {
            if (!is_int($key) || $key < 0 || $key >= count($obj)) {
                return null;
            }
            return $obj[$key];
        }
        throw new SchemaError('spec_lang get expects dict or list');
    }
    if ($op === 'len' || $op === 'count') {
        specLangRequireArity($op, $args, 1);
        $value = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        if (is_string($value)) {
            return strlen($value);
        }
        if (is_array($value)) {
            return count($value);
        }
        throw new SchemaError('spec_lang len expects string/list/dict');
    }
    if ($op === 'trim' || $op === 'lower' || $op === 'upper') {
        specLangRequireArity($op, $args, 1);
        $value = (string)specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        if ($op === 'trim') {
            return trim($value);
        }
        if ($op === 'lower') {
            return strtolower($value);
        }
        return strtoupper($value);
    }
    if ($op === 'json_parse') {
        specLangRequireArity($op, $args, 1);
        $raw = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        if (!is_string($raw)) {
            throw new SchemaError('spec_lang json_parse expects string input');
        }
        try {
            return json_decode($raw, true, 512, JSON_THROW_ON_ERROR);
        } catch (JsonException $e) {
            throw new SchemaError('spec_lang json_parse invalid JSON');
        }
    }
    if ($op === 'add' || $op === 'sub' || $op === 'mul' || $op === 'div' || $op === 'pow') {
        specLangRequireArity($op, $args, 2);
        $left = specLangRequireNumericArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $right = specLangRequireNumericArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        if ($op === 'add') {
            return $left + $right;
        }
        if ($op === 'sub') {
            return $left - $right;
        }
        if ($op === 'mul') {
            return $left * $right;
        }
        if ($op === 'div') {
            if ($right == 0) {
                throw new SchemaError('spec_lang div expects non-zero divisor');
            }
            return $left / $right;
        }
        return $left ** $right;
    }
    if ($op === 'mod') {
        specLangRequireArity($op, $args, 2);
        $left = specLangRequireIntArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $right = specLangRequireIntArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        if ($right === 0) {
            throw new SchemaError('spec_lang mod expects non-zero divisor');
        }
        return $left % $right;
    }
    if ($op === 'abs' || $op === 'negate' || $op === 'inc' || $op === 'dec' || $op === 'round' || $op === 'floor' || $op === 'ceil') {
        specLangRequireArity($op, $args, 1);
        $value = specLangRequireNumericArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        if ($op === 'abs') {
            return abs($value);
        }
        if ($op === 'negate') {
            return -$value;
        }
        if ($op === 'inc') {
            return $value + 1;
        }
        if ($op === 'dec') {
            return $value - 1;
        }
        if ($op === 'round') {
            return specLangRoundHalfAwayFromZero($value);
        }
        if ($op === 'floor') {
            return (int)floor((float)$value);
        }
        return (int)ceil((float)$value);
    }
    if ($op === 'clamp' || $op === 'between') {
        specLangRequireArity($op, $args, 3);
        $low = specLangRequireNumericArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $high = specLangRequireNumericArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        $value = specLangRequireNumericArg($op, specLangEvalNonTail($args[2], $env, $subject, $limits, $state));
        if ($low > $high) {
            throw new SchemaError("spec_lang {$op} expects low <= high");
        }
        if ($op === 'clamp') {
            return min(max($value, $low), $high);
        }
        return $value >= $low && $value <= $high;
    }
    if ($op === 'compare') {
        specLangRequireArity($op, $args, 2);
        $left = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $right = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        if ((is_int($left) || is_float($left)) && (is_int($right) || is_float($right))) {
            return $left <=> $right;
        }
        if (is_string($left) && is_string($right)) {
            return $left <=> $right;
        }
        throw new SchemaError('spec_lang compare expects both args to be numbers or strings');
    }
    if ($op === 'range') {
        specLangRequireArity($op, $args, 2);
        $start = specLangRequireIntArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $end = specLangRequireIntArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        $out = [];
        for ($i = $start; $i < $end; $i++) {
            $out[] = $i;
        }
        return $out;
    }
    if ($op === 'repeat') {
        specLangRequireArity($op, $args, 2);
        $value = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $count = specLangRequireIntArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        if ($count < 0) {
            throw new SchemaError('spec_lang repeat expects non-negative count');
        }
        return array_fill(0, $count, $value);
    }
    if ($op === 'slice') {
        specLangRequireArity($op, $args, 3);
        $start = specLangRequireIntArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $end = specLangRequireIntArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        $seq = specLangRequireListArg($op, specLangEvalNonTail($args[2], $env, $subject, $limits, $state));
        return array_slice($seq, $start, max(0, $end - $start));
    }
    if ($op === 'reverse') {
        specLangRequireArity($op, $args, 1);
        return array_values(array_reverse(specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state))));
    }
    if ($op === 'zip') {
        specLangRequireArity($op, $args, 2);
        $left = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $right = specLangRequireListArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        $n = min(count($left), count($right));
        $out = [];
        for ($i = 0; $i < $n; $i++) {
            $out[] = [$left[$i], $right[$i]];
        }
        return $out;
    }
    if ($op === 'replace') {
        specLangRequireArity($op, $args, 3);
        $text = (string)specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $old = (string)specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        $new = (string)specLangEvalNonTail($args[2], $env, $subject, $limits, $state);
        return str_replace($old, $new, $text);
    }
    if ($op === 'pad_left' || $op === 'pad_right') {
        specLangRequireArity($op, $args, 3);
        $text = (string)specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $width = specLangRequireIntArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        $fill = (string)specLangEvalNonTail($args[2], $env, $subject, $limits, $state);
        if ($fill === '') {
            throw new SchemaError("spec_lang {$op} expects non-empty pad string");
        }
        if ($op === 'pad_left') {
            while (strlen($text) < $width) {
                $text = $fill . $text;
            }
            return $width > 0 ? substr($text, -$width) : '';
        }
        while (strlen($text) < $width) {
            $text .= $fill;
        }
        return $width > 0 ? substr($text, 0, $width) : '';
    }
    if ($op === 'identity') {
        specLangRequireArity($op, $args, 1);
        return specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
    }
    if ($op === 'always') {
        specLangRequireArity($op, $args, 2);
        return specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
    }
    if ($op === 'keys') {
        specLangRequireArity($op, $args, 1);
        return array_values(array_keys(specLangRequireDictArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state))));
    }
    if ($op === 'values') {
        specLangRequireArity($op, $args, 1);
        return array_values(specLangRequireDictArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state)));
    }
    if ($op === 'entries') {
        specLangRequireArity($op, $args, 1);
        $obj = specLangRequireDictArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $out = [];
        foreach ($obj as $k => $v) {
            $out[] = [(string)$k, $v];
        }
        return $out;
    }
    if ($op === 'merge') {
        specLangRequireArity($op, $args, 2);
        $left = specLangRequireDictArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $right = specLangRequireDictArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        return array_merge($left, $right);
    }
    if ($op === 'assoc') {
        specLangRequireArity($op, $args, 3);
        $key = (string)specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $value = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        $obj = specLangRequireDictArg($op, specLangEvalNonTail($args[2], $env, $subject, $limits, $state));
        $obj[$key] = $value;
        return $obj;
    }
    if ($op === 'dissoc') {
        specLangRequireArity($op, $args, 2);
        $key = (string)specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $obj = specLangRequireDictArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        unset($obj[$key]);
        return $obj;
    }
    if ($op === 'pick' || $op === 'omit') {
        specLangRequireArity($op, $args, 2);
        $keys = specLangRequireListArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $obj = specLangRequireDictArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        $set = [];
        foreach ($keys as $k) {
            $set[(string)$k] = true;
        }
        $out = [];
        foreach ($obj as $k => $v) {
            $has = array_key_exists((string)$k, $set);
            if (($op === 'pick' && $has) || ($op === 'omit' && !$has)) {
                $out[(string)$k] = $v;
            }
        }
        return $out;
    }
    if ($op === 'prop_eq') {
        specLangRequireArity($op, $args, 3);
        $key = (string)specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $expected = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        $obj = specLangRequireDictArg($op, specLangEvalNonTail($args[2], $env, $subject, $limits, $state));
        $actual = $obj[$key] ?? null;
        return specLangDeepEquals($actual, $expected);
    }
    if ($op === 'where') {
        specLangRequireArity($op, $args, 2);
        $spec = specLangRequireDictArg($op, specLangEvalNonTail($args[0], $env, $subject, $limits, $state));
        $obj = specLangRequireDictArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        foreach ($spec as $k => $pred) {
            $actual = $obj[(string)$k] ?? null;
            if (specLangIsClosure($pred)) {
                if (count($pred['params']) !== 1) {
                    throw new SchemaError('spec_lang where callable predicate must accept one argument');
                }
                $vars = [(string)$pred['params'][0] => $actual];
                $predicateValue = specLangEvalTail($pred['body'], new SpecLangEnv($vars, $pred['env']), $subject, $limits, $state);
                if (!((bool)$predicateValue)) {
                    return false;
                }
            } else {
                if (!specLangDeepEquals($actual, $pred)) {
                    return false;
                }
            }
        }
        return true;
    }
    if ($op === 'compose' || $op === 'pipe') {
        specLangRequireArity($op, $args, 3);
        $f = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $g = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        $x = specLangEvalNonTail($args[2], $env, $subject, $limits, $state);
        if (!specLangIsClosure($f) || !specLangIsClosure($g)) {
            throw new SchemaError("spec_lang {$op} expects fn closures");
        }
        $applyOne = static function(array $closure, mixed $arg, mixed $subject, array $limits, array &$state): mixed {
            $params = $closure['params'];
            if (count($params) !== 1) {
                throw new SchemaError('spec_lang compose/pipe closures must accept one argument');
            }
            $vars = [(string)$params[0] => $arg];
            return specLangEvalTail($closure['body'], new SpecLangEnv($vars, $closure['env']), $subject, $limits, $state);
        };
        if ($op === 'compose') {
            return $applyOne($f, $applyOne($g, $x, $subject, $limits, $state), $subject, $limits, $state);
        }
        return $applyOne($g, $applyOne($f, $x, $subject, $limits, $state), $subject, $limits, $state);
    }
    if ($op === 'zip_with') {
        specLangRequireArity($op, $args, 3);
        $fn = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        if (!specLangIsClosure($fn)) {
            throw new SchemaError('spec_lang zip_with expects fn closure');
        }
        $left = specLangRequireListArg($op, specLangEvalNonTail($args[1], $env, $subject, $limits, $state));
        $right = specLangRequireListArg($op, specLangEvalNonTail($args[2], $env, $subject, $limits, $state));
        $params = $fn['params'];
        if (count($params) !== 2) {
            throw new SchemaError('spec_lang zip_with closure must accept two arguments');
        }
        $n = min(count($left), count($right));
        $out = [];
        for ($i = 0; $i < $n; $i++) {
            $vars = [(string)$params[0] => $left[$i], (string)$params[1] => $right[$i]];
            $out[] = specLangEvalTail($fn['body'], new SpecLangEnv($vars, $fn['env']), $subject, $limits, $state);
        }
        return $out;
    }
    throw new SchemaError("unsupported spec_lang symbol: {$op}");
}

function specLangEvalTail(mixed $expr, SpecLangEnv $env, mixed $subject, array $limits, array &$state): mixed {
    $currentExpr = $expr;
    $currentEnv = $env;
    while (true) {
        specLangTick($state);
        if (is_string($currentExpr) || is_int($currentExpr) || is_float($currentExpr) || is_bool($currentExpr) || $currentExpr === null) {
            return $currentExpr;
        }
        if (!is_array($currentExpr) || !isListArray($currentExpr)) {
            throw new SchemaError('spec_lang expression must be list-based s-expr or scalar literal');
        }
        if (count($currentExpr) === 0) {
            throw new SchemaError('spec_lang expression list must not be empty');
        }
        $head = $currentExpr[0];
        if (!is_string($head) || trim($head) === '') {
            throw new SchemaError('spec_lang expression head must be non-empty string symbol');
        }
        $op = $head;
        $args = array_slice($currentExpr, 1);

        if ($op === 'if') {
            specLangRequireArity($op, $args, 3);
            $cond = specLangEvalNonTail($args[0], $currentEnv, $subject, $limits, $state);
            $currentExpr = ((bool)$cond) ? $args[1] : $args[2];
            continue;
        }
        if ($op === 'let') {
            specLangRequireArity($op, $args, 2);
            $rawBindings = $args[0];
            $body = $args[1];
            if (!is_array($rawBindings) || !isListArray($rawBindings)) {
                throw new SchemaError('spec_lang let bindings must be a list');
            }
            $nextEnv = new SpecLangEnv([], $currentEnv);
            $pairs = [];
            $unset = specLangUnsetSentinel();
            foreach ($rawBindings as $binding) {
                if (!is_array($binding) || !isListArray($binding) || count($binding) !== 2) {
                    throw new SchemaError('spec_lang let binding must be [name, expr]');
                }
                $name = $binding[0];
                if (!is_string($name) || trim($name) === '') {
                    throw new SchemaError('spec_lang let binding name must be non-empty string');
                }
                $key = trim($name);
                if (array_key_exists($key, $nextEnv->vars)) {
                    throw new SchemaError("duplicate let binding: {$key}");
                }
                $nextEnv->vars[$key] = $unset;
                $pairs[] = [$key, $binding[1]];
            }
            foreach ($pairs as $pair) {
                [$key, $rhs] = $pair;
                $nextEnv->vars[$key] = specLangEvalNonTail($rhs, $nextEnv, $subject, $limits, $state);
            }
            $currentExpr = $body;
            $currentEnv = $nextEnv;
            continue;
        }
        if ($op === 'fn') {
            specLangRequireArity($op, $args, 2);
            $rawParams = $args[0];
            $body = $args[1];
            if (!is_array($rawParams) || !isListArray($rawParams)) {
                throw new SchemaError('spec_lang fn params must be a list');
            }
            $params = [];
            foreach ($rawParams as $param) {
                if (!is_string($param) || trim($param) === '') {
                    throw new SchemaError('spec_lang fn param must be non-empty string');
                }
                $key = trim($param);
                if (in_array($key, $params, true)) {
                    throw new SchemaError("duplicate fn param: {$key}");
                }
                $params[] = $key;
            }
            return ['__type' => 'closure', 'params' => $params, 'body' => $body, 'env' => $currentEnv];
        }
        if ($op === 'call') {
            specLangRequireMinArity($op, $args, 1);
            $fnValue = specLangEvalNonTail($args[0], $currentEnv, $subject, $limits, $state);
            $evalArgs = [];
            foreach (array_slice($args, 1) as $arg) {
                $evalArgs[] = specLangEvalNonTail($arg, $currentEnv, $subject, $limits, $state);
            }
            if (!specLangIsClosure($fnValue)) {
                throw new SchemaError('spec_lang call expects fn closure');
            }
            $params = $fnValue['params'];
            if (count($evalArgs) !== count($params)) {
                throw new SchemaError('spec_lang call argument count mismatch');
            }
            $vars = [];
            foreach ($params as $i => $name) {
                $vars[(string)$name] = $evalArgs[$i];
            }
            $currentEnv = new SpecLangEnv($vars, $fnValue['env']);
            $currentExpr = $fnValue['body'];
            continue;
        }
        return specLangEvalBuiltin($op, $args, $currentEnv, $subject, $limits, $state);
    }
}

function specLangEvalPredicate(mixed $expr, mixed $subject, array $limits, array $symbols = []): bool {
    specLangValidateExprShape($expr, $limits);
    $state = ['steps' => 0, 'started' => microtime(true), 'limits' => $limits];
    $root = [];
    foreach ($symbols as $rawName => $value) {
        $name = trim((string)$rawName);
        if ($name === '') {
            throw new SchemaError('spec_lang symbol name must be non-empty');
        }
        $root[$name] = $value;
    }
    $root['subject'] = $subject;
    $value = specLangEvalTail($expr, new SpecLangEnv($root, null), $subject, $limits, $state);
    return (bool)$value;
}

function compileYamlExprLiteral(mixed $value, string $fieldPath): mixed {
    if (is_array($value)) {
        if (isListArray($value)) {
            $out = [];
            foreach ($value as $idx => $item) {
                $out[] = compileYamlExprLiteral($item, "{$fieldPath}[{$idx}]");
            }
            return $out;
        }
        $out = [];
        foreach ($value as $k => $v) {
            $out[(string)$k] = compileYamlExprLiteral($v, "{$fieldPath}." . (string)$k);
        }
        return $out;
    }
    if (is_string($value) || is_int($value) || is_float($value) || is_bool($value) || $value === null) {
        return $value;
    }
    throw new SchemaError("{$fieldPath}: unsupported literal value type");
}

function compileYamlExprToSexpr(mixed $node, string $fieldPath): mixed {
    if (is_string($node) || is_int($node) || is_float($node) || is_bool($node) || $node === null) {
        return $node;
    }
    if (is_array($node) && isListArray($node)) {
        throw new SchemaError(
            "{$fieldPath}: list expressions are not allowed; use operator-keyed mapping AST and wrap literal lists with lit"
        );
    }
    if (!is_array($node)) {
        throw new SchemaError("{$fieldPath}: expression node must be scalar or mapping");
    }
    $keys = array_keys($node);
    if (count($keys) === 0) {
        throw new SchemaError("{$fieldPath}: expression mapping must not be empty");
    }
    if (array_key_exists('lit', $node)) {
        if (count($keys) !== 1) {
            throw new SchemaError("{$fieldPath}: lit wrapper must be the only key in a mapping");
        }
        return compileYamlExprLiteral($node['lit'], "{$fieldPath}.lit");
    }
    if (count($keys) !== 1) {
        throw new SchemaError("{$fieldPath}: expression mapping must have exactly one operator key");
    }
    $op = trim((string)$keys[0]);
    if ($op === '') {
        throw new SchemaError("{$fieldPath}: operator key must be non-empty");
    }
    $rawArgs = $node[$keys[0]];
    if ($op === 'ref') {
        throw new SchemaError("{$fieldPath}.ref: ref mapping is not supported; use var: subject");
    }
    if ($op === 'var') {
        if (is_array($rawArgs)) {
            throw new SchemaError("{$fieldPath}.var: var list form is not supported; use var: <name>");
        }
        if (!is_string($rawArgs) || trim($rawArgs) === '') {
            throw new SchemaError("{$fieldPath}.var: variable name must be a non-empty string");
        }
        return ['var', trim($rawArgs)];
    }
    if ($op === 'fn') {
        if (!is_array($rawArgs) || !isListArray($rawArgs) || count($rawArgs) !== 2) {
            throw new SchemaError("{$fieldPath}.fn: fn args must be [params, body]");
        }
        $rawParams = $rawArgs[0];
        if (!is_array($rawParams) || !isListArray($rawParams)) {
            throw new SchemaError("{$fieldPath}.fn[0]: params must be a list of variable names");
        }
        $params = [];
        foreach ($rawParams as $idx => $param) {
            if (!is_string($param) || trim($param) === '') {
                throw new SchemaError("{$fieldPath}.fn[0][{$idx}]: param name must be a non-empty string");
            }
            $params[] = trim($param);
        }
        $body = compileYamlExprToSexpr($rawArgs[1], "{$fieldPath}.fn[1]");
        return ['fn', $params, $body];
    }
    if (!is_array($rawArgs) || !isListArray($rawArgs)) {
        throw new SchemaError("{$fieldPath}.{$op}: operator args must be a list");
    }
    $args = [];
    foreach ($rawArgs as $idx => $arg) {
        $args[] = compileYamlExprToSexpr($arg, "{$fieldPath}.{$op}[{$idx}]");
    }
    return array_merge([$op], $args);
}

function asNonEmptyStringList(mixed $value, string $field): array {
    if ($value === null) {
        return [];
    }
    if (!is_array($value) || !isListArray($value)) {
        throw new SchemaError("{$field} must be a list of non-empty strings");
    }
    $out = [];
    foreach ($value as $idx => $item) {
        if (!is_string($item) || trim($item) === '') {
            throw new SchemaError("{$field}[{$idx}] must be a non-empty string");
        }
        $out[] = trim($item);
    }
    return $out;
}

function resolveLibraryPath(string $baseDocPath, string $relPath): string {
    $raw = trim($relPath);
    if ($raw === '') {
        throw new SchemaError('harness.spec_lang.library_paths item must be non-empty');
    }
    if (str_starts_with($raw, 'external://')) {
        throw new SchemaError('harness.spec_lang.library_paths external refs are denied by default');
    }
    $resolved = resolveContractPath($baseDocPath, $raw, 'harness.spec_lang.library_paths');
    if (!is_file($resolved)) {
        throw new SchemaError("library path does not exist: {$relPath}");
    }
    return $resolved;
}

function loadSpecLangLibraryDoc(string $path): array {
    $imports = [];
    $bindings = [];
    $exports = [];
    $compileScope = function(mixed $scope, string $fieldPrefix) use ($path): array {
        if ($scope === null) {
            return [];
        }
        if (!is_array($scope) || isListArray($scope)) {
            throw new SchemaError("spec_lang.library {$fieldPrefix} must be a mapping when provided");
        }
        $out = [];
        foreach ($scope as $rawName => $expr) {
            $name = trim((string)$rawName);
            if ($name === '') {
                throw new SchemaError("spec_lang.library {$fieldPrefix} function name must be non-empty");
            }
            $out[$name] = compileYamlExprToSexpr($expr, "{$path} {$fieldPrefix}.{$name}");
        }
        return $out;
    };
    foreach (parseCases($path) as $case) {
        $type = trim((string)($case['type'] ?? ''));
        if ($type !== 'spec_lang.library') {
            continue;
        }
        foreach (asNonEmptyStringList($case['imports'] ?? null, 'imports') as $imp) {
            $imports[] = $imp;
        }
        $functions = $case['functions'] ?? null;
        if (!is_array($functions) || isListArray($functions)) {
            throw new SchemaError('spec_lang.library requires functions mapping with public/private scopes');
        }
        $public = $compileScope($functions['public'] ?? null, 'functions.public');
        $private = $compileScope($functions['private'] ?? null, 'functions.private');
        if (count($public) === 0 && count($private) === 0) {
            throw new SchemaError('spec_lang.library requires non-empty functions.public or functions.private mapping');
        }
        foreach (array_keys($public) as $name) {
            if (array_key_exists($name, $bindings)) {
                throw new SchemaError("duplicate library function in file {$path}: {$name}");
            }
            $bindings[$name] = $public[$name];
            $exports[] = $name;
        }
        foreach (array_keys($private) as $name) {
            if (array_key_exists($name, $bindings)) {
                throw new SchemaError("duplicate library function in file {$path}: {$name}");
            }
            $bindings[$name] = $private[$name];
        }
    }
    if (count($bindings) === 0) {
        throw new SchemaError("library file has no spec_lang.library functions: {$path}");
    }
    return [
        'path' => $path,
        'imports' => array_values(array_unique($imports)),
        'bindings' => $bindings,
        'exports' => array_values(array_unique($exports)),
    ];
}

function resolveSpecLangLibraryGraph(array $entryDocs): array {
    $docs = [];
    $visiting = [];
    $visited = [];
    $ordered = [];
    $dfs = function(string $path) use (&$dfs, &$docs, &$visiting, &$visited, &$ordered): void {
        if (($visited[$path] ?? false) === true) {
            return;
        }
        if (($visiting[$path] ?? false) === true) {
            throw new SchemaError("library import cycle detected at: {$path}");
        }
        $visiting[$path] = true;
        if (!array_key_exists($path, $docs)) {
            $docs[$path] = loadSpecLangLibraryDoc($path);
        }
        foreach ($docs[$path]['imports'] as $rel) {
            $dep = resolveLibraryPath($path, (string)$rel);
            $dfs($dep);
        }
        unset($visiting[$path]);
        $visited[$path] = true;
        $ordered[] = $path;
    };
    foreach ($entryDocs as $entry) {
        $dfs((string)$entry);
    }
    $out = [];
    foreach ($ordered as $path) {
        $out[] = $docs[$path];
    }
    return $out;
}

function compileSpecLangSymbolBindings(array $bindings, array $limits): array {
    $slots = [];
    foreach ($bindings as $rawName => $_expr) {
        $name = trim((string)$rawName);
        if ($name === '') {
            throw new SchemaError('spec_lang symbol binding name must be non-empty');
        }
        if (array_key_exists($name, $slots)) {
            throw new SchemaError("duplicate symbol binding: {$name}");
        }
        $slots[$name] = specLangUnsetSentinel();
    }
    $env = new SpecLangEnv($slots, null);
    $state = ['steps' => 0, 'started' => microtime(true), 'limits' => $limits];
    foreach ($bindings as $rawName => $rawExpr) {
        $name = trim((string)$rawName);
        specLangValidateExprShape($rawExpr, $limits);
        $env->vars[$name] = specLangEvalNonTail($rawExpr, $env, null, $limits, $state);
    }
    return $env->vars;
}

function loadSpecLangSymbolsForCase(string $fixturePath, array $case, array $limits): array {
    $harness = $case['harness'] ?? [];
    if (!is_array($harness) || isListArray($harness)) {
        return [];
    }
    if (!array_key_exists('spec_lang', $harness) || $harness['spec_lang'] === null) {
        return [];
    }
    $cfg = $harness['spec_lang'];
    if (!is_array($cfg) || isListArray($cfg)) {
        throw new SchemaError('harness.spec_lang must be a mapping');
    }
    $libPaths = asNonEmptyStringList($cfg['library_paths'] ?? null, 'harness.spec_lang.library_paths');
    if (count($libPaths) === 0) {
        return [];
    }
    $entryDocs = [];
    foreach ($libPaths as $rel) {
        $entryDocs[] = resolveLibraryPath($fixturePath, $rel);
    }
    $graph = resolveSpecLangLibraryGraph($entryDocs);

    $mergedBindings = [];
    $exportAllow = [];
    foreach ($graph as $doc) {
        foreach ($doc['bindings'] as $name => $expr) {
            if (array_key_exists($name, $mergedBindings)) {
                throw new SchemaError("duplicate exported library symbol across imports: {$name}");
            }
            $mergedBindings[$name] = $expr;
        }
        foreach ($doc['exports'] as $name) {
            $exportAllow[(string)$name] = true;
        }
    }

    $consumerExports = asNonEmptyStringList($cfg['exports'] ?? null, 'harness.spec_lang.exports');
    if (count($consumerExports) > 0) {
        $exportAllow = [];
        foreach ($consumerExports as $name) {
            $exportAllow[$name] = true;
        }
    }
    if (count($exportAllow) > 0) {
        $filtered = [];
        $unknown = [];
        foreach ($exportAllow as $name => $_true) {
            if (!array_key_exists($name, $mergedBindings)) {
                $unknown[] = $name;
                continue;
            }
            $filtered[$name] = $mergedBindings[$name];
        }
        if (count($unknown) > 0) {
            sort($unknown, SORT_STRING);
            throw new SchemaError(
                'harness.spec_lang.exports contains unknown symbols: ' . implode(', ', $unknown)
            );
        }
        $mergedBindings = $filtered;
    }

    return compileSpecLangSymbolBindings($mergedBindings, $limits);
}

function compileLeafExpr(string $op, mixed $value, string $target): array {
    if ($op === 'evaluate') {
        $compiled = compileYamlExprToSexpr($value, "evaluate");
        if (!is_array($compiled) || !isListArray($compiled)) {
            throw new SchemaError('evaluate expression must compile to a list-based s-expr');
        }
        return $compiled;
    }
    if ($op === 'contain') {
        return ['contains', ['subject'], (string)$value];
    }
    if ($op === 'regex') {
        return ['regex_match', ['subject'], (string)$value];
    }
    if ($op === 'json_type') {
        $want = specLangNormalizeJsonTypeToken($value);
        if (!in_array($want, ['null', 'bool', 'number', 'string', 'list', 'dict'], true)) {
            throw new SchemaError("unsupported json_type: {$value}");
        }
        if ($target === 'body_json') {
            return ['json_type', ['subject'], $want];
        }
        return ['json_type', ['json_parse', ['subject']], $want];
    }
    if ($op === 'exists') {
        if ($value !== true && $value !== null) {
            throw new SchemaError('exists only supports value: true (or null)');
        }
        return ['eq', ['subject'], true];
    }
    throw new SchemaError("unsupported op: {$op}");
}

function assertLeafPredicate(
    string $caseId,
    string $path,
    string $target,
    string $op,
    mixed $expr,
    mixed $subject,
    array $specLangLimits,
    array $specLangSymbols = []
): void {
    if (!specLangEvalPredicate($expr, $subject, $specLangLimits, $specLangSymbols)) {
        if ($op === 'json_type') {
            $want = '';
            if (is_array($expr) && count($expr) >= 3) {
                $want = (string)$expr[2];
            }
            throw new AssertionFailure(
                "[case_id={$caseId} assert_path={$path} target={$target} op=json_type] json_type({$want}) failed"
            );
        }
        $msg = $op === 'evaluate' ? 'evaluate assertion failed' : "{$op} assertion failed";
        throw new AssertionFailure(
            "[case_id={$caseId} assert_path={$path} target={$target} op={$op}] {$msg}"
        );
    }
}

function evalAssertNode(
    mixed $node,
    ?string $inheritedTarget,
    string $caseId,
    string $path,
    callable $evalLeaf
): void {
    if (is_array($node) && isListArray($node)) {
        foreach ($node as $i => $child) {
            evalAssertNode($child, $inheritedTarget, $caseId, "{$path}[{$i}]", $evalLeaf);
        }
        return;
    }
    if (!is_array($node)) {
        throw new SchemaError('assert node must be a mapping or list');
    }
    $target = $inheritedTarget;
    if (array_key_exists('target', $node)) {
        $target = trim((string)$node['target']);
    }

    if (array_key_exists('all', $node) || array_key_exists('any', $node)) {
        throw new SchemaError("assert group aliases 'all'/'any' are not supported; use 'must'/'can'");
    }

    $presentGroups = [];
    foreach (['must', 'can', 'cannot'] as $g) {
        if (array_key_exists($g, $node)) {
            $presentGroups[] = $g;
        }
    }

    if (count($presentGroups) > 1) {
        throw new SchemaError('assert group must include exactly one key (must/can/cannot)');
    }

    if (count($presentGroups) === 1) {
        $group = $presentGroups[0];
        $children = $node[$group];
        if (!is_array($children) || !isListArray($children) || count($children) === 0) {
            throw new SchemaError("assert.{$group} must be a non-empty list");
        }
        $extra = array_diff(array_keys($node), [$group, 'target']);
        if (count($extra) > 0) {
            throw new SchemaError('unknown key in assert group: ' . (string)array_values($extra)[0]);
        }

        if ($group === 'must') {
            foreach ($children as $i => $child) {
                evalAssertNode($child, $target, $caseId, "{$path}.must[{$i}]", $evalLeaf);
            }
            return;
        }
        if ($group === 'can') {
            $anyPassed = false;
            foreach ($children as $i => $child) {
                try {
                    evalAssertNode($child, $target, $caseId, "{$path}.can[{$i}]", $evalLeaf);
                    $anyPassed = true;
                    break;
                } catch (AssertionFailure $e) {
                    // Try next branch.
                }
            }
            if (!$anyPassed) {
                throw new AssertionFailure("all 'can' branches failed");
            }
            return;
        }
        if ($group === 'cannot') {
            $passed = 0;
            foreach ($children as $i => $child) {
                try {
                    evalAssertNode($child, $target, $caseId, "{$path}.cannot[{$i}]", $evalLeaf);
                    $passed += 1;
                } catch (AssertionFailure $e) {
                    // Expected failing branch for cannot.
                }
            }
            if ($passed > 0) {
                throw new AssertionFailure("'cannot' failed: {$passed} branch(es) passed");
            }
            return;
        }
    }

    if (array_key_exists('target', $node)) {
        throw new SchemaError('leaf assertion must not include key: target; move target to a parent group');
    }
    if ($target === null || $target === '') {
        throw new SchemaError('assertion leaf requires inherited target from a parent group');
    }
    $evalLeaf($node, $target, $caseId, $path);
}

function evalTextLeaf(
    array $leaf,
    string $subject,
    string $target,
    string $caseId,
    string $path,
    array $specLangLimits,
    array $specLangSymbols
): void {
    if ($target !== 'text') {
        throw new SchemaError('unknown assert target for text.file');
    }
    foreach ($leaf as $op => $raw) {
        if ($op === 'target') {
            continue;
        }
        if (!is_array($raw) || !isListArray($raw)) {
            throw new SchemaError("assertion op '{$op}' must be a list");
        }
        foreach ($raw as $value) {
            $expr = compileLeafExpr($op, $value, $target);
            $subjectForOp = $op === 'exists' ? trim((string)$subject) !== '' : $subject;
            assertLeafPredicate($caseId, $path, $target, $op, $expr, $subjectForOp, $specLangLimits, $specLangSymbols);
        }
    }
}

function firstNonEmptyLine(string $text): ?string {
    $lines = preg_split('/\R/', $text) ?: [];
    foreach ($lines as $line) {
        $trim = trim((string)$line);
        if ($trim !== '') {
            return $trim;
        }
    }
    return null;
}

function evalCliLeaf(
    array $leaf,
    array $captured,
    string $target,
    string $caseId,
    string $path,
    array $specLangLimits,
    array $specLangSymbols
): void {
    foreach ($leaf as $op => $raw) {
        if ($op === 'target') {
            continue;
        }
        if (!is_array($raw) || !isListArray($raw)) {
            throw new SchemaError("assertion op '{$op}' must be a list");
        }
        if ($target === 'stdout' || $target === 'stderr') {
            $subject = $target === 'stdout' ? (string)$captured['stdout'] : (string)$captured['stderr'];
            foreach ($raw as $value) {
                $expr = compileLeafExpr($op, $value, $target);
                $subjectForOp = $op === 'exists' ? trim((string)$subject) !== '' : $subject;
                assertLeafPredicate($caseId, $path, $target, $op, $expr, $subjectForOp, $specLangLimits, $specLangSymbols);
            }
            continue;
        }
        if ($target === 'stdout_path') {
            $line = firstNonEmptyLine((string)$captured['stdout']);
            foreach ($raw as $value) {
                $expr = compileLeafExpr($op, $value, $target);
                if ($op === 'exists') {
                    $subjectForOp = false;
                    if ($line !== null && $line !== '') {
                        $subjectForOp = file_exists($line);
                    }
                } else {
                    $subjectForOp = $line === null ? '' : $line;
                }
                assertLeafPredicate($caseId, $path, $target, $op, $expr, $subjectForOp, $specLangLimits, $specLangSymbols);
            }
            continue;
        }
        if ($target === 'stdout_path_text') {
            $line = firstNonEmptyLine((string)$captured['stdout']);
            if ($line === null && $op !== 'exists') {
                throw new AssertionFailure(
                    "[case_id={$caseId} assert_path={$path} target={$target} op={$op}] expected stdout to contain a path"
                );
            }
            $subject = '';
            if ($line !== null) {
                $loaded = file_get_contents($line);
                if ($loaded === false && $op !== 'exists') {
                    throw new AssertionFailure(
                        "[case_id={$caseId} assert_path={$path} target={$target} op={$op}] cannot read stdout path"
                    );
                }
                if ($loaded !== false) {
                    $subject = $loaded;
                }
            }
            if ($line !== null && $subject === '' && $op !== 'exists') {
                throw new AssertionFailure(
                    "[case_id={$caseId} assert_path={$path} target={$target} op={$op}] cannot read stdout path"
                );
            }
            foreach ($raw as $value) {
                $expr = compileLeafExpr($op, $value, $target);
                $subjectForOp = $op === 'exists' ? trim((string)$subject) !== '' : $subject;
                assertLeafPredicate($caseId, $path, $target, $op, $expr, $subjectForOp, $specLangLimits, $specLangSymbols);
            }
            continue;
        }
        throw new SchemaError("unknown assert target: {$target}");
    }
}

function evaluateTextFileCase(string $fixturePath, array $case): array {
    $mode = resolveAssertHealthMode($case);
    $diags = lintAssertionHealth($case['assert'] ?? []);
    if (count($diags) > 0 && $mode === 'error') {
        return [
            'status' => 'fail',
            'category' => 'assertion',
            'message' => formatAssertionHealthError($diags),
        ];
    }
    if (count($diags) > 0 && $mode === 'warn') {
        foreach ($diags as $d) {
            fwrite(STDERR, formatAssertionHealthWarning($d) . PHP_EOL);
        }
    }

    $subjectPath = resolveTextFilePath($fixturePath, $case);
    $subject = file_get_contents($subjectPath);
    if ($subject === false) {
        throw new RuntimeException("cannot read fixture file: {$subjectPath}");
    }
    $assertSpec = $case['assert'] ?? [];
    $specLangLimits = specLangLimitsFromHarness($case);
    $specLangSymbols = loadSpecLangSymbolsForCase($fixturePath, $case, $specLangLimits);
    evalAssertNode(
        $assertSpec,
        null,
        (string)$case['id'],
        'assert',
        static fn(array $leaf, string $target, string $caseId, string $path) => evalTextLeaf(
            $leaf,
            $subject,
            $target,
            $caseId,
            $path,
            $specLangLimits,
            $specLangSymbols
        )
    );
    return ['status' => 'pass', 'category' => null, 'message' => null];
}

function parseEntrypointCommand(string $entrypoint): array {
    $parts = str_getcsv($entrypoint, ' ', '"', '\\');
    $cmd = [];
    foreach ($parts as $part) {
        $p = trim((string)$part);
        if ($p !== '') {
            $cmd[] = $p;
        }
    }
    if (count($cmd) === 0) {
        throw new SchemaError('cli.run requires non-empty harness.entrypoint');
    }
    return $cmd;
}

function applyEnvAllowlist(array $env): array {
    $raw = getenv('SPEC_RUNNER_ENV_ALLOWLIST');
    if ($raw === false) {
        return $env;
    }
    $raw = trim((string)$raw);
    if ($raw === '') {
        return $env;
    }
    $allowed = array_filter(
        array_map('trim', explode(',', $raw)),
        static fn(string $name): bool => $name !== ''
    );
    if (count($allowed) === 0) {
        return [];
    }
    $filtered = [];
    foreach ($allowed as $name) {
        if (array_key_exists($name, $env)) {
            $filtered[$name] = (string)$env[$name];
        }
    }
    return $filtered;
}

function evaluateCliRunCase(string $fixturePath, array $case): array {
    $mode = resolveAssertHealthMode($case);
    $diags = lintAssertionHealth($case['assert'] ?? []);
    if (count($diags) > 0 && $mode === 'error') {
        return [
            'status' => 'fail',
            'category' => 'assertion',
            'message' => formatAssertionHealthError($diags),
        ];
    }
    if (count($diags) > 0 && $mode === 'warn') {
        foreach ($diags as $d) {
            fwrite(STDERR, formatAssertionHealthWarning($d) . PHP_EOL);
        }
    }

    $h = $case['harness'] ?? [];
    if (!is_array($h)) {
        throw new SchemaError('harness must be a mapping');
    }
    $supportedHarnessKeys = ['entrypoint', 'env', 'spec_lang'];
    foreach (array_keys($h) as $k) {
        if (!in_array((string)$k, $supportedHarnessKeys, true)) {
            throw new SchemaError("unsupported harness key(s): {$k}");
        }
    }

    $entrypoint = trim((string)($h['entrypoint'] ?? ''));
    if ($entrypoint === '') {
        throw new RuntimeException('cli.run requires explicit harness.entrypoint');
    }
    $command = parseEntrypointCommand($entrypoint);

    $argv = $case['argv'] ?? [];
    if (is_string($argv)) {
        $argv = [$argv];
    }
    if (!is_array($argv) || !isListArray($argv)) {
        throw new SchemaError('argv must be a list or string');
    }
    foreach ($argv as $arg) {
        $command[] = (string)$arg;
    }

    $env = getenv();
    if (!is_array($env)) {
        $env = [];
    }
    $env = applyEnvAllowlist($env);
    if (array_key_exists('env', $h)) {
        if (!is_array($h['env'])) {
            throw new SchemaError('harness.env must be a mapping');
        }
        foreach ($h['env'] as $k => $v) {
            $name = (string)$k;
            if ($v === null) {
                unset($env[$name]);
            } else {
                $env[$name] = (string)$v;
            }
        }
    }

    $descriptors = [
        0 => ['pipe', 'r'],
        1 => ['pipe', 'w'],
        2 => ['pipe', 'w'],
    ];
    $proc = proc_open($command, $descriptors, $pipes, null, $env);
    if (!is_resource($proc)) {
        throw new RuntimeException('failed to launch cli.run entrypoint');
    }

    fwrite($pipes[0], '');
    fclose($pipes[0]);
    $stdout = stream_get_contents($pipes[1]);
    fclose($pipes[1]);
    $stderr = stream_get_contents($pipes[2]);
    fclose($pipes[2]);
    $exitCode = proc_close($proc);

    $got = (int)$exitCode;
    $want = isset($case['exit_code']) ? (int)$case['exit_code'] : 0;
    if ($got !== $want) {
        throw new AssertionFailure("[case_id={$case['id']}] exit_code expected={$want} actual={$got}");
    }

    $captured = ['stdout' => (string)$stdout, 'stderr' => (string)$stderr];
    $assertSpec = $case['assert'] ?? [];
    $specLangLimits = specLangLimitsFromHarness($case);
    $specLangSymbols = loadSpecLangSymbolsForCase($fixturePath, $case, $specLangLimits);
    evalAssertNode(
        $assertSpec,
        null,
        (string)$case['id'],
        'assert',
        static fn(array $leaf, string $target, string $caseId, string $path) => evalCliLeaf(
            $leaf,
            $captured,
            $target,
            $caseId,
            $path,
            $specLangLimits,
            $specLangSymbols
        )
    );

    return ['status' => 'pass', 'category' => null, 'message' => null];
}

function resolveApiHttpUrl(string $fixturePath, string $url): array {
    $trim = trim($url);
    if ($trim === '') {
        throw new SchemaError('api.http request.url is required');
    }
    $parts = @parse_url($trim);
    if ($parts !== false && is_array($parts) && array_key_exists('scheme', $parts)) {
        return ['source_type' => 'url', 'url' => $trim];
    }
    $docAbs = (string)realpath($fixturePath);
    if ($docAbs === '') {
        throw new RuntimeException("cannot resolve fixture path: {$fixturePath}");
    }
    $candidate = resolveContractPath($docAbs, $trim, 'api.http request.url');
    return ['source_type' => 'file', 'path' => $candidate];
}

function evalApiHttpLeaf(
    array $leaf,
    array $resp,
    string $target,
    string $caseId,
    string $path,
    array $specLangLimits,
    array $specLangSymbols
): void {
    foreach ($leaf as $op => $raw) {
        if ($op === 'target') {
            continue;
        }
        if (!is_array($raw) || !isListArray($raw)) {
            throw new SchemaError("assertion op '{$op}' must be a list");
        }
        if ($target === 'status' || $target === 'headers' || $target === 'body_text') {
            $subject = $target === 'status'
                ? (string)$resp['status']
                : ($target === 'headers' ? (string)$resp['headers_text'] : (string)$resp['body_text']);
            foreach ($raw as $value) {
                $expr = compileLeafExpr($op, $value, $target);
                $subjectForOp = $op === 'exists' ? trim((string)$subject) !== '' : $subject;
                assertLeafPredicate($caseId, $path, $target, $op, $expr, $subjectForOp, $specLangLimits, $specLangSymbols);
            }
            continue;
        }
        if ($target === 'body_json') {
            $parsed = json_decode((string)$resp['body_text'], true);
            if ($parsed === null && trim((string)$resp['body_text']) !== 'null') {
                throw new AssertionFailure(
                    "[case_id={$caseId} assert_path={$path} target={$target} op={$op}] body_json parse failed"
                );
            }
            $jsonText = json_encode($parsed, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
            if ($jsonText === false) {
                throw new RuntimeException('failed to serialize body_json');
            }
            foreach ($raw as $value) {
                $expr = compileLeafExpr($op, $value, $target);
                if ($op === 'exists') {
                    $subject = true;
                } elseif ($op === 'evaluate' || $op === 'json_type') {
                    $subject = $parsed;
                } else {
                    $subject = $jsonText;
                }
                assertLeafPredicate($caseId, $path, $target, $op, $expr, $subject, $specLangLimits, $specLangSymbols);
            }
            continue;
        }
        throw new SchemaError("unknown assert target for api.http: {$target}");
    }
}

function evaluateApiHttpCase(string $fixturePath, array $case): array {
    $request = $case['request'] ?? null;
    if (!is_array($request)) {
        throw new SchemaError('api.http requires request mapping');
    }
    $method = strtoupper(trim((string)($request['method'] ?? '')));
    if ($method === '') {
        throw new SchemaError('api.http request.method is required');
    }
    if (!array_key_exists('url', $request) || trim((string)$request['url']) === '') {
        throw new SchemaError('api.http request.url is required');
    }
    $resolved = resolveApiHttpUrl($fixturePath, (string)$request['url']);
    $headersText = '';
    $status = 200;
    $bodyText = '';
    if ($resolved['source_type'] === 'file') {
        $body = file_get_contents((string)$resolved['path']);
        if ($body === false) {
            throw new RuntimeException("cannot read fixture file: {$resolved['path']}");
        }
        $bodyText = (string)$body;
    } else {
        $headers = [];
        $hdrs = $request['headers'] ?? [];
        if ($hdrs !== null && !is_array($hdrs)) {
            throw new SchemaError('api.http request.headers must be a mapping');
        }
        if (is_array($hdrs)) {
            foreach ($hdrs as $k => $v) {
                $headers[] = (string)$k . ': ' . (string)$v;
            }
        }
        $bodyData = null;
        if (array_key_exists('body_text', $request) && array_key_exists('body_json', $request)) {
            throw new SchemaError('api.http request.body_text and request.body_json are mutually exclusive');
        }
        if (array_key_exists('body_text', $request)) {
            $bodyData = (string)$request['body_text'];
        } elseif (array_key_exists('body_json', $request)) {
            $encoded = json_encode($request['body_json'], JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
            if ($encoded === false) {
                throw new SchemaError('api.http request.body_json must be json-serializable');
            }
            $bodyData = $encoded;
            $headers[] = 'Content-Type: application/json';
        }
        $timeout = 5;
        if (isset($case['harness']) && is_array($case['harness']) && array_key_exists('timeout_seconds', $case['harness'])) {
            $timeout = (int)$case['harness']['timeout_seconds'];
            if ($timeout <= 0) {
                $timeout = 5;
            }
        }
        $opts = [
            'http' => [
                'method' => $method,
                'header' => implode("\r\n", $headers),
                'ignore_errors' => true,
                'timeout' => $timeout,
            ],
        ];
        if ($bodyData !== null) {
            $opts['http']['content'] = $bodyData;
        }
        $ctx = stream_context_create($opts);
        $body = @file_get_contents((string)$resolved['url'], false, $ctx);
        if ($body === false) {
            throw new RuntimeException("api.http request failed: {$resolved['url']}");
        }
        $bodyText = (string)$body;
        $responseHeaders = $http_response_header ?? [];
        if (is_array($responseHeaders) && count($responseHeaders) > 0) {
            $headersText = implode("\n", $responseHeaders);
            if (preg_match('/\s(\d{3})\s/', (string)$responseHeaders[0], $m) === 1) {
                $status = (int)$m[1];
            }
        }
    }

    $assertSpec = $case['assert'] ?? [];
    $specLangLimits = specLangLimitsFromHarness($case);
    $specLangSymbols = loadSpecLangSymbolsForCase($fixturePath, $case, $specLangLimits);
    evalAssertNode(
        $assertSpec,
        null,
        (string)$case['id'],
        'assert',
        static fn(array $leaf, string $target, string $caseId, string $path) => evalApiHttpLeaf(
            $leaf,
            [
                'status' => $status,
                'headers_text' => $headersText,
                'body_text' => $bodyText,
            ],
            $target,
            $caseId,
            $path,
            $specLangLimits,
            $specLangSymbols
        )
    );
    return ['status' => 'pass', 'category' => null, 'message' => null];
}

function evaluateCase(string $fixturePath, mixed $case): array {
    if (!is_array($case)) {
        return [
            'id' => 'UNKNOWN',
            'status' => 'fail',
            'category' => 'schema',
            'message' => 'case must be a mapping',
        ];
    }
    $id = isset($case['id']) ? (string)$case['id'] : '';
    $type = isset($case['type']) ? (string)$case['type'] : '';
    if ($id === '' || $type === '') {
        return [
            'id' => $id !== '' ? $id : 'UNKNOWN',
            'status' => 'fail',
            'category' => 'schema',
            'message' => 'case missing id or type',
        ];
    }

    try {
        if ($type === 'text.file') {
            $res = evaluateTextFileCase($fixturePath, $case);
        } elseif ($type === 'cli.run') {
            $res = evaluateCliRunCase($fixturePath, $case);
        } elseif ($type === 'api.http') {
            $res = evaluateApiHttpCase($fixturePath, $case);
        } else {
            return [
                'id' => $id,
                'status' => 'fail',
                'category' => 'runtime',
                'message' => "unknown spec-test type: {$type}",
            ];
        }
    } catch (SchemaError $e) {
        return ['id' => $id, 'status' => 'fail', 'category' => 'schema', 'message' => $e->getMessage()];
    } catch (AssertionFailure $e) {
        return ['id' => $id, 'status' => 'fail', 'category' => 'assertion', 'message' => $e->getMessage()];
    } catch (Throwable $e) {
        return ['id' => $id, 'status' => 'fail', 'category' => 'runtime', 'message' => $e->getMessage()];
    }

    return ['id' => $id, 'status' => $res['status'], 'category' => $res['category'], 'message' => $res['message']];
}

function main(array $argv): int {
    $args = parseArgs($argv);
    $caseFiles = listCaseFiles($args['cases'], (string)$args['case_pattern'], $args['case_formats']);

    $results = [];
    foreach ($caseFiles as $path) {
        foreach (parseCases($path) as $case) {
            $results[] = evaluateCase($path, $case);
        }
    }

    $report = ['version' => 1, 'results' => $results];
    $json = json_encode($report, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
    if ($json === false) {
        throw new RuntimeException('failed to encode JSON report');
    }
    $outPath = $args['out'];
    $parent = dirname($outPath);
    if (!is_dir($parent)) {
        if (!mkdir($parent, 0777, true) && !is_dir($parent)) {
            throw new RuntimeException("cannot create output dir: {$parent}");
        }
    }
    if (file_put_contents($outPath, $json . "\n") === false) {
        throw new RuntimeException("cannot write report: {$outPath}");
    }
    fwrite(STDOUT, "wrote {$outPath}\n");

    foreach ($results as $r) {
        if (($r['status'] ?? '') === 'fail') {
            return 1;
        }
    }
    return 0;
}

try {
    exit(main($argv));
} catch (Throwable $e) {
    fwrite(STDERR, "ERROR: " . $e->getMessage() . "\n");
    exit(1);
}

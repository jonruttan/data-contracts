#!/usr/bin/env php
<?php
declare(strict_types=1);

/*
 * PHP conformance runner bootstrap.
 *
 * This script is intentionally minimal and deterministic:
 * - Reads conformance case fixtures from a directory.
 * - Executes a small text.file subset using real YAML parsing.
 * - Supports assertion tree subset: list + must/can/cannot groups + contain/regex leaves.
 * - Emits JSON report envelope matching report-format.md.
 * - Marks unsupported case types as runtime failures.
 *
 * Usage:
 *   php scripts/php/conformance_runner.php \
 *     --cases docs/spec/conformance/cases \
 *     --out .artifacts/php-conformance-report.json
 */

function usage(): void {
    fwrite(STDOUT, "usage: conformance_runner.php --cases <dir-or-file> --out <file> [--case-file-pattern <glob>] [--case-formats <csv>]\n");
}

const DEFAULT_CASE_FILE_PATTERN = '*.spec.md';

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
    $iter = new RecursiveIteratorIterator(
        new RecursiveDirectoryIterator($path, FilesystemIterator::SKIP_DOTS)
    );
    foreach ($iter as $item) {
        if (!$item->isFile()) {
            continue;
        }
        $name = $item->getFilename();
        if (_pathMatchesFormat($name, $formats, $pattern)) {
            $files[] = $item->getPathname();
        }
    }
    sort($files, SORT_STRING);
    return $files;
}

class SchemaError extends RuntimeException {}
class AssertionFailure extends RuntimeException {}
const PHP_CAPABILITIES = [
    'api.http',
    'assert.op.contain',
    'assert.op.regex',
    'assert.op.evaluate',
    'evaluate.spec_lang.v1',
    'assert.group.must',
    'assert.group.can',
    'assert.group.cannot',
    'assert_health.ah001',
    'assert_health.ah002',
    'assert_health.ah003',
    'assert_health.ah004',
    'assert_health.ah005',
    'requires.capabilities',
];
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
        throw new RuntimeException('yaml_parse extension is required for PHP conformance runner');
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
        if (is_dir($cur . '/.git') || is_file($cur . '/.git')) {
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
    $raw = trim((string)$case['path']);
    if ($raw === '') {
        throw new SchemaError('text.file path must be non-empty');
    }
    if (str_starts_with($raw, '/')) {
        return resolveContractPath($docAbs, $raw, 'text.file path');
    }
    if (preg_match('/^[A-Za-z]:[\/\\\\]/', $raw) === 1) {
        throw new SchemaError('text.file path must not be OS-absolute');
    }
    $candidate = normalizePath(dirname($docAbs) . '/' . $raw);
    $root = contractRootFor($docAbs);
    if (!pathWithinRoot($candidate, $root)) {
        throw new SchemaError('text.file path escapes contract root');
    }
    return $candidate;
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
    $stepClass = trim((string)($node['class'] ?? ''));
    if (in_array($stepClass, ['must', 'can', 'cannot'], true) && array_key_exists('checks', $node)) {
        $checks = $node['checks'];
        if (is_array($checks) && isListArray($checks)) {
            $seen = [];
            foreach ($checks as $child) {
                $key = @json_encode($child, JSON_UNESCAPED_SLASHES);
                if (!is_string($key) || $key === '') {
                    $key = serialize($child);
                }
                if (array_key_exists($key, $seen)) {
                    $diags[] = [
                        'code' => 'AH004',
                        'path' => "{$path}.checks",
                        'message' => "redundant sibling assertion branch in '{$stepClass}'",
                    ];
                    break;
                }
                $seen[$key] = true;
            }
        }
        return array_merge($diags, lintAssertionHealth($checks, "{$path}.checks", $stepClass));
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

function specLangLimitsFromCase(array $case): array {
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

function specLangSpecialForms(): array {
    return ['if' => true, 'let' => true, 'fn' => true, 'call' => true, 'var' => true, 'lit' => true];
}

function specLangFlatBuiltinFromStd(string $symbol): string {
    $map = [
        'std.json.parse' => 'json_parse',
        'std.json.stringify' => 'json_stringify',
        'std.schema.match' => 'schema_match',
        'std.schema.errors' => 'schema_errors',
    ];
    if (array_key_exists($symbol, $map)) {
        return $map[$symbol];
    }
    $parts = explode('.', $symbol);
    return trim((string)end($parts));
}

function specLangCompileImportsForCase(array $case): array {
    $harness = $case['harness'] ?? [];
    if (!is_array($harness) || isListArray($harness)) {
        return [];
    }
    $cfg = $harness['spec_lang'] ?? [];
    if (!is_array($cfg) || isListArray($cfg)) {
        return [];
    }
    $rawImports = $cfg['imports'] ?? null;
    if ($rawImports === null) {
        return [];
    }
    if (!is_array($rawImports) || !isListArray($rawImports)) {
        throw new SchemaError('harness.spec_lang.imports must be a list');
    }
    $reserved = specLangSpecialForms();
    $out = [];
    foreach ($rawImports as $i => $item) {
        $field = "harness.spec_lang.imports[{$i}]";
        if (!is_array($item) || isListArray($item)) {
            throw new SchemaError("{$field} must be a mapping");
        }
        $from = trim((string)($item['from'] ?? ''));
        if ($from === '' || !str_starts_with($from, 'std.')) {
            throw new SchemaError("{$field}.from must be a std.* namespace");
        }
        $names = $item['names'] ?? null;
        if (!is_array($names) || !isListArray($names) || count($names) === 0) {
            throw new SchemaError("{$field}.names must be a non-empty list");
        }
        $alias = $item['as'] ?? [];
        if (!is_array($alias) || isListArray($alias)) {
            throw new SchemaError("{$field}.as must be a mapping");
        }
        foreach ($names as $j => $rawName) {
            $name = trim((string)$rawName);
            if ($name === '') {
                throw new SchemaError("{$field}.names[{$j}] must be a non-empty string");
            }
            $local = trim((string)($alias[$name] ?? $name));
            if ($local === '') {
                throw new SchemaError("{$field}.as value for {$name} must be a non-empty string");
            }
            if (array_key_exists($local, $reserved)) {
                throw new SchemaError("{$field} import collides with reserved special form: {$local}");
            }
            $fq = "{$from}.{$name}";
            if (array_key_exists($local, $out) && $out[$local] !== $fq) {
                throw new SchemaError("{$field} import collision for local name: {$local}");
            }
            $out[$local] = $fq;
        }
    }
    return $out;
}

function specLangResolveOpSymbol(string $head, array $imports): string {
    if (array_key_exists($head, specLangSpecialForms())) {
        return $head;
    }
    if (str_starts_with($head, 'std.')) {
        return specLangFlatBuiltinFromStd($head);
    }
    if (array_key_exists($head, $imports)) {
        return specLangFlatBuiltinFromStd((string)$imports[$head]);
    }
    // Internal list-token AST may still carry flat names; normalize at runtime.
    return specLangFlatBuiltinFromStd($head);
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
    if ($op === 'lt' || $op === 'lte' || $op === 'gt' || $op === 'gte') {
        specLangRequireArity($op, $args, 2);
        $left = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $right = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        if ((!is_int($left) && !is_float($left)) || (!is_int($right) && !is_float($right))) {
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
        $container = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $member = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        if (is_array($container)) {
            if (isListArray($container)) {
                return in_array($member, $container, true);
            }
            return array_key_exists((string)$member, $container);
        }
        if (is_string($container)) {
            return str_contains($container, (string)$member);
        }
        throw new SchemaError('spec_lang includes expects list/dict/string container');
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
    if ($op === 'len') {
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
    if ($op === 'replace') {
        specLangRequireArity($op, $args, 3);
        $subjectText = (string)specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $needle = (string)specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        $replacement = (string)specLangEvalNonTail($args[2], $env, $subject, $limits, $state);
        return str_replace($needle, $replacement, $subjectText);
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
    if ($op === 'add' || $op === 'sub') {
        specLangRequireArity($op, $args, 2);
        $left = specLangEvalNonTail($args[0], $env, $subject, $limits, $state);
        $right = specLangEvalNonTail($args[1], $env, $subject, $limits, $state);
        if ((!is_int($left) && !is_float($left)) || (!is_int($right) && !is_float($right))) {
            throw new SchemaError("spec_lang {$op} expects numeric args");
        }
        return $op === 'add' ? $left + $right : $left - $right;
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
        if (is_array($currentExpr) && !isListArray($currentExpr)) {
            $out = [];
            foreach ($currentExpr as $k => $v) {
                $out[(string)$k] = specLangEvalNonTail($v, $currentEnv, $subject, $limits, $state);
            }
            return $out;
        }
        if (!is_array($currentExpr) || !isListArray($currentExpr)) {
            throw new SchemaError('spec_lang expression must be list-based s-expr or scalar literal');
        }
        if (count($currentExpr) === 0) {
            throw new SchemaError('spec_lang expression list must not be empty');
        }
        $head = $currentExpr[0];
        if (!is_string($head)) {
            $out = [];
            foreach ($currentExpr as $item) {
                $out[] = specLangEvalNonTail($item, $currentEnv, $subject, $limits, $state);
            }
            return $out;
        }
        if (trim($head) === '') {
            throw new SchemaError('spec_lang expression head must be non-empty string symbol');
        }
        $imports = $state['imports'] ?? [];
        $op = specLangResolveOpSymbol($head, is_array($imports) ? $imports : []);
        $args = array_slice($currentExpr, 1);

        if ($op === 'if') {
            specLangRequireArity($op, $args, 3);
            $cond = specLangEvalNonTail($args[0], $currentEnv, $subject, $limits, $state);
            $currentExpr = ((bool)$cond) ? $args[1] : $args[2];
            continue;
        }
        if ($op === 'lit') {
            specLangRequireArity($op, $args, 1);
            return $args[0];
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

function specLangEvalPredicate(
    mixed $expr,
    mixed $subject,
    array $limits,
    array $symbols = [],
    array $imports = [],
): bool {
    specLangValidateExprShape($expr, $limits);
    $state = ['steps' => 0, 'started' => microtime(true), 'limits' => $limits, 'imports' => $imports];
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
        return ['lit', compileYamlExprLiteral($node['lit'], "{$fieldPath}.lit")];
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
        throw new SchemaError('harness.spec_lang.includes item must be non-empty');
    }
    if (str_starts_with($raw, 'external://')) {
        throw new SchemaError('harness.spec_lang.includes external refs are denied by default');
    }
    return resolveContractPath($baseDocPath, $raw, 'harness.spec_lang.includes');
}

function loadSpecLangLibraryDoc(string $path): array {
    $imports = [];
    $bindings = [];
    $exports = [];
    foreach (parseCases($path) as $case) {
        $type = trim((string)($case['type'] ?? ''));
        if ($type !== 'spec.export') {
            continue;
        }
        foreach (asNonEmptyStringList($case['imports'] ?? null, 'imports') as $imp) {
            $imports[] = $imp;
        }
        $rawAssert = $case['assert'] ?? null;
        $assertSteps = [];
        if (is_array($rawAssert) && isListArray($rawAssert)) {
            foreach ($rawAssert as $step) {
                if (!is_array($step) || isListArray($step)) {
                    continue;
                }
                $sid = trim((string)($step['id'] ?? ''));
                if ($sid !== '') {
                    $assertSteps[$sid] = $step;
                }
            }
        }
        $harness = $case['harness'] ?? null;
        $chain = (is_array($harness) && !isListArray($harness)) ? ($harness['chain'] ?? null) : null;
        $producerExports = (is_array($chain) && !isListArray($chain)) ? ($chain['exports'] ?? null) : null;
        if (!is_array($producerExports) || !isListArray($producerExports)) {
            continue;
        }
        foreach ($producerExports as $entryIdx => $entryRaw) {
            if (!is_array($entryRaw) || isListArray($entryRaw)) {
                throw new SchemaError("harness.chain.exports[{$entryIdx}] must be a mapping");
            }
            $name = trim((string)($entryRaw['as'] ?? ''));
            if ($name === '') {
                throw new SchemaError("harness.chain.exports[{$entryIdx}].as is required");
            }
            if (array_key_exists($name, $bindings)) {
                continue;
            }
            $fromSource = trim((string)($entryRaw['from'] ?? ''));
            if ($fromSource !== 'assert.function') {
                throw new SchemaError("harness.chain.exports[{$entryIdx}].from must be assert.function");
            }
            $stepId = ltrim(trim((string)($entryRaw['path'] ?? '')), '/');
            if ($stepId === '') {
                throw new SchemaError("harness.chain.exports[{$entryIdx}].path is required for from=assert.function");
            }
            if (!array_key_exists($stepId, $assertSteps)) {
                throw new SchemaError("harness.chain.exports[{$entryIdx}] unresolved assert step id: {$stepId}");
            }
            $srcStep = $assertSteps[$stepId];
            if (trim((string)($srcStep['class'] ?? '')) !== 'must') {
                throw new SchemaError("harness.chain.exports[{$entryIdx}] source assert step must use class=must");
            }
            $checks = $srcStep['checks'] ?? null;
            if (!is_array($checks) || !isListArray($checks) || count($checks) === 0) {
                throw new SchemaError("harness.chain.exports[{$entryIdx}] source assert step requires non-empty checks");
            }
            $paramsRaw = $entryRaw['params'] ?? null;
            if (!is_array($paramsRaw) || !isListArray($paramsRaw)) {
                throw new SchemaError("harness.chain.exports[{$entryIdx}].params must be a list");
            }
            $params = [];
            foreach ($paramsRaw as $pIdx => $rawParam) {
                if (!is_string($rawParam) || trim($rawParam) === '') {
                    throw new SchemaError("harness.chain.exports[{$entryIdx}].params[{$pIdx}] must be non-empty string");
                }
                $params[] = trim($rawParam);
            }
            $exprs = [];
            foreach ($checks as $cIdx => $rawCheck) {
                $exprs[] = compileYamlExprToSexpr($rawCheck, "{$path} harness.chain.exports[{$entryIdx}].checks[{$cIdx}]");
            }
            $body = $exprs[count($exprs) - 1];
            for ($i = count($exprs) - 2; $i >= 0; $i -= 1) {
                $body = ['std.logic.and', $exprs[$i], $body];
            }
            $bindings[$name] = ['fn', $params, $body];
            $exports[] = $name;
        }
    }
    if (count($bindings) === 0) {
        throw new SchemaError("library file has no spec.export chain exports: {$path}");
    }
    return [
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

function loadSpecLangSymbolsFromEntryDocs(array $entryDocs, array $limits): array {
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
    $compiled = compileSpecLangSymbolBindings($mergedBindings, $limits);
    if (count($exportAllow) > 0) {
        $filtered = [];
        foreach ($exportAllow as $name => $_true) {
            $filtered[$name] = $compiled[$name];
        }
        return $filtered;
    }
    return $compiled;
}

function loadSpecLangSymbolsForCase(string $fixturePath, array $case, array $limits): array {
    $harness = $case['harness'] ?? null;
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
    $libPaths = asNonEmptyStringList($cfg['includes'] ?? null, 'harness.spec_lang.includes');
    if (count($libPaths) > 0) {
        throw new SchemaError(
            'harness.spec_lang.includes is not supported for executable cases; use harness.chain imports'
        );
    }
    $consumerExports = asNonEmptyStringList($cfg['exports'] ?? null, 'harness.spec_lang.exports');
    if (count($consumerExports) > 0) {
        throw new SchemaError(
            'harness.spec_lang.exports is not supported for executable cases; use harness.chain imports'
        );
    }
    return [];
}

function chainRefResolveDocPath(string $fixturePath, string $rawRef): array {
    $trim = trim($rawRef);
    if ($trim === '') {
        throw new SchemaError('harness.chain.steps[*].ref must be a non-empty string');
    }
    $hashPos = strpos($trim, '#');
    if ($hashPos === false) {
        return ['path' => resolveContractPath($fixturePath, $trim, 'harness.chain.steps.ref'), 'case_id' => null];
    }
    $pathPart = trim(substr($trim, 0, $hashPos));
    $casePart = trim(substr($trim, $hashPos + 1));
    if ($casePart === '') {
        throw new SchemaError("harness.chain.steps[*].ref fragment case_id must be non-empty when '#' is present");
    }
    if ($pathPart === '') {
        return ['path' => $fixturePath, 'case_id' => $casePart];
    }
    return ['path' => resolveContractPath($fixturePath, $pathPart, 'harness.chain.steps.ref'), 'case_id' => $casePart];
}

function contractPathFromAbsoluteDoc(string $docPath): string {
    $root = contractRootFor($docPath);
    $prefix = rtrim($root, '/\\') . DIRECTORY_SEPARATOR;
    if (!str_starts_with($docPath, $prefix)) {
        throw new SchemaError("chain library ref escapes contract root: {$docPath}");
    }
    return '/' . ltrim(str_replace('\\', '/', substr($docPath, strlen($prefix))), '/');
}

function loadChainImportedSymbolsForCase(string $fixturePath, array $case, array $limits): array {
    $harness = $case['harness'] ?? null;
    if (!is_array($harness) || isListArray($harness)) {
        return [];
    }
    $chain = $harness['chain'] ?? null;
    if (!is_array($chain) || isListArray($chain)) {
        return [];
    }
    $steps = $chain['steps'] ?? null;
    if (!is_array($steps) || !isListArray($steps)) {
        return [];
    }

    $stepExports = [];
    foreach ($steps as $idx => $step) {
        if (!is_array($step) || isListArray($step)) {
            throw new SchemaError("harness.chain.steps[{$idx}] must be a mapping");
        }
        $stepId = trim((string)($step['id'] ?? ''));
        if ($stepId === '') {
            throw new SchemaError("harness.chain.steps[{$idx}].id must be a non-empty string");
        }
        $refRaw = $step['ref'] ?? null;
        if (!is_string($refRaw) || trim($refRaw) === '') {
            throw new SchemaError("harness.chain.steps[{$idx}].ref must be a non-empty string");
        }
        $resolvedRef = chainRefResolveDocPath($fixturePath, $refRaw);
        $sourceDoc = (string)$resolvedRef['path'];
        if (!is_file($sourceDoc)) {
            throw new SchemaError("chain ref path does not exist as file: {$refRaw}");
        }
        if (array_key_exists('exports', $step) || array_key_exists('imports', $step)) {
            throw new SchemaError(
                "harness.chain.steps[{$idx}] symbol declarations are forbidden; use producer harness.chain.exports"
            );
        }
        $producerCases = parseCases($sourceDoc);
        $targetCaseId = $resolvedRef['case_id'];
        if (is_string($targetCaseId) && $targetCaseId !== '') {
            $filtered = [];
            foreach ($producerCases as $producerCase) {
                if (!is_array($producerCase) || isListArray($producerCase)) {
                    continue;
                }
                if (trim((string)($producerCase['id'] ?? '')) === $targetCaseId) {
                    $filtered[] = $producerCase;
                }
            }
            $producerCases = $filtered;
        }
        $exports = [];
        foreach ($producerCases as $producerCase) {
            if (!is_array($producerCase) || isListArray($producerCase)) {
                continue;
            }
            $producerHarness = $producerCase['harness'] ?? null;
            $producerChain = null;
            if (is_array($producerHarness) && !isListArray($producerHarness)) {
                $producerChain = $producerHarness['chain'] ?? null;
            }
            $producerExports = (is_array($producerChain) && !isListArray($producerChain))
                ? ($producerChain['exports'] ?? null)
                : null;
            if (is_array($producerExports) && isListArray($producerExports)) {
                foreach ($producerExports as $entryIdx => $entryRaw) {
                    if (!is_array($entryRaw) || isListArray($entryRaw)) {
                        throw new SchemaError("producer harness.chain.exports[{$entryIdx}] must be a mapping");
                    }
                    $exportName = trim((string)($entryRaw['as'] ?? ''));
                    if ($exportName === '') {
                        throw new SchemaError("producer harness.chain.exports[{$entryIdx}].as is required");
                    }
                    if (array_key_exists($exportName, $exports)) {
                        continue;
                    }
                    $fromSource = trim((string)($entryRaw['from'] ?? ''));
                    if ($fromSource !== 'assert.function') {
                        throw new SchemaError(
                            "producer harness.chain.exports[{$entryIdx}].from must be assert.function"
                        );
                    }
                    $symbolPath = trim((string)($entryRaw['path'] ?? ''));
                    if ($symbolPath === '') {
                        throw new SchemaError(
                            "producer harness.chain.exports[{$entryIdx}].path is required for from=assert.function"
                        );
                    }
                    $required = !array_key_exists('required', $entryRaw) || (bool)$entryRaw['required'];
                    $exports[$exportName] = [
                        'from' => $fromSource,
                        'path' => $symbolPath,
                        'required' => $required,
                    ];
                }
            }

            // Implicit producer exports for spec_lang.export: defines.public keys.
            if (trim((string)($producerCase['type'] ?? '')) === 'spec_lang.export') {
                $defines = $producerCase['defines'] ?? null;
                $public = is_array($defines) && !isListArray($defines) ? ($defines['public'] ?? null) : null;
                if (is_array($public) && !isListArray($public)) {
                    foreach ($public as $symbolName => $_expr) {
                        $exportName = trim((string)$symbolName);
                        if ($exportName === '' || array_key_exists($exportName, $exports)) {
                            continue;
                        }
                        $exports[$exportName] = [
                            'from' => 'assert.function',
                            'path' => $exportName,
                            'required' => true,
                        ];
                    }
                }
            }
        }
        if (count($exports) === 0) {
            continue;
        }
        $loadedSymbols = loadSpecLangSymbolsFromEntryDocs([$sourceDoc], $limits);
        $resolvedExports = [];
        foreach ($exports as $exportName => $expRaw) {
            if (!is_array($expRaw) || isListArray($expRaw)) {
                continue;
            }
            if (trim((string)($expRaw['from'] ?? '')) !== 'assert.function') {
                continue;
            }
            $symbolPath = ltrim(trim((string)($expRaw['path'] ?? '')), '/');
            $required = !array_key_exists('required', $expRaw) || (bool)$expRaw['required'];
            if ($symbolPath === '') {
                throw new SchemaError("producer harness.chain.exports.{$exportName}.path is required for from=assert.function");
            }
            if (!array_key_exists((string)$exportName, $loadedSymbols)) {
                if ($required) {
                    throw new SchemaError("chain step {$stepId} import {$exportName} unresolved producer symbol: {$exportName}");
                }
                continue;
            }
            $resolvedExports[(string)$exportName] = $loadedSymbols[(string)$exportName];
        }
        $stepExports[$stepId] = $resolvedExports;
    }

    $out = [];
    $imports = $chain['imports'] ?? [];
    if (!is_array($imports) || !isListArray($imports)) {
        return $out;
    }
    foreach ($imports as $idx => $imp) {
        if (!is_array($imp) || isListArray($imp)) {
            throw new SchemaError("harness.chain.imports[{$idx}] must be a mapping");
        }
        $fromStep = trim((string)($imp['from'] ?? ''));
        if ($fromStep === '' || !array_key_exists($fromStep, $stepExports)) {
            continue;
        }
        $names = $imp['names'] ?? null;
        if (!is_array($names) || !isListArray($names)) {
            throw new SchemaError("harness.chain.imports[{$idx}].names must be a non-empty list");
        }
        $aliasesRaw = $imp['as'] ?? [];
        $aliases = (is_array($aliasesRaw) && !isListArray($aliasesRaw)) ? $aliasesRaw : [];
        foreach ($names as $rawName) {
            $name = trim((string)$rawName);
            if ($name === '' || !array_key_exists($name, $stepExports[$fromStep])) {
                continue;
            }
            $local = trim((string)($aliases[$name] ?? $name));
            if ($local === '') {
                continue;
            }
            $out[$local] = $stepExports[$fromStep][$name];
        }
    }
    return $out;
}

function compileAssertionLeafExpr(array $leaf, string $path): array {
    if (array_key_exists('evaluate', $leaf)) {
        throw new SchemaError('explicit evaluate leaf is not supported; use expression mapping directly');
    }
    if (count($leaf) === 0) {
        throw new SchemaError('assertion leaf must be a non-empty expression mapping');
    }
    $compiled = compileYamlExprToSexpr($leaf, $path);
    if (!is_array($compiled) || !isListArray($compiled)) {
        throw new SchemaError('assertion expression must compile to a list-based s-expr');
    }
    return $compiled;
}

function assertLeafPredicate(
    string $caseId,
    string $path,
    string $target,
    string $op,
    mixed $expr,
    mixed $subject,
    array $specLangLimits,
    array $specLangSymbols = [],
    array $specLangImports = []
): void {
    if (!specLangEvalPredicate($expr, $subject, $specLangLimits, $specLangSymbols, $specLangImports)) {
        $msg = $op === 'evaluate' ? 'evaluate assertion failed' : "{$op} assertion failed";
        throw new AssertionFailure(
            "[case_id={$caseId} assert_path={$path} target={$target} op={$op}] {$msg}"
        );
    }
}

function evalTextLeaf(
    array $leaf,
    mixed $subject,
    string $target,
    string $caseId,
    string $path,
    array $specLangLimits,
    array $specLangSymbols,
    array $specLangImports
): void {
    $expr = compileAssertionLeafExpr($leaf, $path);
    assertLeafPredicate($caseId, $path, $target, 'evaluate', $expr, $subject, $specLangLimits, $specLangSymbols, $specLangImports);
}

function evalTextAssertNode(
    mixed $node,
    string $subject,
    array $contextJson,
    ?string $inheritedTarget,
    string $caseId,
    string $path,
    array $specLangLimits,
    array $specLangSymbols,
    array $specLangImports
): void {
    if (is_array($node) && isListArray($node)) {
        foreach ($node as $i => $child) {
            evalTextAssertNode(
                $child,
                $subject,
                $contextJson,
                $inheritedTarget,
                $caseId,
                "{$path}[{$i}]",
                $specLangLimits,
                $specLangSymbols,
                $specLangImports
            );
        }
        return;
    }
    if (!is_array($node)) {
        throw new SchemaError('assert node must be a mapping or list');
    }
    $stepClass = trim((string)($node['class'] ?? ''));
    if (in_array($stepClass, ['must', 'can', 'cannot'], true) && array_key_exists('checks', $node)) {
        $stepId = trim((string)($node['id'] ?? ''));
        if ($stepId === '') {
            throw new SchemaError("{$path}.id must be a non-empty string");
        }
        $extra = array_diff(array_keys($node), ['id', 'class', 'target', 'checks']);
        if (count($extra) > 0) {
            throw new SchemaError('unknown key in assert step: ' . (string)array_values($extra)[0]);
        }
        $target = trim((string)($node['target'] ?? ''));
        if ($target === '') {
            $target = $inheritedTarget ?? '';
        }
        $children = $node['checks'];
        if (!is_array($children) || !isListArray($children)) {
            throw new SchemaError('assert step checks must be a list');
        }
        if (count($children) === 0) {
            throw new SchemaError('assert step checks must not be empty');
        }
        $stepPath = $path;
        if ($stepClass === 'must') {
            foreach ($children as $i => $child) {
                evalTextAssertNode(
                    $child,
                    $subject,
                    $contextJson,
                    $target,
                    $caseId,
                    "{$stepPath}.checks[{$i}]",
                    $specLangLimits,
                    $specLangSymbols,
                    $specLangImports
                );
            }
            return;
        }
        if ($stepClass === 'can') {
            $anyPassed = false;
            foreach ($children as $i => $child) {
                try {
                    evalTextAssertNode(
                        $child,
                        $subject,
                        $contextJson,
                        $target,
                        $caseId,
                        "{$stepPath}.checks[{$i}]",
                        $specLangLimits,
                        $specLangSymbols,
                        $specLangImports
                    );
                    $anyPassed = true;
                    break;
                } catch (AssertionFailure $e) {
                    // Continue trying other branches.
                }
            }
            if (!$anyPassed) {
                throw new AssertionFailure("all 'can' branches failed");
            }
            return;
        }
        $passed = 0;
        foreach ($children as $i => $child) {
            try {
                evalTextAssertNode(
                    $child,
                    $subject,
                    $contextJson,
                    $target,
                    $caseId,
                    "{$stepPath}.checks[{$i}]",
                    $specLangLimits,
                    $specLangSymbols,
                    $specLangImports
                );
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
                evalTextAssertNode(
                    $child,
                    $subject,
                    $contextJson,
                    $target,
                    $caseId,
                    "{$path}.must[{$i}]",
                    $specLangLimits,
                    $specLangSymbols,
                    $specLangImports
                );
            }
            return;
        }
        if ($group === 'can') {
            $anyPassed = false;
            foreach ($children as $i => $child) {
                try {
                    evalTextAssertNode(
                        $child,
                        $subject,
                        $contextJson,
                        $target,
                        $caseId,
                        "{$path}.can[{$i}]",
                        $specLangLimits,
                        $specLangSymbols,
                        $specLangImports
                    );
                    $anyPassed = true;
                    break;
                } catch (AssertionFailure $e) {
                    // Continue trying other branches.
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
                    evalTextAssertNode(
                        $child,
                        $subject,
                        $contextJson,
                        $target,
                        $caseId,
                        "{$path}.cannot[{$i}]",
                        $specLangLimits,
                        $specLangSymbols,
                        $specLangImports
                    );
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
    if ($target !== 'text' && $target !== 'context_json') {
        throw new SchemaError('unknown assert target for text.file');
    }
    evalTextLeaf(
        $node,
        $target === 'context_json' ? $contextJson : $subject,
        $target,
        $caseId,
        $path,
        $specLangLimits,
        $specLangSymbols,
        $specLangImports
    );
}

function evaluateTextFileCase(string $fixturePath, array $case, string $subject): array {
    try {
        $resolvedMode = resolveAssertHealthMode($case);
    } catch (SchemaError $e) {
        return ['status' => 'fail', 'category' => 'schema', 'message' => $e->getMessage()];
    }
    $diags = lintAssertionHealth($case['assert'] ?? []);
    if (count($diags) > 0 && $resolvedMode === 'error') {
        return [
            'status' => 'fail',
            'category' => 'assertion',
            'message' => formatAssertionHealthError($diags),
        ];
    }
    if (count($diags) > 0 && $resolvedMode === 'warn') {
        foreach ($diags as $d) {
            fwrite(STDERR, formatAssertionHealthWarning($d) . PHP_EOL);
        }
    }

    try {
        $assertSpec = $case['assert'] ?? [];
        $specLangLimits = specLangLimitsFromCase($case);
        $specLangImports = specLangCompileImportsForCase($case);
        $specLangSymbols = loadSpecLangSymbolsForCase($fixturePath, $case, $specLangLimits);
        foreach (loadChainImportedSymbolsForCase($fixturePath, $case, $specLangLimits) as $sym => $binding) {
            $specLangSymbols[(string)$sym] = $binding;
        }
        $docAbs = (string)realpath($fixturePath);
        if ($docAbs === '') {
            throw new RuntimeException("cannot resolve fixture path: {$fixturePath}");
        }
        $targetAbs = isset($case['__target_path']) ? (string)$case['__target_path'] : $docAbs;
        $root = contractRootFor($docAbs);
        $prefix = rtrim($root, '/\\') . DIRECTORY_SEPARATOR;
        $metaPath = str_replace('\\', '/', str_starts_with($targetAbs, $prefix) ? substr($targetAbs, strlen($prefix)) : $targetAbs);
        $sourceDoc = str_replace('\\', '/', str_starts_with($docAbs, $prefix) ? substr($docAbs, strlen($prefix)) : $docAbs);
        $contextJson = [
            'profile_id' => 'text.file/v1',
            'profile_version' => 1,
            'value' => $subject,
            'meta' => [
                'target' => 'text',
                'path' => '/' . ltrim($metaPath, '/'),
            ],
            'context' => [
                'source_doc' => '/' . ltrim($sourceDoc, '/'),
            ],
        ];
        evalTextAssertNode(
            $assertSpec,
            $subject,
            $contextJson,
            null,
            (string)$case['id'],
            'assert',
            $specLangLimits,
            $specLangSymbols,
            $specLangImports
        );
    } catch (SchemaError $e) {
        return ['status' => 'fail', 'category' => 'schema', 'message' => $e->getMessage()];
    } catch (AssertionFailure $e) {
        return ['status' => 'fail', 'category' => 'assertion', 'message' => $e->getMessage()];
    } catch (Throwable $e) {
        return ['status' => 'fail', 'category' => 'runtime', 'message' => $e->getMessage()];
    }
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
    if (str_starts_with($trim, '/')) {
        $candidate = resolveContractPath($docAbs, $trim, 'api.http request.url');
        return ['source_type' => 'file', 'path' => $candidate];
    }
    if (preg_match('/^[A-Za-z]:[\/\\\\]/', $trim) === 1) {
        throw new SchemaError('api.http request.url relative path must not be OS-absolute');
    }
    $candidate = normalizePath(dirname($docAbs) . '/' . $trim);
    $root = contractRootFor($docAbs);
    if (!pathWithinRoot($candidate, $root)) {
        throw new SchemaError('api.http request.url relative path escapes contract root');
    }
    return ['source_type' => 'file', 'path' => $candidate];
}

function resolveApiHttpMode(array $case): string {
    $harness = $case['harness'] ?? null;
    if (!is_array($harness)) {
        return 'deterministic';
    }
    $apiHttp = $harness['api_http'] ?? null;
    if (!is_array($apiHttp)) {
        return 'deterministic';
    }
    $mode = trim((string)($apiHttp['mode'] ?? 'deterministic'));
    if ($mode === '') {
        $mode = 'deterministic';
    }
    if ($mode !== 'deterministic' && $mode !== 'live') {
        throw new SchemaError("api.http mode must be one of: deterministic, live");
    }
    return $mode;
}

function parseApiHttpOAuthConfig(string $fixturePath, array $case, string $mode): ?array {
    $harness = $case['harness'] ?? null;
    if (!is_array($harness)) {
        return null;
    }
    $apiHttp = $harness['api_http'] ?? null;
    if (!is_array($apiHttp)) {
        return null;
    }
    $auth = $apiHttp['auth'] ?? null;
    if ($auth === null) {
        return null;
    }
    if (!is_array($auth)) {
        throw new SchemaError('api.http harness.auth must be a mapping');
    }
    $oauth = $auth['oauth'] ?? null;
    if ($oauth === null) {
        return null;
    }
    if (!is_array($oauth)) {
        throw new SchemaError('api.http harness.auth.oauth must be a mapping');
    }

    $grantType = trim((string)($oauth['grant_type'] ?? ''));
    if ($grantType !== 'client_credentials') {
        throw new SchemaError('api.http oauth grant_type must be client_credentials');
    }
    $tokenUrl = trim((string)($oauth['token_url'] ?? ''));
    if ($tokenUrl === '') {
        throw new SchemaError('api.http oauth token_url is required');
    }
    $clientIdEnv = trim((string)($oauth['client_id_env'] ?? ''));
    if ($clientIdEnv === '') {
        throw new SchemaError('api.http oauth client_id_env is required');
    }
    $clientSecretEnv = trim((string)($oauth['client_secret_env'] ?? ''));
    if ($clientSecretEnv === '') {
        throw new SchemaError('api.http oauth client_secret_env is required');
    }
    $authStyle = trim((string)($oauth['auth_style'] ?? 'basic'));
    if ($authStyle === '') {
        $authStyle = 'basic';
    }
    if ($authStyle !== 'basic' && $authStyle !== 'body') {
        throw new SchemaError('api.http oauth auth_style must be one of: basic, body');
    }

    $clientId = getenv($clientIdEnv);
    if ($clientId === false || trim((string)$clientId) === '') {
        throw new SchemaError("oauth env var is required: {$clientIdEnv}");
    }
    $clientSecret = getenv($clientSecretEnv);
    if ($clientSecret === false || trim((string)$clientSecret) === '') {
        throw new SchemaError("oauth env var is required: {$clientSecretEnv}");
    }

    $resolved = resolveApiHttpUrl($fixturePath, $tokenUrl);
    if ($resolved['source_type'] === 'url' && $mode !== 'live') {
        throw new SchemaError('api.http oauth token_url network usage requires harness.api_http.mode=live');
    }

    return [
        'resolved' => $resolved,
        'scope' => isset($oauth['scope']) ? (string)$oauth['scope'] : null,
        'audience' => isset($oauth['audience']) ? (string)$oauth['audience'] : null,
        'auth_style' => $authStyle,
        'token_field' => trim((string)($oauth['token_field'] ?? 'access_token')) ?: 'access_token',
        'client_id' => (string)$clientId,
        'client_secret' => (string)$clientSecret,
    ];
}

function fetchApiHttpOAuthToken(array $cfg): array {
    $started = microtime(true);
    $resolved = $cfg['resolved'];
    $tokenField = (string)$cfg['token_field'];
    if (($resolved['source_type'] ?? '') === 'file') {
        $raw = @file_get_contents((string)$resolved['path']);
        if ($raw === false) {
            throw new RuntimeException('api.http oauth token fetch failed');
        }
        $payload = json_decode((string)$raw, true);
        if (!is_array($payload) || !array_key_exists($tokenField, $payload)) {
            throw new RuntimeException("api.http oauth token response missing field: {$tokenField}");
        }
        $token = trim((string)$payload[$tokenField]);
        if ($token === '') {
            throw new RuntimeException('api.http oauth token response access token is empty');
        }
        return [
            'token' => $token,
            'token_fetch_ms' => (int)round((microtime(true) - $started) * 1000),
            'used_cached_token' => false,
        ];
    }

    $body = ['grant_type' => 'client_credentials'];
    if (isset($cfg['scope']) && $cfg['scope'] !== null && trim((string)$cfg['scope']) !== '') {
        $body['scope'] = (string)$cfg['scope'];
    }
    if (isset($cfg['audience']) && $cfg['audience'] !== null && trim((string)$cfg['audience']) !== '') {
        $body['audience'] = (string)$cfg['audience'];
    }
    if (($cfg['auth_style'] ?? 'basic') === 'body') {
        $body['client_id'] = (string)$cfg['client_id'];
        $body['client_secret'] = (string)$cfg['client_secret'];
    }
    $headers = ['Content-Type: application/x-www-form-urlencoded'];
    if (($cfg['auth_style'] ?? 'basic') === 'basic') {
        $headers[] = 'Authorization: Basic ' . base64_encode((string)$cfg['client_id'] . ':' . (string)$cfg['client_secret']);
    }
    $opts = [
        'http' => [
            'method' => 'POST',
            'header' => implode("\r\n", $headers),
            'content' => http_build_query($body),
            'ignore_errors' => true,
            'timeout' => 10,
        ],
    ];
    $ctx = stream_context_create($opts);
    $raw = @file_get_contents((string)$resolved['url'], false, $ctx);
    if ($raw === false) {
        throw new RuntimeException('api.http oauth token fetch failed');
    }
    $payload = json_decode((string)$raw, true);
    if (!is_array($payload) || !array_key_exists($tokenField, $payload)) {
        throw new RuntimeException("api.http oauth token response missing field: {$tokenField}");
    }
    $token = trim((string)$payload[$tokenField]);
    if ($token === '') {
        throw new RuntimeException('api.http oauth token response access token is empty');
    }
    return [
        'token' => $token,
        'token_fetch_ms' => (int)round((microtime(true) - $started) * 1000),
        'used_cached_token' => false,
    ];
}

function apiHttpJsonOrNull(string $text): mixed {
    if (trim($text) === '') {
        return null;
    }
    $decoded = json_decode($text, true);
    if ($decoded === null && trim($text) !== 'null') {
        return null;
    }
    return $decoded;
}

function apiHttpHeaderMapGet(array $headers, string $key): ?string {
    $want = strtolower(trim($key));
    foreach ($headers as $k => $v) {
        if (strtolower(trim((string)$k)) === $want) {
            return (string)$v;
        }
    }
    return null;
}

function apiHttpHeaderMapSet(array &$headers, string $key, string $value): void {
    $want = strtolower(trim($key));
    foreach ($headers as $k => $_v) {
        if (strtolower(trim((string)$k)) === $want) {
            $headers[$k] = $value;
            return;
        }
    }
    $headers[$key] = $value;
}

function apiHttpCorsProjection(array $headers): array {
    $csv = function (?string $raw): array {
        if ($raw === null) {
            return [];
        }
        $parts = preg_split('/,/', $raw) ?: [];
        $out = [];
        foreach ($parts as $p) {
            $token = trim((string)$p);
            if ($token !== '') {
                $out[] = $token;
            }
        }
        return $out;
    };
    $asBool = function (?string $raw): ?bool {
        if ($raw === null) {
            return null;
        }
        $v = strtolower(trim($raw));
        if ($v === 'true') {
            return true;
        }
        if ($v === 'false') {
            return false;
        }
        return null;
    };
    $asInt = function (?string $raw): ?int {
        if ($raw === null || trim($raw) === '') {
            return null;
        }
        if (!preg_match('/^-?\d+$/', trim($raw))) {
            return null;
        }
        return (int)trim($raw);
    };
    $vary = array_map('strtolower', $csv(apiHttpHeaderMapGet($headers, 'Vary')));
    return [
        'allow_origin' => apiHttpHeaderMapGet($headers, 'Access-Control-Allow-Origin'),
        'allow_methods' => $csv(apiHttpHeaderMapGet($headers, 'Access-Control-Allow-Methods')),
        'allow_headers' => $csv(apiHttpHeaderMapGet($headers, 'Access-Control-Allow-Headers')),
        'expose_headers' => $csv(apiHttpHeaderMapGet($headers, 'Access-Control-Expose-Headers')),
        'allow_credentials' => $asBool(apiHttpHeaderMapGet($headers, 'Access-Control-Allow-Credentials')),
        'max_age' => $asInt(apiHttpHeaderMapGet($headers, 'Access-Control-Max-Age')),
        'vary_origin' => in_array('origin', $vary, true),
    ];
}

function apiHttpRenderTemplate(string $raw, array $steps): string {
    return (string)preg_replace_callback(
        '/\{\{\s*steps\.([A-Za-z0-9_.-]+)\s*\}\}/',
        function (array $m) use ($steps): string {
            $parts = array_values(array_filter(explode('.', (string)$m[1]), fn($x) => $x !== ''));
            if (count($parts) < 2) {
                throw new SchemaError('api.http scenario template must reference a step field');
            }
            $stepId = (string)$parts[0];
            if (!array_key_exists($stepId, $steps)) {
                throw new SchemaError("api.http scenario template references unknown step: {$stepId}");
            }
            $cur = $steps[$stepId];
            for ($i = 1; $i < count($parts); $i++) {
                $key = (string)$parts[$i];
                if (!is_array($cur) || !array_key_exists($key, $cur)) {
                    throw new SchemaError("api.http scenario template path not found: steps." . (string)$m[1]);
                }
                $cur = $cur[$key];
            }
            if (is_array($cur)) {
                $json = json_encode($cur, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
                return $json === false ? '' : $json;
            }
            if ($cur === null) {
                return '';
            }
            return (string)$cur;
        },
        $raw
    );
}

function evalApiHttpLeaf(
    array $leaf,
    array $resp,
    string $target,
    string $caseId,
    string $path,
    array $specLangLimits,
    array $specLangSymbols,
    array $specLangImports
): void {
    $expr = compileAssertionLeafExpr($leaf, $path);
    if ($target === 'status' || $target === 'headers' || $target === 'body_text') {
        $subject = $target === 'status'
            ? (string)$resp['status']
            : ($target === 'headers' ? (string)$resp['headers_text'] : (string)$resp['body_text']);
        assertLeafPredicate($caseId, $path, $target, 'evaluate', $expr, $subject, $specLangLimits, $specLangSymbols, $specLangImports);
        return;
    }
    if ($target === 'body_json') {
        $parsed = $resp['body_json'] ?? null;
        assertLeafPredicate($caseId, $path, $target, 'evaluate', $expr, $parsed, $specLangLimits, $specLangSymbols, $specLangImports);
        return;
    }
    if ($target === 'cors_json') {
        $cors = $resp['cors_json'] ?? null;
        assertLeafPredicate($caseId, $path, $target, 'evaluate', $expr, $cors, $specLangLimits, $specLangSymbols, $specLangImports);
        return;
    }
    if ($target === 'steps_json') {
        $steps = $resp['steps_json'] ?? [];
        assertLeafPredicate($caseId, $path, $target, 'evaluate', $expr, $steps, $specLangLimits, $specLangSymbols, $specLangImports);
        return;
    }
    if ($target === 'context_json') {
        $context = $resp['context_json'] ?? null;
        assertLeafPredicate($caseId, $path, $target, 'evaluate', $expr, $context, $specLangLimits, $specLangSymbols, $specLangImports);
        return;
    }
    throw new SchemaError("unknown assert target for api.http: {$target}");
}

function evalApiHttpAssertNode(
    mixed $node,
    array $resp,
    ?string $inheritedTarget,
    string $caseId,
    string $path,
    array $specLangLimits,
    array $specLangSymbols,
    array $specLangImports
): void {
    if (is_array($node) && isListArray($node)) {
        foreach ($node as $i => $child) {
            evalApiHttpAssertNode(
                $child,
                $resp,
                $inheritedTarget,
                $caseId,
                "{$path}[{$i}]",
                $specLangLimits,
                $specLangSymbols,
                $specLangImports
            );
        }
        return;
    }
    if (!is_array($node)) {
        throw new SchemaError('assert node must be a mapping or list');
    }
    $stepClass = trim((string)($node['class'] ?? ''));
    if (in_array($stepClass, ['must', 'can', 'cannot'], true) && array_key_exists('checks', $node)) {
        $stepId = trim((string)($node['id'] ?? ''));
        if ($stepId === '') {
            throw new SchemaError("{$path}.id must be a non-empty string");
        }
        $extra = array_diff(array_keys($node), ['id', 'class', 'target', 'checks']);
        if (count($extra) > 0) {
            throw new SchemaError('unknown key in assert step: ' . (string)array_values($extra)[0]);
        }
        $target = trim((string)($node['target'] ?? ''));
        if ($target === '') {
            $target = $inheritedTarget ?? '';
        }
        $children = $node['checks'];
        if (!is_array($children) || !isListArray($children)) {
            throw new SchemaError('assert step checks must be a list');
        }
        if (count($children) === 0) {
            throw new SchemaError('assert step checks must not be empty');
        }
        $stepPath = $path;
        if ($stepClass === 'must') {
            foreach ($children as $i => $child) {
                evalApiHttpAssertNode(
                    $child,
                    $resp,
                    $target,
                    $caseId,
                    "{$stepPath}.checks[{$i}]",
                    $specLangLimits,
                    $specLangSymbols,
                    $specLangImports
                );
            }
            return;
        }
        if ($stepClass === 'can') {
            $anyPassed = false;
            foreach ($children as $i => $child) {
                try {
                    evalApiHttpAssertNode(
                        $child,
                        $resp,
                        $target,
                        $caseId,
                        "{$stepPath}.checks[{$i}]",
                        $specLangLimits,
                        $specLangSymbols,
                        $specLangImports
                    );
                    $anyPassed = true;
                    break;
                } catch (AssertionFailure $e) {
                    // Continue trying other branches.
                }
            }
            if (!$anyPassed) {
                throw new AssertionFailure("all 'can' branches failed");
            }
            return;
        }
        $passed = 0;
        foreach ($children as $i => $child) {
            try {
                evalApiHttpAssertNode(
                    $child,
                    $resp,
                    $target,
                    $caseId,
                    "{$stepPath}.checks[{$i}]",
                    $specLangLimits,
                    $specLangSymbols,
                    $specLangImports
                );
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
    $target = $inheritedTarget;
    if (array_key_exists('target', $node)) {
        $target = trim((string)$node['target']);
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
                evalApiHttpAssertNode(
                    $child,
                    $resp,
                    $target,
                    $caseId,
                    "{$path}.must[{$i}]",
                    $specLangLimits,
                    $specLangSymbols,
                    $specLangImports
                );
            }
            return;
        }
        if ($group === 'can') {
            $anyPassed = false;
            foreach ($children as $i => $child) {
                try {
                    evalApiHttpAssertNode(
                        $child,
                        $resp,
                        $target,
                        $caseId,
                        "{$path}.can[{$i}]",
                        $specLangLimits,
                        $specLangSymbols,
                        $specLangImports
                    );
                    $anyPassed = true;
                    break;
                } catch (AssertionFailure $e) {
                    // Continue trying other branches.
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
                    evalApiHttpAssertNode(
                        $child,
                        $resp,
                        $target,
                        $caseId,
                        "{$path}.cannot[{$i}]",
                        $specLangLimits,
                        $specLangSymbols,
                        $specLangImports
                    );
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
    evalApiHttpLeaf(
        $node,
        $resp,
        $target,
        $caseId,
        $path,
        $specLangLimits,
        $specLangSymbols,
        $specLangImports
    );
}

function evaluateApiHttpCase(string $fixturePath, array $case): array {
    $request = $case['request'] ?? null;
    $requests = $case['requests'] ?? null;
    if ($request !== null && $requests !== null) {
        throw new SchemaError('api.http request and requests are mutually exclusive');
    }
    if ($request === null && $requests === null) {
        throw new SchemaError('api.http requires request mapping or requests list');
    }
    $supportedMethods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS'];
    $mode = resolveApiHttpMode($case);
    $oauthCfg = parseApiHttpOAuthConfig($fixturePath, $case, $mode);
    $oauthMeta = [
        'auth_mode' => $oauthCfg === null ? 'none' : 'oauth',
        'oauth_token_source' => $oauthCfg === null ? 'none' : 'env_ref',
        'token_url_host' => null,
        'scope_requested' => false,
        'token_fetch_ms' => 0,
        'used_cached_token' => false,
    ];
    $timeout = 5;
    if (isset($case['harness']) && is_array($case['harness']) && array_key_exists('timeout_seconds', $case['harness'])) {
        $timeout = (int)$case['harness']['timeout_seconds'];
        if ($timeout <= 0) {
            $timeout = 5;
        }
    }
    $stepsOut = [];
    $stepIndex = [];

    $runOne = function (array $req, array $stepIndexCurrent) use (
        $fixturePath,
        $mode,
        $oauthCfg,
        &$oauthMeta,
        $timeout,
        $supportedMethods
    ): array {
        $method = strtoupper(trim((string)($req['method'] ?? '')));
        if ($method === '') {
            throw new SchemaError('api.http request.method is required');
        }
        if (!in_array($method, $supportedMethods, true)) {
            throw new SchemaError('api.http request.method must be one of: GET, HEAD, OPTIONS, PATCH, POST, PUT, DELETE');
        }
        $rawUrl = trim((string)($req['url'] ?? ''));
        if ($rawUrl === '') {
            throw new SchemaError('api.http request.url is required');
        }
        $url = apiHttpRenderTemplate($rawUrl, $stepIndexCurrent);
        $query = $req['query'] ?? null;
        if ($query !== null) {
            if (!is_array($query)) {
                throw new SchemaError('api.http request.query must be a mapping');
            }
            $parts = @parse_url($url);
            if ($parts !== false && is_array($parts) && array_key_exists('scheme', $parts)) {
                $existing = [];
                parse_str((string)($parts['query'] ?? ''), $existing);
                $merged = array_merge($existing, $query);
                $base = (string)$parts['scheme'] . '://' . (string)($parts['host'] ?? '');
                if (isset($parts['port'])) {
                    $base .= ':' . (string)$parts['port'];
                }
                $base .= (string)($parts['path'] ?? '');
                $qs = http_build_query($merged);
                $url = $qs === '' ? $base : $base . '?' . $qs;
            }
        }
        $resolved = resolveApiHttpUrl($fixturePath, $url);
        if ($resolved['source_type'] === 'url' && $mode !== 'live') {
            throw new SchemaError('api.http request.url network usage requires harness.api_http.mode=live');
        }

        $headerMap = [];
        $hdrs = $req['headers'] ?? [];
        if ($hdrs !== null && !is_array($hdrs)) {
            throw new SchemaError('api.http request.headers must be a mapping');
        }
        if (is_array($hdrs)) {
            foreach ($hdrs as $k => $v) {
                $headerMap[(string)$k] = apiHttpRenderTemplate((string)$v, $stepIndexCurrent);
            }
        }

        $cors = $req['cors'] ?? null;
        if ($cors !== null) {
            if (!is_array($cors)) {
                throw new SchemaError('api.http request.cors must be a mapping');
            }
            $origin = trim((string)($cors['origin'] ?? ''));
            if ($origin !== '' && apiHttpHeaderMapGet($headerMap, 'Origin') === null) {
                apiHttpHeaderMapSet($headerMap, 'Origin', $origin);
            }
            $preflight = (bool)($cors['preflight'] ?? false);
            if ($preflight) {
                if ($method !== 'OPTIONS') {
                    throw new SchemaError('api.http request.cors.preflight requires request.method OPTIONS');
                }
                $requestMethod = strtoupper(trim((string)($cors['request_method'] ?? '')));
                if ($requestMethod === '') {
                    throw new SchemaError('api.http request.cors.request_method is required for preflight');
                }
                apiHttpHeaderMapSet($headerMap, 'Access-Control-Request-Method', $requestMethod);
                if (array_key_exists('request_headers', $cors)) {
                    if (!is_array($cors['request_headers'])) {
                        throw new SchemaError('api.http request.cors.request_headers must be a list');
                    }
                    $vals = [];
                    foreach ($cors['request_headers'] as $h) {
                        $token = trim((string)$h);
                        if ($token !== '') {
                            $vals[] = $token;
                        }
                    }
                    apiHttpHeaderMapSet($headerMap, 'Access-Control-Request-Headers', implode(', ', $vals));
                }
            }
        }

        if ($oauthCfg !== null) {
            $tokenResp = fetchApiHttpOAuthToken($oauthCfg);
            $parts = @parse_url(($oauthCfg['resolved']['source_type'] ?? '') === 'url'
                ? (string)$oauthCfg['resolved']['url']
                : (string)$oauthCfg['resolved']['path']);
            $oauthMeta['token_url_host'] = is_array($parts) && isset($parts['host'])
                ? (string)$parts['host']
                : '';
            $oauthMeta['scope_requested'] = $oauthCfg['scope'] ?? false;
            $oauthMeta['token_fetch_ms'] = (int)$tokenResp['token_fetch_ms'];
            $oauthMeta['used_cached_token'] = (bool)$tokenResp['used_cached_token'];
            if (apiHttpHeaderMapGet($headerMap, 'Authorization') === null) {
                apiHttpHeaderMapSet($headerMap, 'Authorization', 'Bearer ' . (string)$tokenResp['token']);
            }
        }

        $status = 200;
        $bodyText = '';
        $headersText = '';
        $respHeaderMap = [];
        if ($resolved['source_type'] === 'file') {
            $body = file_get_contents((string)$resolved['path']);
            if ($body === false) {
                throw new RuntimeException("cannot read fixture file: {$resolved['path']}");
            }
            $bodyText = (string)$body;
        } else {
            $headers = [];
            foreach ($headerMap as $k => $v) {
                $headers[] = (string)$k . ': ' . (string)$v;
            }
            $bodyData = null;
            if (array_key_exists('body_text', $req) && array_key_exists('body_json', $req)) {
                throw new SchemaError('api.http request.body_text and request.body_json are mutually exclusive');
            }
            if (array_key_exists('body_text', $req)) {
                $bodyData = apiHttpRenderTemplate((string)$req['body_text'], $stepIndexCurrent);
            } elseif (array_key_exists('body_json', $req)) {
                $encoded = json_encode($req['body_json'], JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
                if ($encoded === false) {
                    throw new SchemaError('api.http request.body_json must be json-serializable');
                }
                $bodyData = $encoded;
                if (apiHttpHeaderMapGet($headerMap, 'Content-Type') === null) {
                    $headers[] = 'Content-Type: application/json';
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
                foreach ($responseHeaders as $line) {
                    if (!is_string($line) || strpos($line, ':') === false) {
                        continue;
                    }
                    [$k, $v] = explode(':', $line, 2);
                    $respHeaderMap[trim($k)] = trim($v);
                }
            }
        }
        return [
            'status' => $status,
            'headers_text' => $headersText,
            'headers_map' => $respHeaderMap,
            'body_text' => $bodyText,
            'body_json' => apiHttpJsonOrNull($bodyText),
            'cors_json' => apiHttpCorsProjection($respHeaderMap),
            'method' => $method,
            'url' => $url,
        ];
    };

    if ($request !== null) {
        if (!is_array($request)) {
            throw new SchemaError('api.http requires request mapping');
        }
        $result = $runOne($request, []);
    } else {
        if (!is_array($requests) || !isListArray($requests) || count($requests) === 0) {
            throw new SchemaError('api.http requests must be a non-empty list');
        }
        foreach ($requests as $i => $step) {
            if (!is_array($step)) {
                throw new SchemaError("api.http requests[{$i}] must be a mapping");
            }
            $sid = trim((string)($step['id'] ?? ''));
            if ($sid === '') {
                throw new SchemaError("api.http requests[{$i}].id is required");
            }
            if (array_key_exists($sid, $stepIndex)) {
                throw new SchemaError("api.http requests duplicate id: {$sid}");
            }
            $stepResult = $runOne($step, $stepIndex);
            $stepResult['id'] = $sid;
            $stepsOut[] = $stepResult;
            $stepIndex[$sid] = $stepResult;
        }
        $result = $stepsOut[count($stepsOut) - 1];
    }

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

    $assertSpec = $case['assert'] ?? [];
    $specLangLimits = specLangLimitsFromCase($case);
    $specLangImports = specLangCompileImportsForCase($case);
    $specLangSymbols = loadSpecLangSymbolsForCase($fixturePath, $case, $specLangLimits);
    evalApiHttpAssertNode(
        $assertSpec,
        [
            'status' => (int)$result['status'],
            'headers_text' => (string)$result['headers_text'],
            'body_text' => (string)$result['body_text'],
            'body_json' => $result['body_json'],
            'cors_json' => $result['cors_json'],
            'steps_json' => array_map(
                fn($s) => [
                    'id' => $s['id'] ?? '',
                    'method' => $s['method'] ?? '',
                    'url' => $s['url'] ?? '',
                    'status' => $s['status'] ?? 0,
                    'headers' => $s['headers_map'] ?? [],
                    'body_text' => $s['body_text'] ?? '',
                    'body_json' => $s['body_json'] ?? null,
                    'cors_json' => $s['cors_json'] ?? [],
                ],
                $stepsOut
            ),
            'context_json' => [
                'profile_id' => 'api.http/v2',
                'profile_version' => 2,
                'value' => [
                    'status' => (int)$result['status'],
                    'headers' => $result['headers_map'],
                    'body_text' => (string)$result['body_text'],
                    'body_json' => $result['body_json'],
                    'cors' => $result['cors_json'],
                ],
                'meta' => [
                    'auth_mode' => $oauthMeta['auth_mode'],
                    'oauth_token_source' => $oauthMeta['oauth_token_source'],
                ],
                'context' => [
                    'oauth' => [
                        'token_url_host' => $oauthMeta['token_url_host'],
                        'scope_requested' => $oauthMeta['scope_requested'],
                        'token_fetch_ms' => $oauthMeta['token_fetch_ms'],
                        'used_cached_token' => $oauthMeta['used_cached_token'],
                    ],
                    'scenario' => [
                        'setup_started' => false,
                        'setup_ready' => false,
                        'teardown_ran' => false,
                        'step_count' => count($stepsOut) > 0 ? count($stepsOut) : 1,
                        'step_ids' => array_values(array_map(fn($s) => (string)($s['id'] ?? ''), $stepsOut)),
                    ],
                    'steps' => array_map(
                        fn($s) => [
                            'id' => $s['id'] ?? '',
                            'method' => $s['method'] ?? '',
                            'url' => $s['url'] ?? '',
                            'status' => $s['status'] ?? 0,
                            'headers' => $s['headers_map'] ?? [],
                            'body_text' => $s['body_text'] ?? '',
                            'body_json' => $s['body_json'] ?? null,
                            'cors_json' => $s['cors_json'] ?? [],
                        ],
                        $stepsOut
                    ),
                ],
            ],
        ],
        null,
        (string)$case['id'],
        'assert',
        $specLangLimits,
        $specLangSymbols,
        $specLangImports
    );
    return ['status' => 'pass', 'category' => null, 'message' => null];
}

function evaluateRequires(array $case): ?array {
    if (!array_key_exists('requires', $case)) {
        return null;
    }
    $requires = $case['requires'];
    if (!is_array($requires)) {
        return ['status' => 'fail', 'category' => 'schema', 'message' => 'requires must be a mapping when provided'];
    }
    $caps = $requires['capabilities'] ?? [];
    if (!is_array($caps) || !isListArray($caps)) {
        return ['status' => 'fail', 'category' => 'schema', 'message' => 'requires.capabilities must be a list'];
    }
    $needed = [];
    foreach ($caps as $c) {
        $s = trim((string)$c);
        if ($s !== '') {
            $needed[] = $s;
        }
    }
    $whenMissing = strtolower(trim((string)($requires['when_missing'] ?? 'fail')));
    if ($whenMissing === '') {
        $whenMissing = 'fail';
    }
    if ($whenMissing !== 'skip' && $whenMissing !== 'fail') {
        return ['status' => 'fail', 'category' => 'schema', 'message' => 'requires.when_missing must be one of: skip, fail'];
    }
    $capsSet = array_fill_keys(PHP_CAPABILITIES, true);
    $missing = [];
    foreach ($needed as $cap) {
        if (!array_key_exists($cap, $capsSet)) {
            $missing[] = $cap;
        }
    }
    if (count($missing) === 0) {
        return null;
    }
    sort($missing, SORT_STRING);
    if ($whenMissing === 'skip') {
        return ['status' => 'skip', 'category' => null, 'message' => null];
    }
    return [
        'status' => 'fail',
        'category' => 'runtime',
        'message' => "missing required capabilities for implementation 'php': " . implode(', ', $missing),
    ];
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

    $requiresResult = evaluateRequires($case);
    if ($requiresResult !== null) {
        return [
            'id' => $id,
            'status' => $requiresResult['status'],
            'category' => $requiresResult['category'],
            'message' => $requiresResult['message'],
        ];
    }

    if ($type === 'text.file') {
        try {
            $subjectPath = resolveTextFilePath($fixturePath, $case);
        } catch (SchemaError $e) {
            return [
                'id' => $id,
                'status' => 'fail',
                'category' => 'schema',
                'message' => $e->getMessage(),
            ];
        }

        $subject = file_get_contents($subjectPath);
        if ($subject === false) {
            return [
                'id' => $id,
                'status' => 'fail',
                'category' => 'runtime',
                'message' => "cannot read fixture file: {$subjectPath}",
            ];
        }
        $case['__target_path'] = $subjectPath;
        $res = evaluateTextFileCase($fixturePath, $case, $subject);
    } elseif ($type === 'api.http') {
        try {
            $res = evaluateApiHttpCase($fixturePath, $case);
        } catch (SchemaError $e) {
            return ['id' => $id, 'status' => 'fail', 'category' => 'schema', 'message' => $e->getMessage()];
        } catch (AssertionFailure $e) {
            return ['id' => $id, 'status' => 'fail', 'category' => 'assertion', 'message' => $e->getMessage()];
        } catch (Throwable $e) {
            return ['id' => $id, 'status' => 'fail', 'category' => 'runtime', 'message' => $e->getMessage()];
        }
    } else {
        return [
            'id' => $id,
            'status' => 'fail',
            'category' => 'runtime',
            'message' => "unsupported type for php bootstrap: {$type}",
        ];
    }
    return [
        'id' => $id,
        'status' => $res['status'],
        'category' => $res['category'],
        'message' => $res['message'],
    ];
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

    $report = [
        'version' => 1,
        'results' => $results,
    ];
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
    return 0;
}

try {
    exit(main($argv));
} catch (Throwable $e) {
    fwrite(STDERR, "ERROR: " . $e->getMessage() . "\n");
    exit(1);
}

---
title: Config
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Config

Declarative, schema-driven configuration loading. A `Config<T>` describes how to read and validate a value of type `T` from a `ConfigProvider`, and can be composed, transformed, or yielded inside `Effect.gen` where it automatically resolves the ambient provider. Typed `ConfigError`s distinguish missing-data failures (recoverable via defaults) from validation failures. Reach for it for application settings, secrets, and any value sourced from the environment.

## Key Exports
- `Config<T>` — parse-recipe interface with `.parse(provider)` and `Yieldable`
- `ConfigError`, `SourceError`, `SchemaError` — typed failure union
- `string`, `number`, `boolean`, `int`, `port`, `url`, `date`, `duration`, `logLevel`, `redacted` — leaf constructors
- `schema` — build a `Config` from any `Schema.Codec` or struct
- `succeed`, `fail`, `make` — low-level constructors
- `withDefault` — recover from missing-data errors with a fallback
- `option` — make a config optional, yielding `Option<T>`
- `map`, `mapOrFail`, `orElse`, `all` — transformation and combination
- `unwrap` — lift nested configs

## Source
- `raw/effect-smol/packages/effect/src/Config.ts`

## Related
- [[effect-ts-v4]]
- [[effect-config-provider]]
- [[effect-context]]

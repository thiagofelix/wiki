---
title: main (@effect/ai-codegen)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# main (@effect/ai-codegen)

CLI entrypoint (invoked from `bin.ts`) assembling the ai-codegen `Command` tree via `effect/unstable/cli`. Exposes `generate` and `list` subcommands that drive provider discovery, spec fetching, code generation, replacement application, writing output files, and optional lint/format post-processing with colored progress output.

## Key Exports
- `run` — composed `Command.make("effect-ai-codegen")` ready to run via NodeRuntime
- `generate` subcommand — fetch, generate, patch, replace, write, lint, format per provider
- `list` subcommand — enumerate discovered providers with spec/output/client info
- Flags: `--provider`, `--skip-lint`, `--skip-format`

## Source
- `raw/effect-smol/packages/tools/ai-codegen/src/main.ts`
- `raw/effect-smol/packages/tools/ai-codegen/src/bin.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-ai-codegen-discovery]]
- [[effect-pkg-tools-ai-codegen-postprocess]]

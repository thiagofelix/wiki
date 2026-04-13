---
title: Completions (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Completions (unstable)

Generator for shell completion scripts. Given an executable name, a target shell, and a `CommandDescriptor` built from a root `Command`, produces the completion script as a string. Backed by shell-specific implementations in `internal/completions/`.

## Key Exports
- `Shell` — `"bash" | "zsh" | "fish"`
- `generate(executableName, shell, descriptor)` — produces the completion script string

## Source
- `raw/effect-smol/packages/effect/src/unstable/cli/Completions.ts`

## Related
- [[effect-ts-v4]]
- [[effect-cli]]
- [[effect-cli-command]]
- [[effect-cli-internal]]

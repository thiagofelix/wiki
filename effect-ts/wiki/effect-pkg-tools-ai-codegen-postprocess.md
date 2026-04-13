---
title: PostProcess (@effect/ai-codegen)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# PostProcess (@effect/ai-codegen)

Post-processing service that lints and formats generated provider source by spawning `pnpm exec oxlint --fix` and `pnpm exec dprint fmt` as child processes. Collects stdout/stderr streams and surfaces failures via a rich `PostProcessError` with exit code and output context.

## Key Exports
- `PostProcessor` — service tag with `lint(filePath)` and `format(filePath)` methods
- `PostProcessError` — tagged error with step, command, filePath, exitCode, stdout, stderr
- `layer` — Layer that wires the service on top of `ChildProcessSpawner`

## Source
- `raw/effect-smol/packages/tools/ai-codegen/src/PostProcess.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-ai-codegen-generator]]

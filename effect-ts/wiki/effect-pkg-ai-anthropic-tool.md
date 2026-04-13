---
title: AnthropicTool (@effect/ai-anthropic)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# AnthropicTool (@effect/ai-anthropic)

Catalog of Anthropic provider-defined tools built on `effect/unstable/ai/Tool.providerDefined`. Each entry wires a schema for parameters and success values to Anthropic's native tool IDs so Claude can invoke Bash, Code Execution, Computer Use, Memory, Text Editor, and search/fetch tools through the Effect AI runtime.

## Key Exports
- `AnthropicTool` — union of all returned tool constructors
- `Bash_20241022`, `Bash_20250124` — sandboxed bash execution tools
- `CodeExecution_20250522`, `CodeExecution_20250825` — code-execution sandbox tool versions
- `ComputerUse_20241022`, `_20250124`, `_20251124` — screen/keyboard/mouse actions with `Coordinate`, `Region`, `ScrollDirection`, `ModifierKey`, and action schemas
- `Memory_20250818` — conversational memory tool
- `TextEditor_20241022`/`_20250124`/`_20250429`/`_20250728` — file editor tool versions
- `ToolSearchRegex_20251119`, `ToolSearchBM25_20251119` — tool-search helpers
- `WebFetch_20250910`, `WebSearch_20250305` — browsing/search tools

## Source
- `raw/effect-smol/packages/ai/anthropic/src/AnthropicTool.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-pkg-ai-anthropic-language-model]]
- [[effect-ai]]

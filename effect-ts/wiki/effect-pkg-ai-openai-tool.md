---
title: OpenAiTool (@effect/ai-openai)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OpenAiTool (@effect/ai-openai)

Catalog of OpenAI provider-defined tools built on `Tool.providerDefined`. Maps OpenAI's native tools (code interpreter, file search, web search, shells, MCP, image generation, apply patch) to Effect AI `Tool` definitions so the language model can dispatch them through the Responses API.

## Key Exports
- `OpenAiTool` — union of all returned tool constructors
- `ApplyPatch` — file diff application tool requiring a local handler
- `CodeInterpreter` — sandboxed Python execution
- `FileSearch` — search across uploaded files/vector stores
- `ImageGeneration` — GPT image generation tool with background/quality/format args
- `LocalShell` — shell command execution requiring a local handler
- `Mcp` — access remote Model Context Protocol tool servers
- `Shell` — managed function shell requiring a local handler
- `WebSearch`, `WebSearchPreview` — web search tools with user location and context size

## Source
- `raw/effect-smol/packages/ai/openai/src/OpenAiTool.ts`

## Related
- [[effect-pkg-ai]]
- [[effect-pkg-ai-openai-language-model]]
- [[effect-ai]]

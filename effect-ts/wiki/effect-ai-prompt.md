---
title: Prompt (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Prompt (unstable)

Data structures describing conversation inputs to a language model. A `Prompt` is a list of messages (system/user/assistant/tool) whose content is a union of rich `Part` kinds: text, reasoning, files, tool calls, tool results, and approval requests. Also exposes combinators for constructing and concatenating prompts.

## Key Exports
- `Prompt` — schema/opaque wrapping a list of messages
- `make` — constructs a `Prompt` from a string, message list, or raw input
- `RawInput` — input coercible into a `Prompt`
- `concat` — sequentially combines two prompts
- `fromMessages` / `fromResponseParts` — additional constructors
- `ProviderOptions` — schema for per-provider namespaced options
- `Part` / `PartEncoded` — union of all content-part kinds
- `TextPart`, `ReasoningPart`, `FilePart`, `ToolCallPart`, `ToolResultPart`, `ToolApprovalRequestPart`, `ToolApprovalResponsePart` — content-part classes
- `SystemMessage`, `UserMessage`, `AssistantMessage`, `ToolMessage` — message classes
- `isPart`, `isPrompt` — type guards

## Source
- `raw/effect-smol/packages/effect/src/unstable/ai/Prompt.ts`

## Related
- [[effect-ts-v4]]
- [[effect-ai]]
- [[effect-ai-response]]
- [[effect-ai-language-model]]

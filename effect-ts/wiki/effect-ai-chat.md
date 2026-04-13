---
title: Chat (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Chat (unstable)

Stateful conversation interface layered on top of `LanguageModel`. A `Chat` service holds a `Ref<Prompt>` history and exposes generate/stream operations that automatically append to the conversation, plus import/export and backing-persistence hooks for resumable sessions.

## Key Exports
- `Chat` — `Context.Service` tag for the chat service
- `Service` — interface: history ref, export/exportJson, generateText, generateObject, streamText
- `empty` — creates an empty chat session Effect
- `fromPrompt` — creates a chat seeded from an existing `Prompt`
- `fromExport` / `fromExportUnknown` — rehydrate a chat from exported JSON
- `fromPersistence` — persistence-backed chat via `BackingPersistence`
- `generateText` / `generateObject` / `streamText` — turn-taking wrappers over `LanguageModel`
- Integrates `IdGenerator`, tool toolkits, and `AiError`

## Source
- `raw/effect-smol/packages/effect/src/unstable/ai/Chat.ts`

## Related
- [[effect-ts-v4]]
- [[effect-ai]]
- [[effect-ai-language-model]]
- [[effect-ai-prompt]]

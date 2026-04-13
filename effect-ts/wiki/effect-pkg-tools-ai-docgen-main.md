---
title: main (@effect/ai-docgen)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# main (@effect/ai-docgen)

CLI that walks a directory of example TypeScript files and renders them into a single Markdown document, extracting `@title` and leading JSDoc descriptions as metadata. Supports a `--watch` mode that debounces file changes and regenerates documentation on the fly.

## Key Exports
- `effect-ai-docgen` command — `directory` argument, `-o/--output` and `-w/--watch` flags
- `directoryToMarkdown` — recursive walker producing Markdown from directory contents
- `tsFileMetadata` — extracts title/description/content from a TS source file

## Source
- `raw/effect-smol/packages/tools/ai-docgen/src/main.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-ai-docgen-glob]]

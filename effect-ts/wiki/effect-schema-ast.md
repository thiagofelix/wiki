---
title: SchemaAST
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# SchemaAST

`SchemaAST` defines the runtime abstract syntax tree (AST) that represents every Effect `Schema`. Each schema exposes its `.ast` as a discriminated union of node types (`String`, `Objects`, `Union`, `Suspend`, etc.) with shared fields for annotations, checks, encoding chains, and per-property context. Most users work through `Schema` directly and reach for this module only to inspect, traverse, or programmatically transform schema definitions.

## Mental Model
- `AST` is a tagged union; narrow via guard functions (`isString`, `isObjects`, `isUnion`).
- `Base` is the abstract parent carrying annotations, checks, encoding, and context.
- `Encoding` is a non-empty chain of `Link`s describing decode/encode steps.
- `Check` is a `Filter` or `FilterGroup` attached to a node.
- AST nodes are immutable; helpers return new objects via `Object.create`.

## Key Exports
- `AST`, `Base`, `Link`, `Encoding`, `Check`, `Filter`, `FilterGroup`, `Context` — core types
- `Declaration`, `Literal`, `String`, `Number`, `Boolean`, `BigInt`, `Symbol`, `Objects`, `Arrays`, `Union`, `Suspend`, `TemplateLiteral`, `Enum` — node variants
- `isAST`, `isString`, `isObjects`, `isUnion`, `isSuspend`, `isDeclaration`, etc. — guards
- `toType`, `toEncoded` — memoized projections to type/encoded ASTs
- `flip` — swap decode/encode directions
- `resolve`, `resolveAt`, `resolveIdentifier` — annotation lookup helpers
- `ParseOptions`, `defaultParseOptions` — parser configuration
- `replaceEncoding`, `decodeTo`, `isPattern` — AST builders

## Source
- `raw/effect-smol/packages/effect/src/SchemaAST.ts`

## Related
- [[effect-ts-v4]]
- [[effect-schema]]
- [[effect-schema-parser]]
- [[effect-schema-representation]]

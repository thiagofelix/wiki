---
title: DurableDeferred (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# DurableDeferred (unstable)

Named, schema-typed deferred whose resolution is persisted by the workflow engine. Lets a workflow suspend itself and be woken up by an external event (another workflow, a webhook, a timer) without losing its state. Integrates with `Activity.withActivityAttempt` to associate the deferred with the current attempt token.

## Key Exports
- `DurableDeferred` — interface with `name`, schemas, and `withActivityAttempt`
- `make` — construct a named deferred with optional success/error schemas
- `await` — yieldable effect that suspends the workflow until the deferred resolves
- `done` / `succeed` / `fail` — complete a deferred from outside the workflow
- `token` — retrieve a token identifying the deferred for later completion
- `TokenParent` — context reference carrying the parent token during activity runs

## Source
- `raw/effect-smol/packages/effect/src/unstable/workflow/DurableDeferred.ts`

## Related
- [[effect-workflow]]
- [[effect-workflow-workflow]]
- [[effect-workflow-workflow-engine]]
- [[effect-workflow-activity]]

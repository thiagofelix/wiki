---
title: EventLog (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# EventLog (unstable)

Top-level event-sourced write API built on `EventJournal`. Applications define an `EventLogSchema` from one or more `EventGroup`s and register handlers, compactors, remotes, and reactivity keys through a `Registry`. Writes are typed by tag and produce the event's declared success or error.

## Key Exports
- `EventLog` — service with `write`, `entries`, `destroy`
- `EventLogSchema<Groups>` — schema bundle built with `schema` constructor
- `Registry` — service registering handlers, compactors, remotes, reactivity
- `Handlers` — typed handler namespace with `make` / `item` helpers
- `Identity` — service representing the current user identity
- `layer` — wires `EventLog` over `EventJournal`, `EventLogRemote`, `Reactivity`
- Integrates with `PubSub` for entry change broadcasting
- Automatic compaction via registered compactors

## Source
- `raw/effect-smol/packages/effect/src/unstable/eventlog/EventLog.ts`

## Related
- [[effect-eventlog]]
- [[effect-eventlog-event-journal]]
- [[effect-eventlog-event-log-remote]]
- [[effect-reactivity]]

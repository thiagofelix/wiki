---
title: EventGroup (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# EventGroup (unstable)

A collection of related `Event` definitions representing a portion of the domain. Groups can be built incrementally via `add`, merged, and later implemented with handlers through `EventLogBuilder.group`. The set of events is stored as a record keyed by tag.

## Key Exports
- `EventGroup<Events>` — `Pipeable` interface with `events` record
- `TypeId`, `isEventGroup`
- `empty` — builds an empty group
- `add` — appends a new event definition
- `addError` — attaches an error schema to all events
- `merge` — union of two groups
- `Any` — existential base type

## Source
- `raw/effect-smol/packages/effect/src/unstable/eventlog/EventGroup.ts`

## Related
- [[effect-eventlog]]
- [[effect-eventlog-event]]
- [[effect-eventlog-event-log]]

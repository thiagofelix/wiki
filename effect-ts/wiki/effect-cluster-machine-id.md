---
title: MachineId (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# MachineId (unstable)

Branded integer schema identifying a runner's machine id within the snowflake generator. Must be unique cluster-wide to avoid snowflake collisions.

## Key Exports
- `MachineId` — branded `Schema.Int` with pretty formatter annotation
- `make` — brand a plain number as a `MachineId`

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/MachineId.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-snowflake]]
- [[effect-cluster-runner-storage]]

---
title: Snowflake (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Snowflake (unstable)

Branded bigint snowflake id generator used for unique request/message identifiers across the cluster. Encodes a timestamp, machine id, and sequence number; parts can be decoded back. Layers build a `Generator` that assigns its `MachineId` from `RunnerStorage`.

## Key Exports
- `Snowflake` — branded bigint type and constructor
- `Snowflake.Generator` — interface with `nextUnsafe` and `setMachineId`
- `SnowflakeFromBigInt` / `SnowflakeFromString` — codecs
- `parts` / `partsFromBigInt` — decode a snowflake into timestamp/machineId/sequence
- `layerGenerator` — layer providing a live `Generator`

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/Snowflake.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-machine-id]]
- [[effect-cluster-envelope]]

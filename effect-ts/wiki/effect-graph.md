---
title: Graph
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Graph

Immutable and mutable graph data structure supporting directed and undirected variants. Nodes and edges are addressed by plain numeric indices (`NodeIndex`, `EdgeIndex`). Internally keeps forward and reverse adjacency lists for efficient traversal, plus a cached acyclicity flag. Provides graph algorithms (BFS, DFS, topological sort, connected components, shortest path) along with mutation helpers that return a new graph for the immutable variant.

## Key Exports
- `Graph<N, E, Kind>` — immutable graph
- `MutableGraph<N, E, Kind>` — mutable variant
- `DirectedGraph`, `UndirectedGraph` — type aliases
- `Edge<E>` — edge data class (source, target, data)
- `NodeIndex`, `EdgeIndex` — numeric identifiers
- `directed`, `undirected` — constructors
- `addNode`, `addEdge`, `removeNode`, `removeEdge` — mutation
- `neighbors`, `edges`, `bfs`, `dfs`, `topologicalSort` — traversal/algorithms
- `mutate`, `beginMutation`, `endMutation` — immutable/mutable bridging

## Source
- `raw/effect-smol/packages/effect/src/Graph.ts`

## Related
- [[effect-ts-v4]]
- [[effect-data]]
- [[effect-equal]]

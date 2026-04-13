---
title: Multi-Level Modelling
type: concept
sources:
  - raw/architecture-overview.md
  - raw/am-overview.md
created: 2026-04-13
updated: 2026-04-13
---

# Multi-Level Modelling

Multi-level modelling (also called "two-level modelling") is the central design paradigm of openEHR. It separates stable infrastructure (implemented in software) from variable domain knowledge (expressed in archetypes consumed at runtime).

## The Three Levels

| Level | What | Who Authors | Stability | Implemented In |
|-------|------|-------------|-----------|----------------|
| 1. **Reference Model** | Generic information structures | IT architects | Very stable (decades) | Software + databases |
| 2. **Archetypes** | Reusable clinical content definitions | Domain experts (clinicians) | Moderately stable | Consumed at runtime |
| 3. **Templates** | Use-case specific data sets | Local implementers | Changes frequently | Consumed at runtime |

**Only level 1 is implemented in software.** This is the key insight.

## Why It Matters

### Traditional ("Single-Level") Approach

In conventional systems, domain knowledge is hard-coded:
- Database schema encodes clinical concepts directly
- Adding a new lab test type requires schema changes
- Each clinical concept = code changes + deployment
- Constant model changes → system instability
- Domain knowledge locked inside vendor products

### Multi-Level Approach

- The RM defines ~50-100 generic classes (data types, structures, entries)
- Software is built once against the RM
- Clinical concepts are defined in archetypes **outside** the software process
- Systems consume new archetypes at runtime without code changes
- Domain experts work independently of software developers

## Consequences for Software Engineering

### Traditional Process
```
Requirements → Design → Implement → Test → Deploy → Maintain
     ↑                                              ↓
     └──────── expensive change cycle ──────────────┘
```

Each new clinical concept requires a full software cycle. High ongoing costs.

### Multi-Level Process
```
IT Team:     Build generic platform (once, against RM)
                          ↓
Domain Team: Create archetypes → Create templates → Deploy content
                          ↓
Maintenance: Content updates without software changes
```

The IT team focuses on generic infrastructure (storage, querying, caching). Domain teams work independently building archetypes and templates that systems consume at runtime.

## The Meaningful Instance Space

The RM allows an astronomical number of possible data instances (~10^10+). But meaningful clinical patterns number only ~10^4. Archetypes define exactly this meaningful subset — the "meaningful instance space."

Analogy: A grammar allows infinitely many sentences, but only a tiny fraction are meaningful. Archetypes are like a controlled vocabulary ensuring only sensible sentences are constructed.

## Relationship to Terminologies

Archetypes and terminologies serve fundamentally different purposes:

| | Archetypes | Terminologies |
|-|-----------|---------------|
| **Nature** | Epistemological (how we record information) | Ontological (what exists in the world) |
| **Defines** | Information structures ("microbiology result") | Real-world concepts ("types of microbes") |
| **Authors** | Clinical informaticians | Terminology organizations |

They connect via **terminology bindings** in archetypes — archetype nodes are mapped to terminology concepts, and archetype value sets are mapped to terminology subsets.

## Single-Source Semantics

Because archetypes are abstract, technology-independent definitions, they serve as a **single source of truth** for domain semantics. From one archetype, tools can generate:

- Database schemas
- UI screen forms
- XML/JSON schemas for messages
- Validation rules
- API definitions
- Query templates

Change the archetype → all downstream artifacts update automatically.

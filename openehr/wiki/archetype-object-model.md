---
title: Archetype Object Model (AOM)
type: entity
sources:
  - raw/am-aom2.md
  - raw/am-aom14.md
created: 2026-04-13
updated: 2026-04-13
---

# Archetype Object Model (AOM)

The AOM defines the structural model of archetypes and templates — the classes that represent an archetype in memory. It is primarily a specification for tool builders and EHR platform implementers.

**Release**: AM 2.3.0 (STABLE)

## Purpose

While [[archetype-definition-language|ADL]] is the serialisation syntax, the AOM is the definitive formal expression of archetype semantics. The AOM specifies:

- How to parse and represent archetypes in memory
- How to validate archetypes against the [[reference-model|Reference Model]]
- How to flatten specialised archetypes
- How to generate Operational Templates
- RM adaptation for different reference models

## Core Class Hierarchy

### Archetype Classes

```
ARCHETYPE
    └── AUTHORED_ARCHETYPE
            ├── TEMPLATE
            └── TEMPLATE_OVERLAY
OPERATIONAL_TEMPLATE
```

| Class | Description |
|-------|-------------|
| **ARCHETYPE** | Base archetype: definition, terminology, rules |
| **AUTHORED_ARCHETYPE** | Adds authoring metadata (description, translations, annotations) |
| **TEMPLATE** | Special archetype that assembles others for a use case |
| **TEMPLATE_OVERLAY** | Template-specific constraint modifications to included archetypes |
| **OPERATIONAL_TEMPLATE** | Fully flattened, self-contained template for deployment |

### Constraint Model Classes

```
ARCHETYPE_CONSTRAINT (abstract)
├── C_OBJECT (abstract)
│   ├── C_COMPLEX_OBJECT
│   ├── C_PRIMITIVE_OBJECT
│   │   ├── C_BOOLEAN
│   │   ├── C_STRING
│   │   ├── C_INTEGER
│   │   ├── C_REAL
│   │   ├── C_DATE
│   │   ├── C_TIME
│   │   ├── C_DATE_TIME
│   │   ├── C_DURATION
│   │   └── C_TERMINOLOGY_CODE
│   ├── C_ARCHETYPE_ROOT
│   ├── ARCHETYPE_SLOT
│   └── C_COMPLEX_OBJECT_PROXY
└── C_ATTRIBUTE
    ├── C_SINGLE_ATTRIBUTE
    └── C_MULTIPLE_ATTRIBUTE
```

## Key Classes

### C_COMPLEX_OBJECT

The workhorse class — represents a constraint on a complex (non-primitive) RM type:

- Has a `node_id` (at-code) identifying it within the archetype
- Contains `C_ATTRIBUTE` children defining constrained attributes
- Specifies `occurrences` (how many times it can appear)
- References the RM type being constrained via `rm_type_name`

### C_ATTRIBUTE

Constrains a single attribute of an RM class:

- `rm_attribute_name` — which attribute is constrained
- `existence` — whether the attribute must be present (0..1 or 1..1)
- `cardinality` — for container attributes, how many children (e.g., 1..*)
- `children` — list of `C_OBJECT` constraints on the attribute's value

### C_PRIMITIVE_OBJECT and Subtypes

Constrain leaf-level primitive values. Each subtype handles a specific primitive:

| Class | Constrains | Constraint Types |
|-------|-----------|-----------------|
| C_STRING | String values | Pattern (regex), list of allowed values |
| C_INTEGER | Integer values | Range, list of allowed values |
| C_REAL | Real values | Range, list of allowed values |
| C_BOOLEAN | Boolean values | True only, false only, or both |
| C_DATE | Date values | Pattern (yyyy-mm-dd variants) |
| C_TIME | Time values | Pattern (hh:mm:ss variants) |
| C_DATE_TIME | DateTime values | Pattern combinations |
| C_DURATION | Duration values | Pattern + range |
| C_TERMINOLOGY_CODE | Coded terms | Code list or value set reference |

### C_ARCHETYPE_ROOT

Marks a point where another archetype is referenced/used within this one. This is how templates include archetypes and how archetype composition works.

### ARCHETYPE_SLOT

An open constraint defining where archetypes can be plugged in, with include/exclude rules based on archetype ID patterns.

### C_COMPLEX_OBJECT_PROXY

A "use_node" reference — points to another node in the same archetype to reuse its constraint definition without duplication.

## Terminology Package

Each archetype carries its own terminology:

| Class | Purpose |
|-------|---------|
| **ARCHETYPE_TERMINOLOGY** | Container for all terminology data |
| **TERM_DEFINITION** | Maps at-code → text + description per language |
| **TERM_BINDING** | Maps at-code → external terminology concept |
| **CONSTRAINT_BINDING** | Maps ac-code → terminology value set query |

## Validation and Flattening

### Validation

AOM validation ensures:
1. All constrained RM types and attributes actually exist in the RM
2. All constraint narrowing is valid (child constraints are proper subsets of parent)
3. All at-codes have term definitions in all languages
4. All ac-codes (value sets) have constraint bindings
5. Archetype slot rules reference valid archetype patterns

### Flattening

Converts a specialised archetype from differential form to flat form:

1. Start with the flat form of the parent archetype
2. Apply each differential constraint from the child:
   - Override matching nodes (same node_id)
   - Add new nodes at specified positions
   - Narrow existing constraints
3. Result: complete, self-contained flat archetype

### Operational Template Generation

1. Start with a flattened template
2. Resolve all archetype references (C_ARCHETYPE_ROOT nodes)
3. Fill all slots with specified archetypes
4. Close remaining open slots
5. Merge terminologies from all included archetypes
6. Result: single, self-contained OPT ready for system deployment

## RM Adaptation

The AOM supports adaptation to different reference models via **AOM profiles**. These define:
- Which RM types map to which AOM constraint types
- How RM primitive types correspond to C_PRIMITIVE_OBJECT subtypes
- Lifecycle state mappings

This allows the archetype formalism to be used with reference models other than openEHR (e.g., HL7 FHIR, ISO 13606).

## AOM 1.4 (Legacy)

The AOM 1.4 specification defines the object model for ADL 1.4 archetypes. While AOM 2 is the current version, AOM 1.4 remains relevant because many production systems and tools still work with ADL 1.4 archetypes. The key structural and semantic differences are outlined below.

### ARCHETYPE Class

In AOM 1.4, `ARCHETYPE` **directly inherits** from `AUTHORED_RESOURCE` (from the [[resource-model|Resource Model]]). This contrasts with AOM 2, where the inheritance chain is `ARCHETYPE` -> `AUTHORED_ARCHETYPE` -> `AUTHORED_RESOURCE`. The AOM 1.4 ARCHETYPE class carries all authoring metadata directly, with attributes including `archetype_id`, `concept` (the root at-code, typically `at0000`), `parent_archetype_id` (for specialisation), `definition`, `ontology`, and `invariants`.

### Constraint Model Differences

The AOM 1.4 constraint tree uses an **alternating structure** of object constraint nodes and attribute constraint nodes, similar to AOM 2, but with notable differences:

- **C_ATTRIBUTE subtypes**: AOM 1.4 distinguishes `C_SINGLE_ATTRIBUTE` (single-valued attributes where children represent alternatives) and `C_MULTIPLE_ATTRIBUTE` (container-valued attributes where children co-exist). AOM 2 merges these into a unified `C_ATTRIBUTE`.
- **C_DOMAIN_TYPE**: AOM 1.4 provides `C_DOMAIN_TYPE` as an explicit extension point for domain-specific constraint classes (e.g., `C_QUANTITY`, `C_ORDINAL`, `C_CODED_TEXT`). These allow specialized constraint semantics for particular Reference Model types.
- **CONSTRAINT_REF**: AOM 1.4 includes `CONSTRAINT_REF` (inheriting from `C_REFERENCE_OBJECT`) for delegating constraints to external terminology services via ac-codes. In AOM 2, this is handled differently through `C_TERMINOLOGY_CODE`.
- **ARCHETYPE_INTERNAL_REF**: The AOM 1.4 equivalent of AOM 2's `C_COMPLEX_OBJECT_PROXY` for "use_node" references.

### ARCHETYPE_ONTOLOGY vs ARCHETYPE_TERMINOLOGY

In AOM 1.4, the terminology section uses the class `ARCHETYPE_ONTOLOGY` (reflecting the ADL 1.4 `ontology` keyword). AOM 2 renames this to `ARCHETYPE_TERMINOLOGY` (matching the ADL 2 `terminology` keyword). The internal structure is similar -- both carry term definitions, constraint definitions, term bindings, and constraint bindings -- but the naming reflects the conceptual evolution from "ontology" to "terminology."

### See Also

- [[operational-templates]] -- OPT generation from the AOM
- [[archetype-identification]] -- identification scheme across AOM versions
- [[basic-meta-model]] -- the BMM that provides the computable RM representation AOM validates against

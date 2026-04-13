---
title: Archetype Model
type: entity
sources:
  - raw/am-overview.md
  - raw/am-adl2.md
  - raw/am-aom2.md
created: 2026-04-13
updated: 2026-04-13
---

# Archetype Model (AM)

The Archetype Model defines the formalism for creating, identifying, and processing archetypes and templates — the domain content models that give openEHR its power.

**Release**: AM 2.3.0 (STABLE)

## What Are Archetypes?

Archetypes are formal, computable definitions of clinical content patterns. They constrain the [[reference-model|Reference Model]] to define what constitutes meaningful data for a specific clinical concept.

**Example**: A "blood pressure measurement" archetype constrains an RM `OBSERVATION` to define:
- Required data points: systolic, diastolic, mean arterial pressure
- Valid units: mmHg, kPa
- Valid ranges: systolic 0-1000 mmHg
- Associated metadata: patient position, cuff size, measurement method
- Terminology bindings: SNOMED CT codes for each element

### Why Not Just Use the RM?

The RM allows "any data" — it's too permissive. An OBSERVATION could contain anything. Archetypes constrain the RM to define "meaningful data" — the tiny fraction of possible RM instances that actually represent valid clinical information.

The meaningful instance space (~10^4 patterns) is minuscule compared to the possible instance space (~10^10+) allowed by the RM.

### Key Properties

- **Vendor-independent**: Not tied to any product or technology
- **Reusable**: A blood pressure archetype works in GP clinics, hospitals, home monitoring
- **Authored by clinicians**: Domain experts, not software developers
- **Composable**: Templates combine archetypes for specific use cases
- **Terminology-bound**: Link to SNOMED CT, LOINC, ICD, etc.

## Three-Layer Architecture

```
┌─────────────────────────────────────────┐
│  Templates                              │  Use-case specific data sets
│  (combine archetype elements)           │  (forms, documents, messages)
├─────────────────────────────────────────┤
│  Archetypes                             │  Reusable domain content
│  (constrain RM classes)                 │  definitions
├─────────────────────────────────────────┤
│  Reference Model                        │  Stable information model
│  (generic clinical structures)          │  (implemented in software)
└─────────────────────────────────────────┘
```

## Archetype Identification (HRID)

Human-Readable Identifiers follow this structure:

```
namespace::rm_publisher-rm_closure-rm_class.concept_id.vN.N.N

Example: uk.gov.nhs::openEHR-EHR-COMPOSITION.medication_order.v1.2.0
         ├─────────┤  ├────────────────────┤ ├────────────────┤ ├───┤
         namespace    RM class space         semantic entity    version
```

Components:
- **Namespace**: Custodian organization (e.g., `uk.gov.nhs`, `org.openehr`)
- **RM publisher**: `openEHR`
- **RM closure**: Top-level RM package (e.g., `EHR`, `DEMOGRAPHIC`)
- **RM class**: The RM class being constrained (e.g., `COMPOSITION`, `OBSERVATION`)
- **Concept ID**: Domain concept name in snake_case
- **Version**: Semantic versioning (major.minor.patch)

## Archetype Relationships

### Specialisation (Inheritance)

Archetypes can specialize parent archetypes, adding constraints:

```
openEHR-EHR-OBSERVATION.laboratory_test.v1          (parent)
    └── openEHR-EHR-OBSERVATION.laboratory_test-blood_gas.v1  (child)
```

The child inherits all parent constraints and can:
- Narrow existing constraints (tighten value ranges, restrict cardinality)
- Add new nodes within existing structures
- Override terminology bindings

### Composition (Slot-filling)

Archetypes can define **slots** — places where other archetypes can be plugged in:

```
COMPOSITION archetype (e.g., encounter)
    └── SECTION slot (accepts: clinical findings, vital signs, ...)
        └── OBSERVATION slot (accepts: blood_pressure, heart_rate, ...)
```

Slots specify which archetypes are allowed via include/exclude rules on archetype IDs.

## Archetype Definition Language (ADL)

[[archetype-definition-language|ADL]] is the primary syntax for authoring archetypes. An ADL file contains:

1. **Header**: archetype ID, parent (if specialised), language
2. **Description**: metadata (purpose, use, misuse, keywords, copyright)
3. **Definition**: constraint tree in cADL (constraint ADL) syntax
4. **Terminology**: local term definitions, constraint definitions, terminology bindings
5. **Rules** (optional): invariant expressions

See [[archetype-definition-language]] for full syntax details.

## Archetype Object Model (AOM)

The [[archetype-object-model|AOM]] is the structural model of archetypes — it defines the classes that represent an archetype in memory. Key classes:

| Class | Purpose |
|-------|---------|
| `ARCHETYPE` | Base archetype container |
| `AUTHORED_ARCHETYPE` | Archetype with authoring metadata |
| `TEMPLATE` | Special archetype combining others |
| `TEMPLATE_OVERLAY` | Template-specific constraint layer |
| `OPERATIONAL_TEMPLATE` | Fully-resolved template for deployment |
| `C_COMPLEX_OBJECT` | Constraint on a complex RM object |
| `C_ATTRIBUTE` | Constraint on an RM attribute |
| `C_PRIMITIVE_OBJECT` | Constraint on a primitive value |
| `C_TERMINOLOGY_CODE` | Constraint on coded terms |
| `C_ARCHETYPE_ROOT` | Point where another archetype is used |
| `ARCHETYPE_SLOT` | Slot allowing archetype insertion |

### Source vs Flat Forms

- **Source form (differential)**: Only contains constraints that differ from parent. This is what authors edit.
- **Flat form**: Fully expanded with all inherited constraints. This is what tools and systems use.

## Templates

Templates are technically a kind of archetype but serve a different purpose:

| Aspect | Archetype | Template |
|--------|-----------|----------|
| **Scope** | Single clinical concept | Complete use-case data set |
| **Reuse** | High — used across many contexts | Low — specific to a deployment context |
| **Authors** | Domain experts (clinicians) | Local implementers |
| **Constraints** | Define what's possible | Further restrict to what's needed |

### Operational Templates (OPT)

The **Operational Template** is the deployment artifact — a fully-resolved, flattened template ready for system consumption. It is the basis for generating:
- Screen forms
- Message schemas (XML, JSON)
- Database schemas
- Validation rules
- API definitions

## Compilation Process

```
Source Archetypes (ADL files)
    ↓ parse
AOM objects (in-memory)
    ↓ validate + flatten
Flat Archetypes
    ↓ template resolution
Operational Template (OPT)
    ↓ generate
Concrete artifacts (XSD, JSON Schema, forms, ...)
```

## Terminology Integration

Archetypes connect to external terminologies via bindings:

- **Term bindings**: Map archetype node IDs (at-codes) to terminology concepts
- **Constraint bindings**: Map constraint codes (ac-codes) to terminology value sets

Example: An archetype node `at0004` (systolic blood pressure) can be bound to SNOMED CT concept `271649006 |Systolic blood pressure|`.

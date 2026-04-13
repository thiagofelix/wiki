---
title: BASE Component
type: entity
sources:
  - raw/base-foundation-types.md
  - raw/base-types.md
  - raw/architecture-overview.md
  - raw/base-resource.md
  - raw/lang-bmm.md
  - raw/lang-odin.md
  - raw/lang-el.md
created: 2026-04-13
updated: 2026-04-13
---

# BASE Component

The BASE component defines the foundational types, identifiers, and definitions used across all openEHR specifications.

**Release**: BASE 1.2.0 (STABLE)

## Foundation Types

Primitive and structural types assumed by all openEHR models. These map to implementation language types.

### Primitive Types

| openEHR Type | Java | C# | Description |
|-------------|------|-----|-------------|
| Boolean | Boolean | bool | True/false |
| Integer | Integer | int | Whole number |
| Real | Double | double | Floating point |
| String | String | string | Character sequence |
| Character | Character | char | Single character |
| Octet | Byte | byte | Single byte |

### Structure Types

| Type | Description |
|------|-------------|
| `List<T>` | Ordered collection |
| `Set<T>` | Unordered unique collection |
| `Array<T>` | Indexed collection |
| `Hash<K,V>` | Key-value map |

### Interval Types

| Type | Description |
|------|-------------|
| `Interval<T>` | Generic interval with upper/lower bounds |
| `Point_Interval<T>` | Degenerate interval (single point) |
| `Proper_Interval<T>` | Non-degenerate interval |
| `Multiplicity_Interval` | Integer interval for occurrences (e.g., 0..1, 1..*) |
| `Cardinality` | Multiplicity + ordering + uniqueness |

### ISO 8601 Time Types

| Type | Format | Example |
|------|--------|---------|
| `Iso8601_date` | YYYY-MM-DD | 2024-03-15 |
| `Iso8601_time` | HH:MM:SS.sss±HH:MM | 14:30:00.000+01:00 |
| `Iso8601_date_time` | Combined | 2024-03-15T14:30:00Z |
| `Iso8601_duration` | PnYnMnDTnHnMnS | P1Y2M3DT4H5M6S |
| `Iso8601_timezone` | ±HH:MM or Z | +01:00 |

## Base Types

### Definitions Package

Constants and definitions used throughout openEHR:
- Version lifecycle states
- Terminology IDs for openEHR-internal terminologies

### Identification Package

Comprehensive identification hierarchy:

```
UID (abstract)
├── UUID           # RFC 4122 universally unique identifier
├── ISO_OID        # ISO object identifier
└── INTERNET_ID    # Reverse domain name (e.g., org.openehr)

OBJECT_ID (abstract)
├── TERMINOLOGY_ID    # Terminology identifier (e.g., "SNOMED-CT")
├── ARCHETYPE_ID      # Archetype HRID
├── TEMPLATE_ID       # Template identifier
├── GENERIC_ID        # Generic string ID
├── UID_BASED_ID (abstract)
│   ├── HIER_OBJECT_ID     # UID + optional extensions
│   └── OBJECT_VERSION_ID  # object_id::version::system
├── ARCHETYPE_HRID    # Full human-readable archetype ID
└── VERSION_TREE_ID   # Version tree position

OBJECT_REF            # Reference to an object in another service
├── PARTY_REF         # Reference to a demographic party
├── LOCATABLE_REF     # Reference with path
└── ACCESS_GROUP_REF  # Reference to access control group
```

#### Key ID Formats

**OBJECT_VERSION_ID**: `{object_id}::{creating_system_id}::{version_tree_id}`

Example: `87284370-2D4B-4e3d-A3F3-F303D2F4F34B::uk.nhs.ehr1::1`

**ARCHETYPE_HRID**: `{namespace}::{rm_publisher}-{rm_closure}-{rm_class}.{concept_id}.v{major}.{minor}.{patch}`

Example: `org.openehr::openEHR-EHR-OBSERVATION.blood_pressure.v2.1.0`

### Terminology Package

Types for terminology service integration:
- `TERMINOLOGY_ID` — identifies a terminology
- `CODE_PHRASE` — terminology_id + code_string
- `TERM_MAPPING` — maps between terminologies

### Measurement Package

`MEASUREMENT_SERVICE` interface for units-of-measure validation and conversion.

## Languages Component (LANG)

Related specifications in the LANG component:

| Language | Purpose | Details |
|----------|---------|---------|
| **[[odin\|ODIN]]** | Object Data Instance Notation -- serialization format used in ADL and BMM | Human-readable data notation using angle-bracket delimiters; evolved from dADL in ADL 1.4 |
| **[[basic-meta-model\|BMM]]** | Basic Meta-Model -- formal meta-model for expressing RM and other models | Computable object model representation with support for generics, containers, expressions, and Design by Contract |
| **[[expression-language\|EL]]** | Expression Language -- predicate logic expressions used in archetypes and guidelines | Typed expression syntax based on the BMM expression package; used in archetype rules, Task Planning, and GDL |

## Resource Model

The BASE component also includes the **Resource Model** (`base.resource` package), which defines the abstract concept of an authored, translatable online resource. The central class is `AUTHORED_RESOURCE`, providing:

- `original_language` -- the initial authorship language (ISO 639-1)
- `translations` -- keyed `TRANSLATION_DETAILS` instances for each target language
- `description` -- `RESOURCE_DESCRIPTION` with authoring metadata (author, lifecycle state, purpose, etc.)
- `revision_history` -- audit trail when under change control
- `annotations` -- path-keyed annotations on resource items

`AUTHORED_RESOURCE` is the common ancestor of archetypes (in AOM 1.4, `ARCHETYPE` inherits directly; in AOM 2, via `AUTHORED_ARCHETYPE`) and GDL guidelines. See [[resource-model]] for full details.

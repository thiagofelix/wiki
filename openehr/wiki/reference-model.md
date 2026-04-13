---
title: Reference Model
type: entity
sources:
  - raw/rm-ehr.md
  - raw/rm-common.md
  - raw/rm-data-types.md
  - raw/rm-data-structures.md
  - raw/rm-demographic.md
  - raw/rm-support.md
  - raw/rm-integration.md
  - raw/rm-ehr-extract.md
  - raw/architecture-overview.md
created: 2026-04-13
updated: 2026-04-13
---

# Reference Model (RM)

The openEHR Reference Model is the stable information model at the core of the platform. It is the **only part implemented in software** — all domain-specific semantics are captured in [[archetype-model|archetypes and templates]] that constrain RM structures.

**Release**: RM 1.1.0 (STABLE)

## Package Structure

The RM consists of 8 specifications organized into domain and infrastructure packages:

### Domain Packages

| Package | Spec | Key Classes |
|---------|------|-------------|
| `ehr` | [[ehr-information-model\|EHR IM]] | EHR, EHR_STATUS, EHR_ACCESS, VERSIONED_COMPOSITION |
| `composition` | EHR IM | COMPOSITION, EVENT_CONTEXT |
| `content.entry` | EHR IM | ENTRY, OBSERVATION, EVALUATION, INSTRUCTION, ACTION, ADMIN_ENTRY |
| `content.navigation` | EHR IM | SECTION |
| `demographic` | [[demographic-model\|Demographic IM]] | PARTY, ACTOR, PERSON, ORGANISATION, ROLE |
| `ehr_extract` | EHR Extract IM | EXTRACT, EXTRACT_REQUEST |
| `integration` | Integration IM | GENERIC_ENTRY |

### Infrastructure Packages

| Package | Spec | Key Classes |
|---------|------|-------------|
| `common.archetyped` | [[common-information-model\|Common IM]] | PATHABLE, LOCATABLE, ARCHETYPED, FEEDER_AUDIT |
| `common.generic` | Common IM | PARTY_PROXY, PARTICIPATION, AUDIT_DETAILS, ATTESTATION |
| `common.change_control` | Common IM | VERSIONED_OBJECT, VERSION, CONTRIBUTION |
| `common.directory` | Common IM | FOLDER, VERSIONED_FOLDER |
| `common.resource` | Common IM | AUTHORED_RESOURCE |
| `data_types` | [[data-types\|Data Types IM]] | DV_TEXT, DV_CODED_TEXT, DV_QUANTITY, DV_DATE_TIME, ... |
| `data_structures` | [[data-structures\|Data Structures IM]] | ITEM_TREE, ITEM_LIST, HISTORY, EVENT, ELEMENT, CLUSTER |
| `support` | Support IM | TERMINOLOGY_SERVICE, MEASUREMENT_SERVICE |

## The EHR Structure

An openEHR EHR has this high-level structure:

```
EHR (root object)
├── ehr_id: HIER_OBJECT_ID (globally unique, recommended UUID)
├── system_id: HIER_OBJECT_ID
├── time_created: DV_DATE_TIME
├── ehr_status (versioned) → EHR_STATUS
│   ├── subject: PARTY_SELF
│   ├── is_queryable: Boolean
│   └── is_modifiable: Boolean
├── ehr_access (versioned) → EHR_ACCESS
│   └── settings: ACCESS_CONTROL_SETTINGS
├── compositions (versioned) → COMPOSITION[]
├── folders (versioned) → FOLDER[] (optional, hierarchical indexes)
└── contributions → CONTRIBUTION[] (change-set audit trail)
```

### Compositions

COMPOSITION is the primary data container — the unit of committal, integrity, and versioning. Every clinical interaction results in one or more Compositions.

**Temporal categories**:
- **Persistent**: Ongoing patient state (problem list, medications, allergies). Updated as single instance over patient lifetime. Small total number per patient.
- **Event**: Records of healthcare activities (encounter notes, test results, procedures). Each event creates a new Composition instance.
- **Episodic**: Like persistent but for a defined period (pregnancy, major surgery recovery).

### Entry Types (Clinical Statements)

The Entry package models clinical statements using an ontological approach:

| Entry Type | Purpose | Examples |
|------------|---------|----------|
| **OBSERVATION** | Past events — what was observed | Blood pressure reading, lab result, symptom report |
| **EVALUATION** | Opinions — clinical assessments | Diagnosis, risk assessment, prognosis |
| **INSTRUCTION** | Orders — what should happen | Medication order, referral, procedure request |
| **ACTION** | Interventions — what was done | Drug administered, procedure performed |
| **ADMIN_ENTRY** | Administrative events | Admission, discharge, transfer |

This maps to the clinical problem-solving process: observe → assess → plan → execute.

### Instruction State Machine (ISM)

Instructions progress through a standard state machine:
- **Planning**: initial → planned
- **Execution**: active → suspended → aborted
- **Completion**: completed → cancelled

Each ACTION records an ISM transition, creating a traceable execution history.

## LOCATABLE — The Universal Base Class

Most RM classes inherit from LOCATABLE (via PATHABLE), which provides:

- **name** (`DV_TEXT`) — runtime name, used in path construction
- **archetype_node_id** (`String`) — design-time archetype node identifier (e.g., "at0005")
- **uid** (`UID_BASED_ID`) — optional globally unique identifier
- **links** (`List<LINK>`) — cross-references to other archetyped structures
- **archetype_details** (`ARCHETYPED`) — archetype ID + template ID at root points
- **feeder_audit** (`FEEDER_AUDIT`) — audit trail from non-openEHR feeder systems

This makes all RM data path-addressable and archetype-aware.

## Change Control and Versioning

The RM has built-in version control:

- **VERSIONED_OBJECT<T>** — version container with unique UID
- **VERSION<T>** — abstract version with contribution, commit_audit, lifecycle_state
  - **ORIGINAL_VERSION<T>** — content created locally
  - **IMPORTED_VERSION<T>** — wraps an ORIGINAL_VERSION from another system
- **CONTRIBUTION** — documents a change-set (set of committed versions + audit)

Version identification format: `object-id::version-tree-id::system-id`

All changes to the EHR are:
- Audit-trailed via CONTRIBUTION + AUDIT_DETAILS
- Indelible (previous states always available)
- Traceable (who, when, why, what kind of change)

## Data Types

The `DV_` prefixed data types are clinically-aware:

| Category | Key Types |
|----------|-----------|
| **Text** | DV_TEXT, DV_CODED_TEXT (with CODE_PHRASE binding to terminologies) |
| **Quantity** | DV_QUANTITY (magnitude + units + precision), DV_COUNT, DV_PROPORTION, DV_ORDINAL |
| **Date/Time** | DV_DATE, DV_TIME, DV_DATE_TIME, DV_DURATION |
| **Encapsulated** | DV_MULTIMEDIA, DV_PARSABLE |
| **URI** | DV_URI, DV_EHR_URI |
| **Basic** | DV_BOOLEAN, DV_STATE, DV_IDENTIFIER |

Notable features:
- DV_QUANTITY includes units (UCUM), magnitude, precision, and reference ranges
- DV_CODED_TEXT links to terminology services via CODE_PHRASE
- DV_STATE supports archetyped state machines

## Data Structures

Generic structures for clinical data:

| Structure | Use |
|-----------|-----|
| ITEM_SINGLE | Single values (weight, height) |
| ITEM_LIST | Named lists (address parts, blood test results) |
| ITEM_TABLE | Tabular data (visual acuity, reflex tests) |
| ITEM_TREE | Hierarchical data (microbiology, biochemistry) |
| ELEMENT | Leaf node with value (DV_*) and null_flavour |
| CLUSTER | Grouping node containing ELEMENTs or nested CLUSTERs |
| HISTORY | Time-series container |
| EVENT (POINT_EVENT, INTERVAL_EVENT) | Individual observations in time |

## Demographic Model

Separate from the EHR, the demographic model defines:

- **PARTY** (abstract) → ACTOR → PERSON, ORGANISATION, GROUP, AGENT
- **ROLE** — responsibilities undertaken by an actor
- **PARTY_RELATIONSHIP** — directional relationships between parties
- **PARTY_IDENTITY** — names owned by a party (legal, alias, nickname)
- **CONTACT** / **ADDRESS** — contact information
- **CAPABILITY** — what a role can do

All demographic classes are archetypable. The EHR references demographics via PARTY_PROXY objects (PARTY_SELF for the patient, PARTY_IDENTIFIED for others).

## Integration Model

The Integration package provides GENERIC_ENTRY for legacy data integration via a two-step process:
1. **Syntactic conversion**: Legacy data → GENERIC_ENTRY instances using legacy archetypes
2. **Semantic conversion**: GENERIC_ENTRY → proper ENTRY subtypes (OBSERVATION, etc.) using standardized archetypes

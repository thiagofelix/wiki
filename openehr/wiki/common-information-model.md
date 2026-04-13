---
title: Common Information Model
type: entity
sources:
  - raw/rm-common.md
created: 2026-04-13
updated: 2026-04-13
---

# Common Information Model

The Common IM defines abstract concepts and design patterns used across all openEHR reference models. It provides the foundational infrastructure for archetyping, versioning, auditing, and demographic referencing.

**Release**: RM 1.1.0 (STABLE)

## Packages

| Package | Purpose | Key Classes |
|---------|---------|-------------|
| `archetyped` | Two-level modelling support | PATHABLE, LOCATABLE, ARCHETYPED, LINK, FEEDER_AUDIT |
| `generic` | Domain analysis patterns | PARTY_PROXY, PARTICIPATION, AUDIT_DETAILS, ATTESTATION |
| `directory` | Versioned folder structures | FOLDER, VERSIONED_FOLDER |
| `change_control` | Version control | VERSIONED_OBJECT, VERSION, CONTRIBUTION |
| `resource` | Authored resource metadata | AUTHORED_RESOURCE, RESOURCE_DESCRIPTION |

## Archetyped Package

### PATHABLE

Base class providing path navigation capabilities. Any PATHABLE object can:
- Locate child objects using paths
- Know its parent in a compositional hierarchy
- Check if paths exist and whether they're unique

### LOCATABLE

The universal base class for all archetypable RM data. Provides:

| Attribute | Type | Purpose |
|-----------|------|---------|
| `name` | DV_TEXT | Runtime name — used in path construction |
| `archetype_node_id` | String | Design-time node ID (e.g., "at0005") |
| `uid` | UID_BASED_ID | Optional globally unique identifier |
| `links` | List\<LINK\> | Cross-references to other structures |
| `archetype_details` | ARCHETYPED | Archetype + template ID at root points |
| `feeder_audit` | FEEDER_AUDIT | Audit trail from feeder systems |

### FEEDER_AUDIT

Records audit information for data originating from non-openEHR systems. Tracks:
- Originating system identifier and item ID
- Who committed it and when
- Change type and information status
- Sufficient data for duplicate/version detection and traceability

Supports a two-step conversion model:
1. **Syntactic**: Legacy data → GENERIC_ENTRY (preserves original structure)
2. **Semantic**: GENERIC_ENTRY → proper ENTRY subtypes (maps to standard archetypes)

## Generic Package

### PARTY_PROXY and Subtypes

Abstract references to demographic entities:

| Class | Purpose |
|-------|---------|
| **PARTY_PROXY** | Abstract base — optional external_ref to demographic system |
| **PARTY_SELF** | The record subject (patient). May or may not carry an external reference for privacy. |
| **PARTY_IDENTIFIED** | Any identified party (clinician, organization). Carries name and/or identifiers. |
| **PARTY_RELATED** | Identified party with stated relationship to patient (e.g., mother, spouse). |

Three schemes for patient identification:
1. No external_ref (most secure — fully anonymous)
2. Single external_ref in EHR_STATUS.subject only
3. external_ref in every PARTY_SELF instance

### PARTICIPATION

Models party involvement in activities:
- `function` — role in the activity (DV_TEXT)
- `mode` — interaction mode: direct presence, video conference, etc. (DV_CODED_TEXT)
- `performer` — who participated (PARTY_PROXY)
- `time` — when (optional interval)

Used in two patterns:
- **Named attributes**: where participation type is known at design time (e.g., COMPOSITION.composer)
- **Generic PARTICIPATION lists**: where types vary at runtime (e.g., EVENT_CONTEXT.participations)

### AUDIT_DETAILS

Records committal information:
- `system_id` — which system
- `committer` — who (PARTY_PROXY)
- `time_committed` — when
- `change_type` — what kind of change (creation, amendment, correction, deletion)
- `description` — why (optional)

### ATTESTATION

Extends AUDIT_DETAILS for explicit signing/witnessing:
- Authorization of controlled substances
- Content witnessing by senior clinicians
- Acknowledgment by intended recipients
- Uses openPGP (RFC 4880) for digital signatures

## Directory Package

### FOLDER

Hierarchical organizational structure for indexing Compositions:
- Contains sub-FOLDERs and/or item references (OBJECT_REF)
- Folders **reference** Compositions, they don't contain them
- Multiple folders can reference the same Composition
- Fully archetypable via `details` attribute

### VERSIONED_FOLDER

Version-controlled folder hierarchy — the entire folder tree is versioned as a unit.

## Change Control Package

See [[reference-model#change-control-and-versioning]] for details.

### VERSIONED_OBJECT\<T\>

Version container with:
- Unique `uid` (HIER_OBJECT_ID, typically GUID)
- `owner_id` — reference to owning entity

### VERSION\<T\> Subtypes

- **ORIGINAL_VERSION\<T\>**: Created locally with original content. Contains `uid`, `data`, `preceding_version_uid`, optional `other_input_version_uids` (for merges).
- **IMPORTED_VERSION\<T\>**: Wraps an ORIGINAL_VERSION from another system.

### CONTRIBUTION

Documents a change-set:
- `uid` — unique contribution ID
- `versions` — set of committed version IDs
- `audit` — AUDIT_DETAILS recording who/when/why

### Version Lifecycle

`incomplete` → `complete` → `published` → `deleted` (logical deletion — data retained for audit)

### Version Identification

Format: `object-id::version-tree-id::system-id`

Example: `87284370-2D4B-4e3d-A3F3-F303D2F4F34B::1::uk.nhs.ehr1`

## Resource Package

### AUTHORED_RESOURCE

Generic metadata for any authored resource (archetypes, templates, documents):
- `original_language` — source language
- `translations` — list of TRANSLATION_DETAILS
- `description` — RESOURCE_DESCRIPTION with author, contributors, lifecycle state
- `revision_history` — version history

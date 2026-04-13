# Common Information Model

**Issuer**: openEHR Specification Program
**Release**: RM Release-1.1.0
**Status**: STABLE
**Source**: https://specifications.openehr.org/releases/RM/latest/common.html
**Licence**: Creative Commons Attribution-NoDerivs 3.0 Unported

---

## Table of Contents

1. Preface
2. Overview
3. Archetyped Package
4. Generic Package
5. Directory Package
6. Change Control Package
7. Resource Package

---

## 1. Preface

### 1.1 Purpose

This document describes the architecture of the openEHR Common Reference Model, which contains patterns used by other openEHR reference models.

### 1.2 Related Documents

**Prerequisite documents**:
- The openEHR Architecture Overview

**Related documents**:
- The openEHR Support Information Model
- The openEHR Data Types Information Model

---

## 2. Overview

The openEHR Common Information Model defines abstract concepts and design patterns used in higher-level openEHR models. The model consists of five packages:

- **archetyped**: Two-level modelling concepts (PATHABLE, LOCATABLE, ARCHETYPED, LINK, FEEDER_AUDIT)
- **generic**: Domain-specific analysis patterns (PARTICIPATION, PARTY_PROXY, ATTESTATION)
- **directory**: Versioned folder structure abstraction
- **change_control**: Version control semantics for repositories
- **resource**: Online authored resource semantics

---

## 3. Archetyped Package

### 3.1 Overview

The archetyped package defines core types enabling archetyped data structures.

#### 3.1.1 The PATHABLE Class

PATHABLE defines pathing capabilities used throughout the openEHR reference model. Objects can locate child objects using paths and know their parent in a compositional hierarchy.

#### 3.1.2 The LOCATABLE Class

Most openEHR reference model classes inherit from LOCATABLE, which defines locatability in archetyped structures. It provides:

- **name**: Runtime name used to build runtime paths
- **archetype_node_id**: Design-time archetype identifier (e.g., "at0005")
- **archetype_details**: Metadata for archetype root points
- **uid**: Optional globally unique object identifier
- **links**: References to other archetyped structures
- **feeder_audit**: Audit trail from non-openEHR systems

##### 3.1.2.1 Unique Node Identification

LOCATABLE descendants may have a uid containing a GUID. In current openEHR architecture, GUIDs identify top-level objects (COMPOSITION, EHR_STATUS, PARTY). The recommendation for top-level types is to set uid to a copy of the uid.object_id() value from the owning VERSION object.

#### 3.1.3 Feeder System Audit

FEEDER_AUDIT defines semantics of audit trails for data transformed from non-openEHR systems into openEHR form.

##### 3.1.3.1 Requirements

1. Record medico-legal audit information (from originating system)
2. Record information identifying the immediate system (feeder system)
3. Distinguish incoming items and enable duplicate/version detection
4. Allow inclusion of source content via link or inline

##### 3.1.3.2 Design Principles

The design accommodates data communication involving:
- **Originating system**: Where information was initially created
- **Intermediate systems**: Systems moving information toward openEHR
- **Feeder system**: Intermediate system providing information directly
- **Committing openEHR system**: System transforming and committing data

##### 3.1.3.3 Meta-data

**Medico-legal meta-data** includes:
- Originating system identifier
- Information item identifier in originating system
- Agent who committed the item
- Timestamp of creation/committal
- Type of change (creation, correction, logical deletion)
- Information status (interim, final)
- Version id (where supported)

##### 3.1.3.4 Traceability

Sufficient identifier information must be available to trace the information item's path through health computing infrastructure.

##### 3.1.3.5 Version Detection

New versions detected using identifiers, originating system version id, and content status.

##### 3.1.3.6 Duplicate Detection

Duplicates often result from network failures during transmission.

##### 3.1.3.7 Differentially Coded Data

Some originating systems send new versions containing only new or changed elements.

##### 3.1.3.8 Using Feeder Audit in Converted Data

Two-step conversion approach:
1. **Syntactic conversion**: Convert to Compositions with GENERIC_ENTRY instances using legacy archetypes
2. **Semantic conversion**: Convert to ENTRY subtypes (OBSERVATION, EVALUATION, INSTRUCTION, ACTION) per standardized clinical archetypes

### 3.2 Class Definitions

#### 3.2.1 PATHABLE Class

**Description**: Defines pathing capabilities used throughout openEHR reference models.
**Inheritance**: Any

**Functions**:

| Signature | Meaning |
|-----------|---------|
| `parent(): PATHABLE` | Parent node in compositional hierarchy |
| `item_at_path(a_path: String): Any` | Item at unique path |
| `items_at_path(a_path: String): List<Any>` | Items at non-unique path |
| `path_exists(a_path: String): Boolean` | True if path exists |
| `path_unique(a_path: String): Boolean` | True if path resolves to single item |
| `path_of_item(a_loc: PATHABLE): String` | Path to item relative to root |

#### 3.2.2 LOCATABLE Class

**Description**: Root class of information model classes that can be archetyped.
**Inheritance**: PATHABLE

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | name | DV_TEXT | Runtime name for building runtime paths |
| 1..1 | archetype_node_id | String | Design-time archetype identifier |
| 0..1 | uid | UID_BASED_ID | Optional globally unique object identifier |
| 0..1 | links | List<LINK> | Links to other archetyped structures |
| 0..1 | archetype_details | ARCHETYPED | Archetyping details at root points |
| 0..1 | feeder_audit | FEEDER_AUDIT | Audit trail from non-openEHR systems |

**Invariants**:
- `Links_valid`: `links /= Void implies not links.is_empty`
- `Archetyped_valid`: `is_archetype_root xor archetype_details = Void`
- `Archetype_node_id_valid`: `not archetype_node_id.is_empty`

#### 3.2.3 ARCHETYPED Class

**Description**: Contains archetype identification information.

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | archetype_id | ARCHETYPE_ID | Globally unique archetype identifier |
| 0..1 | template_id | TEMPLATE_ID | Globally unique template identifier |
| 1..1 | rm_version | String | Reference model version used |

#### 3.2.4 LINK Class

**Description**: Defines logical relationships between items.

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | meaning | DV_TEXT | Clinical relationship description |
| 1..1 | type | DV_TEXT | Clinical/domain meaning |
| 1..1 | target | DV_EHR_URI | Logical target object as fully qualified path |

---

## 4. Generic Package

### 4.1 Overview

Generic package classes represent domain abstractions applicable across health informatics, including participation patterns, party references, attestation semantics, and audit information.

### 4.2 Design Principles

#### 4.2.1 Referring to Demographic Entities

Two mechanisms exist:
1. **PARTY_REF**: Direct identifier of party in external system
2. **PARTY_PROXY**: Small descriptive data plus optional PARTY_REF

Subtypes represent mutually distinct categories:
- **PARTY_SELF**: Record subject reference
- **PARTY_IDENTIFIED**: Any other party reference

##### 4.2.1.1 PARTY_SELF and Referring to Patient from EHR

Three schemes for patient demographic/PMI reference:
1. No external_ref set (most secure)
2. Single external_ref in EHR_STATUS._subject_
3. external_ref in every PARTY_SELF instance

#### 4.2.2 Participation

Participation abstracts party interaction in activities. Modeled two ways:
- **Named attributes**: Where participation types are known (e.g., `_committer_: PARTY_PROXY`)
- **Generic PARTICIPATION**: Where participation types are design-time unknown

#### 4.2.3 Audit Information

##### 4.2.3.1 Audit Details

AUDIT_DETAILS records: `_system_id_`, `_committer_`, `_time_committed_`, `_change_type_`, optional `_description_`.

##### 4.2.3.2 Revision History

REVISION_HISTORY and REVISION_HISTORY_ITEM express revision history with audit items associated with revision numbers.

#### 4.2.4 Attestation

Attestation represents explicit signing by healthcare agents:
- Authorization of controlled substances/procedures
- Content witnessing by senior clinical professional
- Acknowledgment by intended recipient

Modeled as AUDIT_DETAILS subtype with additional signing-related information.

**Digital signature generation** uses openPGP standard (IETF RFC 4880).

### 4.3 Class Descriptions

#### 4.3.1 PARTY_PROXY Class

**Description**: Abstract concept of party proxy.
**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 0..1 | external_ref | PARTY_REF | Optional demographic/identification system reference |

#### 4.3.2 PARTY_SELF Class

**Description**: Party proxy representing record subject.
**Inheritance**: PARTY_PROXY

#### 4.3.3 PARTY_IDENTIFIED Class

**Description**: Proxy data for identified parties other than record subject.
**Inheritance**: PARTY_PROXY

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 0..1 | name | String | Optional human-readable name |
| 0..1 | identifiers | List<DV_IDENTIFIER> | Formal computable identifiers |

**Invariants**:
- `Basic_validity`: `name /= Void or identifiers /= Void or external_ref /= Void`

#### 4.3.4 PARTY_RELATED Class

**Description**: Party proxy identifying party and its relationship to record subject.
**Inheritance**: PARTY_IDENTIFIED

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | relationship | DV_CODED_TEXT | Subject relationship to record subject |

#### 4.3.5 PARTICIPATION Class

**Description**: Models party participation in activities.

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | function | DV_TEXT | Party function in participation |
| 0..1 | mode | DV_CODED_TEXT | Interaction mode |
| 1..1 | performer | PARTY_PROXY | Participant party identity |
| 0..1 | time | DV_INTERVAL<DV_DATE_TIME> | Participation interval |

#### 4.3.6 AUDIT_DETAILS Class

**Description**: Attributes required documenting repository information item committal.

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | system_id | String | Logical EHR system identifier |
| 1..1 | time_committed | DV_DATE_TIME | Item committal time |
| 1..1 | change_type | DV_CODED_TEXT | Change type |
| 0..1 | description | DV_TEXT | Committal reason |
| 1..1 | committer | PARTY_PROXY | Committing user identity |

#### 4.3.7 ATTESTATION Class

**Description**: Records healthcare agent attestation of record content items.
**Inheritance**: AUDIT_DETAILS

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 0..1 | attested_view | DV_MULTIMEDIA | Optional content visual representation |
| 0..1 | proof | String | Attestation proof |
| 0..1 | items | List<DV_EHR_URI> | Attested items as runtime paths |
| 1..1 | reason | DV_TEXT | Attestation reason |
| 1..1 | is_pending | Boolean | True if outstanding |

#### 4.3.8 REVISION_HISTORY Class

**Description**: Defines revision history notion.

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | items | List<REVISION_HISTORY_ITEM> | History items in most-recent-last order |

#### 4.3.9 REVISION_HISTORY_ITEM Class

**Description**: Revision history entry.

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | version_id | OBJECT_VERSION_ID | Version identifier |
| 1..1 | audits | List<AUDIT_DETAILS> | Revision audits |

---

## 5. Directory Package

### 5.1 Overview

VERSIONED_FOLDER represents VERSIONED_OBJECT<FOLDER>, enabling FOLDER structure versioning over time. FOLDER instances contain FOLDERs and/or item references to other typically-versioned objects.

**Example paths**:
```
/folders[hospital episodes]/items[1]
/folders[patient entered data]/folders[diabetes monitoring]
/folders[homeopathy contacts]
```

### 5.2 Class Descriptions

#### 5.2.1 VERSIONED_FOLDER Class

**Description**: Version-controlled FOLDER hierarchy.
**Inheritance**: VERSIONED_OBJECT

#### 5.2.2 FOLDER Class

**Description**: Named folder concept.
**Inheritance**: LOCATABLE

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 0..1 | items | List<OBJECT_REF> | References to other typically-versioned objects |
| 0..1 | folders | List<FOLDER> | Sub-folders |
| 0..1 | details | ITEM_STRUCTURE | Archetyped FOLDER meta-data |

---

## 6. Change Control Package

### 6.1 Overview

Formal version control and change management support EHR repository properties: consistency, indelibility, traceability, distributed sharing.

### 6.2 Basic Semantics

#### 6.2.1 Typing

Classes VERSIONED_OBJECT<T>, VERSION<T>, ORIGINAL_VERSION<T>, IMPORTED_VERSION<T> are generic with type parameter T.

#### 6.2.2 Versioned Objects

Each VERSIONED_OBJECT has unique identifier (uid attribute, typically GUID-containing HIER_OBJECT_ID) and owning object reference (owner_id attribute).

#### 6.2.3 Version and its Subtypes

**VERSION subtypes**:
1. **ORIGINAL_VERSION<T>**: Version created with original content at creation time. Unit of copying in distributed environments.
2. **IMPORTED_VERSION<T>**: Wraps ORIGINAL_VERSION<T> from another system.

#### 6.2.4 The 'Virtual Version Tree'

Version creation at each system achieves compatibility with virtual version tree resulting from superimposing version trees of all copies.

#### 6.2.5 Contributions

All logical changes achieved by committing new Versions or new Attestation objects:
- **Addition**: New VERSIONED_OBJECT created with first ORIGINAL_VERSION; change_type = `249|creation|`
- **Deletion**: New ORIGINAL_VERSION with data Void; change_type = `523|deleted|`
- **Modification**: New ORIGINAL_VERSION with updated content
- **Correction**: New ORIGINAL_VERSION with corrected content
- **Importing**: IMPORTED_VERSION wrapping ORIGINAL_VERSION from another system
- **Attestation**: New ATTESTATION object added to existing VERSION

#### 6.2.6 Committal and Audits

Repository committal requires Contribution object documenting change set.

### 6.3 Versioning Semantics

#### 6.3.1 Version Lifecycle

- **Incomplete**: Initial state; data still being entered
- **Complete**: Data entry complete
- **Published**: Made available for access
- **Deleted**: Logically deleted but retained for audit

#### 6.3.2 Logical Deletion

Represented by new ORIGINAL_VERSION with Void data attribute, change_type = `523|deleted|`.

#### 6.3.3 Version Identification

##### 6.3.3.1 Local Versioning

Format: `object-id::version-tree-id::system-id`
Example: `87284370-2D4B-4e3d-A3F3-F303D2F4F34B::1::uk.nhs.ehr1`

### 6.4 Semantics in Distributed Systems

#### 6.4.1 Copying

Copy creates IMPORTED_VERSION wrapping original ORIGINAL_VERSION, preserving original version identifier.

#### 6.4.2 Version Merging

Merge creates new ORIGINAL_VERSION whose preceding_version_uid indicates primary predecessor; other_input_version_uids lists merged-in versions.

### 6.5 Class Descriptions

#### 6.5.1 VERSIONED_OBJECT Class

**Description**: Version container providing versioning facilities for one item.

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | uid | HIER_OBJECT_ID | Container unique identifier |
| 1..1 | owner_id | UID | Owning object identifier |

#### 6.5.2 VERSION Class

**Description**: Abstract version class.

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | contribution | CONTRIBUTION | Contribution committing this version |
| 1..1 | commit_audit | AUDIT_DETAILS | Version committal audit |
| 0..1 | attestations | List<ATTESTATION> | Version attestations |
| 1..1 | lifecycle_state | DV_CODED_TEXT | Version lifecycle state |

#### 6.5.3 ORIGINAL_VERSION Class

**Description**: Version created with original content.
**Inheritance**: VERSION<T>

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | uid | OBJECT_VERSION_ID | Version unique identifier |
| 0..1 | preceding_version_uid | OBJECT_VERSION_ID | Preceding version identifier |
| 1..1 | data | T | Version content data |
| 0..1 | other_input_version_uids | List<OBJECT_VERSION_ID> | Merged-in version identifiers |

#### 6.5.4 IMPORTED_VERSION Class

**Description**: ORIGINAL_VERSION wrapper from another system.
**Inheritance**: VERSION<T>

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | item | ORIGINAL_VERSION<T> | Wrapped original version |

#### 6.5.5 CONTRIBUTION Class

**Description**: Change set documentation.

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | uid | OBJECT_ID | Contribution unique identifier |
| 1..1 | versions | Set<OBJECT_VERSION_ID> | Committed version identifiers |
| 1..1 | audit | AUDIT_DETAILS | Change set committal audit |

---

## 7. Resource Package

### 7.1 Overview

The resource package defines online authored resource semantics including documents, templates, archetypes.

### 7.2 Class Descriptions

#### 7.2.1 AUTHORED_RESOURCE Class

**Description**: Online authored resource.

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | original_language | CODE_PHRASE | Original language |
| 0..1 | translations | List<TRANSLATION_DETAILS> | Translations |
| 0..1 | description | RESOURCE_DESCRIPTION | Resource meta-data |
| 0..1 | revision_history | REVISION_HISTORY | Revision history |

#### 7.2.2 TRANSLATION_DETAILS Class

**Description**: Translation information for single language.

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | language | CODE_PHRASE | Translation language |
| 1..1 | translator | PARTY_IDENTIFIED | Translator identity |
| 1..1 | date | DV_DATE | Translation date |

#### 7.2.3 RESOURCE_DESCRIPTION Class

**Description**: Resource meta-data.

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | original_author | Hash<String, String> | Original author details |
| 0..1 | other_contributors | List<String> | Other contributor names |
| 1..1 | lifecycle_state | String | Development lifecycle state |
| 1..1 | resource_package_uri | String | Resource package location |
| 0..1 | details | Hash<String, RESOURCE_DESCRIPTION_ITEM> | Language-specific details |

#### 7.2.4 RESOURCE_DESCRIPTION_ITEM Class

**Description**: Language-specific resource description.

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | language | CODE_PHRASE | Language |
| 1..1 | purpose | String | Resource purpose |
| 0..1 | keywords | List<String> | Keywords |
| 0..1 | use | String | Intended use |
| 0..1 | misuse | String | Misuse avoidance |
| 0..1 | copyright | String | Copyright |

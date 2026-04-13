# EHR Extract Information Model

## Document Metadata

**Issuer**: openEHR Specification Program

**Release**: RM Release-1.1.0

**Status**: STABLE

**Keywords**: EHR, extract, openehr

**Copyright**: © 2003 - 2021 The openEHR Foundation

**License**: Creative Commons Attribution-NoDerivs 3.0 Unported

---

## Table of Contents

1. [Preface](#preface)
2. [Requirements](#requirements)
3. [Design Overview](#design-overview)
4. [Extract.common Package](#extractcommon-package)
5. [The openehr_extract Package](#the-openehr_extract-package)
6. [Generic_extract Package](#generic_extract-package)
7. [Synchronisation Extracts](#synchronisation-extracts)
8. [The Message Package](#the-message-package)
9. [Semantics of openEHR and ISO 13606 Extracts](#semantics-of-openehr-and-iso-13606-extracts)

---

## Preface

### Purpose

This specification defines the architecture of the openEHR EHR Extract Information Model. The model formally establishes the concepts of extract request, extract, various content types including openEHR and non-openEHR materials, and messaging wrappers. It addresses use cases spanning EHR system communication, clinical content messaging, and EHR system synchronisation, and provides an equivalent to ISO 13606-1 EHR Extract.

**Intended audience**:
- Standards bodies producing health informatics standards
- Academic groups using openEHR
- Open source healthcare community
- Solution vendors
- Medical informaticians and clinicians
- Health data managers

### Related Documents

Prerequisite reading:
- The openEHR Architecture Overview
- The openEHR EHR Information Model

### Status

This specification is in the STABLE state. The development version is available at https://specifications.openehr.org/releases/RM/latest/ehr_extract.html

### Feedback

- Forum: openEHR RM specifications forum
- Issues: specifications Problem Report tracker
- Change history: RM component Change Request tracker

### Conformance

Conformance is determined through formal testing against openEHR Implementation Technology Specifications (ITSs), such as IDL interfaces or XML schemas. ITS conformance indicates model conformance.

---

## Requirements

### Overview

The Extract Information Model is designed to satisfy requirements expressed through operational environments, use cases, and functional/security specifications. The model uses openEHR standardised information structures as the shared language for coarse-grained information import and export from health information systems.

The Extract model is neutral regarding communication technology—structures work equally well in web services or messaging environments including secure email.

### Operational Environment

#### openEHR Environments

The assumed operational environment involves:

- **Requesting system**: Creates a Request for information from one or more subject records
- **Subject**: Patient EHR, Person record in demographics, or other logically meaningful top-level entity
- **Responding system(s)**: Reply with one or more Extracts
- **Transport mechanism**: Middleware, web services, or point-to-point protocols (e.g., SMTP)

**Information structure assumptions**:

- Each system contains one or more Subject records; the same Subject may exist in multiple systems
- Each Subject record consists of one or more Version containers holding version history
- Each Version container maintains one piece of content
- Distinct containers hold persistent Compositions (e.g., medications list, problem list) and event Compositions
- Each Version corresponds to content state at a specific commit time
- Groups of Versions from different containers within a system form Contributions (change-sets)

This hierarchy reveals 1:N relationships, with Contributions providing an alternative content view. Each hierarchy level requires identifier systems.

#### Non-openEHR Environments

The Extract can be used in non-openEHR systems where content is expressed as templated archetypes. Two information levels are assumed:

- **Record/patient**: Information division by subject of care
- **Document (Composition)**: Coarsest grain item comprising a record

**Versioning assumptions** in some systems:
- Document version
- Document version set identifier
- Document type/schema type
- Document type version

Typical use involves legacy information in archetyped form for cross-enterprise communications (discharge summaries, referrals).

#### Location of Information

Two scenarios are possible:

1. **Direct request**: Requesting system explicitly identifies target systems
2. **Location service-mediated**: Health information location service identifies relevant systems

The specification assumes Extract requests occur between the Requesting system and each Responding system, even if a location service generated the system list. The specification does not encompass a compendium of Extracts from multiple Responding systems.

#### Granularity of Extract Data

The lowest information level shown in a Responding system is "content," corresponding to top-level structures such as Compositions, Folder trees, and Parties. While database queries typically return fine-grained results, the Extract specification allows only Composition-level granularity.

**Rationale**: Extracts aim to make EHR portions available elsewhere rather than intelligently query the record in situ.

#### Time

Versioned health record systems are bitemporal, including two time notions:

- **Real world time**: Relates to clinical events or states (diagnosis time, discharge date)
- **System time**: Information system events (Contribution committal)

Both dimensions may need specification in a Request.

### Use Cases

#### Single Patient, Ad Hoc Request

A key clinical need is obtaining some or all of a patient's EHR from remote systems. Requests typically arise from patient referrals but also include travel-related scenarios.

**Request possibilities**:
- Entire EHR from identified source on first request
- All changes since last request from specified system
- Persistent Compositions (medications, problem list, allergies)
- Compositions matching specific queries (e.g., blood sugar measurements in past six months)

Time meanings are content-dependent, varying for Observations versus Evaluations.

#### Multiple Patient, Batch Send

Laboratory requirements for sending test result data for multiple patients periodically to known receivers (hospitals, clinics, state health systems) are common. Batch sends typically represent "standing requests" and may occur periodically (e.g., hourly), on availability basis, or per other schemes.

**Note**: Data currently often sent as HL7v2, Edifact, or similar messages.

#### Previous Versions and Revision Histories

Requests may specify versions other than latest for studies or medico-legal investigations establishing what information was visible in systems at earlier times.

**Example**: Determining problem list, allergy list, and patient preferences compatibility with medications list at a specific earlier time.

Revision histories of Versioned containers may be requested to identify interesting Versions.

#### Systematic Update and Persisted Requests

Large healthcare delivery environments (state/regional health services) routinely treat patients via multiple providers with distributed clinical computing. Centralised data aggregation with routine updating is needed.

**Requirements**:
- Request-once, repeated-action paradigm until revoked
- Periodic updates of changes since last update
- Event-driven updates (any EHR change, medications/allergies changes, etc.)

Persisting requests in servers enables referencing by identifier for later invocations, supporting both one-off and systematic scenarios.

#### Sharing of non-EHR openEHR Data

Beyond EHRs, openEHR systems include demographics and workflow services. Extract request forms should work for importing information from openEHR systems to non-openEHR systems (e.g., openEHR demographics to hospital Patient Master Index).

The same general request format applies, but specifies non-EHR business objects (e.g., PARTYs for demographics) instead of patient records.

#### Provision of Data from non-openEHR Systems

Shared EHR systems often aggregate data from existing systems in standardised form. Non-openEHR systems may provide data via:
- Various messaging forms (HL7, Edifact)
- Various EMR documents (ISO 13606, HL7 CDA)
- Other standardised or non-standardised formats

Some developers provide openEHR-compatible export gateways serialising data into openEHR structures, particularly Composition/GENERIC_ENTRY forms.

**Types of source systems**: Pathology systems, departmental hospital systems (radiology RIS, histopathology, etc.)

#### Patient Access to Health Data

Direct patient access outside clinical encounters is a common aspiration. Access modes include:

- USB stick or portable device containing partial or complete health record
- Secure web service access (similar to online banking)
- Encrypted email attachments (unsolicited or by request)
- Kiosk or PC access in waiting rooms

USB and email scenarios involve asynchronous EHR access, addressable by EHR Extract.

**Portable device use**: Device acts as synchronisation transport between home PC and clinic systems, copying required changes via Contributions.

**Email scenario**: Extract contains patient-requested information or laboratory data for integration, often as Compositions with GENERIC_ENTRIEs.

#### Move of Entire Record

Patient EHRs may move permanently due to patient relocation, care transfer, or data centre reorganisation—termed change of custodianship. The record is deleted (possibly archived) at the sending system.

**Requirement**: Complete EHR export (including all previous versions) in interoperable form to the destination system, as implementations typically differ in platform, versioning model, etc.

#### System Synchronisation

##### Mirroring

Two openEHR systems containing identical data kinds may maintain logical "mirrors" (clones). Mirrored records are read-only, with the mirror being a slave to its source. Synchronisation is unidirectional.

**Mechanism**: The openEHR Contribution provides the necessary semantic unit as the change unit to any record and update unit for mirrored records.

##### The Virtual EHR

Multiple systems allowing changes while systematically synchronising form a "virtual EHR"—the totality of changes together constitute a complete EHR even if individual systems lack all changes at any instant.

**Typical situation**: Large-scale distributed e-health environments use ad hoc or systematic synchronisation, possibly bidirectional.

**Advantage**: openEHR version identification directly supports virtual EHRs; synchronisation occurs by copying Versions between places and adding to relevant Versioned containers.

**Strategy**: Large health computing environments may systematically use cloning and mirroring for truly decentralised systems.

**Defining condition**: One or more (possibly all) records in a system are maintained as perfect copies in other systems, with possible delays.

#### Communication between non-openEHR EMR/EHR Systems

Since the openEHR Extract represents a generic, open standardised clinical information specification, non-openEHR systems may use it. Extract content typically consists of Compositions and Generic_entries, with optional versioning depending on source system support.

### Technical Requirements

#### Specification of Content

Content is specifiable via matching criteria in two forms:

1. Lists of specific top-level content items
2. Queries specifying top-level items by matching subparts

Queries are expressed in the Archetype Query Language.

#### Specification of Versions

The openEHR Extract supports detailed versioned data access. Version inclusion can be specified as:

- Source EHR version time (taking all content at specified time)
- More specific terms:
  - Commitment time window
  - With or without revision history, or revision history only
  - All, some, or latest versions per content item
  - Identified Contributions or Contributions since specified time

#### Completeness of Data

Extracted information must be self-standing clinically—understandable without assuming other responding system access. For any references in transferred EHR data, the Extract must either contain targets or assume the requestor has independent access or doesn't require them.

##### References to Other Parts of the Same EHR

openEHR includes two cross-reference kinds: LINKs (in LOCATABLE) and hyperlinks (in DV_TEXT.hyperlink). Both use DV_EHR_URI instances for link targets.

**Decision requirement**: Which links require the referenced item to accompany the original item (e.g., discharge summary referring to medication list, problem list, lab reports) versus unneeded links.

**Specification options**:
- Link depth (number of jumps to continue from original item; 0 means don't follow)
- For LINK instances: link type to follow (matching type attribute)

##### References to Other EHRs

EHR internal references to other EHR items (e.g., parent or organ donor EHRs) may occur. No requirement exists to follow such links when constructing Extracts.

##### References to Resources Outside the EHR

Computable external references occur via DV_URI instances (standalone or in DV_TEXT hyperlinks) to resources like online guidelines, or DV_MULTIMEDIA instances with DV_URI references to multimedia resources (e.g., PACS radiology images).

**Characteristic**: URIs remain semantically valid wherever data moves due to global uniqueness, but resolution isn't guaranteed (e.g., PACS image in one provider environment transferred to another).

**Practical note**: Images are usually small (e.g., 200kb JPG), not large original sets (hundreds of Mb). Original image access would be requested separately from EHR Extracts.

##### References to Demographic Entities

Two demographic entity kinds are referenced throughout openEHR EHRs:

1. **Individual providers and institutions**: Referenced from PARTY_PROXY objects via external_ref (references to demographic repositories, hospital MPI, or identity services). PARTY_IDENTIFIED subtypes can carry human-readable names and computational identifiers.

2. **EHR subject references**: Found in PARTY_SELF subtypes, may or may not be present depending on security levels. When present, references demographic/identity system records.

**Extract requirement**: Referenced demographic items may need inclusion in Extracts if receivers lack demographic system access. Patient demographics inclusion is optional—requestors may specify separately whether to include referenced demographic entities other than the subject.

##### Archetypes and Terminology

Terminology codes are stored in DV_TEXT instances (via mapping attribute) and DV_CODED_TEXT.defining_code. openEHR systems carry text values in locale language. For normal use, this suffices; for decision support or inferencing, terminology must be available separately.

**Assumption**: Where requestors require inferencing or terminology capabilities, independent complete terminology access is obtained.

**Archetype handling**: Archetype identifiers mentioned in EHR data/meta-data aren't included in Extracts; they must be resolved separately.

#### Security and Privacy

Security becomes paramount for EHR Extracts due to exposure in potentially uncontrolled environments. General requirements:

- Access control rules defined in EHR_ACCESS objects at source
- Other access rules in policy services
- Requesting user authentication
- Digital signing using requestor's (preferably certified) public key
- Notarisation optionally providing non-repudiable proof (outside specification scope)

#### Update Basis

Beyond content specification, an update basis must be specified:

- **Simplest case**: Ad hoc one-off query
- **Complex cases**: Periodic update or event-driven update

##### Persistent Request

Requests can be persisted in servers allowing:
- Server-side request storage for later reference by identifier
- Repeat activation by requestor via identifier
- Changes-only extract update patterns

---

## Design Overview

### Abstract Communication Model

The Extract model uses two design concepts:

1. **Request vs. Extract distinction**: Requests are separated from Extracts (replies)
2. **Optional Request inclusion**: Extracts may include a Request copy indicating actual contents (potentially differing from requested)

**Design benefit**: Common Request/Extract semantics are modelled generically, with specialised types based on common classes. Different Extract types address particular requirement groups rather than creating one multi-purpose Extract type.

**Communication scenarios** include various Extract types:

- **EHR Extract**: openEHR system EHR content
- **Generic Extract**: Non-openEHR systems and ISO 13606 users; assumes minimum system knowledge
- **Synchronisation Extract**: Mirrored EHR updating via Contributions

**Future possibilities**: Other Extract types may be defined later.

**Time control patterns**:
- Single request, single reply (simplest)
- Request persistence with 'action' requests for differing Extract content
- Repeat requests per specified period
- Requests with trigger events for automatic replies

### Content Model & Representation

Any extraction environment may require three data categories:

1. Key clinical/administrative information (EHR content like patient vital signs)
2. Demographic information (patient and professional identities)
3. Relevant meta-data

These typically reside in different system parts but must combine in Extracts. The model flexibly aggregates content in Extracts using:

- Generic Extract containment structure
- Specific archetyped content plug-in
- Whole structure templating (each template = one Extract type/message type)

**Implementation approaches**:

1. **Standard schema**: Templates generate content per published schema; all Extract messages conform to standard schema; XML is "standard generic openEHR XML"

2. **Custom schema**: Templates convert to custom schemas; different templates (discharge summaries, referrals) define distinct schemas; XML is schema-specific

**Selection factors**: Environment requirements, artefact stability, and other considerations determine approach choice.

### Package Structure

The `rm.extract` package defines Extracts from openEHR data sources including EHRs.

**Sub-packages**:

- **common**: All Extract types' common semantics
- **ehr_extract**: EHR Extract type semantics
- **generic_extract**: Generic Extract type semantics
- **synchronisation_extract**: Synchronisation Extract type semantics
- **message**: Simple message model containing an Extract

---

## Extract.common Package

### Overview

The `rm.extract.common` package defines semantics common to all Extract requests and types. Requests and Extracts implement as messages or webservice types (with Extract request semantics replaced by equivalent service functions).

**Components**:

- **Request**: Detailed repository content specification
- **Optional inclusion**: Requests aren't always needed; Extracts may be unsolicited
- **Persistence options**: Requests can be persistent and/or event-driven, supporting periodic and continuous update scenarios
- **Multi-entity scope**: Each request specifies data from one or more entities (EHRs, subjects)

**Extract response**:

- **Request copy**: Optional request inclusion
- **Main content**: Chapters containing retrieved content (or as much as retrievable)
- **Specific content types**: openEHR content, generic EMR content, demographic content defined in sub-packages
- **Chapter arrangement**: Archetypes and templates manage chapter/folder content layout

### Design

#### Extract Request

EXTRACT_REQUEST consists of:

1. **update_spec**: Update rules (one-off, periodic, event-driven, etc.)
2. **extract_spec**: Target repository information requirements including:
   - Optional version_spec: Version inclusion specifications
   - manifest: Entity specification (records/subjects, optionally item selections)

##### Content Criteria Specification

The extract_spec part applies to all Extract content with attributes:

- **extract_type**: Extract kind (e.g., |openehr-ehr|, |openehr-demographic|, |openehr-synchronisation|, |openehr-generic|, |generic-emr|)
- **include_multimedia**: Inline binary object inclusion flag
- **link_depth**: Link-following depth (default 0 = don't follow)
- **criteria**: Query content specifications
- **other_details**: Archetypable additional extract details

**Criteria attribute** defines required content retrieval per entity via generic queries (sensible for any record) as DV_PARSABLE instances, enabling any formalism (e.g., Archetype Query Language).

**Query examples**:

```
SELECT * FROM $ehr              -- all record items
SELECT /ehr_access FROM $ehr    -- EHR_ACCESS object
SELECT /ehr_status FROM $ehr    -- EHR_STATUS object
SELECT ...                      -- last 6 months blood glucose
...                             -- ongoing medications list
......                          -- active pregnancy items
.....                           -- GP encounter notes since 12-03-2005
```

##### Update Specification

The update_spec specifies server Request processing. Default (no update_spec) is one-off request. Other alternatives:

- Repeat Request with defined period and/or trigger events
- Server-persisted Request for later reference-based repeat requests

Ad hoc persisted request repetition uses EXTRACT_ACTION_REQUEST with action |repeat|, specifying only previously stored request identifier. Since requests are uniquely identified eternally, identification cannot error.

##### The Manifest

The manifest specifies record retrieval scope. Simplest case (majority scenario): single entity, no specific items (criteria determine content).

**Batch update scenarios** (pathology lab results, referral-matched records):
- Request manifest may identify multiple entities
- Each receives separate chapter in resulting Extract

**item_list attribute**: Individual items identified via OBJECT_REF instances containing HIER_OBJECT_ID identifiers for top-level objects (Compositions, Parties). This mechanism is used when specific identifiers are known rather than filter-criteria items.

##### Version Specification

Simplest Extract requests lack version specification (assuming latest available version). Version specification allows:

- **include_all_versions**: Whole version "stack" of each matched item returned (all available repository versions, not necessarily all ever created—local modifications not propagated elsewhere may exist)

- **include_revision_history**: Indicates whether VERSIONED_OBJECT revision_history inclusion

#### Extract

##### Content Specification

EXTRACT consists of:

- **request_id**: Causing request reference (if any)
- **participations**: Extract-creating party list
- **specification**: Actual Extract contents (EXTRACT_SPEC form)
- **chapters**: Retrieved content chapters

**Difference**: specification usually differs from request specification—manifest lists actual retrieved entities and identifiers at receiver systems, whereas request may specify different entities or rely on query criteria.

##### Content

Extract content is within chapters attribute as EXTRACT_CHAPTER or EXTRACT_ENTITY_CHAPTER instances. Within chapters, content attribute contains folder structures (EXTRACT_FOLDER objects) containing content items.

**Folder structures**: Archetypes define folder structure, separating record parts or grouping by other schemes (episodes).

**EXTRACT_ENTITY_CHAPTER**: Carries single-entity content, enabling multi-entity (multi-patient) Extracts via separate chapters.

**EXTRACT_CONTENT_ITEM**: Subtyped in later sections for specific content metadata.

#### Participations and Demographic Referencing

Extracts combine typically distributed system information—clinical and demographic data regarding participation in documented activities.

**openEHR EHR model**: PARTICIPATION class (rm.common.generic package) with performer (PARTY_PROXY subtype) and optional external reference (PARTY_REF).

**Extract participations occur in two places**:

1. **EHR_EXTRACT participations**: Extract creation parties (new with each Extract). Uses simplified PARTICIPATION form (EXTRACT_PARTICIPATION) with simple string performer reference (GUID to demographics elsewhere in Extract).

2. **EHR content participations**: Original structures copied faithfully, including inline performer information. If external_ref pointed to included demographic entities, references rewrite to local GUID values within Entity chapter.

**Result**: For source data with external demographic references, logical structure preservation occurs within Extracts, with only reference rewriting to GUIDs (possibly from original demographic database/service).

**Typical arrangement**: Single chapter dedicated to all referenced demographic entities, optionally with internal Folder structure.

### Class Descriptions

#### EXTRACT_REQUEST Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| **extract_spec** | EXTRACT_SPEC | Specification details of the request |
| **update_spec** | EXTRACT_UPDATE_SPEC (0..1) | Update details of the request |
| **uid** (redefined) | HIER_OBJECT_ID | Request identifier, generated by requestor |

**Inheritance**: LOCATABLE

#### EXTRACT_ACTION_REQUEST Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| **request_id** | OBJECT_REF | Previous EXTRACT_REQUEST identifier |
| **action** | DV_CODED_TEXT | Requested action: cancel \| resend \| send new. Coded by openEHR Terminology group 'extract action type' |
| **uid** (redefined) | HIER_OBJECT_ID | Request identifier |

**Inheritance**: LOCATABLE

#### EXTRACT_SPEC Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| **version_spec** | EXTRACT_VERSION_SPEC (0..1) | Version inclusion specification. Default: latest versions only |
| **manifest** | EXTRACT_MANIFEST | Entity specification for extraction |
| **extract_type** | DV_CODED_TEXT | Content requirement type: \|openehr-ehr\|, \|openehr-demographic\|, \|generic-emr\|, \|other\|. Coded by openEHR Terminology group 'extract content type' |
| **include_multimedia** | Boolean | Inline DV_MULTIMEDIA instance inclusion flag |
| **priority** | Integer | Requested server handling priority. Likely local, agreed by both ends. TBD: alternative is standard coded terms |
| **link_depth** | Integer | Link-following degree from included content items: 0=don't follow; 1=first degree; 2=second degree; n=nth degree. EXTRACT_CONTENT_ITEM.is_primary differentiates included items |
| **criteria** | List<DV_PARSABLE> (0..1) | Extract content queries |
| **other_details** | ITEM_STRUCTURE (0..1) | Other archetypable specification items |

#### EXTRACT_MANIFEST Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| **entities** | List<EXTRACT_ENTITY_MANIFEST> | Entity manifest list; for openEHR, these are version container UIDs |

#### EXTRACT_ENTITY_MANIFEST Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| **extract_id_key** | String | Entity identifier in Extract. May be another identifier or something else (simple integer) |
| **ehr_id** | String (0..1) | EHR/EMR target system identifier |
| **subject_id** | String (0..1) | Subject (patient/similar) target system identifier |
| **other_ids** | List<String> (0..1) | Other target system identifiers (keyed by type): medicare numbers, drivers license, tax number, etc. |
| **item_list** | List<OBJECT_REF> (0..1) | Item UIDs for individual-item Extract inclusion. For openEHR, these are version container UIDs |

#### EXTRACT_VERSION_SPEC Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| **include_all_versions** | Boolean | Include all item versions |
| **commit_time_interval** | DV_INTERVAL<DV_DATE_TIME> (0..1) | Source repository commitment time interval. Limits included versions to interval range; if include_all_versions true, includes all interval-committed versions |
| **include_revision_history** | Boolean | Include item revision histories (always full if included) |
| **include_data** | Boolean | Include matched content item data. Default true. False includes only revision history in serialised versions. In openEHR, causes X_VERSIONED_OBJECTs to have revision_history set but versions Void. Useful for server interrogation without content examination |

**Invariant**: `not include_data implies include_revision_history`

#### EXTRACT_UPDATE_SPEC Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| **persist_in_server** | Boolean | Persist Request in server until revoked |
| **repeat_period** | DV_DURATION (0..1) | Update Extract resend period |
| **trigger_events** | List<DV_CODED_TEXT> (0..1) | Event names causing update Extract sending: \|any_change\| (matched content changes), \|correction\| (error corrections only), \|update\| (matched item updates). Coded by openEHR Terminology group 'extract update trigger event type' |
| **update_method** | CODE_PHRASE | Update mode: send changed/new items since last send, or send all. For persist_in_server Requests only |

**Invariants**:
- `repeat_period /= Void or trigger_events /= Void`
- `trigger_events /= Void implies not trigger_events.is_empty`
- `send_changes_only implies persist_in_server`

#### EXTRACT Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| **chapters** | List<EXTRACT_CHAPTER> (0..1) | Extracted content serialised from source repository |
| **specification** | EXTRACT_SPEC (0..1) | Extract actual conformance specification (possibly differing from request) |
| **request_id** | HIER_OBJECT_ID (0..1) | Causing Request reference (if any) |
| **time_created** | DV_DATE_TIME | Extract creation time |
| **system_id** | HIER_OBJECT_ID | Creating system identifier |
| **sequence_nr** | Integer | Response sequence number in matching requests. Value 1 if sole response or no request |
| **participations** | List<EXTRACT_PARTICIPATION> (0..1) | Extract-creation relevant participations |

**Inheritance**: LOCATABLE

**Invariant**: `sequence_nr >= 1`

#### EXTRACT_CHAPTER Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| **items** | List<EXTRACT_ITEM> (0..1) | Chapter information content |

**Inheritance**: LOCATABLE

#### EXTRACT_ENTITY_CHAPTER Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| **extract_id_key** | String | Related demographic entity reference (e.g., patient) |

**Inheritance**: EXTRACT_CHAPTER

#### EXTRACT_ITEM Class (Abstract)

**Description**: Extract Folder and Content types abstract parent

**Inheritance**: LOCATABLE

#### EXTRACT_FOLDER Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| **items** | List<EXTRACT_ITEM> (0..1) | Folder items (Folders and content items) |

**Inheritance**: EXTRACT_ITEM

**Note**: Empty Folders are allowed

#### EXTRACT_CONTENT_ITEM Class (Abstract)

| Attribute | Type | Meaning |
|-----------|------|---------|
| **is_primary** | Boolean | Content item was primary set part (not link-following-added) |
| **is_changed** | Boolean (0..1) | Content item is any change since last send in repeat scenarios |
| **is_masked** | Boolean (0..1) | Content exclusion due to insufficient requestor access rights |
| **item** | Any (0..1) | Content object |

**Inheritance**: EXTRACT_ITEM

**Invariant**: `is_masked xor item /= Void`

#### EXTRACT_PARTICIPATION Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| **time** | DV_INTERVAL<DV_DATE_TIME> (0..1) | Participation time interval (observational contexts) or intended interval (future contexts like Instructions) |
| **function** | DV_TEXT | Party participation function (note: parties may participate multiple ways). Should be coded but cannot be limited to HL7v3:ParticipationFunction |
| **mode** | DV_CODED_TEXT (0..1) | Performer/activity interaction mode (present, telephone, email, etc.) |
| **performer** | String | Extract-internal demographic entity UID performing participation |

**Invariants**:
- `function /= Void and then function.generating_type.is_equal ("DV_CODED_TEXT") implies terminology (Terminology_id_openehr).has_code_for_group_id (Group_id_participation_function, function.defining_code)`
- `mode /= Void and terminology (Terminology_id_openehr).has_code_for_group_id (Group_id_participation_mode, mode.defining_code)`

---

## The openehr_extract Package

### Overview

The `rm.extract.openehr_extract` package defines an openEHR-specific EXTRACT_ITEM variant consisting of VERSIONED_OBJECT class form (rm.common.change_control package) suitable for Extracts. The Extract form (X_VERSIONED_OBJECT<T>) replicates functional VERSIONED_OBJECT values as attributes. Binding to non-generic types for openEHR EHR top-level objects (Composition, Directory, etc.) creates further subtypes.

### Design

#### openEHR Extract Item

openEHR system items in EHR Extracts are always top-level objects (Composition, Directory, PARTY, etc., and descendants) expressed as X_VERSIONED_OBJECT<T> descendants. This type provides standard interoperable serialisation for all or partial VERSIONED_OBJECTs for lossless transmission between systems despite implementation differences.

**Approach**: X_VERSIONED_OBJECT turns VERSIONED_OBJECT functional properties into data attributes.

**Key attributes**:

- **revision_history**: Optional complete original VERSIONED_OBJECT revision history
- **versions**: Any or all original versions

**Revision history retrieval**: Requestable alone via version specification include_data flag set to False.

**Typical scenarios**: Most include versions, exclude revision_history. X_VERSIONED_OBJECT.versions items wrap ORIGINAL_VERSION copies from source system VERSIONED_OBJECTs.

#### EHR Extract Structure

openEHR EHR overall structure per subject replicates via archetyped Folder structures creating directory, compositions, ehr_access, and ehr_status groupings from openEHR EHRs.

#### Demographic Referencing

EHR Extract content preserves PARTICIPATION and PARTY_PROXY structures (PARTY_SELF and PARTY_IDENTIFIED descendants) for fidelity. However, final pointers (OBJECT_ID.value) may rewrite to correctly refer to Extract-included demographics.

### Class Descriptions

#### OPENEHR_CONTENT_ITEM Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| **item** (0..1, redefined) | X_VERSIONED_OBJECT | Content object |

**Inheritance**: EXTRACT_CONTENT_ITEM

**Description**: openEHR serialised VERSIONED_OBJECTs containing EHR EXTRACT_ITEM form

#### X_VERSIONED_OBJECT Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| **uid** | HIER_OBJECT_ID | Original VERSIONED_OBJECT UID |
| **owner_id** | OBJECT_REF | Original VERSIONED_OBJECT owner_id (source EHR identifier) |
| **time_created** | DV_DATE_TIME | Original VERSIONED_OBJECT creation time |
| **total_version_count** | Integer | Original VERSIONED_OBJECT total version count at X_VERSIONED_OBJECT creation |
| **extract_version_count** | Integer | This Extract's versions count (versions attribute items count). May be 0 if only revision history requested |
| **revision_history** | REVISION_HISTORY (0..1) | Optional original VERSIONED_OBJECT complete revision history |
| **versions** | List<ORIGINAL_VERSION> (0..1) | 0+ original VERSIONED_OBJECT Versions per Extract specification |

**Description**: shareable data-oriented VERSIONED_OBJECT<T> Extract variant

#### X_VERSIONED_EHR_ACCESS Class

**Inheritance**: X_VERSIONED_OBJECT

**Description**: EHR_ACCESS EHR object X_VERSIONED_OBJECT form

#### X_VERSIONED_EHR_STATUS Class

**Inheritance**: X_VERSIONED_OBJECT

**Description**: EHR_STATUS EHR object X_VERSIONED_OBJECT form

#### X_VERSIONED_COMPOSITION Class

**Inheritance**: X_VERSIONED_OBJECT

**Description**: COMPOSITION EHR object X_VERSIONED_OBJECT form

#### X_VERSIONED_FOLDER Class

**Inheritance**: X_VERSIONED_OBJECT

**Description**: FOLDER EHR object X_VERSIONED_OBJECT form

#### X_VERSIONED_PARTY Class

**Inheritance**: X_VERSIONED_OBJECT

**Description**: PARTY demographic object X_VERSIONED_OBJECT form

---

## Generic_extract Package

### Overview

The `rm.extract.generic_extract` package defines Extract types for non-openEHR systems (including EHR/EMR systems) sending data to other systems using archetype and template-defined openEHR structures. Such systems typically lack standardised native data and variable versioning support.

### Design

#### Structure

The GENERIC_CONTENT_ITEM subtype of EXTRACT_CONTENT_ITEM defines meta-data that typical legacy systems can populate partially, along with IHE/XDS repository document sources.

**Meta-data groups**:

1. **Document type/status information**:
   - **item_type**: Coded term indicating content 'model' or schema (published standard, archetype, template, etc.)
   - **item_type_version**: item_type model version

2. **Original information creation details** (same as 'committal' in some systems, or assembled for Extract purposes):
   - **author**: Original content author identity (demographic UID reference in Extract)
   - **creation_time**: Content creation date/time
   - **authoriser**: Professional authorising content (demographic UID reference in Extract), if relevant
   - **authorisation_time**: Content authorisation date/time
   - **item_status**: Lifecycle status coded term
   - **version_id**: Original system version instance
   - **version_set_id**: 'version set' identifier (version group identity)
   - **system_id**: Content creation/commitment/extraction system
   - **other_details**: Other meta-data (keyed String list)

**Characteristic**: All optional, reflecting varying availability across source systems. Archetypes/templates may mandate specific items.

**Content attribute** (item): Any openEHR LOCATABLE structure (COMPOSITION, ENTRY variants including GENERIC_ENTRY, ITEM_TREE, CLUSTER, etc.), transformed from original system data.

##### Demographic Referencing

Generic Extract content (openEHR COMPOSITIONs) expresses participations via PARTICIPATION instances. This is somewhat inefficient for on-the-fly construction from non-openEHR data; more flexible participation reference mechanisms may be required future.

### Class Descriptions

#### GENERIC_CONTENT_ITEM Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| **item_type** | DV_CODED_TEXT (0..1) | Content 'model' or schema identifier |
| **item_type_version** | String (0..1) | Content creation model/schema version |
| **author** | String (0..1) | Original content author demographic UID (Extract reference) |
| **creation_time** | Iso8601_date_time (0..1) | Original system content creation time (may be earlier commit or Extract-generation time) |
| **authoriser** | String (0..1) | Original system content authoriser demographic UID (Extract reference), if relevant |
| **authorisation_time** | Iso8601_date_time (0..1) | Original system content authorisation time, if relevant |
| **item_status** | DV_CODED_TEXT (0..1) | Item lifecycle status coded term |
| **version_id** | String (0..1) | Original system item version identifier |
| **version_set_id** | String (0..1) | Original system item version set identifier |
| **system_id** | String (0..1) | Item creation/commitment/extraction system identifier (typically domain name) |
| **other_details** | Hash<String, String> (0..1) | Other content item meta-data |
| **item** (0..1, redefined) | LOCATABLE | Content object |

**Inheritance**: EXTRACT_CONTENT_ITEM

**Description**: Non-openEHR system (13606, CDA) data single item in generic extract

---

## Synchronisation Extracts

### Overview

Extract variant for openEHR system synchronisation. Specification allows Contribution lists or Contributions since specified Contribution; actual versions may be included or excluded. Excluding versions retrieves just Contributions—determine other system holdings.

### Class Descriptions

#### SYNC_EXTRACT_REQUEST Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| **specification** | SYNC_EXTRACT_SPEC | Synchronisation request specification |

**Inheritance**: MESSAGE_CONTENT

**Description**: Synchronisation Contribution openEHR server exchange request type

#### SYNC_EXTRACT Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| **specification** | SYNC_EXTRACT_SPEC | This Extract actual specification |
| **items** | List<X_CONTRIBUTION> (0..1) | Serialised Contributions content |

**Inheritance**: MESSAGE_CONTENT

#### SYNC_EXTRACT_SPEC Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| **includes_versions** | Boolean | Contribution Versions inclusion; False retrieves just Contribution and Audit |
| **contribution_list** | List<HIER_OBJECT_ID> (0..1) | Contribution inclusion list |
| **contributions_since** | DV_DATE_TIME (0..1) | Threshold date for Contribution specification |
| **all_contributions** | Boolean (0..1) | Include all record Contributions |

**Description**: Extract specification (request specification or response content description)

#### X_CONTRIBUTION Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| **uid** | HIER_OBJECT_ID | Source system Contribution UID |
| **audit** | AUDIT_DETAILS | Source system Contribution Audit |
| **versions** | List<VERSION> (0..1) | Source system Contribution serialised Versions |

**Description**: Extract serialised Contribution form

---

## The Message Package

### Requirements

In first two EHR extract scenarios (Requirements section), Extracts may arrive as request responses or unsolicited. Most care transfers (discharge summaries, referrals) and pathology test results generate unsolicited Extracts, whereas solicited requests typically occur when patients present elsewhere without explicit care transfer.

### Design

The message package provides point-to-point message sending/receiving basic abstractions with abstract payload type MESSAGE.

**Characteristic**: Each transmission requires new message, even if payload was created once and retransmitted multiple times.

#### Integrity and Security

The MESSAGE object may include digital hash (digest/fingerprint) of serialised content (SHA-1, MD5 algorithms) for integrity checking—protecting non-malicious data changes (software bugs, incorrect transaction management).

**Acceptable in**: Secure closed environments (private hospitals, community health networks).

**Malicious modification protection**: Encryption.

### Class Descriptions

#### ADDRESSED_MESSAGE Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| **sender** | String | Message-sending party |
| **sender_reference** | String | Sender identification of message. Remains same no matter send count to recipients |
| **addressees** | List<String> | Intended recipients (internet addresses) |

**Description**: Party-addressed message concept

---

## Semantics of openEHR and ISO 13606 Extracts

### Versioning Semantics

### Creation Semantics

---

## Amendment Record

| Issue | Details | Raiser | Completed |
|-------|---------|--------|-----------|
| RM Release 1.1.0 | See release notes | — | — |
| RM Release 1.0.4 | 2.1.2: SPECPUB-3 Re-instate X_VERSIONED_OBJECT<T> descendants inheritance to X_VERSIONED_OBJECT from Release 1.0.2 | T Beale | 25 May 2016 |
| RM Release 1.0.3 | 2.1.1: SPECRM-30 Correct EHR_EXTRACT documentation errors (remove generic parameter text) | R Chen, H Frankel, T Beale | 10 Oct 2015 |
| — | SPECRM-24 EHR Extract IM typographical errors correct | P Gummer, T Beale | — |
| — | SPECRM-13 Convert fields to coded: EXTRACT_SPEC.type, EXTRACT_ACTION_REQUEST.action, EXTRACT_UPDATE_SPEC.trigger_events | H Frankel, T Beale | — |
| RM Release 1.0.3 | 2.1: SPECRM-14 EHR Extract improvements: Remove EXTRACT_SPEC includes_directory, directory_archetype; remove EXTRACT_ENTITY_CONTENT; main EXTRACT_FOLDER containment; move X_VERSIONED_OBJECT to openEHR_extract; change EXTRACT.request_id to HIER_OBJECT_ID; change GENERIC_EXTRACT_ITEM.other_details to Hash<String, String> | H Frankel, T Beale | 29 Jun 2011 |
| — | SPECRM-6 Correct EXTRACT_CHAPTER single Entity modelling inconsistency | T Beale | — |
| Release 1.0.1 | 2.0: SPEC-189 Add LOCATABLE.parent. New EHR_EXTRACT invariant | T Beale | 20 Feb 2007 |
| — | SPECRM-10 Upgrade EHR_EXTRACT to Release-1.0. Major redevelopment: Add X_VERSIONED_OBJECT, X_VERSIONED_FOLDER, X_VERSIONED_COMPOSITION, X_VERSIONED_EHR_ACCESS, X_VERSIONED_EHR_STATUS, X_VERSIONED_PARTY | T Beale | — |
| — | SPEC-219 Use constants instead of literals for terminology RM references | R Chen | — |
| Release 0.95 | 1.3.5: SPEC-118 Make package names lower case | T Beale | 10 Dec 2004 |
| Release 0.9 | 1.3.4: SPEC-41 Visually differentiate primitive types in openEHR documents | D Lloyd | 04 Oct 2003 |
| — | 1.3.3: SPEC-13 Change key class names per CEN ENV 13606 | S Heard, D Kalra, D Lloyd, T Beale | 15 Sep 2003 |
| — | 1.3.2: SPEC-3, SPEC-4 (versioning, LOCATABLE changes). MESSAGE_CONTENT inherits LOCATABLE | T Beale, Z Tun | 18 Mar 2003 |
| — | 1.3.1: Formally validated Eiffel 5.2; revised MESSAGE structure per CEN 13606-4; EXTRACT.hca_authorising renamed originator | T Beale | 26 Feb 2003 |
| — | 1.3: Post-CEN Rome Feb 2003 changes. Added X_TRANSACTION attestations. Documentation improvements | T Beale, S Heard, D Kalra, D Lloyd | 07 Feb 2003 |
| — | 1.2.2: Minor diagram and class definition corrections | Z Tun | 08 Jan 2003 |
| — | 1.2.1: Added senders_reference (CEN 13606-4:2000 section 7.4 conformance) | T Beale | 04 Jan 2003 |
| — | 1.2: Rewritten and restructured as two packages | T Beale | 07 Nov 2002 |
| — | 1.1: EXTRACT part moved to MESSAGE; allow multilevel archetypable Folder structures | T Beale, D Kalra, D Lloyd | 07 Oct 2002 |
| — | 1.0: Taken from EHR RM | T Beale | 07 Oct 2002 |

---

## Acknowledgements

Funding contributors:
- University College London - Centre for Health Informatics and Multi-professional Education (CHIME)
- Ocean Informatics

Special recognition: David Ingram, Emeritus Professor of Health Informatics at UCL, for vision and collegial environment since GEHR days (1992).

---

**Document Version**: Release-1.1.0
**Document Type**: Information Model Specification
**Format**: openEHR Standard Documentation

**Source URL**: https://specifications.openehr.org/releases/RM/latest/ehr_extract.html

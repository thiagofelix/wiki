# EHR Information Model

**Issuer**: openEHR Specification Program
**Release**: RM Release-1.1.0
**Status**: STABLE
**Source**: https://specifications.openehr.org/releases/RM/latest/ehr.html
**Licence**: Creative Commons Attribution-NoDerivs 3.0 Unported

---

## Table of Contents

1. Preface
2. Background
3. The EHR Information Model
4. EHR Package
5. Composition Package
6. Content Package
7. Navigation Package
8. Entry Package

---

## 1. Preface

### 1.1 Purpose

This document describes the openEHR EHR Information Model, defining a logical EHR information architecture in the ISO RM/ODP information viewpoint. It establishes an interoperable EHR model rather than just architecture for communication of EHR extracts or documents.

### 1.2 Related Documents

**Prerequisite documents**:
- openEHR Architecture Overview

**Related documents**:
- openEHR Support Information Model
- openEHR Data Types Information Model
- openEHR Data Structures Information Model
- openEHR Common Information Model

---

## 2. Background

### 2.1 Requirements

#### 2.1.1 Original GEHR Requirements (1992-1995)

From the European GEHR project:
- Life-long EHR
- Priority: Clinician/Patient interaction
- Medico-legal faithfulness, traceability, audit-trailing
- Technology & data format independence
- Facilitate sharing of EHRs
- Suitable for primary and acute care
- Secondary uses: education, research, population medicine

#### 2.1.2 GEHR Australia Requirements (1997-2001)

- Support for clinical data structures: lists, tables, time-series
- Safer information model with context attributes only in valid places
- Separation of "persistent," "demographic," and "event" information
- Formally specified archetypes and archetype-enabled information model
- Interoperability at knowledge level (domain definitions)
- XML-enabled architecture
- Compatibility with ISO 13606, OMG Corbamed, HL7v3

### 2.2 Relationship to Other Health Information Models

#### 2.2.1 ISO 13606

openEHR models influenced by and influenced ISO 13606 (2005 revision). Key changes:
- Class name changes (TRANSACTION -> COMPOSITION)
- Improved ATTESTATION model
- Improved feeder audit model

openEHR differs as its scope includes systems while ISO 13606 defines EHR Extract.

#### 2.2.2 HL7 Version 3

Correspondences documented where possible. However, differences exist:
- HL7v3 RIM not intended as EHR model
- HL7v3 RIM is amalgam of semantics from multiple systems
- HL7v3 RIM uses "analysis patterns" requiring custom refinement
- Data in messages not direct instances of HL7v3 RIM classes

---

## 3. The EHR Information Model

### 3.1 Overview

The openEHR EHR information model consists of packages structured as follows:

**Package Structure**:

- **ehr**: Contains top-level EHR structure with EHR_ACCESS object, EHR_STATUS object, versioned data containers (VERSIONED_COMPOSITION), and optional hierarchical FOLDER structures. Includes CONTRIBUTION collection documenting changes.

- **composition**: COMPOSITION class as primary "data container," the EHR's root data point. Key attributes: `_content_`, `_context_`, `_composer_`.

- **content**: Contains Navigation and Entry packages describing structure and semantics of Composition contents:
  - **navigation**: SECTION class provides navigational structure similar to paper record headings.
  - **entry**: Generic structures for recording clinical statements. Entry types include ADMIN_ENTRY, OBSERVATION, EVALUATION, INSTRUCTION, ACTION.

---

## 4. EHR Package

### 4.1 Overview

The openEHR EHR follows a relatively simple structure. A central EHR object identified by EHR id specifies references to:
- Structured, versioned information
- List of Contribution objects acting as audits of change-sets

**High-level EHR structure**:

- **EHR**: Root object, identified by globally unique EHR identifier
- **EHR_access (versioned)**: Contains access control settings for record
- **EHR_status (versioned)**: Contains status and control information, optionally including subject identifier
- **Folders (versioned)**: Optional hierarchical folder structures logically indexing Compositions
- **Compositions (versioned)**: Containers of all clinical and administrative content
- **Contributions**: Change-set records for every change made; reference set of Versions committed or attested together

### 4.2 The Parts of the EHR

#### 4.2.1 Root EHR Object

Records three immutable pieces of information:
- System identifier where EHR was created
- EHR identifier (distinct from subject identifier)
- Time of EHR creation

**_system_id_** records identifier of logical EHR repository to which audit data is committed.

**References vs. Containment**: Uses references rather than containment by value, reflecting majority of retrieval scenarios needing only selected recent items.

#### 4.2.2 EHR Access

Access control settings for entire EHR specified in EHR_ACCESS object. Includes:
- Default privacy policy
- Lists of identified accessors (individuals and groups)
- Exceptions to default policies
- References to particular Compositions

Two hard-wired attributes:
- Name of security scheme in use
- Settings object containing access settings according to that scheme

#### 4.2.3 EHR Status

EHR_STATUS object contains small number of hard-wired attributes and archetyped `_other_details_` part.

**Hard-wired attributes**:
- Identify subject of record (current understanding)
- Whether EHR is actively in use, inactive, or queryable

Subject represented by PARTY_SELF object, enabling anonymous records or patient identifier inclusion.

#### 4.2.4 Compositions

Main EHR data found in Compositions (instances of COMPOSITION class).

**Definition**: Unit of information resulting from interaction of healthcare agent (subject or healthcare professional) with EHR.

**Design satisfies ACID-inspired requirements**:
- **Durability**: Persistent unit of information committal
- **Atomicity**: Minimal unit of integrity for clinical information
- **Consistency**: Contributions leave record in consistent state
- **Isolation**: Simultaneous user contributions don't interfere
- **Indelibility**: Information committed is indelible for later investigations
- **Modification**: Users can modify EHR contents (error correction, information updates)
- **Traceability**: Adequate auditing information at committal

**Temporal classification**: Compositions temporally classified using categories in `COMPOSITION._category_` attribute. Categories include event, episodic, and persistent.

##### 4.2.4.1 Persistent Compositions

Records items summarizing key aspects of patient state, ongoing relevance in record.

**Well-known categories**:
- Problem list
- Current medications
- Therapeutic precautions (allergies, interactions)
- Vaccination history
- Patient preferences
- Lifestyle
- Family history
- Social situation
- Care plan

**Characteristics**:
- Proxies for patient state maintained as single source-of-truth over patient lifetime
- Changes applied to same logical composition instance as new versions
- Small total number per patient

##### 4.2.4.2 Event Compositions

Records what happens during healthcare system activities performed with/for patient.

**Examples**:
- Observations, assessments, orders, actions during patient contact
- Actions during activities without patient participation (e.g., surgery)
- Actions during activities without patient presence (e.g., pathology testing)

##### 4.2.4.3 Episodic Compositions

Classified as _episodic_ if containing information relevant to ongoing care situation spanning significant time (pregnancy/birth, major surgery/recovery, etc.).

- Treated as persistent-like (updated as single instance source-of-truth)
- Maintained only for defined period/set of conditions (not entire patient life)

#### 4.2.5 Folders

As Compositions accumulate, `_folders_` structures can index Compositions using one or more versioned hierarchies of FOLDER objects.

**Key structural principle**: Folder structures do _not contain_ Compositions, only _references_ to them. Multiple Folders can therefore reference same Composition.

**_folders_ and _directory_**: If `_folders_` not void, `_directory_` attribute contains reference to first member (backward compatibility with pre-Release 1.1.0).

### 4.3 Change Control in the EHR

**General requirements** (always met):
- Record always in consistent informational state
- All changes audit-trailed
- All previous record states available for medico-legal investigation

Satisfied via change control and versioning facilities in Common Information Model. Key facet: change-sets known as Contributions.

#### 4.3.1 Versioning of Compositions

Achieved with `VERSIONED_OBJECT<T>` from Common IM `change_control` package.

Explicitly bound to COMPOSITION via `VERSIONED_COMPOSITION` inheriting from `VERSIONED<COMPOSITION>`.

**VERSIONED_COMPOSITION concept**: "Smart repository" -- successive version storage is implementation concern, but functional interface enables any version retrieval.

#### 4.3.2 Versioning Scenarios

**Case 0**: Information authored locally, creating new `ORIGINAL_VERSION<COMPOSITION>`.
**Case 1**: Information modified locally (error correction). Creates new `ORIGINAL_VERSION<COMPOSITION>` with `AUDIT_DETAILS._change_type_` set to "correction".
**Case 2**: Information from feeder system (test result), converted creating new `IMPORTED_VERSION<COMPOSITION>` and `ORIGINAL_VERSION<COMPOSITION>` pair.
**Case 3**: `ORIGINAL_VERSION<COMPOSITION>` received in EHR_EXTRACT from another openEHR system.

### 4.4 EHR Creation Semantics

#### 4.4.1 EHR Identifier Allocation

**Type 1 - New patient**: EHR created without reference to other openEHR EHRs. Allocated new globally unique EHR id.
**Type 2 - Logical clone creation**: openEHR EHR created as logical clone of patient's EHR in other system.

**Strongly recommended**: Use UUID for `_ehr_id_` field.

#### 4.4.2 EHR Creation

At creation, result should be:
- Root EHR object
- EHR Status object
- EHR Access object
- Other house-keeping information

### 4.5 EHR Active Status

`EHR_STATUS._is_modifiable_` indicates whether _EHR contents_ are modifiable. Set to `True` if EHR _active_.

**Deactivation circumstances**:
- Patient death
- Duplicate or additional record discovery
- Patient formal opt-out
- EHR movement to another system

### 4.6 Time in the EHR

Numerous recorded times at varying granularities:
- Sample/collection time
- Measurement time
- Healthcare business event time
- Data committal time

### 4.7 Historical Views of the Record

COMPOSITION versions at previous time represent previously available _informational state_ of EHR. Previous states include only Compositions from other sources acquired by that time.

**Important differentiation**:
- **Previous informational state**: What system users could see at particular moment
- **Previous clinical state**: Derivable view of EHRs at all patient locations

### 4.8 Class Descriptions

#### 4.8.1 EHR Class

**Description**: Root object and access point of EHR for care subject.

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | system_id | HIER_OBJECT_ID | EHR management system identifier where created |
| 1..1 | ehr_id | HIER_OBJECT_ID | Unique EHR identifier (strongly recommend UUID) |
| 0..1 | contributions | List<OBJECT_REF> | Contribution list causing changes |
| 1..1 | ehr_status | OBJECT_REF | EHR_STATUS object reference |
| 1..1 | ehr_access | OBJECT_REF | EHR_ACCESS object reference |
| 0..1 | compositions | List<OBJECT_REF> | Master Versioned Composition references |
| 0..1 | directory | OBJECT_REF | Optional directory structure; first `_folders_` member if present |
| 1..1 | time_created | DV_DATE_TIME | EHR creation time |
| 0..1 | folders | List<OBJECT_REF> | Optional additional Folder structures |

**Invariants**:
- `Contributions_valid`: All contributions type equal "CONTRIBUTION"
- `Ehr_access_valid`: ehr_access type equals "VERSIONED_EHR_ACCESS"
- `Ehr_status_valid`: ehr_status type equals "VERSIONED_EHR_STATUS"
- `Compositions_valid`: All compositions type equal "VERSIONED_COMPOSITION"
- `Directory_valid`: If directory not void, type equals "VERSIONED_FOLDER"
- `Folders_valid`: If folders not void, all type equal "VERSIONED_FOLDER"
- `Directory_in_folders`: If folders not void, first folders item equals directory

#### 4.8.2 VERSIONED_EHR_ACCESS Class

**Description**: EHR_ACCESS instance version container.
**Inheritance**: VERSIONED_OBJECT

#### 4.8.3 EHR_ACCESS Class

**Description**: EHR-wide access control object. All access decisions must follow policies and rules.
**Inheritance**: LOCATABLE

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 0..1 | settings | ACCESS_CONTROL_SETTINGS | Access control settings |

**Functions**:

| Returns | Name | Meaning |
|---|---|---|
| String | scheme() | Access control scheme name |

**Invariants**:
- `Scheme_valid`: scheme not empty
- `Is_archetype_root`: is_archetype_root true

#### 4.8.4 VERSIONED_EHR_STATUS Class

**Description**: EHR_STATUS instance version container.
**Inheritance**: VERSIONED_OBJECT

#### 4.8.5 EHR_STATUS Class

**Description**: Single EHR-wide object containing status flags/settings.
**Inheritance**: LOCATABLE

**Attributes**:

| Cardinality | Name | Type | Meaning |
|---|---|---|---|
| 1..1 | subject | PARTY_SELF | Record subject |
| 1..1 | is_queryable | Boolean | True if EHR included in population queries |
| 1..1 | is_modifiable | Boolean | True if EHR content modification allowed |
| 0..1 | other_details | ITEM_STRUCTURE | Additional EHR summary archetyped details |

**Invariants**:
- `Is_archetype_root`: is_archetype_root true

#### 4.8.6 VERSIONED_COMPOSITION Class

**Description**: Version-controlled composition abstraction by inheriting VERSIONED_OBJECT<COMPOSITION>.
**Inheritance**: VERSIONED_OBJECT

**Functions**:

| Returns | Name | Meaning |
|---|---|---|
| Boolean | is_persistent() | Indicates persistent composition set |

**Invariants**:
- `Archetype_node_id_valid`: All version archetype_node_id equals first version
- `Persistent_validity`: All version is_persistent equals first version data is_persistent

---

## 5. Composition Package

### 5.1 Overview

Composition is primary EHR 'data container,' root clinical content point. COMPOSITION instances may be considered self-standing data aggregations or documents.

**Key information attributes**: `_content_`, `_context_`, `_composer_`.

### 5.2 Context Model of Recording

#### 5.2.1 Overview

openEHR EHR model systematically analyzes "context." Real-world contexts map to information model levels:

**Left side**: Data-entry session context where "healthcare event" containing "clinical statements" added to EHR.
- **Healthcare event**: Any health system business activity for patient
- **Clinical statement**: Minimal indivisible information unit clinician records

**Right side**: EHR recording environment.
- Distinct coarse-grained items: Compositions over time, organized by Folders
- Structure: Composition contains Entries, organized by Sections

#### 5.2.2 Composer

Composer: Person primarily responsible for Composition content. Could be junior doctor, nurse, patient, or software agent. Mandatory since all content created by someone/something.

**Composer vs. Committer**:
- Composer: Demographic identifier (e.g., "RN Jane Williams")
- VERSION.audit.committer: Computer system user identifier (e.g., "jane.williams@westmead.health.au")

#### 5.2.3 Event Context

##### 5.2.3.1 Overview

Optional event_context in COMPOSITION documents healthcare event causing new/changed content.

**Healthcare event definition**: Billable health system business activity with/for/on behalf of patient.

**Event context information**: Start and optional end time, health care facility, setting, participating healthcare professionals, optional archetype-defined details.

##### 5.2.3.2 Occurrence in Data

Primary Composition contains EVENT_CONTEXT instance. Other Compositions in same Contribution (updates to medication list, family history, etc.) may have no EVENT_CONTEXT.

##### 5.2.3.3 Time

Event context times represent encounter/activity time undertaken by health provider for patient. Mandatory start time, optional end time.

##### 5.2.3.4 Participations

Describes who participated and how. Each participation object describes participation "mode" (direct presence, video-conference, etc.).

##### 5.2.3.5 Healthcare Facility, Location and Setting

- **_health_care_facility_**: Records health care facility where event occurred
- **_location_**: Records physical care delivery location
- **_setting_**: Documents care event "setting" using openEHR Terminology "setting" group

### 5.3 Composition Content

Data in Composition stored in `_content_` attribute. Four data structuring kinds:
- Empty
- Unstructured
- Hierarchical (Sections and entries)
- Mixed

---

## 6. Content Package

### 6.1 Overview

Content package contains classes describing EHR Composition content structure and semantics.

### 6.2 Class Descriptions

#### 6.2.1 CONTENT_ITEM Class

**Description**: Abstract parent class for navigation and entry content items.
**Inheritance**: LOCATABLE

---

## 7. Navigation Package

### 7.1 Overview

Navigation package provides SECTION class enabling hierarchical paper record-like "heading" structures.

### 7.2 Class Descriptions

#### 7.2.1 SECTION Class

**Description**: Represents hierarchical heading structure navigating Composition content. May contain Entries or other Sections.
**Inheritance**: CONTENT_ITEM

---

## 8. Entry Package

### 8.1 Design Principles

#### 8.1.1 Information Ontology

Entry package based on scientific realist ontological approach distinguishing:
- **Observations**: Observations of patient state
- **Evaluations**: Assessments and evaluations
- **Instructions**: Actionable directives
- **Actions**: Results of performing instructions

#### 8.1.2 Clinical Statement Status and Negation

Clinical statements may be recorded with various statuses reflecting clinical context.

#### 8.1.3 Demographic Data in the EHR

EHR contains primarily clinical data; demographic information maintained separately. References to people use PARTY_PROXY objects.

### 8.2 Entry and its Subtypes

#### 8.2.1 The Entry Class

**Description**: Abstract parent for all EHR clinical content entries.
**Inheritance**: CONTENT_ITEM

#### 8.2.2 Care_entry and Admin_entry

**CARE_ENTRY**: Clinical entries recording patient care.
**ADMIN_ENTRY**: Administrative entries recording administrative events (admissions, discharges, transfers).

#### 8.2.3 Observation

**Description**: Records observed phenomena including measurements.

**Timing in Observations**: Observations have associated time indicating when observation made. May be single instant or series over time.

#### 8.2.4 Evaluation

**Description**: Records assessments, diagnoses, evaluations based on clinical judgment.

#### 8.2.5 Instruction and Action

##### 8.2.5.1 Requirements

Instructions model actionable clinical directives (medications, procedures, monitoring). Actions record directive execution.

##### 8.2.5.2 Design Principles

Based on workflow principles distinguishing:
- **Intention**: What is intended to happen
- **Planning**: How/when it will happen
- **Execution**: What actually happened
- **Completion**: Whether/how completed

##### 8.2.5.3 Model Overview

INSTRUCTION contains one or more ACTIVITY instances defining what to do. Each ACTIVITY transitions through state machine indicating execution status.

##### 8.2.5.4 The Standard Instruction State Machine (ISM)

Defines standard states through which instructions progress:
- **Planning states**: Initial, planned
- **Execution states**: Active, suspended, aborted
- **Completion states**: Completed, cancelled

### 8.3 Class Descriptions

#### 8.3.1 ENTRY Class

**Description**: Abstract parent for all clinical content entries.
**Inheritance**: CONTENT_ITEM
**Attributes**: Subject, provider, protocol, guideline_id.

#### 8.3.2 ADMIN_ENTRY Class

**Description**: Administrative entries recording system events.
**Inheritance**: ENTRY

#### 8.3.3 CARE_ENTRY Class

**Description**: Clinical entries recording patient care activities.
**Inheritance**: ENTRY
**Attributes**: Guideline_id and clinical context attributes.

#### 8.3.4 OBSERVATION Class

**Description**: Recorded observations of patient phenomena.
**Inheritance**: CARE_ENTRY
**Attributes**: Data (history of observed values) and protocol.

#### 8.3.5 EVALUATION Class

**Description**: Clinical assessments, diagnoses, and evaluations.
**Inheritance**: CARE_ENTRY
**Attributes**: Data (evaluation content) and protocol.

#### 8.3.6 INSTRUCTION Class

**Description**: Actionable clinical directives.
**Inheritance**: CARE_ENTRY
**Attributes**: Narrative, activities, expiry_time, wf_definition.

#### 8.3.7 ACTIVITY Class

**Description**: Component of instruction specifying action details.
**Attributes**: Timing, description, action_archetype_id.

#### 8.3.8 ACTION Class

**Description**: Records execution of instruction activity.
**Inheritance**: CARE_ENTRY
**Attributes**: Instruction_details, time, description, ism_transition.

#### 8.3.9 INSTRUCTION_DETAILS Class

**Description**: References instruction details in action.
**Attributes**: Instruction_id, activity_id, wf_details.

#### 8.3.10 ISM_TRANSITION Class

**Description**: Records instruction state machine transition.
**Attributes**: Current_state, transition, careflow_step, reason.

---

## Glossary

- **Archetype**: Formal definition constraining EHR information structure and values for specific clinical concepts.
- **Care Event**: Healthcare business activity (encounter, test, procedure) with/for patient.
- **Clinical Statement**: Minimal indivisible clinical information unit.
- **Composition**: EHR primary data container recording care event or state update.
- **Contribution**: Change-set recording updates to EHR at single moment.
- **Event Composition**: Records healthcare event data.
- **Folder**: Organizational structure indexing Compositions.
- **Healthcare Facility**: Care delivery management unit responsible for event.
- **Persistent Composition**: Records ongoing patient state (problems, medications, etc.).
- **Versioning**: Recording successive states of EHR objects over time.

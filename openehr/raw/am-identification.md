# Archetype Identification Specification

**Release**: AM Release-2.3.0
**Status**: STABLE
**Date**: Latest Issue
**Keywords**: archetype, identification, governance, openehr

---

## Table of Contents

- [Amendment Record](#amendment-record)
- [Acknowledgements](#acknowledgements)
- [1. Preface](#1-preface)
- [2. Overview](#2-overview)
- [3. Source Artefact Identification](#3-source-artefact-identification)
- [4. Versioning](#4-versioning)
- [5. Lifecycle Model](#5-lifecycle-model)
- [6. Distributed Governance](#6-distributed-governance)
- [7. Referencing](#7-referencing)
- [8. Reliable URI for Knowledge Resources](#8-reliable-uri-for-knowledge-resources)
- [9. Artefact Authentication](#9-artefact-authentication)
- [10. Scenarios](#10-scenarios)

---

## Amendment Record

| Issue | Details | Completed |
|-------|---------|-----------|
| **AM Release 2.3.0** | | |
| 0.7.9 | SPECPUB-7: Convert citations to bibtex form | 15 Dec 2019 |
| 0.7.8 | SPECAM-58: Correct errors and examples; change `_instance_uid_` to `_build_uid_` | 18 Nov 2018 |
| **AM Release 2.2.0** | | |
| **AM Release 2.1.0** | | |
| 0.7.7 | SPECAM-52: Improve version numbering explanation | 13 Feb 2018 |
| 0.7.6 | SPECAM-41: Correct 'unstable' to 'alpha' | 18 Jun 2017 |

---

## Acknowledgements

### Primary Author

- Thomas Beale, Ars Semantica, UK; openEHR International Board

### Contributors

- Sebastian Garde PhD, Ocean Informatics
- Heather Leslie MD, Ocean Informatics
- Ian McNicoll MD, MSc, Ocean Informatics UK
- Martin van der Meer, Code24, Netherlands
- David Moner PhD, Universitat Politecnica de Valencia, Spain
- Erik Sundvall PhD, Linkoping University, Sweden

### Trademarks

- 'openEHR' is a registered trademark of The openEHR Foundation
- 'SNOMED CT' is a registered trademark of IHTSDO

### Supporters

- openEHR Industry Partners
- Better d.o.o, Slovenia
- Ocean Informatics, UK

---

# 1. Preface

## 1.1. Purpose

This specification defines an identification system for openEHR archetypes and templates. It covers:

- Formal human-readable and machine identifiers
- Versioning schemes
- Lifecycle management and states
- Inter-artefact referencing
- Transfer and forking mechanisms
- Integrity and non-repudiation support

Unless otherwise stated, "artefact" refers to these specific types.

## 1.2. Related Documents

**Prerequisite documents:**
- openEHR Architecture Overview
- openEHR Archetypes Technical Overview
- openEHR Base Types Specification

**Related documents:**
- openEHR Archetype Object Model 2 (AOM2) Specification
- openEHR Archetype Description Language (ADL2) Specification

## 1.3. Status

This specification is STABLE. Development versions available at:
https://specifications.openehr.org/releases/AM/latest/Identification.html

**TBD** items indicated with "to be determined" paragraphs throughout.

## 1.4. Feedback

- Forum: https://discourse.openehr.org/c/specifications/adl
- Issue Tracker: https://specifications.openehr.org/components/AM/open_issues

## 1.5. Conformance

Conformance is determined by formal testing against openEHR Implementation Technology Specifications (ITSs), such as IDL interfaces or XML schemas.

## 1.6. Tools

- **ADL Workbench**: Reference compiler and editor
- **Downloads**: https://www.openehr.org/downloads/modellingtools
- **Source**: https://github.com/openEHR

---

# 2. Overview

## 2.1. Scope

This specification addresses reliable identification and referencing of complex knowledge artefacts in distributed authoring environments. Primary focus is archetypes and templates, including operational templates. Related artefacts include terminology subsets and query sets.

**Out of scope**: Atomic concepts in standard terminologies (ICD10, SNOMED CT, LOINC) and ontologies (OGMS, FMA, IAO).

**Note**: "Archetype" means any formal artefact in the Archetype Definition Language (ADL) or Archetype Object Model (AOM) serialised form, including template archetypes.

## 2.2. Environment

Archetypes are produced within either unmanaged environments or through Custodian Organisations (COs), which maintain:

- **Repository**: Stores and manages archetypes
- **Registry**: Maintains archetype metadata
- **Classification**: Semantic indexing via ontologies

COs typically develop archetypes based on "upstream" releases from higher-level organizations (national, international). A logical "virtual inclusion" mechanism enables downstream COs to reuse upstream versions.

## 2.3. The Problem

Knowledge artefacts differ from software in being "outside the software" and implementation-technology-independent. They can be created, developed, and disseminated independently.

**Key requirements addressed:**

- Identify and distinguish versions, variants, and releases within authoring environments
- Define rules for expressing and resolving inter-artefact references
- Define rules for compiled/operational artefact identification
- Establish identifier evolution based on standard lifecycles
- Define rules for retired, moved, or forked artefacts

## 2.4. Human-readable and Machine Identifiers

Two identification approaches exist:

### Human-Readable Identifiers (HRIDs)

Support:
- Specialisation/subsumption hierarchies
- Multi-dimensional concept spaces
- Flexible versioning
- Formal reflection of ontological understanding

Example: `FastSortedList` in object-oriented software

**Key feature**: May change during early development (pre-v1.0) but stabilize later.

### Machine Identifiers

Characteristics:
- Not human-readable
- Don't inherently support versioning (unless specifically designed)
- Enable various computational operations
- Require mapping to human-readable forms
- Don't change once assigned

### Combined Approach

This specification uses both:

1. **GUID assignment**: Upon creation; never changes regardless of artefact modifications
2. **Finer-level snapshots**: Additional GUIDs identify specific changed states
3. **Namespaced HRIDs**: Computed from artefact properties; multiple identifiers possible
4. **Build identification**:
   - Build number (part of version ID)
   - Hash on canonical serialisation

## 2.5. Meta-data

Artefact identification implicates metadata since HRIDs are constructed from properties like:
- Reference model class
- Version
- Namespace
- Concept identifier

Items that may change without affecting semantics (ontological classification, ownership status) should be stored in external Registry rather than within artefacts.

---

# 3. Source Artefact Identification

## 3.1. Overview

Source artefact identification employs multiple logically-identifying properties plus machine identifiers. HRIDs are generated from non-uid properties.

For archetypes/templates, identifying properties from the `ARCHETYPE_HRID` class include:
- `namespace`: Distinguished logical identifiers by organization
- `rm_publisher`, `rm_closure`, `rm_class`, `concept_id`: Main HRID components
- `release_version`: 3-part version identifier (e.g., '1.3.0')
- `build_uid`: Incremented at every commit
- `description.lifecycle_state`: Development state

Functions defined:
- `interface_id()`: Returns interface archetype HRID
- `physical_id()`: Returns physical archetype HRID
- `version_id()`: Returns full version string
- `major_version()`, `minor_version()`, `patch_version()`: Extract version parts

The `uid` property provides machine identification (typically GUID). Both `uid` and `namespace` are optional for legacy reasons; archetypes lacking them are considered "unmanaged."

## 3.2. Formal Model

Grammar for human-readable identifiers (managed and unmanaged):

```
artefact_hrid           =   namespaced_hrid | local_hrid ;
namespaced_hrid         =   namespace '::' local_hrid ;
local_hrid              =   hrid_root '.v' version_id ;
namespace               =   V_REVERSE_DOMAIN_NAME ;
V_REVERSE_DOMAIN_NAME   =   ; (* See IETF RFCs 1035, 123, 2181 *)
```

Namespace uses reverse domain names (publisher organization) to:
- Aid lexical sorting
- Support directory structure construction
- Distinguish managed from unmanaged artefacts

**Examples:**
- `org.openehr`: EHR archetypes at openEHR.org
- `uk.nhs`: UK National Health Service
- `edu.nci`: US National Cancer Institute

### 3.2.1. Human-readable Identifier (HRID)

Consists of two logical parts:

```
hrid_root                       =   qualified_rm_class_name '.' concept_id ;
qualified_rm_class_name         =   rm_publisher '-' rm_closure '-' rm_class ;
rm_publisher                    =   V_ALPHANUMERIC_NAME ;
rm_closure                      =   V_ALPHANUMERIC_NAME ;
rm_class                        =   V_ALPHANUMERIC_NAME ;
concept_id                      =   V_SEGMENTED_ALPHANUMERIC_NAME ;

V_ALPHANUMERIC_NAME             =   ? [a-zA-Z][a-zA-Z0-9_]+ ? ;
V_SEGMENTED_ALPHANUMERIC_NAME   =   ? [a-zA-Z][a-zA-Z0-9_-]+ ? ;
```

**Field meanings:**

| Field | Purpose |
|-------|---------|
| `rm_publisher` | Organization originating the reference model |
| `rm_closure` | Reference model top-level package closure identifier |
| `rm_class` | RM class or equivalent entity name |
| `concept_id` | Identifier from information artefact ontology |

**Examples:**
- `openEHR-EHR-EVALUATION`
- `ISO-ISO13606-ENTRY`

**Closure concept**: Top-level package from which focal class is reachable. For example, openEHR's `CLUSTER` class appears in both `ehr` and `demographic` packages. An archetype for `CLUSTER` would specify which closure it belongs to:
- `openEHR-EHR-CLUSTER` for EHR-based clusters
- Different closure for demographic-based clusters

#### 3.2.1.1. Concept Identifier

Short ontological identifier (historically called 'concept' or 'domain concept'). Examples: `bp_measurement`, `problem_diagnosis` in natural language or mnemonic form.

#### 3.2.1.2. Legacy ADL 1.4 Semantics

Historical ADL 1.4 (ISO 13606-2:2008) encoded specialisation hierarchy using hyphenated segments: `problem` and `problem-diagnosis` indicated hierarchy.

**Modern approach**: Specialisation hierarchy no longer encoded in concept identifier. The `-` character remains permitted but carries no semantic significance. This:
- Frees domain concept assignment
- Aligns with object-oriented naming conventions
- Removes ability to determine specialisation level from identifier alone

#### 3.2.1.3. Concept Identifier Semantics

Concept identifiers must originate from formal ontologies corresponding to the artefact's namespace. Rules govern assignment through maintaining a Custodian Organisation ontology.

Typical ontology structure contains:
- High-level health information recording entities
- Record entry types (derived from Clinical Investigator Record)
- Domain-specific entities

Example ontology node: `measurement_of_systemic_arterial_blood_pressure`

Such lengthy names ensure unambiguous meaning but are unwieldy for identifiers. Ontologies support "short identifiers" as synonyms for full node identifiers, ensuring uniqueness.

Existing archetypes integrate by either:
- Proposing current identifier as ontology short id (if data exist using these identifiers)
- Republishing under new identifier if clashes occur

#### 3.2.1.4. Need for RM Class Name in Identifier

Theoretically, reference model class identification shouldn't be needed in well-constructed identifiers (avoiding clashes regardless of RM class). However, practice shows similar concept names apply across different RM classes. Example: `lab_result` could reasonably name both an ENTRY/OBSERVATION and a COMPOSITION-level container.

The qualified RM class name acts as a "guard against clashes" without requiring a global ontology construction authority.

---

# 4. Versioning

## 4.1. General Model

Unlike software artefacts versioned at repository level, knowledge artefacts undergo **individual version control**. Each source artefact (archetype, template, subset) has its own versioning.

**Consequences:**

- Every committed change resembles a release (vs. software's multiple changes between releases)
- Each revision distinguished by version identifier (vs. software's constant logical name)

**Distinction from software:**

| Aspect | Software | Knowledge Artefacts |
|--------|----------|-------------------|
| Versioning | Repository-level snapshots | Per-artefact, independent |
| Release | Publishing specific snapshots | Publishing artefacts directly |
| Computation | Release IDs not computed | Versioned IDs used computationally |

## 4.2. Version Numbering

Version identifiers follow [Semantic Versioning (semver.org)](http://semver.org) rules with three levels plus optional lifecycle extensions:

```
version_id        =   release_version [ extension ] ;
release_version   =   major_version '.' minor_version '.' patch_version ;
major_version     =   { V_NUMBER } ;
minor_version     =   { V_NUMBER } ;
patch_version     =   { V_NUMBER } ;
extension         =   version_modifier '.' issue_number ;
version_modifier  =   '-rc' | '-alpha' ;
issue_number      =   V_NUMBER ;
V_NUMBER          =   { V_DIGIT }+ ;
V_DIGIT           =   '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' ;
```

**Version levels:**

- **Major version**: Incremented with breaking changes to formal definition; may increment for lesser changes
- **Minor version**: Incremented with non-breaking enhancements to formal definition
- **Patch version**: Incremented with changes to informal parts only
- **Build number**: Incremented at every commit; reset to 1 on version ID change

**Formal definition** includes:
- Identifier section
- `specialize` clause
- `definition` section
- Within `terminology` section:
  - `text` short names in `term_definitions`
  - `term_bindings` section
  - `value_set` section

**Example identifiers:**
```
1.3.5-alpha         # alpha development version based on 1.3.4
1.3.5-rc.3          # release candidate for 1.3.5, issue 3
1.3.5               # release 1.3.5
```

**General rules:**

1. **First version rule**: Initial version is `v0.N.P` (usually `0.0.1`; higher v0 versions indicate relative maturity)

2. **Incrementing rule**:
   - Major version increment: Reset minor and patch to 0
   - Minor version increment: Reset patch to 0

**Variant versions:**
- `rc` (release candidate): `M.N.P-rc.B` format; precedes target version `M.N.P`
- `-alpha`: Indicates development version prior to preceding numeric identifier

**Note**: Only major version appears in source artefact HRID. Breaking changes create new deployable artefacts, similar to software interface versioning.

## 4.3. Change Semantics

The 3-part semver scheme enables distinguishing change levels. Authors may increment versions beyond minimum mechanical requirements based on domain considerations.

**Rule definition**: Specifies _minimum necessary level_ of version change, not mandated level.

## 4.4. Versionable 'interface' for Archetypes

Semver's "interface" concept, adapted for archetypes:

**Archetype signature** = Set of `<path, RM type, AOM constraint>` for every definition node.

Archetype paths are hierarchical structures through Reference Model.

**Path components:**
- RM attribute names (left column)
- Node id-codes (archetype-specific)
- Node RM types (middle column)
- Constraints at each node (type, value, cardinality, occurrence)

### 4.4.1. Interface Preservation

An archetype interface is preserved when:
- Existing paths unchanged (hierarchy and id-codes identical)
- No paths deleted from path set
- No domain meaning changes for id-codes in paths
- RM types identical or ancestor types (super-types) to originals
- Constraints at each path identical or wider than original

### 4.4.2. Major Version (Breaking) Changes

Breaking changes fail to preserve the archetype interface, preventing data from previous releases validating against new versions.

**Examples:**
- Removal of mandatory data points/groups
- Node removal
- Node movement to different sub-tree
- Domain definition change for id-code
- Constraint narrowing (including RM type)

All require new major version.

### 4.4.3. Minor Version Changes

Non-breaking enhancements to the interface:

- Constraints/RM types widened (old constraint subsumed by new)
- Additional definition nodes (new paths)
- Terminology binding additions

**Important consequence**: Minor versions may include additional semantics compared to previous minor versions in same major version. Therefore, **referencing by major version alone may not designate all available interface elements**. Minimum minor version specification often needed.

### 4.4.4. Patch Version Changes

Changes requiring patch version increment:

- Meta-data changes
- Language translation additions
- Terminology wording changes (non-semantic)

---

# 5. Lifecycle Model

## 5.1. Conceptual Model

Artefacts follow multi-level lifecycle with macro-states and micro-states:

**Macro-states** (dark blue):
- `unmanaged`
- `development`
- `release_candidate`
- `published`
- `deprecated`
- `rejected`

**Micro-states**: Optional for finer-grain state indication typically supported in repositories.

**Typical traversals:**
- `[ unmanaged -> ] development -> published`
- `development ... development -> release_candidate -> ... release_candidate => published`
- `published -> deprecated`
- `development -> rejected`

**Linguistic conventions:**
- `start_review`: All actions entering `development` macro-state
- `release` (action): Making artefact available to public (including pre-releases)
- `publish` (action): Making definitive release

## 5.2. Lifecycle-based Versioning

Version evolution according to lifecycle:

- **v0 versions**: Initial unstable development. Artefacts typically start at `0.0.1` (or higher v0 to indicate maturity). Minor/patch numbers updated freely.

- **Upload to managed repository**: Identifier prepended with namespace; `-alpha` appended.

- **Rejection**: Lifecycle state set to `rejected`; version unchanged.

- **Release preparation**: Release version computed as `v1.0.0` or based on difference from base version.

- **Pre-release cycle**: Version becomes `M.N.P-rc.B` format. Options from `release_candidate` state:
  - Publish definitively with stable `M.N.P` version ID
  - Release newer release candidate (patch-level or less changes only)
  - Return to `development` for larger changes

- **Direct release**: Released directly to stable `M.N.P` version

- **Deprecation**: Lifecycle state set to `deprecated`; version unchanged.

**Version precedence example:**
```
1.2.3-rc.1 < 1.2.3-rc.2 < 1.2.3 < 1.2.4-alpha < 1.3.0-alpha < ... < 1.3.0
```

---

# 6. Distributed Governance

## 6.1. Overview

Rules managing artefact identifiers in distributed environments accounting for artefacts coming under management, transfers, and forking.

## 6.2. Management

Initially "unmanaged" artefacts (no custodial organization) may be adopted by a Custodian Organisation following governance and quality assurance rules.

**Management process upon adoption:**

- Lifecycle state progresses to `initial`
- Human-readable identifier changed to namespaced form
- Newly generated GUID assigned as `uid`
- If major version > 0, reset to `0.0.1`; otherwise unchanged
- Meta-data set (copyright, license)
- SHA-1 hash may be generated and stored in repository

## 6.3. Transfer and Forking

Once managed, artefacts may be deployed (data created with identifiers). Two possible artefact roles in organizations:

- Actively developed and maintained
- Deployment only

**Transfer scenario**: Organization ceases maintenance, transferring responsibility to another (e.g., national-level). At acquisition:

**Arguments for changing HRID:**
- New CO identification requirement
- Possibility of original domain's continued local releases (forking)
- New CO may rename for ontological classification fit
- If no data/queries created yet, no concrete impact
- Current namespace easier for support/contact

**Approach**: Rules provided for re-identification without obligation. Requires establishing "artefact equivalence" concept.

**Mutable HRID components upon transfer:**
- `namespace`: Will always change minimally
- `concept_id`: May or may not change
- Version identifier: Likely changes

Reference model parts (`rm_publisher`, `rm_closure`, `rm_class`) cannot change formally.

**Machine identifier rule**: When HRID changes (any aspect), `uid` must also change to prevent confusion between original's new versions and transferred artefact's releases.

**Equivalence tracking**: Metadata section recording equivalence between current and previous identifiers:

```
id_history = <
    ["2001-05-27"] = <
        old = <
            hrid = <"au.com.rbh::openEHR-EHR-EVALUATION.problem_desc.v2.4.1">
            uid = <"5221C9E5-0ECA-469F-83C5-A5D5A0C6682C">
        >
        new = <
            hrid = <"au.gov.nehta::openEHR-EHR-EVALUATION.problem.v1.0.1">
            uid = <"094C8B37-F0CD-45C9-A1B7-CDFDE14C67AB">
        >
    >
    ["2004-14-03"] = <
        old = <
            hrid = <"au.gov.nehta::openEHR-EHR-EVALUATION.problem.v1.6.3">
            uid = <"E50290BB-890A-4344-9480-D40AF01C5BCC")
        >
        new = <
            hrid = <"au.gov.doha::openEHR-EHR-EVALUATION.problem.v1.6.3">
            uid = <"F4166F58-4EDA-4F13-B413-45A8F7A3E53D")
        >
    >
>
```

Resembles DNS CNAME records for alias domain names.

---

# 7. Referencing

References between artefacts use human-readable identifiers (HRIDs) in source form; operational/data references may use either HRIDs or machine identifiers.

**Key distinction**: References differ from identifiers. References contain either full physical identifier or partial version information, matched against full identifications.

**Reference types:**

```
hrid_ref                =   namespaced_hrid_ref | local_hrid_ref ;
namespaced_hrid_ref     =   namespace '::' local_hrid_ref ;
local_hrid_ref          =   ihrid_ref | sihrid_ref | phrid_ref ;
ihrid_ref               =   hrid_root '.v' major_version ;
sihrid_ref              =   hrid_root '.v' major_version '.' minor_version ;
phrid_ref               =   local_hrid ;
```

**Reference categories:**

- **Interface HRID reference (ihrid_ref)**: Matches latest release of major version
- **Specific interface HRID reference (sihrid_ref)**: Matches specific release with major+minor versions
- **Physical HRID reference (phrid_ref)**: Identifies identical artefact instances (full version identifier)

**Example:**
```
org.openehr::openEHR-EHR-EVALUATION.diagnosis.v1    # Different logical archetypes
org.openehr::openEHR-EHR-EVALUATION.diagnosis.v2

org.openehr::openEHR-EHR-EVALUATION.diagnosis.v1.1.5 # Logically substitutable
org.openehr::openEHR-EHR-EVALUATION.diagnosis.v1.1.7
```

## 7.1. Source Artefact References

### 7.1.1. Archetype External References (ADL/AOM 2)

ADL 2 enables direct archetype-archetype references using mini-HRID:

```
ACTIVITY[id2] matches {   -- Medication activity
    description matches {
        use_archetype ITEM_TREE [openEHR-EHR-ITEM_TREE.medication.v1]
    }
}
```

**Resolution algorithm**:
- Most recent released version variant of `openEHR-EHR-ITEM_TREE.medication.v1` (e.g., `v1.0.4`, `v1.2.49`)
- OR latest release candidate version (guaranteed semantically compatible with target version)

**Namespace assumption**: No namespace implies same namespace as current archetype (possibly no namespace).

**General case**: Typically `ihrid_ref`; may include minor version for exact structural form. Testing/research may reference patch and `-rc`/`-alpha` versions.

### 7.1.2. Template References to Archetypes and Templates

Templates carefully control exact contents/structure; references must accommodate all version levels:

- `org.openehr::openEHR-EHR-EVALUATION.problem.v2` (major only)
- `org.openehr::openEHR-EHR-EVALUATION.problem.v2.4` (major+minor)
- `org.openehr::openEHR-EHR-EVALUATION.problem.v2.4.17` (major+minor+patch)

Development/research environments may allow `-rc` and `-alpha` variants. General case: `hrid_ref`.

### 7.1.3. Between Specialised Archetypes

Specialised archetypes reference parents using HRID including only major version:

- Non-namespaced reference: Assumed from same namespace as specialised archetype
- Namespaced reference: Resolves against latest release in locally-available repository copy

**Key rule**: All archetypes in a check-out/release must compile validly at any time. Revised parent invalidating inheritance children requires child revisions before repository validity. New artefact versions may require child archetype re-versioning.

## 7.2. Source Artefact Relationship Constraints

Constraints evaluated at runtime resolve to artefact identifiers.

### 7.2.1. ADL 1.4 Archetype Slots

Slots defined via assertions in slot statements. Current tooling uses regular expressions (REs) on archetype identifiers (major version only):

```
openEHR-EHR-EVALUATION.problem.v1
```

Example slot definition:
```
protocol matches {
    ITEM_TREE[at0015] matches {
        items cardinality matches {0..*; ordered} matches {
            allow_archetype CLUSTER[id20] occurrences matches {0..1} matches {
                include
                    archetype_id/value matches {/openEHR-EHR-CLUSTER\.device(-[a-zA-Z0-9_]+)*\.v1/}
            }
        }
    }
}
```

Allows `openEHR-EHR-CLUSTER.device.v1` or `openEHR-EHR-CLUSTER.device-xxx.v1` (ADL 1.4 specialisation method).

Namespace rule: No namespace means current archetype's namespace; explicit namespace means archetypes from that namespace.

Released archetypes should reference major versions only; technically minor/patch/build versions possible.

### 7.2.2. ADL 2 Archetype Slots

ADL 2 uses semantic (vs. lexical) expressions with archetype concept constraints (SNOMED CT post-coordination style):

```
allow_archetype CLUSTER [id4.1] occurrences matches {0..1} matches {
    include matches {True}
        archetype_id matches {
            ARCHETYPE_ID matches {
                namespace matches {...}
                concept matches {<< investigation_methodology OR << investigation_protocol}
                ...
            }
        }
    }
```

Requires ontological underpinning for `concept_id`.

## 7.3. AQL Query Sets

Multiple AQL queries authored together achieve design objectives (populate reports, screens; analytical purposes). Many are local; others carefully designed for guidelines/standard computations. Within archetyped frameworks, query sets require identification/management similar to other artefacts.

## 7.4. AQL Queries

Archetype-based queries contain archetype/template references and paths. Example:

```
SELECT pulse
FROM EHR[ehr_id/value=$ehruid]
 CONTAINS COMPOSITION c
 CONTAINS OBSERVATION pulse[openEHR-EHR-OBSERVATION.pulse.v1]

WHERE c/name/value='Encounter' AND
    c/context/start_time/value <= $endperiod AND
    c/context/start_time/value >= $startPeriod AND
    pulse/data/events[id6]/data/items[id4]/value/value < 60
```

**Reference semantics differ**: References followed by paths referring to specific data points. For correct query, path must exist in matched archetype.

**Key issue**: Since minor versions can add interface elements (data points/paths), valid paths require oldest archetype containing them. Example path:

```
[openEHR-EHR-OBSERVATION.pulse.v1]/data/events[at0006]/data/items[at0004]/value/value
```

Must exist in earliest v1.x release (v1.0.0). If added in later minor release, reference must include first minor version.

**Query processor matching**:
- Any instance of data point at path in referenced archetype
- Any instance in congruent path in specialisation child archetype

Congruent path example:
```
/data/events[id6.0.4]/data/items[id4.1]/value/value
```

## 7.5. Operational Artefacts

Operational artefacts (flattened archetypes, operational templates) built from source artefacts via compiler tools with reference resolution within repository.

**Configuration tracking**: Managed source artefacts can include fine-grained revision information specifying exact source artefact set used.

Configuration structure:
```
configuration       =   archetype_config template_config subset_config rm_release ;
archetype_config    =   config_item { config_item } ;
template_config     =   { config_item } ;
subset_config       =   { config_item } ;
rm_release          =   rm_name release_id ;

config_item         =   identifier [ revision_id [ commit_id ] ] [ signature ] ;

signature           =   CHARACTER_SEQUENCE ;
revision_id         =   V_INTEGER ;
commit_id           =   V_INTEGER ;
release_id          =   V_STRING ;
```

Example operational template configuration (ODIN format):

```
archetypes = <
    [1] = <
        id = <"org.openehr::openEHR-EHR-OBSERVATION.heartrate.v1.3.28">
        signature = <"23895yw85y0y0">
    >
    [2] = <
        id = <"au.gov.nehta::openEHR-EHR-EVALUATION.genetic-diagnosis.v1.2.0">
        signature = <"98typrhweruhfd">
    >
    [3] = <
        id = <"org.openehr::openEHR-EHR-EVALUATION.problem.v2.4.0">
        signature = <"2rfhweiudfwieurfh">
    >
>
templates = <
    [1] = <
        id = <"au.gov.nehta::openEHR-EHR-COMPOSITION.vital_signs.v5.36.1">
    >
>
subsets = <
    [1] = <
        id = <"org.ihtsdo.general::cardiac_diagnoses.v18.1.0">
    >
>
rm = <
    name = <"org.openehr.rm">
    release = <"1.1">
>
```

## 7.6. References from Data

### 7.6.1. Requirements

In knowledge-enabled systems using archetypes, data "conforms" to relevant artefacts. Artefact references in data enable further processing (display, modification, querying).

**Operational system data requirements:**

1. **Reconstitutability**: Re-connect data with creating archetypes/templates/subsets; major and minor versions necessary
2. **Querying**: Determine available archetype path-sets for querying, including specialisation parents
3. **Optimisation**: Manage archetype identifier overhead in large-scale systems

**Extract/message data requirements:**

1. **Reconstitutability**: Enable receiver systems to correctly reconstitute data
2. **Querying**: Support receiving system's querying capability, potentially using general parents
3. **Optimisation**: Reasonable trade-off between space optimization and clarity

### 7.6.2. Reconstitutability

Record archetype/template identifiers on relevant data nodes. Basic approach: At archetype root nodes, record archetype identifier and template (if relevant); at interior nodes, record at-codes. Formally, archive identifier and at-codes recorded in `LOCATABLE.archetype_node_id`.

**openEHR Release 1.0.2 or earlier example:**
```
openEHR-EHR-EVALUATION.diagnosis.v1
```

**Modern form** includes namespace and full version:
```
org.openehr::openEHR-EHR-EVALUATION.diagnosis.v1.29.0
```

**Unmanaged archetype references**: Remain legal; lack of minor/patch numbers interpreted as `.v1.0.0`.

### 7.6.3. Supporting Archetype-based Querying

Querying based on archetype 'path-sets' extracted from operational archetypes. Paths are simplified X-paths.

**Allowable querying archetypes for data created with archetype X:**
- X itself (exact version, revision, commit)
- Previous minor/patch variants of X
- Specialisation parents of X
- Previous minor/patch variants of parents

**Problem**: Specialisation lineage only obtainable from operational archetype in template. Data imported without template lacks this information, preventing queries using general parent archetypes.

**Solution strategies:**

1. Include template configuration metadata with exchanged data (EHR Extract)
2. Include archetype lineage information in data itself

**Second approach**: Generalization of identifier reference. For non-specialised archetypes, lineage is that archetype's ID. For specialised archetypes, it's a list. Example lineage:

```
au.gov.nehta::openEHR-EHR-EVALUATION.genetic_diagnosis.v1.12.9,
org.openehr::openEHR-EHR-EVALUATION.diagnosis.v1.29.0,
org.openehr::openEHR-EHR-EVALUATION.problem.v2.4.18
```

### 7.6.4. Formal Model

Reference definition supporting requirements:

```
archetype_data_ref  =   archetype_ver_ref { ',' archteype_ver_ref } ;
archteype_ver_ref   =   hrid_root '.' version_id_ref ;
version_id_ref      =   'v' version_id ;
```

### 7.6.5. Optimisations

In typical archetype data, references repeat throughout components (e.g., openEHR COMPOSITION). Example: `COMPOSITION` with 5 problems using archetype:

```
uk.nhs.royalfree.clinical::openEHR-EHR-EVALUATION.diagnosis.v2.15.0
```

Lineage:
```
org.openehr::openEHR-EHR-EVALUATION.diagnosis.v1.29.0
org.openehr::openEHR-EHR-EVALUATION.problem.v2.4.0
```

Total character count: 66 + 57 + 54 = 177 characters. Repeated 5 times: 885 characters for identifiers in data with similar-sized clinical content.

#### 7.6.5.1. Identifier Aliasing

Top-of-Extract variable definitions:

```
id01=uk.nhs.royalfree::openEHR-EHR-EVALUATION.diagnosis.v2.15.0,
    org.openehr::openEHR-EHR-EVALUATION.diagnosis.v1.29.0,
    org.openehr::openEHR-EHR-EVALUATION.problem.v2.4.0
id02=au.gov.nehta::openEHR-EHR-OBSERVATION.hba1c_result.v1.4,
    org.openehr::openEHR-EHR-OBSERVATION.lab_result.v1.18
etc
```

Use `id01`, `id02` etc. in data, reducing overhead ~50% in some cases. Implemented via `EHR_EXTRACT` attributes in openEHR RM.

**Considerations**: Complicates querying (returns data with local variable names vs. proper metadata). Cannot reliably remove reference model/class identifiers despite initial appearance -- data extraction transforms may preserve original RM references; different standards may adopt published archetype libraries.

#### 7.6.5.2. Reference Compression

Further compression via replacing repeated identifier sections with special characters:

```
id01=uk.nhs.royalfree::openEHR-EHR-EVALUATION.diagnosis.v2.15.0,
    org.openehr::~.diagnosis.v1.29.0,
    ~::~.problem.v2.4.0
id02=au.gov.nehta::openEHR-EHR-OBSERVATION.hba1c_result.v1.4.0,
    org.openehr.ehr::~.lab_result.v1.18.0
```

The `~` character means "missing parts from previous identifier in list." Concrete archetype guaranteed first, in entirety.

Debate: Additional space savings (vs. parsing complexity) justification depends on specific system context. Systems using single reference model could reduce further; however, data sharing risks non-interoperability.

---

# 8. Reliable URI for Knowledge Resources

**TBD**: A standardised and reliable Uniform Resource Identifier (URI) for released knowledge resources (source and operational forms) should be established, potentially justifying its own scheme-space or within standard http scheme.

---

# 9. Artefact Authentication

Revision information reliability challenges require mechanisms ensuring:
- Two identical physical artefacts don't have different identifiers/revision info
- Different artefacts aren't identified identically

## 9.1. Integrity Check

Digital hash functions (SHA-1, MD5) generate "fingerprints"; identical hashes guarantee identity. However, typical file representations have semantically-insignificant differences (whitespace, non-significant ordering, metadata changes) generating different hash values.

**Solution**: Canonical artefact form insensitive to semantically-insignificant differences while retaining computational difference indicators.

Integrity check process: Source artefact -> Canonical form -> Hash function -> Hash digest

## 9.2. Authentication

Establishing true origin requires digital signatures. Typical scheme: Producer signs with private key; consumers verify with public key.

For openEHR artefacts, need: Identifying true Custodian Organisation origin.

PKI approach: Each CO generates key pair; public key provided to Central Governance Authority. Signature via CO private key on already-generated artefact hash digest.

Signing process: Source artefact -> Canonical form -> Hash -> Private key signing -> Digital signature

## 9.3. Canonical Form -- Archetype 'semantic view'

Hashing/signing inputs require:
1. Validated artefact (no use signing invalid artefacts)
2. Non-semantic changes removed (requires syntactic canonical form)

Achieved via 'semantic view' -- computable Abstract Syntax Tree (AST) serialization.

**Semantic view contents:**
- Identifier
- Specialisation identifier (where present)
- Concept code
- Definition section (comments stripped)

Suitable serialization: dADL syntax. XML possible but schema-dependent; no single normative openEHR XML-schema for AOM.

**TBD**:
- Canonical forms for other artefact types
- All ADL/template forms now AOM-based (v1.5+); single canonical algorithm possible
- Operational template hashing & signing required

---

# 10. Scenarios

This section describes typical development, deployment, and querying scenarios.

### 10.1. Minor Version Upgrade

**TBD**: Detailed scenario description

### 10.2. Major Version Upgrade

**TBD**: Detailed scenario description

### 10.3. Templates using Archetypes and Subsets

**TBD**: Detailed scenario description

### 10.4. Artefact Transfer / Fork

**TBD**: Detailed scenario description

---

## License

Creative Commons Attribution-NoDerivs 3.0 Unported.
https://creativecommons.org/licenses/by-nd/3.0/

---

## Support

- **Issues**: [Problem Reports](https://specifications.openehr.org/components/AM/open_issues)
- **Web**: [specifications.openehr.org](https://specifications.openehr.org)

(c) 2009 - 2024 The openEHR Foundation

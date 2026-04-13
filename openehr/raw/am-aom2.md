# Archetype Object Model 2 (AOM2) - Complete Specification

## Document Information

**Issuer:** openEHR Specification Program  
**Release:** AM Release-2.3.0  
**Status:** STABLE  
**Keywords:** EHR, ADL, AOM, health records, archetypes, constraint language, ISO 13606, openehr

**Licence:** Creative Commons Attribution-NoDerivs 3.0 Unported

**Source:** https://specifications.openehr.org/releases/AM/latest/AOM2.html

---

## Table of Contents

- [Amendment Record](#amendment-record)
- [Acknowledgements](#acknowledgements)
- [1. Preface](#preface)
- [2. Model Overview](#model-overview)
- [3. The Archetype Package](#archetype-package)
- [4. Constraint Model Package](#constraint-model-package)
- [5. The Rules Package](#rules-package)
- [6. The RM Overlay Package](#rm-overlay-package)
- [7. Terminology Package](#terminology-package)
- [8. Validation and Transformation Semantics](#validation-semantics)
- [9. Serialisation Model](#serialisation-model)
- [10. Templates](#templates)
- [11. Reference Model Adaptation](#reference-model-adaptation)

---

## Amendment Record

### AM Release 2.3.0

| Issue | Details | Contributors | Date |
|-------|---------|--------------|------|
| SPECAM-76 | Correct VSONCO rule for redefinition of nodes with multiple occurrences; add `collective_occurrences()` conformance function | P Bos, S Garde, I McNicoll, P Pazos, J Holslag, T Beale | 09 Nov 2022 |
| SPECAM-75 | Improve specification of constraint patterns in `C_TEMPORAL` classes; add Sections 4.2.9 and 4.2.10 | P Pazos, T Beale | 12 Dec 2022 |
| SPECAM-69 | Support negative durations in `C_DURATION` | P Bos, S Garde | 09 Sep 2020 |
| SPECAM-68 | Add flexible `_constraint_status_` indicator to `C_TERMINOLOGY_CODE` | B Fabjan, I McNicoll, S Garde, P Bos, T Beale | 07 Sep 2020 |
| SPECAM-67 | Adjust package structure: rename packages for regularity | T Beale | 19 May 2020 |

### Previous Releases

**AM Release-2.2.0 (21 May 2019)**
- Add `rm_overlay` top-level section with `rm_visibility` sub-section
- Remove `_revision_history_` from ADL2 specification
- Improve documentation for constraints on lists and intervals

**AM Release-2.1.0 (10 Apr 2018)**
- Move RM adaptation attributes from BMM to AOM profile
- Add meta-attributes for archetype visualization
- Improve `_c_conforms_to()_` and `_c_congruent_to()_` algorithms

**AM Release-2.0.6 (15 Jun 2016)**
- Adjust `C_ATTRIBUTE._any_allowed_` post-condition
- Remove `C_DURATION._fractional_seconds_allowed_`
- Add primitive type matching rules
- Correct VSONT validity rule

---

## Acknowledgements

### Primary Author

Thomas Beale, Ars Semantica, UK; openEHR International Board

### Major Contributors

- Koray Atalag (National Institute for Health Innovation, New Zealand)
- Silje Ljosland Bakke (Nasjonal IKT HF, Norway)
- Pieter Bos (Nedap, Netherlands)
- Diego Boscá (IBIME, Technical University Valencia)
- Rong Chen MD, PhD (Cambio Healthcare Systems, Sweden)
- Joey Coyle MD, PhD (Intermountain Healthcare, New York)
- Borut Fabjan (Better d.o.o., Slovenia)
- Sebastian Garde PhD (Ocean Informatics, UK)
- Sam Heard MD (Ocean Informatics, Australia)
- Ian McNicoll MD (FreshEHR, UK)
- Pablo Pazos Gutierrez (CaboLabs, Uruguay)
- Harold Solbrig (Mayo Clinic, Rochester, USA)

### Supporters

- openEHR Industry Partners
- Ars Semantica, UK
- UCL (University College London) - CHIME
- Ocean Informatics, Australia

---

## 1. Preface

### 1.1. Purpose

This specification presents the normative description of openEHR Archetype and Template semantics in object model form. The model enables development of software representing archetypes and templates independent of their persistent representation, and provides the basis for parsers processing archetypes in linguistic formats such as ADL, XML, and others.

The release described corresponds to archetype formalism version 2.x. Readers should consult the ADL specification for detailed semantic explanations and examples.

**Intended Audience:**
- Standards bodies developing health informatics standards
- Research groups using openEHR and ISO 13606
- Open source healthcare community
- EHR solution vendors
- Medical informaticians and clinicians

### 1.2. Related Documents

**Prerequisite Documents:**
- openEHR Architecture Overview
- openEHR Archetypes Technical Overview
- openEHR Base Types Specification

**Related Documents:**
- openEHR Archetype Definition Language 2 Specification
- openEHR Operational Template Specification

### 1.3. Nomenclature

The term "attribute" denotes any stored property of a type, including primitive attributes and relationships. XML 'attributes' are always explicitly identified. The term "archetype" applies broadly to both specifications of clinical data groups and templates, since ADL/AOM 2 templates are technically archetypes. Statements about archetypes apply equally to templates unless otherwise indicated.

### 1.4. Status

This specification is STABLE. The development version is available at: https://specifications.openehr.org/releases/AM/latest/AOM2.html

### 1.5. Feedback

- Forum: openEHR ADL forum
- Issues: Specifications Problem Report tracker
- Changes: AM component Change Request tracker

### 1.6. Conformance

Conformance is determined by formal testing against relevant openEHR Implementation Technology Specifications (ITSs), such as IDL interfaces or XML schemas.

### 1.7. Tools

- ADL Workbench: reference compiler, visualizer, and editor
- Additional tools: Available at openEHR website
- Source projects: openEHR Github project

### 1.8. Changes from Previous Versions

#### 1.8.1. Release 1.5 to 2.0

Release 2 changes focus on computational tractability with terminology and rigorous validation/flattening:

- Introduction of new internal coding scheme (id-codes, at-codes, ac-codes)
- Replacement of string identifiers with multi-part namespaced identifiers
- Addition of explicit value-sets in terminology section
- Renaming of archetype `ontology` to `terminology`
- Expression of term bindings as IHTSDO-format URIs
- Introduction of tuple constraints replacing custom constrainer types
- Re-engineering of primitive constrainer types (`C_STRING`, `C_DATE`, etc.)
- Removal of openEHR Archetype Profile specification

#### 1.8.2. Release 1.4 to 1.5

Changes facilitate specialised archetype representation through differential form:

- Full specialisation support with path-based redefinitions
- Addition of node-level annotations
- Structural simplification of archetype ontology
- Renaming `invariant` section to `rules`
- Templates now treated as archetypes

#### 1.8.3. Release 0.6 to 1.4

- Added `_adl_version_` attribute to `ARCHETYPE` class
- Changed `_concept_code_` to `_concept_`

---

## 2. Model Overview

The AOM is a pure object-oriented model for use with archetype parsers and in-memory manipulation software, typically output from parsers of any serialized archetype format.

### 2.1. Used BASE Component Packages

The AOM depends on `base.foundation_types` package defining leaf types and utility types including `Interval<T>`. Types documented in the openEHR Foundation Types specification include:

**Leaf Types:**
- Integer
- Real
- String
- Boolean
- Date
- Time
- DateTime
- Duration

**Utility Types:**
- Interval<T>
- List<T>
- Set<T>
- Hash<K,V>

Additional definitions from `base.base_types.definitions` package:

**VALIDITY_KIND Enumeration:**
- mandatory
- optional
- disallowed

**VERSION_STATUS Enumeration:**
- released (empty string)
- release_candidate ("rc")
- alpha ("alpha")
- beta ("beta")

The `base.resource` package provides `AUTHORED_RESOURCE` and subordinate classes. The `base.expressions` package supports the rules component.

### 2.2. AOM2 Package Structure

The Archetype Object Model is defined by package `am.aom2` and subordinate packages:

```
am.aom2
├── archetype
├── constraint_model
│   ├── primitive
│   └── (constraint definitions)
├── definitions
├── rules
├── profile
├── persistence
└── terminology
```

### 2.3. Definition and Utility Classes

#### 2.3.1. Overview

Definitional constants used in AOM are defined in `aom2.definitions` package.

#### 2.3.2. Class Definitions

Various constants and utility functions support the archetype object model.

#### 2.3.3. ADL_CODE_DEFINITIONS Class

**Description:** Definitions relating to the internal code system of archetypes.

**Constants:**

| Constant | Value | Meaning |
|----------|-------|---------|
| Id_code_leader | "id" | Leader of identifier codes for archetype nodes |
| Value_code_leader | "at" | Leader of value codes for terminology items |
| Value_set_code_leader | "ac" | Leader of value set codes |
| Specialisation_separator | '.' | Separator for code specialisation levels |
| Code_regex_pattern | `(0\|[1-9][0-9]*)(\.(0\|[1-9][0-9]*))*` | Pattern for valid numeric code parts |
| Root_code_regex_pattern | `^id1(\.1)*$` | Pattern for archetype root id code |
| Primitive_node_id | "id9999" | Code id for `C_PRIMITIVE_OBJECT` nodes |

**Functions:**

| Function | Signature | Meaning |
|----------|-----------|---------|
| codes_conformant | `(a_child_code, a_parent_code: String): Boolean` | True if child code conforms to parent in specialisation |
| is_adl_code | `(a_code: String): Boolean` | True if code is any kind of ADL code |
| is_id_code | `(a_code: String): Boolean` | True if code is 'id' code |
| is_value_code | `(a_code: String): Boolean` | True if code is 'at' code |
| is_value_set_code | `(a_code: String): Boolean` | True if code is 'ac' code |
| is_redefined_code | `(a_code: String): Boolean` | True if code contains specialisation beyond level 0 |
| code_exists_at_level | `(a_code: String, a_level: Integer): Boolean` | True if code valid at specified level or less |

##### 2.3.3.1. Utility Algorithms

```
codes_conformant (a_child_code, a_parent_code: String): Boolean
    -- True if a_child_code conforms to a_parent_code in specialisation
    do
        Result := is_valid_code (a_child_code) and then 
            a_child_code.starts_with (a_parent_code) and then
            (a_child_code.count = a_parent_code.count or else
            a_child_code.item (a_parent_code.count + 1) = Specialisation_separator)
    end
```

---

## 3. The Archetype Package

### 3.1. Overview

The top-level archetype model defines standard structural representation of all archetype variants. Independently authored archetypes are instances of `AUTHORED_ARCHETYPE`, inheriting from both `AUTHORED_RESOURCE` (providing standardized descriptive metadata, language information, and annotations) and `ARCHETYPE` (defining core structure including definition, terminology, and optional rules).

The `AUTHORED_ARCHETYPE` class adds identifying attributes, flags, and descriptive metadata, with two specializations:

- `TEMPLATE`: Contains fillers/references (ADL `use_archetype` statements), typically representing data sets; may include template overlays
- `OPERATIONAL_TEMPLATE`: Fully flattened template form with all fillers and references substituted; includes merged terminologies from referenced archetypes

### 3.2. Archetype Identification

#### 3.2.1. Human-Readable Identifier (HRID)

All archetype variants have a human-readable, structured identifier defined by `ARCHETYPE_HRID` class, placing the artefact in a multi-dimensional space based on namespace, reference model class, and informational concept.

**HRID Components:**
- **namespace:** Reverse domain name identifier (optional)
- **rm_publisher:** Name of Reference Model publisher
- **rm_package:** Package containing the root class
- **rm_class:** Name of root class
- **concept_id:** Short concept name
- **release_version:** Full version (e.g., "1.8.2")
- **version_status:** Status indicator (released/""/rc/alpha/beta)
- **build_count:** Build count since last version increment

**Computed Forms:**
- **semantic_id():** Interface form down to major version
- **physical_id():** Complete version information
- **version_id():** Full version string (e.g., "1.8.2-rc.4")

For specialised archetypes, `_parent_archetype_id_` provides a string reference to the specialisation parent, typically in interface form or with full version numbers.

#### 3.2.2. Machine Identifiers

Two optional machine identifiers are defined:

**ARCHETYPE._uid_:** Machine identifier equivalent to `ARCHETYPE_HRID` up to major version, changing whenever the semantic identifier does. Useful for custodian organizations implementing this identifier.

**ARCHETYPE._build_uid_:** UUID provided for each change to:
- `ARCHETYPE._archetype_id_._release_version_`
- `ARCHETYPE._archetype_id_._build_count_`
- `ARCHETYPE._description_._lifecycle_state_`

Should be updated with each change in a controlled repository.

### 3.3. Top-level Meta-data

Meta-data items appearing in parentheses in the first line of ADL archetypes.

#### 3.3.1. ADL Version

The `ARCHETYPE._adl_version_` attribute indicates the version of the archetype formalism in which the archetype is expressed. The version number comes from the ADL specification amendment record, covering all synchronously updated archetype-related specifications.

#### 3.3.2. Reference Model Release

The `ARCHETYPE._rm_release_` attribute designates the release of the reference model on which the archetype is based. This can change with new archetype versions when re-versioning includes RM upgrade, provided basic archetype compatibility rules are maintained: later minor, patch versions and builds cannot create data invalid for prior versions.

Format: Semantic versioning 3-part form (e.g., "1.0.2")

This property does not indicate exclusive conformance to the named release, since most archetypes technically conform to multiple RM releases.

#### 3.3.3. Generated Flag

The `ARCHETYPE._is_generated_` flag indicates machine generation from another artefact (e.g., older ADL version). When true, tools know the archetype may be overwritten and another source is primary. Manual authoring should set this to false.

### 3.4. Governance Meta-data

Meta-data elements inherited from `AUTHORED_RESOURCE` provide natural language descriptions, authoring/translation details, use/misuse information, keywords, and resources. Three distinct meta-data categories exist: governance, authorship, and descriptive details.

#### 3.4.1. Governance Meta-data Items

Visible primarily in `RESOURCE_DESCRIPTION` class, consisting of management and intellectual property items.

##### 3.4.1.1. Package

The optional `_resource_package_uri_` property records a reference to a package of archetypes or other resources to which this archetype belongs, typically in the form "text <URL>".

##### 3.4.1.2. Lifecycle_state

The `_description_._lifecycle_state_` records the archetype's state in a defined lifecycle. The lifecycle state machine and versioning rules are explained in the openEHR Archetype Identification specification. The property value corresponds to macro-state names such as 'unmanaged', 'in_development', etc.

##### 3.4.1.3. Original_namespace and Original_publisher

These optional properties indicate the original publishing organization and its namespace. The `_original_namespace_` normally matches `_archetype_id.namespace_` unless the artefact has been forked, in which case `_archetype_id.namespace_` matches `_custodian_namespace_`.

##### 3.4.1.4. Custodian_namespace and Custodian_organisation

These optional properties state the formal namespace and human-readable organization identifier of the current custodian (maintainer/publisher), if applicable.

##### 3.4.1.5. Intellectual Property Items

Three properties relate to intellectual property:

**Licence:** String field for recording the licence under which the artefact may be used. Recommended format:
```
licence name <reliable URL to licence statement>
```

**Copyright:** Records copyright applying to the artefact, typically in form:
```
(c) name
(c) year name
(c) [UTF-8 ©] name
```

**Other IP Items:** Additional intellectual property considerations specific to the archetype context.

#### 3.4.2. Authorship Meta-data

Consists of author name, contributors, and translator information.

##### 3.4.2.1. Original Author

The `RESOURCE_DESCRIPTION._original_author_` property defines name/value pairs documenting the original author. Typical keys include "name", "organisation", "email", "date".

##### 3.4.2.2. Contributors

The `RESOURCE_DESCRIPTION._other_contributors_` property lists strings, one per contributor. Recommended format:
```
first names last name, organisation
first names last name, organisation <contributor email>
first names last name, organisation <organisation email>
```

##### 3.4.2.3. Languages and Translation

The `AUTHORED_RESOURCE._original_language_` and `TRANSLATION_DETAILS` class enable documentation of original authoring language and subsequent translation information. `TRANSLATION_DETAILS._author_` allows translator representation matching `_original_author_` format.

##### 3.4.2.4. Version_last_translated

The `_version_last_translated_` property records a copy of `_archetype_id.physical_id_` for each language when translation was performed. This enables maintainers to determine when new translations are needed. String property records full version identifier at last translation time.

#### 3.4.3. Descriptive Meta-data

Various descriptive metadata may be provided in multiple translations using `RESOURCE_DESCRIPTION_ITEM` class, with one instance per translation language.

##### 3.4.3.1. Purpose

The `_purpose_` item is a String property recording the intended design concept of the artefact.

##### 3.4.3.2. Use and Misuse

The `_use_` and `_misuse_` properties document specific uses and misuses. The latter typically relate to common errors or incorrect assumptions.

##### 3.4.3.3. Keywords

The `_keywords_` property is a String list recording search keywords for the artefact.

##### 3.4.3.4. Resources

The `_original_resource_uri_` property records references to resources in each particular language.

**TBD:** This property has not been widely used and may lack utility since resources are not typically available per language.

### 3.5. Structural Definition

#### 3.5.1. Common Structural Parts

The archetype definition is the main definitional part, represented as a `C_COMPLEX_OBJECT`. The root constraint structure always constrains a non-primitive object type.

The terminology section, represented by its own classes, enables archetypes to be natural language and terminology neutral.

Archetypes may include one or more rules—statements in predicate logic subset constraining multiple object parts. Rules are necessary for constraints referencing more than one attribute but unnecessary for single attribute/object constraints.

The annotations section, inherited from `AUTHORED_RESOURCE`, documents individual nodes within archetypes/templates and reference model data not constrained in the archetype but whose specific use needs documentation. Annotations are keyed by archetype or reference model paths.

#### 3.5.2. Structural Variants

The model defines structures for multiple archetype variants. All concrete instances inherit from `ARCHETYPE` descendants.

**Source Archetype:** Represented by differential form—expressing only changed or new elements relative to the flat parent structure.

**Flat Archetype:** Generated through flattening—applying specialised archetype overlays to flat parent structure and replacing internal references with expanded subtrees.

**Source Template:** Instance of `TEMPLATE` containing `C_ARCHETYPE_ROOT` objects representing slot fillers, each referring to external archetypes/templates or overlay archetypes.

**Template Overlay:** Instance of `TEMPLATE_OVERLAY` representing purely local template components with only definition and terminology. The definition structure is always a specialised overlay on something else. No slot fillers or external references permitted. No identifier, adl_version, languages or description required—these propagate from owning template.

**Operational Template:** Instance of `OPERATIONAL_TEMPLATE` created by composing referenced archetypes/templates and overlays in flattened form into a single composite archetype. Every archetype/template root node is represented using `C_ARCHETYPE_ROOT`. Includes `component_terminologies` property containing ontologies from all constituent archetypes, templates, and overlays.

### 3.6. Class Descriptions

#### 3.6.1. ARCHETYPE Class

**Description:** Abstract root class defining core formal archetype model. Includes basic identification information and structural connections from Archetype to constituent parts (definition as `C_COMPLEX_OBJECT`, terminology as `ARCHETYPE_TERMINOLOGY`, optional rules). Parent class of all concrete archetype types.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| parent_archetype_id | String | Specialisation parent archetype reference if applicable; may be interface identifier or full identifier |
| archetype_id | ARCHETYPE_HRID | Identifier of this archetype |
| is_differential | Boolean | Flag indicating differential or flat form; true for top-level source archetypes |
| definition | C_COMPLEX_OBJECT | Root constraint node of archetype definition |
| terminology | ARCHETYPE_TERMINOLOGY | Archetype terminology |
| rules | List<STATEMENT_SET> | Optional rules in first order predicate logic, typically referring to multiple attributes |
| rm_overlay | RM_OVERLAY | Optional reference model overlay |

**Functions:**

| Function | Returns | Meaning |
|----------|---------|---------|
| concept_code() | String | Root object `_node_id_`, standing for archetype concept |
| physical_paths() | List<String> | Language-independent paths from archetype; XPath-like syntax from alternations of `C_OBJECT._node_id_` and `C_ATTRIBUTE._rm_attribute_name_` |
| logical_paths(lang: String) | List<String> | Language-dependent paths; XPath-like syntax with `_node_ids_` replaced by terminology meanings |
| specialisation_depth() | Integer | Archetype specialisation depth; greater than 0 if has parent |
| is_specialised() | Boolean | True if archetype specialises another |

**Invariants:**

- *Invariant_concept_valid:* terminology.has_term_code(concept_code)
- *Invariant_specialisation_validity:* is_specialised implies specialisation_depth > 0

#### 3.6.2. AUTHORED_ARCHETYPE Class

**Description:** Root object of standalone, authored archetype including all metadata, description, other identifiers, and lifecycle information.

**Inherits:** `ARCHETYPE`, `AUTHORED_RESOURCE`

**Additional Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| adl_version | String | ADL version if archetype read from ADL sharable archetype |
| build_uid | UUID | Unique identifier of archetype instance; assigned each time content changes by tool |
| rm_release | String | Semver.org compatible release of most recent RM release on which current archetype version is based |
| is_generated | Boolean | If true, archetype was machine-generated; tools may overwrite; manual editing should set to false |
| other_meta_data | Hash<String, String> | Additional metadata |

**Invariants:**

- *Invariant_adl_version_validity:* valid_version_id(adl_version)
- *Invariant_rm_release:* valid_version_id(rm_release)
- *Description_validity:* description /= Void

#### 3.6.3. ARCHETYPE_HRID Class

**Description:** Human-readable structured identifier (HRID) for archetype or template.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| namespace | String | Reverse domain name namespace identifier (optional) |
| rm_publisher | String | Reference Model publisher name |
| rm_package | String | Package containing root class reachability graph |
| rm_class | String | Root class name |
| concept_id | String | Short concept name in multi-axial archetype_hrid |
| release_version | String | Full numeric version, e.g., "1.8.2" |
| version_status | VERSION_STATUS | Version status (released/""/rc/alpha/beta) |
| build_count | String | Build count since last version increment |

**Functions:**

| Function | Returns | Meaning |
|----------|---------|---------|
| semantic_id() | String | Interface form down to major version |
| physical_id() | String | Complete version information form |
| version_id() | String | Full version string, e.g., "1.8.2-rc.4" |
| major_version() | String | Major version from release_version |
| minor_version() | String | Minor version from release_version |
| patch_version() | String | Patch version from release_version |

**Invariants:**

- *Inv_rm_publisher_validity:* not rm_publisher.is_empty
- *Inv_rm_package_validity:* not rm_package.is_empty
- *Inv_class_name_validity:* not rm_class.is_empty
- *Inv_concept_id_validity:* not concept_id.is_empty
- *Inv_release_version_validity:* valid_version(release_version)

#### 3.6.4. TEMPLATE Class

**Description:** Source template—archetype that may include template overlays, may be restricted by tools to mandations, prohibitions, and restrictions on elements defined in flat parent.

**Inherits:** `AUTHORED_ARCHETYPE`

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| overlays | List<TEMPLATE_OVERLAY> | Overlay archetypes—partial archetypes with full definition/terminology but logically derived metadata from owning template |

**Invariants:**

- *Inv_is_specialised:* is_specialised

#### 3.6.5. TEMPLATE_OVERLAY Class

**Description:** Concrete bare `ARCHETYPE` form representing overlays in source template. Overlays have no metadata of their own; documentation derives from owning template.

**Inherits:** `ARCHETYPE`

**Invariants:**

- *Inv_is_specialised:* is_specialised

#### 3.6.6. OPERATIONAL_TEMPLATE Class

**Description:** Root object of operational template—derived from `TEMPLATE` definition and referenced archetypes/templates through flattening and potential removal of unneeded languages/terminologies. Used for generating and validating RM-canonical instance data and generating downstream artefacts including XML schemas, APIs, UI form definitions.

**Inherits:** `AUTHORED_ARCHETYPE`

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| component_terminologies | Hash<String, ARCHETYPE_TERMINOLOGY> | Compendium of flattened terminologies from referenced archetypes, keyed by archetype identifier |
| terminology_extracts | Hash<String, ARCHETYPE_TERMINOLOGY> | Compendium of flattened terminology extracts from referenced archetypes, keyed by archetype identifier |

**Functions:**

| Function | Returns | Meaning |
|----------|---------|---------|
| component_terminology(an_id: String) | ARCHETYPE_TERMINOLOGY | Retrieve component terminology by identifier |

**Invariants:**

- *Specialisation_validity:* is_specialised

### 3.7. Validity Rules

Validity rules apply to all `ARCHETYPE` variants and subtypes as follows:

**VARAV:** ADL version validity—`_adl_version_` must exist and consist of valid 3-part version identifier.

**VARRV:** RM release validity—`_rm_release_` must exist and consist of valid 3-part version identifier.

**VARCN:** Archetype concept validity—root `_node_id_` must be form "id1{.1}*" where ".1" count equals specialisation depth; must be defined in terminology.

**VATDF:** Value code validity—each value code (at-code) in archetype definition must be defined in flattened terminology `term_definitions`.

**VACDF:** Constraint code validity—each value set code (ac-code) in definition must be defined in terminology.

**VATDA:** Value set assumed value code validity—each at-code used as assumed_value must exist in value set definition.

**VETDF:** External term validity—each external term in definition must exist in relevant terminology (subject to tool accessibility).

**VOTM:** Terminology translations validity—translations must exist for `term_definitions` and `constraint_definitions` for all languages in description/translations sections.

**VOKU:** Object key unique—each keyed list item including description, terminology, annotations must have unique key among siblings.

**VARDT:** Archetype definition typename validity—outer block typename must match first archetype id segment typename.

**VRANP:** Annotation path valid—each annotation path must be either valid archetype path or reference model path for root class.

**VRRLP:** Rule path valid—each rule path must be found within archetype or be RM-valid extension of path found within archetype.

**For ARCHETYPE subtypes (excluding TEMPLATE_OVERLAY):**

**VARID:** Archetype identifier validity—archetype must have identifier conforming to openEHR archetype identification specification.

**VDEOL:** Original language specified—archetype must have `original_language` section with authoring language metadata.

**VARD:** Description specified—archetype must have `description` section with main metadata.

**For specialised archetypes (is_specialised = true):**

**VASID:** Archetype specialisation parent identifier validity—specialise clause identifier must be immediate parent archetype identifier.

**VALC:** Archetype language conformance—specialised archetype languages must be same as or subset of flat parent languages.

**VACSD:** Archetype concept specialisation depth—archetype specialisation depth must be one greater than parent depth.

**VATCD:** Archetype code specialisation level validity—each at-code and ac-code in definition must have specialisation level no greater than archetype specialisation level.

**For TEMPLATE instances:**

**VTPL:** Template and filler language consistency—all slot fillers and external reference archetypes must contain template's `_original_language_` in their languages for successful flattening.

---

## 4. Constraint Model Package

### 4.1. Overview

The constraint model expresses semantics of constraints on instances of classes described in orthodox object-oriented formalism (e.g., UML). Major abstractions correspond to object-oriented abstractions, including various 'object' notions and 'attribute' notion.

The definition part of an archetype is a `C_COMPLEX_OBJECT` consisting of alternate layers of object and attribute constrainer nodes. Terminal nodes constrain primitive types. Additional node types represent internal references, constraint references to terminology binding, and archetype constraints on external archetypes.

**Concrete Node Types:**

- `C_COMPLEX_OBJECT`: Interior node constraining non-primitive type instances (e.g., OBSERVATION, SECTION)
- `C_ATTRIBUTE`: Node constraining an attribute (relationship or primitive attribute)
- `C_PRIMITIVE_OBJECT`: Node constraining primitive (built-in) type instances
- `C_COMPLEX_OBJECT_PROXY`: Reference to previously defined `C_COMPLEX_OBJECT` using path
- `ARCHETYPE_SLOT`: Node whose statements define which other archetypes can appear; logically similar to `C_COMPLEX_OBJECT` but constraints expressed in different archetype
- `C_ARCHETYPE_ROOT`: Represents external archetype root node reference; enables another archetype reference from current one; used in archetypes and templates

Constraints define which reference model class instance configurations conform to the archetype. Optionality, cardinality, and other choices allow a single archetype to correspond to a set of similar configurations.

### 4.2. Semantics

#### 4.2.1. All Node Types

Some properties are defined for all node types.

##### 4.2.1.1. Path Functions

The `path()` function computes the path to the current node from archetype root. The `has_path()` function indicates whether a given path can be found in an archetype.

##### 4.2.1.2. Conformance Functions

All node types include two functions formalizing specialised archetype conformance to parent archetype. Both functions take a corresponding parent node argument. A 'corresponding' node is found at the same or congruent path. A congruent path is one where one or more at-codes have been redefined in the specialised archetype.

The `_c_conforms_to_()` function returns true if the calling node is a valid specialisation of the 'other' node. The `_c_congruent_to_()` function returns true if the calling node is the same as the other node except for possibly redefined at-codes.

##### 4.2.1.3. Any_allowed

The `_any_allowed_()` function on some node types indicates that any reference model-permitted value is allowed by the archetype, enabling simple expression of completely "open" constraints without further substructure.

#### 4.2.2. Attribute Nodes

Constraints on reference model attributes, including computed attributes (functions with no arguments), are represented by `C_ATTRIBUTE` instances. Expressible constraints include:

- `_is_multiple_`: Flag indicating whether the `C_ATTRIBUTE` constrains multiply-valued (container) or single-valued RM attribute
- `_existence_`: Whether corresponding instance must exist
- **Child objects:** Representing allowable attribute values

For single-valued attributes (e.g., Person.date_of_birth), children represent alternative object constraints.

For multiply-valued attributes (e.g., Person.contacts: List<Contact>), a cardinality constraint on the container can be defined. Child object constraints remain similar except multiple alternatives can co-exist.

Both `_existence_` and `_cardinality_` may appear in `C_ATTRIBUTE`:

- `_existence_`: Indicates whether object will be found in given attribute field
- `_cardinality_`: Indicates valid container membership; only for containers (List<T>, Set<T>, etc.)

When both used, existence states whether container exists, while cardinality states how many items are in container and whether it acts logically as list, set, or bag. Both are optional, overriding reference model settings only when needed.

#### 4.2.3. Object Node Types

The following sections apply to all object nodes (descendants of `C_OBJECT`).

##### 4.2.3.1. Rm_type_name and Reference Model Type Matching

Every object node has an `_rm_type_name_` attribute stating the RM type to be matched. The value is understood as a constraint on dynamic type of data instances of the stated Reference Model type. It is either a class name from the RM or a generic type constructed from RM class names.

The RM type stated in an archetype object node is understood as a static type constraint. It matches instances of any RM subtype of the stated type, as long as inheritance relationship is stated in RM definition. This holds for both sub-classes and generic type subtypes in covariant fashion:

- `_rm_type_name_` = "PARTY" matches PERSON, where PERSON inherits from PARTY
- `_rm_type_name_` = "Interval<Ordered>" matches Interval<Quantity>, SimpleInterval<Ordered>, SimpleInterval<Quantity> where Quantity inherits from Ordered and SimpleInterval inherits from Interval

Special rules apply to primitive type matching enabling 'logical' primitive type names in archetypes to match multiple 'concrete' variants in some reference models and programming type systems.

##### 4.2.3.2. Node_id and Paths

The `_node_id_` attribute in `C_OBJECT` is of key importance. It serves two functions:

- Allows individual identification of archetype object constraint nodes, guaranteeing sibling unique identification
- Provides a code to which human understanding terminology definition can be attached, plus potentially terminology binding

Node identifiers allow archetype paths to be created referencing each node. Every archetype node needs a `_node_id_`. Only `_node_ids_` for nodes under container attributes must have terminology definitions. For single-valued attribute nodes, terminology definition is optional (typically not supplied), since meaning comes from reference model attribute definition.

Note: `C_PRIMITIVE_OBJECT` instances have constant `_node_id_`, not requiring explicit node identifier supply in syntax or serial forms converted to AOM structural form.

##### 4.2.3.3. Sibling Ordering

Within specialised archetypes, redefined or added object nodes may be defined under container attributes. Since specialised archetypes are in differential form (only redefined/added nodes expressed, not inherited unchanged nodes), relative ordering cannot be stated simply by ordering within differential form lists. Explicit ordering indicator is required if order is specific. The `C_OBJECT._sibling_order_` attribute provides this. It can only be set on `C_OBJECT` descendants within multiply-valued attributes (instances of `C_ATTRIBUTE` where `_cardinality_` is ordered).

##### 4.2.3.4. Node Deprecation

Any defined node type instance may be marked as deprecated, indicating preference against use and existence of alternative solution for same information recording. Rules/recommendations for deprecation handling are outside archetype scope, provided by archetype governance framework.

#### 4.2.4. Reference Objects

Two `C_OBJECT` subtypes express constraints as references to other constraints rather than directly:

**ARCHETYPE_SLOT:** Defines a 'slot' specifying other archetypes pluggable at that point, expressed in terms of archetype identifier constraints using `ARCHETYPE_ID_CONSTRAINT` class instances (specialized ELOM `EL_CONSTRAINT_EXPRESSION`).

**C_COMPLEX_OBJECT_PROXY:** Represents reference to another current archetype part expressing exactly needed constraints at proxy appearance point.

#### 4.2.5. Defined Object Nodes (C_DEFINED_OBJECT)

The `C_DEFINED_OBJECT` subtype corresponds to `C_OBJECTs` defined in archetype by value (inline definition). Four properties characterize `C_DEFINED_OBJECTs`:

##### 4.2.5.1. Valid_value

The `_valid_value_` property enables specification of a specific value that data conforming to the archetype must possess. When present, the value constrains data to exactly this value.

##### 4.2.5.2. Prototype_value

The `_prototype_value_` property provides a prototype or template value instance, useful for documentation, instantiation, and default value generation. Unlike `_valid_value_`, it does not constrain data to that value but provides exemplification.

##### 4.2.5.3. Default_value

The `_default_value_` property specifies a value to use when data value is not provided during instantiation. It enables default population of data structures.

#### 4.2.6. Complex Objects (C_COMPLEX_OBJECT)

`C_COMPLEX_OBJECT` represents constraints on non-primitive object types. It contains a list of `C_ATTRIBUTE` children, each constraining a different object attribute.

#### 4.2.7. Primitive Types (C_PRIMITIVE_OBJECT descendants)

Descendant classes constrain specific primitive types including strings, numbers, dates/times, and terminology codes.

##### 4.2.7.1. Assumed_value

The `_assumed_value_` property provides a value to assume for a primitive type if no explicit value is given. It serves documentation and validation purposes.

#### 4.2.8. Terminology Constraints

##### 4.2.8.1. Formal Definition

Terminology constraints are specified through value set references and individual code constraints.

##### 4.2.8.2. Constraint Strengths

Constraint strength indicates whether terminology constraints are mandatory or optional.

##### 4.2.8.3. Terminology Code Resolution

Terminology codes are resolved to their meanings during processing.

#### 4.2.9. Date/Time Constraints

Constraints on Date, Time, and DateTime types are specified using pattern and interval mechanisms.

#### 4.2.10. Duration Constraints

Constraints on Duration types specify allowed ranges and patterns.

#### 4.2.11. Constraints on Enumeration Types

Constraints can be applied to enumeration types through value restrictions.

### 4.3. Second Order Constraints

#### 4.3.1. Tuple Constraints

Tuple constraints enable co-varying attribute constraints, useful for related attributes such as quantity value and unit.

#### 4.3.2. Assertions

Assertions express complex constraints on multiple attributes using predicate logic.

### 4.4. AOM Type Substitutions

AOM supports type substitution rules enabling primitive type abstraction.

### 4.5. Class Definitions

#### 4.5.1. ARCHETYPE_CONSTRAINT Class

**Description:** Abstract parent class for all constraint nodes in archetype definition.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| parent | ARCHETYPE_CONSTRAINT | Parent node in constraint tree |
| validation_status | CONSTRAINT_STATUS | Optional status flag for constraint validation |
| annotations | Hash<String, ANNOTATION_ITEMS> | Optional annotation items keyed by path |

#### 4.5.2. C_ATTRIBUTE Class

**Description:** Represents constraint on reference model attribute (relationship or primitive attribute).

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| rm_attribute_name | String | Name of constrained RM attribute |
| is_multiple | Boolean | True if constraining multiply-valued (container) attribute |
| existence | EXISTENCE | Optional; constraint on whether attribute must exist |
| cardinality | CARDINALITY | Optional; multiplicity constraint for container attributes |
| children | List<C_OBJECT> | Constraint nodes for attribute values |
| rm_visible | Boolean | If false, constrains visibility of RM attribute in resulting data |
| redefined_at_parent_path | String | Optional; path to constraining parent attribute in parent archetype |

**Functions:**

| Function | Signature | Meaning |
|----------|-----------|---------|
| any_allowed | (): Boolean | True if any RM-permitted value is allowed |
| has_children | (): Boolean | True if children list is non-empty |
| child_count | (): Integer | Count of child constraint nodes |

##### 4.5.2.1. Conformance Semantics: C_ATTRIBUTE

The conformance function `_c_conforms_to_(other: C_ATTRIBUTE): Boolean` determines if calling attribute conforms to parent attribute. Requirements:

- Calling attribute's `_rm_attribute_name_` must equal parent's
- Calling attribute's `_is_multiple_` must equal parent's
- Calling existence must be equal or more restrictive
- Calling cardinality must be equal or more restrictive
- Each calling child must have conforming correspondence in parent
- Calling `_redefined_at_parent_path_` must be valid path to parent's parent attribute

The `_collective_occurrences_()` function computes possible occurrences of children when one child has multiple occurrences:

```
collective_occurrences(): Multiplicity_interval
    Result.lower = sum of minimums from child.occurrences
    Result.upper = sum of maximums from child.occurrences (or unbounded)
```

##### 4.5.2.2. Validity Rules: C_ATTRIBUTE

**VSONCO:** Sibling node occurrences validity. When a `C_OBJECT` node in container attribute has multiple occurrences, `_collective_occurrences_()` of all siblings must be valid.

**VSONI:** Sibling node identifiers unique. All child `_node_ids_` must be unique within `C_ATTRIBUTE`.

**VSONIR:** Sibling node id redefinition. In specialised archetype, if sibling node has same `_node_id_` as parent's, it must represent redefinition of that node.

#### 4.5.3. C_OBJECT Class

**Description:** Abstract parent class for all object constraint nodes.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| node_id | String | Identifier for object node; guarantees sibling uniqueness |
| rm_type_name | String | Name of constrained reference model type |
| occurrences | MULTIPLICITY_INTERVAL | Optional; constraint on how many times object can occur |
| sibling_order | SIBLING_ORDER | Optional; explicit ordering indicator for siblings in container attributes |
| is_deprecated | Boolean | Optional; true indicates node is deprecated |
| constraint_status | CONSTRAINT_STATUS | Optional; status of constraint specification |

#### 4.5.4. SIBLING_ORDER Class

**Description:** Provides explicit ordering control for siblings in ordered container attributes.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| is_before | String | Optional; node_id of sibling this node should appear before |
| is_after | String | Optional; node_id of sibling this node should appear after |

##### 4.5.4.1. Occurrences inferencing rules

When `_occurrences_` not specified, inferencing rules determine effective occurrences based on attribute properties and parent occurrences.

##### 4.5.4.2. Conformance Semantics: C_OBJECT

The `_c_conforms_to_(other: C_OBJECT): Boolean` function determines node conformance. Requirements:

- `_rm_type_name_` must be equal or subtype of parent's
- `_node_id_` must be equal or redefinition of parent's
- `_occurrences_` must be equal or more restrictive
- Node-specific properties must conform (see subclass specifications)

The `_c_congruent_to_(other: C_OBJECT): Boolean` function returns true if nodes are congruent (same except possibly redefined at-codes).

##### 4.5.4.3. Validity Rules: C_OBJECT

**VSONI:** Sibling identifiers unique within parent `C_ATTRIBUTE`.

**VSON:** Reference model type name validity; must exist in reference model.

**VSONPO:** Specialised archetype object node prohibited occurrences validity. In specialised archetype, if object node has `occurrences` set to prohibited (0..0), parent must allow optional occurrences.

**VSONPT:** Specialised archetype object node occurrence type validity. In specialised archetype, if parent object has multiple occurrences, specialised child's occurrences must be compatible.

#### 4.5.5. C_DEFINED_OBJECT Class

**Description:** Abstract parent class for `C_OBJECTs` defined by value (inline).

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| valid_value | Object | Optional; exact value data must possess |
| prototype_value | Object | Optional; prototype/template value for instantiation |
| default_value | Object | Optional; default value for unspecified data |

#### 4.5.6. C_COMPLEX_OBJECT Class

**Description:** Constraint on non-primitive reference model type instances.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| attributes | List<C_ATTRIBUTE> | Constraints on object attributes |
| attribute_tuples | List<C_ATTRIBUTE_TUPLE> | Optional; tuple constraints on multiple attributes |

**Functions:**

| Function | Signature | Meaning |
|----------|-----------|---------|
| any_allowed | (): Boolean | True if any RM-permitted value allowed |

##### 4.5.6.1. Validity Rules: C_COMPLEX_OBJECT

**VSONT:** Definition specialisation validity. In specialised archetype, if parent is `C_COMPLEX_OBJECT` and child is `C_PRIMITIVE_OBJECT`, specialisation is invalid.

#### 4.5.7. C_ARCHETYPE_ROOT Class

**Description:** Represents constraint allowing external archetype reference.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| archetype_ref | String | Reference to external archetype identifier |
| is_prohibited | Boolean | Optional; true if this archetype reference is prohibited |

##### 4.5.7.1. Validity Rules: C_ARCHETYPE_ROOT

**VCARD:** Archetype cardinality valid. Cardinality occurrence inference rules must yield valid occurrences.

#### 4.5.8. ARCHETYPE_SLOT Class

**Description:** Constraint node defining which other archetypes can appear at slot point.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| slot_constraints | List<EXPR_ARCHETYPE_ID_CONSTRAINT> | Constraints on archetype identifiers allowed in slot |

**Functions:**

| Function | Signature | Meaning |
|----------|-----------|---------|
| any_allowed | (): Boolean | True if any archetype allowed |

##### 4.5.8.1. Validity Rules: ARCHETYPE_SLOT

**VCARD:** Archetype slot cardinality valid. Cardinality occurrence inference rules must yield valid occurrences.

#### 4.5.9. C_COMPLEX_OBJECT_PROXY Class

**Description:** Reference to previously defined `C_COMPLEX_OBJECT` within same archetype.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| target_path | String | Path to referenced node in same archetype |

##### 4.5.9.1. Validity Rules: C_COMPLEX_OBJECT_PROXY

**VORP:** Object reference path validity. Referenced path must exist in archetype definition.

#### 4.5.10. C_PRIMITIVE_OBJECT Class

**Description:** Abstract parent class for constraints on primitive types.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| assumed_value | Comparable | Optional; value to assume if not explicitly given |
| item | C_PRIMITIVE_OBJECT_ITEM | Optional; constraint item for primitive |

##### 4.5.10.1. Validity Rules: C_PRIMITIVE_OBJECT

**VPRIM:** Primitive constraint validity. Constraint must be consistent with constrained type.

##### 4.5.10.2. Conformance Semantics: C_PRIMITIVE_OBJECT

The `_c_conforms_to_(other: C_PRIMITIVE_OBJECT): Boolean` function checks that calling primitive constraint is valid specialisation.

The `_c_value_conforms_to_(other: C_PRIMITIVE_OBJECT): Boolean` function checks that value constraints conform.

#### 4.5.11. C_BOOLEAN Class

**Description:** Constraint on Boolean type.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| true_valid | Boolean | Optional; true if true values allowed |
| false_valid | Boolean | Optional; true if false values allowed |

##### 4.5.11.1. Conformance semantics: C_BOOLEAN

Conformance requires that calling constraint's valid values be subset of parent's.

#### 4.5.12. C_STRING Class

**Description:** Constraint on String type.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| pattern | String | Optional; regex pattern string must match |
| is_pattern | Boolean | Optional; true if pattern is regex |
| list_values | List<String> | Optional; list of permitted values |

##### 4.5.12.1. Conformance semantics: C_STRING

Conformance requires calling constraint values be subset of parent's.

#### 4.5.13. C_ORDERED Class

**Description:** Abstract parent class for ordered constraints on numeric and temporal types.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| list_value | List<Comparable> | Optional; list of allowed discrete values |

##### 4.5.13.1. Conformance semantics: C_ORDERED

Conformance requires calling constraint values be subset of parent's.

#### 4.5.14. C_INTEGER Class

**Description:** Constraint on Integer type.

**Inherits:** `C_ORDERED`

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| range | List<Interval<Integer>> | Optional; list of permitted integer ranges |

#### 4.5.15. C_REAL Class

**Description:** Constraint on Real type.

**Inherits:** `C_ORDERED`

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| range | List<Interval<Real>> | Optional; list of permitted real ranges |

#### 4.5.16. C_TEMPORAL Class

**Description:** Abstract parent class for temporal type constraints.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| pattern_constraint | List<TEMPORAL_CONSTRAINT> | Optional; pattern constraints on temporal values |
| range_constraint | LIST<Interval<Comparable>> | Optional; interval constraints on temporal values |

#### 4.5.17. C_TEMPORAL_DEFINITIONS Class

**Description:** Provides pattern definitions and constraint patterns for temporal types.

**Constants:**

Patterns include ISO 8601 patterns with variable precision.

##### 4.5.17.1. Conformance semantics: C_TEMPORAL

Conformance requires calling constraint patterns/ranges be subset of parent's.

#### 4.5.18. C_DATE Class

**Description:** Constraint on Date type.

**Inherits:** `C_TEMPORAL`

#### 4.5.19. C_TIME Class

**Description:** Constraint on Time type.

**Inherits:** `C_TEMPORAL`

#### 4.5.20. C_DATE_TIME Class

**Description:** Constraint on DateTime type.

**Inherits:** `C_TEMPORAL`

#### 4.5.21. C_DURATION Class

**Description:** Constraint on Duration type.

**Inherits:** `C_TEMPORAL`

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| range_constraint | List<Interval<Duration>> | Optional; duration range constraints |

#### 4.5.22. C_TERMINOLOGY_CODE Class

**Description:** Constraint on terminology codes with value set references.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| terminology_id | String | Optional; external terminology identifier |
| constraint_status | CONSTRAINT_STATUS | Optional; mandatory/optional constraint indicator |
| code_list | List<String> | Optional; specific allowed codes |
| value_set_codes | List<String> | Optional; value set code references (ac-codes) |

#### 4.5.23. CONSTRAINT_STATUS Enumeration

**Values:**

- required
- optional

##### 4.5.23.1. Conformance semantics: C_TERMINOLOGY_NODE

Conformance requires calling code constraints be subset of parent's.

#### 4.5.24. C_SECOND_ORDER Class

**Description:** Abstract parent class for second-order constraints (tuple constraints, assertions).

#### 4.5.25. C_PRIMITIVE_TUPLE Class

**Description:** Tuple constraint specifying co-varying primitive values.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| members | List<C_PRIMITIVE_OBJECT> | Tuple member constraints |

#### 4.5.26. C_ATTRIBUTE_TUPLE Class

**Description:** Tuple constraint specifying co-varying attributes.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| members | List<String> | Attribute names in tuple |
| value_constraint | List<C_PRIMITIVE_TUPLE> | Constraints on value combinations |

##### 4.5.26.1. Conformance semantics: C_SECOND_ORDER

Conformance requires calling second-order constraints be subset of parent's.

---

## 5. The Rules Package

### 5.1. Archetype Slot Assertions

Assertions in archetype slots define which external archetypes are permitted.

### 5.2. Archetype Rules

Rules define complex constraints on multiple attributes using predicate logic expressions.

### 5.3. Class Descriptions

#### 5.3.1. EXPR_CONSTRAINT Class

**Description:** Expression-based constraint used in archetype slots and rules.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| constraint_expression | STRING | Predicate logic expression |

#### 5.3.2. EXPR_ARCHETYPE_ID_CONSTRAINT Class

**Description:** Expression constraint on archetype identifiers.

**Inherits:** `EXPR_CONSTRAINT`

#### 5.3.3. EXPR_ARCHETYPE_REF Class

**Description:** Expression reference to archetype within constraint.

---

## 6. The RM Overlay Package

### 6.1. Overview

The RM Overlay package provides facilities for controlling visibility and naming of reference model attributes in archetype definitions.

### 6.2. Semantics

#### 6.2.1. RM Attribute Visibility

Controls which reference model attributes are visible/hidden in archetype-constrained data.

##### 6.2.1.1. Validity

Visibility rules must not hide mandatory attributes or create invalid states.

### 6.3. Class Descriptions

#### 6.3.1. RM_OVERLAY Class

**Description:** Top-level container for RM overlay declarations.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| visibility_declarations | List<RM_ATTRIBUTE_VISIBILITY> | Visibility control declarations |

#### 6.3.2. RM_ATTRIBUTE_VISIBILITY Class

**Description:** Declares visibility control for specific RM attribute.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| rm_attribute_path | String | Path to RM attribute |
| visibility | VISIBILITY_TYPE | Visibility control value |
| attribute_alias | String | Optional; alias for attribute |

#### 6.3.3. VISIBILITY_TYPE Enumeration

**Values:**

- visible
- hidden

---

## 7. Terminology Package

### 7.1. Overview

The terminology package represents archetype terminology, enabling language and terminology neutral archetypes through mappings between internal codes and natural language terms and external terminology bindings.

### 7.2. Semantics

#### 7.2.1. Specialisation Depth

Specialisation depth indicates the level of specialisation, enabling validation of codes in specialised archetypes.

### 7.3. Class Descriptions

#### 7.3.1. ARCHETYPE_TERMINOLOGY Class

**Description:** Container for archetype terminology definitions.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| original_language | String | Language of original authoring |
| term_definitions | Hash<String, List<ARCHETYPE_TERM>> | Terms keyed by language |
| term_bindings | Hash<String, List<TERM_BINDING>> | External terminology bindings |
| value_sets | List<VALUE_SET> | Value set definitions |
| constraint_definitions | Hash<String, List<CONSTRAINT_BINDING>> | Constraint bindings |

#### 7.3.2. TERMINOLOGY_RELATION Class

**Description:** Defines relationships between terminology items.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| relation_type | String | Type of relationship |
| source_term | String | Source term code |
| target_term | String | Target term code |

#### 7.3.3. VALUE_SET Class

**Description:** Defines a set of permitted terminology values.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| id | String | Value set identifier (ac-code) |
| members | List<String> | Member codes (at-codes) |

#### 7.3.4. ARCHETYPE_TERM Class

**Description:** Single terminology term definition.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| code | String | Term code (id/at/ac-code) |
| text | String | Natural language text |
| description | String | Optional; detailed description |
| comment | String | Optional; usage comment |

##### 7.3.4.1. Validity Rules

**VTDT:** Term definitions validity. All codes used in definition must be defined in term_definitions.

**VVSC:** Value set code membership. All codes in value_set member lists must be defined in term_definitions.

---

## 8. Validation and Transformation Semantics

### 8.1. Validation

Validation occurs in multiple phases.

#### 8.1.1. Phase 1 - Basic Integrity

Basic structural and semantic integrity checks.

##### 8.1.1.1. Basic checks

Verify essential properties exist and are correctly typed.

##### 8.1.1.2. AUTHORED_ARCHETYPE meta-data checks

Verify metadata completeness and validity.

##### 8.1.1.3. Definition Structure Validation

Verify archetype definition structure conforms to model rules.

##### 8.1.1.4. Basic Terminology Validation

Verify terminology structure and internal consistency.

##### 8.1.1.5. Various Structure Validation

Check specific structural elements.

##### 8.1.1.6. Code Validation

Verify all codes are valid and properly formatted.

##### 8.1.1.7. Validate Annotations

Verify annotation paths and content.

#### 8.1.2. Phase 2 - Validation of Specialised Archetype Against Flat Parent

##### 8.1.2.1. Validate Against Reference Model

Verify types and attributes exist in RM.

##### 8.1.2.2. Validate Specialised Definition

Verify specialised definition conforms to parent.

##### 8.1.2.3. Validate Rules

Verify rules syntax and path validity.

#### 8.1.3. Phase 3 - Validation of Flat Form

Verify flattened archetype is valid standalone archetype.

### 8.2. Flattening

Flattening is the process of creating a complete, non-differential archetype representation by merging specialised overlays with the flat parent structure.

### 8.3. Diffing

Diffing computes differences between archetype versions to support version management and update generation.

---

## 9. Serialisation Model

### 9.1. Overview

The serialisation model describes transformation between AOM structures and serial formats (ADL, XML, etc.).

### 9.2. Model Transformation Description

Transformation rules map between AOM classes and serial format representations.

---

## 10. Templates

### 10.1. Overview

Templates are specialized archetypes designed to represent specific data sets by combining constraints from multiple archetypes and defining localizations through template overlays.

### 10.2. An Example

A blood pressure template might reference a blood pressure observation archetype and specify mandatory fields, define units, and provide local terminology.

### 10.3. Template Identifiers

Templates use the standard ARCHETYPE_HRID identifier system, distinguished by semantic identifiers and optionally by template designation in metadata.

---

## 11. Reference Model Adaptation

### 11.1. Overview

Reference model adaptation enables archetypes to work with multiple RM versions and implementations through profile configuration.

### 11.2. AOM Profile Configuration

Configuration enables mapping between AOM and specific reference model implementations.

#### 11.2.1. Class Definitions

##### 11.2.1.1. AOM_PROFILE Class

**Description:** Configuration profile for AOM-to-RM mapping.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| rm_publisher | String | Reference model publisher identifier |
| rm_release | String | Reference model release version |
| type_mappings | List<AOM_TYPE_MAPPING> | Type mappings |
| property_mappings | List<AOM_PROPERTY_MAPPING> | Property mappings |
| primitive_type_equivalences | Hash<String, List<String>> | Logical-to-concrete primitive type mappings |
| lifecycle_state_mappings | Hash<String, String> | AOM-to-RM lifecycle state mappings |
| archetype_parent_class | String | Default parent class for archetypes |
| archetype_data_value_parent_class | String | Parent class for data value archetypes |
| archetype_visualise_descendants_of | String | Class for descendant visualization |
| archetype_namespace | String | Default archetype namespace |

##### 11.2.1.2. AOM_TYPE_MAPPING Class

**Description:** Maps AOM types to reference model types.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| aom_type | String | AOM type name |
| rm_type | String | Corresponding RM type name |

##### 11.2.1.3. AOM_PROPERTY_MAPPING Class

**Description:** Maps AOM properties to RM properties.

**Attributes:**

| Attribute | Type | Meaning |
|-----------|------|---------|
| aom_property | String | AOM property name |
| rm_property | String | Corresponding RM property name |

#### 11.2.2. Configuration File

Configuration is typically provided in YAML or XML format specifying all mappings and settings.

### 11.3. Mapping RM Entities to AOM Entities

Mapping rules describe correspondence between RM classes/properties and AOM constrainers.

### 11.4. RM Primitive Type Equivalences

Many reference models provide multiple concrete primitive types for logical concepts. Equivalences enable archetypes to work with all variants.

**Example:** A String logical type might map to `String`, `ShortString`, `TextString` in RM.

### 11.5. RM Type Substitutions

Type substitution rules enable substitution of subtypes in specialised archetypes.

### 11.6. AOM Lifecycle State Mappings

Maps AOM lifecycle states to RM-specific representations.

### 11.7. Facilities for RM Visualisation

Metadata attributes guide visualization of RM structures.

#### 11.7.1. archetype_parent_class

Specifies default parent class for new archetypes.

#### 11.7.2. archetype_data_value_parent_class

Specifies parent class for data value archetypes (e.g., quantities).

#### 11.7.3. archetype_visualise_descendants_of

Specifies class whose descendants should be visualized in archetype tooling.

#### 11.7.4. archetype_namespace

Specifies default namespace for archetypes in profile's RM context.

---

## References

**[ISO 13606]** ISO/IEC 13606: Health informatics - EHR communication

**[Beale 2000]** Beale, T. (2000). Archetypes: Constraint-based domain models for future-proof information systems.

**[Beale 2002]** Beale, T. (2002). Ontologies and Archetypes for Portable Electronic Health Records.

**[openEHR AM]** openEHR Specifications: Archetype Model https://specifications.openehr.org/releases/AM/latest/

**[openEHR ADL2]** openEHR Archetype Definition Language 2 Specification

**[openEHR BASE]** openEHR BASE Component Specifications https://specifications.openehr.org/releases/BASE/latest/

**[semver.org]** Semantic Versioning https://semver.org/

---

**End of Document**
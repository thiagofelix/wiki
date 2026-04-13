# Archetype Technology Overview

## Table of Contents

- [Archetype Technology Overview](#archetype-technology-overview)
  - [Amendment Record](#amendment-record)
  - [Acknowledgements](#acknowledgements)
    - [Primary Author](#primary-author)
    - [Support](#support)
    - [Trademarks](#trademarks)
  - [1. Business Purpose of Archetypes](#1-business-purpose-of-archetypes)
  - [2. Archetype Formalism Overview](#2-archetype-formalism-overview)
  - [3. The Specifications](#3-the-specifications)
  - [4. Semantic Overview](#4-semantic-overview)
    - [4.1. Identification and the Virtual Archetype Space](#41-identification-and-the-virtual-archetype-space)
    - [4.2. Collections of Archetypes](#42-collections-of-archetypes)
    - [4.3. Archetype Relationships](#43-archetype-relationships)
      - [4.3.1. Archetype Specialisation](#431-archetype-specialisation)
      - [4.3.2. Archetype Composition](#432-archetype-composition)
    - [4.4. Archetype Internals](#44-archetype-internals)
      - [4.4.1. Archetype Definition Language (ADL)](#441-archetype-definition-language-adl)
    - [4.5. Templates](#45-templates)
  - [5. Artefacts](#5-artefacts)
    - [5.1. Model / Syntax Relationship](#51-model--syntax-relationship)
    - [5.2. The Development Process](#52-the-development-process)
    - [5.3. Compilation](#53-compilation)
    - [5.4. Optimisations](#54-optimisations)
  - [References](#references)

---

## Document Metadata

**Issuer:** openEHR Specification Program

**Release:** AM Release-2.3.0

**Status:** STABLE

**Keywords:** archetype, identification, governance, openehr

**Copyright:** © 2014 - 2024 The openEHR Foundation

**Licence:** Creative Commons Attribution-NoDerivs 3.0 Unported

**Support:**
- Issues: Problem Reports
- Web: specifications.openEHR.org

**Source:** https://specifications.openehr.org/releases/AM/latest/Overview.html

---

## Amendment Record

| Issue | Details | Raiser, Implementer | Completed |
|-------|---------|-------------------|-----------|
| AM Release 2.3.0 | 0.9.4: Convert citations to bibtex form. | T Beale | 15 Dec 2019 |
| AM Release 2.2.0 | (no changes listed) | — | — |
| AM Release 2.1.0 | (no changes listed) | — | — |
| AM Release 2.0.6 | 0.9.3: Added diagrams and improved text in Introduction section. | T Beale | 18 Apr 2016 |
| — | 0.9.2: Correct Fowler reference to 1997. | T Beale | 30 Mar 2016 |
| — | 0.9.1: Minor refinements to text in first section; new version of Fig 1. | T Beale | 12 Nov 2015 |
| — | 0.9.0: Addition of sections on business purpose, identifiers and collections. | T Beale | 10 Jun 2015 |
| — | 0.8.0: Initial writing; taken from overview material of ADL, AOM and template specifications. | T Beale | 10 Oct 2014 |

---

## Acknowledgements

### Primary Author

- Thomas Beale, Ars Semantica, UK; openEHR International Board

### Support

The work reported in this document has been funded by:

- The openEHR Industry Partners
- Ocean Informatics

### Trademarks

- 'Microsoft' and '.Net' are trademarks of the Microsoft Corporation
- 'openEHR' is a registered trademark of The openEHR Foundation
- 'SNOMED CT' is a registered trademark of IHTSDO

---

## 1. Business Purpose of Archetypes

Archetypes function as a mechanism for introducing domain semantics into information models without causing the models themselves to grow indefinitely through accumulating domain-specific details.

### The Domain-Model Distinction

To illustrate, consider e-health systems. Established information models from openEHR, ISO 13606-1, HL7 CDA and similar organizations employ a multi-layered approach separating the foundational information model from a semantic layer expressing domain knowledge. Information models typically define:

- **Clinical data types:** Quantity (with units and accuracy), Coded text, Ordinal (integer/symbol pairing)
- **Generic clinical data structures:** Entry, clinical document, report
- **Infrastructure types:** identification, versioning

Such a model may contain 50-100 classes (including 30+ for clinical data types), enabling construction of instance structures for clinical encounter notes or hospital discharge summaries.

### The Scale Problem

However, neither a model of this size nor standard UML can accommodate:

- The vast number and diversity of possible clinical document values created in specific contexts
- Tens of thousands of clinical observations (systolic blood pressure, visual acuity, etc.), many with multiple data points in specific structures
- Approximately 10^4 laboratory test result analyte types
- Terminology needed to annotate data items (names and values) numbering 10^5 to 10^6 concepts, as exemplified by SNOMED CT, ICD, and other clinical terminologies

### The Meaningful Instance Space Problem

While these numerous values technically could be understood as specific values arising in data creation situations, domain data value patterns representing meaningful combinations constitute only a tiny fraction of the astronomically large number of possible value combinations within information model structures.

"Meaningful instance space" (the actual data of interest) occupies a small portion of possible instances allowed by a typical information model. To illustrate: while some tens to hundreds of thousands of clinical statement patterns would adequately cover nearly all general medical data recording, the same information models technically permit instance structures numbering 10^10 or higher—meaning most possible instance data constructions represent nonsense.

This parallels natural language: meaningful sentences constitute only a tiny fraction of grammatically correct word sequences.

### Classic Approach Limitations

The traditional approach—expanding the information model to accommodate all meaningful patterns—creates problems:

- Information models typically form the basis for deployable software and database schemas
- Constant model changes imply continuous system instability
- In systems operating 24/365 and generating terabytes of data annually, this proves unacceptable

### Domain Expertise Requirement

Beyond technical concerns, domain semantics models must be authored by domain experts—physicians, engineers, etc.—rather than software developers. These professionals typically employ their own domain-specific formalisms incomprehensible to IT professionals and often lack knowledge of programming languages used by IT staff.

### Template Tools: A Partial Solution

Large software products in health and other domains often include configuration or template building tools enabling domain experts to model typical content patterns, usually as screen form definitions. This partially addresses both issues: some domain semantics separate from software, and non-IT personnel can build them using dedicated tools.

However, significant limitations exist: such approaches don't model the complete meaningful instance space, typically tie to user interface specifics, and don't prevent creation of nonsensical data instances.

### Standardization Gap

The primary limitation affecting mainstream IT: no standardized, vendor-independent modeling capability exists for domain patterns. While some advanced tools technically could accomplish this work, they typically remain embedded within specific products and tied to proprietary data models.

### Economic Implications

High-quality domain model creation proves time-consuming and expensive, requiring domain experts—experienced clinicians, engineers, etc.—rather than IT staff. When domain models exist only within specific products and that product is replaced, the original modeling work often cannot be recreated in a new environment. Across products, sites, and entire industry verticals, "the lack of standard representation methods for domain content models has become a significant impediment to producing superior information systems."

### The openEHR Solution

The requirement for an efficient, formal, product-independent, and implementation-format-independent domain modeling approach becomes clear. In health, where the magnitude of domain semantics requiring formalization makes both single-model approaches and simplistic screen templating unscalable, alternative methods have emerged. openEHR developed the Archetype formalism for this purpose, working with terminologies including SNOMED CT, LOINC, ICD, and many others.

### Two Categories of Domain Models

Two distinct requirements emerge:

1. **Use-independent definitions:** modeling individual data points and data groups
2. **Use-case dependent definitions:** modeling comprehensive data sets

For example, patient vital signs recording requires definitions for blood pressure, heart rate, and blood oxygen that function independently of specific contexts (home measurement, GP encounter, hospital bedside). Each vital sign records identically across contexts. However, these vital signs appear within larger data sets corresponding to specific health system events: GP checkup or ED initial assessment.

The domain modeling formalism therefore requires two capabilities:
- Modeling reusable domain data items and structures
- Modeling larger use-case-specific combinations of generic elements

The alternative—creating domain models for every data set and repeatedly redefining recurring sub-models like blood pressure—creates unnecessary duplication and maintenance burden.

---

## 2. Archetype Formalism Overview

The openEHR Archetype formalism, originally described in Beale (2002) as "two-level modelling," intentionally remains independent of any specific information model, product, technical format, or industry vertical. It enables computational processing of archetype instances into desired output forms matching particular technology environments, routinely performed in openEHR tooling.

### Scope and Application

The formalism primarily addresses modeling possible data instance structures rather than higher-level concepts like workflows or clinical guidelines, though its general approach—defining "what can be said" and constraining possibilities to meaningful subsets—applies broadly.

### Three-Layer Architecture

Given the two model categories described above, the archetype formalism combined with orthodox (typically object-oriented) information models enables three-layer information modeling:

**Information Model (Reference Model)**
- Defines data semantics
- Functions as the foundation for meaningful data representation

**Archetypes**
- Models defining possible data arrangements corresponding to logical data points and groups for a domain topic
- Collections constitute reusable domain content definition element libraries

**Templates**
- Models of content corresponding to use-case-specific data sets
- Constituted from archetype elements
- Provide the mechanism for practical system deployment

### Model Relationship Visualization

The information model (Reference Model) intentionally remains limited to domain-invariant data elements and structures (Quantity, Coded text, generic containment structures), enabling stable data processing software deployment independent of specific domain information entity definitions. While generic information models enable "any data" instances, achieving "meaningful data" requires domain content models (archetypes and templates).

### Semantic Layers

The RM/Archetypes/Templates model stack defines information as created and used—an epistemological view—but does not attempt describing the ontological semantics of each information element. Ontologies (found in resources like the Open Biomedical Ontology Foundry) and terminologies (such as SNOMED CT) define naming over ontological frameworks for use in particular contexts.

### Terminology Integration

The information model stack connects to terminology via terminology bindings within archetypes and templates, enabling specification of relationships between:
- Element "names" and terminology/ontology entities
- Element values and value domains on the terminology side

### Query Component

Information queries under archetype methodology are defined solely in terms of:
- Archetype elements (via paths)
- Terminology concepts
- Logical reference model types

This approach produces portable queries requiring single authoring regardless of persistence layer data schemas.

### Semantic Model Space

Reference model, archetypes, and templates (with bound terminology) together constitute a sophisticated semantic model space. Because templates function as abstract artefacts, they enable single-source generation of concrete artefacts (XML schemas, screen forms, etc.). A single definition of "diabetic patient encounter" can generate both message definition XSD and screen form.

The template operational form provides the basis for tool-generation of usable downstream concrete artefacts embodying template semantics in forms usable by typical developers.

### Operational Systems

Deployed operational system artefacts enable data creation and querying. Archetype-based ecosystem artefacts enable significantly higher quality, semantic power, and maintainability information systems because both data and querying remain model-based, with models underpinned by terminology and ontology.

### Formalization and Tooling

Underlying this architecture are formalisms and tooling—the languages and tools of archetypes. This overview describes archetype specifications and how they support tool-building and downstream model-based software development.

---

## 3. The Specifications

Archetype formalism semantics are defined through the following normative specifications:

### Archetype Identification

A normative specification addressing archetype and template model identification, versioning, referencing, and lifecycle management.

### The Archetype Definition Language (ADL)

A normative abstract syntax for archetypes, templates, and terminology binding, serving as the primary document for human understanding of archetype semantics.

### The Archetype Object Model (AOM)

The normative structural model of archetypes and templates, primarily specifying how to build archetype tools and EHR components using archetypes.

### The Operational Template (OPT)

Normative description of Operational Templates (OPTs) semantics, primarily useful to tool-builders.

### The Archetype Querying Language (AQL)

The normative querying language based on archetypes and terminology.

### Specification Relationships

The Archetype Identification specification describes archetype identifier semantics—equivalent to describing archetype-based model space structure—and lifecycle management and versioning aspects.

ADL functions as the formal abstract syntax for archetypes, providing default serial expression. The "primary document for human understanding of the semantics of archetypes" is ADL.

The AOM represents the definitive formal archetype semantic expression, independent of particular syntax. Its "main purpose" involves "specifying to developers how to build archetype tools" and EHR components using archetypes.

AOM semantics express source and flattened archetype object structures. Since ADL 2 treats templates as archetype kinds, the AOM also describes template semantics. User-authored source forms and tool-generated flat forms are described with detailed AOM usage rules in the specification.

The Operational Template specification defines openEHR Templates' operational form for downstream systems and tools, primarily benefiting tool-builders.

The Archetype Query Language specification defines a query language assuming a Reference Model and Archetypes as its semantic base.

---

## 4. Semantic Overview

Archetypes function as topic- or theme-based domain content models, expressed as constraints on reference information models. Each archetype encapsulates a manageable set of data points pertaining to a topic with clear boundaries. For example, an 'Apgar result' archetype of the openEHR reference model class `OBSERVATION` contains data points relevant to newborn Apgar scoring, while a 'blood pressure measurement' archetype contains blood pressure result and measurement data points. Templates assemble archetypes into structures used in computational systems like document and message definitions.

Unless otherwise qualified, "archetype" includes templates, technically constituting archetype special cases.

---

### 4.1. Identification and the Virtual Archetype Space

Two identification mechanisms exist: GUIDs and Human Readable IDs (HRIDs). The Archetype HRID structure corresponds to the model space created by combining Reference Model and Archetypes.

#### HRID Structure Example

A typical archetype HRID: `uk.gov.nhs::openEHR-EHR-COMPOSITION.medication_order.v1`

**Components:**

- **Namespace:** `uk.gov.nhs` (Custodian Organisation identifier)
- **RM class space:** `openEHR-EHR-COMPOSITION` (Reference Model entity)
- **Semantic entity:** `medication_order` (domain-level entity being modeled)
- **Version:** `v1` (major version)

The blue segment indicates the Reference Model class entity. The green part indicates the domain-level entity. The RM class space combined with semantic subspaces defines the logical model space created by archetype formalism.

#### Ontological Interpretation

This model space functions equivalently as an ontological space where models act as ontological descriptions of real data. Philosophically, this involves a measurement: data technically originate from these very models. However, if models were defined representing information from the real world (prescriptions, progress notes, lab results created by healthcare professionals), they can be understood as ontological descriptions of those original informational entities.

#### Namespace Implications

The namespace within the HRID indicates Custodian Organisation, enabling multiple agencies to publish competing ideas without identifier clashes. For example, `uk.gov.nhs::openEHR-EHR-COMPOSITION.medication_order.v1` and `no.regjeringen::openEHR-EHR-COMPOSITION.medication_order.v1` should be understood as UK NHS and Norwegian Health Department interpretations of 'medication_order' based on the same openEHR Reference Model `COMPOSITION` class.

**Practical value:** Avoids immediate chaos. Long-term intention: locating archetype semantic identifiers for given domains in common international ontologies of information artefact types.

#### Clinical Domain Ontology

For clinical domains, it is envisioned that Basic Formal Ontology (BFO) 2nd Edition and Information Artefact Ontology (IAO) upper-level ontologies would provide foundations for clinically specific models. Both NHS and Norwegian variants of 'medication_order' plus universally accepted forms would exist under the document/COMPOSITION node.

#### Namespace Implications for Libraries

Differently namespaced archetypes can coexist within the same Library workspace, potentially due to archetype transfer or forking from an original custodian to another.

#### Uncontrolled Archetypes

An Archetype HRID may legally have no namespace, indicating it remains uncontrolled and not managed by any organization.

#### Versioning

Archetype identifiers include the major version (first of a three-part version, e.g., 1.5.0), as major version changes in IT contexts generally signal breaking changes. Different major versions are computationally considered different artefacts. The full version also constructs identifiers useful for physical resources (files, version system references).

#### Ontology Development Timeline

Progress toward universal domain ontologies proves complex and slow, involving:

- Reference Model custodians (typically standards bodies)
- Archetype custodians (typically domain organizations within major jurisdictions)
- Organizations like OBO

Multi-year development processes appear clearly implied.

#### Practical Ontology Approach

A practical view treats a given Reference Model (or small numbers of closely related RMs) as fixed, developing archetype ontologies underneath. This requires Archetype custodian agreement and, if successful, results in single definitional spaces. All would agree, for example, that 'systemic arterial blood pressure measurement' held that designation with short name 'bp_measurement'. This approach does not eliminate custodians, since real distinctions persist across geographies and sub-specialties. For example, an internationally agreed 'pregnancy record' entity might possess specializations like 'European standard pregnancy record' and 'Swedish pregnancy record', with European and Swedish Ministry of Health bodies as custodians.

Harmonization of this type occurs within openEHR through national-level archetype governance organization cooperation with the openEHR Foundation, acting as international archetype governance body, hosted at the openEHR Clinical Knowledge Manager. Such harmonization remains slow.

#### Formalism Design Basis

The formalism and tooling operates on the simplest realistic assumption: Reference Model types hierarchies combined with optionally namespaced Archetypes form self-standing information ontologies similar to figure examples, constituting IS-A hierarchies of RM types followed by Archetypes.

**Practical value:**

- Real data can be computationally classified under various ontology points—determining computationally if certain data represent 'bp_measurement', 'UK NHS bp_measurement', or even just `OBSERVATION`
- Using subsumption operators on the IS-A hierarchy defines useful overall space subsets, such as `{any-descendant of 'medical_device'}`, `{any-descendant-or-self of OBSERVATION}`

The IS-A hierarchy appears in archetype tools such as the openEHR ADL Workbench.

---

### 4.2. Collections of Archetypes

Within the virtual archetype space described above, identifiable archetype groups relate to tool operations, particularly identifier resolution mechanisms. For the foreseeable future, all following collection types are assumed to occur under specific custodian namespaces—managers and archetype publishers.

#### Archetype Library

An Archetype Library represents a coherent archetype collection actually available within a single workspace or repository. All library archetypes and templates typically base on the same Reference Model, though this need not occur (as in test archetypes). Apart from such cases, Archetype Libraries consist of archetypes normally designed for collaborative use in validating and creating information, potentially including non-namespaced (unmanaged) and differently namespaced archetypes resulting from promotion and/or forking. Library maintainers must ensure all library archetype compatibility.

#### Archetype Repository

One or more Archetype Libraries exist within an Archetype Repository, understood as a physical archetype management location, typically with version control and download capability. Archetype Repositories denote no semantics; rather they provide access, committal, and versioning units for tool operations.

#### Custodian Organisations

Archetype Libraries within Archetype Repositories are published by Custodian Organisations, corresponding to archetype identifier namespace parts.

#### Universe of Archetypes

The outermost level includes the Universe of Archetypes for a Reference Model, corresponding to all existing archetypes for that RM—a virtual collection of all Reference Model-based Archetype Libraries. This encompasses archetypes created by different Custodian Organisations, different RM classes, various semantic entities (what the archetype represents, e.g., 'blood pressure measurement'), and multiple versions and revisions of all these.

---

### 4.3. Archetype Relationships

Within Archetype Libraries, two archetype relationship kinds exist: specialisation and composition.

#### 4.3.1. Archetype Specialisation

An archetype can be specialized in descendant archetypes similarly to object-oriented programming language subclasses. Specialized archetypes, like classes, express themselves in differential form relative to the flat parent archetype (the effective archetype resulting from flattening operations down the specialisation hierarchy)—a necessary sustainable management prerequisite for specialized archetypes.

An archetype specializes another archetype if it mentions that archetype as parent while making only changes narrowing constraints compared to the flat parent. This can include specialized archetypes defining constraints on Reference Model parts unconstrained by parent archetypes—still constituting "narrowing" or constraining.

The archetype chain from specialization back through all parents to the ultimate parent is known as an archetype lineage. Non-specialized (top-level) archetypes have lineages consisting of themselves.

Specialized archetypes require the differential authoring form to flatten through the archetype lineage, creating flat-form archetypes—standalone equivalents of given archetypes as if constructed independently. Flattened archetypes use the same serial and object forms as differential archetypes, though some semantic differences exist beyond differential path usage.

Any data created via archetype usage conforms to both the flat archetype form and every flat archetype up the lineage.

#### 4.3.2. Archetype Composition

For reuse purposes, archetypes can compose into larger structures semantically equivalent to single large archetypes. Composition enables two operations:

1. Archetype definition according to natural information encapsulation "levels"
2. Smaller archetype reuse by higher-level archetypes

Two composition expression mechanisms exist:

- **Direct reference:** explicit archetype reference
- **Archetype slots:** constraint-defined slots enabling any archetype subset—via subsumption relations—as the allowed use set at certain compositional parent archetype points

These semantics appear in detailed syntax form in the ADL specification and structural form in the AOM specification.

---

### 4.4. Archetype Internals

Archetypes are represented computationally as Archetype Object Model instances. For persistence, they require serialization. The Archetype Definition Language (ADL) functions as the normative authoring and persistence language, similarly to programming language syntax representing programming constructs. Intentionally designed as terse and intuitively human-readable, ADL provides the default serialization. Multiple alternative serializations exist for technical reasons: 'object dump' ODIN, XML, and JSON serializations, with potential future representations like OWL and OMG XMI according to emerging development technology needs. For archetype formalism description and documentation, ADL is generally employed.

#### XML Usage and Limitations

XML-schema-based XML applies to many archetype computing purposes and may become the predominant syntax regarding user numbers. However, XML does not function as archetype normative syntax for several reasons:

1. No single enduring XML schema exists. Initially published schemas are replaced by more efficient versions and potentially replaced by alternative XML syntaxes (XML-schema-based versions may be replaced or supplemented by Schematron)
2. XML provides minimal explanatory syntax value for standards purposes, with underlying syntax obscuring archetype semantics or specific application purposes. Acceptable XML archetype expression changes may render standards document examples obsolete
3. JSON increasingly replaces XML usage in many programming environments

An archetype XML schema is available on the openEHR website.

#### 4.4.1. Archetype Definition Language (ADL)

ADL employs three sub-syntaxes:

- **cADL** (constraint form of ADL)
- **ODIN** (Object Data Instance Notation)
- **First-order predicate logic (FOPL)** version

The cADL and FOPL parts express constraints on underlying information model instances data, potentially expressed in UML, relational form, or programming languages. ADL itself functions as simple 'glue' syntax connecting subordinate syntax blocks into overall artefacts. cADL expresses archetype definition sections, while ODIN syntax expresses data appearing in language, description, terminology, and revision_history sections. The top-level ADL archetype structure includes:

- **Header:** identification and metadata
- **Definition:** constraint definition (cADL syntax)
- **Language:** language and terminology information (ODIN syntax)
- **Description:** descriptive metadata (ODIN syntax)
- **Terminology:** term definitions and bindings (ODIN syntax)
- **Revision history:** version history (ODIN syntax)

---

### 4.5. Templates

Practical systems assemble archetypes into larger usable structures using templates. A template expresses itself in the same source form as specialized archetypes, typically using slot-filling mechanisms. Processed against archetype libraries produces operational templates—flat-form archetype equivalents used for runtime validation and downstream artefact generation.

Semantically, templates perform three functions:

1. **Archetype aggregation**
2. **Element selection** for use cases
3. **Existing constraint narrowing** similarly to specialized archetypes

The effect reuses needed library elements, arranging them corresponding directly to template use cases.

#### Template Functions

Templates accomplish the following:

**Composition**
- Aggregate archetypes into larger structures by indicating which archetypes should fill higher-level archetype slots

**Element Choice**
- Choose which parts of selected archetypes remain in final structures through:
  - **Removal:** remove archetype nodes (data points) unneeded for template purposes
  - **Mandation:** mark archetype nodes (data points) mandatory for runtime template usage
  - **Optionality:** leave nodes optional, meaning corresponding data items are optional at runtime

**Narrow Constraints**
- Narrow remaining constraints on archetype elements or Reference Model parts (parts of the RM not yet constrained by template-referenced archetypes)

**Set Defaults**
- Set default values if required

A template may compose any number of archetypes while choosing very few data points from each, creating small data sets from very large original archetype data point numbers.

#### Archetype Semantics Documentation

Archetype semantics used in templates appear in detail in the ADL specification; detailed template use description appears in the ADL2 specification Templates section. The AOM specification describes structural form all template semantics. Note that the AOM does not distinguish between archetypes, specialized archetypes, or templates except by artefact type classifier use. All other operational differences depend on tools that may allow or prevent certain operations based on whether the worked-on artefact is an archetype or template.

---

## 5. Artefacts

### 5.1. Model / Syntax Relationship

The Archetype Object Model represents in-memory archetype or template models, or equivalently, standard syntax trees for any serialized format—not exclusively ADL. While ADL functions as the normative abstract syntax form, archetypes can be equally parsed from and serialized to XML, JSON, or other formats. In-memory archetype representations may also be created through suitable AOM construction API calls from archetype and template editing tools.

These relationships and each form's specification connection appear in corresponding diagrams. Archetype and template serialized forms potentially exist in multiple formats, though any given environment typically uses single serialized forms.

All possible archetype and template artefact types, including file types, are illustrated, encompassing:

- **Source-form differential archetypes**
- **Source-form differential templates**
- **Flat-form archetypes**
- **Flat-form templates**
- **Operational templates**

Each form has corresponding file types and serializations in ADL, XML, JSON, and other formats.

### 5.2. The Development Process

Archetypes are authored and transformed similarly to class definitions within object-oriented programming environments. Development process activities include:

**Authoring**
- Creates source-form archetypes expressed as AOM objects

**Validation**
- Determines archetype semantic validity rule satisfaction
- Requires specialization parent flat form if specialized archetypes

**Flattening**
- Creates flattened archetypes

Templates are authored similarly, typically using only mandations, prohibitions, and refinements. The final step involves generating an operational template—the fully flattened and substituted source definition form.

#### Tool Chain

The process tool chain illustration shows template authoring as the starting point. Templates reference one or more archetypes, so template compilation (parsing, validation, flattening) involves both template source and validated, flattened referenced archetype forms. With these inputs, template flatteners generate final output: operational templates.

### 5.3. Compilation

Tools parsing, validating, flattening, and generating new outputs from artefact libraries are called compilers. Due to specialisation existence, archetype specialisation lineages rather than individual archetypes are processed—specialized archetypes can only compile with specialisation parents through top-level. Each archetype potentially has supplier artefact lists—archetypes referenced via ADL use_reference statements. For archetype compilation, all suppliers and specialisation parents must already compile.

This approach exactly parallels object-oriented programming environments. For any lineage, compilation proceeds top-level downward. Each archetype undergoes validation and, if passing, flattens with the chain parent. This continues until originally compiled archetypes are reached. Archetypes without specialisations involve only the archetype itself and its suppliers.

The illustration shows archetype lineage object structures created by compilation processes, with top-level archetype elements bolded. Differential input files are converted by parsers into differential object parse trees shown left of flattener processes. Editors would create identical structures.

#### Validation Process

Differential in-memory representation validation through semantic checkers verifies numerous aspects:

- Term codes referenced in definition sections are defined in terminology sections
- Classes and attributes mentioned in archetypes validate against relevant Reference Model specifications

Compilation process results appear in archetype visualizations in openEHR ADL Workbench tools.

### 5.4. Optimisations

In authoring (design-time) environments, artefacts should remain considered 'suspect' until proven otherwise through reliable validation, regardless of original syntax (ADL, XML, etc.). Once validated, flat forms can be reserialised in both:

1. **Editor tool formats:** ADL, XML, etc., for tool use
2. **Pure object serialization:** reliable in-memory structure serializations

The latter form often uses XML but can employ any object representation: JSON, openEHR ODIN syntax, YAML, binary forms, or database structures. It will not be abstract syntax forms like ADL, since unavoidable semantic transformations occur between abstract syntax and object forms.

This pure object serialization utility lies in validated artefact persistence, converted to in-memory form using only non-validating stream parsers rather than multi-pass validating compilers. This allows validated artefact usage in both design environments and crucially, runtime systems with no compilation error danger. This parallels Java .jar file creation from source code and .Net assembly creation from C# source code.

Within openEHR environments, archetype authoring and persisted form management occurs through various mechanisms including digital signing, described in openEHR governance documentation.

---

## References

Beale, T. (2002). Archetypes: Constraint-based Domain Models for Future-proof Information Systems. In K. Baclawski & H. Kilov (Eds.), *Eleventh OOPSLA Workshop on Behavioral Semantics: Serving the Customer* (pp. 16-32). Northeastern University, Boston. Retrieved from https://www.openehr.org/publications/archetypes/archetypes_beale_oopsla_2002.pdf

Fowler, M. (1997). *Analysis Patterns: Reusable Object Models*. Addison Wesley.

---

**Last updated:** 2022-11-12 10:23:49 UTC

# Architecture Overview

**Issuer**: openEHR Specification Program

**Release**: BASE Release-1.2.0

**Status**: STABLE

**Keywords**: EHR, openehr, architecture

(c) 2003 - 2021 The openEHR Foundation

The openEHR Foundation is an independent, non-profit foundation, facilitating the sharing of health records by consumers and clinicians via open specifications, clinical models and open platform implementations.

**Licence**: Creative Commons Attribution-NoDerivs 3.0 Unported. https://creativecommons.org/licenses/by-nd/3.0/

**Support**: Issues: Problem Reports | Web: specifications.openEHR.org

**Source**: https://specifications.openehr.org/releases/BASE/latest/architecture_overview.html

---

## Amendment Record

| Issue | Details | Raiser, Implementer | Completed |
|-------|---------|-------------------|-----------|
| **BASE Release 1.2.0** | | | |
| 1.2.3 | SPECPUB-7: Convert citations to bibtex form; SPECBASE-24: Improve specifications block diagram and related explanations in sections 2 and 5. | T Beale | 18 Jan 2020 |
| | SPECRM-88: Improve documentation relating to use of `_uid_` in versioning and `LOCATABLE` descendants in `change_control` package (addresses SPECPR-322). | P Pazos, M Polajnar, T Beale | 15 Oct 2019 |
| **BASE Release 1.1.0** | | | |
| 1.2.2 | SPECBASE-21: Update Architecture Overview with new LANG component, and improved explanation of ITS. Improve package structure description. Replace some diagrams. | T Beale | 26 Nov 2018 |
| | SPECRM-80: Improve description of `_system_id_` field in `EHR`, `AUDIT_DETAILS` and `FEEDER_AUDIT_DETAILS`. | H Frankel, T Beale | |
| | SPECRM-78: Improve documentation on 'plain text' EHR URIs. | H Frankel | 22 Nov 2018 |
| | SPECBASE-18: Update text in Common IM to latest openPGP specification. | P Pazos | 17 May 2018 |
| 1.2.1 | SPECBASE-16: Update Architecture Overview with current high-level elements. Section 5.3.4: Added text indicating BMM usage and alternatives. Section 11.2.4.2: Added JSON format version of example. | E Sundvall, S Iancu | 09 Nov 2017 |
| | SPECBASE-15: Add Foundation Types specification to BASE; SPECBASE-7: Add Base Types specification to BASE. SPECBASE-16: Update Architecture Overview with current high-level elements. Section 2: Updated overview diagram and description to be based on 'components' as per current specifications program; Section 5: Updated package diagrams to exported diags from BASE, RM, AM, SM UML components; Section 7.4.1: small updates to statements to make them more current; fixed some references to ISO standards. | T Beale | 09 Sep 2017 |
| **BASE Release 1.0.3** | | | |
| 1.2.0 | SPECRM-33: Clarify specification of DV_EHR_URI scheme. (solves SPECPR-48, SPECPR-50) | H Frankel, E Sundvall, B Lah, S Iancu | 07 Dec 2015 |
| | SPECRM-27: Relax unique name rule in `LOCATABLE`: change text of sections 11.2.2 and 11.2.4. | H Frankel, T Beale | |
| | SPECRM-25: Corrections to Architecture Overview specification: text in section 9.2.2 about `LOCATABLE_REF` referred to wrong specification. | T Beale | |
| | SPECRM-28: Corrections to EHR and Common IM documentation. SPECPR-2: Changes to Architecture Overview section 5.2.1. | R Erens | |
| **Release 1.0.2** | | | |
| 1.1.1 | SPEC-249: Paths and locators minor errors in Architecture Overview and Common IM. Typos corrected in sections 9.2.2 and 11.3. | C Ma, T Beale, R Chen | 13 Nov 2008 |
| | SPEC-257: Correct minor typos and clarify text. Section 9.2.1 para 1 line 2: with -> within. | C Ma, R Chen, T Cook | |
| | SPEC-284: Correct inconsistencies in naming of `_term_definitions_`, `_constraint_definitions_`, `_term_bindings_`, `_constraint_bindings_` attributes in XML-schema and specifications. | A Torrisi | |
| **Release 1.0.1** | | | |
| 1.1 | SPEC-200: Correct package names in RM diagram. | D Lloyd | 12 Apr 2007 |
| | SPEC-130: Correct security details in `LOCATABLE` and `ARCHETYPED` classes. | T Beale | |
| | SPEC-203: Release 1.0 explanatory text improvements. Improved path explanation. Slight re-ordering of main headings. | T Beale, G Grieve, T Shannon, H van der Linden | |
| | Path shortcuts. | H Frankel | |
| | Added configuration management and versioning material from Common IM. Added section on ontological landscape. Added section on aims. Added section on systems architectures. Added section on security. Added section on system integration. | T Beale | |
| | Added section on terminology. | T Beale, S Heard | |
| **Release 1.0** | | | |
| 1.0 | Initial Writing - content taken from Roadmap document. SPEC-147: Make `DIRECTORY` Re-usable SPEC-167: Move AOM description package to `resource` package in Common IM. SPEC-185: Improved EVENT model. | T Beale | 29 Jan 2006 |

---

## Acknowledgements

The work reported in this paper has been funded by the following organisations:

- University College London - Centre for Health Informatics and Multi-professional Education (CHIME)
- Ocean Informatics

Special thanks to David Ingram, Emeritus Professor of Health Informatics at UCL who provided a vision and collegial working environment ever since the days of GEHR (1992).

### Trademarks

- 'openEHR' is a trademark of the openEHR Foundation
- 'Java' is a registered trademark of Oracle Corporation
- 'Microsoft' and '.Net' are trademarks of the Microsoft Corporation

---

## 1. Preface

### 1.1. Purpose

This document provides an overview of the openEHR architecture in terms of a model overview, key global semantics, deployment and integration architectures, relationship to published standards, and finally the approach to building Implementation Technology Specifications (ITSs). Semantics specific to each information, archetype and service model are described in the relevant specification.

The intended audience includes:

- Standards bodies producing health informatics standards
- Academic groups using openEHR
- The open source healthcare community
- Solution vendors

This document is the key technical overview of openEHR, and should be read before all other technical documents.

### 1.2. Status

This specification is in the STABLE state. The development version of this document can be found at https://specifications.openehr.org/releases/BASE/Release-1.2.0/architecture_overview.html.

Known omissions or questions are indicated in the text with a 'to be determined' paragraph, as follows:

**TBD**: (example To Be Determined paragraph)

### 1.3. Feedback

Feedback may be provided on the technical mailing list.

Issues may be raised on the specifications Problem Report tracker.

To see changes made due to previously reported issues, see the BASE component Change Request tracker.

---

## 2. Overview

This document provides an overview of the openEHR architecture. It commences with a description of the specification project, followed by an overview of the model structure and packages. Key global semantics including security, archetyping, identification, version and paths are then described. The relationship to published standards is described, and finally, the approach to building implementations is outlined.

### 2.1. The openEHR Specification Program

The openEHR Specification Program is responsible for developing the specifications of openEHR, from which the openEHR Health Computing Platform is implemented. The outputs of the program consist of a number of _components_, as shown in the diagram below, with each component (marked in blue) consisting of one or more separate specifications.

The components in the left group contain the _abstract specifications_ (also known as the 'Platform Independent Model' or PIM) and are divided into the following:

- **Foundation (BASE)**: primitive types, definitions, identifiers, other basic types needed across openEHR
- **Formalisms (LANG, AM, QUERY)**: various generic formalisms, including BMM (Basic Meta-Model), ADL (Archetype Definition Language) and AQL (Archetype Query Language)
- **Content (TERM, RM)**: the models of primary content of the openEHR platform, including demographics, EHR; supporting openEHR Terminology (along with expressions of various ISO, IETF and other vocabularies (language names, territory names, MIME types, etc) that are not typically published in a directly usable format)
- **Process & CDS (PROC, CDS)**: clinical process and clinical decision support components, containing the Task Planning and GDL (Guideline Definition Language) specifications
- **Platform Services**: abstract formal APIs defining the interfaces to the openEHR platform

Some of these specifications (e.g. Antlr grammars) are directly usable in software development. Most of the abstract specifications have concrete expressions in formalisms such as JSON, XML schema, openEHR BMM and REST APIs enabling their direct use in development. These are known as Implementation Technology Specifications (ITSs; also known as 'Platform-Specific Models' or PSMs), and are collected in the ITS component shown on the right. They also constitute openEHR's _interoperability specifications_.

As implementation technologies change over time the ITS specifications will be replaced, while the main group of abstract specifications will generally only change in response to real-world requirements other than information technology.

The CNF component at the top defines _conformance criteria_, and is primarily based on ITS artefacts such as REST APIs, XSDs, but also upon AQL queries, archetypes and some other abstract artefacts. It includes a formal definition of the notional openEHR Platform and how to test it in a standard way. This is used as the basis for openEHR product certification and also for procurement tender specification.

The specifications published by openEHR constitute the _primary reference for all openEHR semantics_. The presentation style is deliberately intended to be clear and semantically close to the _ideas_ being communicated. Accordingly, the specifications do not follow any particular programming language or idiom, but instead use various formalisms and illustrations appropriate to each topic.

Change control is performed by the openEHR Specifications Editorial Committee (SEC), using a formal process based on Problem Reports (PRs) and Change Requests (CRs), and a formal release cycle. The details are described in the Specifications Program part of the openEHR website.

The openEHR specification documents and related formal artefacts may be found on the specifications home page. The documents are maintained in Asciidoctor source form, and make significant use of included formal elements, including extracted UML class texts and diagrams, as well as grammar files.

---

## 3. Aims of the openEHR Architecture

### 3.1. Overview

The openEHR architecture incorporates over 20 years of research from numerous projects and standards globally. It was designed based on requirements developed through many years of work, including those from the EU FP3 Good European Health Record (GEHR) project (1992-1995).

Because the architecture is highly generic and archetype-driven, it satisfies many requirements extending beyond the original clinical EHR concept. The same reference architecture can support veterinary health records or even care of public infrastructure. This flexibility exists because the reference model embodies only concepts relating to "service and administrative events relating to a subject of care"; specifics of care event kinds and subject types are defined in archetypes and templates.

The openEHR architecture addresses requirements across two dimensions: scope and kind of subject. Requirements for various health care record flavors can be categorized accordingly.

Each bubble in the requirements figure represents a set of requirements, with contained bubbles representing subsets. The top-left bubble represents generic care record requirements for any subject in local deployment. Moving down the left side adds requirements for living subjects, then human subjects, corresponding to local health records for human care such as radiology records and hospital EPRs. Moving across the diagram extends the scope from episodic to whole-subject records, then to population-level or cohort-based information.

Going down the diagram, requirements corresponding to increasing subject-of-care specificity are primarily implemented through archetypes. Moving across the diagram, requirements corresponding to increasing record scope are mainly expressed through different deployments, generally from standalone to shared interoperable forms. The integrated care record sought by many health authorities aligns with ISO 20514's definition of ICEHR, providing an informational framework for integrated shared care.

Because of openEHR's approach, components and applications built to satisfy integrated shared care record requirements can also be deployed as episodic radiology record systems or other specialized contexts.

#### 3.1.1. Generic Care Record Requirements

The openEHR requirements include the following, corresponding to a basic, generic record of care:

- prioritisation of the patient / carer interaction (over e.g. research use of the record);
- suitable for all care settings (primary, acute etc.);
- medico-legal faithfulness, traceability, audit-trailing;
- technology & data format independence;
- highly maintainable and flexible software;
- support for clinical data structures: lists, tables, time-series, including point and interval events.

#### 3.1.2. Health Care Record (EPR)

The following requirements addressed in openEHR correspond to a local health record, or EPR:

- support for all aspects of pathology data, including normal ranges, alternative systems of units etc.;
- supports all natural languages, as well as translations between languages in the record;
- integrates with any/multiple terminologies.

#### 3.1.3. Shared Care EHR

The following requirements addressed in openEHR correspond to an integrated shared care EHR:

- support for patient privacy, including anonymous EHRs;
- facilitate sharing of EHRs via interoperability at data and knowledge levels;
- compatibility with ISO 13606, Corbamed, and messaging systems;
- support semi-automated and automated distributed workflows.

### 3.2. Clinical Aims

From a more specifically clinical care perspective, the following requirements have been identified during openEHR development:

- The need for a patient-centric, lifelong electronic health record that entails a holistic view of patient needs as opposed to niche problem-solving and decision-support techniques for limited diagnostic purposes;
- Integration of different views of the patient (GP, emergency and acute care, pathology, radiology, computerised patient-order entry, etc.) with the vast body of available knowledge resources (terminologies, clinical guidelines and computerised libraries);
- Clinical decision-support to improve patient safety and reduced costs through repeated medical investigations;
- Access to standards-based computing applications.

The Integrated Care EHR holds great promise: to generalise and make widely available the benefits of computerisation that have been demonstrated individually and in isolated settings. These can be summarised as:

- Reducing adverse events arising from medication errors such as interactions, duplications or inappropriate treatments and the flow-on costs associated with these;
- Improving the timely access to critical information and reduced clinician time searching for information;
- Reducing the incidence of patients being overlooked in the healthcare system due to information not being communicated;
- Reducing the duplication of investigations and other tests and procedures due to results not being available in the local computing environment;
- Improved prevention and early detection, based on predictive risk factor analysis, which is possible with quality EHR data;
- Improved decision making through decision support tools with access to the patient's whole EHR;
- Improving access to and computation of evidence based guidelines;
- Increasing targeted health initiatives known to be effective, based on patient criteria; and
- Reduced hospitalisations and readmissions.

One comprehensive statement of EHR requirements covering many of the above is the ISO 18308, ISO Technical Report 18308 for which an openEHR profile has been created. The requirements summarised above are described in more detail in the openEHR EHR Information Model specification.

### 3.3. Deployment Environments

The openEHR architecture is designed to support construction of various system types. One important category is the integrated shared care health record.

openEHR-enabled systems can provide EMR/EPR functionality at provider locations. Overall, several important categories of system can be implemented using openEHR including the following:

- shared-care community or regional health service EHRs;
- summary EHRs at a national, state, province or similar level;
- small desktop GP systems;
- hospital EMRs;
- consolidated and summary EHRs in federation environments;
- legacy data purification and validation gateways;
- web-based secure EHR systems for mobile patients.

Systems containing health records in anonymised or pseudonymised form can also be implemented, since the openEHR architecture defines an EHR in which demographic links (e.g. to national registry, or via national healthcare number) are optional. Where such links are used in the institutional EMR or shared EHR context, they can easily be removed in an anonymisation process.

---

## 4. Design Principles

The openEHR approach to modelling information, services and domain knowledge is based on several design principles. These principles lead to a separation of the models of the openEHR architecture, consequently enabling high-level componentisation. This leads to better maintainability, extensibility, and flexible deployment.

### 4.1. Ontological Separation

The most basic kind of distinction in any system of models is ontological, meaning separation in levels of abstraction of real-world description. All models carry semantic content, but not all semantics are identical or of the same category. For example, SNOMED CT terminology describes types of bacterial infection, body sites, and symptoms. An information model might specify a logical type Quantity. A content model might define the model of information collected in an ante-natal examination. These types of information are qualitatively different and need to be developed and maintained separately within the overall model ecosystem.

The ontological landscape shows a primary separation between "ontologies of information" (models of information content) and "ontologies of reality" (descriptions and classifications of real phenomena). These two categories must be separated because the type of authors, representation, and purposes are completely different. In health informatics, this separation largely already exists due to the development of terminologies and classifications.

A secondary ontological separation within the information side exists between information models and domain content models. Information models correspond to semantics that are invariant across the domain (e.g. basic data types like coded terms, data structures like lists, identifiers), while domain content models correspond to variable domain-level content descriptions (descriptions of information structures such as "microbiology result" rather than descriptions of actual real-world phenomena such as infection by a microbe). This separation is not generally well understood historically; much domain-level semantics has been hard-wired into software and databases, leading to relatively unmaintainable systems.

By clearly separating the three categories -- information models, domain content models, and terminologies -- the openEHR architecture enables each to have a well-defined, limited scope and clear interfaces. This limits interdependence of each upon the other, leading to more maintainable and adaptable systems.

#### 4.1.1. Multi-level Modelling and Archetypes

One of the key paradigms on which openEHR is based is known as multi-level modelling. Under the multi-level approach, three levels of models are required for a system:

- **reference model (RM)**: a stable reference information model constitutes the first level of modelling;
- **re-usable content element definitions**: formal definitions of clinical content data points and groups, in the form of archetypes;
- **context-specific data set definitions**: formal definitions of use-case specific data sets used for forms, documents, messages etc, created by combining required elements of relevant archetypes into openEHR templates.

Only the first level (the Reference Model) is implemented in software, significantly reducing the dependency of deployed systems and data on variable content definitions. The only other parts of the model universe implemented in software are highly stable languages/models of representation. As a consequence, systems have the possibility of being far smaller and more maintainable than "single-level" systems, in which all semantics are expressed in one model (typically a UML class model or DB schema). Archetype-based systems are also inherently self-adapting, since they are built to consume archetypes and templates as they are developed into the future.

Archetypes and templates act as a well-defined semantic gateway to terminologies, classifications and computerised clinical guidelines. The alternative in the past has been to try to make systems function solely with a combination of hard-wired software and terminology. This approach is flawed, since terminologies do not contain definitions of domain content (e.g. "microbiology result"), but rather facts about the real world (e.g. kinds of microbes and the effects of infection in humans); they are ontological artifacts, whereas archetypes are epistemological artifacts.

The use of archetyping in openEHR engenders new relationships between information and models. With the use of multi-level modelling, runtime data now conform semantically to archetypes as well as concretely to the reference model. All archetypes are expressed in a generic Archetype Definition Language (ADL), which is the basis of ISO standard 13606-2.

The details of how archetypes and templates work in openEHR are described in Section 10.

#### 4.1.2. Consequences for Software Engineering

Multi-level modelling significantly changes the dynamics of the systems development process. In the usual IT-intensive process, requirements are gathered via ad hoc discussions with users (typically via the well-known "use case" methodology), designs and models built from the requirements, implementation proceeds from the design, followed by testing and deployment and ultimately the maintenance part of the lifecycle. This is usually characterised by ongoing high costs of implementation change and/or a widening gap between system capabilities and the requirements at any moment. The approach also suffers from the fact that ad hoc conversations with systems users nearly always fails to reveal underlying content and workflow.

Under the multi-level paradigm, the core part of the system is based on the reference and archetype models (includes generic logic for storage, querying, caching etc.), both of which are extremely stable, while domain semantics are mostly delegated to domain specialists who work building archetypes (reusable), templates (local use) and terminology (general use). Within this process, IT developers concentrate on generic components such as data management and interoperability, while groups of domain experts work outside the software development process, generating definitions that are used by systems at runtime.

Clearly applications cannot always be totally generic (although many data capture and viewing applications are); decision support, administrative, scheduling and many other applications still require custom engineering. However, all such applications can now rely on an archetype- and template-driven computing platform. A key result of this approach is that archetypes now constitute a technology-independent, single-source expression of domain semantics, used to drive database schemas, software logic, GUI screen definitions, message schemas and all other technical expressions of the semantics.

### 4.2. Separation of Responsibilities

A second design paradigm used in openEHR is that of separation of responsibilities within the computing environment. Complex domains are only tractable if the functionality is first partitioned into broad areas of interest, meaning into a "system of systems". This principle has been understood in computer science for a long time under the rubrics "low coupling", "encapsulation" and "componentisation", and was the driver for the explosion of object-oriented languages, libraries and frameworks.

When applied to larger systems, such as that needed to run a hospital or regional health network, the modern form of the paradigm is Services Oriented Architecture (SOA), whereby the components of the system are coarse-grained services. In this approach, each area of functionality is formally modelled and implemented as a self-standing service with a defined interface.

A healthcare services environment contains services at three deployment levels: provider organisation (hospital, clinic, etc); care network (e.g. regional health service, but also non-geographical HMO); and national. These levels may be understood as relating to three perspectives of care:

- **healthcare delivery**: what happens at a provider enterprise, such as a clinic or hospital;
- **continuity of care**: the passage of the patient through multiple clinics and encounters to achieve a care process designed to fulfill a goal;
- **healthcare system**: the perspective of a national healthcare system, including public health, planning, quality reporting, etc.

Within each of these deployment levels there are semantic categories corresponding to data, information, process (planning and logistics) and analytics. From left to right, the services are classified according to what kind of entity they are concerned with: single patient, healthcare professional (HCP), provider enterprise, or knowledge.

E-health services at the care network level are emerging, and in many geographies and health organisations, most of the services shown at this level are available only within provider organisations.

The scope of openEHR in terms of services is primarily as follows:

- patient-centric services at the data and process levels in any deployment level;
- enterprise-centric services within a care network or provider organisation;
- knowledge services relating to models of content and process.

Since there are standards available for some aspects of many services, such as terminology, imaging, messages, EHR Extracts, service-based interoperation, and numerous standards for details such as date/time formats and string encoding, the openEHR specifications sometimes act as a mechanism to adapt and integrate existing standards.

### 4.3. Separation of Viewpoints

The third computing paradigm used in openEHR is a natural consequence of the separation of responsibilities, namely the separation of viewpoints. When responsibilities are divided up among distinct components, it becomes necessary to define a) the information that each processes, and b) how they will communicate. These two aspects of models constitute the two central "viewpoints" of the ISO RM/ODP model:

- **Enterprise**: concerned with the business activities, i.e. purpose, scope and policies of the specified system.
- **Information**: concerned with the semantics of information that needs to be stored and processed in the system.
- **Computational**: concerned with the description of the system as a set of objects that interact at interfaces -- enabling system distribution.
- **Engineering**: concerned with the mechanisms supporting system distribution.
- **Technological**: concerned with the detail of the components from which the distributed system is constructed.

The openEHR specifications accordingly include an information viewpoint -- the openEHR Reference Model -- and a computational viewpoint -- the openEHR Service Model. The Engineering viewpoint corresponds to the openEHR Implementation Technology Specifications (ITS), while the Technological viewpoint corresponds to the technologies and components used in an actual deployment. An important aspect of the division into viewpoints is that there is generally not a 1:1 relationship between model specifications in each viewpoint. For example, there might be a concept of "health mandate" in the enterprise viewpoint. In the information viewpoint, this might have become a model containing many classes. In the computational viewpoint, the information structures defined in the information viewpoint are likely to recur in multiple services, and there may or may not be a "health mandate" service. The granularity of services defined in the computational viewpoint corresponds most strongly to divisions of function in an enterprise or region, while the granularity of components in the information viewpoint corresponds to the granularity of mental concepts in the problem space, the latter almost always being more fine-grained.

---

## 5. openEHR Specification Structure

### 5.1. Overview

This section provides an overview of the specifications of the openEHR platform components (i.e. the components on the left side of the specification program diagram). Each component contains one or more specifications, which come in three types:

- language specifications, expressed in Antlr and/or other formal grammars;
- information models, expressed in UML;
- service models (APIs), expressed in UML.

The specifications are published as generated documents consisting of text and various formal elements including:

- class texts extracted from UML models;
- diagrams extracted from UML models;
- grammar files, typically in Antlr4 syntax;
- EBNF grammars.

The ITS component consists of concrete artefacts of various forms including:

- API definitions (JSON / Swagger / Apiary etc).
- XML schemas;
- JSON schemas;
- BMM schemas.

### 5.2. Consolidated Package Structure

From the software engineering point of view, the consolidated structure of UML packages from the formal specifications that contain them is useful. The top-level packages include: `base`, `lang`, `rm`, `am`, `proc` and `sm`. All packages defining detailed models appear inside one of these outer packages, which are conceptually defined within the `org.openehr` namespace (also represented in UML as packages). In some implementation technologies (e.g. Java / Maven), the `org.openehr` namespace is formally used.

These packages do not include the specifications for various languages (ADL, AQL, ODIN etc), identification systems, or downstream implementation technology specifications (ITSs), which are included in the corresponding component or else in other components.

[Figure 8. Consolidated Package Structure of openEHR]

### 5.3. Base Component (BASE)

The correspondence between the openEHR BASE component specifications and the UML packages is illustrated below. The BASE specifications consist of two UML model-based specifications. These packages fall within the top-level `org.openehr.base` UML package.

[Figure 9. BASE Component of openEHR]

The `base` package defines identifiers, data types, data structures and various common design patterns that can be re-used ubiquitously in the `rm`, `am` and `sm` packages.

[Figure 10. Structure of `org.openehr.base` package]

> **Note**: In RM Release 1.0.3 and earlier releases, the contents of the `base` package resided in the RM `support` package.

#### 5.3.1. Foundation Types

The Foundation Types specification provides a guide for integrating openEHR models proper into the type systems of implementation technologies. It is specified by the `foundations_types` package. This contains the special package `primitive_types`, which describes inbuilt types _assumed_ by openEHR in external type systems. This provides a basis for determining mappings from openEHR to programming languages. For example `String._is_empty_` in openEHR might be mapped to `String._empty()_` in a programming environment.

Other foundation types include basic structures (`Array<T>`, `Hash<K,V>` etc), time types, and various types enabling functional concepts (principally lambda expressions) to be expressed in the openEHR specifications.

#### 5.3.2. Base Types

The Base Types specification defines generic openEHR types used in other openEHR components. It is comprised of the `definitions`, `identification`, `terminology` and `measurement` sub-packages. The semantics defined in these packages allow all other models to use identifiers and to have access to knowledge services like terminology and other reference data.

#### 5.3.3. Resource Model

The Resource Model specification defines a generic 'authored resource' class that carries meta-data relating to:

- authorship;
- copyright, licences and other related meta-data;
- languages and translations;
- annotations.

The class is used via inheritance to provide types in other models with meta-data to enable instances to be managed as resources with appropriate meta-data.

### 5.4. Languages Component (LANG)

> **Note**: Until BASE Release 1.1.0, the contents of the LANG component resided in the BASE component.

The Languages component contains specifications for a number of generic languages used in openEHR, as follows:

- **ODIN**: an object data syntax used in openEHR archetypes (in ADL format), in BMM schemas and generally as a data representation where convenient;
- **BMM**: the Basic-Meta Model, a formal, human-readable meta-model language in which other models may be expressed for use with tools;
- **EL**: Expression Language, a small specification of predicate logic expressions used in other openEHR specifications.

[Figure 11. LANG Component of openEHR]

#### 5.4.1. Basic Meta-Model (BMM)

The BMM specification defines a generic meta-model, suitable for formally expressing object-oriented models, including those of openEHR (RM etc). It is roughly an equivalent of UML's XMI, but fixes various problems with the latter around generic (template) types, while being significantly less complex and fragile. BMM models can be expressed in the ODIN syntax or any other regular object syntax (JSON etc), and conveniently edited by hand. BMM files are used within tools such as the openEHR ADL Workbench and some of the openEHR tooling software.

The BMM is primarily intended to reduce complexity for tools that consume reference model definitions, but is not the only way to implement such tools. Similar tools can be based directly on the openEHR published UML models, as long as typing, template types and qualified attributes are properly handled. Another alternative means of working with models is via software library implementations of the relevant models (openEHR Reference Model etc).

Consequently, understanding or use of BMM specification or models based on it is not necessary in order to implement openEHR systems. However BMM provides a convenient format for model processing, e.g. to auto-generate code stubs in a new language.

#### 5.4.2. Object Data Instance Notation (ODIN)

The ODIN syntax is used to implement faithful machine serialisation and deserialisation of in-memory object graphs, and is a rough equivalent of JSON, YAML and some kinds of XML. It provides more leaf types than any of these, and also supports in-built typing (required to properly represent dynamic binding of polymorphic attributes) and Xpath-like paths.

#### 5.4.3. Expression Language (EL)

The openEHR expression language (EL) is a formal specification of a subset of first order predicate logic expressions, establishing the formal basis for such expressions in ADL archetypes, GDL guidelines and the Task Planning specification.

### 5.5. Reference Model Component (RM)

The openEHR RM component contains all UML model-based specifications.

[Figure 12. RM Component of openEHR]

The `rm` package structure contains packages in two categories:

- _domain-related_: `ehr`, `demographic`, `ehr_extract`, `composition`, `integration`;
- _generic_: `common`, `data_structures`, `data_types`, `support`.

The packages in the latter group are generic, and are used by all openEHR models, in all the outer packages. Together, they provide identification, access to knowledge resources, data types and structures, versioning semantics, and support for archetyping. The packages in the first group define the semantics of enterprise level health information types, including the EHR and demographics.

[Figure 13. Structure of `org.openehr.rm` package]

Each outer package corresponds to one openEHR specification document (with the exception of the EHR and Composition packages, which are both described in the EHR Reference Model document), documenting an "information model" (IM). The package structure will normally be replicated in all ITS expressions, e.g. XML schema, programming languages like Java, C# and Eiffel, and interoperability definitions like WSDL, IDL and .Net.

#### 5.5.1. Package Overview

##### 5.5.1.1. Support Information Model

> **Note**: this part of the RM has been moved to the BASE component; see above.

##### 5.5.1.2. Data Types Information Model

A set of clearly defined data types underlies all other models, and provides a number of general and clinically specific types required for all kinds of health information. The following categories of data types are defined in the data types reference model:

- **Basic types**: boolean, state variable.
- **Text**: plain text, coded text, paragraphs.
- **Quantities**: any ordered type including ordinal values (used for representing symbolic ordered values such as "+", "++", "+++"), measured quantities with values and units, and so on; includes Date/times - date, time, date-time types, and partial date/time types.
- **Encapsulated data**: multimedia, parsable content.
- **TIME_specification**: types for specifying times in the future, mainly used in medication orders, e.g. '3 times a day before meals'.
- **Uri**: Unique Resource Identifiers.

##### 5.5.1.3. Data Structures Information Model

In most openEHR information models, generic data structures are used for expressing content whose particular structure will be defined by archetypes. The generic structures are as follows:

- **Single**: single items, used to contain any single value, such as a height or weight.
- **List**: linear lists of named items, such as many pathology test results.
- **Table**: tabular data, including unlimited and limited length tables with named and ordered columns, and potentially named rows.
- **Tree**: tree-shaped data, which may be conceptually a list of lists, or other deep structure.
- **History**: time-series structures, where each time-point can be an entire data structure of any complexity, described by one of the above structure types. Point and interval samples are supported.

##### 5.5.1.4. Common Information Model

Several concepts that recur in higher level packages are defined in the `common` package. For example, the classes `LOCATABLE` and `ARCHETYPED` provide the link between information and archetype models. The classes `ATTESTATION` and `PARTICIPATION` are generic domain concepts that provide a standard way of documenting involvement of clinical professionals and other agents with the EHR, including signing.

The `change_control` package defines a formal model of change management and versioning which applies to any service that needs to be able to supply previous states of its information, in particular the demographic and EHR services. The key semantics of versioning in openEHR are described in the Versioning section.

##### 5.5.1.5. Security Information Model

The Security Information Model defines the semantics of access control and privacy setting for information in the EHR.

##### 5.5.1.6. EHR Information Model

The EHR IM includes the `ehr` and `composition` packages, and defines the containment and context semantics of the key concepts `EHR`, `COMPOSITION`, `SECTION`, and `ENTRY`. These classes are the major coarse-grained components of the EHR, and correspond directly to the classes of the same names in ISO 13606-1:2005 and fairly closely to the 'levels' of the same names in the HL7 Clinical Document Architecture (CDA) release 2.0.

##### 5.5.1.7. EHR Extract Information Model

The EHR Extract IM defines how an EHR extract is built from `COMPOSITIONs`, demographic, and access control information from the EHR. A number of Extract variations are supported, including "full openEHR", a simplified form for integration with ISO 13606, and an openEHR/openEHR synchronisation Extract.

##### 5.5.1.8. Integration Information Model

The Integration model defines the class `GENERIC_ENTRY`, a subtype of `ENTRY` used to represent freeform legacy or external data as a tree. This Entry type has its own archetypes, known as "integration archetypes", which can be used in concert with clinical archetypes as the basis for a tool-based data integration system. See Section 14 for more details.

##### 5.5.1.9. Demographics Information Model

The demographic model defines generic concepts of `PARTY`, `ROLE` and related details such as contact addresses. The archetype model defines the semantics of constraint on `PARTYs`, allowing archetypes for any type of person, organisation, role and role relationship to be described. This approach provides a flexible way of including the arbitrary demographic attributes allowed in the OMG HDTF PIDS standard.

### 5.6. Archetype Model Component (AM)

[Figure 14. AM Component of openEHR]

The openEHR `am` package contains the models necessary to describe the semantics of archetypes and templates, and their use within openEHR. There are currently two extant major versions of archetype technology in openEHR: 'ADL 1.4', the original version, and 'ADL 2', a more modern version, which is slowly being adopted. Both versions are maintained side by side, to enable implementers to work with the version(s) that suit their needs.

In both versions, the Archetype Model consists of ADL, the Archetype Definition Language (expressed in the form of a syntax specification), and the Archetype Object Model (AOM), a structured model of archetypes.

[Figure 15. Structure of the ADL 2 version `org.openehr.am` package]

[Figure 16. Structure of the ADL 1.4 `org.openehr.am` package]

Another key specification is the Archetype Identification specification, which defines semantics for archetype identifiers, versioning and life-cycle. The formal specifications may be found on the Archetype Model index page.

### 5.7. Service Model (SM)

The openEHR service model includes definitions of basic services in the health information environment, centred around the EHR. The set of services actually included is evolving over time.

[Figure 17. Structure of the `org.openehr.sm` package]

#### 5.7.1. Definitions Service

The Definitions Service defines the interface to online repositories of archetypes, templates and AQL queries, and can be used both by GUI applications designed for human browsing as well as access by other software services such as the EHR.

#### 5.7.2. EHR Service

The EHR Service defines the coarse-grained interface to electronic health record service. The level of granularity is openEHR Contributions and Compositions, i.e. a version-control / change-set interface.

Part of the model defines the semantics of server-side querying, i.e. queries which cause large amounts of data to be processed, generally returning small aggregated answers, such as averages, or sets of ids of patients matching a particular criterion.

#### 5.7.3. Query Service

The Query Service defines the interface via which AQL queries which may be stored via the Definitions Service, or ad hoc, can be executed.

#### 5.7.4. Terminology Interface

The Terminology Service provides the means for all other services to access any terminology available in the health information environment, including basic classification vocabularies such as ICDx and ICPC, as well as more advanced ontology-based terminologies. Following the concept of division of responsibilities in a system-of-systems context, the Terminology Service abstracts the different underlying architectures of each terminology, allowing other services in the environment to access terms in a standard way. The Terminology Service is thus the gateway to all ontology- and terminology-based knowledge services in the environment, which along with services for accessing guidelines, drug data and other "reference data" enables inferencing and decision support to be carried out in the environment.

### 5.8. Global View

The global view shows all of the openEHR specifications, i.e. object models, languages and APIs, arranged by component. This view abstracts away the components and top-level UML packages, providing a useful aide memoire picture of the totality of openEHR specifications. Dependencies only exist from higher elements to lower elements. The CNF and ITS components are separated since they are semantically derivative from the primary specifications, but are primary artefacts for downstream software engineering use. The other usable software artefact comes in the form of class libraries directly implementing the formal specifications.

[Figure 18. openEHR Components and specifications - global view]

---

## 6. Design of the openEHR EHR

### 6.1. The EHR System

The notion of a logical EHR _system_ is central to the openEHR architecture. In openEHR, a system is understood as a distinct logical repository corresponding to an organisational entity that is _legally responsible_ for the management and governance of the healthcare data contained within. This may be a regional health service that serves multiple provider enterprises or a single provider enterprise such as a larger hospital. The 'system' is therefore in general distinct from specific applications and also from provider organisations, even if in some cases it happens to be owned by a single provider. It is also distinct from any underlying virtualisation infrastructure or cloud computing facility, which may house multiple logical EHR systems in a multi-tenant fashion. This is clear by comparing the contractual responsibilities of the infrastructure provider, which are for _generic IT service management_, to a procurer (e.g. a healthcare data management entity). It is the latter that undertakes legal responsibility for the content, on behalf of one or more healthcare provider organisations.

The technical criterion for identifying an EHR system is that it is the entity that assigns version identifiers within a repository.

#### 6.1.1. System Identity

Within the openEHR architecture, a `_system_id_` attribute is recorded both within each patient EHR (`EHR` class), and also within the audit created with each commit of data to an EHR (`AUDIT_DETAILS` class). It is also used in feeder system audits that record the origin of imported data (`FEEDER_AUDIT_DETAILS` class). This identifier identifies the logical EHR system as described above, and may be of any form. Common forms include the reverse domain name and plain and structured string identifiers.

The system identifier is _not assumed to be directly processable_, but may instead be used as a key, for example in a service maintaining location information.

#### 6.1.2. Information Architecture

In informational terms, a minimal EHR system based on openEHR consists of an EHR repository, an archetype repository, terminology (if available), and demographic/identity information.

[Figure 19. Minimal openEHR EHR System]

The latter may be in the form of an existing PMI (patient master index) or other directory, or it may be in the form of an openEHR demographic repository. An openEHR demographic repository can act as a front end to an existing PMI or in its own right. Either way it performs two functions: standardisation of demographic information structures and versioning. An openEHR EHR contains references to entities in whichever demographic repository has been configured for use in the environment; the EHR can be configured to include either no demographic or some identifying data. One of the basic principles of openEHR is the complete separation of EHR and demographic information, such that an EHR taken in isolation contains little or no clue as to the identity of the patient it belongs to. The security benefits are described below. In more complete EHR systems, numerous other services (particularly security-related) would normally be deployed.

### 6.2. Top-level Information Structures

The openEHR information models define information at varying levels of granularity. Fine-grained structures defined in the Support and Data types are used in the Data Structures and Common models; these are used in turn in the EHR, EHR Extract, Demographic and other 'top-level' models. These latter models define the 'top-level structures' of openEHR, i.e. content structures that can sensibly stand alone, and may be considered the equivalent of separate documents in a document-oriented system. In openEHR information systems, it is generally the top-level structures that are of direct interest to users. The major top-level structures include the following:

- **Composition**: the committal unit of the EHR (see type `COMPOSITION` in EHR IM);
- **EHR Access**: the EHR-wide access control object (see type `EHR_ACCESS` in EHR IM);
- **EHR Status**: the status summary of the EHR (see type `EHR_STATUS` in EHR IM);
- **Folder hierarchy**: act as directory structures in EHR, Demographic services (see type `FOLDER` in Common IM);
- **Party**: various subtypes including `ACTOR`, `ROLE`, etc. representing a demographic entity with identity and contact details (see type `PARTY` and subtypes in Demographic IM);
- **EHR Extract**: the transmission unit between EHR systems, containing a serialisation of EHR, demographic and other content (see type `EHR_EXTRACT` in EHR Extract IM).

All persistent openEHR EHR, demographic and related content is found within top-level information structures.

### 6.3. The EHR

The openEHR EHR is structured according to a relatively simple model. A central EHR object identified by an EHR id specifies references to a number of types of structured, versioned information, plus a list of Contribution objects that act as audits for changes made to the EHR.

[Figure 20. High-level Structure of the openEHR EHR]

In this figure, the parts of the EHR are as follows:

- **EHR**: the root object, identified by a globally unique EHR identifier;
- **EHR_access (versioned)**: an object containing access control settings for the record;
- **EHR_status (versioned)**: an object containing various status and control information, optionally including the identifier of the subject (i.e. patient) currently associated with the record;
- **Directory (versioned)**: an optional hierarchical structure of Folders that can be used to logically organise Compositions;
- **Folders (versioned)**: additional optional hierarchical folder structures that can be used to logically organise Compositions;
- **Compositions (versioned)**: the containers of all clinical and administrative content of the record;
- **Contributions**: the change-set records for every change made to the health record; each Contribution references a set of one or more Versions of any of the versioned items in the record that were committed or attested together by a user to an EHR system.

The logical structure of a typical Composition is shown in more detail in the next figure. This shows various hierarchical levels from Composition to the data types in a typical arrangement. The 21 data types provide for all types of data needed for clinical and administrative recording.

[Figure 21. Elements of an openEHR Composition]

### 6.4. Entries and Clinical Statements

#### 6.4.1. Entry Subtypes

All clinical information created in the openEHR EHR is ultimately expressed in 'Entries'. An Entry is logically a single _clinical statement_, and may be a single short narrative phrase, but may also contain a significant amount of data, e.g. an entire microbiology result, a psychiatric examination note, a complex medication order. In terms of actual content, the Entry classes are the most important in the openEHR EHR Information Model, since they define the semantics of all the 'hard' information in the record. They are intended to be archetyped, and in fact, archetypes for Entries and sub-parts of Entries make up the vast majority of archetypes defined for the EHR.

The openEHR `ENTRY` classes include five concrete subtypes: `ADMIN_ENTRY`, `OBSERVATION`, `EVALUATION`, `INSTRUCTION` and `ACTION`, of which the latter four are kinds of `CARE_ENTRY`.

[Figure 22. The openEHR Entry model (in EHR IM)]

The choice of these types is based on the clinical problem-solving process (Beale & Heard, 2007).

[Figure 23. Relationship of information types to the investigation process]

This figure shows the cycle of information creation due to an iterative, problem solving process typical not just of clinical medicine but of science in general. The 'system' as a whole is considered to be made up of two parts: the 'patient system' and the 'clinical investigator system'. The latter consists of health carers, and may include the patient (at points in time when the patient performs observational or therapeutic activities), and is responsible for understanding the state of the patient system and delivering care to it. A problem is solved by making observations, forming opinions (hypotheses), and prescribing actions (instructions) for next steps, which may be further investigation, or may be interventions designed to resolve the problem, and finally, executing the instructions (actions).

This process model is a synthesis of Lawrence Weed's 'problem-oriented' method of EHR recording, and later related efforts, including the model of Rector, Nowlan & Kay (1991), and the 'hypothetico-deductive' model of reasoning (see e.g. Elstein, Shulman & Sprafka, 1978). However hypothesis-making and testing is not the only successful process used by clinical professionals - evidence shows that many (particularly those older and more experienced) rely on pattern recognition and direct retrieval of plans used previously with similar patients or prototype models. The investigator process model used in openEHR is compatible with both cognitive approaches, since it does not say how opinions are formed, nor imply any specific number or size of iterations to bring the process to a conclusion, nor even require all steps to be present while iterating (e.g. GPs often prescribe without making a firm diagnosis). Consequently, the openEHR Entry model does not impose a process model, it only provides the possible types of information that might occur.

##### 6.4.1.1. Ontology of Entry Types

In the clinical world practitioners do not think in terms of only five kinds of data corresponding to the subtypes of Entry described above. There are many subtypes of each of these types, of which some are shown in the ontology figure (reproduced from Beale & Heard, 2007).

[Figure 24. Ontology of Recorded Information]

The key top-level categories are 'care information' and 'administrative information'. The former encompasses all statements that might be recorded at any point during the care process, and consists of the major sub-categories on which the Entry model is based, namely 'observation', 'opinion', 'instruction', and 'action' (a kind of observation) which themselves correspond to the past, present and future in time. The administrative information category covers information which is not generated by the care process proper, but relates to organising it, such as appointments and admissions. This information is not about care, but about the logistics of care delivery. Regardless of the diversity, each of the leaf-level categories shown in this figure is ultimately a sub-category of one of the types from the process model, and hence, of the subtypes of the openEHR Entry model.

Correct representation of the categories from the ontology is enabled by using archetypes designed to express the information of interest (say a risk assessment) in terms of a particular Entry subtype (in this case, Evaluation). In a system where Entries are thus modelled, there will be no danger of incorrectly identifying the various kinds of Entries, as long as the Entry subtype, time, and certainty/negation are taken into account.

##### 6.4.1.2. Clinical Statement Status and Negation

A well-known problem in clinical information recording is the assignment of 'status' to recorded items. Kinds of status include variants like "actual value of P" (P stands for some phenomenon), "family history of P", "risk of P", "fear of P", as well as negation of any of these, i.e. "not/no P", "no history of P" etc. A proper analysis of these so called statuses shows that they are not "statuses" at all, but different categories of information as per the ontology of recorded information. In general, negations are handled by using "exclusion" archetypes for the appropriate Entry type. For example, "no allergies" can be modelled using an Evaluation archetype that describes which allergies are excluded for this patient. Another set of statement types that can be confused in systems that do not properly model information categories concern interventions, e.g. "hip replacement (5 years ago)", "hip replacement (recommended)", "hip replacement (ordered for next Tuesday 10 am)".

All of these statement types map directly to one of the openEHR Entry types in an unambiguous fashion, ensuring that querying of the EHR does not match incorrect data, such as a statement about fear or risk, when the query was for an observation of the phenomenon in question.

Further details on the openEHR model clinical information are given in the EHR IM document, Entry Section.

### 6.5. Managing Interventions

A key part of the investigation process, and indeed healthcare in general, is intervention. Specifying and managing interventions (whether the simplest prescriptions or complex surgery and therapy) is a hard problem for information systems because it is in 'future time' (meaning that intervention activities have to be expressed using branching/looping time specifications, not the simple linear time of observations), unexpected events can change things (e.g. patient reaction to drugs), and the status of a given intervention can be hard to track, particularly in distributed systems. However, from the health professional's point of view, almost nothing is more basic than wanting to find out: what medications is this patient on, since when, and what is the progress? The openEHR approach to these challenges is to use the Entry type `INSTRUCTION`, its subpart `ACTIVITY` to specify interventions in the future, and the Entry subtype `ACTION` to record what has actually happened. A number of important features are provided in this model, including:

- a single, flexible way of modelling all interventions, whether they be single drug medication orders or complex hospital-based therapies;
- a way of knowing the state of any intervention, in terms of the states in a standard state machine; this allows a patient's EHR to be queried in a standard way so as to return "all active medications", "all suspended interventions" etc.;
- a way of mapping particular care process flow steps to the standard state machine states, enabling health professionals to define and view interventions in terms they understand;
- support for automated workflow, without requiring it.

Coupled with the comprehensive versioning capabilities of openEHR, the Instruction/Action design allows clinical users of the record to define and manage interventions for the patient in a distributed environment.

[Figure 25. openEHR standard Instruction State Machine]

### 6.6. Time in the EHR

Time is well-known as a challenging modelling problem in health information. In openEHR, times that are a by-product of the investigation process (e.g. time of sampling or collection; time of measurement, time of a healthcare business event, time of data committal) are concretely modelled, while other times specific to particular content (e.g. date of onset, date of resolution) are modelled using archetyping of generic data attributes. The following figure shows a typical relationship of times with respect to the observation process, and the corresponding attributes within the openEHR reference model. Note that under different scenarios, such as GP consultation, radiology reporting and others, the temporal relationships may be quite different than those shown in the figure.

[Figure 26. Time in the EHR]

### 6.7. Language

In some situations, there may be more than one language used in the EHR. This may be due to patients being treated across borders (common among the Scandinavian countries, between Brazil and northern neighbours), or due to patients being treated while travelling, or due to multiple languages simply being used in the home environment.

Language is handled as follows in the openEHR EHR. The default language for the whole EHR is determined from the operating system locale. It may be included in the EHR_status object if desired. Language is then mandatorily indicated in two places in the EHR data, namely in Compositions and Entries (i.e. Observations, etc), in a language attribute. This allows both Compositions of different languages in the EHR, and Entries of different languages in the same Composition. Additionally, within Entries, text and coded text items may optionally have language recorded if it is different from the language of the enclosing Entry, or where these types are used within other non-Entry structures that don't indicate language.

The use of these features is mostly likely to occur due to translation, although in some cases a truly multi-lingual environment might exist within the clinical encounter context. In the former case, some parts of an EHR, e.g. particular Compositions will be translated before or after a clinical encounter so as to make the information available in the primary language of the EHR. The act of translation (like any other interaction with the EHR) will cause changes to the record, in the form of new Versions. New translations can conveniently be recorded as branch versions, attached to the version of which they are a translation. This is not mandatory, but provides a convenient way to store translations so that they don't appear to replace the original content.

---

## 7. Security and Confidentiality

### 7.1. Requirements

#### 7.1.1. Privacy, Confidentiality and Consent

Privacy represents the right to restrict access to personal information, while confidentiality refers to the obligation others must respect regarding disclosed data. A fundamental principle in e-Health systems holds that information patients provide to healthcare professionals should only be shared with additional parties upon patient consent.

Patients may require differential access permissions to different sections of their health records. For instance, a patient might permit broad access to most of their record while restricting visibility to sensitive areas such as mental health or sexual health information. However, health information interconnection creates complications -- medication lists often reveal conditions even when diagnoses remain hidden, yet clinicians require this information for safe treatment delivery.

#### 7.1.2. Requirements of Healthcare Providers

Clinical professionals need rapid access to relevant patient information and verification that displayed data accurately reflects documented information. Emergency situations sometimes necessitate access by otherwise unrelated healthcare providers, requiring general consent mechanisms rather than case-by-case approval.

Healthcare researchers require access to numerous patient records for care evaluation, improvement, and educational purposes. These research and learning needs represent patient and societal interests. Healthcare systems must therefore balance individual consent principles with broader institutional knowledge development.

#### 7.1.3. Specifying Access Control

Direct identification offers a theoretical access control approach -- patients could designate specific providers or exclude particular individuals. However, this method becomes impractical at scale, particularly within large healthcare settings employing numerous staff. Emerging e-prescribing and e-pharmacy systems will further expand the numbers of health professionals involved in patient care delivery.

Additionally, mobile populations -- military personnel, entertainers, international business professionals, athletes -- cannot predict which nation may provide their care. This reality necessitates access control mechanisms based on role categories rather than individual identification alone.

#### 7.1.4. The Problem of Roles

Defining "roles" for access control purposes presents significant challenges. While some labels seem straightforward -- "nurse," "GP," "psychiatrist" -- the more functionally important distinctions concern relationships to current care processes: primary providers versus general care staff versus support personnel such as pathologists.

Determining individual categorical assignment proves difficult across different sites and jurisdictions. Realistically, translating role categories like "care deliverer" into specific identities requires institution-level knowledge, not centralized EHR knowledge. Consequently, access decisions carry dependencies on provider-site awareness regarding staff participation in specific patient care.

Role-based access control faces additional complications from temporary staffing adjustments and role changes. Medical secretaries employed by physicians may require access to sensitive record sections, creating situations where non-clinically trained individuals gain high-level access. Real-world clinical practice messiness must therefore inform rather than contradict access control systems.

#### 7.1.5. Usability

Security and privacy mechanisms must prioritize usability. Theoretically elegant access control solutions may prove impractical if they require excessive learning time, consume too much clinical time during usage, or demand overly complex software implementation, potentially compromising safety.

### 7.2. Threats to Security and Privacy

openEHR assumes the following security threats require mitigation (where "inappropriate" signifies lack of patient consent):

- Human errors in patient identification potentially causing health data from one patient to enter another's record, resulting in privacy violations and clinical errors, or creating duplicate patient records from incomplete data associations;
- Inappropriate healthcare professional access or other care environment workers not involved in current patient care;
- Inappropriate access by known individuals such as family members;
- Inappropriate organizational access for insurance discrimination or similar corporate purposes;
- Malicious data theft targeting individuals such as celebrities or politicians;
- Standard data integrity and availability threats including viruses, worms, and denial-of-service attacks;
- Software failures from bugs, misconfiguration, or interoperability problems causing data corruption, display errors, or computational mistakes resulting in clinical harm.

A guiding principle for security mechanisms reflects that "the likelihood of any given mode of targeted inappropriate access is proportional to the perceived value of the information and inversely proportional to the cost of access." Rather than relying solely on complex technological solutions, openEHR implements relatively straightforward mechanisms that increase access difficulty without compromising availability.

### 7.3. Solutions Provided by openEHR

#### 7.3.1. Overview

Concrete security and privacy mechanisms typically reside in system deployments rather than specifications like openEHR. Implementation choices regarding authentication, access control, and encryption vary substantially based on deployment requirements -- secure local area networks require minimal internal security, whereas web-accessible health record servers demand different approaches.

openEHR supports key requirements with sufficient flexibility enabling deployments with substantially different needs to implement basic principles standardly. The architecture specifies certain security measures directly, including separation of EHR and demographic data, an EHR-wide access control object, and versioned object features supporting commit audits, digital signatures, and hashes.

#### 7.3.2. Security Policy

openEHR imposes a minimal security policy profile representing necessary but generally insufficient requirements for deployed systems. Additional implementation would occur in layers whose semantics fall outside openEHR specification.

##### 7.3.2.1. General

**Indelibility**: Health record information cannot be deleted; logical deletion occurs through version control marking data as deleted rather than physical removal.

**Audit trailing**: All EHR changes -- including content objects, EHR status, and access control objects -- are audit-trailed with user identity, timestamp, reason, optional digital signature, and version information. Patient-initiated modifications may employ symbolic identifiers rather than explicit user identification.

**Anonymity**: The EHR may be maintained without demographic links to national registries or healthcare numbers. This capability enables completely anonymous records. Additionally, the EHR design separates demographic information completely, such that standalone EHRs contain minimal patient identity indicators, reducing privacy risks.

##### 7.3.2.2. Access Control

An EHR-level access control object (`EHR_ACCESS`) defines record-wide access policies. This object remains version-controlled, enabling historical access control tracking. Access control policies may reference role categories without requiring specific individual identification within EHR structures.

#### 7.3.3. Integrity

##### 7.3.3.1. Versioning

Versioning provides fundamental integrity support. Every EHR data modification creates a new version while preserving previous versions. This enables data change tracking, corruption detection, and recovery. The versioning system supports auditing modifications while maintaining complete historical records.

##### 7.3.3.2. Digital Signature

Digital signatures may be applied to versioned items, providing authentication and non-repudiation. Cryptographic hashing enables corruption detection. These mechanisms operate optionally, allowing deployment flexibility while providing available integrity assurance methods.

#### 7.3.4. Anonymity

The complete separation between EHR and demographic repositories enables multiple anonymity approaches. Fully anonymous records contain no demographic links. Pseudonymous records maintain identifiers enabling re-identification through external systems without internal demographic associations. Records may also support varying anonymity levels across different sections.

### 7.4. Access Control

#### 7.4.1. Overview

openEHR access control reflects the principle that role-based mechanisms must accommodate real-world healthcare complexity rather than theoretical purity. Systems implementing openEHR may employ various access control strategies -- from simple database-level controls to sophisticated policy-based systems -- while maintaining consistent openEHR semantic foundations.

---

## 8. Versioning

### 8.1. Overview

Versioning constitutes a fundamental openEHR architecture component, providing change tracking, audit support, integrity assurance, and recovery capabilities. Every modification to persistent EHR, demographic, and related content generates a new version, with previous versions remaining accessible.

### 8.2. The Configuration Management Paradigm

#### 8.2.1. Organisation of the Repository

openEHR versioning follows configuration management principles used in software engineering. Within an EHR repository, items exist as versioned objects. Each object modification creates a new version while retaining previous versions. A parent-child relationship exists between successive versions, forming version trees.

Version identifiers uniquely specify version instances within an object's version history. These identifiers typically include object identification and version sequence information. The repository maintains complete version histories, enabling comprehensive historical queries and change tracking.

#### 8.2.2. Change Management

Changes to versioned objects occur through contribution objects. A contribution represents an atomic change set -- one or more related modifications committed together, typically during a single session. Contributions maintain audit information including user identity, timestamp, and modification reason.

Contributions support logical grouping of related changes. For instance, a clinical session might generate multiple data modifications grouped within a single contribution. This structure enables meaningful change tracking at appropriate granularity levels.

### 8.3. Managing Changes in Time

#### 8.3.1. General Model of a Change-controlled Repository

A generalized change-controlled repository model establishes versioning semantics applicable across openEHR systems. Each persistent object maintains a version history -- a sequence of versions corresponding to successive object modifications. Version identifiers specify unique version instances.

The repository tracks creation and modification times for each version. Audit information associates each version with the user who created it, the timestamp of creation, and modification rationale. This audit trail enables comprehensive tracking of who made what changes when.

Change semantics support querying at any historical time point. Systems can reconstruct past data states, enabling temporal queries such as "what was the medication list on this past date?" This historical reconstruction capability supports both clinical review and research requirements.

### 8.4. The Virtual Version Tree

Version history organization follows tree structures enabling representation of complex modification scenarios. Linear version sequences represent straightforward cases where each new version directly succeeds the previous one. However, branching occurs when multiple versions emerge from a single predecessor.

Branching scenarios include creation of translations maintained alongside original content, parallel modifications in distributed systems, or alternative clinical decision pathways. Version trees accommodate these patterns while maintaining complete historical records.

The virtual version tree concept enables unified representation of version histories across distributed systems. When EHR data synchronizes between systems, version trees merge appropriately, preserving historical information while establishing relationships between versions from different sources.

---

## 9. Identification

### 9.1. Identification of the EHR

The openEHR EHR is identified by a unique EHR identifier that is assigned at creation time and never changes. This identifier is globally unique and serves as the primary key for locating and accessing a specific patient's EHR within a system or across systems.

### 9.2. Identification of Items within the EHR

#### 9.2.1. General Scheme

Items contained within the EHR are identified using a hierarchical identification scheme that builds upon the EHR identifier. Each versioned item within an EHR has its own unique identifier, and within those items, individual data elements can be located using paths and further identifiers.

The identification scheme supports multiple levels of granularity, allowing both high-level structures (such as Compositions) and fine-grained data elements to be uniquely identified and referenced.

#### 9.2.2. Levels of Identification

Identification operates at several distinct levels within the openEHR architecture:

- **EHR Level**: The top-level EHR object is identified by a unique EHR identifier.
- **Versioned Item Level**: Major information structures within the EHR that are versioned (such as Compositions, EHR Access, EHR Status, and Folder hierarchies) each have unique identifiers within the EHR.
- **Version Level**: Each version of a versioned item has its own identifier that includes information about the version number and parent version.
- **Item Level**: Within versioned items, individual data elements and structures can be identified using object identifiers (uid attributes) where present, combined with path specifications.
- **Attribute Level**: The finest level of identification uses paths to reference specific attributes or values within data structures.

The identification scheme is designed to work seamlessly across distributed systems and to support both temporal and logical references to EHR content. A single identified item can be referenced from multiple locations and in multiple contexts.

---

## 10. Archetypes and Templates

### 10.1. Overview

Archetypes and templates are formal definitions of domain content that work in concert with the openEHR Reference Model to enable system flexibility and maintainability. As described in the multi-level modelling paradigm, archetypes represent the second level of modelling, providing reusable clinical content definitions. Templates represent the third level, defining use-case-specific data sets by combining and constraining archetypes.

The relationship between the Reference Model, archetypes, and templates is fundamental to the openEHR architecture and enables systems to adapt to new clinical requirements without software changes.

### 10.2. Archetype Formalisms and Models

#### 10.2.1. Overview

The openEHR Archetype Model (AM) provides the formal basis for expressing archetypes and templates. Archetypes are expressed using the Archetype Definition Language (ADL), which has two major versions: ADL 1.4 and ADL 2. The underlying semantics are captured in the Archetype Object Model (AOM), which defines the structure and constraints that archetypes can express.

Both ADL versions are actively maintained to support implementers with different needs and deployment scenarios. ADL 2 represents a more modern evolution of the language with enhanced capabilities, while ADL 1.4 remains widely used in existing systems and tools.

#### 10.2.2. Design-time Relationships between Archetypes

Archetypes may have design-time relationships with other archetypes, including specialization, where one archetype refines or constrains the content of a parent archetype. These relationships enable a hierarchical organization of archetypes that reflects the conceptual hierarchy of clinical domains.

Specialization relationships allow for the creation of progressively more specific archetypes that build upon more general ones, supporting both reuse and specialization at the archetype level.

### 10.3. Relationship of Archetypes and Templates to Data

Archetypes and templates define constraints and semantics that runtime data must conform to. Data created in an openEHR system conforms concretely to the Reference Model structures but semantically conforms to one or more archetypes. This dual conformance enables systems to validate data, drive user interfaces, and support querying using archetype-level semantics while maintaining a stable, unchanging Reference Model.

Templates further constrain archetypes for specific use cases, defining exactly which archetype elements are required, optional, or forbidden in particular clinical scenarios. This allows different clinical contexts to use different subsets of a common archetype.

### 10.4. Archetype-enabling of Reference Model Data

The Reference Model provides generic structures for representing clinical content. Archetypes enable these generic structures by specifying what kinds of data can appear in particular contexts. For example, the generic `ENTRY` class in the Reference Model becomes a specific clinical statement (such as a blood pressure observation) through the application of an appropriate archetype.

This archetype-enabling process bridges the gap between generic, reusable reference structures and specific, clinically meaningful information, without requiring changes to the Reference Model itself.

### 10.5. Archetypes, Templates and Paths

Archetypes and templates define the logical structure of clinical content and establish semantic meaning for data elements. This structure is reflected in paths, which are used to locate and reference specific data elements within instances. The paths available within data conform to the constraints defined by applicable archetypes and templates.

Archetype-aware paths include information about the archetype node being referenced, enabling queries and other operations to work at the semantic level rather than just the structural level defined by the Reference Model.

### 10.6. Archetypes and Templates at Runtime

#### 10.6.1. Overview

At runtime, systems use archetypes and templates to guide data capture, validate user input, display information, and support querying. The availability of archetype definitions at runtime enables systems to be self-adapting, incorporating new or modified archetypes without requiring software changes.

#### 10.6.2. Deploying Archetypes and Templates

Archetypes and templates are deployed through a Definitions Service that acts as a repository and access point for archetype definitions. Clinical systems access these definitions at runtime to understand what data structures are available and how to present them to users.

Deployment may occur through centralized repositories accessible to multiple systems, or through local repositories deployed with individual applications. Version control mechanisms ensure that systems using particular archetype versions can continue to do so even as new versions are developed.

#### 10.6.3. Validation during Data Capture

As clinicians enter data into openEHR systems, the data is validated against applicable archetypes to ensure conformance. This validation can occur in real-time during data entry, providing immediate feedback to users about data quality and completeness.

Validation may enforce that required elements are present, that values conform to specified constraints, and that the overall structure of entered data matches the archetype definition.

#### 10.6.4. Querying

Archetypes enable semantic querying of the EHR through mechanisms such as the Archetype Query Language (AQL). Queries can reference data elements by their archetype paths rather than only by Reference Model paths, allowing queries to be expressed in clinically meaningful terms that correspond to archetype concepts.

Query results can be filtered, aggregated, and processed based on archetype-defined semantics, enabling sophisticated clinical knowledge discovery and decision support.

### 10.7. The openEHR Archetypes

openEHR maintains a library of archetypes covering major areas of clinical content, developed through collaboration with clinical experts and standards organizations. These archetypes serve as examples and reference implementations of archetype concepts, and many are used directly in deployed systems.

The archetype library is organized into logical groups corresponding to major clinical domains such as vital signs, laboratory results, medications, diagnoses, and procedures. This organization reflects both clinical structure and the organization of existing health information standards and terminologies.

---

## 11. Paths and Locators

### 11.1. Overview

Paths and locators are mechanisms used within openEHR to identify and locate specific items of information within EHR structures. These tools enable precise references to data elements at various levels of granularity within the complex hierarchical structures of health records.

### 11.2. Paths

#### 11.2.1. Basic Syntax

Paths in openEHR follow a structured format enabling navigation through the object model. The basic path syntax uses forward slashes to separate levels in the hierarchy, similar to file system paths. Paths can reference any point within a data structure, from the top-level EHR down to individual data values.

#### 11.2.2. Predicate Expressions

##### 11.2.2.1. Overview

Predicates are expressions used to refine paths by specifying conditions that must be met. They allow selection of specific items from lists or other collections based on various criteria. Multiple types of predicates are available to suit different identification needs.

##### 11.2.2.2. Archetype path Predicate

The archetype path predicate uses archetype identifiers to locate items. This form of predicate references the archetype ID of the item being identified, allowing precise specification even when multiple items of the same type exist within a structure.

##### 11.2.2.3. Name-based Predicate

Name-based predicates use the name attribute of items to identify them. This approach works well when items have distinct, meaningful names that serve as reliable identifiers within their context.

##### 11.2.2.4. Other Predicates

Additional predicate types support identification by other means. These may include predicates based on specific attribute values or other distinguishing characteristics of data elements.

#### 11.2.3. Paths within Top-level Structures

Paths can traverse top-level structures such as compositions, entries, and their contents. These paths enable navigation from the highest levels of organization down to the most granular data points. Top-level structures establish clear starting points for path expressions.

#### 11.2.4. Data Paths and Uniqueness

Ensuring uniqueness of paths is essential for unambiguous data access. Multiple strategies exist for achieving unique identification of data items within structures that may contain repeated or similar elements.

##### 11.2.4.1. Using a Uid-based Predicate

Unique identifiers (UIDs) provide a reliable basis for path construction. When items possess unique identifiers, these can be incorporated into predicates to guarantee unambiguous selection of the intended item.

##### 11.2.4.2. Using a Name-based Predicate

Where items possess distinctive names, name-based predicates offer a human-readable alternative to UID-based approaches. This method works effectively when naming conventions ensure that names are unique within their context.

##### 11.2.4.3. Using Positional Parameters

Positional parameters reference items by their order within a collection. This approach counts from the first item in a sequence, though it may be less stable than UID or name-based approaches in dynamic data structures.

### 11.3. EHR URIs

#### 11.3.1. EHR Reference URIs

EHR Reference URIs provide a standardized mechanism for creating location-independent references to EHR content. These URIs can be used across systems to identify specific items without dependence on particular system implementations.

##### 11.3.1.1. EHR Location

The EHR location component of a URI identifies the specific EHR instance being referenced. This typically includes system identification and the patient or subject identifier associated with the EHR.

##### 11.3.1.2. Top-level Structure Locator

The top-level structure locator identifies which category of content within the EHR is being referenced, such as a specific composition, folder, or demographic object. This locator narrows the scope from the entire EHR to a particular content division.

##### 11.3.1.3. Item URIs

Item URIs provide complete, unambiguous references to individual data items. These URIs combine EHR location, top-level structure identification, and path information to create globally unique references.

##### 11.3.1.4. Relative URIs

Relative URIs express references in relation to a base location, reducing verbosity when multiple references share common ancestry. These are useful for communication and reference within bounded contexts.

---

## 12. Terminology in openEHR

### 12.1. Overview

Terminology support in openEHR enables the use of standardized vocabularies, classifications, and coding systems throughout the architecture. The terminology layer provides integration points between formal health information models and the vast landscape of external medical vocabularies and knowledge sources.

### 12.2. Terminology to Support the Reference Model

The reference model itself requires certain terminology to function. This includes standard value sets for data type constraints, code systems for representation of common concepts, and vocabularies for expressing definitional content within the models. These support terminologies enable the RM to be expressed in a system-independent manner.

### 12.3. Archetype Internal Terminology

Archetypes contain internal terminology structures that define the possible values and meanings for clinical data elements. These internal terminologies provide the semantic constraints that transform generic reference model structures into clinically meaningful data definitions. Archetype-level terminology remains independent of external coding systems while providing clear binding points to them.

### 12.4. Binding to External Terminologies

#### 12.4.1. Binding External Terminology Codes to Archetype Codes

Archetypes can bind to external terminologies through formal binding declarations. These bindings map archetype-defined codes to codes from external systems such as SNOMED CT, LOINC, or other standard vocabularies. This allows systems to exchange information using standard codes while internally working with archetype terminology.

##### 12.4.1.1. Binding Terminology Value-sets to Archetypes

Value-set bindings allow entire sets of terminology codes to be associated with archetype data elements. This approach supports queries and reasoning across archetype definitions using external terminology concepts. Value-set bindings provide flexibility in terminology use while maintaining reference to standardized external sources.

### 12.5. Querying using External Terminologies

Queries against EHR data can be formulated using external terminologies directly. The query service resolves external terminology expressions into equivalent internal archetype concepts, enabling queries formulated in standard medical terminology to retrieve relevant clinical data regardless of how that data was originally encoded or stored.

---

## 13. Deployment

### 13.1. 5-tier System Architecture

The openEHR architecture supports deployment through a 5-tier system architecture model. This model organises system components into five logical tiers that separate concerns from data persistence through to user presentation. The tiers provide a framework for understanding how openEHR components map to deployment infrastructure, enabling flexible distribution across different hardware and network configurations.

The five tiers typically correspond to: data/persistence, domain logic/services, application logic, presentation/API, and client/user interface layers. This separation allows each tier to be independently scaled, maintained, and potentially distributed across different physical or virtual infrastructure.

---

## 14. Integrating openEHR with other Systems

### 14.1. Overview

openEHR provides mechanisms to integrate with existing systems through defined approaches. The architecture recognizes that many healthcare environments contain legacy systems and external data sources that must coexist with openEHR implementations. Integration is addressed at both the data level (importing and transforming data) and the service level (interoperating with external services).

### 14.2. Integration Archetypes

Integration archetypes serve as semantic bridges between openEHR and external systems. The Integration Information Model defines the `GENERIC_ENTRY` class, which functions as a subtype of `ENTRY`. This specialized entry type enables representation of unstructured legacy or external data as hierarchical tree structures. Integration archetypes work in conjunction with clinical archetypes, providing a tool-based foundation for data integration systems.

The integration archetype approach allows legacy data to be imported into the openEHR EHR in a controlled fashion. Data arrives via `GENERIC_ENTRY` instances conforming to integration archetypes, and can then be transformed into proper clinical Entry types (OBSERVATION, EVALUATION, etc.) conforming to clinical archetypes. This two-stage process separates the concerns of data capture/import from clinical validation and normalization.

### 14.3. Data Conversion Architecture

The architecture supports data conversion through defined gateways. These conversion mechanisms enable transformation between openEHR's formalized structures and formats used by external systems, facilitating bidirectional data exchange while maintaining semantic integrity. The conversion architecture typically involves:

- Import gateways that receive data from external systems and map it to openEHR structures using integration archetypes;
- Transformation services that convert integration archetype data into clinical archetype data;
- Export gateways that extract openEHR data and transform it into formats required by external systems or standards (e.g., HL7 messages, CDA documents).

---

## 15. Relationship to Standards

### 15.1. Standards by which openEHR can be evaluated

openEHR implementations can be assessed against established healthcare informatics standards including:

- ISO 18308 (Requirements for an Electronic Health Record Architecture)
- ISO 20514 (EHR Definition, Scope and Context)

### 15.2. Standards which have influenced the design of openEHR specifications

The development of openEHR specifications has drawn insights from multiple international standards including:

- ISO 13606 (EHR Communication)
- CEN EN 13606 (European EHR Communication standard)
- HL7v2 and HL7v3 (Health Level Seven messaging and reference information model)
- HL7 CDA (Clinical Document Architecture)
- OMG HDTF (Healthcare Domain Task Force) specifications
- ISO RM/ODP (Reference Model of Open Distributed Processing)

### 15.3. Standards which have influenced the design of openEHR archetypes

Archetype development has incorporated lessons from existing healthcare standards including clinical content standards and terminology systems.

### 15.4. Standards which are used "inside" openEHR

Certain standards are directly incorporated within openEHR specifications and implementations:

- ISO 8601 (Date and time format)
- IETF RFC 3066 (Language tags)
- IETF MIME types
- Unicode / ISO 10646 (Character encoding)
- ISO 13606-2 (Archetype interchange, basis for ADL)
- openPGP (Digital signatures)

### 15.5. Standards which require a conversion gateway

Some healthcare standards cannot be directly mapped to openEHR's native structures and require conversion gateways:

- HL7v2 messages
- HL7 CDA documents
- DICOM (medical imaging)
- EDIFACT-based messaging standards

### 15.6. Generic Technology Standards

openEHR relates to multiple technology standards beyond healthcare-specific specifications:

- XML and XML Schema
- JSON
- REST architectural style
- HTTP/HTTPS
- OAuth2 / OpenID Connect (authentication)
- W3C Web standards

---

## 16. Implementation Technology Specifications

### 16.1. Overview

Implementation Technology Specifications (ITSs) constitute the platform-specific models derived from openEHR's abstract specifications. The ITS component provides concrete technical expressions enabling direct use in software development.

The abstract specifications are expressed in concrete forms through ITSs including:

- REST API specifications (defining the openEHR platform service interfaces)
- XML Schemas (XSDs for RM, AM data serialization)
- JSON Schemas (for RM data serialization)
- BMM schemas (for model processing tools)

These specifications form openEHR's interoperability standards and serve as primary artefacts for downstream software engineering use. They translate abstract information models and service definitions into implementable technical formats.

As implementation technologies evolve, ITS specifications can be updated and replaced while maintaining stability in the primary group of abstract specifications, which generally only change in response to substantive requirements beyond technological considerations.

The ITS specifications currently include:

- **REST APIs**: RESTful service interfaces for EHR, Query, Definition and other services
- **XML ITS**: XML Schema definitions for serializing RM and AM objects
- **JSON ITS**: JSON Schema definitions for serializing RM objects
- **BMM ITS**: BMM schema files expressing the RM and other models

Each ITS artefact maintains a clear traceability relationship back to the abstract specification from which it is derived, ensuring semantic consistency across different technology expressions.

---

## References

Key references cited throughout the document:

- Beale, T. (2002). Archetypes: Constraint-based Domain Models for Future-proof Information Systems. OOPSLA 2002 Workshop on Behavioural Semantics.
- Beale, T. & Heard, S. (2007). An Ontology-based Model of Clinical Information. Studies in Health Technology and Informatics, Medinfo 2007, IOS Press.
- Elstein, A.S., Shulman, L.S. & Sprafka, S.A. (1978). Medical Problem Solving: An Analysis of Clinical Reasoning. Harvard University Press.
- Rector, A.L., Nowlan, W.A. & Kay, S. (1991). Foundations for an Electronic Medical Record. Methods of Information in Medicine.
- Anderson, R. (1996). A Security Policy Model for Clinical Information Systems. IEEE Symposium on Security and Privacy.
- ISO 13606:2008. Health informatics - Electronic health record communication.
- ISO 18308:2011. Health informatics - Requirements for an electronic health record architecture.
- ISO 20514:2005. Health informatics - Electronic Health Record - Definition, Scope and Context.
- ISO/IEC 10746. Information technology - Open Distributed Processing - Reference Model.
- HL7 Clinical Document Architecture (CDA), Release 2.0.
- SNOMED CT. Systematized Nomenclature of Medicine - Clinical Terms.

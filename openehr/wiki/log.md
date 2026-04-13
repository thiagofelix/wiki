# Log

## [2026-04-13] ingest | LANG component: BMM, ODIN, Expression Language

- Created: [[basic-meta-model]] (from: raw/lang-bmm.md, raw/lang-bmm-persistence.md) -- comprehensive BMM page covering model access, type hierarchy, class hierarchy, features, expression/statement meta-models, and persistence model
- Created: [[odin]] (from: raw/lang-odin.md) -- ODIN serialization syntax covering artefact types, data types, containers, type markers, paths, and comparison with JSON/XML
- Created: [[expression-language]] (from: raw/lang-el.md, raw/lang-bel.md) -- EL specification with type system, operators, decision structures, higher-order features, plus historical BEL section
- Updated: index.md -- added 3 new entity entries

## [2026-04-13] ingest | GDL, Simplified Formats, SMART on openEHR, Resource Model, REST API Overview

- Created: [[guideline-definition-language]] — GDL v1 (retired) and GDL2 (stable) clinical decision support language (from: raw/cds-gdl.md, raw/cds-gdl2.md)
- Created: [[simplified-formats]] — developer-friendly JSON alternatives to canonical RM: Flat, Structured, ECISFLAT, TDS (from: raw/its-rest-simplified-formats.md, raw/its-rest-simplified-data-template.md)
- Created: [[smart-on-openehr]] — SMART App Launch for openEHR platforms: OAuth 2.0, service discovery, scopes (from: raw/its-rest-smart-app-launch.md)
- Created: [[resource-model]] — AUTHORED_RESOURCE base class, RESOURCE_DESCRIPTION, translations (from: raw/base-resource.md)
- Created: [[rest-api-overview]] — REST API conventions: headers, status codes, content negotiation, resource identification (from: raw/its-rest-overview.md)
- Updated: index.md — added 5 new entity entries

## [2026-04-13] ingest | Admin API, ADL/AOM 1.4, REST API expansion, LANG/CDS cross-refs

- Created: [[admin-api]] (from: raw/its-rest-admin.md) -- hard-delete endpoints for GDPR and dev/test
- Updated: [[archetype-definition-language]] -- added ADL 1.4 legacy section (dADL syntax, differences from ADL 2, production usage)
- Updated: [[archetype-object-model]] -- added AOM 1.4 legacy section (ARCHETYPE class, C_DOMAIN_TYPE, CONSTRAINT_REF, ARCHETYPE_ONTOLOGY)
- Updated: [[rest-api]] -- added Demographic API, System API, Admin API sections; expanded content negotiation with simplified formats
- Updated: [[base-component]] -- expanded LANG table with descriptions and links; added Resource Model section
- Updated: [[demographic-model]] -- added REST API section describing Demographic API endpoints
- Updated: [[openehr-overview]] -- added LANG and CDS cross-references in specification table
- Updated: [[multi-level-modelling]] -- added BMM section explaining its role as the computable RM representation
- Updated: index.md -- added admin-api entry

## [2026-04-13] ingest | Archetype Identification and Operational Templates (OPT2)

- Created: [[archetype-identification]] (from: raw/am-identification.md)
- Created: [[operational-templates]] (from: raw/am-opt2.md)
- Updated: index.md — added both new pages to Entities section
- Key findings:
  - Archetype identification uses a dual scheme: human-readable HRID (namespace + RM class + concept + version) plus machine GUID
  - Semantic versioning with lifecycle extensions (-alpha, -rc.N) governs artefact evolution
  - Six lifecycle states from unmanaged through published/deprecated/rejected
  - Three reference types (ihrid_ref, sihrid_ref, phrid_ref) support different precision levels
  - OPT2 spec is still in DEVELOPMENT status (v0.5.1), distinct from the legacy OPT 1.4 XML format
  - OPTs are generated artefacts (never authored directly) serving as the bridge to TDS, TDO, and APIs

## [2026-04-13] ingest | Fetched 20 additional openEHR specification documents

Completed full coverage of official openEHR GitHub specification repos. Raw sources now total 49 files.

**New sources added:**
- LANG (5): BMM, BMM Persistence, ODIN, Expression Language, Basic Expression Language
- ITS-REST (8): Overview, Admin API, Demographic API, Definitions API, System API, Simplified Data Template, Simplified Formats, SMART App Launch
- AM (4): ADL 1.4, AOM 1.4, Archetype Identification, OPT2
- CDS (2): GDL v1 (retired), GDL2 (stable)
- BASE (1): Resource Model

**Index updated:** Sources section reorganized by component, community/research sources listed separately.

**Not yet ingested into wiki pages** — raw sources saved only. Wiki pages pending for: LANG specs (BMM, ODIN, EL, BEL), additional ITS-REST APIs, AM 1.4 legacy specs, archetype identification, OPT2, CDS/GDL, and resource model.

## [2026-04-13] ingest | Initial crawl of OpenEHR specification documents

Crawled 22 specification documents from specifications.openehr.org and saved as raw markdown sources.

**Sources crawled:**
- BASE: Architecture Overview, Foundation Types, Base Types
- RM: EHR, Common, Data Types, Data Structures, Demographic, Support, Integration, EHR Extract
- AM: Overview, ADL2, AOM2
- QUERY: AQL
- ITS-REST: EHR API, Query API, Definition API
- SM: Platform Service Model
- PROC: Task Planning
- TERM: Support Terminology
- CNF: Platform Conformance

**Wiki pages created (14):**
- Overview: [[openehr-overview]]
- Entities: [[reference-model]], [[ehr-information-model]], [[common-information-model]], [[data-types]], [[data-structures]], [[demographic-model]], [[archetype-model]], [[archetype-definition-language]], [[archetype-object-model]], [[archetype-query-language]], [[rest-api]], [[task-planning]], [[base-component]]
- Concepts: [[multi-level-modelling]]

**Key findings:**
- OpenEHR uses multi-level modelling: stable RM (in software) + archetypes (domain content) + templates (use-case specific)
- The RM has 8 specifications covering EHR, demographics, data types/structures, common patterns, integration, and EHR extract
- Entry types map to clinical problem-solving: OBSERVATION → EVALUATION → INSTRUCTION → ACTION
- AQL queries are portable across all openEHR implementations via archetype paths
- Built-in versioning and audit trail for all EHR content
- Task Planning (PROC 1.7.0) is RETIRED status — being superseded

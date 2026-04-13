---
title: Guideline Definition Language (GDL)
type: entity
sources:
  - raw/cds-gdl.md
  - raw/cds-gdl2.md
created: 2026-04-13
updated: 2026-04-13
---

# Guideline Definition Language (GDL)

The Guideline Definition Language is a formal language for expressing clinical decision support (CDS) logic within the openEHR ecosystem. It enables production-rule-based guidelines that are independent of natural languages and reference terminologies by leveraging openEHR archetypes as both input and output. GDL supports point-of-care decision support, algorithm-based calculators, alerts and reminders, personalized care plans, and retrospective population analytics.

Two versions exist: GDL v1 (now retired) and GDL2 (stable, current).

## GDL v1 (RETIRED)

GDL v1 was the original specification, released as part of CDS Release 2.0.0 and formally retired in CDS Release 2.0.1 (July 2024). It was primarily developed by Cambio Healthcare Systems.

### Object Model

The v1 object model has two packages:

- **Guide Package** -- structures for guide definition and archetype binding
- **Expressions Package** -- structures for rule expressions and operations

### Core Classes

**GUIDE** is the top-level class representing a discrete guideline. Key attributes:

| Attribute | Type | Description |
|-----------|------|-------------|
| `gdl_version` | String | GDL version (e.g., "0.1") |
| `id` | String | Guide identifier |
| `concept` | String | Normative meaning as local gt-code |
| `language` | Language | Natural language resources |
| `description` | RESOURCE_DESCRIPTION | Authorship and lifecycle metadata |
| `definition` | GUIDE_DEFINITION | Archetype bindings and rules |
| `ontology` | GUIDE_ONTOLOGY | Guide ontology with term definitions |

**GUIDE_DEFINITION** contains the logic:

- `archetype_bindings` -- list of ARCHETYPE_BINDING connecting archetypes to local variables
- `rules` -- map of RULE objects indexed by gt-codes
- `pre_conditions` -- list of expressions that must hold before any rule fires

**ARCHETYPE_BINDING** maps archetype elements to local gt-code variables. Each binding specifies an `archetype_id`, an optional `template_id`, a `domain` ("EHR" or "CDS"), element bindings, and optional predicates for filtering.

**RULE** contains `when` statements (firing conditions) and `then` statements (assignments), plus a `priority` integer controlling execution order.

### Expressions

The expressions package provides EXPRESSION_ITEM (abstract), UNARY_EXPRESSION, BINARY_EXPRESSION, ASSIGNMENT_EXPRESSION, and FUNCTIONAL_EXPRESSION. See [[expression-language]] for the broader openEHR expression formalism.

**OPERATOR_KIND** includes arithmetic (`+`, `-`, `*`, `/`, `^`), logical (`&&`, `||`, `!`), relational (`==`, `!=`, `<`, `<=`, `>`, `>=`), assignment (`=`), and terminological reasoning operators (`is_a`, `!is_a`).

**Built-in functions:** `abs`, `ceil`, `exp`, `floor`, `log`, `log10`, `log1p`, `round`, `sqrt`, `max`, `min`.

### Syntax

GDL v1 uses dADL (a predecessor of [[odin]]) as its serialization format. The expression grammar was implemented via JavaCC.

### Implementation

The primary execution engine was JBoss Drools, translating GDL rules to Drools Rule Language (DRL). An open-source GDL Editor was available for authoring and testing guidelines.

## GDL2 (STABLE)

GDL2 is the current version (CDS Release 2.0.1), representing a significant evolution. It was also developed primarily by Rong Chen at Cambio CDS with contributions from Thomas Beale.

### Key Differences from v1

| Aspect | GDL v1 | GDL2 |
|--------|--------|------|
| Status | RETIRED | STABLE |
| Top-level class | GUIDE | GUIDELINE (inherits AUTHORED_RESOURCE) |
| Data model support | openEHR archetypes only | Model-agnostic: openEHR, HL7 FHIR, ISO 13606 |
| Output | Direct variable assignments | Output templates via `use_template` |
| Local variables | Not formally supported | Supported via `internal_variables` |
| Serialization | dADL only | [[odin]] and JSON |
| Additional functions | 11 math functions | 14 functions (adds `sin`, `cos`, `count`, `sum`) |
| Quantifiers | None | `FOR_ALL` universal quantifier |

### Object Model

GDL2 has three packages: **Guideline**, **Expression**, and **Terminology**.

**GUIDELINE** inherits from AUTHORED_RESOURCE (see [[resource-model]]), gaining built-in support for identification, metadata, translations, and annotations. Key attributes:

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | String | Identifier (format: `concept_name.v[N[.M.P]]`) |
| `gdl_version` | String | GDL version (e.g., "2.0") |
| `concept` | String | Normative meaning (gt-code) |
| `definition` | GUIDELINE_DEFINITION | Bindings, rules, templates |
| `terminology` | TERMINOLOGY | Term definitions and bindings |

**GUIDELINE_DEFINITION** contains:

- `data_bindings` -- hash of DATA_BINDING objects (replacing ARCHETYPE_BINDING)
- `pre_conditions` -- list of ASSERTION objects
- `rules` -- hash of RULE objects
- `default_actions` -- always-executed assignments
- `templates` -- hash of OUTPUT_TEMPLATE objects
- `internal_variables` -- locally-scoped variables

**DATA_BINDING** is the v2 replacement for ARCHETYPE_BINDING. It uses `model_id` instead of `archetype_id`, enabling bindings to non-openEHR models (FHIR Resources, ISO 13606). Each binding is typed as "INPUT" or "OUTPUT".

**OUTPUT_TEMPLATE** enables structured output rendering. A rule can invoke `use_template($gtCode)` in its `then` block, and the template object defines the output structure with `{}` variable substitution placeholders. Templates support any output model (e.g., CDS Hooks cards, custom JSON structures).

### Local Variables

GDL2 supports local variables identified by gt-codes, defined in the terminology section and tracked via `GUIDELINE_DEFINITION.internal_variables`. These hold intermediate calculation results independent of external clinical models.

### Enhanced Functions

GDL2 adds to the v1 function set: `sin`, `cos` (trigonometric), `count` (instance counting), and `sum` (aggregation).

## Execution Model

Both versions share a similar execution flow:

1. **Pre-condition evaluation** -- guideline-level conditions are checked. If not satisfied, the guideline is non-applicable for the given patient/data set.
2. **Data binding and predicate evaluation** -- for each data binding, predicates constrain which data instances are selected (e.g., filtering diagnoses by terminology code using `is_a`).
3. **Rule execution** -- rules fire in priority order (higher priority first). For each rule, `when` conditions are evaluated; if all are true, `then` actions execute (variable assignments, calculations).
4. **Template rendering** (GDL2 only) -- if a rule invokes `use_template`, the output template is rendered with variable substitutions.

Rules can be chained across multiple guidelines for complex decision-making workflows.

## Terminology

Both versions use a terminology section with:

- **Term definitions** -- gt-codes mapped to human-readable text per language, enabling multilingual support without changing rule logic
- **Term bindings** -- gt-codes mapped to external terminology codes (ICD-10, SNOMED-CT, etc.), enabling site-specific terminology adaptation

## Related Pages

- [[archetype-model]] -- archetypes used as GDL input/output models
- [[resource-model]] -- AUTHORED_RESOURCE base class for GDL2's GUIDELINE
- [[expression-language]] -- broader openEHR expression formalism
- [[odin]] -- serialization format used by GDL/GDL2

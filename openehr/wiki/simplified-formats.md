---
title: Simplified Formats
type: entity
sources:
  - raw/its-rest-simplified-formats.md
  - raw/its-rest-simplified-data-template.md
created: 2026-04-13
updated: 2026-04-13
---

# Simplified Formats

Simplified Formats are developer-friendly JSON (and XML) representations of openEHR data instances, designed as alternatives to the verbose canonical RM format. They reduce the learning curve for developers with limited openEHR experience by abstracting away structural complexity, eliminating intermediate RM containers, and using human-readable field identifiers derived from Web Templates.

## Motivation

Canonical openEHR formats (XML and JSON) require full RM hierarchy knowledge -- every object needs `_type` declarations, extensive nesting, and boilerplate repetition. Even recording a single blood pressure reading produces deeply nested structures. Simplified formats address this by:

- Using human-readable node IDs instead of archetype codes
- Separating context metadata with a `ctx/` prefix
- Eliminating intermediate RM structures (ITEM_TREE, HISTORY, etc.)
- Mapping elements directly to values
- Prefixing optional RM attributes with underscore

## History: Unification of Vendor-Specific Formats

Simplified formats emerged from several independent vendor implementations:

- **Template Data Schema (TDS)** -- developed by Ocean Health Systems, transforming `.oet` template files into XSD definitions with flattened RM structures and human-readable XML tags
- **ECISFLAT (ncSDT)** -- JSON format from EtherCIS using AQL-style paths based on archetype node codes
- **Web Template format (simSDT/structSDT)** -- developed by Better (formerly Marand), employing radical RM simplification with natural language paths

The openEHR specification unifies these approaches within a formal framework, documented across the Simplified Formats spec (STABLE) and the Simplified Data Template spec (DEVELOPMENT).

## Conceptual Framework

### The sOPT Transformer

The generation pipeline works as follows:

1. An **Operational Template (OPT)** serves as the canonical source definition (see [[operational-templates]])
2. An **sOPT transformer** converts the OPT into a simplified OPT using a **Simplified Information Model (SIM)** -- a logical subset of RM classes relevant to committable EHR content
3. SIM simplifications include **de-normalization** (merging Composition relationships, reducing path depth) and **stringification** (replacing complex low-level types with String)
4. The sOPT produces various JSON Data Templates in both hierarchical and flat formats

Instance conversion flows in the reverse direction: developers create instances in simplified JSON, and server-side converters transform them to canonical RM format during data commitment.

## Format Variants

| Format | Abbreviation | MIME Type | Description |
|--------|-------------|-----------|-------------|
| Flat JSON | simSDT | `application/openehr.wt.flat+json` | All elements as key-value pairs at a single level; keys are full Web Template paths |
| Structured JSON | structSDT | `application/openehr.wt.structured+json` | Hierarchical nested JSON objects following the template tree |
| Near-Canonical Flat JSON | ncSDT / ECISFLAT | `application/openehr.nc.flat+json` | Flat JSON using AQL-style archetype paths instead of WT paths |
| Template Data Schema XML | TDS | `application/openehr.tds2+xml` | XSD-based XML format with human-readable element names |

## Web Templates as Foundation

All simplified formats are built on **Web Templates (WT)**, which provide:

- Simplified node identifiers generated from archetype node names
- AQL paths for all elements
- Input type definitions for data entry
- Localized labels and descriptions
- Multiplicity constraints

Web Templates are JSON representations of Operational Templates, produced by the sOPT transformation process.

## Field Identifier Rules

Hierarchical field identifiers in simplified formats follow these conventions:

### Node ID Generation

Node IDs are generated from archetype node names by:

1. Replacing non-alphanumeric characters (except `_`, `.`, `-`) with underscore
2. Consolidating multiple consecutive underscores
3. Converting to lowercase
4. Removing leading/trailing underscores
5. Using "id" if result is empty
6. Prepending "a" if result starts with a digit
7. Appending numeric suffix if needed for uniqueness

Examples: "Body temperature" becomes `body_temperature`; "1st visit" becomes `a1st_visit`.

### Path Construction

- **Path separators** -- forward slash (`/`) between levels: `composition_id/section_id/observation_id/element_id`
- **Instance indices** -- colon notation for repeating elements: `node_id:0` (first), `node_id:1` (second)
- **Attribute suffixes** -- pipe notation for sub-properties of data types:

| RM Type | Suffix | Description |
|---------|--------|-------------|
| DV_QUANTITY | `\|magnitude` | Numeric value |
| DV_QUANTITY | `\|unit` | Unit of measure |
| DV_CODED_TEXT | `\|code` | Terminology code |
| DV_CODED_TEXT | `\|value` | Display term |
| DV_CODED_TEXT | `\|terminology` | Terminology ID |

- **RM attribute prefix** -- underscore (`_`) for optional RM attributes: `_uid`, `_link`, `_feeder_audit`
- **Raw canonical JSON** -- `|raw` suffix embeds pre-serialized canonical JSON for an element

## Level Removal

Certain intermediate RM container types are always removed from paths to reduce depth:

| Removed Type | Replaced By |
|-------------|-------------|
| ITEM_TREE | ITEM_TREE.items |
| ITEM_LIST | ITEM_LIST.items |
| ITEM_SINGLE | ITEM_SINGLE.item |
| ITEM_TABLE | ITEM_TABLE.rows |
| HISTORY | HISTORY.events |

EVENT nodes are conditionally removed when max occurrence is 1 and no sibling EVENT nodes exist. They are retained when multiple EVENT types exist or the EVENT can occur multiple times.

## Context Fields

Composition-level metadata uses the `ctx/` prefix.

**Mandatory:** `ctx/language`, `ctx/territory`

**Optional context fields include:**
- `ctx/composer_name`, `ctx/composer_id`, `ctx/composer_id_namespace`
- `ctx/time`, `ctx/end_time`
- `ctx/setting|code`, `ctx/setting|value`
- `ctx/_health_care_facility|id`, `ctx/_health_care_facility|name`
- `ctx/_participation:N|function`, `ctx/_participation:N|name`
- `ctx/_provider|name`, `ctx/_provider|id`
- `ctx/_location`
- `ctx/_work_flow_id|id`

## Flat Format Example

```json
{
  "ctx/language": "en",
  "ctx/territory": "US",
  "ctx/composer_name": "Dr. Smith",
  "vital_signs/body_temperature:0/any_event:0/temperature|magnitude": 37.5,
  "vital_signs/body_temperature:0/any_event:0/temperature|unit": "C"
}
```

## Structured Format Example

```json
{
  "ctx": {
    "language": "en",
    "territory": "US"
  },
  "vital_signs": {
    "body_temperature": [{
      "any_event": [{
        "temperature": [{
          "|magnitude": 37.5,
          "|unit": "C"
        }]
      }]
    }]
  }
}
```

## Conversion Between Formats

**Flat to Structured:** Parse each flat key into path segments by splitting on `/`, create nested objects, handle attribute suffixes as pipe-prefixed properties, merge structures, and add context.

**Structured to Flat:** Recursively traverse the nested object, build paths by concatenating property names with `/`, append pipe-prefixed properties, unwrap arrays, and flatten context with `ctx/` prefix.

Both directions are fully machine-generatable from Operational Templates, satisfying the requirement for bidirectional conversion to/from canonical format.

## Related Pages

- [[rest-api]] -- the REST API that accepts simplified format payloads
- [[operational-templates]] -- the source definitions from which simplified formats are generated
- [[reference-model]] -- the canonical RM that simplified formats abstract over

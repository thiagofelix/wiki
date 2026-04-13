---
title: Operational Templates (OPT2)
type: entity
sources:
  - raw/am-opt2.md
created: 2026-04-13
updated: 2026-04-13
---

# Operational Templates (OPT2)

An Operational Template (OPT) is a fully compiled, deployment-ready artefact generated from source archetypes and templates expressed in ADL 2. It serves as the bridge between authored clinical knowledge artefacts and production EHR systems. The OPT2 specification (AM Release 2.3.0) is currently in **DEVELOPMENT** status.

OPT2 is distinct from the original OPT format, which was an XML-schema format based on ADL 1.4 archetypes.

## Purpose

Production EHR systems must never operate directly with source archetypes and templates. The OPT addresses this by providing:

1. **Safety and Validation**: Only validated, compiled artefacts reach production systems.
2. **Specialisation Resolution**: The inheritance hierarchy between archetypes is flattened into usable standalone artefacts, analogous to executable class forms in object-oriented programming.
3. **Customisation**: Selective inclusion of languages and terminology bindings appropriate for specific deployment contexts.
4. **Machine Format Optimisation**: Designed for implementation convenience rather than human authoring, supporting multiple serialisation formats.
5. **Transformation Basis**: A standardised input for generating downstream artefacts including Template Data Schemas (TDS), Template Data Objects (TDO), and APIs.

## Raw OPT vs Profiled OPT

Two types of OPT exist, forming a pipeline:

```
Source Archetypes & Templates -> Raw OPT -> Profiled OPT(s)
                                   |
                              Other Formats
                            (TDS, TDO, APIs)
```

### Raw OPT

The raw OPT is the initial compiled form. It is a unified archetype structure derived from flattened source archetypes and templates, containing **all** content regarding languages and terminology bindings. It is a top-level, non-specialised archetype with all references resolved.

### Profiled OPT

A profiled OPT is a processed raw OPT tailored for a specific operational context. Multiple profiled OPTs may be derived from a single raw OPT. Profiling operations include:

- **Annotations removal**: The `annotations` section may be stripped entirely.
- **Language filtering**: Unnecessary language translations are removed (minimum of one retained). The `original_language` reflects the root source template's authoring language.
- **Terminology binding filtering**: Global filtering of terminology bindings, from selective removal to complete elimination.
- **Terminology substitution**: Choosing between archetype-local value sets and external terminology codes. Selection strategies range from library-level to per-OPT selection. Node-level selection is not yet supported in ADL 2.

## Generation Process

An OPT is generated from a master source template and all referenced archetypes and templates. The generation process applies several transformations beyond standard [[archetype-object-model]] flattening:

1. **Archetype reference resolution**: All archetype references (typically lacking full version information in source form) are resolved to complete identifiers with full three-part versions. See [[archetype-identification]] for the versioning scheme.

2. **Flattening and overlay application**: All template overlays are applied. The specialisation hierarchy is fully resolved into a flat structure. The result has no `specialize` statement.

3. **Sibling order resolution**: Full expression of object node siblings under container attributes eliminates `before`/`after` sibling order markers.

4. **`use_node` expansion**: All internal references (`use_node` nodes) are replaced by inline copies of their target structures.

5. **Slot resolution**: Slot-filler references are replaced by inline archetype copies. Closed slots are removed entirely.

6. **Node deletion**: All deleted nodes are removed, including attributes with `existence matches {0}` and objects with `occurrences matches {0}`.

7. **Terminology consolidation**: The flat form of each constituent archetype or template's `terminology` section (excluding the root template) is consolidated under a `component_terminologies` section in the OPT.

### Resulting Artefact Structure

The raw OPT follows this [[archetype-definition-language]] structure:

```
operational_template (qualifiers?)
    ARCHETYPE_HRID
language
    ...
description
    ...
definition
    ...
rules        (optional)
    ...
terminology
    ...
annotations  (optional)
    ...
component_terminologies
    ...
```

## File Formats

OPTs support four serialisation formats, each with a distinct file extension:

| Extension | Format | Character |
|-----------|--------|-----------|
| `.opt` | ADL | Human-readable, suitable for reference and development tools |
| `.optx` | XML | Structured format for schema-based systems and legacy integration |
| `.optj` | JSON | Machine-friendly for system integration and data interchange |
| `.opty` | YAML | Machine-friendly alternative serialisation |

Raw and profiled OPTs use distinct filenames to prevent confusion.

## Relationship to Source Artefacts

An OPT is always generated from source artefacts -- it is never authored directly. The relationship is one-directional:

- Source archetypes and templates are authored in [[archetype-definition-language]] and maintained in repositories.
- A compiler tool (such as the ADL Workbench) processes the source template and all referenced archetypes to produce the OPT.
- The OPT resolves all references, flattens all specialisations, and consolidates all terminologies into a single standalone artefact.

This means OPTs are reproducible: given the same set of source artefacts and the same compilation rules, the same OPT is produced. Configuration tracking can record the exact source artefact set used (including full version identifiers and hashes).

## Use for Generating TDS, TDO, and APIs

The OPT serves as the canonical input for generating further downstream artefacts:

- **Template Data Schemas (TDS)**: XML or JSON schemas constrained to the specific data shapes defined by the template. Used for data validation. See [[simplified-formats]] for simplified representations.
- **Template Data Objects (TDO)**: Skeleton data instances pre-populated with template structure, used as starting points for data entry.
- **APIs**: RESTful endpoints generated from templates. The [[rest-api]] Definition API manages template upload and retrieval in CDR systems.

## Development Status

The OPT2 specification is in **DEVELOPMENT** status (version 0.5.1). Several areas remain marked as "to be determined" (TBD), including node-level terminology selection control and some profiling details. The specification has been part of AM releases from 2.0.6 through the current 2.3.0.

## Related Pages

- [[archetype-model]] -- The archetype formalism and three-layer architecture that OPTs compile
- [[archetype-object-model]] -- AOM 2 constraint model and standard flattening rules that OPT generation extends
- [[archetype-definition-language]] -- ADL 2 syntax in which OPTs can be serialised
- [[archetype-identification]] -- Versioning and identification scheme; OPTs resolve all references to full versioned identifiers
- [[simplified-formats]] -- Simplified data representations generated from OPTs
- [[rest-api]] -- Definition API for uploading and managing templates in CDR systems

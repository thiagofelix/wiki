# EtherCIS Architecture

Source: Research compilation from EtherCIS GitHub (github.com/ethercis/ethercis) and EtherCIS documentation.

## Overview

EtherCIS is the predecessor to EHRbase. Also PostgreSQL-based with JSONB for clinical data. It introduced several patterns that EHRbase later adopted and refined.

**Repository**: https://github.com/ethercis/ethercis

## Key Architectural Features

### ltree for Hierarchical Paths

EtherCIS used PostgreSQL's native **`ltree`** data type for hierarchical path resolution in CONTAINS clauses. This is significant because `ltree` provides:
- Native tree-structured label data
- Built-in operators for ancestor/descendant queries (`@>`, `<@`)
- GiST index support for fast hierarchical lookups
- Pattern matching with `lquery` and `ltxtquery`

This maps naturally to openEHR archetype path navigation.

### Hexagonal Architecture

EtherCIS follows a hexagonal (ports and adapters) architecture pattern, with strict separation of concerns.

### Database Separation

- Administrative data and clinical data stored in separate databases
- Foreign Data Wrappers (FDW) used for distributed storage across databases

### Three Table Categories

1. **openEHR RM persistence** — core clinical data tables
2. **Template-headings** — cache/summary tables derived from templates
3. **Static reference data** — codes, languages, territories

### Bi-temporal Modeling

Uses bi-temporal table modeling for version history:
- Transaction time (when the change was recorded in the system)
- Valid time (when the clinical event occurred)

### AQL-to-SQL Translation

AQL translator formats queries to avoid multiple I/Os. The translation is tightly coupled to the specific storage schema.

## References

- GitHub: https://github.com/ethercis/ethercis
- Documentation: https://github.com/ethercis/EtherCISdocumentation/blob/gh-pages/pages/etherCIS/dbaspects.md

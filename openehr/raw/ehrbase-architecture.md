# EHRbase Architecture and Storage Model

Source: Research compilation from EHRbase GitHub (github.com/ehrbase/ehrbase), openEHR Discourse threads, and EHRbase documentation.

## Overview

EHRbase is the main open-source openEHR Clinical Data Repository (CDR). It is the reference implementation most widely used in the community.

**Technology Stack:**
- Java (99%+ of codebase), Spring Boot, Maven
- PostgreSQL 16 (recommended), minimum v15
- jOOQ for type-safe SQL generation
- ANTLR4 for AQL parsing
- Flyway for database migrations

## Storage Model (Hybrid Relational + JSONB)

EHRbase v2 uses a hybrid approach. As described by Thomas Beale: "JSONB (JSON binary blob) representation for `Composition.content`, path-based index fields, and mostly orthodox tables for the other high-level structures."

Stefan Spiska further clarifies: "documents are not stored as one large blob but are divided into paths and just the leaves are stored in JSON."

### Key Tables in the `ehr` Schema

- **`comp_data`** — stores composition clinical content as JSONB
- **`comp_version`** — tracks composition versions (change control)
- **`contributions`** — records change-sets
- **`ehr_status`** — EHR-level metadata
- **`ehr_folder`** — directory/folder structure

### Design Principles

- Everything is normalized except the content, which is saved as native JSON columns in Postgres
- Non-RM elements are added for performance, including storing different forms of paths to query and reconstruct data when retrieving
- History tables exist for versioned locatables to store older versions

## AQL-to-SQL Translation Pipeline

1. **Parse**: ANTLR4 grammar parses AQL string into AST
2. **CONTAINS resolution**: Recursive AST traversal from bottom-left to top, creating template traversal queries and boolean validations for logical operators
3. **Path resolution**: Archetype paths are resolved to construct JSON path expressions for querying JSONB structures
4. **SQL generation**: jOOQ builds type-safe PostgreSQL queries with JSONB operators (`#>>` for extraction), `DISTINCT ON`, and complex joins
5. **Execution**: Generated SQL runs against PostgreSQL

The `aql-engine` module and `rm-db-format` module handle this pipeline. The openEHR_SDK provides a DTO model for mapping AQL strings to/from structured objects.

### Key Architectural Insight

"For generating any kind of SQL you need to know your relational schema. EHRBase has its own schema and is not 100% relational, it uses document type from Postgres mixed with relational."

AQL-to-SQL translation is inherently schema-dependent and not portable between implementations. Each CDR must implement its own translation layer matching its specific storage model.

## References

- GitHub: https://github.com/ehrbase/ehrbase
- openEHR_SDK: https://github.com/ehrbase/openEHR_SDK
- Discourse: https://discourse.openehr.org/t/ehrbase-db-schema-definition/4249
- Discourse: https://discourse.openehr.org/t/aql-to-database-sql-convertor/4967
- Discourse: https://discourse.openehr.org/t/ehrbase-datamodel-for-change-control/6737

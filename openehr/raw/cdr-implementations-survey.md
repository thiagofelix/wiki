# openEHR CDR Implementations Survey

Source: Research compilation from 2024 academic survey, GitHub repositories, and openEHR Discourse.

## Major Implementations

### EHRbase (Primary Open-Source CDR)
- **Language**: Java (Spring Boot)
- **Database**: PostgreSQL 16
- **Storage**: Hybrid relational + JSONB
- **AQL**: Full support via ANTLR4 parser + jOOQ SQL generation
- **Status**: Active development, most widely adopted open-source CDR
- **GitHub**: https://github.com/ehrbase/ehrbase

### EtherCIS (Predecessor to EHRbase)
- **Language**: Java
- **Database**: PostgreSQL
- **Storage**: Hybrid with ltree for path resolution
- **AQL**: Supported via custom translator
- **Status**: Superseded by EHRbase
- **GitHub**: https://github.com/ethercis/ethercis

### Better Platform
- **Language**: Proprietary
- **Database**: PostgreSQL (reportedly)
- **Storage**: Proprietary
- **AQL**: Full support
- **Status**: Commercial product, one of the most mature CDRs
- **Notable**: Bostjan Lah from Better is co-author of the AQL ANTLR4 grammar

### EHRServer (Groovy/Grails)
- **Language**: Groovy/Grails
- **Database**: SQL (pure relational, no JSON)
- **Storage**: DATA_VALUES stored as indexed key-value pairs by ADL path
- **AQL**: Uses proprietary "Simple Archetype Query Model" (SAQM) rather than full AQL
- **Notable**: Preserves VERSION as XML files to filesystem

### IPEHR-gateway (Go)
- **Language**: Go
- **Database**: Custom
- **AQL**: Supports AQL queries over encrypted data
- **Notable**: Decentralized medical records approach
- **GitHub**: Available on GitHub, tagged with "aql"

### Ocean Health Systems (Ocean Informatics)
- **Status**: Commercial product
- **Notable**: One of the original openEHR implementers

### Marand (Think!EHR)
- **Status**: Commercial product (now part of Better)
- **Database**: PostgreSQL
- **AQL**: Full support

## 2024 Survey Results

A comprehensive 2024 survey identified 17 openEHR CDR implementations worldwide, interviewing 11 vendors.

### Storage Backend Distribution

| Backend | Usage |
|---------|-------|
| PostgreSQL | Most common |
| SQL Server | Some commercial implementations |
| Oracle | Enterprise deployments |
| MongoDB | Document-store approach |
| eXist-db | XML-native approach |
| ElasticSearch | Search-optimized approach |
| MumpsDB | Legacy healthcare systems |

The majority (11 of surveyed) use RDBMS, often with XML or JSON data fields.

## References

- 2024 CDR Survey: https://www.sciencedirect.com/science/article/abs/pii/S1386505624002545
- IEEE Survey (2013): https://ieeexplore.ieee.org/document/6627806/
- Discourse: https://discourse.openehr.org/t/best-database-for-openehr/117/86

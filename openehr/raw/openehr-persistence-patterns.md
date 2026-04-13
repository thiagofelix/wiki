# openEHR Persistence Patterns

Source: Research compilation from openEHR Persistence FAQs, Archetype Relational Mapping (ARM) paper (PMC4636072), openEHR Discourse, and IEEE survey of storage implementations.

## Four Main Persistence Patterns

The openEHR community has identified four main persistence patterns, documented in the openEHR Persistence FAQs.

### Pattern A: Blob Storage

- Serialize entire top-level objects (Compositions) as single blobs (XML/JSON)
- Table needs fewer than 10 columns; extremely simple and fast for writes
- Drawback: cannot query into blob content without deserializing; changing queryable attributes requires schema migration
- Storage benchmark: ~1.6 GB for test dataset

### Pattern B: Node+Path (EAV-style)

- All data nodes serialized individually; each stored as `<node_path, serialized_value>` pair
- Two-column table with index on path column
- Advantages: simple tabular storage, fine-grained path-based queries
- Disadvantages: complex retrieval logic, poor performance for attribute-centric queries, massive storage overhead
- Storage benchmark: ~43.87 GB for same test dataset (27x more than blob)

### Pattern C: Hybrid (EHRbase/EtherCIS approach)

- Higher-level RM structures (EHR, Composition metadata, versioning) in normalized relational tables
- Clinical content (`Composition.content` / Entry level) stored as JSONB
- Path-based indexes alongside JSONB for query performance
- Leaves decomposed into individual JSON fragments with paths, not monolithic blobs
- Best balance of flexibility, queryability, and performance

### Pattern D: Archetype Relational Mapping (ARM)

- Each archetype mapped to its own relational table
- Single-occurrence items become columns; multiple-occurrence items get child tables with foreign keys
- RM data types mapped to SQL types (e.g., `DvQuantity.magnitude` -> FLOAT, `DvText.value` -> NVARCHAR)
- Templates define identification, query, and generalized-to-specialized constraints
- Performance: 6-50x faster than conventional databases for patient-searching queries
- Storage benchmark: ~2.9 GB (moderate overhead from denormalization)
- Drawback: schema changes required when archetypes change; loses the "future-proof" benefit of openEHR

## Performance Comparison

From ARM paper, 29,743 patients test dataset:

| Pattern | Storage | Query Speed | Notes |
|---------|---------|-------------|-------|
| Blob | 1.6 GB | Fast reads, no deep queries | Simplest implementation |
| Node+Path (EAV) | 43.9 GB | Slow (complex joins) | 27x storage overhead |
| ARM | 2.9 GB | Fast (6-50x for searches) | Schema tied to archetypes |
| Hybrid (JSONB) | ~2 GB est. | Good balance | Most implementations use this |

## Community Consensus

The hybrid approach (Pattern C) has emerged as the most popular choice among openEHR CDR implementations. A 2024 survey of 17 CDR implementations found the majority (11 of surveyed) use RDBMS, often with XML or JSON data fields.

Storage backends across the ecosystem span: PostgreSQL, SQL Server, Oracle, MongoDB, eXist-db, ElasticSearch, and MumpsDB.

## References

- openEHR Persistence FAQs: https://openehr.atlassian.net/wiki/spaces/resources/pages/4554765/Persistence+FAQs
- ARM Paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC4636072/
- 2024 CDR Survey: https://www.sciencedirect.com/science/article/abs/pii/S1386505624002545
- IEEE Survey: https://ieeexplore.ieee.org/document/6627806/
- Discourse: https://discourse.openehr.org/t/best-database-for-openehr/117/86
- Discourse: https://discourse.openehr.org/t/why-use-aql-instead-of-sql-in-openehr/2719

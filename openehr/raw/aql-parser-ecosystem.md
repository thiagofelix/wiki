# AQL Parser Ecosystem

Source: Research compilation from openEHR specifications, GitHub repositories, and community resources.

## Official ANTLR4 Grammar (Canonical Reference)

- Published at: https://specifications.openehr.org/releases/QUERY/latest/docs/AQL/grammar/AqlParser.g4
- Complete rewrite of previous ANTLR3 grammar
- Authors: Sebastian Iancu (Code24/NL), Teun van Hemert (Nedap/NL), Bostjan Lah (Better/SI), Thomas Beale (openEHR Foundation)
- Licensed CC-BY-SA

### Grammar Structure

Defines:
- `selectQuery` root rule
- SELECT/FROM/WHERE/ORDER BY/LIMIT clauses
- `identifiedPath` for archetype path expressions
- `pathPredicate` for node constraints
- Aggregate functions: COUNT, MIN, MAX, SUM, AVG
- Terminology/string/numeric/datetime functions

## openEHR-antlr4 Repository

- GitHub: https://github.com/openEHR/openEHR-antlr4
- Generates **Java** parsers from ANTLR4 grammars
- Covers: ADL 2.x, ADL 1.4, ODIN, AQL, BEL, EL, BMM
- 61% Java, 35% ANTLR grammar

## Archie (Java RM Implementation)

- GitHub: https://github.com/openEHR/archie
- RM 1.0.4 implementation + ADL2/AOM2
- APath queries on RM instances (not full AQL, but path-based navigation)
- Experimental XPath 1.0 support on RM objects

## openEHR_SDK (Java)

- GitHub: https://github.com/ehrbase/openEHR_SDK
- Maps AQL strings to/from an AQL DTO model
- Type-safe AQL building inspired by jOOQ patterns

## Nedap AQL Parser

- Referenced as a dependency in Nedap's archetype-languageserver project
- Java-based
- Part of a larger ecosystem for archetype tooling

## vscode-aql

- VS Code extension providing AQL syntax support
- Syntax highlighting and basic language features

## Notable Gap

**No mature standalone AQL parsers exist in TypeScript, Python, Rust, or Go.** The entire ecosystem is heavily Java-centric. This represents a significant opportunity for a non-Java implementation.

## Related Tools

- **Medblocks**: Provides an intuitive guide to AQL for developers new to the query language
  - Reference: https://medblocks.com/blog/an-intuitive-guide-to-aql-archetype-query-language

## AQL Specification

- Full specification: https://specifications.openehr.org/releases/QUERY/latest/AQL.html
- Release: QUERY 1.1.0 (STABLE)

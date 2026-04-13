---
title: Archetype Identification
type: entity
sources:
  - raw/am-identification.md
created: 2026-04-13
updated: 2026-04-13
---

# Archetype Identification

The Archetype Identification specification (AM 2.3.0, STABLE) defines how openEHR archetypes and templates are identified, versioned, referenced, and authenticated in distributed authoring environments. It addresses the unique challenge that knowledge artefacts -- unlike software -- are individually version-controlled and exist "outside the software," requiring their own identification and governance schemes.

## Human-Readable Identifier (ARCHETYPE_HRID)

Every archetype carries a structured human-readable identifier built from the `ARCHETYPE_HRID` class. The full identifier follows this grammar:

```
[namespace '::'] qualified_rm_class_name '.' concept_id '.v' version_id
```

### Components

| Field | Purpose | Example |
|-------|---------|---------|
| `namespace` | Reverse domain name of the custodian organisation | `org.openehr`, `uk.nhs` |
| `rm_publisher` | Organisation that publishes the reference model | `openEHR`, `ISO` |
| `rm_closure` | Top-level RM package from which the focal class is reachable | `EHR`, `DEMOGRAPHIC` |
| `rm_class` | The RM class being constrained | `EVALUATION`, `CLUSTER`, `OBSERVATION` |
| `concept_id` | Short ontological identifier for the clinical concept | `problem_diagnosis`, `bp_measurement` |
| `release_version` | Three-part semantic version | `1.3.0` |

The `rm_publisher`, `rm_closure`, and `rm_class` are combined into a qualified RM class name, e.g. `openEHR-EHR-EVALUATION`. This acts as a guard against concept identifier clashes across different RM classes.

**Full example:** `org.openehr::openEHR-EHR-EVALUATION.problem_diagnosis.v2.4.1`

The concept identifier is drawn from a formal ontology maintained by each Custodian Organisation. In modern ADL 2, the `-` character in concept identifiers no longer encodes specialisation hierarchy (a change from ADL 1.4).

## Interface ID vs Physical ID

The `ARCHETYPE_HRID` class defines two key derived identifiers:

- **Interface ID** (`interface_id()`): Includes only the major version -- e.g. `openEHR-EHR-EVALUATION.diagnosis.v1`. This is the primary reference form used in source artefacts, because all releases sharing a major version preserve backward compatibility.
- **Physical ID** (`physical_id()`): Includes the full three-part version -- e.g. `openEHR-EHR-EVALUATION.diagnosis.v1.29.0`. This identifies a specific artefact instance.

Only the major version appears in source archetype HRIDs. Breaking changes create a new major version and thus a new deployable artefact, analogous to software interface versioning.

## Machine Identifier (GUID uid)

In addition to the human-readable HRID, every managed archetype receives a machine identifier -- a GUID stored in the `uid` property. The GUID is assigned at creation and never changes for the life of the artefact. A separate `build_uid` is incremented at every commit.

Archetypes lacking both `uid` and `namespace` are considered **unmanaged** -- typically early-stage or legacy artefacts not yet under custodial governance.

When an artefact's HRID changes (e.g. through transfer or forking), a new `uid` must also be assigned to prevent confusion between the original and the transferred artefact.

## Semantic Versioning

Version identifiers follow [Semantic Versioning](http://semver.org) with three levels plus optional lifecycle extensions:

```
version_id      = release_version [ extension ]
release_version = major_version '.' minor_version '.' patch_version
extension       = version_modifier '.' issue_number
version_modifier = '-rc' | '-alpha'
```

### Version Levels

- **Major version**: Incremented on breaking changes to the formal definition (paths removed, constraints narrowed, nodes moved). Resets minor and patch to 0.
- **Minor version**: Incremented on non-breaking enhancements (new nodes, widened constraints, new terminology bindings). Resets patch to 0.
- **Patch version**: Incremented on changes to informal parts only (metadata, translations, non-semantic terminology wording).
- **Build number** (`build_uid`): Incremented at every commit; reset to 1 when any version component changes.

### Extensions

- **`-alpha`**: Development version prior to the target release. Example: `1.3.5-alpha`.
- **`-rc.N`**: Release candidate N for the target version. Example: `1.3.5-rc.3`.

**Version precedence:** `1.2.3-rc.1 < 1.2.3-rc.2 < 1.2.3 < 1.2.4-alpha < 1.3.0-alpha < 1.3.0`

The first version of an artefact is `v0.N.P` (typically `0.0.1`). Higher v0 versions indicate relative maturity before the first stable release.

## Archetype Signature

The **archetype signature** is the formal definition of what constitutes the archetype's "interface" for versioning purposes:

> Archetype signature = the set of `<path, RM type, AOM constraint>` tuples for every definition node.

An archetype interface is **preserved** (non-breaking) when:

- All existing paths remain unchanged (hierarchy and id-codes identical)
- No paths are deleted
- No domain meaning changes for id-codes in paths
- RM types are identical or ancestor types of originals
- Constraints at each path are identical or wider than originals

Changes that break the interface (node removal, constraint narrowing, node movement) require a new **major** version. Non-breaking additions (new paths, widened constraints) require a **minor** version increment. Note that referencing by major version alone may not designate all available interface elements -- a minimum minor version is sometimes needed.

## Lifecycle States

Artefacts progress through macro-level lifecycle states:

| State | Description |
|-------|-------------|
| `unmanaged` | No custodial organisation; early-stage or legacy artefact |
| `development` | Under active development within a managed repository |
| `release_candidate` | Candidate for publication; version tagged as `M.N.P-rc.B` |
| `published` | Definitive public release with stable `M.N.P` version |
| `deprecated` | Still available but superseded; version unchanged |
| `rejected` | Reviewed and rejected; version unchanged |

**Typical progression:** `[unmanaged ->] development -> published` or `development -> release_candidate -> published -> deprecated`.

From `release_candidate`, three outcomes are possible: publish definitively, release a newer RC (patch-level changes only), or return to `development` for larger changes.

## Reference Types

References between artefacts use partial HRIDs that are matched against full identifiers. Three reference types exist:

| Reference Type | Format | Matches |
|----------------|--------|---------|
| **ihrid_ref** (Interface HRID) | `hrid_root.vN` | Latest release of major version N |
| **sihrid_ref** (Specific Interface HRID) | `hrid_root.vN.M` | Specific release with major.minor version |
| **phrid_ref** (Physical HRID) | `hrid_root.vN.M.P` | Exact artefact instance |

**Example:**
```
org.openehr::openEHR-EHR-EVALUATION.diagnosis.v1       # ihrid_ref: any v1.x.x
org.openehr::openEHR-EHR-EVALUATION.diagnosis.v1.1     # sihrid_ref: any v1.1.x
org.openehr::openEHR-EHR-EVALUATION.diagnosis.v1.1.5   # phrid_ref: exact version
```

Source archetypes typically use `ihrid_ref` (major version only). Templates may use any level of specificity. AQL queries need to reference at least the minor version if they depend on paths added after the initial major release.

References without a namespace are assumed to be in the same namespace as the referencing artefact.

## Distributed Governance and Namespace Management

Archetypes are produced either independently (unmanaged) or within **Custodian Organisations (COs)** that maintain repositories, registries, and ontological classifications.

### Management Adoption

When an unmanaged artefact is adopted by a CO:

1. Lifecycle state progresses to `initial`
2. HRID gains a namespace prefix
3. A new GUID is assigned as `uid`
4. If major version > 0, it resets to `0.0.1`
5. Metadata is set (copyright, license)
6. A SHA-1 hash may be generated

### Transfer and Forking

When a CO transfers custodianship to another organisation, HRID components may change:

- `namespace` always changes (at minimum)
- `concept_id` may change if the new CO's ontology requires it
- `release_version` likely changes
- `rm_publisher`, `rm_closure`, `rm_class` cannot change

Both the HRID and `uid` must change upon transfer, and an **equivalence record** is maintained in the artefact's metadata (similar to DNS CNAME records), tracking the mapping between old and new identifiers with timestamps.

## Artefact Authentication

### Integrity Check (Hashing)

A digital hash (SHA-1 or MD5) on a **canonical form** of the artefact provides a fingerprint guaranteeing identity. The canonical form strips semantically-insignificant differences (whitespace, non-significant ordering, metadata) to ensure that functionally identical artefacts always produce the same hash.

The canonical form (called the "semantic view") is built from the validated artefact's Abstract Syntax Tree and includes: identifier, specialisation identifier, concept code, and definition section (comments stripped). It is serialised in dADL syntax.

### Digital Signatures

True origin authentication uses PKI: each Custodian Organisation generates a key pair, publishes the public key with a Central Governance Authority, and signs the hash digest with its private key. Consumers verify signatures using the public key.

**Process:** Source artefact -> Canonical form -> Hash digest -> Private key signing -> Digital signature

## Related Pages

- [[archetype-model]] -- The archetype formalism including three-layer architecture and specialisation
- [[archetype-object-model]] -- AOM 2 constraint model classes and flattening
- [[archetype-definition-language]] -- ADL 2 syntax where these identifiers are expressed
- [[operational-templates]] -- Compiled artefacts that resolve all references to full versioned identifiers
- [[base-component]] -- Foundation types including the identification hierarchy

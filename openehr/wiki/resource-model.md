---
title: Resource Model
type: entity
sources:
  - raw/base-resource.md
created: 2026-04-13
updated: 2026-04-13
---

# Resource Model

The Resource Model defines the structure and semantics of an online resource created by a human author, with support for identification, metadata, annotations, natural language translations, and revision history. It resides in the `resource` package of the [[base-component]] (BASE Release 1.2.0) and carries STABLE status.

## History

The Resource Model was extracted from the RM Common Information Model specification (RM 1.0.3) in BASE Release 1.2.0 (February 2016) to enable reuse across openEHR components beyond the Reference Model. This separation allows any authored artifact -- not just RM-based ones -- to inherit standard metadata and translation infrastructure.

## AUTHORED_RESOURCE

The central abstract class representing any online resource created by a human author. All openEHR authored artifacts that need metadata, translations, and revision control inherit from this class.

### Attributes

| Cardinality | Attribute | Type | Description |
|-------------|-----------|------|-------------|
| 0..1 | `uid` | UUID | Unique identifier of the resource family |
| 1..1 | `original_language` | Terminology_code | Initial authorship language (ISO 639-1) |
| 0..1 | `description` | RESOURCE_DESCRIPTION | Descriptive metadata and lifecycle information |
| 0..1 | `is_controlled` | Boolean | Whether the resource is under change control |
| 0..1 | `annotations` | Hash | Path-keyed annotations on resource items |
| 0..1 | `translations` | Hash<String, TRANSLATION_DETAILS> | Language-keyed translation records |

### Functions

| Return | Signature | Description |
|--------|-----------|-------------|
| String | `current_revision()` | Most recent revision, or "(uncontrolled)" if not controlled |
| List<String> | `languages_available()` | All languages present in the resource |

### Key Invariants

- Original language must be a valid ISO 639-1 code
- Translations must not include the original language
- Description language codes must match translation keys
- Revision history is required if `is_controlled` is True
- Original language always appears in `languages_available()`

### Who Inherits from AUTHORED_RESOURCE

- **ARCHETYPE** (via the [[archetype-object-model]]) -- all archetypes carry authorship metadata, translations, and lifecycle state through this inheritance
- **GUIDELINE** (in [[guideline-definition-language]] GDL2) -- clinical decision support guidelines inherit metadata infrastructure directly

## RESOURCE_DESCRIPTION

Captures the language-independent descriptive metadata of a resource.

### Attributes

| Cardinality | Attribute | Type | Description |
|-------------|-----------|------|-------------|
| 1..1 | `original_author` | Hash<String, String> | Original author details (name, email, organization, date) |
| 0..1 | `original_namespace` | String | Author organization namespace (reverse internet form) |
| 0..1 | `original_publisher` | String | Original publishing organization |
| 0..1 | `other_contributors` | List<String> | Additional contributors in "name <email>" format |
| 1..1 | `lifecycle_state` | Terminology_code | Resource lifecycle status (e.g., draft, published, deprecated) |
| 1..1 | `parent_resource` | AUTHORED_RESOURCE | Back-reference to the owning resource |
| 0..1 | `custodian_namespace` | String | Current custodian's namespace |
| 0..1 | `custodian_organisation` | String | Current custodian organization |
| 0..1 | `copyright` | String | Copyright statement |
| 0..1 | `licence` | String | License in "name <URL>" format |
| 0..1 | `ip_acknowledgements` | Hash<String, String> | Intellectual property acknowledgments |
| 0..1 | `references` | Hash<String, String> | Citation references |
| 0..1 | `resource_package_uri` | String | URI of the resource package |
| 0..1 | `conversion_details` | Hash<String, String> | Model conversion metadata |
| 0..1 | `other_details` | Hash<String, String> | Additional non-linguistic metadata |
| 0..1 | `details` | Hash<String, RESOURCE_DESCRIPTION_ITEM> | Language-specific descriptions |

## RESOURCE_DESCRIPTION_ITEM

Captures language-specific descriptive details. Each supported language has its own instance.

### Attributes

| Cardinality | Attribute | Type | Description |
|-------------|-----------|------|-------------|
| 1..1 | `language` | Terminology_code | The language of this description (ISO 639-1) |
| 1..1 | `purpose` | String | Statement of the resource's purpose |
| 0..1 | `keywords` | List<String> | Indexing and search keywords |
| 0..1 | `use` | String | Appropriate usage contexts |
| 0..1 | `misuse` | String | Inappropriate usage contexts |
| 0..1 | `original_resource_uri` | Hash<String, String> | URIs of source clinical documents |
| 0..1 | `other_details` | Hash<String, String> | Additional language-sensitive metadata |

## TRANSLATION_DETAILS

Provides metadata about a natural language translation.

### Attributes

| Cardinality | Attribute | Type | Description |
|-------------|-----------|------|-------------|
| 1..1 | `language` | Terminology_code | Translation target language (ISO 639-1) |
| 1..1 | `author` | Hash<String, String> | Translator name and demographics |
| 0..1 | `accreditation` | String | Translator registration or membership ID |
| 0..1 | `other_details` | Hash<String, String> | Additional metadata |
| 0..1 | `version_last_translated` | String | Resource version when last translated |
| 0..1 | `other_contributors` | List<String> | Additional translation contributors |

## Natural Language and Translation Model

Authored resources are created in an original language stored in `original_language`. Translation involves:

1. Converting all language-dependent elements to the target language
2. Adding a new TRANSLATION_DETAILS instance to the `translations` attribute
3. Recording translator details, organization, and quality assurance information

The `languages_available()` function returns the complete list of supported languages (original plus all translations).

## Revision History

When `is_controlled` is True, changes undergo audit trail recording. The `revision_history` attribute stores a documentary copy of the revision history for interoperable use across tools and repositories.

## Related Pages

- [[base-component]] -- the BASE component that contains the resource package
- [[archetype-object-model]] -- ARCHETYPE inherits from AUTHORED_RESOURCE
- [[guideline-definition-language]] -- GDL2 GUIDELINE inherits from AUTHORED_RESOURCE

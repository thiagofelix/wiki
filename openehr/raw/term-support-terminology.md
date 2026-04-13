# Support Terminology Specification

## Amendment Record

| Issue | Details | Raiser | Completed |
|-------|---------|--------|-----------|
| **TERM Release 3.0.0** | | | |
| 3.0.0 | SPECTERM-23: Improving translations | S Kobayashi, V Pereira, D Bosca | 26 Jun 2023 |
| | SPECTERM-25: Adding "format conversion" and "restoration" new types to audit_change_type group | S Iancu | 05 Mar 2023 |
| | SPECTERM-5: Adding "report" to Composition Category | B Næss, S Iancu | 05 Mar 2023 |
| | SPECTERM-15: Rendering terminology code sets and vocabulary in SupportTerminology document | S Iancu | 11 Feb 2023 |
| | SPECTERM-16: Rendering terminology as FHIR CodeSystem and ValueSet | S Iancu | 11 Feb 2023 |
| | SPECTERM-17: Improving terminology XML file format | S Iancu | 11 Feb 2023 |
| | SPECTERM-24: Added PropertyUnitData.xml file | V Pereira, S Ljosland Bakke | 04 Feb 2023 |
| **TERM Release 2.4.0** | | | |
| 2.4.2 | SPECTERM-22: Added missing SHA-* integrity check algorithms | S Iancu | 13 Dec 2022 |
| | SPECTERM-21: Corrected terminology rubric typos in "property" group | S Iancu, P Pazos | 13 Dec 2022 |
| | SPECTERM-4: Added new vocabulary groups for EHR Extract | S Iancu, T Beale | 13 Dec 2022 |
| | SPECTERM-10: Added "inactive" and "abandoned" to version lifecycle state | S Iancu, T Beale | 13 Dec 2022 |
| | SPECTERM-20: Added "mental healthcare" to "setting" group | S Iancu, J Holslag | 13 Dec 2022 |

## Acknowledgements

The work reported in this specification has been funded in part by:

- FreshEHR Informatics, UK
- Ocean Informatics, Australia
- Code24, The Netherlands

### Trademarks

'openEHR' is a trademark of the openEHR Foundation

## 1. Preface

### 1.1. Purpose

This document describes the openEHR Support Terminology and code sets, defining the vocabulary and codes needed for the openEHR Reference, Archetype and Service models. The openEHR terminology differs from externally defined terminologies such as SNOMED CT and ICDx, as it functions as "informational classifiers needed by the openEHR models" rather than an ontology of clinical facts.

The audience includes:

- Standards bodies producing health informatics standards
- Software development organisations developing EHR systems
- Academic groups studying the EHR
- The open source healthcare community

### 1.2. Related Documents

Prerequisite documents:

- The openEHR Architecture Overview

### 1.3. Status

This specification is in the STABLE state. The development version is available at: https://specifications.openehr.org/releases/TERM/latest/SupportTerminology.html

### 1.4. Feedback

Feedback may be provided on the [openEHR Terminology specifications forum](https://discourse.openehr.org/c/specifications/terminology).

Issues may be raised on the [specifications Problem Report tracker](https://specifications.openehr.org/components/TERM/open_issues).

### 1.5. Requests for new Terminology Codes

Requests for codes may be made by raising a new issue on the specifications Problem Report tracker; the 'Component' field must be set to 'TERM - openEHR Terminology'.

### 1.6. Creating and Maintaining Translations

A new translation is created by:

1. Forking the `specifications-TERM` repository
2. Creating a new file `openehr_terminology.xml` in directory `/computable/XML/xx`, where `xx` is an ISO 639-1 two-character language code
3. Upon completion, creating a Pull Request
4. Raising a new issue on the specifications Problem Report tracker with 'Component' set to 'TERM - openEHR Terminology'

Translations are maintained through notifications to editors or GitHub authors of current translations when new codes are added.

## 2. Overview

This document provides a documentary expression of the openEHR Support Terminology, consisting of code sets and vocabulary providing values for coded attributes in the openEHR Reference Model.

The computable form of this terminology is available in the [openEHR `specifications-TERM` repository](https://github.com/openEHR/specifications-TERM), serving as the definitive expression. Access to terminology in the openEHR reference model is via classes defined in the package `rm.support.terminology`.

Two types of coded entities are used in openEHR:

**Self-defining codes:** Codes that do not have separate rubrics and "stand for themselves". ISO country and language codes are examples. These are represented by the `CODE_PHRASE` type. Code sets are mostly internet vocabularies defined by ISO or IETF.

**True coded terms:** Codes are concept identifiers with rubrics and descriptions, potentially in multiple languages. The linguistic expression depends on language. Most clinical terminologies and openEHR vocabularies fall into this category. Terms are expressed as instances of the openEHR data type `DV_CODED_TEXT`.

The openEHR Terminology provides mappings to other recognised terminologies or vocabularies where available.

## 3. Terminology

### 3.1. Code Sets

#### 3.1.1. Countries

**Code Set details**

- **Name:** countries
- **Id:** countries
- **External_id:** ISO_3166-1
- **Reference:** [ISO Countries list](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Current_codes)
- **Status:** active

This code set defined by the ISO 3166-1 "alpha-2" standard consists of two-character names of countries and country subdivisions.

**Used in:** `COMPOSITION.territory`

| Code | Description | Status |
|------|-------------|--------|
| AF | AFGHANISTAN | active |
| AX | ÅLAND ISLANDS | active |
| AL | ALBANIA | active |
| DZ | ALGERIA | active |
| AS | AMERICAN SAMOA | active |
| AD | ANDORRA | active |
| AO | ANGOLA | active |
| AI | ANGUILLA | active |
| AQ | ANTARCTICA | active |
| AG | ANTIGUA AND BARBUDA | active |
| AR | ARGENTINA | active |
| AM | ARMENIA | active |
| AW | ARUBA | active |
| AU | AUSTRALIA | active |
| AT | AUSTRIA | active |
| AZ | AZERBAIJAN | active |
| BS | BAHAMAS | active |
| BH | BAHRAIN | active |
| BD | BANGLADESH | active |
| BB | BARBADOS | active |
| BY | BELARUS | active |
| BE | BELGIUM | active |
| BZ | BELIZE | active |
| BJ | BENIN | active |
| BM | BERMUDA | active |
| BT | BHUTAN | active |
| BO | BOLIVIA | active |
| BQ | BONAIRE, SINT EUSTATIUS AND SABA | active |
| BA | BOSNIA AND HERZEGOVINA | active |
| BW | BOTSWANA | active |
| BV | BOUVET ISLAND | active |
| BR | BRAZIL | active |
| IO | BRITISH INDIAN OCEAN TERRITORY | active |
| BN | BRUNEI DARUSSALAM | active |
| BG | BULGARIA | active |
| BF | BURKINA FASO | active |
| BI | BURUNDI | active |
| KH | CAMBODIA | active |
| CM | CAMEROON | active |
| CA | CANADA | active |
| CV | CAPE VERDE | active |
| KY | CAYMAN ISLANDS | active |
| CF | CENTRAL AFRICAN REPUBLIC | active |
| TD | CHAD | active |
| CL | CHILE | active |
| CN | CHINA | active |
| CX | CHRISTMAS ISLAND | active |
| CC | COCOS (KEELING) ISLANDS | active |
| CO | COLOMBIA | active |
| KM | COMOROS | active |
| CG | CONGO | active |
| CD | CONGO, THE DEMOCRATIC REPUBLIC OF THE | active |
| CK | COOK ISLANDS | active |
| CR | COSTA RICA | active |
| CI | CÔTE D'IVOIRE | active |
| HR | CROATIA | active |
| CU | CUBA | active |
| CW | CURAÇAO | active |
| CY | CYPRUS | active |
| CZ | CZECH REPUBLIC | active |
| DK | DENMARK | active |
| DJ | DJIBOUTI | active |
| DM | DOMINICA | active |
| DO | DOMINICAN REPUBLIC | active |
| EC | ECUADOR | active |
| EG | EGYPT | active |
| SV | EL SALVADOR | active |
| GQ | EQUATORIAL GUINEA | active |
| ER | ERITREA | active |
| EE | ESTONIA | active |
| SZ | ESWATINI | active |
| ET | ETHIOPIA | active |
| FK | FALKLAND ISLANDS (MALVINAS) | active |
| FO | FAROE ISLANDS | active |
| FJ | FIJI | active |
| FI | FINLAND | active |
| FR | FRANCE | active |
| GF | FRENCH GUIANA | active |
| PF | FRENCH POLYNESIA | active |
| TF | FRENCH SOUTHERN TERRITORIES | active |
| GA | GABON | active |
| GM | GAMBIA | active |
| GE | GEORGIA | active |
| DE | GERMANY | active |
| GH | GHANA | active |
| GI | GIBRALTAR | active |
| GR | GREECE | active |
| GL | GREENLAND | active |
| GD | GRENADA | active |
| GP | GUADELOUPE | active |
| GU | GUAM | active |
| GT | GUATEMALA | active |
| GG | GUERNSEY | active |
| GN | GUINEA | active |
| GW | GUINEA-BISSAU | active |
| GY | GUYANA | active |
| HT | HAITI | active |
| HM | HEARD ISLAND AND MCDONALD ISLANDS | active |
| VA | HOLY SEE (VATICAN CITY STATE) | active |
| HN | HONDURAS | active |
| HK | HONG KONG | active |
| HU | HUNGARY | active |
| IS | ICELAND | active |
| IN | INDIA | active |
| ID | INDONESIA | active |
| IR | IRAN, ISLAMIC REPUBLIC OF | active |
| IQ | IRAQ | active |
| IE | IRELAND | active |
| IM | ISLE OF MAN | active |
| IL | ISRAEL | active |
| IT | ITALY | active |
| JM | JAMAICA | active |
| JP | JAPAN | active |
| JE | JERSEY | active |
| JO | JORDAN | active |
| KZ | KAZAKHSTAN | active |
| KE | KENYA | active |
| KI | KIRIBATI | active |
| KP | KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF | active |
| KR | KOREA, REPUBLIC OF | active |
| KW | KUWAIT | active |
| KG | KYRGYZSTAN | active |
| LA | LAO PEOPLE'S DEMOCRATIC REPUBLIC | active |
| LV | LATVIA | active |
| LB | LEBANON | active |
| LS | LESOTHO | active |
| LR | LIBERIA | active |
| LY | LIBYA | active |
| LI | LIECHTENSTEIN | active |
| LT | LITHUANIA | active |
| LU | LUXEMBOURG | active |
| MO | MACAO | active |
| MG | MADAGASCAR | active |
| MW | MALAWI | active |
| MY | MALAYSIA | active |
| MV | MALDIVES | active |
| ML | MALI | active |
| MT | MALTA | active |
| MH | MARSHALL ISLANDS | active |
| MQ | MARTINIQUE | active |
| MR | MAURITANIA | active |
| MU | MAURITIUS | active |
| YT | MAYOTTE | active |
| MX | MEXICO | active |
| FM | MICRONESIA, FEDERATED STATES OF | active |
| MD | MOLDOVA, REPUBLIC OF | active |
| MC | MONACO | active |
| MN | MONGOLIA | active |
| ME | MONTENEGRO | active |
| MS | MONTSERRAT | active |
| MA | MOROCCO | active |
| MZ | MOZAMBIQUE | active |
| MM | MYANMAR | active |
| NA | NAMIBIA | active |
| NR | NAURU | active |
| NP | NEPAL | active |
| NL | NETHERLANDS | active |
| AN | NETHERLANDS ANTILLES - DEPRECATED | active |
| NC | NEW CALEDONIA | active |
| NZ | NEW ZEALAND | active |
| NI | NICARAGUA | active |
| NE | NIGER | active |
| NG | NIGERIA | active |
| NU | NIUE | active |
| NF | NORFOLK ISLAND | active |
| MK | NORTH MACEDONIA | active |
| MP | NORTHERN MARIANA ISLANDS | active |
| NO | NORWAY | active |
| OM | OMAN | active |
| PK | PAKISTAN | active |
| PW | PALAU | active |
| PS | PALESTINIAN, STATE OF | active |
| PA | PANAMA | active |
| PG | PAPUA NEW GUINEA | active |
| PY | PARAGUAY | active |
| PE | PERU | active |
| PH | PHILIPPINES | active |
| PN | PITCAIRN | active |
| PL | POLAND | active |
| PT | PORTUGAL | active |
| PR | PUERTO RICO | active |
| QA | QATAR | active |
| RE | RÉUNION | active |
| RO | ROMANIA | active |
| RU | RUSSIAN FEDERATION | active |
| RW | RWANDA | active |
| BL | SAINT BARTHÉLEMY | active |
| SH | SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA | active |
| KN | SAINT KITTS AND NEVIS | active |
| LC | SAINT LUCIA | active |
| MF | SAINT MARTIN (FRENCH PART) | active |
| PM | SAINT PIERRE AND MIQUELON | active |
| VC | SAINT VINCENT AND THE GRENADINES | active |
| WS | SAMOA | active |
| SM | SAN MARINO | active |
| ST | SAO TOME AND PRINCIPE | active |
| SA | SAUDI ARABIA | active |
| SN | SENEGAL | active |
| RS | SERBIA | active |
| SC | SEYCHELLES | active |
| SL | SIERRA LEONE | active |
| SG | SINGAPORE | active |
| SX | SINT MAARTEN (DUTCH PART) | active |
| SK | SLOVAKIA | active |
| SI | SLOVENIA | active |
| SB | SOLOMON ISLANDS | active |
| SO | SOMALIA | active |
| ZA | SOUTH AFRICA | active |
| GS | SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS | active |
| SS | SOUTH SUDAN | active |
| ES | SPAIN | active |
| LK | SRI LANKA | active |
| SD | SUDAN | active |
| SR | SURINAME | active |
| SJ | SVALBARD AND JAN MAYEN | active |
| SE | SWEDEN | active |
| CH | SWITZERLAND | active |
| SY | SYRIAN ARAB REPUBLIC | active |
| TW | TAIWAN, PROVINCE OF CHINA | active |
| TJ | TAJIKISTAN | active |
| TZ | TANZANIA, UNITED REPUBLIC OF | active |
| TH | THAILAND | active |
| TL | TIMOR-LESTE | active |
| TG | TOGO | active |
| TK | TOKELAU | active |
| TO | TONGA | active |
| TT | TRINIDAD AND TOBAGO | active |
| TN | TUNISIA | active |
| TR | TÜRKIYE | active |
| TM | TURKMENISTAN | active |
| TC | TURKS AND CAICOS ISLANDS | active |
| TV | TUVALU | active |
| UG | UGANDA | active |
| UA | UKRAINE | active |
| AE | UNITED ARAB EMIRATES | active |
| GB | UNITED KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND | active |
| US | UNITED STATES OF AMERICA | active |
| UM | UNITED STATES MINOR OUTLYING ISLANDS | active |
| UY | URUGUAY | active |
| UZ | UZBEKISTAN | active |
| VU | VANUATU | active |
| VE | VENEZUELA, BOLIVARIAN REPUBLIC OF | active |
| VN | VIET NAM | active |
| VG | VIRGIN ISLANDS, BRITISH | active |
| VI | VIRGIN ISLANDS, U.S. | active |
| WF | WALLIS AND FUTUNA | active |
| EH | WESTERN SAHARA | active |
| YE | YEMEN | active |
| ZM | ZAMBIA | active |
| ZW | ZIMBABWE | active |

#### 3.1.2. Character Sets

**Code Set details**

- **Name:** character sets
- **Id:** character_sets
- **External_id:** IANA_character-sets
- **Reference:** [IANA Character Sets](https://www.iana.org/assignments/character-sets)
- **Status:** active

This IANA (Internet Naming Authority) code set consists of the names of recognised character sets.

**Used in:** `ENTRY.encoding`, `DV_ENCAPSULATED.charset`

| Code | Description | Status |
|------|-------------|--------|
| ISO-10646-UTF-1 | | active |
| ISO_8859-1:1987 | | active |
| ISO-8859-2 | | active |
| ISO_8859-3:1988 | | active |
| ISO-8859-15 | | active |
| US-ASCII | | active |
| UTF-7 | | active |
| UTF-8 | | active |
| UTF-16 | | active |
| UTF-16BE | | active |
| UTF-16LE | | active |
| UTF-32 | | active |
| UTF-32BE | | active |
| UTF-32LE | | active |

#### 3.1.3. Languages

**Code Set details**

- **Name:** languages
- **Id:** languages
- **External_id:** ISO_639-1
- **Reference:** [ISO Language codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)
- **Status:** active

This code set consists of the language tags defined by RFC-5646. The syntax consists of the ISO 639-1 "alpha-2" form of names of languages, often followed by a region subtag from the ISO 3166-1 "alpha-2" country list. These are maintained by the [IANA Language Subtag Registry](https://www.iana.org/assignments/language-subtag-registry).

**NOTE:** This code set does not cover all languages, whereas ISO 639-2 "alpha-3" covers many more languages of cultural or indigenous interest.

**Used in:** `ENTRY.language`, `COMPOSITION.language`, `DV_ENCAPSULATED.language`

| Code | Description | Status |
|------|-------------|--------|
| aa | Afar | active |
| af | Afrikaans | active |
| ak | Akan | active |
| sq | Albanian | active |
| am | Amharic | active |
| ar | Arabic | active |
| ar-sa | Arabic (Saudi Arabia) | active |
| ar-iq | Arabic (Iraq) | active |
| ar-eg | Arabic (Egypt) | active |
| ar-ly | Arabic (Libya) | active |
| ar-dz | Arabic (Algeria) | active |
| ar-ma | Arabic (Morocco) | active |
| ar-tn | Arabic (Tunisia) | active |
| ar-om | Arabic (Oman) | active |
| ar-ye | Arabic (Yemen) | active |
| ar-sy | Arabic (Syria) | active |
| ar-jo | Arabic (Jordan) | active |
| ar-lb | Arabic (Lebanon) | active |
| ar-kw | Arabic (Kuwait) | active |
| ar-ae | Arabic (U.A.E.) | active |
| ar-bh | Arabic (Bahrain) | active |
| ar-qa | Arabic (Qatar) | active |
| an | Aragonese | active |
| hy | Armenian | active |
| as | Assamese | active |
| av | Avaric, Avar | active |
| ay | Aymara | active |
| az | Azerbaijani, Azeri | active |
| bm | Bambara | active |
| ba | Bashkir | active |
| eu | Basque | active |
| be | Belarusian | active |
| bn | Bengali, Bangla | active |
| bi | Bislama | active |
| bs | Bosnian | active |
| br | Breton | active |
| bg | Bulgarian | active |
| my | Burmese, Myanmar | active |
| ca | Catalan, Valencian | active |
| ch | Chamorro | active |
| ce | Chechen | active |
| ny | Chichewa, Chewa, Nyanja | active |
| zh | Chinese | active |
| zh-tw | Chinese (Taiwan) | active |
| zh-cn | Chinese (PRC) | active |
| zh-hk | Chinese (Hong Kong SAR) | active |
| zh-sg | Chinese (Singapore) | active |
| zh-mo | Chinese (Macau) | active |
| cv | Chuvash | active |
| kw | Cornish | active |
| co | Corsican | active |
| cr | Cree | active |
| hr | Croatian | active |
| hr-ba | Croatian (Bosnia and Herzegovina) | active |
| cs | Czech | active |
| da | Danish | active |
| dv | Divehi, Dhivehi, Maldivian | active |
| nl | Dutch | active |
| nl-be | Dutch (Belgium) | active |
| dz | Dzongkha | active |
| en | English | active |
| en-us | English (United States) | active |
| en-gb | English (United Kingdom) | active |
| en-au | English (Australia) | active |
| en-ca | English (Canada) | active |
| en-nz | English (New Zealand) | active |
| en-ie | English (Ireland) | active |
| en-za | English (South Africa) | active |
| en-jm | English (Jamaica) | active |
| en-cb | English (Caribbean) | active |
| en-bz | English (Belize) | active |
| en-tt | English (Trinidad and Tobago) | active |
| en-ph | English (Republic of the Philippines) | active |
| en-zw | English (Zimbabwe) | active |
| eo | Esperanto | active |
| et | Estonian | active |
| ee | Ewe | active |
| fo | Faroese | active |
| fj | Fijian | active |
| fi | Finnish | active |
| fr | French | active |
| fr-be | French (Belgium) | active |
| fr-ca | French (Canada) | active |
| fr-ch | French (Switzerland) | active |
| fr-lu | French (Luxembourg) | active |
| fr-mc | French (Principality of Monaco) | active |
| fy | Frisian, Western Frisian | active |
| ff | Fulah, Fulani | active |
| gd | Gaelic, Scottish Gaelic | active |
| gd-ie | Gaelic (Ireland) | active |
| gl | Galician | active |
| lg | Ganda | active |
| ka | Georgian | active |
| de | German | active |
| de-ch | German (Switzerland) | active |
| de-at | German (Austria) | active |
| de-lu | German (Luxembourg) | active |
| de-li | German (Liechtenstein) | active |
| el | Greek | active |
| kl | Kalaallisut, Greenlandic | active |
| gn | Guarani | active |
| gu | Gujarati | active |
| ht | Haitian, Haitian Creole | active |
| ha | Hausa | active |
| he | Hebrew | active |
| hz | Herero | active |
| hi | Hindi | active |
| ho | Hiri Motu, Pidgin Motu | active |
| hu | Hungarian | active |
| is | Icelandic | active |
| ig | Igbo | active |
| id | Indonesian | active |
| iu | Inuktitut | active |
| ik | Inupiaq | active |
| ga | Irish | active |
| it | Italian | active |
| it-ch | Italian (Switzerland) | active |
| ja | Japanese | active |
| jv | Javanese | active |
| kn | Kannada | active |
| kr | Kanuri | active |
| ks | Kashmiri | active |
| kk | Kazakh | active |
| km | Central Khmer, Cambodian | active |
| ki | Kikuyu, Gikuyu | active |
| rw | Kinyarwanda | active |
| ky | Kirghiz, Kyrgyz | active |
| kv | Komi | active |
| kg | Kongo | active |
| ko | Korean | active |
| kj | Kuanyama, Kwanyama | active |
| ku | Kurdish | active |
| lo | Lao | active |
| la | Latin | active |
| lv | Latvian | active |
| li | Limburgan, Limburger, Limburgish | active |
| ln | Lingala | active |
| lt | Lithuanian | active |
| lu | Luba-Katanga, Luba-Shaba | active |
| lb | Luxembourgish, Letzeburgesch | active |
| mk | Macedonian | active |
| mg | Malagasy | active |
| ms | Malay | active |
| ml | Malayalam | active |
| mt | Maltese | active |
| gv | Manx | active |
| mi | Maori | active |
| mr | Marathi | active |
| mh | Marshallese | active |
| mn | Mongolian | active |
| na | Nauru, Nauruan | active |
| nv | Navajo, Navaho | active |
| nd | North Ndebele | active |
| nr | South Ndebele | active |
| ng | Ndonga | active |
| ne | Nepali | active |
| nb | Norwegian Bokmal | active |
| nn | Norwegian Nynorsk | active |
| ii | Sichuan Yi, Nuosu, Northern Yi, Liangshan Yi | active |
| oc | Occitan | active |
| oj | Ojibwa, Ojibwe | active |
| or | Oriya, Odia | active |
| om | Oromo | active |
| os | Ossetian, Ossetic | active |
| ps | Pashto, Pushto | active |
| fa | Persian, Farsi | active |
| pl | Polish | active |
| pt | Portuguese | active |
| pt-br | Portuguese (Brazil) | active |
| pt-pt | Portuguese (Portugal) - DEPRECATED | active |
| pa | Punjabi, Panjabi | active |
| qu | Quechua | active |
| qu-bo | Quechua (Bolivia) | active |
| qu-ec | Quechua (Ecuador) | active |
| qu-pe | Quechua (Peru) | active |
| ro | Romanian | active |
| ro-mo | Romanian (Moldavia) | active |
| rm | Romansh, Rhaeto-Romanic | active |
| rn | Rundi, Kirundi | active |
| ru | Russian | active |
| ru-mo | Russian (Moldavia) | active |
| se | Northern Sami | active |
| sz | Sami (Lappish) - DEPRECATED | active |
| sm | Samoan | active |
| sg | Sango | active |
| sc | Sardinian | active |
| sr | Serbian | active |
| sr-ba | Serbian (Bosnia and Herzegovina) | active |
| sb | Serbian - DEPRECATED | active |
| sn | Shona | active |
| sd | Sindhi | active |
| si | Sinhala, Sinhalese | active |
| sk | Slovak | active |
| sl | Slovenian, Slovene | active |
| so | Somali | active |
| st | Southern Sotho, Sesotho, Sutu | active |
| es | Spanish, Castilian | active |
| es-mx | Spanish (Mexico) | active |
| es-gt | Spanish (Guatemala) | active |
| es-cr | Spanish (Costa Rica) | active |
| es-pa | Spanish (Panama) | active |
| es-do | Spanish (Dominican Republic) | active |
| es-ve | Spanish (Venezuela) | active |
| es-co | Spanish (Colombia) | active |
| es-pe | Spanish (Peru) | active |
| es-ar | Spanish (Argentina) | active |
| es-ec | Spanish (Ecuador) | active |
| es-cl | Spanish (Chile) | active |
| es-uy | Spanish (Uruguay) | active |
| es-py | Spanish (Paraguay) | active |
| es-bo | Spanish (Bolivia) | active |
| es-sv | Spanish (El Salvador) | active |
| es-hn | Spanish (Honduras) | active |
| es-ni | Spanish (Nicaragua) | active |
| es-pr | Spanish (Puerto Rico) | active |
| su | Sundanese | active |
| sx | Sutu - DEPRECATED | active |
| sw | Swahili | active |
| ss | Swati, Swazi | active |
| sv | Swedish | active |
| sv-fi | Swedish (Finland) | active |
| tl | Tagalog | active |
| ty | Tahitian | active |
| tg | Tajik | active |
| ta | Tamil | active |
| tt | Tatar | active |
| te | Telugu | active |
| th | Thai | active |
| bo | Tibetan | active |
| ti | Tigrinya | active |
| to | Tonga, Tongan | active |
| ts | Tsonga | active |
| tn | Tswana | active |
| tr | Turkish | active |
| tk | Turkmen | active |
| tw | Twi | active |
| ug | Uighur, Uyghur | active |
| uk | Ukrainian | active |
| ur | Urdu | active |
| uz | Uzbek | active |
| ve | Venda | active |
| vi | Vietnamese | active |
| wa | Walloon | active |
| cy | Welsh | active |
| cy-gb | Welsh (United Kingdom) | active |
| cy-ar | Welsh (Argentina) | active |
| wo | Wolof | active |
| xh | Xhosa | active |
| yi | Yiddish | active |
| ji | Yiddish - DEPRECATED | active |
| yo | Yoruba | active |
| za | Zhuang, Chuang | active |
| zu | Zulu | active |

#### 3.1.4. Media Types

**Code Set details**

- **Name:** media types
- **Id:** media_types
- **External_id:** IANA_media-types
- **Reference:** [IANA Media Types](https://www.iana.org/assignments/media-types)
- **Status:** active

This IANA (Internet Naming Authority) code set consists of the names of media types.

**Used in:** `DV_MULTIMEDIA.media_type`

| Code | Description | Status |
|------|-------------|--------|
| audio/DVI4 | | active |
| audio/G722 | | active |
| audio/G723 | | active |
| audio/G726-16 | | active |
| audio/G726-24 | | active |
| audio/G726-32 | | active |
| audio/G726-40 | | active |
| audio/G728 | | active |
| audio/L8 | | active |
| audio/L16 | | active |
| audio/LPC | | active |
| audio/G729 | | active |
| audio/G729D | | active |
| audio/G729E | | active |
| video/BT656 | | active |
| video/CelB | | active |
| video/JPEG | | active |
| video/H261 | | active |
| video/H263 | | active |
| video/H263-1998 | | active |
| video/H263-2000 | | active |
| video/H264 | | active |
| video/MPV | | active |
| video/mp4 | | active |
| video/ogg | | active |
| video/mpeg | | active |
| audio/basic | | active |
| audio/mpeg | | active |
| audio/mpeg3 | | active |
| audio/mpeg4-generic | | active |
| audio/mp4 | | active |
| audio/L20 | | active |
| audio/L24 | | active |
| audio/telephone-event | | active |
| audio/ogg | | active |
| audio/vorbis | | active |
| video/quicktime | | active |
| text/calendar | | active |
| text/directory | | active |
| text/html | | active |
| text/plain | | active |
| text/richtext | | active |
| text/rtf | | active |
| text/rfc822-headers | | active |
| text/sgml | | active |
| text/tab-separated-values | | active |
| text/uri-list | | active |
| text/xml | | active |
| text/xml-external-parsed-entity | | active |
| image/avif | | active |
| image/bmp | | active |
| image/cgm | | active |
| image/gif | | active |
| image/png | | active |
| image/tiff | | active |
| image/jpeg | | active |
| image/jp2 | | active |
| image/svg+xml | | active |
| application/cda+xml | | active |
| application/EDIFACT | | active |
| application/fhir+json | | active |
| application/fhir+xml | | active |
| application/hl7v2+xml | | active |
| application/gzip | | active |
| application/json | | active |
| application/msword | | active |
| application/pdf | | active |
| application/rtf | | active |
| application/dicom | | active |
| application/dicom+json | | active |
| application/dicom+xml | | active |
| application/octet-stream | | active |
| application/ogg | | active |
| application/vnd.oasis.opendocument.base | | active |
| application/vnd.oasis.opendocument.chart | | active |
| application/vnd.oasis.opendocument.chart-template | | active |
| application/vnd.oasis.opendocument.formula | | active |
| application/vnd.oasis.opendocument.formula-template | | active |
| application/vnd.oasis.opendocument.graphics | | active |
| application/vnd.oasis.opendocument.graphics-template | | active |
| application/vnd.oasis.opendocument.image | | active |
| application/vnd.oasis.opendocument.image-template | | active |
| application/vnd.oasis.opendocument.presentation | | active |
| application/vnd.oasis.opendocument.presentation-template | | active |
| application/vnd.oasis.opendocument.spreadsheet | | active |
| application/vnd.oasis.opendocument.spreadsheet-template | | active |
| application/vnd.oasis.opendocument.text | | active |
| application/vnd.oasis.opendocument.text-master | | active |
| application/vnd.oasis.opendocument.text-template | | active |
| application/vnd.oasis.opendocument.text-web | | active |
| application/vnd.ms-word.document.macroEnabled.12 | | active |
| application/vnd.openxmlformats-officedocument.wordprocessingml.document | | active |
| application/vnd.ms-word.template.macroEnabled.12 | | active |
| application/vnd.openxmlformats-officedocument.wordprocessingml.template | | active |
| application/vnd.ms-powerpoint.slideshow.macroEnabled.12 | | active |
| application/vnd.openxmlformats-officedocument.presentationml.slideshow | | active |
| application/vnd.ms-powerpoint.presentation.macroEnabled.12 | | active |
| application/vnd.openxmlformats-officedocument.presentationml.presentation | | active |
| application/vnd.ms-excel.sheet.binary.macroEnabled.12 | | active |
| application/vnd.ms-excel.sheet.macroEnabled.12 | | active |
| application/vnd.openxmlformats-officedocument.spreadsheetml.sheet | | active |
| application/vnd.ms-xpsdocument | | active |
| application/vnd.ms-excel | | active |
| application/vnd.ms-outlook | | active |
| application/vnd.ms-powerpoint | | active |
| application/vnd.rar | | active |
| application/zip | | active |

#### 3.1.5. Compression Algorithms

**Code Set details**

- **Name:** compression algorithms
- **Id:** compression_algorithms
- **External_id:** openehr_compression_algorithms
- **Reference:** [HL7 Compression Algorithms domain](https://www.hl7.org/fhir/v3/CompressionAlgorithm/cs.html)
- **Status:** active

This code set consists of the names of algorithms used to compress data.

**Used in:** `DV_MULTIMEDIA.compression_algorithm`

| Code | Description | Status |
|------|-------------|--------|
| compress | | active |
| deflate | | active |
| gzip | | active |
| zlib | | active |
| other | | active |

#### 3.1.6. Integrity Check Algorithms

**Code Set details**

- **Name:** integrity check algorithms
- **Id:** integrity_check_algorithms
- **External_id:** openehr_integrity_check_algorithms
- **Reference:** [HL7 IntegrityCheckAlgorithm domain](https://www.hl7.org/fhir/v3/IntegrityCheckAlgorithm/cs.html)
- **Status:** active

This code set consists of the names of algorithms used to generate hashes for the purpose of integrity checks on data.

**Used in:** `DV_MULTIMEDIA.integrity_check_algorithm`

| Code | Description | Status |
|------|-------------|--------|
| SHA-1 | | active |
| SHA-224 | | active |
| SHA-256 | | active |
| SHA-384 | | active |
| SHA-512 | | active |
| SHA-512/224 | | active |
| SHA-512/256 | | active |

#### 3.1.7. Normal Statuses

**Code Set details**

- **Name:** normal statuses
- **Id:** normal_statuses
- **External_id:** openehr_normal_statuses
- **Reference:** [HL7 Observation-Interpretation vocabulary](https://www.hl7.org/fhir/valueset-observation-interpretation.html)
- **Status:** active

This code set codifies statuses of quantitative values with respect to a normal range for the measured analyte or phenomenon. Use is generally restricted to laboratory results. It maps to some codes in HL7v2 User-defined table 0078 - Abnormal flags.

**Used in:** `DV_ORDERED.normal_status`

| Code | Description | Status |
|------|-------------|--------|
| HHH | | active |
| HH | | active |
| H | | active |
| N | | active |
| L | | active |
| LL | | active |
| LLL | | active |

### 3.2. Vocabularies

Within the openEHR vocabularies, terms are identified in groups, each with its own identifier. The identifiers of the groups is defined in the Support Information Model, Terminology package. Each set of terms is described below on a per-group basis.

#### 3.2.1. Attestation Reason

**Vocabulary details**

- **Name:** attestation reason
- **Id:** attestation_reason
- **Status:** active
- **Languages:** en, es, ja, pt
- **FHIR Terminology:** [CodeSystem](https://specifications.openehr.org/fhir/codesystem-attestation_reason), [ValueSet](https://specifications.openehr.org/fhir/valueset-attestation_reason)

This vocabulary codifies attestation statuses of Compositions or other elements of the health record.

**External reference:** [HL7 ParticipationSignature domain](https://www.hl7.org/fhir/v3/ParticipationSignature/cs.html)

**Used in:** `ATTESTATION.reason`

| Code | Description | Status |
|------|-------------|--------|
| 240 | signed | active |
| 648 | witnessed | active |

#### 3.2.2. Audit Change Type

**Vocabulary details**

- **Name:** audit change type
- **Id:** audit_change_type
- **Status:** active
- **Languages:** en, es, ja, pt
- **FHIR Terminology:** [CodeSystem](https://specifications.openehr.org/fhir/codesystem-audit_change_type), [ValueSet](https://specifications.openehr.org/fhir/valueset-audit_change_type)

This vocabulary codifies the kinds of changes to data which are recorded in audit trails.

**Used in:** `AUDIT_DETAILS.change_type`

| Code | Description | Status |
|------|-------------|--------|
| 249 | creation | active |
| 250 | amendment | active |
| 251 | modification | active |
| 252 | synthesis | active |
| 523 | deleted | active |
| 666 | attestation | active |
| 816 | restoration | active |
| 817 | format conversion | active |
| 253 | unknown | active |

#### 3.2.3. Composition Category

**Vocabulary details**

- **Name:** composition category
- **Id:** composition_category
- **Status:** active
- **Languages:** en, es, ja, pt
- **FHIR Terminology:** [CodeSystem](https://specifications.openehr.org/fhir/codesystem-composition_category), [ValueSet](https://specifications.openehr.org/fhir/valueset-composition_category)

This vocabulary codifies the values of the `category` attribute in Compositions.

**Used in:** `COMPOSITION.category`

| Code | Description | Status |
|------|-------------|--------|
| 431 | persistent | active |
| 451 | episodic | active |
| 433 | event | active |
| 815 | report | active |

#### 3.2.4. Property

**Vocabulary details**

- **Name:** property
- **Id:** property
- **Status:** active
- **Languages:** en, es, ja, pt
- **FHIR Terminology:** [CodeSystem](https://specifications.openehr.org/fhir/codesystem-property), [ValueSet](https://specifications.openehr.org/fhir/valueset-property)

This vocabulary codifies purposes for physical properties corresponding to formal unit specifications, and allows comparison of Quantities with different units but which measure the same property.

**External reference:** [Regenstrief Institute - Unified Codes for Units of Measure](http://unitsofmeasure.org/ucum.html)

**Used in:** `DV_QUANTITY`

| Code | Description | Status |
|------|-------------|--------|
| 339 | Acceleration | active |
| 342 | Acceleration, angular | active |
| 381 | Amount (Eq) | active |
| 384 | Amount (mole) | active |
| 497 | Angle, plane | active |
| 500 | Angle, solid | active |
| 335 | Area | active |
| 119 | Concentration | active |
| 350 | Density | active |
| 362 | Diffusion coefficient | active |
| 501 | Electric capacitance | active |
| 498 | Electric charge | active |
| 502 | Electric conductance | active |
| 334 | Electric current | active |
| 377 | Electric field strength | active |
| 655 | Electric potential time | active |
| 121 | Energy | active |
| 366 | Energy density | active |
| 508 | Energy dose | active |
| 365 | Energy per area | active |
| 364 | Energy, linear | active |
| 347 | Flow rate, mass | active |
| 352 | Flow rate, mass/force | active |
| 351 | Flow rate, mass/volume | active |
| 126 | Flow rate, volume | active |
| 348 | Flux, mass | active |
| 355 | Force | active |
| 358 | Force per mass | active |
| 357 | Force, body | active |
| 382 | Frequency | active |
| 586 | Glomerular filtration rate | active |
| 373 | Heat transfer coefficient | active |
| 505 | Illuminance | active |
| 379 | Inductance | active |
| 122 | Length | active |
| 499 | Light intensity | active |
| 123 | Loudness | active |
| 504 | Luminous flux | active |
| 378 | Magnetic flux | active |
| 503 | Magnetic flux density | active |
| 124 | Mass | active |
| 385 | Mass (IU) | active |
| 445 | Mass (Units) | active |
| 349 | Mass per area | active |
| 344 | Moment inertia, area | active |
| 345 | Moment inertia, mass | active |
| 340 | Momentum | active |
| 346 | Momentum flow rate | active |
| 343 | Momentum, angular | active |
| 363 | Power | active |
| 369 | Power density | active |
| 368 | Power flux | active |
| 367 | Power, linear | active |
| 125 | Pressure | active |
| 507 | Proportion | active |
| 380 | Qualified real | active |
| 506 | Radioactivity | active |
| 375 | Resistance | active |
| 370 | Specific energy | active |
| 371 | Specific heat, gas constant | active |
| 337 | Specific surface | active |
| 336 | Specific volume | active |
| 354 | Specific weight | active |
| 356 | Surface tension | active |
| 127 | Temperature | active |
| 372 | Thermal conductivity | active |
| 128 | Time | active |
| 359 | Torque | active |
| 338 | Velocity | active |
| 341 | Velocity, angular | active |
| 360 | Viscosity, dynamic | active |
| 361 | Viscosity, kinematic | active |
| 374 | Electric potential | active |
| 129 | Volume | active |
| 130 | Work | active |
| 685 | Refractive power | active |
| 118 | <not set> | active |
| 709 | Time fraction | active |
| 708 | Rate of change, pressure | active |
| 754 | Rate of change, frequency | active |
| 755 | Arbitrary | active |
| 756 | Medication dose rate | active |
| 757 | Spectral power | active |
| 758 | Spectral power density | active |
| 759 | Pace | active |
| 760 | Enzyme activity | active |

#### 3.2.5. Version Lifecycle State

**Vocabulary details**

- **Name:** version lifecycle state
- **Id:** version_lifecycle_state
- **Status:** active
- **Languages:** en, es, ja, pt
- **FHIR Terminology:** [CodeSystem](https://specifications.openehr.org/fhir/codesystem-version_lifecycle_state), [ValueSet](https://specifications.openehr.org/fhir/valueset-version_lifecycle_state)

This vocabulary codifies lifecycle states of Compositions or other elements of the health record.

**Used in:** `ORIGINAL_VERSION.lifecycle_state`, `IMPORTED_VERSION.lifecycle_state`, `VERSIONED_OBJECT.lifecycle_state`

| Code | Description | Status |
|------|-------------|--------|
| 532 | complete | active |
| 553 | incomplete | active |
| 523 | deleted | active |
| 800 | inactive | active |
| 801 | abandoned | active |

#### 3.2.6. Participation Function

**Vocabulary details**

- **Name:** participation function
- **Id:** participation_function
- **Status:** active
- **Languages:** en, es, ja, pt
- **FHIR Terminology:** [CodeSystem](https://specifications.openehr.org/fhir/codesystem-participation_function), [ValueSet](https://specifications.openehr.org/fhir/valueset-participation_function)

This vocabulary codifies functions of participation of parties in an interaction.

**Used in:** `PARTICIPATION.function`

| Code | Description | Status |
|------|-------------|--------|
| 253 | unknown | active |

#### 3.2.7. Null Flavours

**Vocabulary details**

- **Name:** null flavours
- **Id:** null_flavours
- **Status:** active
- **Languages:** en, es, ja, pt
- **FHIR Terminology:** [CodeSystem](https://specifications.openehr.org/fhir/codesystem-null_flavours), [ValueSet](https://specifications.openehr.org/fhir/valueset-null_flavours)

This vocabulary codifies 'flavours of null' for missing data items.

**Used in:** `ELEMENT.null_flavour`

| Code | Description | Status |
|------|-------------|--------|
| 271 | no information | active |
| 253 | unknown | active |
| 272 | masked | active |
| 273 | not applicable | active |

#### 3.2.8. Participation Mode

**Vocabulary details**

- **Name:** participation mode
- **Id:** participation_mode
- **Status:** active
- **Languages:** en, es, ja, pt
- **FHIR Terminology:** [CodeSystem](https://specifications.openehr.org/fhir/codesystem-participation_mode), [ValueSet](https://specifications.openehr.org/fhir/valueset-participation_mode)

This vocabulary codifies modes of participation of parties in an interaction.

**External reference:** [HL7 ParticipationMode domain](https://www.hl7.org/fhir/v3/ParticipationMode/cs.html)

**Used in:** `PARTICIPATION.mode`

| Code | Description | Status |
|------|-------------|--------|
| 193 | not specified | active |
| 216 | face-to-face communication | active |
| 223 | interpreted face-to-face communication | active |
| 217 | signing (face-to-face) | active |
| 195 | live audiovisual; videoconference; videophone | active |
| 198 | videoconferencing | active |
| 197 | videophone | active |
| 218 | signing over video | active |
| 224 | interpreted video communication | active |
| 194 | asynchronous audiovisual; recorded video | active |
| 196 | recorded video | active |
| 202 | live audio-only; telephone; internet phone; teleconference | active |
| 204 | telephone | active |
| 203 | teleconference | active |
| 205 | internet telephone | active |
| 222 | interpreted audio-only | active |
| 199 | asynchronous audio-only; dictated; voice mail | active |
| 200 | dictated | active |
| 201 | voice-mail | active |
| 212 | live text-only; internet chat; SMS chat; interactive written note | active |
| 213 | internet chat | active |
| 214 | SMS chat | active |
| 215 | interactive written note | active |
| 206 | asynchronous text; email; fax; letter; handwritten note; SMS message | active |
| 211 | handwritten note | active |
| 210 | printed/typed letter | active |
| 207 | email | active |
| 208 | facsimile/telefax | active |
| 221 | translated text | active |
| 209 | SMS message | active |
| 219 | physically present | active |
| 220 | physically remote | active |

#### 3.2.9. Instruction States

**Vocabulary details**

- **Name:** instruction states
- **Id:** instruction_states
- **Status:** active
- **Languages:** en, es, ja, pt
- **FHIR Terminology:** [CodeSystem](https://specifications.openehr.org/fhir/codesystem-instruction_states), [ValueSet](https://specifications.openehr.org/fhir/valueset-instruction_states)

This vocabulary codifies the names of the states in the standard Instruction state machine.

**Used in:** `ISM_TRANSITION.current_state`

| Code | Description | Status |
|------|-------------|--------|
| 524 | initial | active |
| 526 | planned | active |
| 527 | postponed | active |
| 528 | cancelled | active |
| 529 | scheduled | active |
| 245 | active | active |
| 530 | suspended | active |
| 531 | aborted | active |
| 532 | completed | active |
| 533 | expired | active |

#### 3.2.10. Instruction Transitions

**Vocabulary details**

- **Name:** instruction transitions
- **Id:** instruction_transitions
- **Status:** active
- **Languages:** en, es, ja, pt
- **FHIR Terminology:** [CodeSystem](https://specifications.openehr.org/fhir/codesystem-instruction_transitions), [ValueSet](https://specifications.openehr.org/fhir/valueset-instruction_transitions)

This vocabulary codifies the names of the transitions in the standard Instruction state machine.

**Used in:** `ISM_TRANSITION.transition`

| Code | Description | Status |
|------|-------------|--------|
| 535 | initiate | active |
| 536 | plan step | active |
| 537 | postpone | active |
| 538 | restore | active |
| 166 | cancel | active |
| 542 | postponed step | active |
| 539 | schedule | active |
| 534 | scheduled step | active |
| 540 | start | active |
| 541 | do | active |
| 543 | active step | active |
| 544 | suspend | active |
| 545 | suspended step | active |
| 546 | resume | active |
| 547 | abort | active |
| 548 | finish | active |
| 549 | time out | active |
| 550 | notify aborted | active |
| 551 | notify completed | active |
| 552 | notify cancelled | active |

#### 3.2.11. Subject Relationship

**Vocabulary details**

- **Name:** subject relationship
- **Id:** subject_relationship
- **Status:** active
- **Languages:** en, es, ja, pt
- **FHIR Terminology:** [CodeSystem](https://specifications.openehr.org/fhir/codesystem-subject_relationship), [ValueSet](https://specifications.openehr.org/fhir/valueset-subject_relationship)

This vocabulary codifies the relationship between the subject of care and some other party mentioned in the health record.

**Used in:** `PARTY_RELATED.relationship`

| Code | Description | Status |
|------|-------------|--------|
| 0 | self | active |
| 3 | foetus | active |
| 10 | mother | active |
| 9 | father | active |
| 6 | donor | active |
| 253 | unknown | active |
| 261 | adopted daughter | active |
| 260 | adopted son | active |
| 259 | adoptive father | active |
| 258 | adoptive mother | active |
| 256 | biological father | active |
| 255 | biological mother | active |
| 23 | brother | active |
| 28 | child | active |
| 265 | cohabitee | active |
| 257 | cousin | active |
| 29 | daughter | active |
| 264 | guardian | active |
| 39 | maternal aunt | active |
| 8 | maternal grandfather | active |
| 7 | maternal grandmother | active |
| 38 | maternal uncle | active |
| 189 | neonate | active |
| 254 | parent | active |
| 22 | partner/spouse | active |
| 41 | paternal aunt | active |
| 36 | paternal grandfather | active |
| 37 | paternal grandmother | active |
| 40 | paternal uncle | active |
| 27 | sibling | active |
| 24 | sister | active |
| 31 | son | active |
| 263 | step father | active |
| 262 | step mother | active |
| 25 | step or half brother | active |
| 26 | step or half sister | active |

#### 3.2.12. Term Mapping Purpose

**Vocabulary details**

- **Name:** term mapping purpose
- **Id:** term_mapping_purpose
- **Status:** active
- **Languages:** en, es, ja, pt
- **FHIR Terminology:** [CodeSystem](https://specifications.openehr.org/fhir/codesystem-term_mapping_purpose), [ValueSet](https://specifications.openehr.org/fhir/valueset-term_mapping_purpose)

This vocabulary codifies purposes for term mappings as used in openEHR coded text data.

**Used in:** `TERM_MAPPING.purpose`

| Code | Description | Status |
|------|-------------|--------|
| 669 | public health | active |
| 670 | reimbursement | active |
| 671 | research study | active |

#### 3.2.13. Event Math Function

**Vocabulary details**

- **Name:** event math function
- **Id:** event_math_function
- **Status:** active
- **Languages:** en, es, ja, pt
- **FHIR Terminology:** [CodeSystem](https://specifications.openehr.org/fhir/codesystem-event_math_function), [ValueSet](https://specifications.openehr.org/fhir/valueset-event_math_function)

This vocabulary codifies mathematical functions applied to non-instantaneous time series events.

**Used in:** `INTERVAL_EVENT.math_function`

| Code | Description | Status |
|------|-------------|--------|
| 145 | minimum | active |
| 144 | maximum | active |
| 267 | mode | active |
| 268 | median | active |
| 146 | mean | active |
| 147 | change | active |
| 148 | total | active |
| 149 | variation | active |
| 521 | decrease | active |
| 522 | increase | active |
| 640 | actual | active |

#### 3.2.14. Setting

**Vocabulary details**

- **Name:** setting
- **Id:** setting
- **Status:** active
- **Languages:** en, es, ja, pt
- **FHIR Terminology:** [CodeSystem](https://specifications.openehr.org/fhir/codesystem-setting), [ValueSet](https://specifications.openehr.org/fhir/valueset-setting)

This vocabulary codifies broad types of settings in which clinical care is delivered. It is not intended as a perfect classification of the real world, but as "a practical coarse-grained categorisation to aid querying."

**Used in:** `EVENT_CONTEXT.setting`

| Code | Description | Status |
|------|-------------|--------|
| 225 | home | active |
| 227 | emergency care | active |
| 228 | primary medical care | active |
| 229 | primary nursing care | active |
| 230 | primary allied health care | active |
| 231 | midwifery care | active |
| 232 | secondary medical care | active |
| 233 | secondary nursing care | active |
| 234 | secondary allied health care | active |
| 235 | complementary health care | active |
| 236 | dental care | active |
| 237 | nursing home care | active |
| 802 | mental healthcare | active |
| 238 | other care | active |

#### 3.2.15. Extract Content Type

**Vocabulary details**

- **Name:** extract content type
- **Id:** extract_content_type
- **Status:** active
- **Languages:** en, es, ja, pt
- **FHIR Terminology:** [CodeSystem](https://specifications.openehr.org/fhir/codesystem-extract_content_type), [ValueSet](https://specifications.openehr.org/fhir/valueset-extract_content_type)

This vocabulary codifies the type of the content required for an Extract specification.

**Used in:** `EXTRACT_SPEC.extract_type`

| Code | Description | Status |
|------|-------------|--------|
| 803 | openEHR EHR | active |
| 804 | openEHR Demographic | active |
| 805 | openEHR synchronisation | active |
| 806 | openEHR generic | active |
| 807 | generic EMR | active |
| 808 | other | active |

#### 3.2.16. Extract Action Type

**Vocabulary details**

- **Name:** extract action type
- **Id:** extract_action_type
- **Status:** active
- **Languages:** en, es, ja, pt
- **FHIR Terminology:** [CodeSystem](https://specifications.openehr.org/fhir/codesystem-extract_action_type), [ValueSet](https://specifications.openehr.org/fhir/valueset-extract_action_type)

This vocabulary codifies the action types of a Request for an Extract specification.

**Used in:** `EXTRACT_ACTION_REQUEST.action`

| Code | Description | Status |
|------|-------------|--------|
| 809 | cancel | active |
| 810 | resend | active |
| 811 | send new | active |

#### 3.2.17. Extract Update Trigger Event Type

**Vocabulary details**

- **Name:** extract update trigger event type
- **Id:** extract_update_trigger_event_type
- **Status:** active
- **Languages:** en, es, ja, pt
- **FHIR Terminology:** [CodeSystem](https://specifications.openehr.org/fhir/codesystem-extract_update_trigger_event_type), [ValueSet](https://specifications.openehr.org/fhir/valueset-extract_update_trigger_event_type)

This vocabulary codifies the event names of an update Extract specification.

**Used in:** `EXTRACT_UPDATE_SPEC.trigger_events`

| Code | Description | Status |
|------|-------------|--------|
| 812 | any change | active |
| 813 | correction | active |
| 814 | update | active |

## 4. Representation

### 4.1. Model

The UML model of the openEHR code sets and vocabularies provides a representation of structured information. This model is not intended as a normative model for internal terminology representation in openEHR services and does not directly correspond to the terminology classes defined in the openEHR Data Types or openEHR Base Types specifications.

The `TERMINOLOGY` type may include both code sets and vocabularies; however, a single instance represents all code sets, while each translation of the vocabularies has its own instance.

#### 4.1.1. Class Definitions

##### 4.1.1.1. TERMINOLOGY Class

**Description:** Container for code sets and/or vocabularies that belong to a given logical terminology.

**Attributes:**

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| name | String | Name of this terminology |
| language | String | Language of this terminology, as ISO:639 2-letter code |
| code_sets | List<CODE_SET> | Code sets in this Terminology |
| vocabularies | List<TERMINOLOGY_GROUP> | Vocabularies of coded terms in this terminology |
| version | String | Version of this instance of the terminology |
| date | Iso8601_date | Date of issue of this version of the terminology |

##### 4.1.1.2. CODE_SET Class

**Description:** A code set.

**Attributes:**

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| name | String | Name of this code set |
| openehr_id | String | Identifier used for code set in openEHR Reference Model. Valid xs:NCName values cannot contain: `:, @, $, %, &, /, +, ,, ;`, whitespace, or parentheses. Cannot begin with a number, dot, or minus character. |
| issuer | String | Name of the issuing organisation |
| codes | List<CODE> | Codes in this code set |
| external_id | String | Optional identifier assumed by openEHR to be the identifier of this code set. Valid xs:NCName values follow same restrictions as openehr_id. |
| status | TERMINOLOGY_STATUS | Status of this code set (default = active) |

##### 4.1.1.3. CODE Class

**Description:** A single code entity in a code set.

**Attributes:**

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| value | String | The code string for this code entity, e.g., "AF" |
| description | String | Optional description of this code, e.g., "AFGHANISTAN". May be used for translations in language-specific versions. |
| status | TERMINOLOGY_STATUS | Status of this code within the code set (default = active) |

##### 4.1.1.4. TERMINOLOGY_GROUP Class

**Description:** A single vocabulary, in a particular language, within a Terminology.

**Attributes:**

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| name | String | Name of this vocabulary |
| concepts | List<TERMINOLOGY_CONCEPT> | List of concepts (i.e., coded terms) in this vocabulary |
| openehr_id | String | Identifier used for terminology group in openEHR Reference Model. Valid xs:NCName values cannot contain: `:, @, $, %, &, /, +, ,, ;`, whitespace, or parentheses. Cannot begin with a number, dot, or minus character. |
| status | TERMINOLOGY_STATUS | Status of this vocabulary (default = active) |

##### 4.1.1.5. TERMINOLOGY_CONCEPT Class

**Description:** A single terminology concept in a vocabulary.

**Attributes:**

| Attribute | Signature | Meaning |
|-----------|-----------|---------|
| id | String | The code of this concept |
| rubric | String | The rubric, i.e., linguistic expression of this concept in the language of this terminology instance |
| status | TERMINOLOGY_STATUS | Status of this concept within the vocabulary (default = active) |

##### 4.1.1.6. TERMINOLOGY_STATUS Enumeration

**Description:** Enumeration of possible lifecycle states of any part of the terminology.

**Values:**

- **trial:** Terminology element is in Trial state
- **active:** Terminology element is in Active state, i.e., published and in use
- **retired:** Terminology element has been Retired, i.e., deprecated

### 4.2. XML Representation

The concrete representation of the openEHR code sets and vocabularies is in XML format, as described by the XML Schema found in the [openEHR `specifications-TERM` repository](https://github.com/openEHR/specifications-TERM/tree/master/computable/XML).

The structure under the `/computable/XML` directory consists of:

- A single file for all code sets (no translations needed - codes are self-describing)
- A single file for each translation of the vocabularies

### 4.3. Content Artefacts

The concrete artefacts based on this model are:

- Single file for all code sets (e.g., openehr_codeset.xml)
- Single file for each translation of the vocabularies (e.g., openehr_terminology.xml for English, Spanish, Japanese, Portuguese)

**Example Code Sets XML Structure:**

```xml
<terminology name="openehr" language="en" version="3.0.0" date="2023-02-07">
	<codeset issuer="ISO" openehr_id="countries" name="countries" 
		external_id="ISO_3166-1">
		<code value="AF" description="AFGHANISTAN"/>
		<code value="AX" description="ÅLAND ISLANDS"/>
		<code value="AL" description="ALBANIA"/>
		...
		<code value="ZW" description="ZIMBABWE"/>
	</codeset>
	...
	<codeset issuer="IANA" openehr_id="character_sets" 
		name="character sets" external_id="IANA_character-sets">
		<code value="ISO-10646-UTF-1"/>
		<code value="ISO_8859-3:1988"/>
		<code value="UTF-8"/>
		...
		<code value="ISO_8859-1:1987"/>
	</codeset>
</terminology>
```

**Example Vocabulary XML Structure (English):**

```xml
<terminology name="openehr" language="en" version="3.0.0" date="2023-02-07">
	<group openehr_id="attestation_reason" name="attestation reason">
		<concept id="240" rubric="signed"/>
		<concept id="648" rubric="witnessed"/>
	</group>
	<group openehr_id="audit_change_type" name="audit change type">
		<concept id="249" rubric="creation"/>
		<concept id="250" rubric="amendment"/>
		<concept id="251" rubric="modification"/>
		<concept id="252" rubric="synthesis"/>
		<concept id="523" rubric="deleted"/>
		<concept id="666" rubric="attestation"/>
		<concept id="253" rubric="unknown"/>
	</group>
	<group openehr_id="composition_category" name="composition category">
		<concept id="431" rubric="persistent"/>
		<concept id="451" rubric="episodic"/>
		<concept id="433" rubric="event"/>
	</group>
	<group openehr_id="property" name="property">
		<concept id="339" rubric="Acceleration"/>
		<concept id="342" rubric="Acceleration, angular"/>
		<concept id="381" rubric="Amount (Eq)"/>
		<concept id="384" rubric="Amount (mole)"/>
		<concept id="497" rubric="Angle, plane"/>
		<concept id="500" rubric="Angle, solid"/>
		...
	</group>
	...
</terminology>
```

An [XML Schema (XSD)](https://github.com/openEHR/specifications-TERM/tree/master/computable/XML/schema) has been defined for these files, for use with software that processes them.

---

**Last updated:** 2023-06-26 20:25:04 UTC
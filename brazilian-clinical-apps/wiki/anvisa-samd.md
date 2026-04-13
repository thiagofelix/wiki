---
title: ANVISA SaMD — Software as Medical Device Framework
type: concept
sources:
  - raw/market-landscape-research.md
created: 2026-04-12
updated: 2026-04-12
---

**ANVISA** is Brazil's health surveillance agency (equivalent to the US FDA). As of 2022, ANVISA has established a comprehensive regulatory framework specifically for **SaMD (Software as Medical Device)** — any software intended for medical purposes that operates independently of hardware. Clinical software vendors must assess whether their products qualify as SaMD and, if so, determine the applicable registration pathway.

**Primary regulation:** RDC 657/2022 (effective July 1, 2022)  
**Classification rules:** RDC 751/2022, Rule 11  
**Enforcement:** ANVISA  

---

## Key Regulatory Instruments

| Resolution | Content | Effective |
|---|---|---|
| **RDC 657/2022** | Core SaMD regulation — defines SaMD, classification, exemptions, registration requirements, labeling, lifecycle, cybersecurity | July 1, 2022 |
| **RDC 751/2022** | General medical device risk classification (Classes I–IV, 22 rules). Rule 11 specifically governs SaMD. Replaces RDC 185/2001 | 2022 |
| **RDC 777/2023** | Updates and complements RDC 751/2022 | 2023 |
| **RDC 848/2024** | Essential safety and performance requirements for medical devices and IVDs | 2024 |
| **RDC 665/2022** | Brazilian GMP (Good Manufacturing Practices) — required for Classes III/IV | 2022 |

Sources: [Elendiabs](https://www.elendilabs.com/en/articles/bra-software-as-a-medical-device), [CGM Law](https://cgmlaw.com.br/en/anvisa-resolution-no-657-2022-standard-for-registration-and-notification-of-software-as-a-medical-device/), [ANVISA.gov.br](https://www.gov.br/anvisa/pt-br/assuntos/noticias-anvisa/2025/anvisa-publica-nova-versao-de-manual-para-regularizacao-de-equipamentos-medicos)

---

## What Is (and Is Not) SaMD

### SaMD Definition

SaMD includes **any software intended for medical purposes** (prevention, diagnosis, treatment, rehabilitation, contraception) that **operates independently of hardware** — including:
- Mobile health apps with diagnostic or therapeutic functions
- SaaS platforms with clinical decision support
- Cloud-hosted diagnostic image analysis tools
- Remote monitoring software with clinical alerting

([RDC 657/2022 English PDF](https://www.gov.br/anvisa/pt-br/assuntos/produtosparasaude/temas-em-destaque/arquivos/2024/rdc-657-2022-en.pdf))

### Explicitly Excluded from SaMD Regulation

1. Software for **well-being only** (no medical purpose)
2. Software in ANVISA's non-regulated list
3. **Software used exclusively for administrative and financial management** in health services — this is the key exemption for pure clinic management platforms
4. Software that processes demographic or epidemiological data **without** clinical/diagnostic/therapeutic purpose
5. Software **embedded in a registered hardware medical device** (regulated as part of the device)

([RDC 657/2022 English PDF](https://www.gov.br/anvisa/pt-br/assuntos/produtosparasaude/temas-em-destaque/arquivos/2024/rdc-657-2022-en.pdf), [CMS Law](https://cms.law/en/int/expert-guides/cms-expert-guide-to-digital-health-apps-and-telemedicine/brazil))

### The Gray Zone for Clinical Software

Most EHR and clinic management platforms sit in a gray zone:
- **Pure scheduling/billing/admin** → exempt
- **Clinical decision support, diagnostic algorithms, vital sign monitoring with alerts** → likely SaMD
- **AI-powered diagnosis or triage** → SaMD, likely Class II–IV

Vendors should conduct a formal intended-purpose analysis. The test is whether the software's **primary intended purpose** is medical.

---

## SaMD Risk Classification (RDC 751/2022, Rule 11)

Risk classification is determined by (a) the severity of the condition addressed and (b) the software's role in the clinical decision.

| Class | Risk Level | Examples | Registration Pathway |
|---|---|---|---|
| **Class I** | Low | Admin-supporting software; wellness monitoring with no clinical decision impact | Notification (simplified) |
| **Class II** | Medium | Software providing information for diagnostic or therapeutic decisions in non-life-threatening situations | Notification (simplified) |
| **Class III** | High | Software monitoring vital physiological parameters where errors could cause immediate patient danger | Full registration |
| **Class IV** | Maximum | Software for decisions where errors cause death or irreversible health deterioration | Full registration + BGMP (Brazilian GMP) |

([Saúde Digital Brasil](https://saudedigitalbrasil.com.br/anvisa-atualiza-regras-para-regularizacao-de-dispositivos-medicos-no-brasil/), [QServe Group](https://qservegroup.com/en/brazil-medical-device-regulations))

---

## In-House SaMD Exemption

Low-risk SaMD (Classes I and II) developed in-house and used exclusively within the **same health service** (including branches) is **exempt from ANVISA registration**, provided:

1. It does not interfere with registered hardware medical devices
2. Validation records are maintained for **≥10 years** after disposal
3. Commercialization or donation without registration is **prohibited** — the exemption ends if the software is sold or licensed

Health services had a **2-year adaptation period** from July 1, 2022 to bring in-house software into compliance.

([RDC 657/2022 English PDF](https://www.gov.br/anvisa/pt-br/assuntos/produtosparasaude/temas-em-destaque/arquivos/2024/rdc-657-2022-en.pdf))

---

## Technical Dossier Requirements (by Class)

| Requirement | Class I | Class II | Class III | Class IV |
|---|---|---|---|---|
| Description and intended purpose | ✓ | ✓ | ✓ | ✓ |
| Risk management documentation | ✓ | ✓ | ✓ | ✓ |
| Conformity declaration | ✓ | ✓ | ✓ | ✓ |
| Software architecture and algorithms | — | ✓ | ✓ | ✓ |
| Cybersecurity plan | — | ✓ | ✓ | ✓ |
| Verification and validation (V&V) | — | ✓ | ✓ | ✓ |
| Usability (IEC 62366) | — | ✓ | ✓ | ✓ |
| Software lifecycle (IEC 62304) | — | ✓ | ✓ | ✓ |
| Clinical evidence (literature or studies) | — | — | ✓ | ✓ |
| BGMP certification | — | — | ✓ | ✓ |

---

## Labeling Requirements for SaMD

- Primarily in **Portuguese**
- Must include:
  - Update procedures
  - Hardware and software requirements
  - Operating principles
  - Interoperability specifications
  - Cybersecurity environment description
- Electronic distribution is acceptable; no physical labeling required for online-only distribution

([Elendiabs](https://www.elendilabs.com/en/articles/bra-software-as-a-medical-device), [Freyr Solutions](https://www.freyrsolutions.com/blog/resolution-for-regulation-of-software-as-medical-device-samd-in-brazil))

---

## Non-Compliance Consequences

- Administrative sanctions
- Fines
- Suspension of sales
- Product seizure
- Possible criminal and civil liability

([CMS Law](https://cms.law/en/int/expert-guides/cms-expert-guide-to-digital-health-apps-and-telemedicine/brazil))

---

## Intersection with Other Regulations

### ANVISA SaMD + CFM 2.454/2026 (AI)
CFM Resolution 2.454/2026 (effective August 10, 2026 — see [[telemedicine-regulation]]) creates a risk tiering framework for AI tools (Low/Medium/High) that implicitly maps onto ANVISA SaMD classes. Software vendors offering AI-powered clinical decision support should align their ANVISA SaMD classification with their CFM 2.454 AI risk tier.

### ANVISA SaMD + LGPD
SaMD processing patient data must comply with [[lgpd-health-data]] obligations — particularly encryption, legal basis documentation, and breach notification — in addition to ANVISA technical dossier requirements.

### ANVISA SaMD + SBIS
[[sbis-certification]] at NGS2 level provides documented security conformity that supports the cybersecurity plan required in SaMD technical dossiers for Classes II–IV.

### ANVISA SaMD + RNDS
Clinical software connecting to [[sus-integration]] (RNDS/FHIR R4) and performing clinical functions must resolve both ANVISA registration and RNDS integration simultaneously — the two are independent but complementary compliance tracks.

---

## Practical Classification Decision Tree

```
Does the software have a medical intended purpose?
├─ NO → Not SaMD; no ANVISA registration required
└─ YES → Is it used exclusively for administrative/financial management?
         ├─ YES → Exempt (exclusion 3)
         └─ NO → SaMD → Apply RDC 751/2022 Rule 11 classification
                  ├─ Class I/II → Notification (simplified); in-house exemption may apply
                  └─ Class III/IV → Full registration + BGMP required
```

---

## Relevance for Clinical Software Vendors in This Wiki

Most pure clinic management platforms ([[iclinic]], [[feegow]], [[amplimed]], [[clinica-nas-nuvens]], [[prontmed]], [[shosp]], [[ninsaude]], [[hidoctor]], [[medicina-direta]], [[prodoctor]], [[consultorio-live]], [[simdoctor]], [[conclinica]]) are likely **exempt** under the administrative/financial management exclusion — but any module offering diagnostic decision support, vital monitoring alerts, or AI-powered clinical recommendations triggers SaMD classification.

Platforms with diagnostic imaging or laboratory functions ([[pixeon]], [[mv-sistemas]]) are more likely to have registered SaMD modules.

---

## See Also

- [[telemedicine-regulation]] — CFM 2.454/2026 AI rules complement ANVISA SaMD classification
- [[lgpd-health-data]] — Data protection obligations apply to SaMD processing patient data
- [[sbis-certification]] — NGS2 security conformity supports SaMD cybersecurity dossier
- [[sus-integration]] — RNDS integration is a separate (but compatible) compliance track
- [[market-overview]] — Market dynamics; regulatory complexity as consolidation driver
- [[mna-landscape]] — ANVISA compliance burden as M&A driver for smaller vendors

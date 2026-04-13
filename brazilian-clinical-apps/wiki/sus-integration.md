---
title: SUS Integration Requirements for Clinical Software
type: concept
sources:
  - raw/market-landscape-research.md
created: 2026-04-12
updated: 2026-04-12
---

SUS (Sistema Único de Saúde) serves approximately **72% of Brazilians — 164 million people** — making it one of the world's largest public health systems. Clinical software operating in Brazil's public health network, or seeking national interoperability, must integrate with a set of federal infrastructure components: **RNDS**, **HL7 FHIR R4**, **CNES**, **ICP-Brasil**, and comply with **Decree 12.560/2025**.

---

## RNDS — Rede Nacional de Dados em Saúde

The RNDS is the **national health data interoperability platform** — the structural backbone of Brazil's digital health system.

**Origin:** Created in 2020 via Ministry of Health Ordinance GM/MS 1.434/2020 as a COVID-19 response measure.  
**Current status:** Formally enshrined as the official national interoperability infrastructure by **Decree 12.560/2025** (July 2025), which mandated interoperability between public and private systems and established citizen data rights ([Telesíntese](https://telesintese.com.br/decreto-regulamenta-rede-nacional-de-dados-em-saude-e-sus-digital/), [LinkedIn/Firely](https://www.linkedin.com/pulse/unlocking-health-data-brazil-rnds-patient-rights-power-ward-weistra-nh2ze)).

([DATASUS](https://datasus.saude.gov.br/modelo-padrao-de-dados-mad/), [Gov.br RNDS](https://www.gov.br/saude/pt-br/composicao/seidigi/rnds))

---

## Technical Standard: HL7 FHIR R4

RNDS uses **HL7 FHIR R4** as the mandatory interoperability standard for all data exchanges ([DATASUS](https://datasus.saude.gov.br/modelo-padrao-de-dados-mad/)).

Brazil launched one of the world's largest national health interoperability platforms using FHIR in 2020 ([Wikipedia — FHIR](https://en.wikipedia.org/wiki/Fast_Healthcare_Interoperability_Resources)).

Historical note: Prior to FHIR, early mandates (2011) required HL7 V2, CDA, and OpenEHR — all of which have been superseded by FHIR R4 for RNDS purposes ([LinkedIn/Firely](https://www.linkedin.com/pulse/unlocking-health-data-brazil-rnds-patient-rights-power-ward-weistra-nh2ze)).

FHIR profiles specific to Brazil are maintained at [Simplifier.net — FHIR Brazil](https://simplifier.net/jurisdictions/br).

---

## Prerequisites for RNDS Integration

Establishments connecting to RNDS must complete four steps ([Voa Health Docs](https://docs.voa.health/integracao/rnds)):

| Step | Requirement |
|---|---|
| **1. CNES registration** | Register in the Cadastro Nacional de Estabelecimentos de Saúde (National Healthcare Facility Registry) |
| **2. ICP-Brasil certificate** | Obtain a valid ICP-Brasil Type A1 digital certificate (e-CPF for individuals, e-CNPJ for organizations) |
| **3. DATASUS credentialing** | Complete credentialing via the DATASUS portal (servicos-datasus.saude.gov.br) |
| **4. Homologation** | Achieve homologation in the RNDS test environment before production go-live |

---

## CNES — Cadastro Nacional de Estabelecimentos de Saúde

CNES is the **national registry of health establishments**. All healthcare facilities — public and private — must be registered in CNES. The CNES registration number is a prerequisite for:
- RNDS integration credentialing
- SUS contract eligibility
- TISS electronic claims (insurers verify CNES registration of providers)

CNES registration data is publicly accessible via the Ministry of Health's data portals.

---

## ICP-Brasil Digital Certificates

**ICP-Brasil** (Infraestrutura de Chaves Públicas Brasileira) is the Brazilian Public Key Infrastructure standard. It underpins digital signatures and authentication across the Brazilian health system.

| Certificate Type | Use Case |
|---|---|
| **Type A1** (software) | RNDS API authentication; automated system-to-system integration |
| **Type A3** (hardware token) | Physician digital signatures on prescriptions and reports |
| **e-CPF** | Individual (physician) digital identity |
| **e-CNPJ** | Organizational digital identity (clinic/hospital) |

ICP-Brasil is required by:
- **RNDS integration** (A1 or A3 certificate for API calls)
- **CFM Resolution 2.314/2022** (NGS2 digital signatures for telemedicine SRES — see [[telemedicine-regulation]])
- **[[sbis-certification]]** NGS2 level
- **TISS electronic claims** with ICP-Brasil signature (see [[tiss]])

---

## Decree 12.560/2025 — RNDS Formalization

Issued July 2025, Decree 12.560/2025 formalized RNDS as the official national health interoperability infrastructure. Key provisions:

- **Mandates interoperability** between public and private health information systems
- **Establishes citizen data rights** — patients can access their own health data via Meu SUS Digital
- **Private sector obligations** — private hospitals and health plans must connect to RNDS
- Creates the legal framework for [[lgpd-health-data]]-compliant national health data sharing

([Telesíntese](https://telesintese.com.br/decreto-regulamenta-rede-nacional-de-dados-em-saude-e-sus-digital/), [LinkedIn/Firely](https://www.linkedin.com/pulse/unlocking-health-data-brazil-rnds-patient-rights-power-ward-weistra-nh2ze))

---

## What RNDS Currently Exchanges

Current RNDS FHIR-based data models ([Simplifier.net — FHIR Brazil](https://simplifier.net/jurisdictions/br)):

| Data Type | Status |
|---|---|
| Immunization records | Active |
| COVID-19 test results | Active |
| Hospital discharge summaries | Active |
| Medication dispensing records | Active |
| Clinical care records | In development |
| Prescription drug records | In development |

---

## Patient-Facing Access

- **Meu SUS Digital** app — citizens view their health data
- **SUS Digital Profissional** — health professionals access patient records

([Gov.br RNDS](https://www.gov.br/saude/pt-br/composicao/seidigi/rnds))

---

## SUS Digital Programs Driving Software Demand

| Program | Scope | Investment |
|---|---|---|
| **APS Digital** | IT equipment and software to basic care units; 3,613 municipalities (65% of Brazil) | — |
| **UBS Digital** | Telemedicine in remote areas (cardiology, dermatology, endocrinology, geriatrics) | USD 3M |
| **SUS Digitalization (2023)** | Broad digital transformation across SUS | USD 200M |
| **North/Northeast Informatics (2024)** | Infrastructure for underserved regions | USD 84M |

([ITA / Trade.gov](https://www.trade.gov/country-commercial-guides/brazil-healthcare))

---

## Key Challenge: Digital Divide

Nearly **40% of SUS primary care units lack stable broadband**. Many facilities still use paper records or WhatsApp. Brazil's National Digital Health Strategy identifies this as a "new social determinant of health" ([Columbia Emerging Markets Review](https://www.columbiaemergingmarketsreview.com/p/public-health-meets-private-capital)).

This creates a two-speed adoption challenge: well-funded private hospitals adopt RNDS quickly, while primary care SUS units face infrastructure barriers.

---

## Regulatory Drivers for Upgrade Pressure

The combination of RNDS integration requirements, [[tiss]] compliance, and [[anvisa-samd]] registration creates substantial pressure on smaller clinical software vendors to upgrade or consolidate:

- **RNDS integration requirement** pressures legacy systems to adopt FHIR R4 APIs
- **TISS compliance** favors vendors with dedicated compliance teams
- **ANVISA SaMD registration** adds regulatory burden smaller players struggle to bear
- **AI regulation** (CFM 2.454/2026 — see [[telemedicine-regulation]]) requires institutional AI governance

---

## Summary: SUS/RNDS Integration Checklist

| Requirement | Action |
|---|---|
| CNES registration | Register facility in the national health establishment registry |
| ICP-Brasil certificate | Obtain Type A1 (system) and/or A3 (physician) certificates |
| FHIR R4 implementation | Build HL7 FHIR R4 APIs for applicable data models |
| DATASUS credentialing | Complete portal registration and test environment homologation |
| Data models | Implement active RNDS profiles (immunizations, discharge summaries, medication dispensing) |
| Decree 12.560/2025 | Assess private-sector obligations under new interoperability mandate |

---

## See Also

- [[tiss]] — ICP-Brasil certificates also required for TISS electronic claims
- [[telemedicine-regulation]] — CFM 2.314/2022 requires ICP-Brasil NGS2 for SRES
- [[sbis-certification]] — NGS2 certification requires ICP-Brasil integration
- [[lgpd-health-data]] — Decree 12.560/2025 citizen rights intersect with LGPD
- [[anvisa-samd]] — SaMD classification relevant to RNDS-connected clinical software
- [[market-overview]] — SUS market size and investment figures

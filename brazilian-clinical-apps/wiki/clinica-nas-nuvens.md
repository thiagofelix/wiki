---
title: Clínica nas Nuvens / Bionexo
type: entity
sources:
  - raw/major-platforms-research.md
created: 2026-04-12
updated: 2026-04-12
---

Clínica nas Nuvens ("Clinic in the Clouds") is a cloud-native clinic-management platform founded in 2015 in Xanxerê, Santa Catarina, by professors and technology professionals affiliated with Unoesc (Universidade do Oeste de Santa Catarina). The platform grew at approximately 70% annually before being acquired in November 2021 by **Bionexo** — the largest healthtech in Latin America — for R$ 28.5 million. Bionexo's first acquisition after a landmark R$ 440 million investment from Bain Capital Tech Opportunities, the deal positioned Clínica nas Nuvens as Bionexo's clinical-management SaaS for medium and large clinics. With 200+ features, 35,000+ daily users, and R$ 1 billion+ in annual transactions processed, it is one of the most feature-rich clinic management platforms in Brazil. It competes primarily with [[doctoralia]] (via Feegow) and [[iclinic]] in the clinic-management space, while serving a larger-clinic segment than solo-practice tools like [[shosp]]. See [[market-overview]] for positioning.

## Key Facts

| Attribute | Detail |
|-----------|--------|
| **Founded** | 2015 |
| **Original HQ** | Xanxerê, Santa Catarina, Brazil |
| **Current Parent / Owner** | Bionexo (largest healthtech in Latin America) |
| **Website** | [clinicanasnuvens.com.br](https://clinicanasnuvens.com.br) |
| **Employees** | Not publicly disclosed |
| **Platform Scale** | 35,000+ daily professionals; 7M+ patient records; R$ 1B+ annual transactions; 10M+ appointments |

## Founders

- **André Luiz Forchesatto** — CEO and Founder; former professor at Unoesc; remained as CEO post-acquisition. ([Unoesc article](https://www.unoesc.edu.br/blog/venda-milionaria-de-startup-de-ex-professores-da-unoesc-incentiva-a-formacao-em-areas-de-tecnologia/), [SC Inova](https://scinova.com.br/startup-clinica-nas-nuvens-e-vendida-para-a-bionexo/))
- Additional co-founders (also former Unoesc professors) — names not fully disclosed in public sources

## Funding & Ownership

| Event | Date | Amount | Detail |
|-------|------|--------|--------|
| Acquisition by Bionexo | November 2021 | R$ 28.5 million | 100% acquisition; Bionexo's first M&A after Bain Capital investment |

**Parent company context:**
- Bionexo raised **R$ 440 million** from **Bain Capital Tech Opportunities** in 2021
- Bionexo was the first Brazilian healthtech valued at over R$ 1 billion
- Bionexo's core business prior to acquisition was healthcare procurement and supply-chain management; Clínica nas Nuvens extends its reach into clinical SaaS (EHR, scheduling, telemedicine)

Sources: [Medicina S/A](https://medicinasa.com.br/bionexo-aquisicao/), [Clínica nas Nuvens blog](https://clinicanasnuvens.com.br/blog/clinica-nas-nuvens-bionexo-a-parceria-que-vai-aumentar-sua-imunidade-contra-problemas-de-gestao/)

## Key Features

The platform offers 200+ resources for full clinic management:

| Category | Features |
|----------|----------|
| **Prontuário Eletrônico** | Fully customizable anamnesis and clinical evolutions; exam and image storage; file attachments; AI-assisted transcription of consultations (under 2 minutes); [[lgpd-health-data]]-compliant |
| **Agendamento Online** | Real-time availability, multi-channel booking, automatic WhatsApp/SMS confirmations and reminders; reported reduction of no-shows by up to 50% |
| **Telemedicina** | Integrated teleconsulta module with digital prescription and electronic signature |
| **Gestão Financeira** | Revenue control, boleto emission, cash-flow tracking, procedure packages, budgets, automatic bank reconciliation, medical repasse |
| **Faturamento de Convênios** | Health-insurance billing management (convênio billing) |
| **Controle de Estoque** | Lot management, consumption monitoring, low-stock alerts, barcode reader, replacement reports |
| **Relatórios Inteligentes** | Performance and management dashboards |
| **Múltiplas Unidades** | Multi-branch integration for clinic networks |
| **Central de Agendamentos** | Centralized scheduling hub |
| **Padronização de Rotinas** | Workflow standardization and process automation |

## Target Market

**Medium and large clinics, multi-specialty clinics, popular clinics (clínicas populares), franchise medical networks, and clinic schools (clínicas-escola).** Serves 30+ specialties including medical, aesthetic, psychology, dentistry, cardiology, dermatology, and pediatrics.

The platform explicitly states it is **not aimed at solo practitioners** — its FAQ notes it is designed for medium and large clinics. ([Clínica nas Nuvens FAQ](https://clinicanasnuvens.com.br/blog/5-perguntas-e-respostas-para-voce-conhecer-melhor-o-clinica-nas-nuvens/)) This differentiates it from [[iclinic]] and [[shosp]], which serve the individual-practitioner segment. The franchise and multi-unit support puts it closer to [[doctoralia]]'s clinic product (via Feegow), but without the patient marketplace component.

## Pricing

SaaS subscription with monthly plans. Secretaries and admin users are unlimited on all plans.

| Plan | Monthly Price (BRL) | Notes |
|------|---------------------|-------|
| **Essencial** | From R$ 499 | Core features; unlimited secretaries/admins |
| **Enterprise** | Higher (undisclosed) | Advanced features; unlimited secretaries/admins |

Source: [Clínica nas Nuvens FAQ blog](https://clinicanasnuvens.com.br/blog/5-perguntas-e-respostas-para-voce-conhecer-melhor-o-clinica-nas-nuvens/)

The R$ 499 starting price is notably higher than [[iclinic]] (from R$ 99/professional) or [[shosp]] (from R$ 0), reflecting the platform's larger-clinic focus and feature breadth.

## Integrations & Compliance

| Integration / Standard | Status |
|------------------------|--------|
| [[tiss]] billing | ✅ — Convênio billing listed as core feature (explicit TISS branding not confirmed in FAQ, but health-insurance billing is included) |
| Telemedicine | ✅ — Native integrated module |
| [[telemedicine-regulation]] | ✅ — Teleconsulta with digital prescription |
| [[lgpd-health-data]] | ✅ — Explicitly stated as LGPD-compliant |
| Digital signature | ✅ — Electronic signature via ArqSign integration |
| RD Station | ✅ — Marketing automation integration |
| PipeDrive | ✅ — CRM / contact management integration |
| ArqSign | ✅ — Electronic signature |
| Open API | ✅ — Available for custom integrations |
| WhatsApp / SMS | ✅ — Automated appointment confirmations and reminders |
| AI transcription | ✅ — AI-assisted clinical note transcription (< 2 minutes) |

## Tech Stack

Cloud-native SaaS — built from the ground up as a web-first platform (not a port of legacy desktop software), consistent with the brand name. Specific infrastructure (cloud provider, database) not publicly disclosed. AI layer for consultation transcription introduced as a key differentiator.

## Notable News / Timeline

| Year | Event |
|------|-------|
| 2015 | Founded in Xanxerê, Santa Catarina by former Unoesc professors |
| 2015–2021 | Grew at ~70% annually |
| **November 2021** | Acquired 100% by Bionexo for R$ 28.5 million — Bionexo's first acquisition after the Bain Capital R$ 440M investment ([Medicina S/A](https://medicinasa.com.br/bionexo-aquisicao/)) |
| Post-2021 | Integrated into Bionexo's strategy to serve the full Latin American health ecosystem — extending from procurement/supply-chain into clinical management |
| Ongoing | Present in management of major franchise dental and medical networks in Brazil |

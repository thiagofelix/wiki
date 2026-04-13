---
title: Câmbio — Câmbio para Pagamentos de Importação
type: conceito
created: 2026-04-12
updated: 2026-04-12
sources:
  - raw/regulatory.md
  - raw/providers.md
tags:
  - pagamentos
  - câmbio
  - regulatório
---

# Câmbio — Câmbio para Pagamentos de Importação

## Lei Governante

**Nova Lei Cambial (Lei 14.286/2021)** — vigente desde 31 de dezembro de 2022. Modernizou a estrutura de câmbio do Brasil, substituindo 40+ instrumentos dos anos 1930. Implementada via Resoluções BCB 277–282.

## Regras-Chave

### Prazo de Pagamento
- Até **360 dias antes** do embarque esperado (antecipação)
- Padrão: dentro de 360 dias do desembaraço aduaneiro
- Importações financiadas >360 dias, ≥ US$500K → Registro do Banco Central obrigatório
- Importações financiadas >180 dias, ≥ US$500K → Reporte de informação BCB

### Operações de Câmbio
- Nenhum contrato formato-fixo obrigatório (eliminado por Lei 14.286/2021)
- **≤ US$50.000**: Dados de liquidação reportados ao BCB até o 5º do mês seguinte
- **> US$50.000**: Reporte no mesmo dia
- Enquadramento cambial (classificação câmbio) é agora **responsabilidade do importador**

### Flexibilidade de Moeda
- Pagamentos em **qualquer moeda** (não apenas moeda DI)
- Pode pagar em **BRL** para conta não-residente no Brasil
- Cartões de crédito internacionais usáveis para importações até US$50.000

### Liquidação em Moeda Local (Março 2023)
Brasil e China concordaram em **eliminar o dólar americano como intermediário**. Liquidação direta BRL↔CNY operacional. Em Q1 2025, **41% do comércio Brasil-China foi liquidado em yuan** — economiza 1–5% em custos financeiros.

Um **swap de moeda de R$157B (US$27,7B)** foi assinado em maio de 2025 (prazo de 5 anos).

## Métodos de Pagamento

| Método | Provedor | Custo | Melhor Para |
|--------|----------|------|----------|
| TT Wire (USD) | Qualquer banco comercial | Spread de 1,5–3% + taxa fixa | B2B padrão |
| TT Wire (Yuan) | BB, Itaú, Santander | Economia de 1–5% vs. USD | Pagamentos regulares China |
| [XTransfer](xtransfer.md) + Ouribank | XTransfer | Menor que banco | Simplicidade baseada em PIX |
| [Wise](wise.md) Business | Wise | ~0,5–1,5% | PMEs, primeiro-tempo importadores |
| CIPS | Via bancos | Similar ao SWIFT | Institucional grande |

## Stablecoins & Cripto (Novembro 2025)

Resoluções BCB 519, 520, 521 trouxeram stablecoins e transferências de ativos virtuais dentro do perímetro regulatório do BCB. Mesmas regras AML/câmbio de transferências bancárias.

## Retenção de Documentos

**10 anos** para todas as transações de câmbio.

## Páginas Relacionadas

- [xtransfer.md](xtransfer.md) — Plataforma de pagamento transfronteiriço
- [kyc-aml.md](kyc-aml.md) — Requisitos AML
- [cascata-tributária.md](cascata-tributária.md) — Impostos de importação
- [acordos-bilaterais.md](acordos-bilaterais.md) — Acordo de liquidação em yuan

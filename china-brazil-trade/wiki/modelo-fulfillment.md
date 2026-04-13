---
title: Estratégia de Fulfillment em Marketplace
type: análise
created: 2026-04-12
updated: 2026-04-12
sources:
  - raw/providers.md
tags:
  - fulfillment
  - strategy
  - marketplace
---

# Estratégia de Fulfillment em Marketplace

## O Modelo Central

```
Fábrica China → Armazém de consolidação (Shenzhen/Yiwu) → Frete FCL oceânico →
Porto de Santos → Armazém aduaneiro (suspensão fiscal) → Nacionalizar sob demanda →
Dividir estoque entre: ML Full DC + Amazon FBA DC + Shopee DC →
Cada marketplace lida com entrega de última milha para consumidores
```

## Benefícios

- Sem necessidade de rede de entrega de última milha própria
- ML/Amazon/Shopee absorvem devoluções e atendimento ao cliente
- Full badge (ML), Prime (Amazon) = **prêmio de conversão de 2–3×**
- DCs de marketplace geralmente melhor localizados que armazéns independentes
- Integrações ERP para visibilidade de inventário multi-canal

## Resumo de Requisitos de Marketplace

| Marketplace | Conta | Requisitos-Chave | Comissão |
|-------------|---------|-----------------|------------|
| [Mercado Livre](mercado-livre.md) | Grátis; Full por convite | CPF/CNPJ; 15–30 vendas/mês para Full | 10–16% |
| [Amazon](amazon-fba-brasil.md) | Profissional (pago) | CNPJ + SEFAZ + IE em estados apoiados | 8%+ |
| [Shopee](shopee.md) | Grátis | CPF/CNPJ; conta bancária | 12–18% |

## Benefícios do Armazém Aduaneiro

| Tipo | Propósito | Benefício-Chave |
|------|---------|-------------|
| Entreposto Aduaneiro | Armazenar sob suspensão fiscal | Suspender todos os impostos até 1 ano |
| Porto Seco (EADI) | Desembaraço aduaneiro interior | 31 registrados; evitar congestionamento de portos |
| CLIA | Logística de contêineres | Aduanas de zona secundária |

## Modelo de Receita para Facilitador de Comércio

- Margem de markup em produtos (preço de importação + impostos + margem de fulfillment)
- Taxa de serviço de fulfillment para marcas clientes usando CNPJ do facilitador
- Descontos de volume de transportadoras (negociado em volume combinado)
- Taxas de consultoria/conformidade para RADAR, INMETRO, ANVISA

## Stack Tecnológico Recomendado

| Camada | Ferramenta |
|-------|------|
| Inteligência de importação | Logcomex |
| Rastreamento de envios | API TrackingMore |
| ERP | TOTVS / Omie |
| Hub de marketplace | Bling, Anymarket ou VTEX |

## Páginas Relacionadas

- [mercado-livre.md](mercado-livre.md) — Mercado Envios Full
- [amazon-fba-brasil.md](amazon-fba-brasil.md) — Amazon FBA
- [shopee.md](shopee.md) — Fulfillment Shopee
- [rotas-comerciais.md](rotas-comerciais.md) — Corredores de envio
- [cascata-tributária.md](cascata-tributária.md) — Estrutura de impostos

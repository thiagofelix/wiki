---
title: Modelo Operacional Recomendado para Facilitador de Comércio
type: análise
created: 2026-04-12
updated: 2026-04-12
sources:
  - raw/providers.md
  - raw/competitors.md
  - raw/regulatory.md
tags:
  - strategy
  - operating-model
  - synthesis
---

# Modelo Operacional Recomendado

## Stack de Provedores

### Sourcing (lado China)
- **1688 / Alibaba** — sourcing de produtos
- Agente de compras Yiwu ou parceiro de consolidação Shenzhen
- **QIMA / SGS** — [inspeção pré-envio](inspecao-qualidade.md) (US$250–350/envio)
- Despachante de frete com experiência Brasil (BL Shipping, CFC, YQN)

### Envio
- **COSCO / MSC / CMA CGM** — frete oceânico FCL/LCL (US$1.500–3.000/contêiner)
- **DHL / FedEx** — frete aéreo (US$6–8.50/kg) para mercadorias urgentes
- [XTransfer](xtransfer.md) + liquidação em moeda local (yuan)

### Entrada no Brasil
- Despachante aduaneiro com experiência em importação da China
- [RADAR](radar-siscomex.md): Limitada (US$150K/sem) → Ilimitada conforme o volume cresce
- Armazém aduaneiro em Santos ou EADI-SP para staging de inventário
- Seguro de carga: apólice aberta, 0,5–0,8% do CIF

### Fulfillment
- [Mercado Envios Full](mercado-livre.md) (primário — 75% de preferência do comprador)
- [Amazon FBA](amazon-fba-brasil.md) (secundário — badge Prime)
- [Shopee SLS](shopee.md) (canal de crescimento — sensível a preço)
- Backup 3PL: Total Express para canais não-marketplace

### Tecnologia
- **Logcomex** — inteligência de importação, preços competitivos
- **API TrackingMore** — visibilidade de envios para clientes
- **TOTVS / Omie** — ERP financeiro
- **Bling / Anymarket / VTEX** — integrações de marketplace

### Pagamentos
- [XTransfer + Ouribank](xtransfer.md) — PIX → CNY
- Yuan direto via Banco do Brasil ou Itaú (>US$50K)
- Itaú BBA / Santander — trade finance, L/C

## Benchmarks de Custo-Chave

| Item de Custo | Faixa |
|-----------|-------|
| Frete oceânico FCL 40HQ (China→Santos) | US$1.500–3.000 |
| Frete oceânico LCL | US$180–220/CBM |
| Frete aéreo | US$6.00–8.50/kg |
| AFRMM | 25% do frete oceânico |
| Carga tributária total de importação | 40–70% do CIF |
| Despachante aduaneiro | US$100–300/envio |
| Inspeção pré-envio | US$250–450/dia |
| Seguro de carga | 0,5–2% da carga |
| Comissão ML | 10–16% |
| Comissão Amazon | 8%+ |

## Observações Estratégicas

1. **[Remessa Conforme](remessa-conforme.md)** é a alavanca regulatória-chave para e-commerce
2. **Logística é o fossado-chave** — Cainiao (40→4 dias de entrega) e Shopee (19 DCs) são as maiores vantagens
3. **Sourcing B2B é fragmentado** — nenhum player tech dominante; oportunidade para um "Alibaba.com para Brasil"
4. **Localização é a resposta aos tarifas** — 75% de produção local da Shein mostra a tendência
5. **[Mercado Livre](mercado-livre.md) entrando na cadeia de suprimentos China** é um divisor de águas
6. **Portos SC** proporcionam otimização fiscal via TTD (embora diminuindo com [reforma tributária](reforma-tributaria.md))

## Páginas Relacionadas

- [modelo-fulfillment.md](modelo-fulfillment.md) — Estratégia de DC de marketplace
- [comparacao-agentes-sourcing.md](comparacao-agentes-sourcing.md) — Paisagem competitiva
- [cascata-tributária.md](cascata-tributária.md) — Estrutura de impostos
- [armadilhas-conformidade.md](armadilhas-conformidade.md) — Riscos regulatórios

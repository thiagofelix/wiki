---
title: RADAR / SISCOMEX Habilitação
type: conceito
created: 2026-04-12
updated: 2026-04-12
sources:
  - raw/regulatory.md
  - raw/providers.md
tags:
  - regulatória
  - conformidade
  - siscomex
---

# RADAR / SISCOMEX Habilitação

## O que é RADAR?

RADAR (Registro e Rastreamento da Atuação dos Intervenientes Aduaneiros) é a autorização da Receita Federal que permite uma pessoa jurídica ou física operar no SISCOMEX. **Sem RADAR, uma empresa não pode registrar declarações de importação**, independentemente de CNPJ ou atividade comercial.

## O que é SISCOMEX?

SISCOMEX (Sistema Integrado de Comércio Exterior) é a plataforma eletrônica unificada do Brasil para todas as operações importação/exportação, estabelecida por Decreto 660/1992. Administrada por:
- **Receita Federal (RFB)** — aduanas, impostos, controle fiscal
- **SECEX/MDIC** — política comercial, licenciamento
- **Banco Central (BACEN)** — aspectos financeiros/forex

## Modalidades RADAR

| Modalidade | Limite de Importação (por semestre) | Exportação | Perfil |
|----------|---------------------------|--------|---------|
| **Expressa** | Até USD 50.000 | Ilimitada | Empresas públicas, SOEs, MEIs; aprovação online automática |
| **Limitada I** | Até USD 50.000 | Ilimitada | Empresas pequenas/novas |
| **Limitada II** | Até USD 150.000 | Ilimitada | Empresas médias |
| **Ilimitada** | Ilimitada | Ilimitada | Capacidade financeira comprovada |
| **Pessoa Física** | Limitado à declaração de IR | Ilimitada | Pessoas físicas |

Quando o limite do semestre é atingido, o sistema bloqueia registros posteriores até que uma **Revisão de Estimativa** (upgrade de limite) seja processada.

## Processo de Habilitação

**Expressa:** Online via Portal SISCOMEX; deferimento automático.

**Limitada/Ilimitada:**
1. Juntar documentação (contrato social, demonstrações financeiras, certificados de conformidade tributária, extratos bancários)
2. DTE (Domicílio Tributário Eletrônico) obrigatório
3. Formalizar solicitação online (Portal SISCOMEX)
4. Agendar atendimento Receita Federal
5. Apresentar documentos; receber protocolo
6. Aprovação: **até 10 dias úteis** se documentação completa

## RADAR para Intermediários de Importação

Em **importação por conta e ordem**, **tanto o importador (trading) QUANTO o adquirente (cliente)** devem ser RADAR-habilitados. O RADAR do cliente deve ser especificamente configurado para conta e ordem. Esta é uma **lacuna comum de conformidade**.

## Funções-Chave SISCOMEX

| Função | Descrição |
|----------|-------------|
| DI / DUIMP | Declaração de importação (DI sendo faseado → DUIMP) |
| LI | Licença de importação para produtos controlados |
| LPCO | Licenças, permissões, certificados (novo módulo Portal Único) |
| Parametrização de risco | Canais inspeção verde/amarelo/vermelho/cinza |
| Anuentes | Integração com ANVISA, MAPA, IBAMA, Exército |

## Transição para DUIMP / Portal Único

O sistema DI legado está sendo substituído por **DUIMP (Declaração Única de Importação)** no Portal Único de Comércio Exterior. Meta: 100% migração até dezembro 2025.

Mudanças-chave:
- **Módulo Catálogo de Produtos**: Pré-registrar todos os produtos com atributos detalhados antes de importar
- **"Canal Único" janela única**: Todas as agências parametrizam canais através de um sistema
- **Integração LPCO**: Licenças de ANVISA/MAPA/Exército gerenciadas no mesmo portal

## Páginas Relacionadas

- [receita-federal.md](receita-federal.md) — Receita Federal do Brasil
- [cascata-tributária.md](cascata-tributária.md) — Estrutura impostos de importação
- [comparacao-modalidades-importacao.md](comparacao-modalidades-importacao.md) — Conta e ordem vs. encomenda
- [armadilhas-conformidade.md](armadilhas-conformidade.md) — Falhas comuns e penalidades

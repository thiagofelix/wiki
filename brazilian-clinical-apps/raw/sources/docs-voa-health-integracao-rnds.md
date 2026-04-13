---
source_url: https://docs.voa.health/integracao/rnds
title: "RNDS | Voa Docs"
type: web-page
fetched: 2026-04-12
---

# RNDS | Voa Docs

Source: https://docs.voa.health/integracao/rnds

---

- RNDS | Voa DocsVoa Docs⌘CtrlkVoa DocsSeja bem-vindo(a)! 👋
- InícioPrimeiros passos
- Escolha sua integração
- IntegraçãoPlugin
- iFrame
- Extensão do Navegador
- Webhooks
- RNDSComo funciona
- Ativação
- Endpoints
- API ReferenceIntrodução
- Autenticação
- Endpoints
- Chaves de API do Usuário
- ApêndiceTestes de CargaFornecido por GitBookNesta páginaCopiar
## RNDS

## Visão Geral

A Voa possui integração nativa com a RNDS (Rede Nacional de Dados em Saúde), a plataforma nacional de interoperabilidade em saúde do Ministério da Saúde do Brasil. Através dessa integração, os dados clínicos gerados durante as consultas são automaticamente formatados no padrão FHIR R4 e enviados ao barramento nacional, contribuindo com o histórico clínico unificado do cidadão no Conecte SUS.

## O que é possível fazer

- 
Envio automático de registros clínicos — Consultas finalizadas na Voa geram documentos no padrão FHIR e são enviados à RNDS

- 
Consulta de dados do paciente — Acesse informações demográficas e clínicas do paciente diretamente do barramento nacional

- 
Envio de prescrições e exames — Prescrições médicas e solicitações de exames são formatadas e transmitidas automaticamente

- 
Rastreabilidade completa — Cada envio é registrado com identificador único, permitindo consulta, substituição ou exclusão do registro na RNDS

## Tipos de documentos suportados
TipoDescrição
RAC

Registro de Atendimento Clínico — gerado automaticamente ao finalizar uma consulta

RPM

Registro de Prescrição de Medicamento — enviado quando há prescrições na consulta

REL

Resultado de Exame Laboratorial — para integrações com laboratórios

RIRA

Registro de Informações de Regulação Assistencial — para encaminhamentos

## Pré-requisitos

Para ativar a integração RNDS, o estabelecimento de saúde precisa:

- 
Estar cadastrado no CNES (Cadastro Nacional de Estabelecimentos de Saúde)

- 
Possuir certificado digital ICP-Brasil tipo A1 (e-CPF ou e-CNPJ)

- 
Ter completado o credenciamento no DATASUS via Portal de Serviços

- 
Ter sido homologado no ambiente de testes da RNDS

A equipe Voa auxilia no processo de credenciamento e homologação. Entre em contato com [email&#160;protected] para iniciar.

## Suporte

Para questões técnicas ou suporte, entre em contato com nossa equipe de integração em [email&#160;protected].
AnteriorTestes e segurançaPróximoComo funciona
Atualizado há 1 mês

Isto foi útil?

- Visão Geral
- O que é possível fazer
- Tipos de documentos suportados
- Pré-requisitos
- Suporte
Isto foi útil?

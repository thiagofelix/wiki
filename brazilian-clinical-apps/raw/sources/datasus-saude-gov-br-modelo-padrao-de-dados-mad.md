---
source_url: https://datasus.saude.gov.br/modelo-padrao-de-dados-mad/
title: "Modelo padrão de dados MAD &#8211; DATASUS"
type: web-page
fetched: 2026-04-12
---

# Modelo padrão de dados MAD &#8211; DATASUS

Source: https://datasus.saude.gov.br/modelo-padrao-de-dados-mad/

---

- 

	Modelo padrão de dados MAD &#8211; DATASUS

    Ir para o conteúdo

Ministério da Saúde

## DATASUS

						Alto contraste

- 
						VLibras

				Buscar no portal

## DATASUS

				Buscar no portal

## DATASUS

- O DATASUS

- Quem-é-Quem

- Estrutura

## Sistemas

- Sistemas

- Material de Apoio

## Interoperabilidade

- Interoperabilidade

## Metodologias

- Metodologias

## Contato

- Fale conosco

- Perguntas frequentes

## Aplicativos

- Aplicativos MS

## Redes Sociais

- 
		    Twitter

- 
		    Youtube

- 
		    Facebook

- 
		    Flickr

- 
		    Instagram

- 
		    Twitter

- 
		    Youtube

- 
		    Facebook

- 
		    Flickr

- 
		    Instagram

## Modelo padrão de dados

Introdução

A Rede Nacional de Dados em Saúde (RNDS) é a plataforma nacional de interoperabilidade (troca de dados), instituída pela Portaria GM/MS nº 1.434, de 28 de maio de 2020 como medida para enfrentamento da pandemia de COVID-19. A RNDS, além de ser um projeto estruturante, é um programa do Governo Federal voltado para a transformação digital da saúde no Brasil e tem o objetivo de promover a troca de informações entre os pontos da Rede de Atenção à Saúde, e assim promover a transição e continuidade do cuidado nos setores público e privado.

Na perspectiva de um estabelecimento de saúde, a RNDS desempenha um papel central, possibilitando que um estabelecimento de saúde compartilhe informações acessíveis e qualificadas para o repositório centralizado, de onde outros estabelecimentos podem acessá-las uma vez que estejam integrados, promovendo a continuidade do cuidado do cidadão.

Quando um estabelecimento de saúde se integra à RNDS, ele pode contribuir com as informações em um contexto centrado no cidadão assistido, bem como, pode consumir informações geradas pelos demais estabelecimentos, em um contexto de atendimento ao cidadão – as informações disponíveis na RNDS podem ser acessadas apenas em um contexto de atendimento, não estão disponíveis para uso indiscriminado. É importante ressaltar que a segurança da informação é garantida por meio de métodos criptográficos, a fim de salvaguardar que os dados individuais dos pacientes permaneçam protegidos contra acessos não autorizado entre sistemas.

Contexto de fluxo de dados na RNDS

A RNDS como plataforma de interoperabilidade necessita de um padrão para permitir a troca de informações, motivo pelo qual foi estabelecido, a nível nacional, o uso obrigatório do padrão de interoperabilidade em saúde para trocas com a RNDS, o HL7 FHIR12. O padrão FHIR (Fast Healthcare Interoperability Resources) é um padrão desenvolvido pela organização Health Level Seven International (HL7) para a troca de informações eletrônicas em saúde, credenciada pela ANSI-standards (American National Standards) para a definição de frameworks e padrões para a troca, integração, compartilhamento e recuperação de informações eletrônicas.

Nesse cenário, como em outros padrões modernos, o padrão FHIR adota uma estratégia de camadas, que visa a separação de uma camada para a tomada de decisões de especialistas em saúde, e outra para a representação destas decisões abstraídas da área da saúde para uma representação computacional. Os profissionais da saúde que definem as informações que irão compor um conjunto de dados, são especialistas em seus contextos clínicos, por exemplo obstetrícia, transplante, imagens diagnósticas, entre outros, e não tem contato com a representação computacional do padrão FHIR. Essa equipe especialista é responsável por selecionar os componentes conceituais para contemplar os requisitos de informações de saúde em um contexto clínico e, posteriormente, a equipe de tecnologia é responsável por representar estas informações computacionalmente, nos diferentes formatos permitidos no padrão HL7 FHIR3 (JSON, XML e RDF). Essa separação é denominada, no contexto do Ministério da Saúde e RNDS, de Modelo Informacional e Modelo Computacional.

Modelo Informacional

Um Modelo Informacional (MI) é uma abstração conceitual que descreve um conjunto de informações dentro do contexto da saúde. Esse modelo é elaborado por especialistas em saúde, e resulta no desenvolvimento de um Modelo de Informações para um contexto clínico, que é instituído independente de padrões, essencial para atingir objetivos de interoperabilidade. Uma vez instituído o MI, conforme as definições estabelecidas na norma ISO/TS 13972:2015(E), que orienta, com especificações detalhadas de modelos clínicos, os processos e características, o MI representa, conceitualmente, a estrutura de informações que se deseja compartilhar em um contexto clínico.

Uma vez que a RNDS troca informações seguindo um padrão, definido como o padrão HL7 FHIR, é necessário definir os contextos clínicos que a RNDS espera receber. Atualmente, já existem desenvolvidos os modelos: Registro de Imunobiológico Administrado (RIA), MI instituído conforme portaria Nº 25 de 25 de novembro de 2023, Resultados de Exames Laboratoriais (REL), MI instituído conforme portaria atualizada Nº 883 de 29 de novembro de 2022, Registro de Atendimento Clínico (RAC), MI instituído conforme portaria Nº234 de 18 de julho de 2022, Sumário de Alta Hospitalar (SA), MI instituído conforme portaria Nº 701 de 29 de setembro de 2022. A RNDS está em desenvolvimento e constante processo de evolução, a publicação de novos modelos faz parte de seu plano para garantir a interoperabilidade em todos os níveis de atenção em escala nacional.

Modelo Computacional

Um Modelo Computacional (MC) é a representação em formato computacional das informações que foram definidas no Modelo Informacional (MI), seguindo as normas estabelecidas pela ISO/TS 13972:2015(E), e as definições quanto a restrições e terminologias nas portarias. É apenas no momento de definir o Modelo Computacional que o padrão de interoperabilidade adotado será evidenciado, uma vez um Modelo Informacional é independente de padrões, podendo ser traduzido e representado em qualquer padrão. Neste cenário, é no MC que as restrições nacionais necessárias são definidas, tais como definições de terminologias, dicionários, vocabulários, classificações e mapeamento para atender o escopo do Modelo Informacional, não só do ponto de vista técnico e estrutural, mas semântico.

Retomando o conceito da estratégia de um modelo de camadas, uma vez definido o modelo informacional (MI), o próximo passo é representar estas informações computacionalmente, através do Modelo Computacional (MC) em um formato compartilhável, possível de ser lido por máquinas e humanos, bem como garantindo a qualidade da informação trocada. A modelagem do computacional não segue necessariamente a mesma ordem lógica das informações da modelagem informacional. A modelagem computacional vem para formalizar a modelagem da informação de forma digital e computacionalmente compartilhável, e pode nortear a criação de um único recurso FHIR ou da composição de vários, relacionados entre si, de acordo com o escopo do que foi definido no modelo informacional.

Fluxo para propor novos modelos de Interoperabilidade para a RNDS

De forma geral, a proposição de novos modelos informacionais e computacionais é feita através da proposição da necessidade e justificativa para o Comitê Gestor de Saúde Digital (CGSD) instituído pela resolução CIT nº 05, de 25 de agosto de 2016, o qual avalia e toma providências de forma tripartite. Tratando-se de uma plataforma de dados nacional, a RNDS apenas recebe dados que estejam no padrão HL7 FHIR, desta forma, o processo de recebimento de dados deve, obrigatoriamente, passar pela qualificação e padronização dos dados para atender ao padrão adotado.

Dados da RNDS

Em um país de dimensões continentais como o Brasil, esse desafio se torna ainda mais complexo, devido a grande quantidade de ministérios, órgãos, empresas públicas e privadas, secretarias, dentre outros presentes nos mais de 5570 municípios e Distrito Federal. Sistemas e artefatos tecnológicos já se tornaram itens indispensáveis na rotina diária. De acordo com [e-Estonia 2020], 67% da população da Estônia utiliza a carteira digital de identidade regularmente, 99% dos serviços públicos estão online, 2773 diferentes serviços podem se comunicar por uma camada de troca de dados chamada X-Road. A incrível digitalização dos serviços faz da Estônia um exemplo tecnológico de qualidade, rapidez e sistematização não burocrática a ser seguida. O estudo de técnicas que visam a troca de dados entre sistemas de maneira segura, rápida e íntegra pode ser avaliado como um fator que alavanca o processo de digitalização de serviços públicos, reduzindo assim tempo de trabalho, tempo de resposta em atendimentos e solicitações da sociedade e público em geral e além do mais, pode fornecer mais transparência e padronização.

Quando se trata de alcançar a interoperabilidade em ambientes complexos de saúde digital, o conceito de barramento de interoperabilidade emerge como uma estrutura fundamental que engloba três momentos críticos: ingestão, armazenamento e exposição de dados (disponibilização). Cada um desses momentos desempenha um papel essencial na garantia de que sistemas de informação em saúde possam compartilhar informações de maneira eficaz e coordenada, beneficiando pacientes e profissionais de saúde.

A exposição de dados por meio de um aplicativo com interface front-end ou API (Application Programming Interface), representam duas abordagens distintas para disponibilizar informações. O primeiro, refere-se a um aplicativo com interface com o usuário de forma visual, onde os dados são apresentados e permite a interação pelos usuários finais. Por outro lado, uma API traz um catálogo de serviços de dados, que permite a sistemas e aplicativos que se comuniquem e troquem dados de forma programática, uma vez que as regras definidas para integração/autenticação são atendidas. As APIs não possuem uma interface de usuário visível, projetadas para que sistemas interajam de forma automatizada. Essa abordagem é valiosa quando se deseja permitir a integração de sistemas, facilitando a troca de informações entre diferentes aplicativos, sistemas e plataformas de maneira eficiente e padronizada. Neste cenário, os dados podem ser acessados através da plataforma fornecida, por meio de sua interface, seja para o cidadão – através do aplicativo de celular, quanto para o profissional – no contexto de um atendimento em prontuários integrados, bem como no consumo automatizado e sistematizado dos sistemas através das APIs.

Os canais oficiais de disseminação de informações sobre a RNDS são os meios autorizados e estabelecidos pelo Datasus e Ministério da Saúde para compartilhar os manuais, portarias e comunicados sobre os modelos de interoperabilidade em produção, em desenvolvimento e previstos. Através desses canais, o Datasus garante que as informações importantes cheguem aos implementadores, gestores de saúde e partes interessadas de forma apropriada, promovendo a transparência e a coesão nas comunicações.

Canais oficiais

- Portal de serviços do Datasus
- Portal da Rede Nacional de Dados em Saúde 
- Guia RNDS
- Guia de Integração – Modelos publicados 
- Conteúdo educativo
- Documentação facilitada
- Portarias e referências
Padrão de Interoperabilidade HL7 FHIR – adotado pela RNDS

A RNDS apenas recepciona e troca de dados que estejam no padrão de interoperabilidade definido pelo Ministério da Saúde, o HL7 FHIR. Neste cenário, um desafio central para a adoção de padrões de saúde é como lidar com a grande variabilidade causada pelos diversos processos de saúde. Com o tempo, mais informações são adicionadas à especificação, acentuando gradualmente custo e complexidade às implementações resultantes. A alternativa é contar com personalizações, mas elas também criam muitos problemas de implementação. Neste contexto, as soluções FHIR são construídas a partir de um conjunto de componentes modulares denominados “Recursos”. Esses recursos podem ser facilmente reunidos em sistemas funcionais que resolvem problemas clínicos e administrativos do mundo real por uma fração do preço das alternativas existentes. O FHIR é adequado para uso em uma ampla variedade de contextos – aplicativos de telefonia móvel, comunicações em nuvem, compartilhamento de dados baseado em EHR, comunicação de servidor em grandes provedores institucionais de saúde e muito mais. O padrão é publicado de forma mista, com partes normativas, que são mantidas estáveis para os implementadores, e partes ainda em uso experimental.

O HL7 monitora ativamente as implementações para continuar melhorando as especificações e responder às necessidades em sua plataforma 4disponibilizada para a comunidade internacional. Apesar de não haver um consenso mundial sobre padrões de saúde, devido às muitas vantagens que o FHIR oferece, ele tem sido amplamente utilizado, e sua comunidade está crescendo rapidamente. Orienta-se acompanhar o canal oficial de discussões para novas implementações e atualizações do padrão HL7 FHIR. O FHIR possui recursos para conceitos administrativos como paciente, provedor, organização e dispositivo, bem como uma ampla variedade de conceitos clínicos que abrangem problemas, medicamentos, diagnósticos, planos de cuidados, questões financeiras e muito mais.

2.1 Identidade do Recurso e Metadados

O recurso &#8220;Patient&#8221; por exemplo, representa as informações relacionadas a uma pessoa no sistema de saúde. Este recurso pertence à camada básica da estrutura do FHIR. Cada instância desse recurso é identificada de maneira única, geralmente expressa por meio de uma URL. Além disso, o recurso contém metadados, que oferecem detalhes sobre o recurso, como sua versão, data de criação ou última atualização, e a entidade responsável por essas ações. Esses metadados desempenham um papel crucial no rastreamento e gerenciamento das informações, garantindo que os sistemas operem com os dados mais recentes e precisos.

Definição de extensões através de uma URL

FHIR é projetado para ser extensível, permitindo que as organizações adicionem informações que não estão no seu padrão original, conhecido como recurso “canônico”. Uma &#8220;extensão&#8221; permite que novos dados sejam incluídos em um recurso padrão original, como o recurso Patient. Cada extensão tem uma URL única que aponta para sua definição, garantindo que qualquer sistema que encontre essa extensão possa entender seu propósito e significado. Assim, enquanto o FHIR fornece um conjunto de campos padrão, as organizações podem adaptá-lo às suas necessidades específicas usando extensões, e criando perfis específicos.

Dados padrão

- No contexto do recurso canônico &#8220;Patient&#8221;, os dados padrão podem incluir campos como:
- MRN (Medical Record Number): Um número único que identifica o paciente no sistema de saúde.
- Nome: Nome completo do paciente.
Gênero: Sexo do paciente, como masculino, feminino, entre outros.
- Data de Nascimento: A data em que o paciente nasceu.
- Provedor: Informações sobre o profissional ou instituição que fornece cuidados ao paciente, como um médico ou hospital.
O padrão FHIR, desenvolvido pela HL7, tem experimentado várias versões desde o seu lançamento, cada uma introduzindo melhorias, correções e novos recursos para responder às necessidades em constante evolução da comunidade de saúde. Na gestão de versionamento, é crucial para a metodologia de administração de dados reconhecer e gerenciar essas diferentes versões, tal como orienta a documentação oficial para os níveis de maturidade.

A especificação FHIR

O padrão FHIR é estruturado em uma série de módulos de especificação, cada um abordando diferentes aspectos e componentes da interoperabilidade em saúde. Em termos gerais, a especificação FHIR é dividida nos conjuntos de módulos, abaixo traz-se alguns principais, conforme a versão que a própria RNDS implementa, a R4:

- Fundação: A infraestrutura básica de definição sobre a qual o restante da especificação é construído;
- Suporte ao Implementador: Serviços para ajudar os implementadores a fazer uso da especificação;
- Segurança e Privacidade: Documentação e serviços para criar e manter segurança, integridade e privacidade;
- Conformidade: como testar a conformidade com a especificação e definir guias de implementação;
- Terminologia: Uso e suporte de terminologias e artefatos relacionados;
- Dados vinculados: métodos definidos de troca de recursos;
- Administração: Recursos básicos para rastrear pacientes, profissionais, organizações, dispositivos, substâncias etc.;
- Clínico: conteúdo clínico central, como problemas, alergias e processo de atendimento (planos de atendimento, encaminhamentos);
- Medicamentos: gerenciamento de medicamentos e rastreamento de imunização;
- Diagnóstico: Observações, relatórios de diagnóstico e solicitações de conteúdo relacionado;
Estes módulos são projetados para fornecer uma abordagem modular e flexível para representar, trocar e gerenciar informações de saúde. Eles cobrem uma ampla gama de tópicos, desde recursos clínicos básicos, como &#8220;Paciente&#8221; ou &#8220;Observação&#8221;, até componentes mais avançados, como operações, extensões e terminologias. Os recursos têm uma ampla gama de usos, desde conteúdo clínico puro, como planos de cuidados e relatórios de diagnóstico, até infraestrutura pura, como cabeçalho de mensagem e declarações de capacidade. Todos eles compartilham características técnicas comuns, mas podem ser usados de formas totalmente diferentes.

Objetivo do FHIR no MAD

O principal propósito da integração do FHIR em nossa metodologia de administração de dados é alcançar a interoperabilidade aprimorada. Isso significa que buscamos garantir que todos os sistemas de informação em saúde dentro da organização estejam em harmonia com o padrão FHIR, possibilitando uma troca de informações de saúde eficaz e segura. Além disso, temos a intenção de padronizar todos os nossos registros de saúde eletrônicos e outros dados pertinentes usando os recursos e estruturas fornecidos pelo FHIR. Este padrão não apenas facilitará a interoperabilidade, mas também melhorará a consistência e a qualidade dos dados.

No entanto, é importante destacar que reconhecemos a necessidade de flexibilidade. Portanto, outro objetivo crucial é implementar a extensibilidade do FHIR, permitindo que a organização personalize e expanda os dados conforme as necessidades específicas. Isso será feito mantendo os mais altos padrões de segurança e garantindo conformidade com os regulamentos pertinentes.

A modelagem FHIR segue uma abordagem de composição, na qual definimos as informações básicas, as definições de negócios e as estratégias para atingir um objetivo de interoperabilidade específico. A modelagem computacional implica em encontrar recursos, perfis ou composições FHIR adequadas para transmissão computacional de uma mensagem, podendo utilizar recursos canônicos ou especializados, conforme necessário. Com o FHIR, os casos de uso específicos geralmente são implementados combinando recursos por meio do uso de referências de recursos. Embora um único recurso possa ser útil por si só para um determinado caso de uso, é mais comum que os recursos sejam combinados e adaptados para atender aos requisitos específicos do caso de uso. Dessa forma, a integração do FHIR não só estabelece um padrão sólido de interoperabilidade, mas também permite a personalização e adaptação para atender às necessidades específicas da organização em relação aos dados de saúde.

Dois tipos especiais de recursos são usados para descrever como os demais recursos são definidos e usados:

- Declaração de capacidade (CapabilityStatement): descreve as interfaces que uma implementação expõe para troca de dados.
- Definição da Estrutura (StructureDefinition): fornece regras adicionais que servem para restringir se opcional ou obrigatória, cardinalidade, ligações de terminologia, tipos de dados e extensões definidas nos recursos usados pela implementação.
Sendo assim, o alicerce básico do FHIR é um recurso. Todo conteúdo intercambiável é definido como um recurso. Todos os recursos compartilham o seguinte conjunto de características:

- Uma maneira comum de defini-los e representá-los, construídos a partir de tipos de dados reutilizáveis comuns;
- Um conjunto comum de metadados;
- Uma parte legível por humanos;
É impraticável modelar a totalidade dos dados de saúde num único modelo de informação. Cada iniciativa de modelagem em saúde, desde especificações de mensagens HL7 versão 2 até recursos FHIR, decompõe o domínio de saúde em subdomínios ou fragmentos de modelo de informações menores e mais gerenciáveis. Com o FHIR, cada recurso é essencialmente um trecho do domínio mais amplo de informações sobre saúde. Ao dividir o modelo de informação sobre cuidados de saúde em partes menores (recursos, composições ou perfis para FHIR), é importante ter uma estrutura e um conjunto de diretrizes para promover a consistência e a integridade dentro das estruturas de recursos e na forma como os recursos se referenciam entre si.

Semântica e FHIR

A semântica refere-se ao significado, desempenhando um papel crucial na administração de dados para garantir que as informações sejam compreendidas de maneira uniforme em diferentes sistemas e contextos. No setor de saúde, a necessidade de uma interpretação consistente é tão fundamental que faz parte da interoperabilidade entre sistemas de informação. Ao incorporar princípios semânticos, o FHIR garante que os dados de saúde sejam não apenas transferidos, mas também interpretados de forma consistente e, independentemente do sistema ou plataforma em uso, o profissional de saúde que acessa os dados pode tomar uma decisão com base em dados contextualizados.

O FHIR atende a essa demanda, estabelecendo padrões para a troca de informações de saúde com precisão semântica. Ele incorpora elementos como &#8220;CodeableConcept&#8221;, que traduz conceitos codificados em textos compreensíveis; &#8220;ValueSet&#8221;, que define conjuntos específicos de códigos para contextos particulares; e &#8220;CodeSystem&#8221;, que detalha sistemas de codificação específicos. Central a isso, a &#8220;terminologia&#8221; no FHIR abrange o conjunto de códigos e conceitos usados em registros de saúde eletrônicos, refletindo o estudo de termos e suas relações em um domínio específico.

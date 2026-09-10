Chamada CNPq/FNDCT nº 06/2026  
– UNIVERSAL

**OTIMIZAÇÃO DE PROTOCOLOS DE TOMOGRAFIA COMPUTADORIZADA: SOLUÇÕES BASEADAS EM TAREFAS USANDO INTELIGÊNCIA ARTIFICIAL**

**Coordenador: Paulo Roberto Costa**

**Instituição: Instituto de Física da USP**

**RESUMO**

O projeto propõe o desenvolvimento e a implementação de uma plataforma avançada de Inteligência Artificial (IA) para otimizar os protocolos de Tomografia Computadorizada (TC), além do aprimoramento de objetos simuladores (*phantoms*) iniciados em projeto anterior. O objetivo principal é equilibrar a redução da dose de radiação ionizante entregue ao paciente com a manutenção da qualidade diagnóstica da imagem médica. A fundamentação do estudo baseia-se na avaliação de desempenho baseada em tarefas, superando as limitações das métricas tradicionais que falham ao analisar algoritmos não-lineares modernos. Metodologicamente, a pesquisa utilizará os *phantoms* geométricos e antropomórficos aprimorados para coletar dados sob variadas condições de aquisição e reconstrução (filtros, kV, mA). Redes Neurais Convolucionais (CNNs) e Redes Adversariais Generativas (GANs) serão treinadas para correlacionar parâmetros técnicos à qualidade clínica usando imagens de baixa dose. O *software* integrará ferramentas automatizadas que preveem o impacto de alterações nos protocolos antes do exame, além de criar um repositório centralizado de dados estruturados para auditoria e garantia de qualidade. Com isso, o projeto visa estabelecer novos padrões de excelência em TC, promovendo a segurança do paciente através do princípio ALARA (*As Low As Reasonably Achievable),* personalizando exames e fornecendo uma ferramenta robusta de suporte à decisão clínica para físicos médicos e radiologistas.

**FAPESP**  
**Auxílio à Inovação Regular (AIR)**  
**OPTIMIZATION OF COMPUTED TOMOGRAPHY PROTOCOLS: TASK-BASED SOLUTIONS USING ARTIFICIAL INTELLIGENCE**

**Coordenador: Paulo Roberto Costa**

**Instituição: Instituto de Física da USP**

**ABSTRACT**

The project proposes the development and implementation of an advanced Artificial Intelligence (AI) platform to optimize Computed Tomography (CT) protocols and improve phantoms developed in a prior project. The main objective is to balance the reduction of ionizing radiation dose delivered to the patient with the maintenance of diagnostic medical image quality. The study's rationale is based on task-based performance assessment, overcoming the limitations of traditional metrics that fail when analyzing modern non-linear algorithms. Methodologically, the research will utilize geometrical and anthropomorphic phantoms to collect data under varied acquisition and reconstruction conditions (filters, kV, mA). Convolutional Neural Networks (CNNs) and Generative Adversarial Networks (GANs) will be trained to correlate technical parameters to clinical quality using low-dose images. The software will integrate automated tools that predict the impact of changes in protocols prior to the exam, in addition to creating a centralized repository of structured data for auditing and quality assurance. Consequently, the project aims to establish new standards of excellence in digital radiology, promoting patient safety through the ALARA principle (As Low As Reasonably Achievable), personalizing exams, and providing a robust clinical decision support tool for medical physicists and radiologists.

# MOTIVAÇÃO / PROBLEMÁTICA / QUESTÃO CENTRAL / PERGUNTA DE PESQUISA / HIPÓTESE / PRESSUPOSTO INICIAL (indicar a motivação / problemática / questão central / pergunta de pesquisa / hipótese / pressuposto inicial, indicando diálogo com a literatura específica) \- até 4000 caracteres

**PROBLEMÁTICA: C**omplexidade do processo de otimização de procedimentos de TC dada a grande quantidade de variáveis técnicas e de reconstrução associadas à qualidade das imagens e doses entregues aos pacientes

**MOTIVAÇÃO**: De acordo com o Comitê Científico das Nações Unidas sobre os Efeitos da Radiação Atômica (UNSCEAR, 2022), aproximadamente, 4,3 bilhões de exames radiológicos médicos são realizados anualmente em todo o mundo, resultando em uma dose efetiva anual média decorrente desse tipo de procedimento de 0,62 mSv per capita. A maior contribuição para a dose efetiva coletiva foi a TC (62%). Porém, a TC se tornou uma das modalidades de imagem mais utilizadas na radiologia diagnóstica moderna\, devido à sua ampla disponibilidade, rápida aquisição e excelentes capacidades diagnósticas em uma grande variedade de aplicações clínicas (Milos et al., 2023, Park et al., 2022, Ben Alaya et al., 2026).

O aumento do uso da TC nos últimos anos (OECD, 2025\) levantou preocupações em relação à exposição do paciente à radiação ionizante. A otimização dos protocolos de TC para alcançar uma qualidade de imagem adequada para uma tarefa de detecção específica, mantendo a dose de radiação a mais baixa possível, tornou-se um desafio crucial para o uso seguro da TC.

# OBJETIVO GERAL E ESPECÍFICO (apresentar objetivo geral e os objetivos específicos da pesquisa de forma clara, consistente e adequada a linha de pesquisa escolhida) \- até 4000 caracteres

## **Objetivo Geral:** 

Desenvolvimento e validação de uma plataforma integrada (*phantoms* \+ *software*) para otimização de protocolos de TC (tórax, abdômen e cabeça), balanceando redução de dose com qualidade diagnóstica, aplicável em ambiente clínico real.

## **Objetivos específicos:**

1) Desenvolvimento de ferramentas computacionais para a determinação de:  
   1) medidas decorrentes de imagens das configurações geométricas do *phantom* híbrido desenvolvido (NPS, TTF e d´);  
   2) propriedades subjetivas das imagens\, dados por meio de análises de radiologistas (curvas ROC e análise AUC);  
2) Validação do *software* a ser desenvolvido, visando o registro de propriedade intelectual;  
3) Finalização e acabamento do *phantom* híbrido para tórax, abdome e crânio;  
4) Treinamento de profissionais (físicos, radiologistas, engenheiros, biomédicos, tecnólogos etc.); e  
5) Submissão de pedidos de patentes e artigos científicos.

Deseja-se que, ao final do projeto, os *phantoms* híbridos possam ser utilizados para reproduzir uma ampla gama de casos clínicos, com o objetivo de simplificar o processo de otimização de procedimentos, adequação das doses entregues aos pacientes, além de contribuir para o treinamento de profissionais. Para isso, espera-se que os *phantoms* híbridos sejam validados com sucesso, a partir das análises do *software* associado a ser desenvolvido no presente projeto. Desta forma, os dispositivos desenvolvidos deverão ser capazes de gerar parâmetros suficientes para que, tanto equipes de físicos médicos quanto radiologistas, tenham subsídios estratégicos para otimizar os protocolos de acordo com os objetivos clínicos específicos e as tecnologias de TC disponíveis. Além disso, busca-se contribuir para o treinamento de profissionais, visando a redução do tempo necessário para tomadas de decisão. Ao final, o resultado mais esperado é que o paciente receba a menor dose possível, no menor intervalo de tempo de exame possível, porém com a produção de imagens de adequada qualidade diagnóstica. 

# ESTADO DA ARTE (descrever o estado da arte e da tecnologia relativos ao projeto proposto) \- até 4000 caracteres

A Tomografia Computadorizada (TC) consolidou-se como uma das modalidades de imagem médica mais importantes da radiologia moderna devido à elevada capacidade diagnóstica, ampla disponibilidade e rapidez de aquisição. Entretanto, o crescimento contínuo de sua utilização tem intensificado as preocupações relacionadas à exposição dos pacientes à radiação ionizante, impulsionando o desenvolvimento de estratégias para otimização de protocolos que permitam reduzir a dose sem comprometer a qualidade diagnóstica. Tradicionalmente, a avaliação da qualidade de imagem em TC é realizada por meio de métricas globais, como a relação sinal-ruído (SNR) e a relação contraste-ruído (CNR), obtidas a partir de objetos simuladores (*phantoms*) geométricos. Esses simuladores fornecem informações quantitativas sobre o desempenho dos equipamentos e são amplamente utilizados em programas de controle de qualidade. Em paralelo, *phantoms* antropomórficos permitem avaliações qualitativas mais próximas das condições clínicas reais. Nos últimos anos, a introdução de técnicas avançadas de reconstrução de imagens, incluindo reconstruções iterativas (IR) e baseadas em aprendizado profundo (Deep Learning Reconstruction – DLR), modificou significativamente o paradigma de avaliação da qualidade de imagem. Como esses algoritmos introduzem comportamentos não lineares nas imagens reconstruídas, as métricas tradicionais passaram a apresentar limitações para caracterizar adequadamente seu desempenho clínico. Nesse contexto, abordagens baseadas em tarefas vêm ganhando destaque na literatura científica. O relatório Task Group 233 da American Association of Physicists in Medicine (AAPM) estabelece o índice de detectabilidade (d’) como uma das principais figuras de mérito para avaliação de sistemas modernos de TC. O cálculo do d’ é fundamentado em métricas como o espectro de potência de ruído (Noise Power Spectrum – NPS) e a função de transferência de modulação baseada em tarefas (Task Transfer Function – TTF), permitindo quantificar o desempenho do sistema em tarefas específicas de detecção de lesões. Apesar desses avanços, importantes lacunas permanecem abertas. A maioria dos simuladores disponíveis comercialmente foi projetada para avaliações simplificadas, utilizando estruturas geométricas uniformes e alvos artificiais de baixo contraste que não reproduzem adequadamente a complexidade anatômica observada em pacientes. Além disso, a correlação entre métricas objetivas, como o índice de detectabilidade, e o desempenho observacional humano em tarefas diagnósticas reais ainda não está completamente estabelecida. Outra limitação importante reside na ausência de ferramentas capazes de integrar métricas físicas de qualidade de imagem, avaliações observacionais realizadas por radiologistas, parâmetros técnicos de aquisição e reconstrução, bem como informações relacionadas à dose de radiação. Consequentemente, os processos de otimização de protocolos continuam dependentes de análises extensas e com limitada capacidade de generalização entre diferentes equipamentos e fabricantes. Diante desse cenário, observa-se uma tendência crescente de utilização de Inteligência Artificial para suporte à análise de imagens médicas e à tomada de decisão em radiologia. Entretanto, ainda são escassas as soluções capazes de utilizar dados provenientes de *phantoms* avançados para construir modelos preditivos voltados à otimização de protocolos tomográficos. Assim, o estado atual da tecnologia evidencia uma oportunidade para o desenvolvimento de plataformas integradas que combinem *phantoms* híbridos antropomórfico-geométricos, métricas avançadas baseadas em tarefas e Inteligência Artificial. Essa abordagem tem potencial para aproximar a avaliação física do desempenho clínico real e permitir processos de otimização mais robustos, padronizados e aplicáveis à prática hospitalar.

# METODOLOGIA (descrever a metodologia a ser empregada na execução do projeto para o alcance dos resultados, produtos e impactos esperados no prazo e orçamento previstos) \- até 4000 caracteres

## A metodologia proposta está estruturada em etapas integradas que contemplam o desenvolvimento tecnológico dos phantoms híbridos, a implementação de ferramentas computacionais baseadas em Inteligência Artificial e sua validação em ambiente clínico, visando otimizar protocolos de Tomografia Computadorizada por meio de uma abordagem baseada em tarefas (Tabela 1). Inicialmente, serão realizados o aprimoramento e a finalização dos phantoms híbridos de tórax, abdome e crânio\, desenvolvidos em projetos anteriores. As melhorias envolverão a incorporação de novas estruturas anatômicas, seleção e caracterização de materiais equivalentes aos tecidos humanos, aperfeiçoamento dos processos de manufatura aditiva e modular, além da produção de lesões sintéticas representativas de diferentes condições clínicas. Os dispositivos serão caracterizados quanto às propriedades físicas, radiológicas e geométricas, garantindo reprodutibilidade e compatibilidade com diferentes sistemas de TC. 

## Na etapa experimental, os phantoms serão submetidos à aquisição de imagens em diferentes tomógrafos e sob múltiplas combinações de parâmetros técnicos, incluindo tensão do tubo (kV), corrente (mA), espessura de corte, pitch, métodos de reconstrução e níveis de dose. Essa estratégia permitirá a construção de um banco de dados padronizado contendo imagens obtidas em condições controladas, representando ampla diversidade de protocolos clínicos. As imagens provenientes das configurações geométricas serão processadas automaticamente pelo software desenvolvido, permitindo a extração de métricas objetivas de qualidade de imagem, como NPS, TTF e d’. Paralelamente, as imagens adquiridas com os phantoms antropomórficos serão submetidas à avaliação de radiologistas experientes, possibilitando a obtenção de métricas subjetivas de desempenho diagnóstico, como curvas ROC e área sob a curva (AUC). Os dados físicos e observacionais serão integrados em uma base estruturada para treinamento e validação de modelos de aprendizado de máquina supervisionado. Serão investigadas diferentes abordagens estatísticas e computacionais, incluindo regressão regularizada, árvores de decisão, Random Forest, Gradient Boosting e Processos Gaussianos, com o objetivo de estabelecer modelos preditivos capazes de correlacionar parâmetros de aquisição\, dose de radiação e desempenho diagnóstico. 

## A validação dos modelos será realizada por meio de validação cruzada, reduzindo riscos de sobreajuste e aumentando sua capacidade de generalização. Com os modelos treinados, será implementado um processo de otimização multiobjetivo fundamentado na fronteira de Pareto, permitindo identificar protocolos que maximizem a detectabilidade clínica e minimizem simultaneamente a dose de radiação (Figura 1). Adicionalmente, será empregada a abordagem de ε-dominância para ampliar o conjunto de protocolos candidatos, considerando as incertezas experimentais inerentes às medições. 

## O software incorporará ferramentas de visão computacional para detecção automática de regiões de interesse, extração de métricas, processamento local das imagens e geração automática de relatórios, assegurando interoperabilidade com diferentes equipamentos e conformidade com os requisitos de segurança e proteção de dados. Por fim, toda a plataforma será validada em estudo-piloto conduzido no Instituto de Radiologia do Hospital das Clínicas da Faculdade de Medicina da USP (InRad/HCFMUSP), utilizando tomógrafos de diferentes fabricantes. Essa etapa permitirá calibrar os modelos de IA, avaliar sua robustez em ambiente clínico e verificar sua capacidade de recomendar protocolos personalizados que conciliem redução da dose de radiação e manutenção da qualidade diagnóstica. Os resultados obtidos subsidiarão a consolidação da plataforma tecnológica, a proteção da propriedade intelectual, a transferência de tecnologia e a futura adoção da solução por hospitais, clínicas e instituições de pesquisa.

**CAPACITAÇÃO DA EQUIPE E COMPETÊNCIAS NECESSÁRIAS (descrever as competências, habilidades e atitudes da equipe para o desenvolvimento do projeto. Citar produção bibliográfica, técnica e/ou artística/cultural (máximo de cinco itens), que demonstrem a qualificação prévia no tema) \- até 4000 caracteres**

LEVANTAR OS ORCIDS E/OU LATTES DE CADA UM

Paulo Roberto Costa \- Coordenação geral do projeto

* Otimização de protocolos de TC e aprimoramento dos *phantoms*  
   Edilaine Honório da Silva (Pesquisadora associada \- IFUSP)

  Wagner H. Marques (Aluno de Doutorado \- FMUSP)

* Desenvolvimento do *software* para otimização utilizando IA

  Alexandre Passos Suaide (Pesquisador Associado \- IFUSP)  
  Alessandra Tomal (Pesquisadora associada – IFGW/Unicamp))  
  Márcio Sawamura (Pesquisador Associado – INRAD/HCFMUSP)  
  Eduardo K. U. N. Fonseca (Pesquisador Associado – INCOR/HCFMUSP)  
  Davi V. P do Amaral (Aluno de Mestrado \- IFUSP)

* Concepção e melhorias para o *phantom* de pulmão

  Márcio Sawamura (Pesquisador Associado – INRAD/HCFMUSP)  
  Eduardo K. U. N. Fonseca (Pesquisador Associado – INCOR/HCFMUSP)  
  Giovana Negro (Bolsista de IC – IFUSP)

* Concepção e melhorias para o *phantom* de abdome  
   Cinthia Ortega (Pesquisadora Associada – INRAD/HCFMUSP)

  Douglas R. Godoy (Bolsista de IC – IFUSP)

* Concepção e melhorias para o *phantom* de cabeça  
   Leandro T. Lucato (Pesquisador Associado – INRAD/HCFMUSP)

  Victor H. F. Oliveira (Bolsista de IC – IFUSP)

* Desenvolvimento e Implementação de técnicas de manufatura aditiva

  Marcelo Oliveira (Pesquisador Associado – CTI Renato Archer)  
  João Luiz Amaro (Pesquisador Associado – UNESP)  
  Giovana Negro (Bolsista de IC – IFUSP)  
  Victor H. F. Oliveira (Bolsista de IC – IFUSP)  
  Douglas R. Godoy (Bolsista de IC – IFUSP)

* Implementação dos novos *phantoms* e do *software* para validações 

  Denise Yanikian Nersissian (Pesquisadora associada \- IFUSP)  
  Amanda Fernandes do Nascimento (Apoio Técnico \- IFUSP)  
  Isaías Petroni (Apoio Técnico \- IFUSP)

**COLABORAÇÕES E PARCERIAS NACIONAIS (descrever as parcerias e principais atuações da equipe no âmbito nacional, com destaque aquelas estabelecidas especificamente para a execução deste projeto) \- até 4000 caracteres**

IFGW

LAPRINT/CTI Renato Archer. Este laboratório é especializado em técnicas de manufatura aditiva, com a instrumentação e corpo técnico especializado para apoio aos desenvolvimentos propostos. (COMPLEMENTAR CONSULTANDO AQUI [https://www1.cti.gov.br/colab/language/pt-br/laprint.html](https://www1.cti.gov.br/colab/language/pt-br/laprint.html)

UNIESP

Departamento de Especialidades Cirúrgicas e Anestesiologia da Faculdade de Medicina da UNESP de Botucatu também permite a realização de pesquisas inovadoras utilizando parte da infraestrutura de impressão 3D daquela instituição. COMPLEMENTAR

INRAD

Para os desenvolvimentos computacionais propostos, além da expertise da equipe participante desta etapa do projeto, conta-se com o apoio do InLab/InovaHC, que é o Centro de Pesquisa, Desenvolvimento e Inovação em Tecnologias Aplicadas à Saúde do INRAD/HCFMUSP destinado a parceiros, pesquisadores, startups e desenvolvedores que tenham ou queiram criar projetos de Inteligência Artificial (IA) voltados às melhorias e soluções que abrangem diferentes etapas na jornada do paciente e na cadeia da saúde. Este laboratório de inovação conta com recursos de *hardware* e *software*, além de recursos humanos especializados, que irão apoiar o desenvolvimento e a validação das ferramentas computacionais previstas, incluindo o treinamento da rede neural. 

COMPLEMENTAR COM OS TOMOGRAFOS

**COLABORAÇÕES E PARCERIAS INTERNACIONAIS (descrever as parcerias e principais atuações da equipe no âmbito internacional, com destaque aquelas estabelecidas especificamente para a execução deste projeto) \- até 4000 caracteres**

Radbould – PAULO E ALESSANDRA prof. colaborador

Tewnte

UniPenn

**INFRAESTRUTURA INSTITUCIONAL PARA EXECUÇÃO DO PROJETO (descrever a infraestrutura da instituição executora e instituições colaboradoras para o desenvolvimento deste projeto) \- até 4000 caracteres**

o IFUSP tem pessoal técnico de informática e sistemas computacionais necessários, além de oficina mecânica plenamente capacitada

o IFUSP tem um escritório de administração de projetos

Completar a infraestrutura das instituições

**RECURSOS DE OUTRAS FONTES PARA EXECUÇÃO DO PROJETO (outras fontes de financiamento para a execução deste projeto ou projetos diretamente relacionados\, descrever o valor dos recursos e a natureza da despesa) \- até 4000 caracteres**

Dois projetos Fapesp foram recentemente coordenados pelo proponente e seu projeto de Produtividade em Desenvolvimento Tecnológico e Extensão Inovadora está em andamento:

* PRODUÇÃO DE OBJETOS SIMULADORES PARA TOMOGRAFIA COMPUTADORIZADA UTILIZANDO TÉCNICAS DE MANUFATURA ADITIVA (CNPQ DT 302986/2023-5 – R$39600,00 bolsa e R$ 36000,00 RT)  
* APLICAÇÃO DE TÉCNICAS DE MANUFATURA ADITIVA PARA PRODUÇÃO DE OBJETOS SIMULADORES PARA TOMOGRAFIA COMPUTADORIZADA (Fapesp Linha Regular \- 2022/11457-0 – R$96617,84 Mat. Permanente e de consumo e US$ 11056,10 material de consumo importado)  
* DESENVOLVIMENTO, VALIDAÇÃO E APLICAÇÃO DE TÉCNICAS PARA AVALIAÇÃO DE PROTOCOLOS TOMOGRÁFICOS DE BAIXAS DOSES (FAPESP BPE \- 2023/03945-8 – R$36574,33 transporte e seguro e US$ 46391,51 Bolsas)

O primeiro e o segundo desses projetos propuseram, com abordagem complementares, o desenvolvimento de três *phantoms* antropomórficos para a investigação qualitativa de índices de detectabilidade para avaliações de protocolos de TC realizados em três anatomias distintas: tórax (Figura 2), abdome (Figura 3\) e cabeça (Figuras 4 e 5). Os três *phantoms* foram finalizados com sucesso. O terceiro projeto consistiu em um estágio de pesquisa de um ano na Radboudumc, Holanda, no qual um dos *phantoms,* projetado e construído para avaliação de procedimentos de tórax, foi validado em equipamentos de última geração naquela Universidade (Figura 6). Estes projetos geraram diversos trabalhos, sendo o mais relevante publicado na revista *Medical Physics* (Costa et al., 2025). Além disso, o projeto deste *phantom* foi submetido ao INPI para obter sua patente através da Agência USP de Inovação (comunicação CC-PI-2024-0022).

Parte dos recursos a serem utilizados no desenvolvimento do presente projeto já foram adquiridos com apoio da Fapesp no processo 2022/11457-0. Além disso, o proponente é Bolsista de Produtividade Desenvolvimento Tecnológico e Extensão Inovadora do CNPq \- Nível 2 em uma área correlata à presente proposta e parte de sua reserva técnica também é utilizada para os desenvolvimentos propostos.

Por fim, como símbolo de engajamento e de forte interesse em empreendedorismo do grupo\, desde maio de 2026, três membros da equipe estão conduzindo um trabalho dentro da 1ª temporada do Programa SEBRAE SuperNova, competindo com equipes de todo o Brasil, em busca do prêmio de melhor projeto apresentado (Pitch \+ Canvas), em uma área temática compatível com a proposta do presente projeto.

**ORIGINALIDADE DA PROPOSTA E RELEVÂNCIA DO PROJETO PARA O DESENVOLVIMENTO CIENTÍFICO, TECNOLÓGICO E DE INOVAÇÃO NO PAÍS (relevância do projeto para expandir a fronteira do conhecimento científico e tecnológico ou caráter inovador) \- até 4000 caracteres**

A originalidade da proposta fundamenta-se na superação das limitações das métricas globais tradicionais de qualidade de imagem (como SNR e CNR), que falham ao analisar os algoritmos não-lineares modernos de reconstrução iterativa (IR) e baseados em aprendizado profundo (DLR). Alinhado às diretrizes do Relatório do Task Group 233 da AAPM, o projeto expande a fronteira do conhecimento ao estabelecer *phantoms* híbridos (geométricos e antropomórficos) capazes de correlacionar\, de forma inédita, índices físicos de qualidade baseados em tarefas — como o espectro de potência de ruído (NPS), a função de transferência de modulação baseada em tarefas (TTF) e o índice de detectabilidade (d′) — com dados de percepção visual clínica de médicos radiologistas (curvas ROC e análise AUC). Não há hoje no mercado de simuladores uma solução comercial eficiente capaz de simplificar essa análise unificada por meio de modelos preditivos automatizados. A relevância científica e social do projeto é evidenciada pelo cenário radiológico atual: realizam-se anualmente cerca de 4,3 bilhões de exames no mundo, sendo a tomografia computadorizada responsável por 62% da dose coletiva de radiação ionizante entregue à população. Diante disso, o projeto viabiliza a aplicação prática e customizada do princípio ALARA (*As Low As Reasonably Achievable*), equilibrando a redução de dose com a estrita manutenção da qualidade diagnóstica. Com o auxílio de Inteligência Artificial (redes CNNs e GANs), o software executará análises preditivas a partir de simulações de uma ampla gama de condições clínicas. A otimização multiobjetivo, formulada por meio do conceito de ϵ-dominância na fronteira de Pareto, resultará em protocolos que: 1\) preveem potenciais falhas e impactos técnicos antes do exame; 2\) reduzem o tempo para liberação do paciente; 3\) reduzem a sobrecarga de trabalho do radiologista; e 4\) minimizam a repetição de exames, maximizando o fluxo de atendimento e a exatidão dos laudos. No contexto da pesquisa em Física Médica e Inteligência Artificial aplicada à saúde, a proposta contribui para expandir a fronteira do conhecimento ao investigar uma questão ainda não completamente resolvida: a relação entre métricas objetivas de detectabilidade e o desempenho observacional humano em tarefas diagnósticas de tomografia computadorizada. A integração entre *phantoms* híbridos, observadores humanos e modelos preditivos permitirá gerar bases de dados inéditas para compreender a influência simultânea da dose\, dos parâmetros de aquisição e dos métodos modernos de reconstrução sobre a qualidade diagnóstica das imagens. Os resultados esperados possuem potencial para estabelecer novas metodologias de avaliação e otimização de protocolos de TC, contribuindo para a consolidação de abordagens baseadas em tarefas e para o desenvolvimento de futuras aplicações de Inteligência Artificial em radiologia diagnóstica. 

**DESENVOLVIMENTO TECNOLOGICO E POTENCIAL DE INOVAÇÃO (informar se os resultados serão imediatamente usados para resolver problemas práticos ou se contribuirão para o desenvolvimento técnico) \- até 4000 caracteres**

O projeto possui forte caráter de desenvolvimento tecnológico orientado à aplicação prática, uma vez que seus resultados foram concebidos para atender uma demanda concreta e crescente dos serviços de diagnóstico por imagem: a otimização de protocolos de Tomografia Computadorizada com redução da dose de radiação e preservação da qualidade diagnóstica. Dessa forma, os conhecimentos e produtos gerados não permanecerão restritos ao ambiente acadêmico, mas poderão ser incorporados diretamente às rotinas de hospitais, clínicas e centros de diagnóstico. O principal resultado tecnológico esperado é uma plataforma integrada composta por *phantoms* híbridos e software inteligente para suporte à tomada de decisão em processos de otimização de protocolos tomográficos. Essa plataforma permitirá a análise sistemática de parâmetros de aquisição e reconstrução, automatizando cálculos de métricas avançadas de qualidade de imagem, incluindo NPS, TTF e índice de detectabilidade, além de integrar resultados provenientes de avaliações observacionais realizadas por especialistas. A incorporação de técnicas de Inteligência Artificial representa um diferencial importante da proposta. A partir de um banco de dados estruturado obtido em diferentes tomógrafos e protocolos clínicos, serão desenvolvidos modelos preditivos capazes de estimar o impacto de alterações técnicas sobre a qualidade da imagem e a dose entregue ao paciente. Essa abordagem permitirá reduzir significativamente o tempo necessário para processos de otimização, além de fornecer suporte objetivo para decisões que atualmente dependem de análises extensas e altamente especializadas.

O potencial de inovação também está associado ao desenvolvimento de *phantoms* híbridos nacionais de alta fidelidade anatômica, produzidos por técnicas avançadas de manufatura aditiva e materiais radiologicamente equivalentes aos tecidos humanos. Esses dispositivos poderão ser utilizados não apenas para otimização de protocolos, mas também para treinamento profissional, validação de novas tecnologias de imagem, pesquisa clínica e programas de garantia da qualidade. Os resultados do projeto possuem potencial de aplicação imediata em ambientes clínicos. O estudo-piloto previsto no Instituto de Radiologia do Hospital das Clínicas da FMUSP permitirá validar a tecnologia em condições reais de operação, acelerando sua maturidade tecnológica e aproximando-a dos estágios finais de transferência para o setor produtivo. A estratégia contempla ainda proteção da propriedade intelectual por meio de registros de software e patentes, além da possibilidade de licenciamento industrial ou formação de parcerias com empresas do setor de dispositivos médicos e informática em saúde. Adicionalmente, o projeto contribui para a formação de recursos humanos altamente qualificados em áreas estratégicas como Inteligência Artificial, Física Médica, Engenharia Biomédica e Manufatura Aditiva. Esse aspecto amplia seu impacto tecnológico de longo prazo, fortalecendo competências nacionais em setores de elevada intensidade tecnológica. Assim, a proposta apresenta potencial de inovação ao transformar resultados científicos em soluções aplicáveis, escaláveis e economicamente relevantes, capazes de gerar benefícios diretos para pacientes, profissionais de saúde, instituições hospitalares e para o ecossistema brasileiro de inovação em saúde.

**PRODUTOS E RESULTADOS ESPERADOS (descrever quais os resultados efetivos esperados neste projeto, incluindo os avanços no estado da arte e da tecnologia que se pretende alcançar) \- até 4000 caracteres**

Ao final do projeto, espera-se disponibilizar uma plataforma integrada para otimização de protocolos de Tomografia Computadorizada composta por *phantoms* híbridos antropomórfico-geométricos, software de análise automatizada e modelos preditivos baseados em Inteligência Artificial. Os resultados esperados abrangem tanto avanços científicos quanto tecnológicos, contribuindo para o estado da arte em Física Médica, avaliação de qualidade de imagem e aplicações de IA em radiologia. Entre os principais produtos tecnológicos previstos estão a finalização e validação dos *phantoms* híbridos de tórax, abdome e crânio, capazes de reproduzir características anatômicas e radiológicas relevantes para estudos de detectabilidade e otimização de protocolos. Os dispositivos serão produzidos utilizando técnicas avançadas de manufatura aditiva e materiais equivalentes aos tecidos humanos, permitindo aplicações em controle de qualidade, treinamento profissional e validação de novas tecnologias de imagem.

Outro resultado central será o desenvolvimento de um software capaz de automatizar a extração de métricas avançadas de qualidade de imagem, incluindo NPS, TTF e índice de detectabilidade, reduzindo significativamente a necessidade de análises manuais. O sistema também incorporará ferramentas de visão computacional para identificação automática de regiões de interesse e geração de relatórios padronizados para suporte aos programas de garantia da qualidade. No âmbito da Inteligência Artificial, serão desenvolvidos modelos preditivos treinados a partir de dados obtidos em diferentes equipamentos e protocolos clínicos. Esses modelos permitirão estimar o impacto de alterações nos parâmetros de aquisição e reconstrução sobre a dose de radiação e a qualidade diagnóstica das imagens, fornecendo suporte objetivo para processos de otimização de protocolos.

Do ponto de vista científico, o projeto produzirá uma base de dados inédita relacionando métricas físicas de qualidade de imagem\, detectabilidade observacional, parâmetros técnicos e dose de radiação. Espera-se avançar significativamente na compreensão das relações entre indicadores objetivos e desempenho diagnóstico humano, contribuindo para a consolidação de metodologias baseadas em tarefas para avaliação de sistemas de TC. Adicionalmente, estão previstos depósitos de patentes associadas aos *phantoms* desenvolvidos, registro de propriedade intelectual do software, submissão de artigos científicos em periódicos de alto impacto e formação de recursos humanos especializados em Física Médica, Inteligência Artificial e manufatura aditiva aplicada à saúde.

Como resultado final, espera-se disponibilizar uma tecnologia nacional capaz de acelerar processos de otimização de protocolos tomográficos, contribuindo para a redução de dose aos pacientes e para a melhoria da qualidade diagnóstica em serviços de radiologia.

**POTENCIAIS IMPACTOS ECONÔMICOS, SOCIAIS E AMBIENTAIS (descrever quais os potenciais impactos esperados deste projeto, explicitando os passos futuros (posteriores ao término do projeto) necessários para que tal impacto se torne efetivo) \- até 4000 caracteres**

Os impactos esperados do projeto abrangem dimensões econômicas, sociais, tecnológicas e ambientais, com potencial de geração de benefícios duradouros para o sistema de saúde brasileiro. Do ponto de vista econômico, a proposta contribui para reduzir a dependência nacional de simuladores e tecnologias importadas utilizadas em programas de controle de qualidade em radiologia. O desenvolvimento de *phantoms* híbridos e ferramentas computacionais nacionais cria oportunidades para geração de propriedade intelectual, transferência de tecnologia e estabelecimento de parcerias com empresas dos setores de dispositivos médicos, informática em saúde e manufatura aditiva. A adoção da tecnologia também poderá reduzir custos operacionais associados à otimização de protocolos, treinamentos e processos de validação em hospitais e clínicas. No âmbito social, o principal impacto está relacionado à segurança dos pacientes. A utilização de protocolos mais eficientes permitirá reduzir exposições desnecessárias à radiação ionizante sem comprometer a qualidade diagnóstica dos exames. Adicionalmente, a ferramenta fornecerá suporte à tomada de decisão por físicos médicos e radiologistas, contribuindo para maior padronização dos procedimentos, redução de retrabalho e melhoria da qualidade assistencial. O projeto também favorecerá a formação de profissionais qualificados em áreas estratégicas para o desenvolvimento tecnológico nacional. Os impactos tecnológicos incluem a consolidação de competências nacionais em Inteligência Artificial aplicada à saúde, manufatura aditiva para dispositivos médicos e avaliação avançada de qualidade de imagem. A plataforma proposta poderá servir como base para futuras aplicações envolvendo otimização automatizada de protocolos, radiômica, validação de algoritmos de reconstrução e integração com sistemas hospitalares. Sob a perspectiva ambiental, a utilização de técnicas de manufatura aditiva permite reduzir desperdícios de matéria-prima quando comparada a métodos convencionais de fabricação. Além disso, o desenvolvimento local dos dispositivos contribui para diminuir a dependência de cadeias internacionais de suprimento e os impactos associados ao transporte de equipamentos importados.

Após o término do projeto, a efetivação desses impactos dependerá da conclusão dos processos de proteção da propriedade intelectual\, da validação multicêntrica da tecnologia em novos hospitais e da formalização de parcerias para transferência tecnológica e escalonamento produtivo. Também será importante estabelecer diálogo com órgãos regulatórios e entidades de acreditação para ampliar a adoção da metodologia em programas nacionais de garantia da qualidade e otimização de protocolos em tomografia computadorizada.

**PLANO DE DIVULGAÇÃO CIENTÍFICA (descrever as formas utilizadas para divulgação do trabalho para o público não especializado) \- até 4000 caracteres**

Assim como ocorreu no desenvolvimento do protótipo do *phantom* de pulmão[^1], os dispositivos resultantes do presente projeto, bem como o programa de análise com base em Inteligência Artificial, serão impulsionados para terem visibilidade junto ao público geral, externo à academia. Além disso\, dadas as vantagens de que as inovações propostas sejam conhecidas por radiologistas e físicos médicos, serão prospectadas parcerias com a iniciativa privada para demonstrações dos dispositivos em feiras que acompanham eventos tais como a Jornada Paulista de Radiologia e o Congresso Brasileiro de Física Médica. 

Além das publicações dirigidas para o público geral, são esperadas submissões de, no mínimo, 2-3 artigos científicos para revistas indexadas, apresentando as inovações decorrentes tanto dos desenvolvimentos quanto das aplicações dos dispositivos e do *software* a ser criado.

**REFERÊNCIAS (conjunto padronizado de elementos descritivos, retirados de um documento, que permite sua identificação individual \- NBR 6023:2002) \- até 4000 caracteres**

BEN ALAYA, I., FELHI, F., MESSELMANI, M. & LABIDI, S. 2026\. Advancing Stroke Diagnosis: A Comprehensive Review of Artificial Intelligence in Detecting Early Ischemic Changes on Noncontrast CT (NCCT). *Academic Radiology,* 33**,** 1060-1069.  
COSTA, P. R., BOISET, G. R., PIMENTA, E. B., ROCHA, R. M. V., MOURA, R. A. S., MARQUES, W. H., OOSTVEEN, L. J., GEURTS, B., SAWAMURA, M. V. Y., NERSISSIAN, D. Y., YOSHIMURA, E. M. & SECHOPOULOS, I. 2025\. Hybrid phantom for lung CT: Design and validation. *Medical Physics,* 52**,** e17990.  
GIANSANTE, L., MARTINS, J. C., NERSISSIAN, D. Y., KIERS, K. C., KAY, F. U., SAWAMURA, M. V. Y., LEE, C., GEBRIM, E. M. M. S. & COSTA, P. R. 2019\. Organ doses evaluation for chest computed tomography procedures with TL dosimeters: Comparison with Monte Carlo simulations. *Journal of applied clinical medical physics,* 20**,** 308-320.  
MILOS, R. I., RÖHRICH, S., PRAYER, F., STRASSL, A., BEER, L., HEIDINGER, B. H., WEBER, M., WATZENBOECK, M. L., KIFJAK, D., TAMANDL, D. & PROSCH, H. 2023\. Ultrahigh-Resolution Photon-Counting Detector CT of the Lungs: Association of Reconstruction Kernel and Slice Thickness With Image Quality.  
OECD 2025\. *Health at a Glance 2025: OECD Indicators* ,  Paris,. OECD Publishing.  
PARK, J. A.-O., SHIN, J. A.-O., MIN, I. A.-O., BAE, H. A.-O., KIM, Y. A.-O. & CHUNG, Y. A.-O. 2022\. Image Quality and Lesion Detectability of Lower-Dose Abdominopelvic CT Obtained Using Deep Learning Image Reconstruction.  
PIMENTA, E. B. & COSTA, P. R. 2025\. Model observers and detectability index in x-ray imaging: historical review, applications and future trends. *Physics in Medicine & Biology,* 70\.  
POZZESSERE, C. A.-O., VON GARNIER, C. & BEIGELMAN-AUBRY, C. 2023\. Radiation Exposure to Low-Dose Computed Tomography for Lung Cancer Screening: Should We Be Concerned?  
SAMEI, E., BAKALYAR D., BOEDEKER K. L., BRADY S., FAN J., LENG S., MYERS K. J., POPESCU L. M., RAMIREZ G. J. CARLOS, R. F., SOLOMON J., VAISHNAV J., WANG J. 2019\. Performance evaluation of computed tomography systems: Summary of AAPM Task Group 233\. *Medical Physics,* 46**,** e735-e756.  
SHEKTER, D. H. A. S. F. W. 2020\. *Efficiently calculating ROC curves, AUC, and uncertainty from 2AFC studies with finite samples , booktitle \= Medical Imaging 2020: Image Perception, Observer Performance, and Technology Assessment*.  
SHUNHAVANICH, P., MEI, K., SHAPIRA, N., STAYMAN, J. W., MCCOLLOUGH, C. H., GANG, G., LENG, S., GEAGAN, M., YU, L., NOËL, P. B. & HSIEH, S. S. 2024\. 3D printed phantom with 12 000 submillimeter lesions to improve efficiency in CT detectability assessment. *Med Phys*.  
SOLOMON, J. & SAMEI, E. 2016\. Correlation between human detection accuracy and observer model-based image quality metrics in computed tomography. *J Med Imaging (Bellingham),* 3**,** 035506\.  
TSENG, H. W., FAN, J. & KUPINSKI, M. A. 2016\. Design of a practical model-observer-based image quality assessment method for x-ray computed tomography imaging systems. *J Med Imaging (Bellingham),* 3**,** 035503\.  
UNSCEAR 2022\. Evaluation of medical exposure to ionizing radiation. *2020/2021 Report.* New York: United Nations: United Nations Scientific Committee on the Effects of Atomic Radiation.  
ZHOU, W., LI, H. & ANASTASIO, M. A. 2019\. Approximating the Ideal Observer and Hotelling Observer for Binary Signal Detection Tasks by Use of Supervised Learning Methods. *IEEE Trans Med Imaging,* 38**,** 2456-2468.

[^1]:  Ver links das seguintes reportagens: 
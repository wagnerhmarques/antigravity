**FAPESP** 

**Auxílio à Inovação Regular (AIR)** 

**SOLUÇÕES BASEADAS EM TAREFAS USANDO  INTELIGÊNCIA ARTIFICIAL PARA OTIMIZAÇÃO DE  PROTOCOLOS DE TOMOGRAFIA COMPUTADORIZADA** 

**Pesquisador responsável: Paulo Roberto Costa** 

**Instituição sede: Instituto de Física da USP** 

**RESUMO** 

O projeto propõe o desenvolvimento e a implementação de uma plataforma avançada  de Inteligência Artificial (IA) para otimizar os protocolos de Tomografia  Computadorizada (TC), além do aprimoramento de objetos simuladores (*phantoms*)  iniciados em projeto anterior. O objetivo principal é equilibrar a redução da dose de  radiação ionizante entregue ao paciente com a manutenção da qualidade diagnóstica  da imagem médica. A fundamentação do estudo baseia-se na avaliação de desempenho  baseada em tarefas, superando as limitações das métricas tradicionais que falham ao  analisar algoritmos não-lineares modernos. Metodologicamente, a pesquisa utilizará os  *phantoms* geométricos e antropomórficos aprimorados para coletar dados sob variadas  condições de aquisição e reconstrução (filtros, kV, mA). Redes Neurais Convolucionais  (CNNs) e Redes Adversariais Generativas (GANs) serão treinadas para correlacionar  parâmetros técnicos à qualidade clínica usando imagens de baixa dose. O *software* integrará ferramentas automatizadas que preveem o impacto de alterações nos  protocolos antes do exame, além de criar um repositório centralizado de dados  estruturados para auditoria e garantia de qualidade. Com isso, o projeto visa estabelecer  novos padrões de excelência em TC, promovendo a segurança do paciente através do  princípio ALARA (*As Low As Reasonably Achievable),* personalizando exames e  fornecendo uma ferramenta robusta de suporte à decisão clínica para físicos médicos e  radiologistas.  
**FAPESP** 

**Auxílio à Inovação Regular (AIR)** 

**AI-DRIVEN TASK-BASED SOLUTIONS FOR OPTIMIZING CT  PROTOCOLS** 

**Pesquisador responsável: Paulo Roberto Costa** 

**Instituição sede: Instituto de Física da USP** 

**ABSTRACT** 

The project proposes the development and implementation of an advanced Artificial  Intelligence (AI) platform to optimize Computed Tomography (CT) protocols and  improve phantoms developed in a prior project. The main objective is to balance the  reduction of ionizing radiation dose delivered to the patient with the maintenance of  diagnostic medical image quality. The study's rationale is based on task-based  performance assessment, overcoming the limitations of traditional metrics that fail  when analyzing modern non-linear algorithms. Methodologically, the research will  utilize geometrical and anthropomorphic phantoms to collect data under varied  acquisition and reconstruction conditions (filters, kV, mA). Convolutional Neural  Networks (CNNs) and Generative Adversarial Networks (GANs) will be trained to  correlate technical parameters to clinical quality using low-dose images. The software  will integrate automated tools that predict the impact of changes in protocols prior to  the exam, in addition to creating a centralized repository of structured data for auditing  and quality assurance. Consequently, the project aims to establish new standards of  excellence in digital radiology, promoting patient safety through the ALARA principle (As  Low As Reasonably Achievable), personalizing exams, and providing a robust clinical  decision support tool for medical physicists and radiologists.  
**ENUNCIADO DO PROBLEMA** 

**PROBLEMA A SER TRATADO: Complexidade do processo de otimização de  procedimentos de tomografia computadorizada dada a grande quantidade de  variáveis técnicas e de reconstrução associadas à qualidade das imagens e doses  entregues aos pacientes** 

**CONTRIBUIÇÃO PARA A ÁREA: Desenvolvimento e validação de uma plataforma  integrada (*phantoms* \+ *software*) para otimização de protocolos de TC (tórax,  abdômen e cabeça), balanceando redução de dose com qualidade diagnóstica,  aplicável em ambiente clínico real.**  

De acordo com o Comitê Científico das Nações Unidas sobre os Efeitos da Radiação  Atômica (UNSCEAR, 2022), aproximadamente, 4,3 bilhões de exames radiológicos  médicos são realizados anualmente em todo o mundo, resultando em uma dose efetiva  anual média decorrente desse tipo de procedimento de 0,62 mSv per capita. A maior  contribuição para a dose efetiva coletiva foi a tomografia computadorizada (TC) (62%).  Porém, a TC se tornou uma das modalidades de imagem mais utilizadas na radiologia  diagnóstica moderna\, devido à sua ampla disponibilidade, rápida aquisição e excelentes  capacidades diagnósticas em uma grande variedade de aplicações clínicas (Milos et al.,  2023, Park et al., 2022, Ben Alaya et al., 2026). 

O aumento do uso da TC nos últimos anos (OECD, 2025\) levantou preocupações em  relação à exposição do paciente à radiação ionizante. A otimização dos protocolos de TC  para alcançar uma qualidade de imagem adequada para uma tarefa de detecção  específica, mantendo a dose de radiação a mais baixa possível, tornou-se um desafio  crucial para o uso seguro da TC. 

Para mitigar este desafio, pesquisadores estão explorando melhorias técnicas para  reduzir ainda mais a dose de radiação ionizante (Pozzessere et al., 2023). Contudo,  qualquer processo de redução de doses deve ser acompanhado de uma cuidadosa  análise de qualidade de imagens\, de forma a garantir que o aumento de ruído  decorrente desta redução de dose não possibilite eventuais falhas no reconhecimento  de lesões, comprometendo, portanto, a qualidade do diagnóstico. Este processo,  identificado como otimização de protocolos\, deve ser realizado por profissionais   
treinados e com dispositivos que permitam avaliar a qualidade destas imagens não  somente do ponto de vista tradicional, utilizando objetos simuladores ou\, do inglês,  *phantoms*. O presente projeto trata somente de *phantoms* de qualidade de imagens,  que podem ser classificados como geométricos, que fornecem informações  quantitativas relacionadas às métricas de qualidade de imagens, e antropomórficos, que  permitem a avaliação qualitativa da resposta dos sistemas de imagem. 

Embora as métricas globais, como a relação sinal-ruído (SNR) ou a relação contraste ruído (CNR), sejam comumente usadas para descrever a qualidade da imagem, elas não  transmitem adequadamente o desempenho do observador (ex: médicos radiologistas)  em tarefas de imagem diagnóstica. No caso da TC, essas limitações são, ainda, mais  evidenciadas pelo fato de que os métodos de reconstrução de imagens mais modernos,  tais como as reconstruções iterativas (IR) ou as baseadas em aprendizado profundo  (DLR), incorporarem não-linearidades nas imagens – que não podem ser  apropriadamente identificadas pelas métricas de qualidade tradicionais. Por essa razão,  o relatório 233 da AAPM (Samei, 2019\) sugere que o índice de detectabilidade (d’) deva  ser adotado para a avaliação deste tipo de tecnologia, considerando essas limitações  das outras métricas de qualidade (Pimenta and Costa, 2025). 

As métricas de qualidade de imagem (IQ), como o espectro de potência de ruído (NPS)  e a função de transferência de modulação baseada em tarefas (TTF), são úteis para  avaliar as características de ruído e resolução espacial de imagens de *phantoms*. O  Relatório do Task Group 233 da AAPM apresenta diferentes métodos para o  estabelecimento de Figuras de Mérito (FOMs) relacionadas com as técnicas modernas  de TC. Este Relatório também exemplifica o uso de diferentes designs de simuladores  para avaliar quantitativamente a qualidade da imagem através destas métricas e de suas  combinações, resultando no índice de detectabilidade. 

No entanto, a associação entre o d’ e as capacidades de um observador para identificar  achados clínicos relevantes em imagens de TC ainda não está totalmente estabelecida.  Os designs atuais de simuladores assumem que as capacidades do equipamento e dos  protocolos de TC são bem avaliadas por estruturas simples, uniformes e de formato não  anatômico de baixo contraste para simulação de detecção de lesões em doentes. Além  disso, a adoção do d’ para fins de otimização de protocolos em situações clínicas   
realistas é limitada, uma vez que depende de imagens de coortes de casos clínicos com  características anatômicas semelhantes, examinados utilizando diferentes protocolos e  métodos de reconstrução. Portanto, simuladores híbridos (antropomórfico geométricos) – que permitam avaliar, quantitativamente, as grandezas baseadas em  tarefas e, ao mesmo tempo, permite uma análise qualitativa, por meio da detecção de  estruturas que mimetizam o paciente – são convenientes para fins de otimização de  protocolos. 

Contudo, apesar da relevância do d’ para esse tipo de avaliação em TC, a correlação  entre os valores obtidos desta métrica e as respostas observacionais decorrentes,  levando em consideração as doses aplicadas, os parâmetros de aquisição e de  reconstrução da imagem, ainda não é uma questão totalmente resolvida. Para a solução  desta limitação, o desenvolvimento de *phantoms* híbridos (geométricos e  antropomórficos) é de fundamental importância. 

Para avançar nesta área de investigação\, dois projetos Fapesp foram recentemente  coordenados pelo proponente: 

● APLICAÇÃO DE TÉCNICAS DE MANUFATURA ADITIVA PARA PRODUÇÃO DE  OBJETOS SIMULADORES PARA TOMOGRAFIA COMPUTADORIZADA (Linha  Regular \- 2022/11457-0) 

● DESENVOLVIMENTO, VALIDAÇÃO E APLICAÇÃO DE TÉCNICAS PARA AVALIAÇÃO  DE PROTOCOLOS TOMOGRÁFICOS DE BAIXAS DOSES (BPE \- 2023/03945-8) 

O primeiro deles propôs o desenvolvimento de três *phantoms* antropomórficos para a  investigação qualitativa de índices de detectabilidade para avaliações de protocolos de  TC realizados em três anatomias distintas: tórax, abdome e cabeça. Os três *phantoms* foram finalizados com sucesso. O segundo projeto consistiu em um estágio de pesquisa  de um ano na Radboudumc, Holanda, no qual um dos *phantoms,* projetado e construído  para avaliação de procedimentos de tórax, foi validado em equipamentos de última  geração naquela Universidade. Estes projetos geraram diversos trabalhos, sendo o mais  relevante publicado na revista *Medical Physics* (Costa et al., 2025). Além disso, o projeto  deste *phantom* foi submetido ao INPI para obter sua patente através da Agência USP de  Inovação (comunicação CC-PI-2024-0022).  
As próximas etapas para tornar estes *phantoms* ferramentas práticas que possam ser  utilizadas por equipes responsáveis pela otimização de procedimentos de tomografia  computadorizada em clínicas e hospitais são: 

• Melhorias em suas construções visando praticidade em suas aplicações em  ambiente clínico; 

• Consolidação de suas metodologias de análise de resultados quantitativos (configuração geométrica) e qualitativos (configuração antropomórfica) de  forma a permitir a utilização em processos de otimização; 

• Desenvolvimento de ferramentas computacionais que permitam sua aplicação  sistemática e consistente para otimização de protocolos de TC de tórax, abdome  e cabeça.  

**RESULTADOS ESPERADOS**  

1\) Desenvolvimento de ferramentas computacionais para a determinação de: a) medidas decorrentes de imagens das configurações geométricas do *phantom* híbrido desenvolvido (NPS, TTF e d´); 

b) propriedades subjetivas das imagens\, dados por meio de análises de  radiologistas (curvas ROC e análise AUC); 

2\) Validação do *software* a ser desenvolvido, visando o registro de propriedade  intelectual; 

3\) Finalização e acabamento do *phantom* híbrido para tórax, abdome e crânio; 4\) Treinamento de profissionais (físicos, radiologistas, engenheiros, biomédicos,  tecnólogos etc.); e 

5\) Submissão de pedidos de patentes e artigos científicos. 

Deseja-se que, ao final do projeto, os *phantoms* híbridos possam ser utilizados para  reproduzir uma ampla gama de casos clínicos, com o objetivo de simplificar o processo  de otimização de procedimentos, adequação das doses entregues aos pacientes, além  de contribuir para o treinamento de profissionais. Para isso, espera-se que os *phantoms* híbridos sejam validados com sucesso, a partir das análises do *software* associado a ser  desenvolvido no presente projeto. Desta forma, os dispositivos desenvolvidos deverão  ser capazes de gerar parâmetros suficientes para que, tanto equipes de físicos médicos   
quanto radiologistas, tenham subsídios estratégicos para otimizar os protocolos de  acordo com os objetivos clínicos específicos e as tecnologias de TC disponíveis. Além  disso, busca-se contribuir para o treinamento de profissionais, visando a redução do  tempo necessário para tomadas de decisão. Ao final, o resultado mais esperado é que o  paciente receba a menor dose possível, no menor intervalo de tempo de exame possível,  porém com a produção de imagens de adequada qualidade diagnóstica.  

Cabe destacar que a seguinte proposta tem aderência aos seguintes eixos estratégicos  definidos no documento “Temas Estratégicos da FAPESP para Ciência, Tecnologia e  Inovação – Período de 2026-2028”, aprovado pelo Conselho Superior da Fapesp em  18/03/2026: 4\. Transição digital e inteligência artificial e 6\. Saúde humana e animal.  Neste contexto, a produção final do projeto deve, potencialmente, gerar valores sociais  e econômicos, incentivando o impulsionamento a cadeia produtiva nesta área com  trajetórias tecnológicas empreendedoras e inovadoras, com respeito ao meio ambiente  e à saúde humana. 

**Métricas de acompanhamento** 

Em atendimento ao critério 12.1.5 (a.6) da Chamada AIR (FAPESP/2026), as métricas de  acompanhamento do projeto estão organizadas em três fases semestrais, com  indicadores quantitativos mensuráveis ao longo da vigência de 36 meses (Tabela 1). 

**Usuários-alvo e rota de adopção tecnológica** 

Os resultados do projeto são direcionados a três grupos principais de usuários. O  primeiro é o segmento hospitalar e clínico: físicos médicos e radiologistas de hospitais  públicos e privados que realizam controle de qualidade e otimização de protocolos de  TC — estima-se que existam mais de 7.000 tomógrafos instalados no Brasil (CFR/ANS),  representando uma base potencial significativa de adoção imediata. O segundo é a  indústria de dispositivos médicos: fabricantes de *phantoms* (como CIRS e Gammex) e  desenvolvedores de sistemas PACS/CAD, para os quais os *phantoms* híbridos e o  *software* poderão ser licenciados mediante contrato de transferência de tecnologia  intermediado pela AUSPIN, reduzindo a dependência brasileira de insumos importados.  O terceiro é o setor regulatório e de acreditação: órgãos como a ANVISA e o CBR (Colégio  Brasileiro de Radiologia e Diagnóstico por Imagem) que estabelecem protocolos   
nacionais de qualidade em imagem médica poderiam adotar a metodologia como  padrão de referência. A rota de adoção contempla três etapas: (i) validação e  demonstração no InRad/HCFMUSP; (ii) registro de PI e elaboração de proposta  comercial com apoio do programa SEBRAE SuperNova e do InLab; (iii) licenciamento ou  parceria com empresa do setor, ou disponibilização como ferramenta *open-source* para  redes públicas de saúde. 

*Tabela 1: Métricas de acompanhamento do projeto e critérios de validação*

| Fase / Período  Fase 1  (M 1–12)   Finalização dos   *phantoms* | Métrica / Entregável  | Valor-alvo / Critério |
| :---: | :---: | :---: |
|  | *Phantom* de tórax finalizado e caracterizado | Desvio de atenuação ≤ 5% em  relação ao tecido humano de  referência |
|  | *Phantoms* de abdome e crânio finalizados (esboços  e materiais definidos) | ≥ 3 anatomias validadas por   imagem |
|  | Coleta de dataset inicial (protocolos ×   equipamentos) | ≥ 3 tomógrafos mapeados com ≥ 5  protocolos cada |
| **Fase 2**  (M 13–24)   Desenvolvimento  do *software* | Módulo de cálculo automático de NPS, TTF e d’  funcional | Erro de previsão de d’ ≤ 10% vs.  cálculo manual em conjunto de  teste |
|  | Modelos preditivos (ML) treinados e validados por  validação cruzada | R² ≥ 0,80 entre d’ predito e   observado no conjunto de   validação |
|  | Pedido de registro de PI do *software* protocolado  na AUSPIN | Protocolo de submissão   protocolado até o mês 24 |
| **Fase 3** (M 25–36)  Validação clínica e  transferência | Estudo-piloto no InRad/HCFMUSP concluído (todos  os 7 tomógrafos testados) | AUC média dos observadores ≥ 0,80 em pelo menos 2 anatomias |
|  | Artigos científicos indexados submetidos  | Mínimo 2 artigos submetidos a  periódicos Qualis A1/A2 |
|  | Pedidos de patente dos *phantoms* protocolados | ≥ 1 patente de *phantom* e 1 de  *software* depositadas na AUSPIN  até M 36 |

**DESAFIOS E OS MEIOS E MÉTODOS PARA SUPERÁ-LOS**  

**Finalização dos *phantoms* híbridos para tórax, abdome e crânio** 

**DESAFIO: Prover o país de tecnologia nacional para confecção de *phantoms* híbridos  para otimização de protocolos de tomografia computadorizada** 

**MEIOS E MÉTODOS PARA SUPERÁ-LOS:** 

O desenvolvimento e a finalização da plataforma integrada de *phantoms* híbridos para  tórax, abdome e crânio — fundamentados nas provas de conceito consolidadas nos projetos anteriores (processos 2022/11457-0 e 2023/03945-8) — estabelecem uma  robusta trajetória de inovação focada na transição tecnológica do nível TRL 6 ao TRL 9,  visando à geração de valor econômico e social para o setor de saúde nacional. Para  romper com o atual estado da arte e superar a limitação da utilização de polímeros  comerciais tradicionais na produção de *phantoms* para a área de imagens médicas, a  metodologia proposta implementará formulações proprietárias baseadas na produção 

de resinas com agentes radiopacos em variadas concentrações (Patente  BR1020200235800). Adicionalmente, para atender à demanda crítica de algoritmos  modernos de Inteligência Artificial, o projeto adotará um processo inédito de  manufatura híbrida e modular, combinando métodos de manufatura aditiva para os  órgãos-base e lesões sintéticas extraídas de imagens DICOM de exames reais.  

Esse modelo não apenas soluciona os gargalos de escalabilidade industrial e  reprodutibilidade geométrica e radiológica entre lotes, mas também terá sua  durabilidade e usabilidade clínica em ambiente hospitalar real por meio de um estudo piloto a ser realizado Instituto de Radiologia do Hospital das Clínicas da FMUSP (InRad),  que funcionará como *testbed* de validação. Por fim, a consolidação dessa tecnologia  disruptiva culminará no mapeamento de normas regulatórias e no registro de  propriedade intelectual junto à AUSPIN, estruturando o ativo para futuros contratos de  licenciamento ou transferência de tecnologia com a indústria, reduzindo de forma  estratégica a dependência brasileira por estes tipos insumos médicos importados. Os  *phantoms* desenvolvidos durante a execução do projeto citado e suas provas-de conceito foram bem estabelecidas, mas com possíveis ajustes, como descrito a seguir.  
● *Phantom* híbrido para tórax1 

Este *phantom* foi projetado e construído como um protótipo composto por árvore  traqueobrônquica e parênquima pulmonar, o qual permitiu a realização de testes com  inserção de nódulos sólidos e de opacidade em vidro fosco (GGO) em tomógrafos  convencionais e de contagem de fótons (processo 2023/03945-8). Esse modelo também  contou com um ensaio exploratório bem-sucedido utilizando espuma de poliuretano  (PU) para simular o parênquima (Figura 1). Como melhorias propostas, o *phantom* 

*![][image1]![][image2]Figura 2 **\-** Segmentação de um novo modelo antropomórfico de tórax (a)*  

*Figura 1 \- Aquisição tomográfica do phantom  antropomórfico de tórax, Freddie, em sua configuração  original. (b) Ensaio exploratório com espuma de poliuretano  (PU) como material simulador do parênquima pulmonar.*   
*cortes axiais de tomografia computadorizada com segmentação das  principais estruturas torácicas (b) reconstruções, evidenciando a distribuição  espacial da anatomia interna e da arborização vascular. (c) reconstrução das  costelas e coração (d) reconstrução das vias aéreas e rede vascular.* 

existente será modificado com a incorporação definitiva da espuma de PU como  preenchimento fixo do pulmão e serão adicionadas novas estruturas anatômicas — como costelas e um coração — para elevar o realismo do simulador (Figura 2). Além  disso, novos nódulos pulmonares com morfologias variadas serão projetados e  impressos em 3D com possibilidade de serem agregadas propriedades radiômicas aos  estudos de detectabilidade.  

● *Phantom* híbrido de abdome 

As atividades previstas para esta etapa incluem a caracterização de materiais que  atendam aos requisitos de densidade, espectro de atenuação e número CT, permitindo  o preenchimento das estruturas já impressas (Figura 3\) e a realização de estudos de  detectabilidade voltados a patologias abdominais frequentes. Serão avaliados  diferentes protocolos de aquisição, fabricantes de tomógrafos e intercorrências clínicas  

1 Este é o *phantom* mais testado dos três. Seu processo de validação foi publicado no artigo COSTA, P. R., *et al*. 2025\.  Hybrid phantom for lung CT: Design and validation. *Medical Physics,* 52\.   
simuladas. Também, pretende-se ampliar o número de estruturas anatômicas  simuladas, seguindo a metodologia já desenvolvida, além de realizar estudos com a  parte maciça do *phantom* híbrido (Figura 4\) para investigar a influência da quantidade  de material e do nível de contraste na detectabilidade das estruturas, considerando  apenas parâmetros físicos das imagens adquiridas. 

![][image3]  
*Figura 3 – (a) Segmentações anatômicas realizadas e refinadas no software 3D Slicer; (b) Modelos em formato STL preparados para  impressão 3D, juntamente com os respectivos materiais selecionados; (c) Estruturas impressas prontas para utilização e  preenchimento: (A) Rim direito; (B) Rim esquerdo; (C) Porção inferior do fígado; (D) Coluna vertebral; (E) Estrutura elíptica utilizada  como base do phantom.* 

*![][image4]*  
*Figura 4 – (a) Esquema representando a base para o phantom elíptico para estudos da região abdominal; (b) o dispositivo oco usinado  em polietileno de ultra alto peso molecular (UHMW); (c) phantom elíptico maciço usinado no mesmo material e dimensões do  primeiro protótipo, a fim de estudos de métricas de detectabilidade.*  

● *Phantom* híbrido de cabeça 

A metodologia de fabricação deste simulador já se encontra consolidada, tendo sido  realizada a impressão 3D da calota e da base do crânio (Figura 5), além da confecção de  seis lesões simulando meningiomas com resina epóxi dopada com óxido de magnésio  (MgO). Essas estruturas foram acomodadas dentro de um parênquima cerebral  simulado com resina epóxi pura e validadas clinicamente por radiologistas (Figura 6). As  melhorias propostas para esta fase consistem no aprimoramento da polimerização da  resina epóxi por meio de desgaseificação em vácuo, visando eliminar microbolhas e  artefatos de imagem. Adicionalmente, serão aplicadas métricas de física médica para  avaliar resoluções de baixo contraste e será desenvolvida uma nova geração do  simulador encefálico via modelagem 3D para reproduzir macroestruturas cerebrais   
complexas, permitindo pesquisas voltadas a novas manifestações clínicas, vasculares,  radiologia intervencionista e técnicas de subtração.  

![][image5]  
*Figura 5 – Etapas da manufatura aditiva das peças simulantes do tecido ósseo do crânio, incluindo impressão, modelos com suporte  e resultado final após refinamento manual.* 

*![][image6]![][image7]![][image8]![][image9]![][image10]Figura 6 –Modelo finalizado da calota craniana com destaque para os locais de inserção: simulante S1 (20mm) sob o osso clivo,  simulante S2 (30mm) sob o osso esfenóide e insert régua na região cerebelar. Modelo finalizado da calota craniana com destaque  para os locais de inserção: simulantes S3 (40mm) e S4 (50mm) sob a convexidade e simulante S5 (60mm) na região parassagital.* 

**Desenvolvimento do *software* com ferramentas de IA para otimização de  procedimentos de TC** 

**DESAFIO: Prover aos profissionais que participam de programas de otimização de  protocolos de tomografia computadorizada de ferramenta computacional baseada  em IA para adequação dos parâmetros técnicos e de reconstrução de imagens que  combinem baixas doses com qualidade de imagens clinicamente adequadas** 

**MEIOS E MÉTODOS PARA SUPERÁ-LOS:** 

Será desenvolvida uma ferramenta computacional que viabilize a sistematização de  informações provenientes dos *phantoms* híbridos desenvolvidos e que proponha  protocolos otimizados para TC de tórax, abdome e crânio. A Figura 7 apresenta os blocos  operacionais básicos da ferramenta a ser desenvolvida. A operação prevista consiste nas  seguintes etapas  
i. Obtenção de imagens de um dado protocolo clínico utilizando um dos *phantoms* híbridos desenvolvidos considerando diferentes níveis de dose, padrões de  modulação de corrente, espessura de corte, *pitch*, tensão e métodos de  reconstrução de imagens; 

ii. Entrada das imagens obtidas com a configuração geométrica para cálculo das  métricas NPS, TTF e d´ de cada combinação de parâmetros; 

iii. Disponibilização das imagens obtidas com a configuração antropomórfica em  estações de trabalho, para avaliação subjetiva de detectabilidade por  observadores humanos. 

Os resultados dos itens ii e iii serão integrados por meio de ferramentas estatísticas e  métodos de aprendizado de máquina, visando estabelecer modelos preditivos que  relacionem os parâmetros de aquisição e reconstrução às métricas de detectabilidade,  dose e desempenho humano. A partir dessa modelagem, será possível explorar o  conjunto de protocolos avaliados e identificar combinações que apresentem melhor  compromisso entre preservação da detectabilidade e redução da dose, contribuindo  para a seleção de protocolos candidatos à aplicação clínica.  

![][image11]  
*Figura 7 – Estrutura básica do software a ser desenvolvido e validado para aplicações utilizando os  phantoms híbridos propostos.*  
Otimizar protocolos exige equilibrar a menor dose possível com a qualidade diagnóstica.  Correlacionar métricas físicas (NPS, TTF, d') com a percepção humana subjetiva (ROC,  AUC) para treinar o *software* sem gerar sobreajuste de dados é altamente complexo  (Shunhavanich et al., 2024, Shekter, 2020, Zhou et al., 2019, Tseng et al., 2016). Esse  problema será superado por um estudo-piloto, a ser realizado no InRad (HCFMUSP),  conforme descrito no próximo item. A variação de parâmetros nos sete tomógrafos de  diferentes fabricantes da instituição gerará um vasto *dataset* que, validado pelas  avaliações de radiologistas especialistas e físicos médicos, treinará os algoritmos de  *Machine Learning* propostos.  

O processo de modelagem estatística e aprendizado de máquina seguirá os seguintes  passos:  

Organização dos Protocolos:  

Define-se o conjunto de protocolos a serem avaliados por:  

onde cada θi é uma combinação específica dos parâmetros de aquisição/reconstrução:    
Para cada protocolo, estão associados o d′ calculado, a dose (CTDIvol) e, quando possível,  o índice de detectabilidade obtido através de estudos observacionais (d′obs). Este  conjunto de informações irá estabelecer uma base de dados tabular.  

Modelagem Preditiva com Aprendizado de Máquina 

A partir da base de protocolos construídos, serão avaliados modelos estatísticos e de  aprendizado de máquina (como um problema de aprendizado supervisionado) para  estabelecer modelos preditivos que relacionam os protocolos de máquina e  reconstrução com a detectabilidade (HASTIE, et al., 2009). Entre os métodos  inicialmente considerados estão: regressão regularizada, árvores de decisão, *random  forests*, *gradient boosting* e modelos baseados em processos gaussianos.  

De forma geral, a modelagem buscará estabelecer relações do tipo:   
Para os protocolos avaliados por observadores humanos, também poderá ser  investigada a relação entre as métricas objetivas e o desempenho observacional, por  exemplo:

Essa etapa tem como objetivo identificar padrões multivariados, avaliar a influência  relativa dos parâmetros técnicos e investigar possíveis interações entre eles.  

Dessa forma, a modelagem preditiva fornecerá suporte para a exploração sistemática  do conjunto de protocolos avaliados e para futura seleção de combinações com melhor  compromisso entre detectabilidade e dose.  

Tarefa de Otimização e Definição de Conjunto Candidato Ampliado: 

A seleção dos protocolos candidatos será formulada como um problema de otimização  multiobjetivo, no qual se busca simultaneamente maximizar a detectabilidade e  minimizar a dose. Para isso, será utilizada o formalismo da fronteira de Pareto,  permitindo identificar o conjunto de protocolos não dominados no plano dose– detectabilidade, isto é, combinações para as quais não exista outro protocolo com  desempenho simultaneamente superior em termos de dose e detectabilidade (DEB et  al., 2002).  

Esquematicamente\, dado θi ∈ Θ\, da base tabular determinada, pode-se estabelecer a  seguinte relação:

um protocolo é tido como dominado se existir θj tal que d′i ≤ d′j e Dj ≤ Di com pelo menos  uma dessas desigualdades sendo estritas. 

Considerando o contexto experimental e que pequenas flutuações na  detectabilidade/dose podem não representar diferenças clínicas relevantes, será adotado com um conjunto candidato ampliado usando o conceito de ��\-dominância (um  elemento é tido se existir θj tal que �� \- dominado se Dj ≤ Di \- �� e d′i \+ �� ≤ d′j).  
Dessa forma, pode-se encontrar um algoritmo para determinação de protocolos com  maior relevância clínica, considerando incertezas experimentais, contidos no conjunto  de protocolos estudados.  

Validação e Calibração com observadores reais:  

Os resultados obtidos por observadores humanos serão utilizados como etapa de  validação e calibração da ferramenta. A comparação entre o d' e métricas derivadas das  avaliações humanas, como AUC, permitirá investigar em que medida as métricas  objetivas de detectabilidade são compatíveis com o desempenho observado em tarefas  de detecção (Solomon and Samei, 2016). Dessa forma, os dados provenientes de  observadores humanos poderão ser utilizados para avaliar a coerência do  ranqueamento dos protocolos, identificar faixas de detectabilidade associadas ao desempenho observacional real e refinar a seleção dos protocolos candidatos.  

Para garantir que o algoritmo generalize de forma adequada, o modelo será alimentado  pelo robusto *dataset* controlado gerado no estudo-piloto do InRad utilizando técnicas  de validação cruzada para correlacionar métricas físicas com as avaliações humanas. No  aspecto da infraestrutura, a interoperabilidade e a incorporação segura no PACS,  frequentemente, encontram restrições de *firewall* e nas exigências da LGPD. Para  contornar isso, o *software* atuará de forma a processar as imagens e extrair os  metadados localmente, sem risco à rede principal do hospital. Já a praticidade para uso  na rotina clínica e em programas de controle de qualidade, que costuma ser prejudicada  por análises manuais exaustivas, será resolvida por meio da visão computacional. O  *software* realizará a detecção automática de bordas e demarcará as ROIs sem  intervenção humana, gerando relatórios instantâneos. Por fim, o desafio da  generalização entre tomógrafos de diferentes fabricantes e modelos, que utilizam  algoritmos de reconstrução proprietários, será superado através da padronização pelo  resultado. A Inteligência Artificial será calibrada pelo d’, indicando qual configuração  específica de cada máquina atinge o nível de detectabilidade necessária com a menor  dose de radiação possível, para o conjunto de casos clínicos que serão estudados.  
**Validação do *software* e aplicação-piloto no INRAD do HCFMUSP**  

**DESAFIO: Garantir que os *phantoms* híbridos e o software desenvolvido operam  adequadamente e apresentam respostas que permitem aprimorar os protocolos de  tomografia computadorizada** 

**MEIOS E MÉTODOS MARA SUPERÁ-LOS:** 

O *software* descrito no item anterior será validado por meio de um estudo-piloto no  Instituto de Radiologia do Hospital das Clínicas da FMUSP (INRAD), instituição que conta  com sete tomógrafos dos quatro principais fabricantes, mantidos sob rigoroso controle  de qualidade há mais de duas décadas. O projeto já possui aprovação do Comitê de Ética  em Pesquisa (CAAE: 27.912.619.6.0000.0068), e nenhuma irradiação experimental em  pacientes ocorrerá sem a devida anuência institucional. Essa implementação inicial visa  testar a resposta conjunta dos *phantoms* e do *software*, avaliando o custo-benefício do  processo e enfrentando o desafio da ampla variabilidade tecnológica dos métodos de  reconstrução proprietários. Para superar esse obstáculo, a metodologia adotará os  *phantoms* híbridos como um 'padrão-ouro' equalizador: em vez de unificar os  parâmetros de entrada das máquinas, o estudo mapeará exaustivamente o  comportamento das variáveis em cada equipamento. Ao vincular esses dados mapeados  ao d', o modelo computacional baseado em Inteligência Artificial aprenderá as  especificidades de cada algoritmo de reconstrução. Isso alimentará a versão final do  *software*, permitindo-lhe acelerar os processos de otimização em ambiente clínico real  e indicar — de forma personalizada e independente da marca/modelo do tomógrafo — a configuração ideal para garantir a qualidade diagnóstica com a menor dose possível.  Caso essa ferramenta computacional resulte em vantagens competitivas, o registro de  sua propriedade intelectual será solicitado através da AUSPIN, segundo o regramento  da FAPESP e das instituições participantes.  
**CRONOGRAMA DE EXECUÇÃO**

|  | Ano 1  |  | Ano 2  |  | Ano 3 |  |
| ----- | ----- | :---: | :---: | :---: | :---: | :---: |
| **Meses**  | **1-6**  | **7-12**  | **1-6**  | **7-12**  | **1-6**  | **7-12** |
| Finalização Phantom  Tórax |  |  |  |  |  |  |
| Finalização Phantom  Abdome |  |  |  |  |  |  |
| Finalização Phantom  Crânio |  |  |  |  |  |  |
| Desenvolvimento   *Software* e treinamento  da IA |  |  |  |  |  |  |
| Testes dos phantoms e  melhorias nos projetos |  |  |  |  |  |  |
| Validação Piloto no   InRad |  |  |  |  |  |  |
| Registro de propriedade  intelectual na AUSPIN |  |  |  |  |  |  |
| Publicações |  |  |  |  |  |  |
| Relatórios |  |  |  |  |  |  |

**DESCRIÇÃO DAS ATIVIDADES DESENVOLVIDAS PELA EQUIPE** 

Paulo Roberto Costa \- Coordenação geral do projeto 

• Otimização de protocolos de TC e aprimoramento dos *phantoms* Edilaine Honório da Silva (Pesquisadora associada \- IFUSP) 

Wagner H. Marques (Aluno de Doutorado \- FMUSP) 

Pós-doutorando (a ser selecionado – IFUSP) 

• Desenvolvimento do *software* para otimização utilizando IA 

Alexandre Passos Suaide (Pesquisador Associado \- IFUSP) 

Alessandra Tomal (Pesquisadora associada – IFGW/Unicamp)) 

Márcio Sawamura (Pesquisador Associado – INRAD/HCFMUSP) 

Eduardo K. U. N. Fonseca (Pesquisador Associado – INCOR/HCFMUSP) Davi V. P do Amaral (Aluno de Mestrado \- IFUSP) 

Pós-doutorando (a ser selecionado – IFUSP) 

• Concepção e melhorias para o *phantom* de pulmão 

Márcio Sawamura (Pesquisador Associado – INRAD/HCFMUSP) 

Eduardo K. U. N. Fonseca (Pesquisador Associado – INCOR/HCFMUSP) Giovana Negro (Bolsista de IC – IFUSP) 

• Concepção e melhorias para o *phantom* de abdome 

Cinthia Ortega (Pesquisadora Associada – INRAD/HCFMUSP) 

Douglas R. Godoy (Bolsista de IC – IFUSP) 

• Concepção e melhorias para o *phantom* de cabeça 

Leandro T. Lucato (Pesquisador Associado – INRAD/HCFMUSP) 

Victor H. F. Oliveira (Bolsista de IC – IFUSP) 

• Desenvolvimento e Implementação de técnicas de manufatura aditiva Marcelo Oliveira (Pesquisador Associado – CTI Renato Archer) 

João Luiz Amaro (Pesquisador Associado – UNESP) 

Giovana Negro (Bolsista de IC – IFUSP) 

Victor H. F. Oliveira (Bolsista de IC – IFUSP) 

Douglas R. Godoy (Bolsista de IC – IFUSP) 

Pós-doutorando (a ser selecionado – IFUSP)  
• Implementação dos novos *phantoms* e do *software* para validações Denise Yanikian Nersissian (Pesquisadora associada \- IFUSP) 

Amanda Fernandes do Nascimento (Apoio Técnico \- IFUSP) 

Isaías Petroni (Apoio Técnico \- IFUSP) 

**DISSEMINAÇÃO E AVALIAÇÃO** 

Assim como ocorreu no desenvolvimento do protótipo do *phantom* de pulmão,  resultante dos projetos Fapesp anteriores (processos 2022/11457-0 e 2023/03945-8)2,  os dispositivos resultantes do presente projeto, bem como o programa de análise com  base em Inteligência Artificial, serão impulsionados para terem visibilidade junto ao  público geral, externo à academia. Além disso\, dadas as vantagens de que as inovações  propostas sejam conhecidas por radiologistas e físicos médicos, serão prospectadas  parcerias com a iniciativa privada para demonstrações dos dispositivos em feiras que  acompanham eventos tais como a Jornada Paulista de Radiologia e o Congresso  Brasileiro de Física Médica.  

Além das publicações dirigidas para o público geral, são esperadas submissões de, no  mínimo, 2-3 artigos científicos para revistas indexadas, apresentando as inovações  decorrentes tanto dos desenvolvimentos quanto das aplicações dos dispositivos e do  *software* a ser criado.  

**OUTROS APOIOS** 

Parte dos recursos a serem utilizados no desenvolvimento do presente projeto já foram  adquiridos com apoio da Fapesp no processo 2022/11457-0. Além disso, o proponente  é Bolsista de Produtividade Desenvolvimento Tecnológico e Extensão Inovadora do  CNPq \- Nível 2 em uma área correlata à presente proposta e parte de sua reserva técnica  também é utilizada para os desenvolvimentos propostos. 

Em termos de infraestrutura, além daquelas já existente na Instituição Sede, o projeto  conta com o apoio formal do LAPRINT/CTI Renato Archer. Este laboratório é  

2 Ver links das seguintes reportagens:    
Jornal Fala Brasil Jornal da USP Revista Fapesp  
especializado em técnicas de manufatura aditiva, com a instrumentação e corpo técnico  especializado para apoio aos desenvolvimentos propostos. Além desse laboratório, a  parceria com o Departamento de Especialidades Cirúrgicas e Anestesiologia da  Faculdade de Medicina da UNESP de Botucatu também permite a realização de  pesquisas inovadoras utilizando parte da infraestrutura de impressão 3D daquela  instituição. 

Para os desenvolvimentos computacionais propostos, além da expertise da equipe  participante desta etapa do projeto, conta-se com o apoio do InLab/InovaHC, que é o Centro de Pesquisa, Desenvolvimento e Inovação em Tecnologias Aplicadas à Saúde do  INRAD/HCFMUSP destinado a parceiros, pesquisadores, startups e desenvolvedores que  tenham ou queiram criar projetos de Inteligência Artificial (IA) voltados às melhorias e  soluções que abrangem diferentes etapas na jornada do paciente e na cadeia da saúde. 

Este laboratório de inovação conta com recursos de *hardware* e *software*, além de  recursos humanos especializados, que irão apoiar o desenvolvimento e a validação das  ferramentas computacionais previstas, incluindo o treinamento da rede neural. 

Por fim, como símbolo de engajamento e de forte interesse em empreendedorismo do  grupo\, desde maio de 2026, três membros da equipe estão conduzindo um trabalho  dentro da 1ª temporada do Programa SEBRAE SuperNova, competindo com equipes de  todo o Brasil, em busca do prêmio de melhor projeto apresentado (Pitch \+ Canvas), em  uma área temática compatível com a proposta do presente projeto.  
**Bibliografia** 

BEN ALAYA, I., FELHI, F., MESSELMANI, M. & LABIDI, S. 2026\. Advancing Stroke Diagnosis: A  Comprehensive Review of Artificial Intelligence in Detecting Early Ischemic Changes on  Noncontrast CT (NCCT). *Academic Radiology,* 33**,** 1060-1069. 

COSTA, P. R., BOISET, G. R., PIMENTA, E. B., ROCHA, R. M. V., MOURA, R. A. S., MARQUES, W. H.,  OOSTVEEN, L. J., GEURTS, B., SAWAMURA, M. V. Y., NERSISSIAN, D. Y., YOSHIMURA, E.  M. & SECHOPOULOS, I. 2025\. Hybrid phantom for lung CT: Design and validation.  *Medical Physics,* 52**,** e17990. 

GIANSANTE, L., MARTINS, J. C., NERSISSIAN, D. Y., KIERS, K. C., KAY, F. U., SAWAMURA, M. V. Y.,  LEE, C., GEBRIM, E. M. M. S. & COSTA, P. R. 2019\. Organ doses evaluation for chest  computed tomography procedures with TL dosimeters: Comparison with Monte Carlo  simulations. *Journal of applied clinical medical physics,* 20**,** 308-320. 

MILOS, R. I., RÖHRICH, S., PRAYER, F., STRASSL, A., BEER, L., HEIDINGER, B. H., WEBER, M.,  WATZENBOECK, M. L., KIFJAK, D., TAMANDL, D. & PROSCH, H. 2023\. Ultrahigh Resolution Photon-Counting Detector CT of the Lungs: Association of Reconstruction  Kernel and Slice Thickness With Image Quality. 

OECD 2025\. *Health at a Glance 2025: OECD Indicators* , Paris,. OECD Publishing. PARK, J. A.-O., SHIN, J. A.-O., MIN, I. A.-O., BAE, H. A.-O., KIM, Y. A.-O. & CHUNG, Y. A.-O. 2022\.  Image Quality and Lesion Detectability of Lower-Dose Abdominopelvic CT Obtained  Using Deep Learning Image Reconstruction. 

PIMENTA, E. B. & COSTA, P. R. 2025\. Model observers and detectability index in x-ray imaging:  historical review, applications and future trends. *Physics in Medicine & Biology,* 70\. POZZESSERE, C. A.-O., VON GARNIER, C. & BEIGELMAN-AUBRY, C. 2023\. Radiation Exposure to  Low-Dose Computed Tomography for Lung Cancer Screening: Should We Be Concerned? SAMEI, E., BAKALYAR D., BOEDEKER K. L., BRADY S., FAN J., LENG S., MYERS K. J., POPESCU L. M.,  RAMIREZ G. J. CARLOS, R. F., SOLOMON J., VAISHNAV J., WANG J. 2019\. Performance  evaluation of computed tomography systems: Summary of AAPM Task Group 233\.  *Medical Physics,* 46**,** e735-e756. 

SHEKTER, D. H. A. S. F. W. 2020\. *Efficiently calculating ROC curves, AUC, and uncertainty from  2AFC studies with finite samples , booktitle \= Medical Imaging 2020: Image Perception,  Observer Performance, and Technology Assessment*. 

SHUNHAVANICH, P., MEI, K., SHAPIRA, N., STAYMAN, J. W., MCCOLLOUGH, C. H., GANG, G.,  LENG, S., GEAGAN, M., YU, L., NOËL, P. B. & HSIEH, S. S. 2024\. 3D printed phantom with  12 000 submillimeter lesions to improve efficiency in CT detectability assessment. *Med  Phys*. 

SOLOMON, J. & SAMEI, E. 2016\. Correlation between human detection accuracy and observer  model-based image quality metrics in computed tomography. *J Med Imaging  (Bellingham),* 3**,** 035506\. 

TSENG, H. W., FAN, J. & KUPINSKI, M. A. 2016\. Design of a practical model-observer-based image  quality assessment method for x-ray computed tomography imaging systems. *J Med  Imaging (Bellingham),* 3**,** 035503\. 

UNSCEAR 2022\. Evaluation of medical exposure to ionizing radiation. *2020/2021 Report.* New  York: United Nations: United Nations Scientific Committee on the Effects of Atomic  Radiation. 

ZHOU, W., LI, H. & ANASTASIO, M. A. 2019\. Approximating the Ideal Observer and Hotelling  Observer for Binary Signal Detection Tasks by Use of Supervised Learning Methods. *IEEE  Trans Med Imaging,* 38**,** 2456-2468.
  
 PROJETO DE MESTRADO

GDRFM-IFUSP

Desenvolvimento de ferramentas para análise das imagens utilizando observadores computacionais

ORIENTADOR: Prof. Dr. Paulo Roberto Costa – IFUSP

CANDIDATO: Davi Vasconcelos Pacheco do Amaral

Novembro/2025

# **Sumário** {#sumário}

[Sumário 2](#sumário)

[Resumo 3](#resumo)

[Introdução 5](#introdução)

[Objetivos 8](#objetivos)

[Metodologia 9](#metodologia)

[1\. Dados experimentais 9](#dados-experimentais)

[2\. Pré-processamento e amostragem de ROIs 10](#pré-processamento-e-amostragem-de-rois)

[3\. Estimativas de  TTF, NPS, filtro ocular E(f) e WTASK(f): 11](#estimativas-de-ttf,-nps,-filtro-ocular-e\(f\)-e-wtask\(f\):)

[4\. Observadores-modelo 12](#observadores-modelo)

[5\. Validação e incerteza 13](#validação-e-incerteza)

[6\. Implementação 13](#implementação)

[Resultados esperados 15](#resultados-esperados)

[Cronograma de Execução 16](#cronograma-de-execução)

[**Bibliografia: 18**](#bibliografia:)

# **Resumo** {#resumo}

A avaliação da qualidade de imagens médicas, em tempos recentes, vem se desvinculando de uma avaliação puramente física das imagens e cada vez mais se aproximando de métricas “task-based”, nas quais a qualidade da imagem é quantificada pela capacidade de observadores detectarem estruturas de interesse associadas a uma tarefa específica. Neste contexto, o “índice de detectabilidade” e “observadores modelo” tornam-se ferramentas relevantes para a comparação de protocolos e sistemas de aquisição; algoritmos de reconstrução e avaliações de redução de dose mais precisas, em especial no contexto de tomografia computadorizada.

Este projeto de mestrado tem por objetivo desenvolver e validar ferramentas computacionais para a análise de imagens usando modelos observacionais, focando principalmente na estimativa do índice de detectabilidade em *phantoms* de tórax antropomórficos em baixa dose. A proposta busca sedimentar o entendimento de métodos já aplicados comumente em *phantoms* geométricos no contexto dos *phantoms* antropomórficos, além de desenvolver novas ferramentas em um contexto volumétrico \- muito relevante para tomografias computadorizadas.

Para atingir estes objetivos, serão utilizadas imagens de phantoms de tórax antropomórficos adquiridas em tomógrafos clínicos, em diferentes condições de dose e utilizando diferentes algorítmos de reconstrução. Sobre esses dados serão aplicados procedimentos de pré-processamento e amostragem de ROIs, estimação de métricas relevantes (TTF, NPS) e implementação de observadores modelo, focando majoritariamente no modelo NPWE para estabelecimento dos parâmetros de detectabilidade dos nódulos. O desempenho dos observadores modelo será comparado com leituras de observadores humanos em experimentos do tipo 2AFC, permitindo assim, validar a coerência entre os modelos teóricos e o desempenho real humano na tarefa de detecção.

Espera-se que o projeto resulte não somente em uma ferramenta computacional reprodutível para estimar o índice de detectabilidade em tarefas de detecção em contextos antropomórficos, mas também em uma melhor compreensão da validade e das limitações do uso de observadores-modelo e do índice de detectabilidade como métricas task-based em tomografia computadorizada. Contribuindo, portanto, para a otimização de protocolos, comparação de algoritmos de reconstrução e futura incorporação de métricas task-based em rotinas de controle de qualidade.

# **Introdução** {#introdução}

O equilíbrio entre qualidade de imagem e doses empregadas em procedimentos de tomografia computadorizada utilizando ferramentas estatísticas sofisticadas como o índice de detectabilidade tem sido tema de trabalhos recentes28,29. Este projeto propõe o desenvolvimento e validação de uma ferramenta computacional baseada em observadores modelo para quantificar o índice de detectabilidade de objetos em imagens médicas obtidas em diferentes modalidades e protocolos.   
Conceitualmente, o índice de detectabilidade1 (d′) é uma métrica “task‑based”2 (baseada na realização de uma tarefa pelo observador)  que quantifica a separação entre as distribuições da variável‑resposta do observador para os conjuntos sinal‑presente e sinal‑ausente.3 Na prática, esta grandeza está associada à relação sinal‑ruído dessa variável de decisão. Quanto maior d′, melhor a capacidade de detecção para a tarefa definida.  
Tal índice tem sido aplicado em imagens médicas para integrar métricas objetivas com avaliações subjetivas, pois considera tanto as propriedades do processamento de imagem quanto limitações do sistema visual humano4, melhorando assim a eficácia clínica das tecnologias de imagem.  
O cálculo5 de d′ se dá pela utilização de observadores-modelo do tipo *Ideal Observer* (IO), *Hotelling Observer* (HO), *Channelized Hotelling Observer* (CHO), *non-pre-whitening model* (NPW) e *non-pre-whitening model with eye filter* (NPWE) — modelagens matemáticas distintas do “observador”6,7. O mais usualmente empregado e recomendado pela Associação Americana de Física Médica (AAPM)1 é o NPWE.  
O NPWE8 é calculado no espaço de frequências. Para tal\, define-se uma função tarefa WTASK(f) (associada ao sinal a ser detectado), TTF(f) (*task transfer function* \- função associada a resolução do sinal), NPS(f) (*noise power spectrum* \- densidade espectral de potência do ruído) e E(f) (função que modela a sensibilidade espacial do sistema visual humano). Com isso, o cálculo de d′ se torna, nesse contexto 2-dimensional: 

![][image1]

Tal modelo é amplamente utilizado em tomografias computadorizadas por combinar TTF/NPS com um filtro de sensibilidade visual E(f).Em cenários clínicos controlados, têm mostrado correlação significativa com a área sob curvas ROC (*receiver operating characteristics*), AUC (*área under the curve*) resultantes de experimentos com observadores humanos ao comparar protocolos e métodos de reconstruções de imagens9. A AUC tem sido adotada como um parâmetro quantitativo importante para medir o desempenho de dispositivos de imagem médica (hardware e software), tendo forte correlação com aspectos estatísticos inerentes da qualificação destas imagens.  
Ao fornecer uma única métrica que captura múltiplos aspectos da qualidade da imagem, o índice de detectabilidade oferece uma avaliação abrangente de imagens clínicas. Numerosas aplicações deste índice em diversas áreas da imagem médica estão documentadas na literatura10,11, juntamente com recomendações para seu uso em avaliações periódicas de desempenho de dispositivos de imagem.  
Do ponto de vista prático, a qualidade de imagem em *phantoms* antropomórficos tem sido tradicionalmente avaliada por estudos observacionais com especialistas que executam tarefas específicas (detecção/identificação de nódulos) sob protocolos variados. Embora clinicamente relevantes, esses estudos são custosos (tempo de leitura, recrutamento e treinamento dos observadores), podem sofrer de variabilidade inter/intra-observador12 e exigem tamanhos amostrais elevados \- que por sua vez, podem acarretar no aumento do risco de falsos positivos13.  
O d′, estimado via observadores-modelo, surge como alternativa complementar para agilizar e padronizar essa avaliação, calculando por meio de dados presentes na “imagem”, uma estimativa da visibilidade/realizabilidade da tarefa14. Portanto, fornece uma métrica *task-based* objetiva, reprodutível e mais econômica, permitindo considerar múltiplos fatores (dose, método de reconstrução, textura do ruído etc) com rapidez.   
 No entanto, como diferentes modalidades5 de imagem podem requerer diferentes índices de detectabilidade, é crucial avaliar a adequação das propriedades da imagem sendo analisada e daquelas do índice adotado. Além disso, o uso de d′ é consolidado em *phantoms* simples1 (*phantom* com geometria elementar e propriedades homogêneas, contendo alvos artificiais bem controlados e sem texturas ou estruturas anatômicas). Porém, há incerteza acerca de sua aplicabilidade/validação em *phantoms* antropomórficos5 e utilização em contextos 3-dimensionais (volumétricos) \- o que é crítico no contexto de tomografias.  
O projeto aborda essas lacunas ao avaliar d′ em cenários antropomórficos e investigar possíveis extensões 3D do modelo. Para isso, o projeto propõe a integração de dados simulados e experimentais de *phantoms* antropomórficos, a fim de agilizar e padronizar a avaliação de qualidade de imagem e dar suporte à otimização de protocolos e o controle de qualidade em tomografia computadorizada.  
Portanto, um entendimento aprofundado desta métrica, incluindo sua natureza estatística e complexa relação com observadores modelo, é essencial para garantir sua aplicação e interpretação corretas, e para prevenir usos inadequados.   
O fluxo de trabalho deverá integrar o aperfeiçoamento teórico das ferramentas matemáticas associadas ao d′, checagem/validação dos métodos no contexto dos *phantoms* antropomórficos em imagens de tomografia computadorizada (por meio de estudos observacionais do estilo 2AFC \- *two-alternative forced choice15*,16) e o desenvolvimento de ferramenta computacional capaz de realizar o cálculo de d′ para otimização de protocolos e controle de qualidade. 

# **Objetivos** {#objetivos}

Desenvolver e validar uma metodologia reprodutível para estimar o índice de detectabilidade, d′, em imagens tomográficas 2D e 3D. 

Objetivos específicos

1. Implementar NPWE (principal) e CHO/HO(NPW) (comparativos) para tarefas de detecção definidas (2D).

2. Estimar TTF, NPS, filtro ocular E(f) e WTASK(f) em contextos antropomórficos. 

3. Avaliar sensibilidade de d′ a diferentes protocolos \- dose, kernel de reconstrução, tamanho/contraste do alvo e textura/inomogeneidade do ruído.

4. Investigar estratégias 3D: NPWE 3D

5. Validar contra leituras humanas de estudos observacionais e quantificar incerteza.

6. Entregar software reprodutível, relatórios e guias de uso aderentes ao AAPM/TG-233.

# **Metodologia** {#metodologia}

1. ## **Dados experimentais** {#dados-experimentais}

Serão utilizados conjuntos de imagens CT de um *phantom* antropomórfico30,[^1] de tórax adquiridos previamente, em regimes de baixa dose, pelo grupo de Dosimetria e Física Médica da USP. Tal região foi escolhida devido a sua alta complexidade estrutural (parênquima pulmonar) e alto ruído anatômico17, tornando as tarefas de detecção em baixo contraste mais desafiadoras8. 

Tais dados incluem conjuntos tomográficos completos, variando: tecnologias de detectores (EICT – energy integration e PCCT – photon counting), kernel de convolução (FC51, FC52 e LUNG), algoritmo de reconstrução (AICE e AIDR), método de filtragem (Cu e Al) e a dose (valores de CTDIvol 0,3 à 2,8 mGy).  As imagens tomográficas já foram adquiridas no Radboudumc, Holanda\, durante pesquisa no exterior realizada pelo orientador do candidato (Bolsa Fapesp/BPE – processo 2023/03945-8).

A utilização de um *phantom* antropomórfico, em vez de um geométrico usual, permite incorporar de forma mais realista o ruído anatômico e estrutural na tarefa de detecção. Os nódulos escolhidos para a análise variam em densidade (vidro fosco, sólidos e sub-sólidos), tamanho e localização, sendo inseridos em um fundo anatomicamente realista. Nesses contextos, a não-linearidade e a heterogeneidade do fundo exercem forte influência sobre a textura do ruído e sobre a própria detectabilidade do sinal\, de maneira análoga ao que ocorre em pacientes reais.

Assim, é possível definir tarefas de detecção bem especificadas, em linha com a abordagem task-based18 recomendada em documentos como o relatório TG-2331 da AAPM e em revisões recentes4,7 sobre observadores-modelo e índice de detectabilidade. Além disso, a disponibilidade de múltiplos protocolos de aquisição para um mesmo *phantom* permite a comparação direta da detectabilidade entre diferentes combinações de variáveis (aparelho, kernel de convolução, algoritmo de reconstrução, método de filtragem e dose).

2. ## **Pré-processamento e amostragem de ROIs** {#pré-processamento-e-amostragem-de-rois}

Primeiramente\, deve-se garantir que as imagens sejam expressas em unidades de frequência espacial em ciclos·mm⁻¹, a partir dos espaçamentos de pixel/voxel registrados nos cabeçalhos DICOM. Tal cuidado permite consistência nas análises tanto em 2D quanto em 3D e em diferentes protocolos. Além disso, uma normalização básica de intensidade sobre as imagens\, de modo a facilitar a comparação entre condições de dose e algoritmos de reconstrução \- ambas se alinham com as recomendações do relatório TG-233 da AAPM1.  
A textura do ruído é uma das características que mais afetam a tarefa de detecção; tal grandeza pode ser quantificada através do cálculo do Noise Power Spectrum (NPS)19. A estimação do NPS pressupõe a hipótese de quase-estacionariedade do ruído em regiões locais; portanto, serão selecionadas ROIs em áreas aparentemente homogêneas do *phantom* , evitando estruturas anatômicas.

Sendo I(x,y) a função de intensidade do sinal, o cálculo 2D do NPS20 segue a seguinte relação: 

![][image2]

Na prática, para imagens discretas, o NPS 2D será estimado a partir de um *ensemble* de ROIs de fundo aproximadamente estacionárias. Para cada ROI, subtrai-se a média​ e aplica-se a transformada de Fourier bidimensional; o NPS estimado é então obtido como

![][image3]  
Quando necessário, será aplicado *detrending* (remoção de planos ou polinômios de baixa ordem) antes da transformada de Fourier, seguindo metodologias clássicas de análise de NPS em sistemas de raios X e tomografia computadorizada1.  
As ROIs destinadas ao cálculo de d′ serão amostradas de forma estratificada em duas classes principais: (i) sinal-presente, contendo o nódulo alvo totalmente incluído, e (ii) sinal-ausente, contendo apenas fundo anatomicamente semelhante, na mesma região do *phantom*. Nos casos 3D, serão definidos volumes de interesse (VOIs) com dimensões compatíveis com o tamanho dos nódulos e com o campo de visão relevante para a tarefa, garantindo consistência. O dimensionamento das ROIs/VOIs seguirá recomendações1,21 da literatura sobre observadores-modelo e métricas *task-based* adaptadas para o contexto de *phantoms* antropomórficos. A Figura 1 mostra um exemplo ilustrativo de amostragem de ROIs/VOIs realizado no software IMQuest (Duke University)22.

![][image4]![][image5]  
**Figura 1 –** Exemplo de amostragem de ROIs de fundo para cálculo de NPS (esquerda) e ROI sinal-presente para cálculo de TTF (direita) no software IMQuest

3. ## **Estimativas de  TTF, NPS, filtro ocular E(f) e WTASK(f):** {#estimativas-de-ttf,-nps,-filtro-ocular-e(f)-e-wtask(f):}

A *Modulation Transfer Function* (MTF)5,22 é uma importante métrica para determinação da resolução espacial do sistema, quantificando a recuperação de contraste do sistema em função da frequência espacial. Matematicamente temos19   
![][image6]   
ou seja, a transformada de Fourier da resposta do sistema a um objeto linear (função de espalhamento em linha (LSF)). No entanto, equipamentos de CT modernos utilizam algoritmos de reconstrução não lineares, o que torna a MTF estritamente válida apenas como aproximação. Nesse contexto, é usual empregar a *task transfer function* (TTF), uma aproximação quase linear da resposta em frequência para um objeto e uma tarefa específica. A partir da MTF, a TTF será ajustada à geometria e ao tamanho dos nódulos considerados\, de modo a representar a resposta efetiva do sistema para a tarefa de detecção de baixo contraste24.  
 O NPS será utilizado em sua forma 2D ou 3D, conforme estimado na subseção anterior (a partir de *ensembles* de ROIs de fundo aproximadamente estacionárias e tomando a média sobre as ROIs). Nas análises 3D, quando viável, será utilizada média esférica sobre NPS(fx,fy,fz), em linha com *frameworks* clássicos21 de análise de NPS em imagens n-dimensionais.  
O filtro ocular E(f) será usado a fim de simular efeitos de desfocamento e sensibilidade de contraste em termos da magnitude da frequência espacial. Para tal, usaremos uma modelagem de um filtro banda-passa radial do modelo de Eckstein25  
![][image7]  
em que η é um fator de normalização e a1, a2, a3 controlam a banda de frequências em que o olho humano apresenta maior sensibilidade.   
 A função tarefa Wtask descreve o conteúdo espectral do sinal que diferencia as duas hipóteses consideradas pelo modelo observador: sinal-presente (nódulo), associada a uma função h1 correspondente a média das imagens com nódulo, e sinal-ausente  (apenas fundo), associada à uma função h2 correspondente à média das imagens sem nódulo26. A função tarefa é então definida como o módulo da transformada de Fourier da diferença entre essas duas hipóteses  
![][image8]

em que c(r) é o perfil de contraste do objeto em função da distância radial ao centro do nódulo que deve ser parametrizado de acordo com o tamanho e o contraste dos nódulos inseridos nos *phantoms* antropomórficos23. 

4. ## **Observadores-modelo** {#observadores-modelo}

   
Será adotado o observador NPWE (*non–prewhitening with eye filter*) como principal forma de estimar o índice de detectabilidade no domínio da frequência. Essa modelagem considera os efeitos visuais humanos ao avaliar a qualidade da imagem. Nesse modelo, as grandezas TTF(f), NPS(f), E(f) e Wtask(f) entram na expressão geral de d´ já apresentada na introdução.  
Como observadores comparativos, utilizaremos o observador de Hotelling (HO) e o observador de Hotelling canalizado (CHO). O HO pode ser visto como uma aproximação prática do observador ideal (IO) para sinais gaussianos: a decisão é baseada em um discriminante linear aplicado à imagem e é feita uma substituição da resposta ideal por uma combinação linear dos dados que maximiza a separação entre as hipóteses sinal-presente e sinal-ausente7. Assim, o HO serve como limite superior teórico para o desempenho de observadores humanos e de outros modelos lineares quando a matriz de covariância do ruído é conhecida.  
O observador de Hotelling canalizado (CHO) será utilizado como aproximação prática do HO em situações em que a estimação completa da matriz de covariância é inviável ou numericamente instável7. Neste modelo, projetam-se as imagens em um conjunto de canais pré-definidos (de forma análoga aos mecanismos de resposta de neurônios no córtex visual primário26), reduzindo a dimensionalidade do problema e permitindo uma aproximação prática do HO em fundos anatomicamente estruturados. Ao mesmo tempo, introduz uma redução do desempenho em relação ao HO “ideal”, refletindo limitações como a impossibilidade de *prewhitening* completo do ruído e aproximando-se mais do observador humano.   
Para cada combinação de protocolo de aquisição e algoritmo de reconstrução, o d′ estimado pelos modelos (NPWE, HO e CHO) será calculado a partir de *ensembles* de ROIs/VOIs sinal-presente e sinal-ausente, conforme descrito nas seções anteriores. Sempre que possível, esses resultados serão comparados ao desempenho de observadores humanos em experimentos 2AFC27\, dos quais também serão obtidos d′ e AUC(ROC)9, em analogia a estudos anteriores de validação de observadores-modelo em tomografia computadorizada.

5. ## **Validação e incerteza** {#validação-e-incerteza}

 Serão realizados estudos observacionais com leitores voluntários, utilizando o protocolo tradicional de 2AFC. As imagens (pares sinal-presente/sinal-ausente) serão apresentadas de forma randomizada e mascarada quanto ao protocolo de aquisição/reconstrução, e cada leitor indicará, para cada par, qual imagem contém o nódulo, podendo também registrar um grau de confiança. A partir dessas respostas estima-se a AUC(ROC) humana para cada protocolo, permitindo avaliar a correlação entre o desempenho humano e os valores de d´ previstos pelos observadores-modelo. A concordância entre leitores e entre protocolos será quantificada por meio do coeficiente de correlação intraclasse (ICC).  
Além disso\, de forma complementar, será também realizada uma tarefa 2AFC de comparação entre protocolos, na qual ambos os intervalos conterão nódulos reconstruídos em protocolos distintos. Nessa tarefa, os leitores deverão indicar em qual das duas imagens o nódulo se apresenta mais evidente e, a partir das frequências de escolha será possível a comparação direta entre os d´s calculados e o desempenho de observadores reais.   
 A incerteza associada aos estimadores de d´, AUC(ROC) e às métricas físicas (TTF, NPS) será quantificada por técnicas de *bootstrap* aplicadas aos *ensembles* de casos e de ROIs/VOIs, obtendo intervalos de confiança de 95% para cada protocolo avaliado \- aqui, assume-se que o número de voluntários seja suficiente para permitir tais métodos estatísticos.

6. ## **Implementação** {#implementação}

O software a ser desenvolvido será implementado em ambiente científico (Python) e organizado em módulos específicos para o cálculo de TTF, NPS, Wtask e observadores-modelo (NPWE, HO e CHO). Serão disponibilizados *notebooks* que contenham detalhamentos de como os cálculos são realizados e configurações que permitirão reproduzir combinações específicas de parâmetros relevantes. 

# **Resultados esperados** {#resultados-esperados}

Entregáveis técnicos

* Ferramenta NPWE 2D/3D e comparativos CHO/HO/PCM, com documentação e exemplos.  
   *Indicador:* repositório público/privado com notebooks executáveis e guia passo-a-passo.

* Relatórios com d′/AUC por cenário (tabelas e gráficos), mapas de decisão e intervalos de confiança.  
   *Indicador:* relatório por conjunto de dados.

Validação e desempenho

* Correlação d′ ↔ AUC humana quando disponível

* Reprodutibilidade intra-cenário (ICC ≥ 0,8)

* Sensibilidade: detectar mudanças coerentes de d′ com variações nos protocolos e concordância com resultados experimentais de observadores humanos. 

Aplicação 3D / Antropomórfica

* Investigação de NPWE 3D em protocolos de CT com *phantoms* antropomórficos.

# **Cronograma de Execução** {#cronograma-de-execução}

 Com base nas informações relatadas na seção anterior, é mostrado na Tabela 1 (Bimestres 1–6) e Tabela 2 (Bimestres 7–12) o cronograma a ser executado durante a realização deste projeto dividido em primeiro e segundo ano de atividades: 

Tabela 1: Cronograma primeiro ano de projeto

| Etapas | Bimestres: | 1 | 2 | 3 | 4 | 5 | 6 |
| :---- | :---- | ----- | ----- | ----- | ----- | ----- | ----- |
| Realização de disciplinas |  | x | x | x | x | x | x |
| Revisão bibliográfica |  | x | x | x | x |  |  |
| Dados experimentais |  |  | x | x | x |  |  |
| Pré-processamento & ROIs |  |  |  |  | x | x | x |
| TTF/NPS/E(f)/W\_task |  |  |  |  | x | x | x |
| Observadores-modelo |  |  |  |  | x | x | x |
| Validação e incerteza |  |  |  |  |  |  |  |
| Implementação |  |  |  |  |  |  |  |
| Submissão de artigos |  |  |  |  |  |  |  |
| Relatórios |  |  |  |  |  |  | x |
| Elaboração da dissertação |  |  |  |  |  |  | x |
| participação em congressos |  |  |  |  |  |  |  |

Tabela 2: Cronograma segundo ano de projeto

| Etapas | Bimestres: | 7 | 8 | 9 | 10 | 11 | 12 |
| :---- | :---- | ----- | ----- | ----- | ----- | ----- | ----- |
| Realização de disciplinas |  | x | x |  |  |  |  |
| Revisão bibliográfica |  |  |  |  |  |  |  |
| Dados experimentais |  |  |  |  |  |  |  |
| Pré-processamento & ROIs |  | x |  |  |  |  |  |
| TTF/NPS/E(f)/W\_task |  | x |  |  |  |  |  |
| Observadores-modelo |  | x |  |  |  |  |  |
| Validação e incerteza |  |  | x | x | x | x | x |
| Implementação |  |  | x | x | x | x | x |
| Submissão de artigos |  |  | x | x | x | x | x |
| Relatórios |  |  |  |  |  | x | x |
| Elaboração da dissertação |  |  |  |  | x | x | x |
| participação em congressos |  |  | x | x | x | x | x |

# Bibliografia:  {#bibliografia:}

1. **AAPM TG-233.** *Report of AAPM Task Group 233: task-based assessment of image quality using model observers (d′) in CT.* College Park (MD): American Association of Physicists in Medicine; **(2019)**.  
2. **Barrett H H, Myers K J, Hoeschen C, Kupinski M A and Little M P** 2015 Task-based measures of image quality and their relation to radiation dose and patient risk. *Phys Med Biol.* **2015**;60:R1–R75.  
3. **Tanner W P and Swets JA.**  A decision-making theory of visual detection. *Psychol Rev.* **1954**;61:401–409.  
4. **Abbey C K and Eckstein M P** Observer models as a surrogate to perception experiments. In: *The Handbook of Medical Image Perception and Techniques.* Cambridge: Cambridge University Press; **2018** p. 240–50  
5. **Pimenta EB, Costa PR.** Model observers and detectability index in x-ray imaging: historical review, applications and future trends. *Phys Med Biol.* 2025;70:07TR02.  
6. **Abbey C K and Bochud F O** Modeling visual detection tasks in correlated image noise with linear model observers. In: *Handbook of Medical Imaging.* Vol 1\. Bellingham (WA): SPIE Press; **2000**. p. 284–95  
7. **Barrett H H, Yao J, Rolland J P and Myers K J** Model observers for assessment of image quality. *Proc Natl Acad Sci U S A.* **1993**;90:9758–9765.  
8. **Burgess A E, Li X and Abbey C K** Visual signal detectability with two noise components: anomalous masking effects. *J Opt Soc Am A.* **1997**;14:2420–2432.  
9. **Solomon J and Samei E.** What observer models best reflect low-contrast detectability in CT? *Proc SPIE.* **2015**;9416:94160I.  
10. **Lévêque L, Outtas M, Liu H and Zhang L.** 2021 Comparative study of the methodologies used for subjective medical image quality assessment Phys. Med. Biol. 66 15TR02.  
11. **Greffier J, Frandon J, Si-Mohamed S, Dabli D, Hamard A, Belaouni A, Akessoul P, Besse F, Guiu B, Beregi J-P.** Comparison of two deep learning image reconstruction algorithms in chest CT images: a task-based image quality assessment on phantom data. *Diagn Interv Imaging*. **2022**;103(1):21–30.  
12. **Hernandez AM, Chen AF, Sen F, Mitchell AS, McKenney SE, Nardo L, et al.** A multireader, multicase study comparing ultra-high-resolution and conventional-resolution computed tomography for lung nodule characterization. *J Clin Imaging Sci.* **2025**;15:25. doi:10.25259/JCIS\_17\_2025.  
13. **Long N Mand Smith CS** Causes and imaging features of false positives and false negatives on 18F-PET/CT in oncologic imaging. *Insights Imaging.* **2011**;2:(2 679–98).  
14.  **Krupinski E A** 2021 The important role of task-based model observers and related techniques in medical imaging J. Nucl. Cardiol. 28 638–40.  
15. **Chakraborty DP.** *Observer Performance Methods for Diagnostic Imaging: Foundations, Modeling, and Applications.* Boca Raton: CRC Press; 2006\.  
16. **Samei E and Richard S** Assessment of the dose reduction potential of a model-based iterative reconstruction algorithm using a task-based performance metrology. *Med Phys.* **2015**;42:(314–23).   
17. **Samei E, Flynn MJ, Eyler WR.** “Detection of subtle lung nodules: Relative influence of quantum and anatomic noise on chest radiographs.” *Radiology* **1999**;213(3):727–734  
18. **Barrett H H, Myers K J**. Foundations of Image Science. Hoboken: Wiley; 2013  
19. **Bushberg JT, Seibert JA, Leidholdt EM Jr, Boone JM.** *The Essential Physics of Medical Imaging.* 4ª ed. Philadelphia: Wolters Kluwer; **2021**.  
20. **Siewerdsen J H.** Task-based assessment of image quality using model observers. In: **Samei E, Krupinski E A,** eds. *The Handbook of Medical Image Perception and Techniques*. 2nd ed. Cambridge: Cambridge University Press; **2018**. p. 417–439.  
21. **Siewerdsen JH, Cunningham IA, Jaffray DA.** A framework for noise-power spectrum analysis of multidimensional images. *Med Phys*. **2002**;29(11):2655–2671.  
22. **Solomon J, Samei E.** IMQuest: image quality assessment software for CT \[software\]. Duke University, Durham (NC), USA; **2018**. Disponível em: [https://imquest.vm.duke.edu](https://imquest.vm.duke.edu) Acesso em: 23 nov. 2025  
23. **Chen B, Richard S, Christianson O, Zhou X, Samei E.** CT performance as a variable function of resolution, noise, and task property for iterative reconstructions. In: *Medical Imaging **2012**: Physics of Medical Imaging*. Proc SPIE. 2012;8313:83131K.  
24. **Boone J M**. Determination of the presampled MTF in computed tomography. *Med Phys*. **2001**;28(3):356–360.  
25. **Eckstein M P, Bartroff J L, Abbey C K, Whiting J S, Bochud F O.** Automated computer evaluation and optimization of image compression of x-ray coronary angiograms for signal known exact detection tasks. *Opt Express*. **2003**;11(5):460–467.  
26. **Choopani M R, Abedi I, Dalvand F.** Quality assessment of computed tomography images using a channelized Hotelling observer: optimization of protocols in clinical practice. *Adv Biomed Res*. **2023**;12:8.  
27. **Abbey C K, Eckstein M P, Bochud F O.** Estimation of human-observer templates in two-alternative forced-choice experiments. *Proc SPIE*. **1999**;3663:284–295.  
28. **Greffier J, Van Ngoc Ty C, Sammoud S, Croisille C, Beregi J-P, Dabli D, Fitton I.** Image quality and dose reduction with photon counting detector CT: Comparison between ultra-high resolution mode and standard mode using a phantom study. Diagn Interv Imaging. 2025;106(9):320–326.   
29. **Lee W, Wagner F, Galdran A, Shi Y, Xia W, Wang G, Mou X, Ahamed M A, Imran A A Z, Oh J E, Kim K, Baek J T, Lee D, Hong B, Tempelman P, Lyu D, Kuiper A, van Blokland L, Calisto M B, Hsieh S, Han M, Baek J, Maier A, Wang A, Gold G E, Choi J H.** Low-dose computed tomography perceptual image quality assessment. Med Image Anal. 2025;99:103343.   
30. **Costa P R, Boiset G R, Pimenta E B, Rocha R M V, Moura R A S, Marques W H, Oostveen L J, Geurts B, Sawamura M V Y, Nersissian D Y, Yoshimura E M, Sechopoulos I.** Hybrid phantom for lung CT: Design and validation. Med Phys. 2025;52(8):e17990.

[^1]:  Ver também: Jones F. *Pesquisadores brasileiros desenvolvem dispositivo que simula pulmão e nódulos*. Revista Pesquisa FAPESP, 1 nov. 2025\. Disponível em: [https://revistapesquisa.fapesp.br/pesquisadores-brasileiros-desenvolvem-dispositivo-que-simula-pulmao-e-nodulos.](https://revistapesquisa.fapesp.br/pesquisadores-brasileiros-desenvolvem-dispositivo-que-simula-pulmao-e-nodulos) Nascimento A. *Dispositivo pode aprimorar o rastreamento do câncer de pulmão*. Jornal da USP, 12 nov. 2025\. Disponível em: [https://jornal.usp.br/ciencias/dispositivo-pode-aprimorar-o-rastreamento-do-cancer-de-pulmao](https://jornal.usp.br/ciencias/dispositivo-pode-aprimorar-o-rastreamento-do-cancer-de-pulmao).
---
title: "Observadores de Aprendizado Profundo para a Otimização de Protocolos de Tomografia Computadorizada Baseada em Tarefas"
author: "Wagner Henrique Marques"
advisor: "Prof. Dr. Paulo Roberto Costa"
institution: "Grupo de Dosimetria das Radiações e Física Médica (GDRFM) / InRad-HCFMUSP / IFUSP"
academic_level: "Doutorado Direto (FAPESP)"
date: 2026-09-21
tags:
  - doutorado
  - fisica-medica
  - tomografia-computadorizada
  - task-based-image-quality
  - deep-learning
  - reconstrucao-de-imagens
  - otimizacao-de-protocolos
  - aapm-tg233
  - npwe
  - cho
  - dlmo
  - 2afc
---

# Projeto de Doutorado Direto

**Candidato:** Wagner Henrique Marques  
**Orientador:** Prof. Dr. Paulo Roberto Costa  
**Instituição Sede:** Faculdade de Medicina da Universidade de São Paulo (FMUSP) / Instituto de Radiologia do Hospital das Clínicas (InRad-HCFMUSP)  
**Grupo de Pesquisa:** Grupo de Dosimetria das Radiações e Física Médica (GDRFM - IFUSP/FMUSP)  
**Área de Concentração:** Diagnóstico por Imagem / Física Médica  

---

% --- CAPA PRÉ-TEXTUAL (Não contabilizada nas 20 páginas da proposta) ---
\begin{titlepage}
\centering
\onehalfspacing
{\large**UNIVERSIDADE DE SÃO PAULO**}\\[0.2cm]
{\large**FACULDADE DE MEDICINA DA UNIVERSIDADE DE SÃO PAULO**}\\[0.2cm]
{\normalsize Departamento de Radiologia e Oncologia}\\[0.2cm]
{\normalsize Grupo de Dosimetria das Radiações e Física Médica (GDRFM)}\\[3.5cm]

{\Large**PROJETO DE DOUTORADO DIRETO**}\\[1.2cm]


{\LARGE**Observadores de aprendizado profundo para a otimização de protocolos de tomografia computadorizada baseada em tarefas**}\\[2.5cm]

\begin{flushright}
\begin{minipage}{0.65\textwidth}
\normalsize
**Candidato:** Wagner Henrique Marques\\[0.3cm]
**Orientador:** Prof. Dr. Paulo Roberto Costa\\[0.3cm]
**Instituição Sede:** Faculdade de Medicina da Universidade de São Paulo - Instituto de Radiologia do Hospital das Clínicas da FMUSP\\[0.3cm]
**Área de Concentração:** Diagnóstico por imagem / Física Médica
\end{minipage}
\end{flushright}

\vfill
{\normalsize São Paulo, SP}\\[0.2cm]
{\normalsize Setembro de 2026}
\end{titlepage}


---

\setcounter{page}{1} % Início da contagem das 20 páginas de corpo de texto

% =========================================================================
% 1. RESUMO
% =========================================================================

# Resumo


A Tomografia Computadorizada (TC) é uma das principais ferramentas para o diagnóstico por imagem e sua otimização envolve o equilíbrio entre dose de radiação ionizante, qualidade da imagem e tempo operacional. Em imagens médicas, a adoção de reconstruções iterativas e de redução de ruído por aprendizado profundo modificou a textura do ruído e a resolução espacial de grande parte das imagens médicas atuais, limitando o uso de métricas globais tradicionais e reforçando a necessidade de avaliações baseadas na tarefa diagnóstica. Nesse contexto, o presente projeto propõe desenvolver e validar um observador de aprendizado profundo, com mecanismo de atenção, capaz de estimar a detectabilidade de lesões e apresentar maior concordância com o desempenho perceptual de radiologistas do que observadores-modelo lineares. Uma vez validado, o observador será utilizado como ferramenta para duas finalidades: (i) apoiar a otimização multiobjetivo de dose, tempo operacional e detectabilidade; e (ii) avaliar a robustez e a transferibilidade das estimativas de desempenho na tarefa de detecção entre diferentes equipamentos e fabricantes. Serão utilizados três *phantoms* híbridos: de tórax, abdome e crânio, avaliados em sete tomógrafos de quatro fabricantes, integrando automatização das métricas de NPS, TTF e índice de detectabilidade. A calibração perceptual será realizada por meio de estudos 2AFC e/ou paradigmas ROC de respostas livres (FROC/AFROC) com radiologistas especialistas, estabelecendo uma referência humana para a validação do observador proposto. Posteriormente, os resultados serão empregados na otimização conjunta de dose, tempo operacional e desempenho na tarefa de detecção, caracterizando a respectiva fronteira de Pareto com incorporação da incerteza experimental. Espera-se estabelecer uma metodologia automatizada e baseada em tarefa para apoiar a otimização de protocolos de TC, contribuindo para a adequação das doses de radiação sem comprometer a capacidade de detecção das estruturas de interesse.

\vspace{0.3cm}
\noindent**Palavras-chave:** tomografia computadorizada; otimização de protocolos; qualidade de imagem baseada em tarefa; observadores-modelo; aprendizado profundo; dose de radiação.

% =========================================================================
% 2. INTRODUÇÃO E JUSTIFICATIVA
% =========================================================================

# Introdução e Justificativa


Estima-se que sejam realizados 4,3 bilhões de exames radiológicos médicos por ano no mundo, e a TC responde por aproximadamente 62% da dose coletiva decorrente dessas exposições [[unscear2022]]. Sua ampla disponibilidade, rapidez de aquisição e capacidade de fornecer informações anatômicas detalhadas consolidaram a TC como uma das principais modalidades da radiologia diagnóstica, com utilização ainda crescente [[oecd2025]]. Nesse contexto, a otimização dos protocolos de TC permanece um desafio central: embora a redução da dose seja fundamental para a proteção radiológica, ela não pode ocorrer à custa da capacidade de detectar a estrutura ou lesão de interesse clínico [[icru2012]].

Avanços recentes mostram que a redução de dose é tecnicamente possível. Um levantamento de 5,2 milhões de aquisições realizadas em 592 instituições dos Estados Unidos demonstrou redução média de 21,8% nos níveis de referência diagnóstica (DRL) de TC em adultos entre 2014 e 2025, com reduções mais expressivas no tórax e mais discretas no crânio [[kanal2026]]. Entretanto, os DRLs caracterizam apenas os níveis de exposição e não informam se a imagem mantém desempenho adequado para a tarefa diagnóstica em questão [[mccollough2026]]. Assim, a redução da dose, embora necessária, não constitui por si só um critério suficiente de otimização. O problema passa a ser o de determinar qual o menor nível de dose que produz a informação diagnóstica necessária para cada tarefa clínica. Essa questão é particularmente relevante diante da evolução dos algoritmos de reconstrução de imagem. Reconstruções iterativas (IR) e, sobretudo, reconstruções baseadas em aprendizado profundo (DLR)^[Embora designados comercialmente e na literatura especializada como Deep Learning Reconstruction (DLR), a maioria desses algoritmos opera preponderantemente no domínio da imagem ou em domínios híbridos como processos avançados de redução de ruído (*denoising*) e preservação de textura, e não como reconstrução tomográfica direta, a partir do espaço de projeções.] modificam de forma não linear a textura do ruído e a resolução espacial das imagens, tornando insuficientes as métricas globais tradicionalmente empregadas na avaliação da qualidade de imagem [[barrett2015, shi2023, greffier2022]]. Nesse cenário, abordagens baseadas na tarefa diagnóstica(*task-based*), como o índice de detectabilidade ($d'$), permitem relacionar as propriedades físicas da imagem à capacidade médica de detectar estruturas de interesse [[shi2023]]. Entretanto, permanece pouco estabelecida a correspondência entre essas métricas e o desempenho perceptual de observadores humanos em diferentes anatomias, algoritmos de reconstrução e equipamentos. Essa lacuna limita a utilização das métricas *task-based* como instrumento direto de otimização de protocolos.

Além da dose e do desempenho diagnóstico, existe uma terceira dimensão relevante que permanece pouco explorada: o tempo operacional. Em um protocolo de TC, o tempo de aquisição depende de parâmetros como tempo de rotação, *pitch*, colimação e extensão da varredura, enquanto o tempo de reconstrução pode variar substancialmente entre algoritmos convencionais (como Retroprojeção Filtrada, FBP), iterativos e de aprendizado profundo. A soma desses componentes determina o intervalo entre o início da aquisição e a disponibilidade das imagens reconstruídas em sala de laudo. Portanto, o tempo não representa apenas uma variável administrativa: ele está relacionado tanto às condições físicas de aquisição quanto à capacidade operacional do serviço. Essa questão é particularmente evidente em programas de rastreamento por TC de baixa dose, nos quais a capacidade de atendimento pode ser limitada não apenas pela dose, mas também pela disponibilidade dos equipamentos e pelo tempo necessário para processamento e interpretação dos exames. 

Consequentemente, um protocolo que seja ótimo quando considerado apenas dose e qualidade de imagem pode não ser ótimo quando suas implicações operacionais são incorporadas. Este projeto parte, portanto, da hipótese de que dose, tempo operacional e desempenho na tarefa de detecção constituem objetivos que devem ser considerados conjuntamente. Formalmente, a seleção de protocolos pode ser representada pela otimização simultânea do vetor $(D, T, W)$, buscando-se a minimização dos dois primeiros componentes e a maximização do terceiro, em que $D$ representa a dose, $T$ o tempo operacional e $W$ o desempenho na tarefa diagnóstica.

A complexidade desse problema decorre ainda da elevada dimensionalidade do espaço de protocolos. Os parâmetros de aquisição e reconstrução, como tensão e corrente do tubo, *pitch*, espessura de corte, *kernel* e algoritmo de reconstrução, interagem entre si e produzem diferentes combinações de dose, tempo e desempenho. Nesse sentido, há estratégias de otimização baseadas em detectabilidade que já demonstraram que esse espaço pode ser explorado de forma sistemática e adaptado ao porte do paciente e ao equipamento [[zhang2017]]. Recentemente, a convergência entre inteligência artificial e ensaios virtuais de imagem (VIT) 
foi explorada para a seleção automatizada de parâmetros em TC baseada em tarefa utilizando aprendizado por reforço [[zou2026]]. Embora tais abordagens demonstrem o potencial 
da automação, elas recorrem às formulações analíticas lineares de detectabilidade (como NPWE e CHO), as quais não capturam a 
não-estacionaridade e o comportamento não linear característicos dos algoritmos comerciais de 
reconstrução por aprendizado profundo (DLR). Além disso, a transposição de resultados obtidos 
em ambientes virtuais para tomógrafos clínicos reais permanece limitada pela discrepância de 
domínio (*sim-to-real gap*). 

Entretanto, sua exploração experimental não pode ser realizada diretamente em seres humanos, uma vez que a avaliação de diferentes protocolos deve respeitar os princípios de justificação e proteção radiológica. Nesse contexto, os *phantoms* se posicionam como alternativa, pois permitem a aquisição repetida e controlada de imagens, sob diferentes condições de exposição e reconstrução. Além disso, abordagens recentes se basearam na radiômica para caracterizar esse *trade-off* em *phantom* [[karimipourfard2026]], reforçando a viabilidade de explorações sistemáticas do espaço experimental, ainda que sem ancorar a otimização em métricas perceptualmente validadas. Nessa linha, mas como complemento, estratégias recentes de fabricação de *phantoms* com grande número de lesões em escala submilimétrica demonstram o potencial desses dispositivos para aumentar a eficiência das avaliações de detectabilidade em TC [[shunhavanich2024]]. 

Porém, a escolha do *phantom* a ser utilizado é particularmente importante quando se pretende relacionar métricas físicas de qualidade de imagem ao desempenho perceptual. *Phantoms* puramente geométricos oferecem condições controladas e reprodutíveis para a metrologia, mas não reproduzem adequadamente a complexidade anatômica; por outro lado, simuladores exclusivamente antropomórficos proporcionam maior realismo, mas dificultam a realização de medidas quantitativas controladas [[wilson2013, choopani2023]]. 

Dado isso, o presente projeto avança em relação a essas abordagens anteriores ao ancorar a matriz 
experimental em *phantoms* híbridos físicos avaliados em sete equipamentos clínicos de quatro fabricantes, 
desenvolver um observador profundo (DLMO) treinado diretamente frente à percepção humana e incorporar as restrições de tempo operacional do serviço. Os *phantoms* híbridos empregados neste projeto integram essas duas características em um mesmo dispositivo, permitindo realizar a caracterização quantitativa das propriedades da imagem e, simultaneamente, estudos qualitativos em condições anatômicas mais realistas. O Grupo de Dosimetria das Radiações e Física Médica (GDRFM) do IFUSP desenvolveu, com apoio da FAPESP (processos 2022/11457-0 e 2023/03945-8), três *phantoms* híbridos destinados às regiões de tórax, abdome e crânio. O *phantom* de tórax (Figura (fig:fig1)) foi validado em equipamentos de última geração na Radboudumc, Holanda, e seus resultados foram publicados em *Medical Physics* [[costa2025]], tendo o candidato como coautor^[A patente deste *phantom* foi recentemente submetida ao INPI sob número BR 10 2026 019854-4]. Os de abdome e crânio se encontram em estágio avançado de finalização. Sendo assim, essa infraestrutura fornece a base experimental necessária para investigar, de forma sistemática e controlada, a relação entre parâmetros técnicos, dose, tempo operacional e desempenho na tarefa de detecção.

Dessa forma, o presente projeto busca avançar além da avaliação convencional de qualidade de imagem, investigando se um observador de aprendizado profundo^[No contexto da avaliação da qualidade de imagem baseada em tarefas (*task-based*), define-se como 'observador de aprendizado profundo' o modelo computacional baseado em redes neurais profundas (neste projeto, estruturado com mecanismos de atenção) treinado para executar tarefas psicofísicas controladas (como detecção binária de sinal/lesão em fundo estruturado). Diferentemente de classificadores diagnósticos convencionais, o DLMO é calibrado para modelar e predizer o desempenho perceptual de observadores humanos (radiologistas), superando as premissas de linearidade e estacionaridade estatística do ruído que limitam os observadores-modelo analíticos clássicos (como CHO e NPWE) sob reconstruções não lineares.], treinado na tarefa de detecção e calibrado a partir do desempenho perceptual de radiologistas, pode representar de maneira mais adequada a detectabilidade em imagens produzidas por algoritmos de reconstrução não lineares. A partir dessa calibração, pretende-se utilizar o observador como componente de uma estratégia de otimização conjunta de dose, tempo operacional e desempenho diagnóstico, avaliando ainda a robustez das recomendações diante da mudança de anatomia, algoritmo de reconstrução e equipamento. O objetivo final é estabelecer uma metodologia *task-based* automatizada e experimentalmente validada que permita identificar protocolos de TC mais eficientes, reduzindo exposição e tempo operacional sem comprometer a capacidade de detecção das estruturas de interesse. A variação das características de intensidade e contraste entre diferentes condições de aquisição constitui ainda um desafio para a generalização de modelos de aprendizado profundo, tornando relevante avaliar estratégias de harmonização e robustez entre diferentes domínios.


> [!INFO] Figura
> Módulos no gantry.


A avaliação da qualidade de imagem em TC foi historicamente baseada em métricas como a relação sinal-ruído (SNR) e o contraste-ruído (CNR), adequadas sobretudo aos sistemas nos quais as propriedades do ruído podem ser descritas por modelos aproximadamente lineares e estacionários. A introdução de IR e DLR modificou essa relação ao produzir texturas de ruído e resoluções espaciais dependentes do conteúdo da imagem, do nível de contraste e da dose [[samei2021, greffier2020]]. Nesse contexto, métricas globais podem não representar adequadamente o desempenho do sistema na tarefa diagnóstica. O AAPM Task Group 233 recomenda, por isso, uma avaliação baseada na tarefa clínica, na qual o índice de detectabilidade, $d'$, integra informações sobre a textura do ruído, caracterizada por seu espectro de potência (NPS) [[siewerdsen2002]], e a resolução espacial dependente do contraste, caracterizada pela função de transferência de tarefa (TTF) [[samei2019]]. O $d'$ pode ser estimado por observadores-modelo lineares, como o *Non-Prewhitening with Eye Filter* (NPWE), o *Hotelling Observer* (HO) e o *Channelized Hotelling Observer* (CHO), cuja utilização constitui uma abordagem estabelecida para a avaliação objetiva da qualidade de imagem [[barrett1993, zhou2019]]. Entretanto, esses modelos foram desenvolvidos sob pressupostos que podem ser violados por reconstruções não lineares, limitando sua capacidade de representar a complexidade das texturas produzidas por DLR e sua correspondência com a percepção humana. Uma alternativa para essa limitação é o emprego de observadores de aprendizado profundo, capazes de aprender diretamente padrões associados à detectabilidade a partir das imagens. Neste projeto, propõe-se especificamente uma arquitetura com mecanismo de atenção, capaz de ponderar diferentes regiões e características da imagem de forma dependente do contexto. A questão central não é apenas desenvolver um novo modelo matemático para representar um observador, mas determinar se sua estimativa de detectabilidade apresenta maior concordância com o desempenho humano do que os observadores lineares de referência, particularmente em imagens produzidas por algoritmos de reconstrução não lineares [[solomon2016]]. Para isso, a resposta perceptual de radiologistas com diferentes níveis de experiência, em diferentes anatomia, a partir de séries de imagens de *phantoms* realizadas em equipamentos de diferentes fabricantes. Esta etapa do trabalho deverá  estabelecer referências humanas independentes para a avaliação do modelo em condições experimentais não vistas. O desempenho humano será estabelecido por meio de estudos de escolha forçada entre duas alternativas (*two-alternative forced choice*, 2AFC), nos quais o observador identifica, em cada par de imagens simultâneas, aquela que contém a lesão. Em tarefas de detecção, esse paradigma psicofísico é formalmente livre de critério (criterion-free), eliminando os vieses decorrentes de limiares decisórios subjetivos dos leitores. Sob o modelo padrão de detecção de sinal, a proporção de escolhas corretas ($P_C$) é matematicamente equivalente à área sob a curva ROC ($\text{AUC} = P_C$) e relaciona-se diretamente ao índice de detectabilidade por $d' = \sqrt{2} \Phi^{-1}(P_C)$, permitindo estimar o desempenho perceptual humano com elevada eficiência estatística e menor fadiga observacional [[chakraborty2017, burgess1995]]. Entretanto, estudos perceptuais com leitores humanos são operacionalmente complexos, exigem recrutamento de especialistas e apresentam elevado custo de tempo. Por essa razão, sua utilização em larga escala para caracterizar numerosas combinações de protocolos é pouco viável. Neste projeto, o estudo 2AFC será empregado como conjunto calibrador, estrategicamente selecionado para representar as diferentes anatomias, equipamentos, níveis de dose e famílias de reconstrução, evitando que a avaliação humana se torne o fator limitante da exploração experimental.

Existe também uma limitação relacionada à escala e à reprodutibilidade das avaliações quantitativas. A obtenção de NPS, TTF e $d'$ ainda é frequentemente realizada por procedimentos que dependem de delimitação manual de regiões de interesse e de fluxos de processamento específicos para determinado equipamento ou anatomia. Essa dependência dificulta a aplicação sistemática de métricas baseadas em tarefas em programas de avaliação de qualidade e limita sua utilização em estudos que envolvem grande número de protocolos e equipamentos [[choopani2023]]. Estudos perceptuais recentes demonstram a dimensão desse problema: a caracterização da detectabilidade de pequenas lesões sob reconstrução por aprendizado profundo já exigiu 24 leitores em um estudo com *phantom* [[toia2023]], enquanto estudos *task-based* em TC abdominal permanecem restritos a condições experimentais específicas, como, por exemplo, uma anatomia e um equipamento [[racine2020, racine2021]]. A combinação entre avaliação humana e caracterização quantitativa, portanto, permanece difícil de escalar.

O presente projeto acrescenta a essa problemática uma dimensão ainda pouco incorporada aos métodos de otimização: o tempo operacional. O tempo de aquisição possui relação direta com as condições de formação da imagem. Para um mesmo índice de dose volumétrica ($\text{CTDI}_{\text{vol}}$), alterações no tempo de rotação ou no *pitch* podem exigir mudanças proporcionais na corrente do tubo de raios X. Quando são atingidos os limites de potência do tubo do equipamento, a redução do tempo de aquisição pode limitar a fluência de fótons por elemento de volume, aumentando o ruído quântico e potencialmente reduzindo a detectabilidade (AAPM TG-233). O tempo de reconstrução introduz, adicionalmente, uma latência entre a aquisição e a disponibilidade das imagens, que pode variar entre algoritmos convencionais, iterativos e de aprendizado profundo. Assim, protocolos equivalentes em dose e desempenho de imagem podem apresentar custos operacionais , relacionados aos tempos de operação. A consequência é que uma otimização restrita à dose e qualidade pode não identificar soluções eficientes quando as restrições temporais do serviço são consideradas [[oostveen2021]]. A tomografia computadorizada por contagem de fótons (*photon-counting CT*, PCCT) constitui uma extensão exploratória adicional do problema de otimização. Diferentemente dos equipamentos convencionais, a PCCT permite a reconstrução de imagens monoenergéticas virtuais (VMI), introduzindo a energia de reconstrução como variável adicional. Energias mais baixas podem aumentar o contraste de estruturas contendo iodo, enquanto energias mais elevadas tendem a reduzir o ruído relativo; a combinação dessas características com a resolução espacial do detector amplia o espaço de possíveis protocolos. Assim, para uma determinada tarefa, pode existir uma faixa de energia virtual associada à maior detectabilidade. Entretanto, como não há acesso nacional a equipamento de contagem de fótons no escopo principal desta pesquisa, essa dimensão será tratada como extensão exploratória e não condicionará as conclusões centrais da tese.

As métricas baseadas em observadores-modelo e o índice de detectabilidade constituem uma abordagem consolidada para avaliação objetiva da qualidade de imagem em radiologia, com aplicações em diferentes tarefas e modalidades [[vasconcelos2024, pimenta2025]]. As lacunas investigadas nesta proposta decorrem diretamente dos resultados do trabalho de doutorado mais recente do grupo. Recentemente, Pimenta~[[pimenta2026]] validou o *framework task-based* em TC pulmonar, empregando sistemas de integração de energia (EDCT) e de contagem de fótons (PCCT) [[costa2025spie]]. Esse estudo identificou lacunas metodológicas determinantes, tais como: (i) o uso exclusivo do observador NPWE sem calibração com leitores humanos; (ii) a restrição a uma única anatomia; (iii) a dependência de equipamentos de um único fabricante; e (iv) a desconsideração do tempo operacional na otimização de protocolos. A presente proposta parte dessas limitações para avançar o *framework* em direção a uma avaliação mais representativa da percepção humana, mais abrangente quanto às condições de aquisição e mais adequada à otimização de protocolos de TC.

A infraestrutura metodológica necessária para esse avanço também já se encontra em desenvolvimento. Em projeto de mestrado do grupo (FAPESP 2025/26836-5), estão sendo implementados o *pipeline* automatizado para extração de NPS, TTF e $d'$ e os observadores-modelo NPWE, HO e CHO para o *phantom* de tórax. Este projeto de Doutorado Direto visa desenvolver e validar um observador de aprendizado profundo com mecanismo de atenção, calibrado pelo desempenho de radiologistas e contrastado a observadores lineares. A hipótese central é que o modelo reproduz a detectabilidade humana em reconstruções não lineares de forma mais acurada. Subsequentemente, o observador será empregado na otimização conjunta de dose, tempo e detectabilidade e submetido a testes de robustez frente à variação anatômica e instrumental em sete tomógrafos de quatro fabricantes, comprovando a aplicabilidade e generalização da contribuição proposta.

% =========================================================================
% 3. OBJETIVOS
% =========================================================================

# Objetivos



## Pergunta central

Em que medida um observador de aprendizado profundo, desenvolvido para estimar o desempenho em tarefas de detecção e calibrado em relação à percepção de radiologistas, pode representar, de forma mais adequada, o desempenho perceptual humano em imagens de tomografia computadorizada reconstruídas por métodos não lineares e, a partir dessa representação, apoiar a otimização conjunta de dose, tempo operacional e desempenho na tarefa de detecção, mantendo-se válido diante da variação de anatomia, equipamento e algoritmo de reconstrução?


## Objetivo geral

Desenvolver, validar e avaliar um observador de aprendizado profundo para tarefas de detecção em TC, calibrado em relação ao desempenho perceptual de radiologistas, e investigar sua aplicação na otimização conjunta de dose, tempo operacional e desempenho na tarefa de detecção, considerando diferentes anatomias, algoritmos de reconstrução e equipamentos de diferentes fabricantes.


## Objetivos específicos

\begin{enumerate}
    \item Avaliar a aplicabilidade e a reprodutibilidade de métricas de qualidade de imagem baseadas em tarefa, incluindo NPS, TTF e $d'$, em imagens de TC de tórax, abdome e crânio obtidas em diferentes equipamentos e condições de reconstrução, utilizando o *pipeline* automatizado.
    \item Estabelecer uma referência de desempenho perceptual humano para tarefas controladas de detecção, por meio de experimentos 2AFC com radiologistas especialistas nas diferentes regiões anatômicas, e quantificar a relação entre esse desempenho e as métricas de qualidade de imagem baseadas em tarefas.
    \item Desenvolver e validar um observador de aprendizado profundo com mecanismo de atenção para estimar o desempenho em tarefas de detecção em imagens reconstruídas por métodos lineares e não lineares, comparando seu desempenho com os observadores-modelo lineares NPWE, HO e CHO previamente estabelecidos pelo grupo.
    \item Determinar se o observador de aprendizado profundo apresenta maior concordância com o desempenho perceptual humano do que os observadores-modelo lineares, particularmente em imagens produzidas por reconstruções iterativas e por aprendizado profundo, nas quais a textura do ruído apresenta comportamento espacialmente dependente.
    \item Investigar a influência conjunta da dose e do tempo operacional sobre o desempenho na tarefa de detecção, considerando o tempo de aquisição e o tempo de reconstrução como componentes mensuráveis do protocolo.
    \item Formular e avaliar a otimização multiobjetivo de protocolos de TC, considerando simultaneamente a minimização da dose, a minimização do tempo operacional e a maximização do desempenho na tarefa de detecção, e caracterizar a respectiva fronteira de Pareto considerando a incerteza experimental utilizando o observador de aprendizado profundo validado como estimador de desempenho na tarefa de detecção.
    \item Avaliar a transferibilidade do observador e das recomendações de protocolo entre equipamentos de diferentes fabricantes, por meio de validação com equipamentos não utilizados no treinamento, quantificando a degradação de desempenho e o esforço experimental necessário para a recalibração.
    \item Determinar as condições nas quais o observador de aprendizado profundo pode ser utilizado como ferramenta de apoio à otimização de protocolos, identificando suas limitações quanto à anatomia, equipamento, algoritmo de reconstrução e domínio de treinamento.
\end{enumerate}

% =========================================================================
% 4. MATERIAL E MÉTODOS
% =========================================================================

# Material e Métodos



## Instrumentos: *phantoms
*
Serão utilizados três *phantoms* híbridos desenvolvidos pelo GDRFM, representativos das regiões anatômicas de tórax, abdome e crânio. Os dispositivos combinam uma configuração geométrica, destinada à caracterização quantitativa da qualidade de imagem, e uma configuração antropomórfica, destinada à avaliação qualitativa. Os modelos anatômicos foram gerados a partir de exames tomográficos de pacientes reais do Instituto de Radiologia do Hospital das Clínicas da FMUSP (InRad-HCFMUSP), devidamente anonimizados e aprovados pelo Comitê de Ética em Pesquisa (CEP-FMUSP, CAAE: 27.912.619.6.0000.0068). A reconstrução volumétrica e as segmentações anatômicas das estruturas de interesse foram executadas combinando os *softwares* 3D Slicer [[fedorov2012]] e Mimics Innovation Suite [[mimics2024]], com posterior conversão para arquivos de manufatura aditiva (*Standard Triangle Language*, STL). As estruturas internas foram confeccionadas por impressão 3D em colaboração técnico-científica com o Centro de Tecnologia da Informação Renato Archer (CTI Renato Archer / MCTI), utilizando materiais poliméricos com densidade e atenuação de raios X equivalentes aos tecidos biológicos humanos (osso, parênquima e tecidos moles) segundo a metodologia validada por Boiset et al.~[[boiset2023]] e Costa et al.~[[costa2025]].

O *phantom* de tórax reproduz a árvore traqueobrônquica e o parênquima pulmonar, incluindo nódulos sólidos e em vidro fosco de dimensões e contrastes controlados, tendo sido previamente validado em equipamentos convencionais e de contagem de fótons [[costa2025]]. O *phantom* de crânio reproduz a geometria e as propriedades atenuadoras da calota craniana humana, integrando simulação de osso cortical e trabecular, a partir de exames clínicos reais do InRad. A Figura (fig:fig2) apresenta o protótipo do módulo de crânio e as etapas de manufatura aditiva das estruturas internas do *phantom* de abdome. Em complemento, a Figura (fig:fig3) apresenta o projeto e a usinagem da base elíptica em polietileno de ultra-alto peso molecular (UHMW), tanto na versão oca, destinada a alojar as estruturas anatômicas, quanto na versão maciça, utilizada para as caracterizações físicas de ruído e detectabilidade em fundo uniforme. A utilização dos mesmos nas etapas metrológica e perceptual permite relacionar as métricas físicas de qualidade de imagem ao desempenho dos observadores-modelo e dos radiologistas, sob condições experimentais controladas.


> [!INFO] Figura
> Módulo de crânio no gantry.



> [!INFO] Figura
> Base elíptica do *phantom* de abdome: (a) esquema da estrutura projetada para os estudos da região abdominal; (b) dispositivo oco usinado em polietileno de ultra-alto peso molecular (UHMW); (c) *phantom* elíptico maciço, usinado no mesmo material e nas mesmas dimensões do primeiro protótipo, destinado às medidas de detectabilidade em fundo homogêneo. Fonte: Autor.



## Matriz experimental

Será realizado um desenho experimental sistemático envolvendo três regiões anatômicas e sete tomógrafos de quatro fabricantes disponíveis no parque tecnológico do InRad-HCFMUSP, estruturados conforme a Tabela (tab:scanners).

\begin{table}[H]
\centering
\small
\setstretch{1.15}
\caption{Especificações dos tomógrafos clínicos que compõem o parque experimental (InRad-HCFMUSP).}
\label{tab:scanners}
\begin{tabularx}{\textwidth}{l p{3.8cm} c c X}
\toprule
**Fabricante** & **Modelo do Tomógrafo** & **Cortes** & **Tecnologia** & **Famílias de Reconstrução** \\
\midrule
nn \\
\bottomrule
\end{tabularx}
\end{table}

Serão avaliados parâmetros de aquisição e reconstrução, incluindo tensão e corrente do tubo de raios X, *pitch*, espessura de corte, *kernel* e algoritmo de reconstrução. Os níveis definitivos serão estabelecidos após ensaios-piloto, respeitando os limites operacionais dos equipamentos. Para reduzir o número de aquisições, será adotado delineamento em duas etapas: inicialmente, testes para identificação dos fatores de maior influência, seguido de uma caracterização mais detalhada das regiões relevantes do espaço experimental. As condições serão estratificadas por família de reconstrução, incluindo FBP, HIR e DLR, quando disponíveis. Os dois primeiros serão utilizados como referências para a comparação com as reconstruções não lineares. Para cada aquisição serão registrados, a partir dos metadados DICOM (*Digital Imaging and Communications in Medicine*), os parâmetros técnicos, $\text{CTDI}_{\text{vol}}$, DLP e os tempos de aquisição e reconstrução. Esses dados contribuirão para a avaliação conjunta de dose, tempo operacional e desempenho na tarefa de detecção. A ordem das aquisições será randomizada e a versão de *firmware* de cada equipamento será registrada como potencial covariável. A Figura (fig:fig4) apresenta o fluxo metodológico do projeto.


> [!INFO] Figura
> Representação esquemática das etapas de desenvolvimento, validação e aplicação do observador de aprendizado profundo, desde a preparação e validação metrológica até o estudo perceptual, a otimização multiobjetivo e a avaliação de transferibilidade entre equipamentos. O fluxo integra dados de aquisição, dose, tempo operacional e desempenho na tarefa de detecção para a definição de protocolos otimizados. Fonte: Autor.



## Eixo 1: Construção da referência task-based

O Eixo 1 incorporará à matriz experimental desta tese o *pipeline* automatizado previamente desenvolvido para extração das métricas objetivas de qualidade da imagem (NPS, TTF e $d'$), validando sua aplicação nas três anatomias, nos sete tomógrafos clínicos e sob as diferentes famílias de reconstrução investigadas. As séries DICOM serão processadas em ambiente *Python*, estruturando um fluxo metrológico computacional em conformidade com as recomendações do AAPM TG-233 [[samei2019, samei2021]].

Para caracterizar a magnitude e a correlação espacial das flutuações estocásticas nas imagens, a textura do ruído será quantificada pelo Espectro de Potência do Ruído bidimensional, $\text{NPS}(u, v)$. O cálculo será executado a partir de múltiplas regiões de interesse (ROIs) homogêneas de dimensões $N_x \times N_y$ pixels extraídas dos módulos uniformes dos *phantoms* híbridos, subtraindo-se o perfil médio de atenuação $\bar{I}(x, y)$ para isolar as flutuações estocásticas:

$$
\text{NPS}(u, v) = \frac{\Delta x \Delta y}{N_x N_y} \left\langle \left| \mathcal{F}_{2D} \left\{ I(x, y) - \bar{I}(x, y) \right\} \right|^2 \right\rangle
$$

em que $\Delta x$ e $\Delta y$ representam o espaçamento físico entre pixels no plano axial, $\mathcal{F}_{2D}$ denota a Transformada de Fourier bidimensional e os colchetes $\langle \cdot \rangle$ indicam a média de *ensemble* calculada sobre o conjunto de sub-ROIs independentes.

A resolução espacial, por sua vez, será caracterizada pela Função de Transferência da Tarefa, $\text{TTF}(f)$. Como algoritmos de reconstrução iterativa (MBIR e HIR) e de aprendizado profundo (DLR) exibem comportamento não linear e dependente do nível de contraste do objeto, a resposta em frequência do sistema não pode ser descrita por uma função de transferência de modulação (MTF) convencional. A TTF será extraída a partir da Função de Espalhamento de Borda circular, $\text{ESF}(r)$, obtida na interface dos *inserts* cilíndricos calibrados de baixo e alto contraste presentes nos módulos geométricos dos simuladores:

$$
\text{TTF}(f) = \frac{\left| \mathcal{F} \left\{ \frac{d}{dr}\text{ESF}(r) \right\} \right|}{\left| \mathcal{F} \left\{ \frac{d}{dr}\text{ESF}(r) \right\} \right|_{f=0}}
$$

em que $d/dr$ representa a derivada radial que produz a função de espalhamento de linha equivalente (LSF) e $\mathcal{F}\{\cdot\}$ é a Transformada de Fourier unidimensional, normalizada na frequência espacial zero ($f = 0$).

A integração das propriedades físicas do sistema com a tarefa diagnóstica será realizada primeiramente pelo observador-modelo analítico clássico Não Pré-Branqueador com Filtro Visual (*Non-Prewhitening with Eye Filter*, NPWE). A resposta do sistema visual humano é incorporada por meio do filtro visual isotrópico $E(u, v)$, expresso em função da frequência espacial radial $f = \sqrt{u^2 + v^2}$ (em ciclos/mm). Para relacionar a resolução espacial física na tela com o ângulo subtendido na retina do observador, converte-se $f$ na frequência angular visual $f_{\text{ang}} = \left( \frac{\pi}{180} d_{\text{obs}} \right) f$ (em ciclos por grau, cpd), onde $d_{\text{obs}}$ é a distância nominal de visualização do monitor médico (em mm). A função de sensibilidade ao contraste visual do olho humano é modelada segundo a curva psicofísica de Barten:

$$
E(u, v) = E(f_{\text{ang}}) = f_{\text{ang}}^{ 1{,}3} \exp\left( -c \cdot f_{\text{ang}} \right)
$$

em que o expoente $1{,}3$ rege a atenuação nas baixas frequências e o parâmetro $c$ calibra o pico de máxima sensibilidade perceptual (tipicamente em torno de $4\text{ cpd}$), sendo $E(u, v)$ normalizada ao pico unitário.

A partir dessa filtragem perceptual, o índice de detectabilidade escalar $(d'_{\text{NPWE}})^2$ sintetiza a transferibilidade da informação diagnóstica através da relação:

$$
(d'_{\text{NPWE}})^2 = \frac{\left[ \iint |W_{\text{task}}(u, v)|^2 \cdot \text{TTF}^2(u, v) \cdot E^2(u, v)   du   dv \right]^2}{\iint |W_{\text{task}}(u, v)|^2 \cdot \text{TTF}^2(u, v) \cdot \text{NPS}(u, v) \cdot E^4(u, v)   du   dv}
$$

na qual $W_{\text{task}}(u, v)$ representa o espectro da tarefa diagnóstica (dado pela Transformada de Fourier da lesão-alvo circular simulada em cada anatomia).

Complementarmente, com o intuito de estabelecer uma referência estatística ótima direta no domínio espacial da imagem, serão implementados os observadores lineares Hotelling: (*Hotelling Observer*, HO) e *Channelized Hotelling Observer*, CHO. O modelo HO ideal opera sobre a estatística da diferença média do sinal e a matriz de covariância do ruído:

$$
d'_{\text{HO}} = \sqrt{\Delta \mathbf{s}^T \mathbf{K}^{-1} \Delta \mathbf{s}}
$$

em que $\Delta \mathbf{s} = \bar{\mathbf{s}}_1 - \bar{\mathbf{s}}_0$ é o vetor que descreve a diferença média de atenuação nos pixels da ROI entre a hipótese com sinal (lesão presente) e ruído puro (lesão ausente), e $\mathbf{K}$ é a matriz de covariância do ruído de fundo. No observador CHO, esses vetores são previamente projetados sobre uma base de canais antropomórficos (como canais de diferenças de gaussianas, DOG), mimetizando a seletividade por bandas de frequência do córtex visual humano.

A validação da automação do pipeline de extração de NPS, TTF e $d'$ será realizada pela comparação direta com o procedimento manual de referência (delimitação manual de ROIs em conformidade com o AAPM TG-233), executado de forma cega e independente por físicos médicos pesquisadores em um subconjunto representativo das condições experimentais. A concordância e a reprodutibilidade entre o método automatizado e a metrologia manual de referência serão quantificadas pelo Coeficiente de Correlação Intraclasse (ICC, adotando-se como critério de validação $\text{ICC} \ge 0{,}90$) e por gráficos de dispersão de Bland--Altman. Os médicos radiologistas especialistas atuarão nas tarefas perceptuais de detecção no Eixo 2, cujo dimensionamento amostral de leitores e imagens é fundamentado na teoria de análise de poder MRMC descrita no Capítulo 11 de Chakraborty~[[chakraborty2017]]. Nas imagens reconstruídas por DLR, a possível não-estacionaridade da textura do ruído será considerada na interpretação das métricas. Além disso, as imagens reconstruídas por FBP e HIR serão utilizadas como condições de comparação, por apresentarem características mais próximas das premissas metodológicas dos observadores lineares.


## Eixo 2: Desenvolvimento e validação do observador DL

O Eixo 2 terá como contribuição central o desenvolvimento e a validação de um observador de aprendizado profundo com mecanismo de atenção para tarefas de detecção em imagens de TC. Será desenvolvido um observador baseado em Vision Transformer [[dosovitskiy2021]], ou arquitetura equivalente com mecanismo de atenção [[liu2021]], tendo como tarefa a classificação da presença ou ausência da estrutura-alvo $\hat{t} = f_\theta(I)$. Para mimetizar a percepção visual humana, introduz-se a calibração com ruído interno estocástico:

$$
z = \hat{t} + \varepsilon_{\text{int}}, \quad \varepsilon_{\text{int}} \sim \mathcal{N}(0, \sigma_{\text{int}}^2)
$$


O conjunto de dados será particionado previamente em treinamento, validação e teste, sem compartilhamento de aquisições entre esses conjuntos. A arquitetura, os parâmetros, a função de perda, o esquema de otimização e os critérios de parada serão definidos a partir dos conjuntos de treinamento e validação. O desempenho final será avaliado em conjunto de teste independente e comparado aos observadores-modelo NPWE, HO e CHO. 

A validação perceptual será realizada por meio de estudos 2AFC com observadores humanos convidados voluntariamente no InRad-HCFMUSP^[O recrutamento e a avaliação observacional com imagens de simuladores contam com o amparo de projeto aprovado pelo Comitê de Ética em Pesquisa da Faculdade de Medicina da Universidade de São Paulo (CEP-FMUSP, CAAE: 27.912.619.6.0000.0068). Caso a Comissão de Pesquisa da FMUSP ou do InRad recomende uma submissão de emenda específica para esta etapa do estudo observacional com voluntários, todos os trâmites regulatórios pertinentes serão protocolados oportunamente.], abrangendo tanto radiologistas assistentes experientes quanto médicos residentes vinculados aos setores de imagem de tórax, abdome e neurorradiologia. A relação psicofísica formal entre a proporção de escolhas corretas ($P_C$) e o índice de detectabilidade $d'_v$ no paradigma 2AFC, como mencionado anteriormente, é dada por:

$$
P_C = \text{AUC} = \Phi\left( \frac{d'_v}{\sqrt{2}} \right) \quad \Longleftrightarrow \quad d'_v = \sqrt{2} \Phi^{-1}(P_C)
$$


Para maximizar a aderência dos voluntários e mitigar os efeitos de fadiga visual, o desenho do estudo observacional será estruturado com base nas diretrizes metodológicas de Chakraborty~[[chakraborty2017]]: as sessões de leitura serão fracionadas em blocos curtos (com duração estimada de 15 a 20 minutos), minimizando a sobrecarga de imagens apresentadas a cada especialista, considerando o poder estatístico adequado para a identificação de diferenças de detectabilidade ($\alpha = 0{,}05$, $1 - \beta \ge 0{,}80$ sob modelagem MRMC). Os ensaios 2AFC serão conduzidos por meio de uma plataforma computacional web desenvolvida pelo GDRFM em ambiente Python, projetada especificamente para estudos psicofísicos de percepção médica. A interface apresentará os pares de imagens de forma randomizada, em conformidade com os padrões de exibição radiológica (DICOM GSDF / AAPM TG-18), registrando de forma automatizada e anonimizada a escolha forçada do leitor e o tempo de latência até a decisão.

A comparação principal será a concordância do observador de aprendizado profundo e dos observadores lineares com a referência humana, com análise específica das condições de reconstrução não linear. As reconstruções FBP e HIR atuarão como condições de controle para desacoplar a capacidade real do modelo de aprendizado profundo em mimetizar o leitor humano das distorções teóricas que os observadores lineares exibem diante do ruído não gaussiano e das texturas complexas dos métodos não lineares. A tarefa perceptual será realizada em condições controladas, com apresentação randomizada dos pares de imagens e registro da resposta e do tempo até a decisão. Esse desfecho representa uma tarefa controlada de detecção em *phantom* e não uma medida de exatidão diagnóstica clínica. A contribuição principal será avaliada pela capacidade do observador de reproduzir o desempenho perceptual humano, e não pela superioridade de uma arquitetura específica.


## Eixo 3: Aplicação do observador à otimização multiobjetivo

Após a validação do observador de aprendizado profundo no Eixo 2, ele será utilizado para estimar o índice de detectabilidade na otimização multiobjetivo de protocolos de TC. Cada protocolo será avaliado simultaneamente quanto a três objetivos: minimização da dose de radiação (representada pelo $\text{CTDI}_{\text{vol}}$), minimização do tempo operacional (composto pelo tempo de aquisição e tempo de reconstrução) e maximização do desempenho na tarefa de detecção (estimado pelo observador validado):

$$
\min_{\mathbf{p} \in \Omega} \mathbf{F}(\mathbf{p}) = \Big( D(\mathbf{p}), \; T(\mathbf{p}), \; -d'_{\text{DLMO}}(\mathbf{p}) \Big)
$$


$$
\text{sujeito a:} \quad T(\mathbf{p}) = T_{\text{aquisição}}(\mathbf{p}) + T_{\text{reconstrução}}(\mathbf{p}); \quad d'_{\text{DLMO}}(\mathbf{p}) \ge d'_{\text{ref}} - \delta_{\text{tol}}
$$


A exploração do espaço de protocolos será formulada como um problema de otimização com restrições operacionais dos equipamentos. A fronteira de Pareto será estimada utilizando algoritmos genéticos multiobjetivo, como o NSGA-II [[deb2002]], ou métodos baseados em $\varepsilon$-dominância [[laumanns2002]], apropriados para a identificação de soluções de compromisso entre objetivos conflitantes. Para reduzir o custo computacional e experimental da amostragem direta, serão empregados modelos substitutos (*surrogate models*) baseados em Processos Gaussianos [[rasmussen2006]] ou redes neurais para interpolar o desempenho nos parâmetros não medidos diretamente, incorporando a incerteza experimental na definição da fronteira. Os protocolos não dominados constituirão a fronteira de Pareto, permitindo identificar os compromissos entre dose, tempo e detectabilidade. A comparação entre as fronteiras obtidas para diferentes anatomias permitirá avaliar como a região anatômica condiciona o espaço de soluções viáveis.

A estratégia de otimização proposta será confrontada experimentalmente com a abordagem de 
referência recentemente estabelecida por Zou et al.~[[zou2026]]. Para isso, serão implementados dois 
cenários de otimização na matriz experimental dos sete tomógrafos:
\begin{enumerate}
    \item Cenário Baseline (Zou et al.~[[zou2026]], adaptado): formulação bi-objetivo entre dose ($\text{CTDI}_{\text{vol}}$) e detectabilidade estimada analiticamente 
    pelo observador linear NPWE, sob a restrição clássica $d'_{\text{NPWE}} \ge d'_{\text{ref}}$, 
    desconsiderando a latência temporal e as não-linearidades de reconstrução;
    \item Cenário Proposto (Espaço $D, T, W$): formulação tri-objetivo com busca da 
    Fronteira de Pareto integrando simultaneamente dose, tempo operacional total 
    ($T = T_{\text{aquisição}} + T_{\text{reconstrução}}$) e detectabilidade não linear estimada 
    pelo DLMO calibrado perceptualmente ($d'_{\text{DLMO}}$).
\end{enumerate}
Essa comparação direta permitirá quantificar experimentalmente a divergência nas recomendações 
de protocolo entre o modelo linear focado em dosimetria de Zou et al.~[[zou2026]] e o modelo proposto, 
evidenciando os riscos de subdosagem ou perda diagnóstica sob reconstruções DLR no ambiente clínico real.



## Eixo 4: Validação da generalização e transferibilidade do observador

Uma vez validado o observador no Eixo 2, sua robustez diante de mudanças de equipamento será avaliada por meio de um esquema de validação entre os sete tomógrafos. A transferibilidade do observador e das recomendações de protocolo será avaliada entre os sete tomógrafos de quatro fabricantes. Como os parâmetros de aquisição e reconstrução não são diretamente equivalentes entre plataformas, a comparação será realizada pelo desempenho na tarefa de detecção, utilizando o índice de detectabilidade como referência comum. Será adotado esquema de validação com equipamento retido, no qual o modelo será treinado em seis tomógrafos e avaliado no sétimo, alternando-se o equipamento excluído. Inicialmente, será quantificado o desempenho do observador no equipamento não utilizado durante o treinamento, caracterizando sua capacidade de transferência sem adaptação. Em seguida, será avaliado o efeito da recalibração, quantificando a redução inicial do índice de detectabilidade no equipamento retido e o número de aquisições necessárias para recuperar um nível de desempenho previamente definido. O objetivo será determinar a robustez da transferência entre os equipamentos avaliados e caracterizar seus limites de generalização, sem extrapolar os resultados para fabricantes ou plataformas não representados no estudo.


## Estágio de pesquisa no exterior

O projeto prevê um estágio BEPE na University of Pennsylvania, cuja formalização está em curso, para testar o observador em condições de alto rigor, utilizando PCCT e *phantoms* com nível de realismo bastante elevado, por conta da tecnologia de PixelPrint [[mei2022]]. Essa etapa fornecerá dados anatômicos ultrarrealistas para refinar o modelo no Brasil. Portanto, terá caráter complementar e exploratório, permitindo avaliar a robustez do observador em condições adicionais de aquisição e reconstrução, sem constituir requisito para o cumprimento dos objetivos centrais da tese.

% =========================================================================
% 5. FORMA DE ANÁLISE DOS RESULTADOS
% =========================================================================

# Forma de Análise dos Resultados


Os desfechos primários e os critérios de sucesso serão definidos a priori para cada hipótese e eixo do projeto, conforme sintetizado na Tabela (tab:hipoteses). A análise será conduzida em uma sequência coerente com o fluxo experimental: primeiro será verificada a validade da infraestrutura metrológica automatizada (Eixo 1), condição necessária para a geração confiável dos dados que alimentarão as etapas seguintes; em seguida, será avaliado o observador de aprendizado profundo (Eixo 2), que constitui a ferramenta central do projeto; por fim, serão avaliadas suas aplicações à otimização multiobjetivo (Eixo 3) e à transferibilidade entre equipamentos (Eixo 4).

No estudo 2AFC, o dimensionamento amostral será estabelecido por análise de potência multi-leitor--multi-caso (MRMC) [[hillis2011, chakraborty2017]], visando a uma potência estatística de 0,80 para detectar diferenças de AUC de 0,05 ($\alpha = 0{,}05$, bilateral). O número definitivo de observadores voluntários e de casos será estabelecido a partir das variâncias observadas em ensaios-piloto, recrutando-se a quantidade de leitores necessária para assegurar o poder estatístico adequado ao delineamento de cada região anatômica (tórax, abdome e crânio). O desfecho primário será a concordância entre o desempenho estimado pelos observadores e o desempenho perceptual humano, avaliada por análise MRMC. A comparação principal será realizada entre o observador de aprendizado profundo e o NPWE. Serão consideradas as correlações decorrentes da estrutura multi-leitor--multicaso, com análises estratificadas por anatomia e família de reconstrução.

\begin{table}[H]
\centering
\small
\setstretch{1.15}
\caption{Plano de análise por hipótese, com critérios de sucesso definidos a priori.}
\label{tab:hipoteses}
\begin{tabularx}{\textwidth}{l p{3.2cm} p{3.0cm} X}
\toprule
**Hipótese / eixo** & **Desfecho** & **Análise** & **Critério principal** \\
\midrule
P1 / Eixo 1 & Concordância da automação & ICC + Bland--Altman & $\text{ICC} \ge 0{,}90$ frente à extração manual de referência; viés médio não significativo ($p > 0{,}05$). \\
\addlinespace
H1 / Eixo 2 & Desempenho do observador DL & AUC; MRMC; comparação com NPWE & DL observer apresenta maior concordância com a referência humana que NPWE/HO/CHO ($p < 0{,}05$). \\
\addlinespace
H2 / Eixo 3 & Trade-off detectabilidade--dose & Otimização multiobjetivo; Pareto & Identificação de protocolo não dominado com redução de dose e/ou tempo, mantendo detectabilidade não inferior à referência dentro da incerteza. \\
\addlinespace
H3 / Eixo 4 & Transferibilidade entre equipamentos & Validação leave-one-scanner-out & Desempenho no equipamento retido dentro do limite pré-especificado e recuperação após recalibração ($r \ge 0{,}90$). \\
\bottomrule
\end{tabularx}
\end{table}

% =========================================================================
% 6. PLANO DE TRABALHO E CRONOGRAMA DE EXECUÇÃO
% =========================================================================

# Plano de Trabalho e Cronograma de Execução


O cronograma (Tabela (tab:cronograma)) viabiliza-se em 60 meses pela infraestrutura já consolidada: *phantoms* financiados (FAPESP 2022/11457-0; 2023/03945-8), o *pipeline* metrológico automatizado advindo de dissertação de mestrado do grupo (FAPESP 2025/26836-5), o parque tecnológico do InRad-HCFMUSP (sete tomógrafos e GPUs do InLab) e o *framework task-based* validado em TC pulmonar de baixa dose por Pimenta~[[pimenta2026]], que fornece linha de base metodológica e critérios de referência para os observadores lineares clássicos. Contamos com suporte para manufatura aditiva (CTI Renato Archer, UNESP) e parcerias internacionais (Radboudumc, University of Twente) com tecnologias de TC avançadas. As etapas obedecem a uma precedência estrita: validação automatizada (Eixo 1), calibração do observador profundo e estudo perceptual (Eixo 2), culminando na otimização multiobjetivo e testes de transferibilidade (Eixos 3 e 4). Essa sequência reflete a estrutura científica do projeto: o desenvolvimento e a validação do observador constituem a contribuição central, enquanto a otimização e a avaliação de transferibilidade constituem aplicações e testes de robustez dessa contribuição.

\begin{table}[H]
\centering
\scriptsize
\setstretch{1.1}
\caption{Cronograma de execução. S = semestre de vigência. A atividade A6 (BEPE) será submetida como proposta complementar à FAPESP.}
\label{tab:cronograma}
\begin{tabularx}{\textwidth}{X cccccccccc}
\toprule
**Atividade / Semestre** & **S1** & **S2** & **S3** & **S4** & **S5** & **S6** & **S7** & **S8** & **S9** & **S10** \\
\midrule
A1. Revisão bibliográfica e padronização dos phantoms & $\bullet$ & $\bullet$ & & & & & & & & \\
A2. Aquisições e validação da automação (Eixo 1) & $\bullet$ & $\bullet$ & $\bullet$ & & & & & & & \\
A3. Estudo perceptual 2AFC com radiologistas no InRad & & $\bullet$ & $\bullet$ & $\bullet$ & & & & & & \\
A4. Desenvolvimento e calibração do observador DL (Eixo 2) & & & $\bullet$ & $\bullet$ & $\bullet$ & & & & & \\
A5. Exame de qualificação & & & & $\bullet$ & & & & & & \\
A6. Estágio de pesquisa no exterior (BEPE) & & & & & $\bullet$ & $\bullet$ & & & & \\
A7. Otimização multiobjetivo e fronteira de Pareto (Eixo 3) & & & & & & $\bullet$ & $\bullet$ & $\bullet$ & & \\
A8. Avaliação de transferibilidade inter-scanners (Eixo 4) & & & & & & & $\bullet$ & $\bullet$ & $\bullet$ & \\
A9. Redação de artigos científicos e tese & & & & & & & & $\bullet$ & $\bullet$ & $\bullet$ \\
A10. Defesa de doutorado & & & & & & & & & & $\bullet$ \\
\bottomrule
\end{tabularx}
\end{table}

% =========================================================================
% 7. REFERÊNCIAS BIBLIOGRÁFICAS (Não contabilizadas nas 20 páginas)
% =========================================================================

---



# Referências



## Referências Bibliográficas



- **[[unscear2022]]**  UNITED NATIONS SCIENTIFIC COMMITTEE ON THE EFFECTS OF ATOMIC RADIATION (UNSCEAR). **Evaluation of medical exposure to ionizing radiation: 2020/2021 report, Scientific Annex A**. New York: United Nations, 2022.


- **[[oecd2025]]**  ORGANISATION FOR ECONOMIC CO-OPERATION AND DEVELOPMENT. **Health at a glance 2025: OECD indicators**. Paris: OECD Publishing, 2025.


- **[[icru2012]]**  INTERNATIONAL COMMISSION ON RADIATION UNITS AND MEASUREMENTS. Radiation dose and image-quality assessment in computed tomography: ICRU Report 87. **Journal of the ICRU**, v. 12, n. 1, 2012.


- **[[kanal2026]]**  KANAL, K. M.; FRUSH, D.; GINGOLD, E. et al. A decade of change in adult CT radiation doses: 2025 U.S. diagnostic reference levels. **Radiology**, v. 320, n. 1, e260322, 2026.


- **[[mccollough2026]]**  MCCOLLOUGH, C. H. Good news about CT doses [editorial]. **Radiology**, v. 320, n. 1, e261781, 2026.


- **[[barrett2015]]**  BARRETT, H. H.; MYERS, K. J.; HOESCHEN, C.; KUPINSKI, M. A.; LITTLE, M. P. Task-based measures of image quality and their relation to radiation dose and patient risk. **Physics in Medicine and Biology**, v. 60, n. 2, p. R1--R75, 2015.


- **[[shi2023]]**  SHI, Y.; WANG, G.; MOU, X. Task-based assessment of deep networks for sinogram denoising with a transformer-based observer. In: **SPIE Medical Imaging**, 2023. Disponível em: arXiv:2212.12838.


- **[[greffier2022]]**  GREFFIER, J.; FRANDON, J.; SI-MOHAMED, S.; DABLI, D.; HAMARD, A.; BELAOUNI, A.; AKESSOUL, P.; BESSE, F.; GUIU, B.; BEREGI, J.-P. Comparison of two deep learning image reconstruction algorithms in chest CT images: a task-based image quality assessment on phantom data. **Diagnostic and Interventional Imaging**, v. 103, n. 1, p. 21--30, 2022.


- **[[zhang2017]]**  ZHANG, Y.; SMITHERMAN, C.; SAMEI, E. Size-specific optimization of CT protocols based on minimum detectability. **Medical Physics**, v. 44, n. 4, p. 1301--1311, 2017.


- **[[zou2026]]**  ZOU, J.; FENWICK, D.; TAROKH, V.; FELICE, N.; RAJAGOPAL, J.; KAPADIA, A.; SAMEI, E.; NADERIALIZADEH, N.; ABADI, E. Task-Based CT Protocol Optimization Using Reinforcement Learning and Virtual Imaging Trials. **arXiv preprint arXiv:2609.13309**, 2026.


- **[[karimipourfard2026]]**  KARIMIPOURFARD, M. et al. Radiomics-informed CT protocol optimization through feature-level trade-off analysis in a phantom study. **Physics in Medicine and Biology**, v. 71, n. 12, 125006, 2026.


- **[[shunhavanich2024]]**  SHUNHAVANICH, P. et al. 3D printed phantom with 12 000 submillimeter lesions to improve efficiency in CT detectability assessment. **Medical Physics**, v. 51, n. 5, p. 3265--3274, 2024.


- **[[wilson2013]]**  WILSON, J. M. et al. A methodology for image quality evaluation of advanced CT systems. **Medical Physics**, v. 40, n. 3, 031908, 2013.


- **[[choopani2023]]**  CHOOPANI, M. R.; ABEDI, I.; DALVAND, F. Quality assessment of computed tomography images using a channelized Hotelling observer: optimization of protocols. **Radiation Physics and Chemistry**, v. 204, 110698, 2023.


- **[[costa2025]]**  COSTA, P. R. et al. Hybrid phantom for lung CT: design and validation. **Medical Physics**, v. 52, n. 8, e17990, 2025.


- **[[samei2021]]**  SAMEI, E. et al. Assessment of image quality in advanced CT scanning: Report of AAPM Task Group 233. **Medical Physics**, v. 48, n. 8, p. e754--e787, 2021.


- **[[greffier2020]]**  GREFFIER, J. et al. Image quality and dose reduction opportunity of deep learning image reconstruction algorithm for CT: a phantom study. **European Radiology**, v. 30, n. 7, p. 3951--3959, 2020.


- **[[siewerdsen2002]]**  SIEWERDSEN, J. H. et al. A framework for noise-power spectrum analysis of multidimensional images. **Medical Physics**, v. 29, n. 11, p. 2655--2671, 2002.


- **[[samei2019]]**  SAMEI, E. et al. Performance evaluation of computed tomography systems: summary of AAPM Task Group 233. **Medical Physics**, v. 46, n. 11, p. e735--e756, 2019.


- **[[barrett1993]]**  BARRETT, H. H.; YAO, J.; ROLLAND, J. P.; MYERS, K. J. Model observers for assessment of image quality. **Proceedings of the National Academy of Sciences**, v. 90, n. 21, p. 9758--9765, 1993.


- **[[zhou2019]]**  ZHOU, W.; LI, H.; ANASTASIO, M. A. Approximating the ideal observer and Hotelling observer for binary signal detection tasks by use of supervised learning methods. **IEEE Transactions on Medical Imaging**, v. 38, p. 2456--2468, 2019.


- **[[solomon2016]]**  SOLOMON, J.; SAMEI, E. Correlation between human detection accuracy and observer model-based image quality metrics in computed tomography. **Journal of Medical Imaging**, v. 3, 035506, 2016.


- **[[chakraborty2017]]**  CHAKRABORTY, D. P. **Observer Performance Methods for Diagnostic Imaging: Foundations, Modeling, and Applications with R-Based Examples**. Boca Raton: CRC Press, Taylor & Francis Group, 2017.


- **[[burgess1995]]**  BURGESS, A. E. Comparison of receiver operating characteristic and forced choice observer performance measurement methods. **Medical Physics**, v. 22, n. 5, p. 643--655, 1995.


- **[[toia2023]]**  TOIA, G. V. et al. Detectability of small low-attenuation lesions with deep learning CT image reconstruction: a 24-reader phantom study. **American Journal of Roentgenology**, v. 220, n. 2, p. 283--295, 2023.


- **[[racine2020]]**  RACINE, D. et al. Task-based characterization of a deep learning image reconstruction and comparison with filtered back-projection and a partial model-based iterative reconstruction in abdominal CT: a phantom study. **Physica Medica**, v. 76, p. 28--37, 2020.


- **[[racine2021]]**  RACINE, D. et al. Image texture, low contrast liver lesion detectability and impact on dose: deep learning algorithm compared to partial model-based iterative reconstruction. **European Journal of Radiology**, v. 141, 109808, 2021.


- **[[oostveen2021]]**  OOSTVEEN, L. J. et al. Deep learning–based reconstruction may improve non-contrast cerebral CT imaging compared to other current reconstruction algorithms. **European Radiology**, v. 31, n. 8, p. 5498--5506, 2021. DOI: 10.1007/s00330-020-07668-x.


- **[[vasconcelos2024]]**  VASCONCELOS, M. L. S. **Predição da qualidade de mamografias digitais sob a perspectiva da detectabilidade de microcalcificações: uma abordagem radiômica**. 2024. Tese (Doutorado em Física Médica) --- Instituto de Física, Universidade de São Paulo, São Paulo, 2024.


- **[[pimenta2025]]**  PIMENTA, E. B.; COSTA, P. R. Model observers and detectability index in x-ray imaging: historical review, applications and future trends. **Physics in Medicine and Biology**, v. 70, 07TR02, 2025.


- **[[pimenta2026]]**  PIMENTA, E. B. **Otimização de procedimentos de tomografia computadorizada pulmonar de baixa dose utilizando o índice de detectabilidade**. 2026. Tese (Doutorado em Física Médica) --- Instituto de Física, Universidade de São Paulo, São Paulo, 2026.


- **[[costa2025spie]]**  COSTA, P. R.; PIMENTA, E. B.; OOSTVEEN, L. J.; SECHOPOULOS, I. Comparative evaluation of noise texture and images of a synthetic lung nodule using energy-integrating and photon-counting CT. In: **Proceedings of SPIE (Medical Imaging: Physics of Medical Imaging)**, v. 13405, p. 134050X, 2025b. DOI: 10.1117/12.3048606.


- **[[fedorov2012]]**  FEDOROV, A. et al. 3D Slicer as an image computing platform for the Quantitative Imaging Network. **Magnetic Resonance Imaging**, v. 30, n. 9, p. 1323--1341, 2012.


- **[[mimics2024]]**  MATERIALISE. **Mimics Innovation Suite: Software for Biomedical Research and Medical Image Segmentation**. Leuven: Materialise NV, 2024.


- **[[boiset2023]]**  BOISET, G. R.; ROSINELLI, R. R.; FREIRE, G.; MOURA, R. A. S.; MORATTA, R.; YOSHIMURA, E. M.; COSTA, P. R. Anthropomorphic physical phantom of the thorax for image quality evaluation in computed tomography. **Physica Medica**, v. 114, 102685, 2023.


- **[[dosovitskiy2021]]**  DOSOVITSKIY, A. et al. An image is worth 16x16 words: transformers for image recognition at scale. In: **International Conference on Learning Representations (ICLR)**, 2021.


- **[[liu2021]]**  LIU, Z. et al. Swin Transformer: hierarchical vision transformer using shifted windows. In: **IEEE/CVF International Conference on Computer Vision (ICCV)**, 2021.


- **[[deb2002]]**  DEB, K. et al. A fast and elitist multiobjective genetic algorithm: NSGA-II. **IEEE Transactions on Evolutionary Computation**, v. 6, n. 2, p. 182--197, 2002.


- **[[laumanns2002]]**  LAUMANNS, M.; THIELE, L.; DEB, K.; ZITZLER, E. Combining convergence and diversity in evolutionary multiobjective optimization. **Evolutionary Computation**, v. 10, n. 3, p. 263--282, 2002.


- **[[rasmussen2006]]**  RASMUSSEN, C. E.; WILLIAMS, C. K. I. **Gaussian Processes for Machine Learning**. Cambridge: MIT Press, 2006.


- **[[mei2022]]**  MEI, K.; GEAGAN, M.; SHAPIRA, N.; LIU, L. P.; PASYAR, P.; GANG, G. J.; STAYMAN, J. W.; NOËL, P. B. PixelPrint: Three-dimensional printing of patient-specific soft tissue and bone phantoms for CT. **Medical Physics**, v. 49, n. 2, p. 825--835, 2022. DOI: 10.1002/mp.15391.


- **[[hillis2011]]**  HILLIS, S. L. et al. Power estimation for multireader ROC methods: an updated and unified approach. **Academic Radiology**, v. 18, n. 2, p. 129--140, 2011. DOI: 10.1016/j.acra.2010.09.007.


- **[[delong1988]]**  DELONG, E. R. et al. Comparing the areas under two or more correlated receiver operating characteristic curves: a nonparametric approach. **Biometrics**, v. 44, n. 3, p. 837--845, 1988.


- **[[leveque2021]]**  LÉVÊQUE, L. et al. Comparative study of the methodologies used for subjective medical image quality assessment. **Physics in Medicine and Biology**, v. 66, n. 15, 15TR02, 2021.

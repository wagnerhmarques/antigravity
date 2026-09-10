> 📅 **Data:** 2026-08-27 | 🔗 **Conexões:** [[Projeto Doutorado Direto FAPESP Wagner 2026]], [[Projeto AIR]], [[Projeto Universal CNPq]], [[Otimização Multiobjetivo em TC]], [[Phantoms Híbridos]]

## 1. Visão Geral da Matriz de Pesquisa Integrada

A investigação metodológica no âmbito da [[Fisica Medica]] e da [[tomografia-computadorizada|Tomografia Computadorizada (CT)]] desenvolvida no grupo (USP/FAPESP) articula três frentes de fomento e execução científica complementares: o projeto de Doutorado Direto de [[projeto-dd-fapesp-wagner-2026]], o Projeto AIR e o projeto financiado pelo Universal CNPq. Enquanto os projetos macro estruturais (AIR e Universal) fornecem a infraestrutura metrológica de base e a validação multicêntrica para a caracterização de desempenho de sistemas, o doutorado direto foca no desenvolvimento algorítmico avançado e na otimização multiobjetivo por inteligência artificial.

A articulação entre essas iniciativas resolve gargalos históricos na avaliação de qualidade de imagem baseada em tarefas ([[task-based-image-quality]]) e na transição de algoritmos não-lineares, como [[reconstrucao-iterativa]] e [[deep-learning-image-reconstruction|DLR]], para a prática clínica rotineira.

## 2. Eixos de Complementaridade e Alinhamento Temático

A tabela abaixo sintetiza o escopo e o papel específico de cada eixo na arquitetura de pesquisa integrada:

| Iniciativa de Pesquisa | Foco Metrológico Principal | Contribuição Estrutural para o Ecossistema | Relação com a [[Fisica Medica]] |
| :--- | :--- | :--- | :--- |
| **Projeto AIR** | Harmonização multicêntrica de protocolos e plataformas de tomografia | Fornece dados empíricos de variabilidade inter-fabricantes (múltiplos tomógrafos) | Padronização de métricas físicas em escala clínica |
| **Universal CNPq** | Infraestrutura base e automação de metrologia física clássica | Validação de referências metrológicas para NPS, TTF e $d'$ clássico | Sustentação da cadeia de rastreabilidade física |
| **Doutorado Direto ([[projeto-dd-fapesp-wagner-2026]])** | [[deep-learning-model-observer]] e [[otimizacao-multiobjetivo-tc]] | Introduz observadores neurais com atenção e otimização por Fronteira de Pareto ($\varepsilon$-dominância) | Inovação em algoritmos preditivos e otimização de dose |

## 3. Integração Prática entre Metrologia Física e Observadores Neurais

O projeto de Doutorado Direto expande os alicerces metrológicos estabelecidos pelas vertentes AIR e CNPq através de três frentes de acoplamento direto:

1. **Superação da Dependência de Fantons Físicos via [[phantoms-hibridos]]:**
   Enquanto os projetos gerais utilizam fantons modulares padrão para aferir o [[noise-power-spectrum|espectro-de-potencia-de-ruido-nps]] e a [[task-transfer-function|ttf-task-transfer-function]], o doutorado direto emprega [[phantoms-hibridos]] antropomórficos acoplados a simulações numéricas para treinar redes de aprendizado profundo, permitindo avaliar a detectabilidade ($d'$) em anatomias complexas sem exaustão de tempo de bancada.

2. **Calibração Psicofísica com Especialistas (Estudos [[2afc-observer-study]]):**
   A validação dos observadores neurais ([[deep-learning-model-observer]]) alimentados pelas métricas dos projetos AIR e CNPq é calibrada diretamente contra a resposta perceptual humana obtida de leitores clínicos especialistas, garantindo alta correlação com a acurácia diagnóstica real.

3. **Formulações de Otimização Multiobjetivo da Tríade $(D, T, W)$:**
   Utilizando o índice de detectabilidade ($d'$) derivado do arcabouço metrológico geral, o projeto de doutorado aplica algoritmos como o [[nsga-ii]] para resolver o problema de otimização multiobjetivo:

   

$$
\min_{\mathbf{p} \in \Omega} \left\{ D(\mathbf{p}), \, T(\mathbf{p}), \, -W(\mathbf{p}) \right\}
$$

   Onde $D$ representa a dose de radiação ([[metricas-de-dose-tc|ctdivol]]/DLP), $T$ o tempo operacional computacional e $W$ o desempenho diagnóstico quantificado pelo $d'$ otimizado. Isso eleva os resultados dos projetos base a uma ferramenta de tomada de decisão clínica em tempo real.

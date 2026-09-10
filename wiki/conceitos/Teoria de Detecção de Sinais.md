---
tipo: conceito
aliases: [teoria-de-deteccao-de-sinais, SDT, Signal Detection Theory]
tags: [fisica-medica, tomografia-computadorizada, qualidade-de-imagem, observadores-de-modelo]
data: 2026-08-25
---

# teoria-de-deteccao-de-sinais

## 1. Definição Conceitual e Fundamentação Física
A **Teoria de Detecção de Sinais** (*Signal Detection Theory* - SDT), formalizada inicialmente nas décadas de 1940 e 1950 no contexto de engenharia de telecomunicações e psicofísica, constitui a fundação matemática e conceitual para a avaliação da qualidade de imagem baseada em tarefas (*task-based image quality*) na física médica moderna e na Tomografia Computadorizada (TC). No escopo da imagem diagnóstica, a SDT modela o processo de tomada de decisão — seja por um observador humano (radiologista) ou por um observador computacional — ao tentar discernir a presença de um sinal de interesse (por exemplo, uma microcalcificação, um nódulo pulmonar incipiente ou uma lesão hepática hipodensa) imerso em um fundo estocástico ruidoso (ruído quântico, granulosidade anatômica e artefatos de reconstrução).

A premissa central da SDT é que o sistema visual humano ou o algoritmo de detecção não opera em um vácuo determinístico, mas deve lidar com distribuições probabilísticas sobrepostas de "ruído puro" ($H_0$: ausência de sinal) e "sinal mais ruído" ($H_1$: presença de sinal). O desempenho da detecção não é, portanto, governado apenas pela intensidade nominal do contraste, mas pela separabilidade estatística entre essas duas hipóteses, quantificada de maneira rigorosa por métricas como o índice de detectabilidade ($d'$) e avaliada por meio de Curvas de Característica de Operação do Receptor (ROC).

## 2. Formulação Matemática e Propriedades
Matematicamente, seja $g(\mathbf{r})$ a imagem bidimensional ou tridimensional reconstruída, onde $\mathbf{r}$ representa o vetor de coordenadas espaciais. A tarefa de detecção de um sinal conhecido exatamente em localização e morfologia (TASK: *Signal Known Exactly* - SKE) em um fundo de ruído estacionário pode ser formulada testando duas hipóteses estatísticas:

$$
\begin{aligned}
H_0 &: g(\mathbf{r}) = n(\mathbf{r}) \quad \text{(Apenas Ruido)} \H_1 &: g(\mathbf{r}) = s(\mathbf{r}) + n(\mathbf{r}) \quad \text{(Sinal + Ruido)}
\end{aligned}
$$

Onde $s(\mathbf{r})$ é o sinal determinístico a ser detectado e $n(\mathbf{r})$ é a realização do campo aleatório estocástico que descreve o ruído e a textura anatômica, tipicamente caracterizado por sua função de densidade de potência de ruído (*Noise Power Spectrum* - NPS).

Para um observador ideal linear (como o Observador de Hotelling), a estatística de teste scalar $\lambda$ é obtida através de uma operação de filtragem linear acoplada ao vetor de dados da imagem $\mathbf{g}$:

$$
\lambda = \mathbf{w}^T \mathbf{g}
$$

Onde o vetor peso $\mathbf{w}$ para o observador de Hotelling é definido considerando a matriz de covariância do ruído e da textura $\mathbf{K}$ e o vetor de sinal $\mathbf{s}$:

$$
\mathbf{w} = \mathbf{K}^{-1} \mathbf{s}
$$

A métrica de desempenho máximo predita pela SDT para esta tarefa é o **índice de detectabilidade de Hotelling** ($d'_H$), que expressa a distância estatística normalizada entre as médias das hipóteses sob a métrica de Mahalanobis:

$$
d'_H = \left[ \mathbf{s}^T \mathbf{K}^{-1} \mathbf{s} \right]^{1/2}
$$

No domínio contínuo, utilizando a densidade espectral de potência do ruído $W(\mathbf{u})$ e a transformada de Fourier do sinal $S(\mathbf{u})$, o desempenho do observador ideal pode ser reescrito na frequência espacial $\mathbf{u}$ como:

$$
(d')^2 = \iint_{-\infty}^{\infty} \frac{|S(\mathbf{u})|^2 \cdot |\text{TTF}(\mathbf{u})|^2}{W(\mathbf{u})} d\mathbf{u}
$$

onde $\text{TTF}(\mathbf{u})$ representa a função de transferência de tarefa (*Task Transfer Function*), acoplando a resolução espacial do sistema de TC diretamente à mecânica estocástica da detecção descrita pela SDT.

## 3. Contexto no Acervo do Pesquisador & Aplicações
No acervo de pesquisas do grupo USP/FAPESP, a **teoria-de-deteccao-de-sinais** atua como o alicerce conceitual para transicionar a avaliação de imagens de tomografia computadorizada de métricas puramente visuais ou físicas isoladas (como a MTF ou o desvio padrão do ruído) para métricas de desempenho baseadas em tarefas clínicas reais. 

Conforme documentado em [[model-observers-and-detectability-index-in-x-ray-imaging.md]], a SDT permite fundamentar objetivamente a otimização de protocolos de aquisição e varredura. Na síntese sobre [[indice-de-detectabilidade-em-tomografia-computadorizada.md]], o índice $d'$ derivado da SDT substitui avaliações subjetivas na quantificação do impacto de algoritmos avançados, como a reconstrução iterativa e a reconstrução baseada em inteligência artificial/deep learning ([[Deep Learning Image Reconstruction (DLR)|deep-learning-image-reconstruction]]).

Além disso, nas discussões metodológicas presentes no documento `queries/Comente sobre a evolução dos modelos de observadores computacionais. Preciso entender como se deu o avanço...md`, a SDT é o ponto de partida para a evolução dos [[Observadores de Modelo (Model Observers)|observadores-de-modelo]], permitindo que limitações de não-linearidade introduzidas por reconstruções iterativas avançadas sejam contornadas por meio de observadores baseados em canais e abordagens de aprendizado profundo ([[Deep Learning Model Observer|deep-learning-model-observer]]). A formulação clássica da SDT garante que a validação física e a otimização de dose ([[Otimização de Dose em TC|otimizacao-de-dose-em-tc]]) estejam estritamente correlacionadas à detectabilidade de lesões reais em exames de TC.

## 4. Conexões e Wikilinks
- [[Índice de Detectabilidade|indice-de-detectabilidade]]
- [[Observadores de Modelo (Model Observers)|observadores-de-modelo]]
- [[Task Based Image Quality|task-based-image-quality]]
- [[Noise Power Spectrum|noise-power-spectrum]]
- [[Task Transfer Function|task-transfer-function]]
- [[Deep Learning Model Observer|deep-learning-model-observer]]
- [[Otimização de Dose em TC|otimizacao-de-dose-em-tc]]
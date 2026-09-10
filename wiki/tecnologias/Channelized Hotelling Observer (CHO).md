---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, avaliacao-de-imagem, observadores-matematicos, percepcao-visual, otimizacao]
data: 2026-08-25
---

# cho-model-observer

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **Channelized Hotelling Observer (CHO)**, ou **Observador de Hotelling Canalizado**, é um modelo matemático computacional avançado projetado para simular o desempenho de observadores humanos na tarefa de detecção e discriminação de sinais visuais, com ênfase primordial em imagens médicas de diagnóstico, como aquelas geradas por Tomografia Computadorizada (TC).

No domínio da Física Médica e da metrologia de imagens, a avaliação da qualidade de imagem tradicionalmente dependia de métricas puramente físicas de baixo nível, tais como a Função de Transferência de Modulação (MTF), o Espectro de Potência de Ruído (NPS) e a Relação Sinal-Ruído (SNR). Embora fundamentais, essas métricas frequentemente falham em prever com precisão a detectabilidade de lesões reais por leitores humanos, uma vez que não incorporam as propriedades espaciais e espectrais do sistema visual humano (HVS).

O observador ideal de Hotelling (IO) maximiza a detectabilidade estatística para tarefas de detecção de sinais conhecidos em fundo conhecido (SKE/BK) com ruído gaussiano. Contudo, o observador ideal falha ao ser aplicado diretamente a imagens de alta dimensionalidade (como matrizes de TC de $512 \times 512$ ou superiores) devido à sobreparametrização e à incapacidade de modelar a seletividade espacial e a limitação de largura de banda do HVS. O **CHO** resolve essa limitação introduzindo um conjunto de canais de frequência espacial (filtros band-pass) que reduzem a dimensionalidade dos dados e emulam a percepção retiniana e cortical humana, seguido por uma etapa de classificação linear de Hotelling.

## 2. Formulação Matemática e Propriedades

Seja $g$ um vetor coluna de dimensão $M \times 1$ que representa a imagem digitalizada (ou uma região de interesse - ROI) vetorizada. O objetivo do observador é computar uma estatística de decisão scalar $t(g)$ que determine a presença ou ausência de um sinal.

### A Transformação por Canais (Channeling)
O vetor de imagem $g$ é inicialmente processado por um banco de $K$ filtros de canal (onde $K \ll M$). Seja $U$ uma matriz de transformação de canais de dimensões $M \times K$, cujas colunas representam os perfis dos canais (frequentemente funções de diferença de gaussianas - DoG, ou funções de Gabor). O vetor de características do canal $v$ de dimensão $K \times 1$ é obtido por:

$$
v = U^T g
$$

### O Classificador de Hotelling
No espaço reduzido de canais, o observador de Hotelling calcula a estatística de decisão $t(v)$ maximizando a razão entre a variância inter-classes e a variância intra-classes (critério de Fisher-Hotelling):

$$
t(v) = w^T v = w^T U^T g
$$

O vetor de pesos ótimos $w$ (de dimensão $K \times 1$) é definido por:

$$
w = K_v^{-1} \Delta v
$$

Onde:
* $\Delta v = \bar{v}_s - \bar{v}_b$ é a diferença entre os vetores médios de canal para a classe com sinal ($\bar{v}_s$) e a classe de fundo puro (fundo sem sinal, $\bar{v}_b$).
* $K_v$ é a matriz de covariância combinada dos canais, calculada tipicamente como a média das matrizes de covariância sob as hipóteses de presença e ausência de sinal:

$$
K_v = \frac{1}{2} \left( K_{v,s} + K_{v,b} \right)
$$

### Medida de Desempenho: Detectability Index ($d'$)
A performance do CHO é quantificada pelo Índice de Detectabilidade ($d'$), análogo à métrica $d'$ da Teoria de Detecção de Sinais:

$$
d' = \sqrt{\Delta v^T K_v^{-1} \Delta v}
$$

O valor de $d'$ pode ser mapeado diretamente para a Área Sob a Curva ROC (AUC) através da função distribuição cumulativa normal padrão $\Phi(\cdot)$:

$$
\text{AUC} = \Phi\left(\frac{d'}{2}\end{\right)}
$$

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Na Tomografia Computadorizada moderna, o CHO desempenha um papel central nos processos de otimização de protocolos de aquisição e reconstrução de imagem, especialmente com a ascensão de algoritmos de Reconstrução Iterativa (IR) e Reconstrução Baseada em Aprendizado Profundo (DLR - *Deep Learning Reconstruction*).

1. **Otimização de Dose e Qualidade de Imagem:** Métricas tradicionais de ruído (como desvio padrão em ROI) são insuficientes para avaliar algoritmos de DLR que introduzem texturas de ruído não-estacionárias e dependentes da dose. O CHO permite correlacionar diretamente a dose de radiação e os parâmetros de reconstrução com a detectabilidade clínica real de lesões sutiles (ex: nódulos pulmonares precoces, metástases hepáticas hipodensas).
2. **Sintonização de Hiperparâmetros:** Algoritmos de reconstrução iterativa contêm parâmetros de regularização (penalização espacial). O CHO é utilizado em bancadas de teste virtuais para encontrar o ponto ótimo de suavização que preserva a detectabilidade do sinal sem introduzir artefatos de textura indesejados.
3. **Substituição de Estudos de Percepção Humana (ROC/LROC):** Estudos de ROC com leitores humanos são dispendiosos\, demorados e sujeitos à fadiga do observador. O CHO validado estatisticamente atua como um substituto preditivo altamente correlacionado com o desempenho humano, permitindo varreduras paramétricas automatizadas.

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|computed-tomography]]
* [[Image Reconstruction|image-reconstruction]]
* [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction]]
* [[Noise Power Spectrum|noise-power-spectrum]]
* [[Modulation Transfer Function (MTF)|modulation-transfer-function]]
* [[Task Based Image Quality|task-based-image-quality]]
* [[Análise ROC|roc-analysis]]
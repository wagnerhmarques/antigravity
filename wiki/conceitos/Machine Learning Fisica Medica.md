---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, machine-learning, inteligencia-artificial, reconstrucao-de-imagem, dosimetria, metrologia]
data: 2026-08-25
---

# machine-learning-fisica-medica

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O termo **Machine Learning em Física Médica** refere-se à intersecção entre algoritmos de aprendizado estatístico computacional, modelagem preditiva e os princípios fundamentais da física de radiação, imagem médica e metrologia das radiações. Na prática clínica e de investigação, sua aplicação transcende o processamento de imagem convencional, integrando-se diretamente à cadeia de aquisição, processamento, reconstrução e garantia da qualidade (QA) em modalidades de imagem diagnóstica e terapia.

Do ponto de vista metrológico, a introdução de modelos baseados em *Machine Learning* (ML) e *Deep Learning* (DL) exige uma reavaliação rigorosa dos conceitos de incerteza de medição, rastreabilidade dosimétrica e viés algorítmico (*algorithmic bias*). Enquanto a física médica tradicional fundamenta-se em soluções determinísticas para a equação de transporte de radiação (como simulações de Monte Carlo e formalismos analíticos baseados na Equação de Radon), o aprendizado de máquina introduz abordagens estocásticas baseadas em dados empíricos. Isso gera desafios específicos para a aceitação regulatória e metrológica: a preservação da fidelidade quantitativa das imagens médicas — onde cada pixel ou voxel representa um coeficiente de atenuação linear mapeado em unidades Hounsfield ($\text{UH}$) — não pode ser comprometida por artefatos de alucinação gerados por redes neurais profundas.

Portanto, a fundamentação física exige que os modelos de ML respeitem leis de conservação da energia, restrições radiométricas e modelos cinéticos e de atenuação física (como a lei de Beer-Lambert), garantindo que a otimização da dose de radiação e a precisão diagnóstica ocorram sem perda de determinismo físico essencial.

---

## 2. Formulação Matemática e Propriedades

O aprendizado de máquina em física médica formula-se, de maneira geral, como um problema de otimização estocástica ou de mapeamento não linear de espaços de alta dimensionalidade.

Seja $\mathbf{x} \in \mathbb{R}^{N}$ o espaço de entrada (por exemplo, projeções sinogramas corrompidas por ruído quântico e subamostragem em Tomografia Computadorizada) e $\mathbf{y} \in \mathbb{R}^{M}$ o espaço de saída desejado (imagens reconstruídas de alta resolução com dose padrão). O objetivo é encontrar uma função parametrizada $\mathcal{F}_{\boldsymbol{\theta}}: \mathbb{R}^{N} \to \mathbb{R}^{M}$, onde $\boldsymbol{\theta}$ representa o conjunto de parâmetros treináveis (pesos e vieses).

A otimização desses parâmetros é realizada minimizando uma função de perda empírica $\mathcal{L}(\boldsymbol{\theta})$ sobre um conjunto de dados de treinamento $\mathcal{D} = \{(\mathbf{x}_i, \mathbf{y}_i)\}_{i=1}^{K}$:

$$
\mathcal{L}(\boldsymbol{\theta}) = \frac{1}{K} \sum_{i=1}^{K} \mathcal{D}_{\text{loss}}\left( \mathcal{F}_{\boldsymbol{\theta}}(\mathbf{x}_i), \mathbf{y}_i \right) + \lambda \mathcal{R}(\boldsymbol{\theta})
$$

Onde $\mathcal{D}_{\text{loss}}$ mede a divergência entre a predição e o ground truth (como o Erro Quadrático Médio - MSE, Erro Absoluto Médio - MAE, ou perdas perceptuais baseadas em redes adversariais), e $\mathcal{R}(\boldsymbol{\theta})$ é um termo de regularização (como a norma $L_1$ ou $L_2$) parametrizado pelo hiperparâmetro de regularização $\lambda$.

Em contextos de reconstrução iterativa profunda (*Deep Learning Reconstruction* - DLR) aplicada à Tomografia Computadorizada, a formulação frequentemente incorpora o modelo de aquisição física direto $\mathbf{A}$ (matriz do sistema que modela a geometria do feixe cônico, espalhamento e atenuação):

$$
\min_{\boldsymbol{\theta}} \mathbb{E}_{(\mathbf{y}, \mathbf{p})} \left[ \left\| \mathcal{F}_{\boldsymbol{\theta}}(\mathbf{A}\mathbf{y} + \mathbf{n}) - \mathbf{y} \right\|_p^p \right]
$$

Onde $\mathbf{p}$ representa os dados brutos (sinograma), $\mathbf{A}\mathbf{y}$ é a projeção linear ideal, e $\mathbf{n}$ modela o ruído estatístico de Poisson associado aos fótons detectados, conforme a estatística de contagem de fótons:

$$
P(N_i) = \frac{\exp(-\bar{N}_i)(\bar{N}_i)^{N_i}}{N_i!}
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

As aplicações de Machine Learning em Tomografia Computadorizada (TC) revolucionaram o tripé fundamental da modalidade: **qualidade de imagem, dose de radiação e tempo de escaneamento**.

1. **Reconstrução Baseada em Aprendizado Profundo (DLR):**
   Modelos de DLR substituem ou complementam métodos analíticos tradicionais (como a Retroprojeção Filtrada - FBP) e abordagens iterativas estatísticas (IR). Eles removem ruídos e artefatos de feixe endurecido (*beam hardening*) e estrias por subamostragem sem suprimir detalhes anatômicos finos ou texturas de pequeno porte, mantujući a exatidão quantitativa das unidades Hounsfield.

2. **Otimização de Dose e Dosimetria Preditiva:**
   Algoritmos de aprendizado supervisionado são empregados para prever mapas de dose de radiação tridimensionais em órgãos de risco e tecidos fantomas com base em parâmetros de varredura (mAs, kVp, pitch, espessura de corte e filtros de reconstrução). Isso permite a dosimetria personalizada em tempo real e o ajuste dinâmico do produto corrente-tempo ($mAs$) por meio de modulação de corrente guiada por inteligência artificial.

3. **Controle de Qualidade (QA) Automatizado e Radiômica:**
   Redes neurais convolucionais (CNNs) e modelos de visão computacional monitoram a estabilidade de scanners de TC analisando imagens de fantomas de controle de qualidade (ex: fantomas AAPM ou ACR). Avaliam automaticamente métricas como modulação da função de transferência (MTF), ruído, linearidade de número TC e artefatos de anel, reduzindo a variabilidade inter-observador.

4. **Observadores Computacionais e Avaliação de Imagem:**
   Modelos de ML simulam o desempenho de observadores humanos (tarefas de detecção e discriminação baseadas na Teoria da Detecção de Sinais) para otimizar protocolos de aquisição de TC com foco na detectabilidade de lesões de baixo contraste.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|tomografia-computadorizada]]
* [[Reconstrução de Imagem|reconstrucao-de-imagem]]
* [[dosimetria-radiologica]]
* [[Controle de Qualidade em TC|controle-de-qualidade-tc]]
* [[inteligencia-artificial-medicina]]
* [[fbp-iterative-reconstruction]]
* [[Unidades Hounsfield|unidades-hounsfield]]
* [[radiomica-fisica-medica]]
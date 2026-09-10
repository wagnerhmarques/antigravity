---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, processamento-de-imagem, filtragem-espacial, reconstrucao-de-imagem, IA]
data: 2026-08-25
---

# filtragem-espacial

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **filtragem-espacial** é uma operação fundamental de processamento de imagem aplicada diretamente no domínio espacial de uma matriz digital bidimensional (ou tridimensional) em Tomografia Computadorizada (TC). Fisicamente, o processo consiste na modificação dos valores de intensidade de cada pixel ou voxel de uma imagem com base nos valores dos pixels situados em sua vizinhança geométrica imediata. Esta técnica constitui a base para a modulação da resolução espacial, supressão de ruído quântico e realce de bordas em imagens médicas antes ou depois da reconstrução tomográfica propriamente dita.

Metrologicamente, a filtragem espacial atua como um sistema linear e espacialmente invariante (LSI), desde que implementada na forma de convolução linear. O objetivo primordial na física da imagem diagnóstica é otimizar a balança entre a **resolución espacial** (capacidade de distinguir estruturas pequenas de alto contraste) e a **relação sinal-ruído (SNR)**. Na TC, onde o ruído estatístico decorrente da contagem de fótons de raios X é proeminente, a filtragem espacial atua frequentemente como um filtro passa-baixas para suavização (redução de ruído, com penalização da resolução) ou como um filtro passa-altas/realce para enfatizar interfaces anatômicas de alta frequência espacial (como trabeculado ósseo ou microcalcificações pulmonares).

Historicamente e algoritmicamente, a filtragem espacial na TC está profundamente interligada ao processo de **Retroprojeção Filtrada (FBP)**. O teorema da fatia central estabelece que a projeção filtrada no domínio espacial por meio de filtros de rampa (como *Ram-Lak*, *Hamming*, *Hann*) corrige o desfoque inerente à retroprojeção simples ($1/r$). Embora essa filtragem analítica ocorra tipicamente no domínio da frequência (via Transformada Rápida de Fourier - FFT), a implementação de pós-processamentos clínicos (como filtros de suavização de tecidos moles ou filtros de alta definição para ossos) é executada diretamente no domínio espacial por meio de máscaras de convolução (kernels).

---

## 2. Formulação Matemática e Propriedades

Matematicamente, a filtragem espacial linear de uma imagem digital $f(x, y)$ por uma máscara ou núcleo de convolução (kernel) $h(x, y)$ de tamanho $(2k+1) \times (2k+1)$ é definida pela operação integral de convolução discreta:

$$
g(x, y) = f(x, y) * h(x, y) = \sum_{i=-k}^{k} \sum_{j=-k}^{k} f(x - i, y - j) \, h(i, j)
$$

Onde:
- $g(x, y)$ é a imagem resultante filtrada.
- $f(x, y)$ é a imagem original de entrada (em unidades Hounsfield - HU, por exemplo).
- $h(i, j)$ representa os coeficientes do filtro espacial (pesos da vizinhança).

### Resposta ao Impulso e Função de Transferência de Modulação (MTF)
Um filtro espacial é completamente caracterizado por sua resposta ao impulso espacial $h(x, y)$. Aplicando a Transformada de Fourier bidimensional $\mathcal{F}\{\cdot\}$, obtém-se a Função de Transferência óptica ou do Sistema (OTF), cuja magnitude define a **Função de Transferência de Modulação (MTF)**:

$$
\text{MTF}(u, v) = \left| \mathcal{\iint}_{-\infty}^{\infty} h(x, y) e^{-j 2\pi (ux + vy)} \, dx \, dy \right|
$$

Em termos metrológicos, a filtragem espacial altera a MTF do sistema de imagem:
- **Filtros Passa-Baixas (Suavização):** Atenuam as componentes de alta frequência espacial $(u, v)$, reduzindo o ruído padrão $\sigma_{\text{ruído}}$, mas degradando a MTF (menor resolução espacial).
- **Filtros Passa-Altas (Realce):** Amplificam as altas frequências, elevando a MTF em limites de resolução, porém provocando amplificação do ruído e artefatos de transição (*overshoot/undershoot*).

### Filtragem Espacial Não-Linear
Quando as propriedades estatísticas do ruído em TC são não-estacionárias (dependentes da dose e da atenuação local do paciente), filtros espaciais lineares tornam-se subótimos, pois geram borramento em bordas agudas. Nesses cenários, utilizam-se filtros espaciais não-lineares, como o **Filtro Mediana** ou algoritmos de **Filtração Baseada em Borda (Edge-Preserving Filters)**, a exemplo do filtro bilateral:

$$
g(x, y) = \frac{1}{W_p} \sum_{i,j \in \Omega} f(i, j) \, g_s(\lVert(i,j) - (x,y)\rVert) \, g_r(\left|f(i,j) - f(x,y)\right|)
$$

Onde $g_s$ representa a função de proximidade espacial e $g_r$ a função de similaridade radiométrica (diferença de intensidade), preservando descontinuidades anatômicas abruptas enquanto remove ruído flutuante.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A filtragem espacial desempenha um papel crítico em diversas etapas do fluxo de trabalho e controle de qualidade em Tomografia Computadorizada:

1. **Seleção de Kernels de Reconstrução:** Na aquisição helicoidal ou axial, os dados brutos (*sinograma*) são multiplicados por filtros espaciais antes da retroprojeção. A escolha do kernel (ex: *soft tissue* vs. *bone kernel*) determina diretamente o compromisso clínico entre resolução de alto contraste (foco em patologias pulmonares ou ortopédicas) e baixo ruído (foco em contraste de parênquima cerebral ou abdominal).
2. **Otimização de Dose (ALARA):** Com a redução drástica da corrente do tubo (mAs) para minimizar a dose de radiação ionizante ao paciente, o nível de ruído quântico e artefatos de estrias aumentam exponencialmente. Filtros espaciais avançados (incluindo abordagens iterativas e de aprendizado profundo) são aplicados para restaurar a qualidade diagnóstica sem aumentar a exposição radiológica.
3. **Controle de Qualidade (CQ) Metrológico:** A avaliação da MTF e da Distância de Resolução Espacial Limite (ex: em frequências de 10%, 50% da MTF) em imagens de fantomas (fantasmas de teste de QA, como o ACR) depende de operações de filtragem espacial para extração de perfis de linha e cálculo da Função de Espalhamento de Ponto (PSF).
4. **Interface com Inteligência Artificial (IA):** Redes Neurais Convolucionais (CNNs) utilizadas em Redução de Ruído Baseada em Aprendizado Profundo (*Deep Learning Reconstruction* - DLR) operam conceitualmente como filtros espaciais adaptativos de alta complexidade e não-linearidade, aprendidos a partir de grandes bases de dados de alta versus baixa dose.

---

## 4. Conexões e Wikilinks

- [[retroprojetor-filtrado]]
- [[Modulation Transfer Function (MTF)|funcao-de-transferencia-de-modulacao-mtf]]
- [[ruido-quantico-tc]]
- [[Teorema da Fatia Central|teorema-da-fatia-central]]
- [[Reconstrução Iterativa|reconstrucao-iterativa]]
- [[dose-de-radiacao-em-tc]]
- [[Artefatos em TC|artefatos-em-tomografia]]
- [[Processamento de Imagens Médicas|processamento-de-imagem-medica]]
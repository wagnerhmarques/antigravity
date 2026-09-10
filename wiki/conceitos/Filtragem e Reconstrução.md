---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-de-imagem, processamento-de-sinal, fbp, inteligencia-artificial]
data: 2026-08-25
---

# filtragem-e-reconstrucao

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O binômio **filtragem-e-reconstrucao** representa o núcleo computacional e físico responsável por transformar os dados brutos de atenuação — coletados pelos detectores de um sistema de Tomografia Computadorizada (TC) ao longo de múltiplas projeções angulares — em uma matriz tridimensional de coeficientes de atenuação linear espacialmente resolvidos (representados em imagens tomográficas bidimensionais). 

Do ponto de vista da física médica e da metrologia de imagem, a aquisição tomográfica mede a integral de linha do coeficiente de atenuação linear $\mu(x,y)$ de um objeto ao longo de trajetórias de raios X, conforme formalizado pela **Transformada de Radon**. A reconstrução direta por retroprojeção (*Simple Backprojection* - SBP), contudo, sofre intrinsecamente de um desfoque espacial severo, modelado matematicamente como uma convolução no domínio espacial com um núcleo do tipo $\frac{1}{r}$, o que gera uma atenuação de altas frequências espaciais e uma perda drástica de resolução horizontal e vertical.

Para mitigar esse artefato físico e matemático, introduz-se a etapa de **filtragem**. No contexto da técnica padrão de **Retroprojeção Filtrada** (*Filtered Backprojection* - FBP), as projeções unidimensionais obtidas em cada ângulo são submetidas a um filtro de rampa (*ramp filter*) no domínio de Fourier (ou sua equivalente implementação espacial via convolução) antes de serem retroprojetadas. Este filtro amplifica as altas frequências espaciais de modo a compensar exatamente o desfoque $\frac{1}{r}$ da retroprojeção simples. 

Metrologicamente, a filtragem e a reconstrução determinam diretamente a função de dispersão do ponto (*Point Spread Function* - PSF), a função de transferência de modulação (*Modulation Transfer Function* - MTF), o ruído textural (quantificado pelo espectro de potência do ruído - *Noise Power Spectrum* - NPS) e a detectabilidade de lesões em baixos contrastes. Com a evolução tecnológica, os métodos estritamente analíticos foram complementados por abordagens de reconstrução iterativa (IR) e algoritmos baseados em Inteligência Artificial e Aprendizado Profundo (*Deep Learning Reconstruction* - DLR), onde a filtragem deixa de ser um operador fixo (como o filtro de Hann, Hamming ou Shepp-Logan) para se tornar um operador não-linear adaptativo baseado em aprendizado de máquina.

## 2. Formulação Matemática e Propriedades

A formulação matemática clássica da filtragem e reconstrução baseia-se no **Teorema da Fatia Central** (*Central Slice Theorem*), que estabelece que a Transformada de Fourier 1D de uma projeção paralela obtida em um ângulo $\theta$ corresponde a uma linha que passa pela origem na Transformada de Fourier 2D do objeto $\mu(x,y)$ sob o mesmo ângulo $\theta$.

Seja $p_\theta(t)$ a projeção paralela obtida na posição $t$ e no ângulo $\theta$, definida pela Transformada de Radon:

$$
p_\theta(t) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \mu(x,y) \, \delta(x \cos\theta + y \sin\theta - t) \, dx \, dy
$$

A Transformada de Fourier 1D de $p_\theta(t)$ em relação à coordenada espacial $t$ é dada por:

$$
P_\theta(\omega) = \mathcal{F}\{p_\theta(t)\} = \int_{-\infty}^{\infty} p_\theta(t) e^{-j 2 \pi \omega t} \, dt
$$

Onde $\omega$ representa a frequência espacial. O Teorema da Fatia Central garante que:

$$
S(\omega \cos\theta, \omega \sin\theta) = P_\theta(\omega)
$$

Onde $S(K_x, K_y)$ é a Transformada de Fourier 2D de $\mu(x,y)$. Para recuperar a imagem $\mu(x,y)$ no domínio espacial através da inversão da transformada polar para cartesiana, surge um fator jacobiano $|\omega|$ (em coordenadas polares). Portanto, a reconstrução exata requer a aplicação de um filtro rampa $|\omega|$ antes da retroprojeção:

$$
\mu(x,y) = \int_{0}^{\pi} \left[ \int_{-\infty}^{\infty} P_\theta(\omega) |\omega| e^{j 2 \pi \omega t} \, d\omega \right]_{\substack{t = x \cos\theta + y \sin\theta}} \, d\theta
$$

Em termos de convolução no domínio espacial, a operação de filtragem de cada projeção $p_\theta(t)$ com um núcleo de filtro $q(t)$ (derivado da transformada inversa do filtro de rampa multiplicado por uma janela de apodização para controle de ruído) é expressa por:

$$
\tilde{p}_\theta(t) = p_\theta(t) * q(t) = \int_{-\infty}^{\infty} p_\theta(\tau) q(t - \tau) \, d\tau
$$

Onde o núcleo do filtro de rampa ideal no domínio espacial é dado por funções generalizadas que oscilam, exigindo o uso de janelas de suavização (como o filtro de Hann ou Hamming) para limitar a amplificação excessiva de ruído quântico de alta frequência:

$$
Q(\omega) = |\omega| \cdot W(\omega)
$$

sendo $W(\omega)$ a função de janela. Nos métodos modernos de reconstrução iterativa estatística (建模 - Model-based Iterative Reconstruction, MBIR) e DLR, a equação de otimização minimiza uma função custo da forma:

$$
\hat{\mu} = \arg\min_{\mu} \left\{ \frac{1}{2} \|y - A\mu\|_2^2 + \beta R(\mu) \right\}
$$

onde $y$ representa os dados de projeção ruidosos, $A$ é o operador do sistema (matriz de projeção física), $R(\mu)$ é o termo de regularização (função de penalização ou prior espacial) e $\beta$ é o hiperparâmetro de正则ização que controla o balanço entre resolução espacial e supressão de ruído (filtragem implícita não-linear).

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

O processo de **filtragem-e-reconstrucao** é determinante para a prática clínica e o cumprimento dos princípios de radioproteção (ALARA - *As Low As Reasonably Achievable*):

* **Controle de Qualidade (CQ) e Metrologia:** Os mantenedores de física médica utilizam imagens de fantasmas (*phantoms*) para avaliar como diferentes kernels de reconstrução afetam a resolução espacial (MTF) e o ruído (desvio padrão em regiões de interesse). Um filtro muito agudo (*sharp kernel*, ex. para osso) maximiza a resolutibilidade de micro-estruturas trabeculares, mas degrada a relação sinal-ruído (SNR). Um filtro suave (*soft kernel*, ex. para tecido mole/fígado) reduz o ruído, permitindo a detecção de lesões de baixo contraste, às custas de borrar bordas anatômicas.
* **Otimização de Dose e Redução de Ruído:** Com a introdução de algoritmos avançados de Inteligência Artificial (redes neurais convolucionais e modelos generativos aplicados à reconstrução), a etapa tradicional de filtragem analítica é substituída ou aprimorada por redes treinadas para remover o ruído de Poisson característico de exibições de baixa dose (*low-dose CT*), preservando a textura anatômica sem os artefatos de borramento típicos dos filtros lineares tradicionais.
* **Redução de Artefatos:** A filtragem adequada das projeções atua diretamente na atenuação de artefatos de meio de contraste, endurecimento de feixe (*beam hardening*), e artefatos de c_utoff_ ou aliasing decorrentes de amostragem insuficiente no espaço de Radon.
* **Observadores Computacionais:** A avaliação rigorosa de cadeias de filtragem e reconstrução emprega frequentemente observadores ideais e humanos simulados (*Channelized Hotelling Observers* - CHO) para correlacionar parâmetros de reconstrução com a detectabilidade clínica real de lesões nodulares pulmonares ou hepáticas.

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|tomografia-computadorizada]]
* [[Transformada de Radon|transformada-de-radon]]
* [[Retroprojeção Filtrada (FBP)|retroprojecao-filtrada]]
* [[Reconstrução Iterativa|reconstrucao-iterativa]]
* [[Deep Learning Image Reconstruction (DLR)|inteligencia-artificial-em-tc]]
* [[funcao-de-transferencia-de-modulacion-mtf]]
* [[Noise Power Spectrum|espectro-de-potencia-do-ruido-nps]]
* [[otimizacion-de-dose]]
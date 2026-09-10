---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-de-imagem, transformada-de-fourier, inteligencia-artificial, processamento-de-sinal]
data: 2026-08-25
---

# Reconstrução de Imagem em Tomografia

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Reconstrução de Imagem em Tomografia Computadorizada (TC)** refere-se ao processo matemático e computacional pelo qual imagens tomográficas transversais (cortes axiais) são geradas a partir de um conjunto de medições de atenuação de raios X obtidas em múltiplos ângulos de projeção ao redor do paciente. 

Do ponto de vista da física médica, o feixe de raios X policromático incide sobre o objeto de estudo, sofrendo atenuação exponencial descrita pela Lei de Beer-Lambert modificada para trajetórias contínuas. Seja $f(x,y)$ a distribuição espacial do coeficiente de atenuação linear ($\mu$) no plano de varredura. Um feixe de raios X que viaja ao longo de uma linha reta (linha de projeção) com distância perpendicular $s$ à origem e ângulo $\theta$ em relação ao eixo $x$ mede uma projeção integral, comumente denominada **Projeção Paralela** ou **Soma de Linha**:

$$
p(s, \theta) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) \, \delta(x \cos\theta + y \sin\theta - s) \, dx \, dy
$$

O conjunto bidimensional de todas as projeções $p(s, \theta)$ para $\theta \in [0, \pi)$ e $s \in (-\infty, \infty)$ constitui o **Sinograma**. O objetivo fundamental da reconstrução de imagem é inverter essa relação integral para recuperar a função original $f(x,y)$ a partir de $p(s, \theta)$.

Metrologicamente, a precisão da reconstrução de imagem impacta diretamente a exatidão quantitativa dos números de tomografia (Unidades Hounsfield - HU), a resolução espacial de alto contraste, a detectabilidade de baixo contraste e o nível de ruído estatístico governado pela Poissonagem dos fótons detectados.

---

## 2. Formulação Matemática e Propriedades

A base matemática para a inversão do problema de projeção reside em teoremas fundamentais do cálculo integral e da análise de Fourier.

### O Teorema da Fatia Central (Fourier Slice Theorem)
O Teorema da Fatia Central estabelece que a Transformada de Fourier unidimensional de uma projeção paralela $p(s, \theta)$, tomada em relação à coordenada espacial $s$, é igual a uma fatia bidimensional da Transformada de Fourier bidimensional da função original $f(x,y)$, avaliada ao longo de uma linha que passa pela origem com o mesmo ângulo $\theta$.

Matematicamente, seja $P(\omega, \theta)$ a Transformada de Fourier 1D de $p(s, \theta)$ em relação a $s$:

$$
P(\omega, \theta) = \int_{-\infty}^{\infty} p(s, \theta) e^{-j 2 \pi \omega s} \, ds
$$

E seja $F(u, v)$ a Transformada de Fourier 2D de $f(x,y)$. O Teorema da Fatia Central afirma que:

$$
P(\omega, \theta) = F(\omega \cos\theta, \omega \sin\theta)
$$

### Retroprojeção Filtrada (Filtered Backprojection - FBP)
Aplicando a inversão da Transformada de Fourier em coordenadas polares e introduzindo um filtro de rampa para compensar a densidade de amostragem no espaço de Fourier (que é maior perto da origem), chega-se à equação analítica da **Retroprojeção Filtrada (FBP)**:

$$
f(x,y) = \int_{0}^{\pi} \int_{-\infty}^{\infty} P(\omega, \theta) |\omega| e^{j 2 \pi \omega (x \cos\theta + y \sin\theta)} \, d\omega \, \, d\theta
$$

No domínio espacial, isso se traduz na operação de convolução da projeção com um núcleo (kernel) de filtro $h(s)$ seguida pela retroprojeção geométrica:

$$
f(x,y) = \int_{0}^{\pi} \left[ p(s, \theta) * h(s) \right]_{s = x \cos\theta + y \sin\theta} \, d\theta
$$

Onde o filtro rampa ideal no domínio espacial possui decaimento analítico que amplifica ruíveis de alta frequência, exigindo filtros apodizados (como *Ram-Lak*, *Hamming*, *Hann* ou *Butterworth*) para controlar a relação sinal-ruído (SNR).

### Reconstrução Iterativa (Iterative Reconstruction - IR) e Aprendizado Profundo (Deep Learning Reconstruction - DLR)
Quando o sistema possui dados incompletos, ruído quântico severo (baixa dose) ou artefatos metálicos, os métodos analíticos falham. Formula-se então o problema como um sistema linear discreto:

$$
\mathbf{p} = \mathbf{A} \mathbf{f} + \boldsymbol{\epsilon}
$$

Onde $\mathbf{p}$ é o vetor de projeções vetorizadas, $\mathbf{A}$ é a matriz do sistema (modelo geométrico e físico de aquisição), $\mathbf{f}$ é a imagem discretizada e $\boldsymbol{\epsilon}$ representa o ruído.

Métodos iterativos estatísticos (como *OSEM - Ordered Subset Expectation Maximization*) resolvem o problema minimizando uma função custo penalizada:

$$
\hat{\mathbf{f}} = \arg\min_{\mathbf{f} \ge 0} \left( \frac{1}{2} \|\mathbf{p} - \mathbf{A}\mathbf{f}\|_{\mathbf{\Sigma}^{-1}}^2 + \beta R(\mathbf{f}) \right)
$$

Onde o primeiro termo quantifica a verossimilhança estatística do ruído e o segundo termo $R(\mathbf{f})$ é uma penalização de regularização (como variação total - *Total Variation*). 

Nas abordagens modernas de **Reconstrução Baseada em Inteligência Artificial (DLR)**, redes neurais profundas (como redes convolucionais U-Net ou arquiteturas de difusão) atuam diretamente na correção do sinograma, na eliminação de ruído no domínio da imagem FBP, ou são embutidas iterativamente em laços de otimização (*Plug-and-Play Priors* e *Deep Equilibrium Models*).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A escolha e o ajuste do algoritmo de reconstrução de imagem são pilares cruciais na prática clínica e na otimização de protocolos radiológicos:

*   **Otimização de Dose e Redução de Ruído:** Algoritmos de Reconstrução Iterativa Avançada (ADMIRE, AIDR 3D, iDose) e DLR (AiCE, TrueFidelity, Pixels Shifting baseados em IA) permitem a manutenção da detectabilidade diagnóstica mesmo sob reduções significativas de corrente no tubo ($mAs$), atendendo ao princípio ALARA (*As Low As Reasonably Achievable*).
*   **Controle de Qualidade (CQ) e Metrologia:** A avaliação da qualidade da imagem reconstruída depende de métricas quantitativas obtidas por meio de **fantasmas (phantoms)**, avaliando a função de espalhamento de ponto (PSF), a função de transferência de modulação (MTF), o ruído textural e a linearidade de número de Hounsfield.
*   **Mitigação de Artefatos:** Técnicas de reconstrução iterativa e modelagem física avançada ajudam a suprimir artefatos de feixe endurecido (*beam hardening*), c, ruído quântico severo e artefatos de movimento.
*   **Avaliação por Observadores Computacionais:** Otimizadores de algoritmos de reconstrução frequentemente utilizam observadores ideais e humanos simulados para maximizar a acurácia diagnóstica em tarefas específicas (ex: detecção de nódulos pulmonares ou lesões hepáticas).

---

## 4. Conexões e Wikilinks

*   [[Tomografia Computadorizada|Tomografia Computadorizada]]
*   [[Física das Radiações|Física da Radiação]]
*   [[Processamento de Sinal e Imagem]]
*   [[Inteligência Artificial em Medicina]]
*   [[Controle de Qualidade em TC|Controle de Qualidade em Radiologia]]
*   [[Dosimetria em Radiodiagn Stico|Dosimetria em Radiodiagnóstico]]
*   [[Transformada de Fourier]]
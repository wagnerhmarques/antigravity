---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-de-imagem, processamento-de-sinal]
data: 2026-08-25
---

# filtered-backprojection

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A Retroprojeção Filtrada (*Filtered Backprojection* - FBP) é o algoritmo analítico padrão ouro clássico utilizado na reconstrução de imagens em Tomografia Computadorizada (TC) de 3ª e 4ª gerações. Historicamente derivada do teorema da fatia central (ou teorema de Fourier-Slice), a FBP resolve o problema inverso de reconstruir uma distribuição espacial bidimensional de coeficientes de atenuação linear, $\mu(x, y)$, a partir de um conjunto infinito ou discretizado de projeções unidimensionais obtidas em múltiplos ângulos (sinograma).

Fisicamente, a simples retroprojeção (*simple backprojection*) de perfis de atenuação atinge a reconstrução espacial borrada, devido à densidade espectral decrescente no domínio de Fourier do operador de projeção (o borrão $1/r$ no espaço real). Para corrigir este artefato físico inerente à geometria de aquisição fan-beam ou parallel-beam, a FBP aplica um filtro de rampa (*ramp filter*) ou variantes suavizadas (como Hann, Hamming ou Shepp-Logan) em cada projeção antes de realizar a operação geométrica de retroprojeção ao longo dos caminhos dos raios X. Do ponto de vista metrológico, a FBP é altamente determinística, linear e computacionalmente eficiente, servindo como base comparativa fundamental para a quantificação de ruído, resolução espacial e linearidade numérica em protocolos de controle de qualidade (QC) e testes de aceitação de scanners de TC.

---

## 2. Formulação Matemática e Propriedades (se aplicável)

Matematicamente, seja $p(\theta, t)$ o sinograma que representa a projeção paralela do objeto $\mu(x, y)$, onde $\theta$ é o ângulo de projeção e $t$ é a coordenada linear ao longo do detector:

$$
t = x \cos\theta + y \sin\theta
$$

A transformada de Fourier unidimensional de $p(\theta, t)$ em relação à variável espacial $t$ é dada por:

$$
P(\theta, \omega) = \int_{-\infty}^{\infty} p(\theta, t) e^{-j 2 \pi \omega t} dt
$$

O Teorema da Fatia Central estabelece que $P(\theta, \omega)$ é igual à transformada de Fourier bidimensional da imagem $\mu(x, y)$ avaliada em coordenadas polares na frequência espacial:

$$
\mathcal{F}_2\{\mu(x, y)\}(\omega \cos\theta, \omega \sin\theta) = P(\theta, \omega)
$$

Para recuperar a imagem espacial $\mu(x, y)$ através da transformada inversa de Fourier em coordenadas polares, surge um fator de Jacobiano igual a $|\omega|$ (em duas dimensões). Portanto, a reconstrução analítica exata requer a filtragem da projeção por uma função rampa no domínio das frequências espaciais:

$$
Q(\theta, t) = \int_{-\infty}^{\infty} P(\theta, \omega) |\omega| e^{j 2 \pi \omega t} d\omega
$$

A imagem final $\mu(x, y)$ é obtida pela retroprojeção dessas projeções filtradas $Q(\theta, t)$ sobre todos os ângulos de projeção $\theta \in [0, \pi]$:

$$
\mu(x, y) = \int_{0}^{\pi} Q(x \cos\theta + y \sin\theta, \theta) \, d\theta
$$

### Propriedades Analíticas:
* **Linearidade:** Sendo um operador linear, a propagação de ruído e artefatos na FBP pode ser modelada analiticamente por meio de funções de transferência de modulação (MTF) e distribuições de Wiener de ruído (NPS).
* **Amplificação de Ruído:** O filtro de rampa $|\omega|\text{}$ possui ganho ilimitado nas altas frequências, o que amplifica significativamente o ruído quântico de fótons (*quantum noise*). Por essa razão, filtros de apodização (como o filtro de Shepp-Logan, $H(\omega) = |\omega| \frac{\sin(\pi \omega / \omega_c)}{\pi \omega / \omega_c}$) são aplicados para atenuar as altas frequências em detrimento da resolução espacial.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Na prática clínica contemporânea, a FBP desempenha um papel duplo:
1. **Linha de Base Analítica:** Embora algoritmos de Reconstrução Iterativa (IR) e Reconstrução Baseada em Aprendizado Profundo (*Deep Learning Reconstruction* - DLR) tenham dominado a prática clínica devido à sua capacidade superior de redução de dose e controle de ruído, a FBP continua a ser a métrica de referência para validação regulatória e testes de constância em física médica.
2. **Tempo de Reconstrução:** A complexidade computacional da FBP é da ordem de $\mathcal{O}(N^3)$ ou $\mathcal{O}(N^2 \log N)$ quando implementada com transformadas rápidas de Fourier (FFT), permitindo reconstrução em tempo real essencial para fluxos de trabalho de emergência e exames de perfusão.

### Otimização e Dosimetria:
Como a FBP não modela a estatística de Poisson dos fótons de raios X nem a óptica do sistema (tamanho focal do tubo, resposta temporal do detector e espalhamento Compton), imagens reconstruídas exclusivamente por FBP em doses baixas de radiação sofrem de ruído severo e artefatos de granulação (*streak artifacts*). Consequentemente, a otimização dos protocolos de TC modernos frequentemente utiliza a FBP como semente inicial para algoritmos híbridos de reconstrução iterativa ou para treinar redes neurais profundas (DLR) que buscam mitigar as limitações analíticas da FBP mantendo sua fidelidade geométrica.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|computed-tomography]]
* [[sinogram]]
* [[central-slice-theorem]]
* [[Reconstrução Iterativa|iterative-reconstruction]]
* [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction]]
* [[Noise Power Spectrum|noise-power-spectrum]]
* [[Modulation Transfer Function (MTF)|modulation-transfer-function]]
* [[quality-control-ct]]
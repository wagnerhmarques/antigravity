---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-de-imagem, processamento-de-sinal, fbp]
data: 2026-08-25
---

# Filtro de Retroprojeção

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **Filtro de Retroprojeção** (frequentemente associado à *Filtered Backprojection* ou FBP) é o algoritmo analítico fundamental e histórico utilizado na Tomografia Computadorizada (TC) para reconstruir imagens tomográficas bidimensionais a partir de projeções unidimensionais (perfis de atenuação) obtidas em múltiplos ângulos ao redor do paciente. 

Do ponto de vista físico, a aquisição de dados na TC mede a atenuação de feixes de raios X transmitidos através do objeto, conforme descrito pela **Transformada de Radon**. A retroprojeção simples (*simple backprojection*), que consiste em borrar as projeções adquiridas de volta ao longo de suas trajetórias originais na matriz de imagem, resulta em uma representação física inerentemente borrada e geometricamente distorcida. O fenômeno de desfoque ocorre porque a densidade reconstruída em um ponto decresce proporcionalmente à distância radial a partir do centro (comportamento característico do filtro rampa no domínio espacial, correspondente à densidade espectral $1/\rho$ em coordenadas polares).

Para corrigir essa degradação matemática e restaurar a nitidez espacial, aplica-se um **filtro de rampa** (ou operador de rampa) nas projeções filtradas antes do processo de retroprojeção geométrica. Esse filtro opera como um filtro passa-alta que compensa exatamente o esmaecimento $1/|f$| (onde $f$ é a frequência espacial), garantindo que a imagem reconstruída corresponda fielmente à distribuição espacial real dos coeficientes de atenuação linear $\mu(x,y)$ do meio irradiado. Metrologicamente, o algoritmo FBP é valorizado por sua determinabilidade, linearidade e rapidez computacional, servindo como o padrão de referência para métricas de resolução espacial e ruído em protocolos de controle de qualidade.

---

## 2. Formulação Matemática e Propriedades

A formulação matemática do Filtro de Retroprojeção baseia-se no **Teorema da Slicing Central** (ou Teorema do Corte Central de Fourier), que estabelece que a Transformada de Fourier unidimensional de uma projeção paralela obtida a um ângulo $\theta$ é igual a uma fatia bidimensional da Transformada de Fourier bidimensional do objeto original ao longo de uma linha inclinada pelo mesmo ângulo $\theta$.

Seja $P_\theta(t)$ a projeção paralela obtida na posição linear $t$ e ângulo $\theta$, definida pela Transformada de Radon:

$$
P_\theta(t) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) \delta(x \cos\theta + y \sin\theta - t) \, dx \, dy
$$

Onde $f(x,y)$ é a função de atenuação espacial a ser reconstruída. A reconstrução por retroprojeção filtrada no espaço de Fourier é expressa formalmente como:

$$
f(x,y) = \int_{0}^{\pi} Q_\theta(x \cos\theta + y \sin\theta) \, \, d\theta
$$

Onde $Q_\theta(t)$ representa a projeção filtrada, obtida pela convolução da projeção original $P_\theta(t)$ com um núcleo de filtro $h(t)$:

$$
Q_\theta(t) = P_\theta(t) * h(t) = \int_{-\infty}^{\infty} P_\theta(t') h(t - t') \, dt'
$$

No domínio da frequência, a operação de filtragem corresponde a uma multiplicação simples. Sendo $\mathcal{F}\{P_\theta(t)\} = S_\theta(\omega)$, onde $\omega$ é a frequência espacial, o filtro ideal (filtro rampa) é definido como:

$$
H(\omega) = |\omega|
$$

Portanto, a projeção filtrada no domínio de Fourier é dada por:

$$
S_\theta^{\text{filt}}(\omega) = S_\theta(\omega) \cdot |\omega|
$$

### Modificações e Filtros Apodizados
Como o filtro de rampa puro $H(\omega) = |\omega|$ possui ganho infinito nas altas frequências, ele amplifica severamente o ruído quântico inerente aos dados de contagem de fótons em TC. Para mitigar esse efeito indesejado, o filtro rampa é multiplicado por janelas de apodização (ou funções de corte/suavização) $W(\omega)$, tais como os filtros **Hamming**, **Hann**, **Butterworth** ou **Shepp-Logan**:

$$
H_{\text{mod}}(\omega) = |\omega| \cdot W(\omega)
$$

Por exemplo, o filtro de Hann é definido analiticamente no domínio das frequências até uma frequência de corte $\omega_c$ como:

$$
W_{\text{Hann}}(\omega) = \begin{cases} 
0.5 \left(1 + \cos\left(\frac{\pi \omega}{\omega_c}\right)\right) & \text{se } |\omega| \le \omega_c \\
0 & \text{se } |\omega| > \omega_c
\end{cases}
$$

---

## 3. Aplicações e Relembrança em Tomografia Computadorizada e Otimização

O Filtro de Retroprojeção permanece como a espinha dorsal computacional em scanners de TC clínicos devido à sua estabilidade analítica, ausência de artefatos de convergência iterativa e baixíssimo tempo de processamento em comparação com métodos avançados. Suas principais aplicações e frentes de otimização incluem:

* **Controle de Qualidade e Metrologia:** Protocolos de aceitação e testes periódicos de desempenho de imagem (avaliação de função de dispersão pontual - *PSF*, função de transferência de modulação - *MTF*, e ruído) utilizam prioritariamente imagens reconstruídas por FBP pura ou com filtros padronizados para evitar vieses introduzidos por algoritmos não-lineares.
* **Seleção de Kernels Clínicos:** Os fabricantes implementam diferentes variantes de filtros de retroprojeção ajustados para aplicações clínicas específicas (ex: kernels *sharp* para alta resolução espacial em estruturas ósseas e pulmões, e kernels *smooth* para redução de ruído em tecidos moles e parênquima cerebral).
* **Base para Abordagens Híbridas e Inteligência Artificial:** Embora a Reconstrução Iterativa (IR) e a Reconstrução Baseada em Aprendizado Profundo (DLR) tenham ganhado espaço para mitigar o ruído em baixas doses de radiação, muitos modelos de redes neurais profundas (CNNs e redes generativas adversariais - *GANs*) utilizam imagens brutas em FBP como entrada (*input*) para realizar o mapeamento de remoção de ruído (*denoising*) ou correção de artefatos de feixe endurecido.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[Transformada de Radon]]
* [[Reconstrução Iterativa|Reconstrução Iterativa]]
* [[Inteligência Artificial em Tomografia]]
* [[Função de Transferência de Modulação]]
* [[Controle de Qualidade em TC|Controle de Qualidade em Radiodiagnóstico]]
* [[Dosimetria em Radiologia|Dosimetria em Raio-X]]
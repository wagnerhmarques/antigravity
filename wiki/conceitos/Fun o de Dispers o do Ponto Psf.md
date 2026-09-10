---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, qualidade-de-imagem, processamento-de-sinal, inteligencia-artificial]
data: 2026-08-25
---

# Função de Dispersão do Ponto (PSF)

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Função de Dispersão do Ponto** (do inglês *Point Spread Function* - PSF) é a descrição fundamental da resposta de um sistema de imagem linear e invariante no espaço (LSI - *Linear Space-Invariant*) a uma fonte pontual ideal (uma função delta de Dirac). Em Física Médica e, particularmente, em Tomografia Computadorizada (TC), a PSF quantifica o grau de borramento (*blurring*), degradação e espalhamento espacial introduzido pelo sistema de aquisição e reconstrução de imagem ao mapear um objeto idealmente puntiforme no espaço real para uma distribuição de intensidade ou número de Tomografia (unidades Hounsfield - HU) no domínio da imagem digital.

Do ponto de vista metrológico, a PSF serve como a métrica definitiva para avaliar a **resolução espacial** de um tomógrafo. Em um sistema perfeitamente ideal (que não existe na prática), a imagem de um ponto infinitamente pequeno seria outro ponto infinitamente pequeno. No entanto, devido a limitações físicas inerentes ao equipamento — tais como o tamanho finito do ponto focal do tubo de raios X, o *crosstalk* óptico nos cristais do detector, a amostragem discreta (geometria de feixe cônico ou leque), os algoritmos de interpolação e os filtros de rampa aplicados na retroprojeção filtrada (FBP) —, a energia de um único ponto é "espalhada" por uma região tridimensional adjacente.

A PSF é intrinsecamente dependente de três dimensões espaciais ($x, y, z$), mas frequentemente é decomposta em suas componentes no plano de corte (*in-plane PSF*) e no eixo longitudinal ($z$-axis PSF ou *slice sensitivity profile*). A caracterização precisa da PSF permite aos físicos médicos preverem como estruturas finas, bordas e interfaces de diferentes densidades (como o parênquima pulmonar e os vasos sanguíneos, ou microcalcificações em exames avançados) serão reproduzidas, sendo a base conceitual para o cálculo da Função de Transferência de Modulação (MTF).

---

## 2. Formulação Matemática e Propriedades

Matematicamente, seja $f(x, y)$ a distribuição de atenuação de um objeto bidimensional contendo uma fonte pontual ideal na origem, representada pela função delta de Dirac bidimensional $\delta(x, y)$. O sistema de imagem de TC atua como um operador linear $H\{\cdot\}$ que transforma o objeto na imagem resultante $g(x, y)$:

$$
g(x, y) = H\{f(x, y)\} = H\{\delta(x, y)\} = \text{PSF}(x, y)
$$

Assumindo que o sistema seja aproximadamente linear e invariante no espaço dentro de uma região de interesse local, a imagem $g(x, y)$ de um objeto arbitrário $f(x, y)$ pode ser formulada como a operação de convolução (indicada por $*$) entre o objeto e a PSF:

$$
g(x, y) = \iint_{-\infty}^{\infty} f(\xi, \eta) \cdot \text{PSF}(x - \xi, y - \eta) \, d\xi \, d\eta = (f * \text{PSF})(x, y)
$$

### O Domínio da Frequência e a MTF
Pelo Teorema da Convolução, a operação no espaço real corresponde a uma multiplicação no domínio das frequências espaciais. Aplicando a Transformada de Fourier bidimensional ($\mathcal{F}$):

$$
G(u, v) = F(u, v) \cdot \text{OTF}(u, v)
$$

Onde:
- $G(u, v)$ e $F(u, v)$ são as transformadas de Fourier de $g(x, y)$ e $f(x, y)$, respectivamente.
- $\text{OTF}(u, v)$ é a **Função de Transferência Óptica** (*Optical Transfer Function*), uma função complexa definida como a transformada de Fourier da PSF normalizada:

$$
\text{OTF}(u, v) = \frac{\mathcal{F}\{\text{PSF}(x, y)\}}{\iint_{-\infty}^{\infty} \text{PSF}(x, y) \, dx \, dy}
$$

A **Função de Transferência de Modulação (MTF)** é definida como o módulo da OTF:

$$
\text{MTF}(u, v) = \left| \text{OTF}(u, v) \right|
$$

A MTF mede a capacidade do sistema de preservar o contraste de detalhes em diferentes frequências espaciais (ciclos por centímetro, $\text{cm}^{-1}$).

### Modelagem Analítica
Muitas vezes, para fins de simulação e ajuste de curvas (*curve fitting*), a PSF bidimensional em TC é aproximada por uma função gaussiana simétrica ou assimétrica. Em coordenadas polares ou cartesianas, uma Gaussiana 2D isotrópica é expressa como:

$$
\text{PSF}(x, y) = \frac{1}{2\pi \sigma^2} \exp\left( -\frac{x^2 + y^2}{2\sigma^2} \right)
$$

Onde $\sigma$ (desvio padrão) está diretamente relacionado à largura a meia altura ($\text{FWHM}$ - *Full Width at Half Maximum*), uma métrica clínica padrão de resolução espacial, calculada analiticamente por:

$$
\text{FWHM} = 2\sqrt{2\ln 2} \sigma \approx 2.3548 \sigma
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Em Tomografia Computadorizada moderna, o controle, a modelagem e a manipulação da PSF são críticos para o equilíbrio entre a **resolução espacial** e o **ruído quântico**, regido fundamentalmente pelo compromisso dose-ruído-resolução.

### 1. Controle de Qualidade (QC) e Metrologia
Físicos médicos utilizam phantoms especializados contendo fios de tungstênio, esferas de alta densidade ou placas de níquel-cromo para medir empiricamente a PSF ou sua derivada (por meio da Função de Dispersão de Borda - LSF). A partir da LSF, obtém-se a MTF para determinar a frequência de corte na qual a MTF cai para 10% ($\text{MTF}_{10}$), indicando o limite prático de resolução espacial do tomógrafo para diferentes protocolos (filtros de retroprojeção como *sharp* ou *smooth*).

### 2. Algoritmos de Reconstrução Iterativa (IR) e Aprendizado Profundo (DLR)
Nos algoritmos de Retroprojeção Filtrada (FBP) tradicionais, a PSF é essencialmente determinada pelo filtro rampa combinado com o filtro de apodização (kernel). No entanto, com o advento da **Reconstrução Iterativa Baseada em Modelos (MBIR)** e dos modelos de **Inteligência Artificial** voltados à restauração de imagem (DLR - *Deep Learning Reconstruction*):
- **Modelagem do Sistema ($\mathcal{A}$):** A matriz do sistema de projeção e retroprojeção incorpora uma modelagem avançada da PSF física do scanner (incluindo o tamanho do ponto focal e a resposta do detector em 3D). Isso permite recuperar a resolução espacial perdida sem amplificar catastroficamente o ruído da imagem.
- **Redes Neurais de Correção de PSF:** Redes convolucionais (CNNs) e modelos gerativos adversariais (GANs) são treinados para deconvulsionar a imagem degradada, estimando e revertendo espacialmente a PSF variante do sistema, gerando imagens com nitidez aprimorada em doses reduzidas de radiação.

### 3. Dosimetria e Observadores Computacionais
Na avaliação de qualidade de imagem baseada em tarefas (*task-based image quality*), a PSF interage diretamente com o ruído (caracterizado pelo Espectro de Potência de Ruído - NPS). A métrica combinada, como a **Detectabilidade Ideal Pre-Whitening** ($d'$), utiliza a MTF (derivada da PSF) para modelar como observadores humanos ou ideais (matemáticos) detectam lesões de Baixo Contraste (CDL) em exames oncológicos ou cardiovasculares.

---

## 4. Conexões e Wikilinks

- [[Task Transfer Function|Função de Transferência de Modulação (MTF)]]
- [[FBP|Retroprojeção Filtrada (FBP)]]
- [[Reconstrução Iterativa em TC (IR)]]
- [[Inteligência Artificial em Tomografia Computadorizada (DLR)]]
- [[Noise Power Spectrum|Espectro de Potência de Ruído (NPS)]]
- [[Controle de Qualidade em Tomografia Computadorizada]]
- [[Unidades Hounsfield e Calibração de Densidade]]
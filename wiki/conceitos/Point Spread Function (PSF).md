---
title: "Point Spread Function (PSF) e Resolução Espacial"
slug: "point-spread-function"
tipo: "conceito"
aliases:
  - "Função de Espalhamento de Ponto"
  - "PSF"
  - "Resolução Espacial em Imagem Médica"
  - "Matriz de Espalhamento de Ponto"
tags:
  - "fisica-medica"
  - "tomografia-computadorizada"
  - "metrologia"
  - "processamento-de-imagem"
  - "aapm-tg233"
  - "dlr"
---

# Point Spread Function (PSF) e Resolução Espacial

## 1. Definição Conceitual, Fundamentação Física e Metrológica

Em imageamento médico e física dos sistemas de imagem, a **Point Spread Function (PSF)** — ou *Função de Espalhamento de Ponto* — representa a resposta impulsiva espacial de um sistema de aquisição e reconstrução de imagem linear e shift-invariante (LSI). Metrologicamente, a PSF descreve o grau de desfoque (*blurring*) e degradação espacial que um ponto infinitesimal de sinal (idealmente uma função delta de Dirac $\delta(x, y, z)$) sofre ao transitar do objeto anatômico para a matriz digital reconstruída.

Do ponto de vista da física dos meios contínuos e da mecânica quântica/ondulatória aplicada aos raios X (em [[Tomografia Computadorizada (TC)|Tomografia Computadorizada]]), a PSF emerge de múltiplos fenômenos físicos fundamentais:
1. **Tamanho finito do foco focal do tubo de raios X**: A geometria do ponto focal introduz uma projeção penumbral geométrica.
2. **Abertura e discretização do detector**: Os elementos de scintilação e os fotodiodos possuem dimensões finitas, integrando espacialmente a radiação incidente sobre uma área finita $\Delta_x \times \Delta_y$.
3. **Filtros de reconstrução (Kernels)**: A retroprojeção filtrada (FBP) utiliza filtros de rampa e janelas de apodização que moldam diretamente a resposta espacial do sistema.
4. **Efeitos de difusão e dispersão (*scatter*)**: O espalhamento Compton nos tecidos e no meio de detecção reduz o contraste de alta frequência.

A metrologia da PSF estabelece a base para a quantificação rigorosa da **Resolução Espacial**\, definindo a capacidade do sistema em discernir estruturas anatômicas de pequeno calibre adjacentes.

---

## 2. Formulações Matemáticas Rigorosas

Considerando um sistema de imagem linear, a formação da imagem de um objeto $f(x, y)$ corrompida pela PSF do sistema $h(x, y; x', y')$ é expressa pelo operador integral de Fredholm de primeira espécie:

$$
g(x, y) = \iint_{-\infty}^{\infty} f(x', y') h(x, y; x', y') \, dx' \, dy'
$$

Sob a hipótese de Invariância Espacial (*Shift-Invariance*), a PSF depende apenas das diferenças espaciais, reduzindo a equação a uma convolução bidimensional pura:

$$
g(x, y) = (f * h)(x, y) = \iint_{-\infty}^{\infty} f(x', y') h(x - x', y - y') \, dx' \, dy'
$$

Aplicando a Transformada de Fourier bidimensional $\mathcal{F}\{\cdot\}$, o teorema da convolução mapeia a degradação espacial para o domínio das frequências espaciais $u$ e $v$:

$$
G(u, v) = F(u, v) \cdot H(u, v)
$$

Onde $H(u, v) = \mathcal{F}\{h(x, y)\}$ é definido como a **Optical Transfer Function (OTF)**. O módulo da OTF constitui a **Modulation Transfer Function (MTF)**, métrica fundamental para avaliar a fidelidade de contraste em função da frequência espacial:

$$
\text{MTF}(u, v) = \left| H(u, v) \right| = \left| \frac{\mathcal{F}\{g(x, y)\}}{\mathcal{F}\{f(x, y)\}} \right|
$$

Para caracterização analítica simplificada, a PSF é frequentemente modelada como uma distribuição Gaussiana bidimensional de desvio padrão $\sigma$:

$$
h(x, y) = \frac{1}{2\pi \sigma^2} \exp\left( -\frac{x^2 + y^2}{2\sigma^2} \right)
$$

Cuja transformada de Fourier analítica resulta em uma MTF também gaussiana no domínio espacial recíproco:

$$
\text{MTF}(u, v) = \exp\left( -2\pi^2 \sigma^2 (u^2 + v^2) \right)
$$

A largura a meia altura (**FWHM** - *Full Width at Half Maximum*) da PSF relaciona-se diretamente com o desvio padrão por:

$$
\text{FWHM} = 2\sqrt{2\ln 2} \, \sigma \approx 2.355 \, \sigma
$$

---

## 3. Contexto no Acervo do Pesquisador & Aplicações em Tomografia Computadorizada

No escopo da física médica moderna e dos protocolos avançados de [[Controle de Qualidade em TC|Controle de Qualidade em TC]], a avaliação da PSF evoluiu de phantom físicos estáticos para análises baseadas em simulações de Monte Carlo e inteligência artificial.

### Deep Learning Reconstruction (DLR) e a PSF
Os algoritmos de reconstrução baseados em aprendizado profundo ([[Deep Learning Reconstruction (DLR)|DLR]]) alteram drasticamente a natureza da PSF em tomografia. Enquanto a retroprojeção filtrada tradicional (FBP) e a reconstrução iterativa estatística (IR) exibiam PSFs predominantemente estacionárias e simétricas, as redes neurais DLR frequentemente geram uma PSF *não-linear* e *dependente do nível de sinal* (dose). Em regiões de baixo contraste ou alta granulosidade de ruído, a DLR pode suprimir a largura da PSF para preservar a nitidez aparente, exigindo novos paradigmas metrológicos recomendados pela [[AAPM TG-233 - Avaliação de Desempenho em TC|AAPM Task Group 233]].

### Detectabilidade e Índice $d'$ (Task-Based Image Quality)
A metrologia contemporânea afasta-se de métricas isoladas como a FWHM da PSF em favor da **Detectabilidad Baseada em Tarefa ($d'$)**, formalizada pelo *Rose Model* estendido e pela teoria de detecção de sinais de Hotelling. A detectabilidade $d'$ integra a PSF (através da MTF) com o Espectro de Potência de Ruído ([[Noise Power Spectrum|NPS]]):

$$
(d')^ = \iint_{-\infty}^{\infty} \frac{\left| W(u, v) \cdot \text{MTF}(u, v) \right|^2}{\text{NPS}(u, v)} \, du \, dv
$$

Onde $W(u, v)$ representa a função de tarefa (perfil do objeto de teste ou lesão simulada). Essa formulação demonstra que uma PSF excessivamente estreita (obtida por filtros agressivos) pode inflar o ruído na NPS\, degradando o desempenho clínico geral ($d'$) do observador ideal ou humano.

### Otimização de Dose e Resolução Espacial
O balanço entre [[Otimização de Dose em TC|Dose e Qualidade de Imagem]] é diretamente mediado pela PSF. Aumentar a corrente do tubo ($mAs$) reduz o ruído quântico, permitindo o uso de kernels de reconstrução de alta resolução (que mantêm a PSF estreita e a FWHM baixa) sem perda catastrófica de detectabilidade. Por outro lado, protocolos de baixa dose dependem de filtros de suavização que alargam a PSF\, degradando a resolução espacial em prol da redução de artefatos de quantum mottle.

---

## 4. Conexões Bidirecionais

- **Fundamentos**: [[Tomografia Computadorizada (TC)|tomografia-computadorizada-avancada]]
- **Metrologia e Normas**: [[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg233]]
- **Processamento e Ruído**: [[Noise Power Spectrum|noise-power-spectrum]], [[Deep Learning Reconstruction (DLR)|reconstrucao-deep-learning]]
- **Garantia de Qualidade**: [[Controle de Qualidade em TC|controle-de-qualidade-tc]], [[Otimização de Dose em TC|otimizacao-dose-tc]]

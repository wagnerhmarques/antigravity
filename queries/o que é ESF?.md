> 📅 **Data:** 2026-09-27 | 🔗 **Conexões:** [[Função de Espalhamento de Borda (ESF)]], [[Função de Espalhamento de Ponto (PSF)]], [[Modulation Transfer Function (MTF)]], [[Resolução Espacial]]

> 📅 **Data:** 2026-03-30 | 🔗 **Conexões:** [[Resolução Espacial]], [[Modulation Transfer Function (MTF)]]

## 1. Definição Conceitual e Fundamentação Física

A **Função de Espalhamento de Borda** (ESF - *Edge Spread Function*) é uma métrica fundamental na metrologia de sistemas de imagem em Tomografia Computadorizada (TC) que descreve a resposta do sistema de aquisição e reconstrução diante de uma transição abrupta e ideal de atenuação, equivalente a uma borda degrau (*step edge*). Do ponto de vista da física dos sistemas de imagem, a ESF representa a integral unidimensional da Função de Espalhamento de Linha (LSF) ou a projeção bidimensional da Função de Espalhamento de Ponto (PSF) ao longo de uma linha de corte perpendicular à interface de transição de contraste.

Na prática experimental, objetos físicos contendo interfaces nítidas entre materiais de diferentes números atômicos ou densidades (como um cilindro de teflon inserido em água ou uma lâmina metálica no interior de um fantom) são escaneados para gerar perfis de transição. A imperfeição do sistema físico — decorrente do tamanho finito do foco do tubo de raios X, da abertura finita dos elementos do detector e dos filtros de reconstrução empregados — faz com que a borda ideal em degrau seja suavizada, gerando uma curva sigmoide contínua conhecida como ESF.

A ESF serve como uma ponte analítica crucial no processamento de imagem, permitindo derivar tanto a LSF quanto a **[[Modulation Transfer Function (MTF)|Modulation Transfer Function (MTF)]]**, que quantifica a fidelidade de transferência de contraste em diferentes frequências espaciais.

## 2. Formulação Matemática e Propriedades

Matematicamente, seja $I(x)$ a imagem unidimensional obtida perpendicularmente a uma borda ideal posicionada na origem $x = 0$, onde a transmitância ou o coeficiente de atenuação linear passa abruptamente de um valor baixo para um valor alto, representado por uma função degrau de Heaviside $u(x)$. A imagem observada com ruído desprezível é modelada pela convolução da derivada da borda com a Função de Espalhamento de Linha $\text{LSF}(x)$:

$$
\text{ESF}(x) = \int_{-\infty}^{x} \text{LSF}(x') \\, dx'
$$

A relação fundamental entre a ESF, a LSF e a PSF estabelece que a LSF é obtida diretamente por meio da diferenciação da ESF em relação à coordenada espacial $x$:

$$
\text{LSF}(x) = \frac{d}{dx} \left[ \text{ESF}(x) \right]
$$

Com a LSF calculada, a Função de Transferência de Modulação ($\text{MTF}$) é obtida aplicando a transformada de Fourier normalizada:

$$
\text{MTF}(u) = \left| \int_{-\infty}^{\infty} \text{LSF}(x) e^{-j 2\pi u x} \\, dx \right| \left/ \int_{-\infty}^{\infty} \text{LSF}(x) \\, dx \right.
$$

Onde:
- $u$ é a frequência espacial expressa em pares de linhas por centímetro ($\text{lp/cm}$) ou ciclos por centímetro.
- $j$ é a unidade imaginária.

### Propriedades e Vantagens Metrológicas:
- **Estabilidade Experimental:** Medir diretamente a PSF pontual exige fios de tungstênio extremamente finos e alinhamentos milimétricos complexos que sofrem com artefatos de ruído quântico localizado. A ESF utiliza bordas extensas, o que melhora a relação sinal-ruído (SNR) estatística das medições.
- **Derivada Numérica:** A principal fragilidade matemática da ESF reside no fato de que a diferenciação numérica $\frac{d}{dx}$ amplifica severamente o ruído de alta frequência presente na imagem reconstruída, exigindo o uso de técnicas de suavização prévia (como ajustes por funções sigmoides paramétricas ou splines cúbicas) antes de calcular a LSF e a MTF.

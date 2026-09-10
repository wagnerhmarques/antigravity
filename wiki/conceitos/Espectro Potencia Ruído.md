---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, ruido, qualidade-imagem, processamento-sinal, metrologia]
data: 2026-08-25
---

# Espectro_Potencia_Ruido

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **Espectro de Potência do Ruído** (conhecido na literatura em inglês como *Noise Power Spectrum* - NPS, ou *Wiener Spectrum*) é uma ferramenta metrológica fundamental na Física Médica e na engenharia de imagem aplicada à Tomografia Computadorizada (TC). O NPS quantifica a textura, a magnitude e a distribuição espacial das flutuações de ruído estocástico em uma imagem reconstruída, decompondo a variância do ruído em suas componentes de frequência espacial pura.

Diferente do desvio padrão global do ruído ($\sigma$), que fornece apenas uma medida escalar (integrada) da flutuação de pixel em uma região de interesse (ROI) homogênea, o NPS descreve *como* esse ruído está distribuído ao longo de diferentes escalas espaciais (frequências espaciais, medidas em $\text{mm}^{-1}$ ou $\text{cycles/cm}$). 

Em TC, o ruído não é puramente branco (ou seja, sua densidade espectral não é uniforme em todas as frequências). Os filtros de retroprojeção filtrada (FBP), os algoritmos de reconstrução iterativa (IR) e as técnicas de reconstrução baseadas em aprendizado profundo (*Deep Learning Reconstruction* - DLR) moldam profundamente a textura do ruído. Por exemplo, filtros de rampa acentuam as altas frequências espaciais para preservar a resolução espacial, resultando em um ruído de alta frequência ("granulado" ou *sandy*). Em contrapartida, algoritmos iterativos e DLR frequentemente suprimem o ruído em altas frequências de forma não linear, alterando drasticamente o NPS, o que pode inducer a uma textura de ruído de baixa frequência ("manchada" ou *blotchy*), perceptível e por vezes indesejada por radiologistas se não calibrada corretamente.

Metrologicamente, o NPS é o equivalente bidimensional (ou tridimensional) da Densidade Espectral de Potência (PSD) de sinais estacionários, adaptado para imagens médicas discretas e normalizadas.

---

## 2. Formulação Matemática e Propriedades

Para estimar o NPS bidimensional de uma imagem de TC de um objeto homogêneo (como um fantoma de água), o procedimento padrão envolve a extração de uma ou mais regiões de interesse (ROI) centrais, planas e estacionárias, de tamanho $N \times N$ pixels.

Seja $I(x, y)$ a matriz de intensidade de pixel na ROI e $\bar{I}(x, y)$ a tendência determinística estimada (geralmente a média da ROI ou um ajuste polinomial de baixa ordem para remover artefatos de *beam hardening* ou não-uniformidade do feixe). A imagem de ruído residual $\Delta I(x, y)$ é dada por:

$$
\Delta I(x, y) = I(x, y) - \bar{I}(x, y)
$$

O NPS bidimensional, denotado por $W(f_x, f_y)$, é calculado através da magnitude quadrada da Transformada de Fourier Discreta (DFT) bidimensional da imagem de ruído residual, normalizada pelo tamanho da matriz e pelo espaçamento dos pixels:

$$
W(f_x, f_y) = \frac{\Delta_x \Delta_y}{N_x N_y} \left\langle \left| \sum_{x=0}^{N_x-1} \sum_{y=0}^{N_y-1} \Delta I(x, y) e^{-2\pi i (f_x x \Delta_x + f_y y \Delta_y)} \right|^2 \right\rangle
$$

Onde:
*   $\Delta_x$ e $\Delta_y$ são os tamanhos dos pixels nas direções $x$ e $y$ (em $\text{mm}$).
*   $N_x$ e $N_y$ são as dimensões da ROI em número de pixels.
*   $f_x$ e $f_y$ são as frequências espaciais correspondentes (em $\text{mm}^{-1}$).
*   $\langle \dots \rangle$ representa o operador de valor esperado (enamble average), tipicamente calculado fazendo a média sobre múltiplos cortes axiais e/ou múltiplas realizações independentes do mesmo fantoma para reduzir a variância estatística da própria estimativa do NPS.

### Relação com a Variância Total
Pelo Teorema de Parseval, a integral (ou soma) do NPS sobre todo o domínio de frequência espacial é igual à variância total ($\sigma^2$) do ruído na imagem:

$$
\sigma^2 = \iint_{-\infty}^{\infty} W(f_x, f_y) \, df_x \, df_y \approx \sum_{f_x} \sum_{f_y} W(f_x, f_y) \, \Delta f_x \, \Delta f_y
$$

### NPS Radialmente Simétrico ($1D$)
Em sistemas de TC de gantry axial com simetria rotacional, o NPS bidimensional é frequentemente convertido em um perfil unidimensional radial $W(f)$, integrando-se $W(f_x, f_y)$ em coordenadas polares ($f = \sqrt{f_x^2 + f_y^2}$):

$$
W(f) = \int_{0}^{2\pi} W(f \cos\theta, f \sin\theta) \, \, d\theta
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

O Espectro de Potência do Ruído desempenha um papel crítico na garantia de qualidade avançada, na otimização de protocolos de dose de radiação e no desenvolvimento de algoritmos de reconstrução:

1.  **Controle de Qualidade e Padronização de Fabricantes:** Diferentes marcas de scanners de TC utilizam filtros de retroprojeção e algoritmos proprietários distintos. O NPS serve como a "assinatura espectral" do tomógrafo, permitindo que físicos médicos comparem se um novo protocolo de varredura mantém características de ruído equivalentes a protocolos legados.
2.  **Avaliação de Algoritmos Avançados (IR e DLR):** Métodos de Reconstrução Iterativa e Inteligência Artificial (DLR) são altamente não-lineares. O ruído gerado por essas técnicas varia frequentemente com o sinal local (dose-dependente e contraste-dependente). O estudo do NPS local (*Task-specific NPS*) é essencial para evitar texturas de ruído artificiais que possam mimetizar lesões sutis ou mascarar microcalcificações.
3.  **Teoria de Detecção e Observadores Computacionais:** O desempenho de tarefas visuais (tanto por radiologistas quanto por [[Modelo_Matematico_Observador]]) é modelado pela relação entre a função de transferência de modulação ([[Funcao_Transferencia_Modulacao_FTM]]) e o NPS. A [[Detectabilidade_Ideal]] e o observador de Hotelling utilizam o NPS como a matriz de covariância do ruído no domínio da frequência para calcular índices de desempenho como a *Detectability Index* ($d'$).
4.  **Otimização de Dose:** Ao alterar parâmetros como corrente do tubo ($mAs$), tensão ($kVp$) ou filtros de bowtie, o NPS escala em amplitude, mas idealmente deve preservar sua forma normalizada (frequência dominante) para não degradar a diagnosticabilidade clínica.

---

## 4. Conexões e Wikilinks

*   [[Tomografia Computadorizada|Tomografia_Computadorizada]]
*   [[Funcao_Transferencia_Modulacao_FTM]]
*   [[Reconstrucao_Iterativa_TC]]
*   [[Deep Learning Reconstruction (DLR)|Deep_Learning_Reconstruction_DLR]]
*   [[Modelo_Matematico_Observador]]
*   [[Detectabilidade_Ideal]]
*   [[Controle de Qualidade em TC|Controle_Qualidade_TC]]
*   [[Dosimetria_e_Dose_Em_TC]]
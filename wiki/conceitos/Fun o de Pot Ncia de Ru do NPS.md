---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, ruido, qualidade-de-imagem, metrologia, processamento-de-sinal]
data: 2026-08-25
---

# Função de Potência de Ruído - NPS

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Função de Potência de Ruído** (*Noise Power Spectrum* - NPS), frequentemente referida na literatura clássica de processamento de imagem como o espectro de Wiener do ruído, é uma métrica metrológica fundamental na Física Médica para a caracterização quantitativa e espacial do ruído estocástico em imagens digitais, com ênfase particular na Tomografia Computadorizada (TC). 

Enquanto o desvio padrão global ($\sigma$) do ruído fornece apenas uma estimativa escalar da magnitude flutuante dos pixels em uma região de interesse homogênea (ROI), ele falha em descrever a **textura** ou a **distribuição espacial** desse ruído. Diferentes algoritmos de reconstrução — como a Retroprojeção Filtrada (FBP) tradicional, Reconstruções Iterativas (IR) e técnicas baseadas em Aprend profundo (*Deep Learning Reconstruction* - DLR) — podem apresentar o mesmo desvio padrão nominal de ruído, mas resultam em aparências visuais drasticamente distintas (ruído grosseiro *vs.* ruído manchado ou de granulação fina). A NPS resolve essa limitação ao decomponer o ruído em suas componentes de frequência espacial bidimensionais (ou tridimensionais), mapeando como a variância do ruído se distribui ao longo de diferentes frequências espaciais (ciclos por centímetro ou milímetro).

Do ponto de vista metrológico, a NPS atua como a assinatura espectral do processo de formação de imagem ruidosa. Ela reflete a interação complexa entre os fótons de raios X incidentes (estatística de Poisson e ruído quântico), o design do feixe (filtração bow-tie), a geometria do sistema de detecção (eficiência quântica de detecção - DQE, diafonia/crosstalk), o processo de amostragem e a função de filtro rampa combinada com os filtros de suavização ou realce aplicados no kernel de reconstrução.

---

## 2. Formulação Matemática e Propriedades (se aplicável)

Rigorosamente, seja $I(x, y)$ a matriz de imagem ruidosa obtida em um fantoma homogêneo e $n(x, y) = I(x, y) - \bar{I}(x, y)$ a flutuação de ruído espacial, onde $\bar{I}(x, y)$ representa a imagem média ou a tendência determinística de fundo (frequentemente aproximada por uma média constante ou um ajuste polinomial para remover artefatos de calibração ou não-uniformidades inerentes ao feixe).

A estimativa bidimensional da NPS é calculada por meio da Transformada de Fourier Discretizada (DFT) das flutuação de ruído em ROIs quadradas de tamanho $N \times N$ pixels, com dimensões físicas de pixel dadas por $\Delta_x$ e $\[ \Delta_y ]$. A expressão formal para a NPS 2D é definida como:

$$
\text{NPS}(f_x, f_y) = \frac{\Delta_x \Delta_y}{N_x N_y} \sum_{m=1}^{M} \left| \sum_{x=1}^{N_x} \sum_{y=1}^{N_y} n_m(x, y) e^{-2\pi i (f_x x \Delta_x + f_y y \Delta_y)} \right|^2
$$

Onde:
- $f_x$ e $f_y$ são as frequências espaciais nas direções $x$ e $y$, respectivamente.
- $n_m(x, y)$ representa a matriz de ruído da $m$-ésima realização independente (ou de múltiplas ROIs extraídas de fatias e exames homólogos).
- $M$ é o número total de amostras de ROI utilizadas para reduzir a variância estatística do estimador da NPS.
- Os fatores de espaçamento $\Delta_x \Delta_y$ asseguram a correta escalabilidade dimensional (unidades típicas de $\text{HU}^2 \cdot \text{mm}^2$ ou normalizadas).

### Propriedades Notáveis:
1. **Relação com a Variância (Teorema de Parseval):** A integração da NPS em todo o domínio de frequência espacial recupera exatamente a variância global ($\sigma^2$) do ruído na imagem:
   
$$
\sigma^2 = \iint_{-\infty}^{\infty} \text{NPS}(f_x, f_y) \, df_x \, df_y \approx \sum_{i} \sum_{j} \text{NPS}(f_{\xi}, f_{yj}) \Delta f_x \Delta f_y
$$

2. **Redução Dimensional (NPS Radial):** Em sistemas de TC rotacionalmente simétricos, a NPS 2D é frequentemente convertida em uma função de frequência radial unidimensional $\text{NPS}(f)$, obtida por média azimutal:
   
$$
\text{NPS}(f) = \frac{1}{2\pi} \int_{0}^{2\pi} \text{NPS}(f \cos\theta, f \sin\theta) \, \, d\theta
$$

3. **Anisotropia:** Algoritmos modernos de reconstrução não linear ou iterativa frequentemente quebram a simetria rotacional, gerando uma NPS marcadamente anisotrópica (com comportamento de frequência direcional dependente), o que pode ser detectado analisando cortes angulares da NPS 2D.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Na prática clínica e industrial da Tomografia Computadorizada, a NPS é indispensável para:

* **Controle de Qualidade e Otimização de Protocolos:** Permite avaliar o impacto real de modificações na corrente do tubo (mAs), tensão (kVp) e filtros de quadratura na textura da imagem.
* **Caracterização de Reconstruções Avançadas (IR e DLR):** Algoritmos de Reconstrução Iterativa e Inteligência Artificial frequentemente exibem uma NPS dependente da dose e do contraste (propriedades não lineares e não estacionárias). A análise da NPS nestes sistemas revela se o algoritmo está suprimindo seletivamente altas frequências espaciais (simulando uma perda de resolução disfarçada de redução de ruído) ou preservando a textura natural.
* **Projeto de Observadores Computacionais:** Modelos de percepção visual humana e observadores ideais (como o *Non-Preembedding Signal-Known Statistically* - SKE/BKE) exigem o conhecimento rigoroso da NPS combinada com a Função de Transferência de Modulação (MTF) para prever a detectabilidade de lesões de baixo contraste (ex: nódulos pulmonares incipientes ou lesões hepáticas focais) por meio da métrica de Detectabilidade de Jones ($\text{d}'$).

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[Task Transfer Function|Função de Transferência de Modulação - MTF]]
* [[Detectabilidade e Observadores Computacionais]]
* [[Reconstrução Iterativa|Reconstrução Iterativa e DLR]]
* [[Dosimetria em Radiologia|Dosimetria em Tomografia Computadorizada]]
* [[Controle de Qualidade em TC|Controle de Qualidade em Imagem Médica]]
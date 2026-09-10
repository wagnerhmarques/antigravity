---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, controle-de-qualidade, metrologia, dosimetria, qualidade-de-imagem]
data: 2026-08-25
---

# Fantasmas_TC

## 1. Definição Conceitual e Fundamentação Física / Metrológica

Em Tomografia Computadorizada (TC) diagnóstica e terapêutica, os **fantasmas de TC** (*CT phantoms*) são dispositivos físicos metrologicamente calibrados, projetados para simular as propriedades de atenuação, espalhamento e absorção de radiação dos tecidos biológicos humanos. Eles constituem a base experimental indispensável para a metrologia da radiação ionizante, o controle de qualidade (CQ) regulatório, a otimização de protocolos clínicos e a validação de algoritmos avançados de reconstrução de imagem, como a Retroprojetção Filtrada (FBP), Reconstrução Iterativa (IR) e Reconstrução Baseada em Aprendizado Profundo (DLR).

Do ponto de vista físico-metrológico, o corpo humano é um meio heterogêneo tridimensional complexo. Os fantasmas são construídos com materiais equivalentes a tecidos (*tissue-equivalent materials*), cujos números atômicos efetivos ($Z_{\text{eff}}$) e massas específicas volumétricas ($\rho$) mimetizam tecidos específicos (por exemplo, tecido adiposo, tecido muscular, osso cortical, osso trabecular, parênquima pulmonar e água pura). A calibração de um tomógrafo com esses dispositivos garante a rastreabilidade metrológica das Unidades Hounsfield ($\text{HU}$), definidas em relação à atenuação linear da água e do ar:

$$
\text{HU} = 1000 \times \frac{\mu - \mu_{\text{água}}}{\mu_{\text{água}} - \mu_{\text{ar}}}
$$

onde $\mu$, $\mu_{\text{água}}$ e $\mu_{\text{ar}}$ representam os coeficientes de atenuação linear mássica efetivos do voxel, da água e do ar, respectivamente, para o espectro policromático de raios-X incidente.

Os fantasmas classificam-se estruturalmente em:
*   **Fantasmas Antropomórficos:** Possuem geometria e heterogeneidades anatômicas realistas (esqueleto sintético, cavidades pulmonares, órgãos parenquimatosos), sendo empregados em dosimetria complexa de órgãos e avaliação end-to-end de protocolos clínicos.
*   **Fantasmas Geométricos / Modulares:** Possuem formas geométricas simples (cilindros, esferas) e contêm módulos intercambiáveis para avaliação de parâmetros físicos específicos (resolução espacial, ruído, linearidade, uniformidade e artefatos).

---

## 2. Formulação Matemática e Propriedades (se aplicável)

A avaliação quantitativa da qualidade de imagem e do desempenho dos sistemas de TC utilizando fantasmas fundamenta-se em métricas matemáticas rigorosas aplicadas sobre matrizes de imagem digitalizadas.

### A. Uniformidade e Ruído de Imagem
A uniformidade espacial avalia a constância do valor médio de $\text{HU}$ em diferentes regiões de interesse ($\text{ROI}$) ao longo da seção transversal do fantasma cilíndrico de água. Sendo $\overline{\text{HU}}_c$ o valor médio no centro e $\overline{\text{HU}}_p$ o valor médio em uma ROI periférica, a não-uniformidade é expressa por:

$$
\Delta_{\text{unif}} = \left| \overline{\text{HU}}_c - \overline{\text{HU}}_p \right|
$$

O ruído da imagem, definido como a flutuação estatística dos números de tomografia em uma ROI homogênea de área $N$ pixels, é calculado pelo desvio padrão amostral:

$$
\sigma = \sqrt{\frac{1}{N - 1} \sum_{i=1}^{N} \left( \text{HU}_i - \overline{\text{HU}} \right)^2}
$$

### B. Função de Transferência de Modulação (MTF)
A resolução espacial de alto contraste é caracterizada pela Função de Transferência de Modulação ($\text{MTF}$), frequentemente derivada a partir da Função de Dispersão de Ponto ($\text{PSF}$) ou da Função de Espalhamento de Borda ($\text{ESF}$) obtida de fios finos (tungstênio ou platina) ou interfaces de alta densidade inseridas no fantasma. A $\text{MTF}$ como função da frequência espacial $f$ (em pares de linhas por centímetro, $\text{lp/cm}$) é a magnitude da transformada de Fourier da $\text{PSF}(x, y)$:

$$
\text{MTF}(f_x, f_y) = \left| \iint_{-\infty}^{\infty} \text{PSF}(x, y) e^{-j 2 \pi (f_x x + f_y y)} \, dx \, dy \right|
$$

Normalmente, reporta-se a frequência espacial correspondente a 50% ou 10% da modulação máxima ($\text{MTF}_{50}$ e $\text{MTF}_{10}$).

### C. Detectabilidade de Baixo Contrastes e NPS
A avaliação de estruturas de baixo contraste (simulando lesões hepáticas ou nodulares sutis) é modelada pelo Espectro de Potência do Ruído (*Noise Power Spectrum*, $\text{NPS}$), que descreve a textura espacial do ruído em função da frequência espacial $u$ e $v$:

$$
\text{NPS}(u, v) = \lim_{X, Y \to \infty} \frac{Ab}{X Y} \left\langle \left| \sum_{x, y} \left( \text{HU}(x, y) - \overline{\text{HU}} \right) e^{-j 2 \pi (ux + vy)} \right|^2 \right\rangle
$$

onde $Ab$ é a área do pixel e $\langle \cdot \rangle$ denota o operador de expectativa estatística. A integração da $\text{NPS}$ combinada com a $\text{MTF}$ permite estimar a Detectabilidade de alvos através de modelos de **Observadores Computacionais** (como o *Channelized Hotelling Observer* - $\text{CHO}$).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Os fantasmas de TC são ferramentas centrais em múltiplos domínios da física médica moderna:

1.  **Controle de Qualidade (CQ) Regulatório:**
    Programas de garantia de qualidade exigem varreduras periódicas (diárias, semanais e anuais) de fantasmas padronizados (como o fantasma ACR - *American College of Radiology* ou o fantasma Catphan) para monitorar desvios na calibração de $\text{HU}$, espessura de corte nominal, linearidade espacial, artefatos de anel ou endurecimento de feixe (*beam hardening*).
2.  **Dosimetria e Otimização de Dose:**
    Fantasmas dosimétricos cilíndricos de acrílico (PMMA) de diâmetros padronizados (16 cm para crânio e 32 cm para abdômen/corpo) contêm cavidades para inserção de câmaras de ionização tipo lápis. Eles são fundamentais para o cálculo do Índice de Dose em Tomografia Computadorizada ($\text{CTDI}_{\text{vol}}$) e do Produto Dose-Comprimento ($\text{DLP}$), parâmetros regulatórios essenciais para a otimização do balanço entre qualidade de imagem e risco radiobiológico.
3.  **Validação de Algoritmos Avançados (IR e DLR):**
    Com a introdução de algoritmos não-lineares de reconstrução, métricas tradicionais de ruído baseadas em desvio padrão tornam-se insuficientes, pois a textura do ruído varia com a dose e o sinal. Fantasmas especializados permitem avaliar a preservação de textura, a supressão de ruído dependente de dose e a prevenção de artefatos de "textura plástica" ou perda de resolução espacial em baixas doses.
4.  **Desenvolvimento de Observadores Computacionais:**
    A Inteligência Artificial aplicada à avaliação de imagens médicas utiliza conjuntos de dados gerados a partir de fantasmas físicos e digitais (*digital phantoms* / simuladores Monte Carlo) para treinar modelos preditivos de desempenho diagnóstico humano e robótico.

---

## 4. Conexões e Wikilinks

*   [[Unidades Hounsfield|Unidades_Hounsfield]]
*   [[Função Transferencia Modulacao|Funcao_Transferencia_Modulacao]]
*   [[CTDI_e_Dosimetria_TC]]
*   [[Reconstrucao_Iterativa_TC]]
*   [[Deep_Learning_Reconstruction_TC]]
*   [[Controle de Qualidade em TC|Controle_Qualidade_TC]]
*   [[Artefatos_Tomografia]]
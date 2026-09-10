---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, metrologia, controle-de-qualidade, reconstrucao-de-imagem]
data: 2026-08-25
---

# Dependencias_Eixo1

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O termo **Dependencias_Eixo1** refere-se ao conjunto de acoplamentos físicos, geométricos e metrológicos que governam a variação de parâmetros de imagem e desempenho dosimétrico ao longo do eixo longitudinal ($z$) de um sistema de Tomografia Computadorizada (TC). No contexto da metrologia aplicada à física médica, o "Eixo 1" (ou eixo z) é o vetor de translação do leito do paciente e de varredura do feixe de raios X helicoidal ou axial.

As dependências associadas a este eixo manifestam-se em múltiplos níveis:
1. **Geometria do Feixe e Perfil de Dose ($P(z)$):** A distribuição da dose de radiação ao longo do eixo $z$ não é perfeitamente retangular devido à dispersão (scatter) e à geometria focal finita, resultando em caudas de dose (dose tails) que afetam o cálculo do CTDI (Computed Tomography Dose Index).
2. **Homogeneidade e Resposta do Detector:** Variações na eficiência de conversão e na calibração dos elementos de detecção ao longo da direção longitudinal introduzem artefatos em anel helicoidais ou flutuações de número CT ($\text{HU}$).
3. **Filtração e Espectro de Energia:** A modulação da intensidade e o endurecimento do feixe (*beam hardening*) dependem da posição do gantry e da filtragem bow-tie, que varia dinamicamente em algumas arquiteturas para otimizar o perfil de dose longitudinal e transversal.
4. **Resolução Espacial Longitudinal:** Determinada pela largura do feixe colimado na isocentral ($T$), pelo passo da hélice (pitch, $p$) e pelo kernel de interpolação longitudinal (ex., algoritmos $3\pi$ ou $2\pi$ de ponderação em TC helicoidal).

Metrologicamente, a quantificação dessas dependências é essencial para garantir a reprodutibilidade dos exames, a acurácia dos protocolos de Inteligência Artificial voltados para a segmentação volumétrica e a conformidade com normas internacionais de controle de qualidade (como IEC 60601-2-44 e relatórios AAPM TG-111 e TG-200).

---

## 2. Formulação Matemática e Propriedades

A modelagem matemática das **Dependencias_Eixo1** envolve a integração do perfil de dose ao longo do eixo longitudinal e a formulação da resposta espacial do sistema. 

### Perfil de Dose Longitudinal e CTDI
O perfil de dose absorvida ao longo do eixo $z$\, denotado por $D(z)$, para uma varredura axial única com largura nominal de colimação $T$, é expresso por:

$$
D(z) = \int_{-\infty}^{\infty} \dot{d}(z, t) \, dt
$$

Para varreduras helicoidais, a dose acumulada em um ponto $z$ é dependente do *pitch* helicoidal $p$\, definido como:

$$
p = \frac{d}{N \cdot T}
$$

onde $d$ é o deslocamento do leito por rotação do gantry e $N \cdot T$ é a largura total nominal do feixe colimado no detector. A dose em equilíbrio para uma varredura helicoidal longa é inversamente proporcional ao *pitch*:

$$
D_{\text{helical}}(z) \approx \frac{1}{p} \cdot D_{\text{axial}}(z)
$$

### Interpolação e Resolução Longitudinal
Na reconstrução de imagens de TC helicoidal, os dados adquiridos em projeções oblíquas precisam ser reamostrados para planos axiais ortogonais ao eixo $z$. O processo de interpolação longitudinal utiliza funções de ponderação $w(z, \beta)$, onde $\beta$ é o ângulo do tubo. A resposta ao impulso espacial longitudinal ($PSF_z$) pode ser descrita pela convolução da abertura do detector com o núcleo de interpolação:

$$
PSF_z(z) = \text{Rect}\left(\frac{z}{T}\right) * W_{\text{kernel}}(z, p)
$$

Onde $W_{\text{kernel}}(z, p)$ representa o filtro de ponderación (por exemplo, algoritmos *Extended Interpolation* ou *pi-massage*). A Modulação da Função de Transferência (MTF) no eixo $z$ é dada pela transformada de Fourier do $PSF_z$:

$$
\text{MTF}_z(f_z) = \left| \mathcal{F} \left\{ PSF_z(z) \right\} \right|
$$

garantindo que flutuações nas **Dependencias_Eixo1** degradem diretamente a resolução espacial isotrópica se $p > 1$.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

O entendimento e o controle rigoroso das **Dependencias_Eixo1** são críticos em diversas frentes da Física Médica moderna:

* **Controle de Qualidade (CQ) e Dosimetria:** A avaliação da largura do feixe e do perfil de dose longitudinal ($P(z)$) em aberturas de múltiplos canais exige dosímetros de câmara de íon de comprimento estendido (ou o uso de dosimetria baseada em arranjos de estado sólido e filmes radiocrômicos) para evitar a subestimação da dose preconizada pelo AAPM TG-200.
* **Reconstrução Iterativa (IR) e Deep Learning Reconstruction (DLR):** Algoritmos avançados de reconstrução frequentemente assumem ruído estacionário e resposta espacial uniforme. Variações não corrigidas ao longo do Eixo 1 introduzem artefatos de "banding" (bandas transversોas) ou perda de resolução textural que podem confundir redes neurais convolucionais (CNNs) treinadas para detecção de lesões hepáticas ou pulmonares.
* **Redução de Dose por Modulação Automática de Corrente (ATCM):** Os sistemas de ATCM dependem da modulação longitudinal baseada no scout (topograma) para ajustar a corrente do tubo ($mA$) em função da atenuação do paciente ao longo do eixo $z$. Qualquer dessincronização entre a resposta do eixo 1 e a geometria do paciente resulta em saltos abruptos de ruído na imagem.
* **Observadores Computacionais:** A avaliação de desempenho de tarefas visuais por observadores modelo (como o *Channelized Hotelling Observer*) requer que a matriz de covariância do ruído seja caracterizada levando em conta a não-estacionaridade impuesta pelas dependências longitudinais.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia_Computadorizada]]
* [[Métricas de Dose em TC|CTDI]]
* [[Pitch Helicoidal|Pitch Helicoidal]]
* [[Reconstrução Iterativa|Reconstrucao_Iterativa]]
* [[Deep Learning Image Reconstruction (DLR)|Deep_Learning_Reconstruction]]
* [[Controle de Qualidade em TC|Controle_de_Qualidade_TC]]
* [[Dosimetria em TC|Dosimetria_em_TC]]
* [[Filtragem Bowtie|Filtro Bow-Tie]]
* [[Task Transfer Function|MTF]]
---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, qualidade-de-imagem, radiologia, metrologia, inteligencia-artificial]
data: 2026-08-25
---

# Qualidade de Imagem em Tomografia Computadorizada

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Qualidade de Imagem em Tomografia Computadorizada (TC)** é um construto multidimensional que define a acurácia com a qual a distribuição espacial dos coeficientes de atenuação linear de um objeto escaneado é representada na matriz digital reconstruída. Diferente da radiografia planar, onde a imagem é uma projeção bidimensional integrada, a TC reconstrói imagens tomográficas tridimensionais a partir de projeções angulares múltiplas ($0^\circ$ a $360^\circ$), exigindo uma rigorosa harmonia entre fatores físicos, geométricos, estatísticos e computacionais.

Metrologicamente, a qualidade da imagem em TC não pode ser reduzida a um único parâmetro. Ela é governada por um balanço estrito — frequentemente referido como o "tripé da TC" — entre:
1. **Resolução Espacial:** A capacidade de discriminar estruturas anatômicas de pequeno porte e alto contraste espacial.
2. **Resolução de Baixo Contraste (CNR e Ruído):** A habilidade de distinguir tecidos com diferenças sutis nos coeficientes de atenuação linear ($\mu$), limitada inerentemente pelas flutuações quânticas de fótons (ruído quântico) e ruído eletrônico do sistema.
3. **Artefatos:** Distorções geométricas, estrias, sombreamentos ou artefatos de feixe endurecido que corrompem a fidelidade quantitativa das Unidades Hounsfield (HU).

O princípio fundamental da formação da imagem baseia-se na Lei de Atenuação de Lambert-Beer para feixes policromáticos. O sinal detectado é uma função não-linear da energia dos fótons e da espessura do caminho atravessado. Consequentemente, a otimização da qualidade de imagem deve operar sob o paradigma **ALARA** (*As Low As Reasonably Achievable*), maximizando a diagnosticabilidade clínica enquanto minimiza a dose absorvida pelo paciente ($D$).

---

## 2. Formulação Matemática e Propriedades

Para quantificar rigorosamente a qualidade de imagem em TC, utilizam-se métricas espaciais e estatísticas consolidadas na teoria de sistemas lineares e na ciência de imagens.

### A. Ruído da Imagem e Desvio Padrão
O ruído em uma região de interesse homogênea (ROI) é tipicamente avaliado pelo desvio padrão ($\sigma$) dos valores de pixel em Unidades Hounsfield. Estatisticamente, assumindo contagens de fótons governadas pela distribuição de Poisson, a relação fundamental do ruído com a dose e o tamanho do voxel é dada por:

$$
\sigma \propto \frac{1}{\sqrt{N_0 \cdot \Delta_x \cdot \Delta_y \cdot \Delta_z \cdot D}}
$$

Onde:
* $N_0$ é a intensidade do feixe incidente (fluência de fótons).
* $\Delta_x, \Delta_y$ representam as dimensões do pixel no plano de reconstrução.
* $\Delta_z$ é a espessura do corte tomográfico.
* $D$ é a dose de radiação administrada.

### B. Função de Espalhamento de Ponto (PSF) e Função de Transferência de Modulação (MTF)
A **Função de Espalhamento de Ponto (PSF - *Point Spread Function*)** descreve a resposta do sistema de imagem a uma fonte pontual ideal. A **Função de Transferência de Modulação (MTF)** é formalmente definida como o módulo da transformada de Fourier bidimensional da PSF normalizada:

$$
\text{MTF}(u, v) = \left| \iint_{-\infty}^{\infty} \text{PSF}(x, y) \, e^{-j 2\pi (ux + vy)} \, dx \, dy \right|
$$

Normalmente avaliada em sua forma unidimensional radial, a frequência espacial na qual a MTF cai para 10% ($\text{MTF}_{10}$) é o padrão ouro metrológico para definir a resolução espacial limite do sistema.

### C. Função de Espalhamento de Ruído (NSF) e o Espectro de Potência de Wiener (NPS)
O ruído na TC não é puramente branco; ele é colorido pelo filtro de rampa e pelos filtros de reconstrução aplicados na Retroprojeção Filtrada (FBP). O **Espectro de Potência de Wiener (NPS - *Noise Power Spectrum*)** quantifica a textura e a distribuição espacial do ruído em função da frequência espacial $(f_x, f_y)$:

$$
\text{NPS}(f_x, f_y) = \lim_{X, Y \to \infty} \frac{1}{X Y} \left\langle \left| \iint_{X, Y} \left[ \mu(x,y) - \bar{\mu} \right] e^{-j 2\pi (f_x x + f_y y)} \, dx \, dy \right|^2 \right\rangle
$$

### D. Detectabilidade Ideal e o Índice de Detectabilidade ($d'$)
Para unificar resolução, ruído e a tarefa do observador, utiliza-se o índice de detectabilidade ($d'$) baseado no observador ideal de Hotelling ou na Teoria de Detecção de Sinais:

$$
(d')^2 = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \frac{|W(f_x, f_y)|^2 \cdot \text{MTF}^2(f_x, f_y)}{\text{NPS}(f_x, f_y)} \, df_x \, df_y
$$

Onde $W(f_x, f_y)$ representa a transformada de Fourier do sinal (objeto de teste) a ser detectado.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A gestão e quantitativa da qualidade de imagem são pilares na prática clínica moderna e na pesquisa translacional, desdobrando-se em quatro frentes principais:

* **Controle de Qualidade (CQ) Metrológico:** Utilização de fantasmas (*phantoms*) padronizados (como o fantasma ACR ou catphan) para monitorar periodicamente a linearidade do número de Hounsfield, uniformidade espacial, artefatos de anel, espessura de corte e resolução espacial limite.
* **Algoritmos de Reconstrução Avançados:** 
  * *Retroprojeção Filtrada (FBP):* Sofre de limitações severas de ruído em doses baixas.
  * *Reconstrução Iterativa (IR) e Model-Based Iterative Reconstruction (MBIR):* Incorporam modelos estatísticos complexos do sistema e da física de aquisição para suprimir o ruído mantendo a resolução de baixo contraste.
  * *Reconstrução Baseada em Inteligência Artificial (Deep Learning Reconstruction - DLR):* Redes neurais convolucionais (CNNs) treinadas para mapear imagens de alta ruído/baixa dose para o domínio de alta qualidade, preservando a textura anatômica sem os artefatos de "borracha" típicos de algoritmos iterativos antigos.
* **Dosimetria e Protocolos Personalizados:** O ajuste dinâmico da corrente do tubo baseada no tamanho e atenuação do paciente (Modulação de Corrente Automática - *ATCM*) e a seleção otimizada de quilovoltagem pico ($\text{kVp}$) visam manter a qualidade de imagem constante enquanto otimizam a dose efetiva.
* **Observadores Computacionais e IA:** Avaliação da qualidade de imagem não apenas por métricas puramente físicas (como RMSE ou PSNR), mas pelo desempenho de redes neurais e observadores humanos virtuais em tarefas clínicas específicas, como detecção de nódulos pulmonares ou acidentes vasculares cerebrais precoces.

---

## 4. Conexões e Wikilinks

* [[Física da Tomografia Computadorizada]]
* [[Unidades Hounsfield|Unidade Hounsfield]]
* [[Reconstrução de Imagem|Reconstrução de Imagem em TC]]
* [[Filtros de Retroprojeção Filtrada]]
* [[Reconstrução Iterativa|Reconstrução Iterativa e DLR]]
* [[Artefatos em Tomografia Computadorizada]]
* [[Dosimetria em Radiologia|Dosimetria em Radiologia Diagnóstica]]
* [[Controle de Qualidade em TC|Controle de Qualidade em Radiologia]]
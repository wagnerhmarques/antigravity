---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, controle-de-qualidade, metrologia-das-radiacoes, dosimetria, radioprotecao]
data: 2026-08-25
---

# Control de Qualidade em CT

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **Controle de Qualidade em Tomografia Computadorizada (CT)** engloba o conjunto sistemático de procedimentos operacionais, físicos, metrológicos e computacionais destinados a garantir que um sistema de CT opere dentro de tolerâncias estipuladas, maximizando a qualidade diagnóstica da imagem e minimizando a dose de radiação ionizante absorvida pelo paciente. Do ponto de vista metrológico, o controle de qualidade atua como a garantia de rastreabilidade e constância das grandezas físicas associadas tanto à geração e modulação do feixe de raios X quanto à conversão optoeletrônica e processamento digital da imagem.

A fundamentação física baseia-se na avaliação rigorosa da cadeia de formação de imagem tomográfica, a qual transita desde a emissão estocástica de fótons de raios X pelo tubo até a reconstrução matemática por retroprojeção filtrada ([[FBP|FBP - Filtered Backprojection]]) ou algoritmos avançados baseados em aprendizado profundo ([[DLR - Deep Learning Reconstruction]] e [[IR - Iterative Reconstruction]]). As falhas sistemáticas ou estocásticas no sistema — tais como flutuações na alta tensão ($kVp$), degradação do ânodo, descalibração dos elementos detetores de cintilação (geralmente cerâmicas de gadolínio ou granada) e instabilidades na geometria do gantry — manifestam-se diretamente na matriz de coeficientes de atenuação linear reconstruídos $\mu(x,y,z)$.

Os programas de controle de qualidade são estruturados em níveis de periodicidade (diários, semanais, mensais e anuais) e utilizam fantomas antropomórficos e geométricos padronizados (como o fantoma ACR - *American College of Radiology* ou fantomas IEC equivalentes) preenchidos com água, materiais tecidos-equivalentes, e insertos de alta densidade (teflon, osso, acrílico, ar e polietileno).

---

## 2. Formulação Matemática e Propriedades

Para quantificar o desempenho físico de um sistema de CT, diversas métricas matemáticas e estatísticas são avaliadas através de análise de imagem em regiões de interesse (ROIs). 

### A. Número de Tomografia Computadorizada (Unidades Hounsfield - HU)
O valor de um pixel é convertido em Unidades Hounsfield para normalizar o coeficiente de atenuação linear do tecido ($\mu$) em relação ao da água ($\mu_{\text{água}}$) sob a mesma energia efetiva do feixe:

$$
\text{HU} = 1000 \times \frac{\mu - \mu_{\text{água}}}{\mu_{\text{água}} - \mu_{\text{ar}}}
$$

Onde $\mu_{\text{ar}}$ é tipicamente considerado igual a $0 \, \text{cm}^{-1}$.

### B. Ruído da Imagem e Desvio Padrão
O ruído em CT é fundamentalmente limitado pela estatística de fótons (ruído quântico de Poisson) e pela filtragem espacial do algoritmo de reconstrução. É medido estatisticamente como o desvio padrão ($\sigma$) dos valores de pixel em uma ROI homogênea localizada no centro de um fantoma de água:

$$
\sigma_{\text{ROI}} = \sqrt{\frac{1}{N - 1} \sum_{i=1}^{N} \left( \text{HU}_i - \overline{\text{HU}} \right)^2}
$$

Onde $N$ é o número total de pixels na ROI e $\overline{\text{HU}}$ é a média aritmética dos valores de pixel na região.

### C. Função de Transferência de Modulação (MTF)
A resolução espacial é rigorosamente descrita pela Função de Transferência de Modulação (MTF), que representa o módulo da transformada de Fourier da Função de Dispersão do Ponto (PSF - *Point Spread Function*):

$$
\text{MTF}(
u) = \left| \mathcal{F} \left\{ \text{PSF}(x,y) \right\} \right| = \left| \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \text{PSF}(x,y) e^{-j 2\pi (
u_x x + 
u_y y)} \, dx \, dy \right|
$$

Onde $
u$representa a frequência espacial expressa em pares de linhas por centímetro ($\text{lp/cm}$). A frequência de corte (frequentemente avaliada no limiar de$\text{MTF} = 0.1$ou$10\%$) define o limite de resolução espacial discernível do sistema.

### D. Função de Espalhamento de Borda (ESF) e LSF
Na prática, devido à dificuldade de criar uma fonte pontual infinitesimal, mede-se a Função de Espalhamento de Borda ($\text{ESF}$) a partir de uma interface abrupta entre dois materiais de densidades distintas. A derivada da $\text{ESF}$ resulta na Função de Espalhamento de Linha ($\text{LSF}$):

$$
\text{LSF}(x) = \frac{d}{dx} \left[ \text{ESF}(x) \right]
$$

### E. Doutrinação Dosimétrica: CTDI e DLP
A dosimetria em CT baseia-se no Índice de Dose em Tomografia Computadorizada ($\text{CTDI}$), integrado ao longo do eixo $z$. O $\text{CTDI}_{100}$ é definido por:

$$
\text{CTDI}_{100} = \frac{1}{nT} \int_{-50\,\text{mm}}^{+50\,\text{mm}} D(z) \, dz
$$

Onde $n$ é o número de cortes tomográficos gerados simultaneamente por varredura, $T$ é a espessura nominal de cada corte no isocentro, e $D(z)$ é o perfil de dose ao longo do eixo longitudinal $z$ medido com uma câmara de ionização tipo lápis de $100\,\text{mm}$ de comprimento.

Para corrigir assimetrias espaciais entre o centro e a periferia do fantoma (corpo ou crânio), calcula-se o $\text{CTDI}_{\text{w}}$ (ponderado):

$$
\text{CTDI}_{\text{w}} = \frac{1}{3} \text{CTDI}_{100,\text{centro}} + \frac{2}{3} \text{CTDI}_{100,\text{periferia}}
$$

Considerando o avanço tecnológico com a varredura helicoidal e a modulação de corrente, o índice normalizado pelo passo da hélice ($pitch$, $p$) é o $\text{CTDI}_{\text{vol}}$:

$$
\text{CTDI}_{\text{vol}} = \frac{\text{CTDI}_{\text{w}}}{p}
$$

Por fim, o Produto Dose-Comprimento ($\text{DLP}$), que correlaciona a energia total depositada com o volume anatômico escaneado de comprimento $L$, é dado por:

$$
\text{DLP} = \text{CTDI}_{\text{vol}} \times L
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

O controle de qualidade em CT transcende o mero cumprimento de normativas regulatórias (como resoluções da CNEN ou equivalentes internacionais da IAEA e AAPM); ele constitui o alicerce operacional para a **otimização da dose** e a **fidelidade diagnóstica**. 

Com a proliferação de algoritmos avançados de reconstrução ([[IR - Iterative Reconstruction]] e [[DLR - Deep Learning Reconstruction]]), a relação tradicional entre ruído, dose e resolução espacial foi profundamente alterada. Sistemas de DLR, treinados em redes neurais profundas para remover ruído estruturado e artefatos de quantum, exigem um controle de qualidade metrológico rigoroso para assegurar que a supressão de ruído não induza ao mascaramento de patologias sutis (como nódulos pulmonares precoces ou pequenos AVCs isquêmicos) ou à distorção radiômica em pipelines de [[Radiômica e Textura em CT]].

Ademais, na era da tomografia quantitativa (QCT) e de exames perfusionais avançados, a constância da calibração em HU é mandatória. Desvios na linearidade do número de Hounsfield comprometem diretamente a acurácia de mapas de perfusão cerebral, quantificação de esteatose hepática e densitometria óssea quantitativa. A avaliação contínua de observadores computacionais (como a avaliação automatizada da MTF e do ruído por softwares dedicados de CQ) mitiga a variabilidade inter-observador humana e assegura o princípio ALARA (*As Low As Reasonably Achievable*).

---

## 4. Conexões e Wikilinks

- [[FBP|FBP - Filtered Backprojection]]
- [[IR - Iterative Reconstruction]]
- [[DLR - Deep Learning Reconstruction]]
- [[Radiômica e Textura em CT]]
- [[Física da Radiação X e Interação com a Matéria]]
- [[Dosimetria em Radiodiagn Stico|Dosimetria em Radiodiagnóstico]]
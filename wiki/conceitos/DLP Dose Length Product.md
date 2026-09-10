---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, dosimetria, radioprotecao, dlp, qualidade-da-imagem]
data: 2026-08-25
---

# dlp-dose-length-product

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **Produto Dose-Comprimento** (em inglês, *Dose-Length Product* - **DLP**) é uma grandeza dosimétrica fundamental utilizada em Tomografia Computadorizada (TC) para quantificar a energia total depositada por uma varredura tomográfica completa em um fantoma padrão ou, por extensão, no paciente. Diferentemente do Índice de Dose em Tomografia Computadorizada ($\text{CTDI}$), que mede a intensidade da dose de radiação absorvida em um único corte ou rotação por unidade de comprimento nominal do feixe, o $\text{DLP}$ integra essa dose ao longo de todo o eixo longitudinal ($z$) do escaneamento.

Metrologicamente, o $\text{DLP}$ não representa a dose de radiação absorvida em um tecido ou órgão específico (dose absorvida em $\text{Gy}$ ou $\text{J/kg}$), mas sim uma grandeza correlacionada à energia total impartida ao longo da extensão anatômica irradiada. É o parâmetro primário exibido nas estações de trabalho dos scanners de TC e nos relatórios estruturados de dose (*Dose Structured Reports* - RDSR) para descrever a carga estocástica global imposta pelo exame. 

A compreensão física do $\text{DLP}$ fundamenta-se na integração espacial da dose ao longo da direção do movimento da mesa do tomógrafo. Enquanto o $\text{CTDI}_{\text{vol}}$ reflete a severidade da exposição local, o $\text{DLP}$ pondera essa severidade pelo volume anatômico coberto, tornando-se indispensável para a otimização de protocolos e para a epidemiologia da radiação médica.

---

## 2. Formulação Matemática e Propriedades

Matematicamente, o $\text{DLP}$ é definido como a integral ao longo do eixo longitudinal $z$ do Índice de Dose em Tomografia Computadorizada ponderado ($\text{CTDI}_{\text{w}}$) ou volumétrico ($\text{CTDI}_{\text{vol}}$):

$$
\text{DLP} = \int_{-L/2}^{L/2} \text{CTDI}_{\text{vol}}(z) \, dz
$$

Onde:
- $L$ representa o comprimento total da varredura anatômica (em $\text{cm}$).
- $\text{CTDI}_{\text{vol}}(z)$ é o índice de dose volumétrico, o qual pode variar ao longo do eixo $z$ em sistemas com modulação de corrente automática de tubo (*Automatic Tube Current Modulation* - ATCM).

Para varreduras helicoidais ou axiais convencionais onde os parâmetros de aquisição (corrente, tensão, filtragem do feixe e colimação) permanecem constantes ao longo do eixo $z$, a formulação se simplifica para o produto algébrico entre o $\text{CTDI}_{\text{vol}}$ e o comprimento efetivo da varredura ($L$):

$$
\text{DLP} = \text{CTDI}_{\text{vol}} \times L
$$

No contexto de aquisições helicoidais (espirais), o comprimento $L$ é determinado pelo produto entre o número total de rotações ($N_{\text{rot}}$), a espessura nominal do feixe colimado ($T$) e o passo helicoidal ($p$, ou *pitch*):

$$
L = N_{\text{rot}} \times T \times p
$$

### Unidades de Medida
A unidade SI para o $\text{DLP}$ é o miliGray-centímetro ($\text{mGy}\cdot\text{cm}$), derivado da multiplicação do $\text{CTDI}_{\text{vol}}$ (expresso em $\text{mGy}$) pelo comprimento linear (expresso em $\text{cm}$).

### Conversão para Dose Efetiva
Embora o $\text{DLP}$ quantifique a exposição física, a avaliação de risco radiológico estocástico requer a estimativa da Dose Efetiva ($E$, em $\text{mSv}$). Esta conversão é realizada multiplicando-se o $\text{DLP}$ por um coeficiente deconversão específico para a região anatômica inspecionada, denotado por $k$:

$$
E = \text{DLP} \times k_{\text{região}}
$$

Os coeficientes $k$ (em $\text{mSv}\cdot\text{mGy}^{-1}\cdot\text{cm}^{-1}$) são derivados de simulações de Monte Carlo utilizando modelos antropomórficos computacionais (fantasmas matemáticos e voxelizados) e variam significativamente dependendo da região anatômica (por exemplo, crânio vs. tórax vs. abdome) e da faixa etária do paciente (pediátrico vs. adulto).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

### Controle de Qualidade e Conformidade Regulatória
O $\text{DLP}$ serve como indicador essencial para o estabelecimento de Níveis de Referência Diagnósticos (NRDs ou *Diagnostic Reference Levels* - DRLs) estabelecidos por agências reguladoras (como a Comissão Nacional de Energia Nuclear - CNEN, ou órgãos internacionais como a ICRP). Hospitais e clínicas utilizam o $\text{DLP}$ cumulativo por procedimento para auditar a prática clínica e identificar protocolos que excedam as médias estabelecidas para exames semelhantes.

### Otimização de Protocolos e Reconstrução de Imagem
Com o advento de técnicas avançadas de reconstrução, como a **[[Retroprojeção Filtrada (FBP)|FBP]]**, **[[Reconstrução Iterativa|Reconstrução Iterativa (IR)]]** e abordagens baseadas em **[[Deep Learning Reconstruction (DLR)|Inteligência Artificial e DLR]]**, o $\text{DLP}$ tornou-se a métrica balizadora para estudos de redução de dose. As técnicas de DLR permitem que a qualidade diagnóstica da imagem seja mantida ou aprimorada mesmo quando o $\text{CTDI}_{\text{vol}}$ e, consequentemente, o $\text{DLP}$, são reduzidos drasticamente.

### Dosimetria Baseada em Inteligência Artificial e Automação
Sistemas modernos integrados à IA utilizam o $\text{DLP}$ extraído automaticamente dos metadados DICOM (por meio de *Dose Tracking Systems*) para estimar a dose específica em órgãos de maneira individualizada, superando as limitações dos coeficientes globais $k$. Redes neurais profundas podem mapear a geometria do paciente obtida em imagens de *topograma* (scout) combinada com o $\text{DLP}$ nominal para prever mapas tridimensionais de dose absorvida com alta acurácia computacional.

---

## 4. Conexões e Wikilinks

- [[Métricas de Dose em TC|CTDI (Computed Tomography Dose Index)]]
- [[Métricas de Dose em TC|CTDI_vol]]
- [[effective-dose|Dose Efetiva]]
- [[Retroprojeção Filtrada (FBP)|Filtered Back-Projection (FBP)]]
- [[Reconstrução Iterativa|Reconstrução Iterativa]]
- [[Deep Learning Reconstruction (DLR)|Reconstrução Baseada em Deep Learning (DLR)]]
- [[automatic-tube-current-modulation|Modulação Automática de Corrente de Tubo (ATCM)]]
- [[Níveis de Referência Diagnóstica (DRL)|Níveis de Referência Diagnósticos (NRD)]]
- [[monte-carlo-simulation-in-dosimetry|Simulação de Monte Carlo em Dosimetria]]
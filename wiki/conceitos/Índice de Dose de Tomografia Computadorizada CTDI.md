---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, dosimetria, radioprotecao, ctdi]
data: 2026-08-25
---

# indice-de-dose-de-tomografia-computadorizada-ctdi

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **Índice de Dose de Tomografia Computadorizada** (em inglês, *Computed Tomography Dose Index* - **CTDI**) é a métrica padrão fundamental utilizada em dosimetria de raios-X em tomografia computadorizada (TC) para quantificar a dose de radiação emitida por uma única rotação do tubo de raios-X. Diferente da radiografia convencional, onde a dose é frequentemente avaliada pelo produto dose-área (DAP) ou dose na pele incidente, a geometria helicoidal ou axial da TC exige uma abordagem que considere o perfil de dose acumulado ao longo do eixo longitudinal do paciente ($z$).

Metrologicamente, o CTDI baseia-se na integração do perfil de dose ao longo de uma varredura completa, normalizada pela largura nominal do feixe de radiação. A mensuração padrão é realizada utilizando câmaras de ionização de tipo lápis (*pencil ionization chambers*), tipicamente com comprimento ativo de $100\text{ mm}$, posicionadas no interior de fantomas cilíndricos padronizados de polimetilmetacrilato (PMMA). Esses fantomas simulam a atenuação e o espalhamento da radiação em dimensões típicas da cabeça (diâmetro de $16\text{ cm}$) e do corpo/abdome (diâmetro de $32\text{ cm}$).

O conceito evoluiu para mitigar as limitações inerentes à heterogeneidade anatômica e à distribuição espacial da dose, servindo como base para métricas mais avançadas de avaliação de risco e otimização de protocolos radiológicos.

---

## 2. Formulação Matemática e Propriedades

A formulação matemática do CTDI fundamenta-se no conceito de perfil de dose axial $D(z)$, que representa a distribuição de dose absorvida ao longo do eixo $z$ para uma rotação única do tubo.

O **CTDI básico** ou **$CTDI_{100}$** é definido pela integral do perfil de dose $D(z)$ ao longo de um comprimento de integração de $100\text{ mm}$, centrado no plano de tomografia ($z = 0$), normalizado pelo produto do número de tomografias ($N$) e pela largura nominal de cada tomografia ($T$):

$$
CTDI_{100} = \frac{1}{N \cdot T} \int_{-50\text{ mm}}^{+50\text{ mm}} D(z) \, dz
$$

Onde:
- $N$ é o número de cortes tomográficos adquiridos simultaneamente por rotação.
- $T$ é a espessura (largura nominal) de cada corte no eixo isocêntrico ($mm$).
- $D(z)$ é a taxa de dose absorvida em função da posição $z$ ($mGy$).

Devido à variação da dose entre a periferia e o centro do fantoma de PMMA — causada pela atenuação do feixe e pelo espalhamento Compton —, define-se o **$CTDI_{w}$ (CTDI ponderado)**. Esta métrica pondera as medições centrais e periféricas para estimar a dose média na seção transversal do fantoma:

$$
CTDI_{w} = \frac{1}{3} CTDI_{100,\text{centro}} + \frac{2}{3} CTDI_{100,\text{periferia}}
$$

Onde $CTDI_{100,\text{periferia}}$ é a média aritmética obtida em quatro posições angulares distintas (geralmente $0^\circ, 90^\circ, 180^\circ \text{ e } 270^\circ$) localizadas a uma profundidade de $1\text{ cm}$ abaixo da superfície interna do fantoma.

Para sistemas modernos de aquisição helicoidal (espiral), introduz-se o **$CTDI_{vol}$ (CTDI volumétrico)**, que incorpora o efeito do passo da hélice (*pitch*, denotado por $p$). O $CTDI_{vol}$ representa a dose média real administrada no volume escaneado, considerando o espaçamento ou sobreposição entre as rotações consecutivas:

$$
CTDI_{vol} = \frac{CTDI_{w}}{p}
$$

Onde o passo da hélice $p$ é definido como:
- Para sistemas de múltiplos detectores (MDCT): $p = \frac{d}{N \cdot T}$, sendo $d$ o avanço da mesa por rotação completa.

Finalmente, para correlacionar a energia depositada com o risco estocástico em todo o volume anatomicamente irradiado, define-se o **Produto Dose-Comprimento** (*Dose-Length Product* - **DLP**), expresso em $\text{mGy}\cdot\text{cm}$:

$$
DLP = CTDI_{vol} \cdot L
$$

Onde $L$ é o comprimento total da varredura anatômica (excluindo a sobreposição inicial/final de over-ranging).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

O CTDI e suas variantes ($CTDI_{w}$, $CTDI_{vol}$, DLP) constituem os pilares fundamentais para o controle de qualidade, a conformidade regulatória e a **otimização de protocolos** em tomografia computadorizada.

1. **Controle de Qualidade e Conformidade Regulatória:**
   Físicos médicos utilizam o $CTDI_{100}$ e o $CTDI_{w}$ durante os testes de aceitação e controle de qualidade periódico dos equipamentos de TC para verificar se a saída de radiação do tubo está em conformidade com as tolerâncias dos fabricantes e as diretrizes de agências reguladoras.

2. **Gerenciamento de Dose e Níveis de Referência Diagnósticos (NRD):**
   O $CTDI_{vol}$ é a métrica obrigatória exibida na console de todos os scanners de TC comerciais antes e após a varredura (indicada nos relatórios DICOM *Radiation Dose Structured Report* - RDSR). Ele serve de base para o estabelecimento de Níveis de Referência Diagnósticos (DRLs), permitindo comparar a prática clínica de uma instituição com benchmarks nacionais e internacionais.

3. **Reconstrução de Imagem e Algoritmos Avançados:**
   Embora o CTDI meça a energia entregue ao fantoma independentemente do algoritmo de reconstrução utilizado (seja Retroprojeção Filtrada - FBP, Reconstrução Iterativa - IR, ou Deep Learning Reconstruction - DLR), o conhecimento rigoroso do $CTDI_{vol}$ permite avaliar a *eficiencia de dose*. Algoritmos avançados (IR e DLR) mantêm a qualidade diagnóstica e a detectabilidade de baixo contraste (avaliadas por observadores computacionais) sob valores de $CTDI_{vol}$ significativamente reduzidos.

4. **Limitações e Evolução para Dosimetria Preditiva:**
   O CTDI apresenta limitações fundamentais: ele **não** representa a dose real absorvida por um paciente específico, pois os fantomas de PMMA padronizados não refletem a biometria real (peso, altura, índice de massa corporal - IMC). Por essa razão, o CTDI atua como um índice normalizado de desempenho da máquina, sendo complementado em dosimetria avançada por métricas como o **Tamanho Específico de Dose** (*Size-Specific Dose Estimate* - **SSDE**), que ajusta o $CTDI_{vol}$ com base nas dimensões transversais do paciente obtidas a partir do próprio topograma.

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|tomografia-computadorizada]]
- [[dosimetria-em-radiodiagnostico]]
- [[produto-dose-comprimento-dlp]]
- [[tamanho-especifico-de-dose-ssde]]
- [[fantomas-dosimetricos-pmma]]
- [[niveis-de-referencia-diagnosticos-drl]]
- [[Reconstrução Iterativa|reconstrucao-iterativa-ir]]
- [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction-dlr]]
- [[Controle de Qualidade em TC|controle-de-qualidade-em-tc]]
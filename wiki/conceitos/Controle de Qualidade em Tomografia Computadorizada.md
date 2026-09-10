---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, controle-de-qualidade, metrologia-das-radiacoes, dosimetria, otimizacao-de-imagem]
data: 2026-08-25
---

# controle-de-qualidade-em-tomografia-computadorizada

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **Controle de Qualidade em Tomografia Computadorizada (CQ-TC)** constitui o conjunto sistemático de procedimentos operacionais, físicos, metrológicos e computacionais destinados a garantir que um sistema de Tomografia Computadorizada (TC) opere de maneira otimizada, reprodutível e segura. O objetivo primário é duplo: maximizar a diagnosticabilidade clínica da imagem reconstruída e minimizar a dose de radiação ionizante depositada no paciente, em estrita conformidade com os princípios de radioproteção (justificação, otimização e limitação de dose).

Do ponto de vista metrológico, o CQ-TC fundamenta-se na avaliação quantitativa de parâmetros físicos estritos utilizando fantomas padronizados (frequentemente acrílico, poliestireno, teflon, ar e água, simulando o coeficiente de atenuação linear humano). Os testes são classificados temporalmente em:
- **Testes de Aceitação (Commissioning):** Realizados pelo físico médico na instalação do equipamento para verificar o cumprimento das especificações contratuais e regulatórias do fabricante.
- **Testes de Desempenho de Rotina (Constância):** Executados periodicamente (diariamente, semanalmente, mensalmente ou anualmente) por tecnólogos ou físicos médicos para detectar desvios sutis ou degradação progressiva de componentes críticos (tubo de raios X, gerador, matriz de detectores, sistema de aquisição de dados - DAS, e algoritmos de reconstrução).

Os parâmetros físicos fundamentais avaliados englobam:
1. **Exatidão e Uniformidade do Número de Hounsfield (HU):** A calibração numérica que mapeia o coeficiente de atenuação linear ($\mu$) de um voxel em uma escala normalizada onde a água destilada é $0\text{ HU}$ e o ar é $-1000\text{ HU}$.
2. **Ruído da Imagem e Resolução de Baixo Contraste (Low-Contrast Detectability - LCD):** A capacidade de distinguir estruturas com pequenas diferenças nos coeficientes de atenuação linear ($\Delta\mu / \mu$), intimamente correlacionada com a dose e a modulação quântica de fótons.
3. **Resolução Espacial (High-Contrast Spatial Resolution):** A capacidade de discriminar objetos anatômicos finos e espacialmente próximos, limitada pelo tamanho do ponto focal (*focal spot*), geometria do sistema, amostragem dos detectores e funções de espalhamento de borda (ESF) ou linha (LSF).
4. **Espessura de Corte Tomográfica:** Verificação do perfil de sensibilidade ao longo do eixo $z$, garantindo que a espessura nominal do corte corresponda à física real.
5. **Dosimetria Computadorizada:** Mensuração e verificação de índices dosimétricos padronizados, como o Índice de Dose em Tomografia Computadorizada ponderado ($CTDI_{w}$), o Índice de Dose em Tomografia Computadorizada volumétrico ($CTDI_{vol}$) e o Produto Dose-Comprimento ($DLP$).

---

## 2. Formulação Matemática e Propriedades

A avaliação cuantitativa no CQ-TC baseia-se em formulações matemáticas rigurosas que traduzem propriedades físicas em métricas de desempenho de imagem.

### Escala de Número de Hounsfield (HU)
O valor de pixels em unidades Hounsfield é definido linearmente em relação ao coeficiente de atenuação linear do material analisado ($\mu$) em comparação com a água ($\mu_{\text{água}}$) e o ar ($\mu_{\text{ar}}$):

$$
\text{HU} = 1000 \times \frac{\mu - \mu_{\text{água}}}{\mu_{\text{água}} - \mu_{\text{ar}}}
$$

Como o ar possui $\mu_{\text{ar}} \approx 0$, a equação simplifica-se operacionalmente para:

$$
\text{HU} = 1000 \times \frac{\mu - \mu_{\text{água}}}{\mu_{\text{água}}}
$$

### Ruído da Imagem e Desvio Padrão
O ruído da imagem ($\sigma_{\text{img}}$) é quantificado estatisticamente pelo desvio padrão dos valores de pixels medidos em uma Região de Interesse (ROI - *Region of Interest*) central homogênea inserida em um fantoma de água:

$$
\sigma_{\text{img}} = \sqrt{\frac{1}{N - 1} \sum_{i=1}^{N} \left( \text{HU}_i - \overline{\text{HU}} \right)^2}
$$

Onde $N$ é o número total de pixels na ROI, $\text{HU}_i$ é o valor do pixel $i$, e $\overline{\text{HU}}$ é a média aritmética dos valores de HU na ROI.

### Função de Modulação de Transferência (MTF)
A resolução espacial é rigorosamente caracterizada pela Função de Modulação de Transferência (MTF - *Modulation Transfer Function*), que representa a magnitude da transformada de Fourier da Função de Espalhamento de Linha (LSF):

$$
\text{MTF}(f) = \left| \int_{-\infty}^{\infty} \text{LSF}(x) e^{-i 2 \pi f x} dx \right|
$$

Na prática clínica e de controle de qualidade, a LSF é frequentemente derivada da derivada espacial da Função de Espalhamento de Borda ($\text{ESF}(x)$):

$$
\text{LSF}(x) = \frac{d}{dx} \left[ \text{ESF}(x) \right]
$$

### Dosimetria: $CTDI_{100}$, $CTDI_{w}$ e $CTDI_{vol}$
O Índice de Dose em Tomografia Computadorizada é integrado ao longo de um eixo de varredura linear de $100\text{ mm}$ utilizando uma câmara de ionização tipo *pencil*. O $CTDI_{100}$ é definido por:

$$
CTDI_{100} = \frac{1}{nT} \int_{-50\text{ mm}}^{+50\text{ mm}} D(z) \, dz
$$

Onde $n$ é o número de cortes tomográficos simultâneos, $T$ é a espessura nominal de cada corte, e $D(z)$ é o perfil de dose ao longo do eixo $z$.

O $CTDI$ ponderado ($CTDI_{w}$) pondera as doses medidas no centro e na periferia de fantomas cilíndricos padronizados de polimetilmetacrilato (PMMA) — tipicamente de $16\text{ cm}$ de diâmetro (cabeça) e $32\text{ cm}$ de diâmetro (corpo):

$$
CTDI_{w} = \frac{1}{3} CTDI_{100,\text{centro}} + \frac{2}{3} CTDI_{100,\text{periferia}}
$$

Finalmente, o $CTDI_{vol}$ normaliza o $CTDI_{w}$ pelo passo da hélice (*pitch*, denotado por $I$ ou $p$), avaliando a energia média depositada por unidade de comprimento durante exames helicoidais:

$$
CTDI_{vol} = \frac{CTDI_{w}}{p}
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

O CQ-TC moderno estendeu-se muito além da verificação mecânica e dosimétrica tradicional, integrando-se profundamente aos modernos paradigmas de reconstrução e avaliação computacional.

### Otimização em Algoritmos de Reconstrução Avançados
Com a transição dos métodos clássicos de Retroprojeção Filtrada (FBP) para a Reconstrução Iterativa (IR) e algoritmos baseados em Inteligência Artificial e Aprendizado Profundo (*Deep Learning Reconstruction* - DLR), os protocolos de controle de qualidade exigem novas métricas. Algoritmos DLR tendem a suprimir ruído de maneira não linear, alterando a textura da imagem (frequências espaciais do ruído) e potencialmente mascarando artefatos ou mascarando a detecção de baixo contraste. O CQ-TC avalia o espectro de potência do ruído (NPS - *Noise Power Spectrum*) e a Task-based MTF para assegurar que a otimização de dose não comprometa a detectabilidade diagnóstica de lesões sutis (como nódulos pulmonares incipientes ou pequenos adenomas hepáticos).

### Observadores Computacionais e Avaliação Baseada em Tarefas
Testes contemporâneos de CQ utilizam modelos matemáticos de observadores humanos (como o *Non-Prewhitening Matched Filter with an Eye Filter* - NPWE ou o *Channelized Hotelling Observer* - CHO) para prever o desempenho diagnóstico em tarefas específicas de detecção (ex: detecção de lesões de baixo contraste em imagens de fígado). Isso substitui a subjetividade visual humana tradicional por critérios estocásticos e quantitativos rigorosos.

### Gestão da Dose e Conformidade Regulatória
Através de auditorias periódicas e do monitoramento contínuo dos indicadores de dose ($CTDI_{vol}$ e $DLP$), o CQ-TC assegura que os protocolos clínicos estejam alinhados aos Níveis de Referência Diagnóstica (NRD / DRL - *Diagnostic Reference Levels*) estabelecidos por agências reguladoras (como a CNEN no Brasil ou órgãos internacionais como a ACR e a IAEA).

---

## 4. Conexões e Wikilinks

- [[reconstrucao-em-tomografia-computadorizada]]
- [[fbp-reconstrucao-retroprojecao-filtrada]]
- [[reconstrucao-iterativa-tomografia]]
- [[deep-learning-reconstruction-tomografia]]
- [[Dosimetria em Radiologia|dosimetria-em-tomografia-computadorizada]]
- [[ctdi-volume-e-dlp]]
- [[Artefatos em Tomografia Computadorizada|artefatos-em-tomografia-computadorizada]]
- [[fisica-medica-das-radiacoes]]
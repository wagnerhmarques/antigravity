---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, dosimetria, aquisicao-de-dados, otimizacao-de-dose]
data: 2026-08-25
---

# fator-de-pitch

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **fator de pitch** (frequentemente abreviado apenas como *pitch*) é um parâmetro adimensional fundamental na Tomografia Computadorizada (TC) helicoidal (ou espiral). Ele rege a relação geométrica entre o avanço translacional da mesa do paciente e a colimação do feixe de raios X ao longo do eixo longitudinal ($z$) durante uma rotação completa do tubo de raios X.

Historicamente, com o advento da TC helicoidal de canal único (terceira geração) na década de 1990, a definição padronizada pelo *International Electrotechnical Commission* (IEC) e pela *American Association of Physicists in Medicine* (AAPM - Report 39 e Report 111) divergiu sutilmente dependendo da arquitetura do scanner (monocanal vs. multicanal/MDCT). 

Em sistemas de múltiplos cortes (*Multi-Detector Computed Tomography* - MDCT), a definição formal e universalmente aceita é dada pela distância percorrida pela mesa em uma rotação de $360^\circ$ dividida pela largura nominal total do feixe colimado no isocentro do gantry. 

O fator de pitch determina diretamente:
1. A **velocidade de varredura** e o tempo total de apneia do paciente.
2. A **sobreposição** ou **lacuna** espacial dos dados de projeção adquiridos no domínio $z$.
3. A **dose de radiação absorvida** pelo paciente (sendo inversamente proporcional ao pitch para uma corrente de tubo constante).
4. Os artefatos potenciais decorrentes do processo de interpolação longitudinal (*longitudinal interpolation artifacts*).

---

## 2. Formulação Matemática e Propriedades

Matematicamente, o fator de pitch ($\left( P \right)$) em sistemas MDCT é formulado rigorosamente como:

$$
P = \frac{d}{N \times T}
$$

Onde:
* $d$ é o deslocamento linear da mesa por rotação de $360^\circ$ do gantry ($\text{mm}$).
* $N$ é o número total de canais de dados adquiridos simultaneamente (número de cortes ativos).
* $T$ é a espessura nominal de cada corte individual (*detector row collimation*) medida no isocentro ($\text{mm}$).

O produto $N \times T$ representa a **largura nominal total do feixe** ($W$) na direção do eixo $z$:

$$
W = N \times T
$$

Portanto, a equação pode ser reescrita de forma compacta como:

$$
P = \frac{d}{W}
$$

### Regimes Operacionais do Fator de Pitch

Dependendo do valor numérico de $P$, a aquisição se enquadra em três regimes distintos:

1. **Sub-pitch ($P < 1.0$):**
   * A mesa avança uma distância menor que a largura total do feixe por rotação.
   * Ocorre **sobreposição de amostragem** (oversampling) no eixo $z$.
   * Consequências: Aumento da dose de radiação proporcional ao fator $1/P$ (se os parâmetros de corrente-tempo forem mantidos) e melhora potencial na resolução espacial longitudinal e na relação sinal-ruído (SNR), à custa de um tempo de varredura mais longo.

2. **Pitch Unitário ($P = 1.0$):**
   * O avanço da mesa por rotação é exatamente igual à largura do feixe.
   * Representa a amostragem padrão de referência em muitos protocolos clínicos legados, equilibrando cobertura, tempo de exame e dose.

3. **Super-pitch ($P > 1.0$):**
   * A mesa avança uma distância maior que a largura do feixe por rotação.
   * Ocorre **subamostragem** (undersampling) geométrica direta, criando lacunas potenciais que exigem algoritmos sofisticados de interpolação longitudinal (como o algoritmo $180^\circ\text{LI}$ ou $360^\circ\text{LI}$) para estimar os dados faltantes antes da reconstrução por retroprojeção filtrada ([[reconstrucao-fbp]]).
   * Consequências: Redução drástica do tempo de varredura (essencial para pacientes politraumatizados ou com restrição respiratória) e diminuição da dose de radiação ($Dose \propto 1/P$). No entanto, valores excessivamente altos de $P$ introduzem artefatos em hélice (*helices artifacts*) e degradação da resolução espacial no eixo $z$ devido à largura efetiva do *slice sensitivity profile* (SSP) se tornar maior.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

### Dosimetria e Otimização de Dose
O fator de pitch é uma das variáveis operacionais mais potentes para o gerenciamento e otimização da dose de radiação ionizante. A dose em TC é parametrizada pelo Índice de Dose em Tomografia Computadorizada ($\text{CTDI}_{\text{vol}}$). A relação matemática que governa essa dependência é:

$$
\text{CTDI}_{\text{vol}} = \frac{\text{CTDI}_{\text{w}}}{P}
$$

Onde $\text{CTDI}_{\text{w}}$ é a dose ponderada no manequim de referência. Esta relação demonstra que, mantendo inalterados os demais parâmetros de aquisição (como quilovoltagem $\text{kVp}$, produto corrente-tempo $\text{mAs}$ e filtros de bowtie), **o aumento do fator de pitch resulta em uma redução linear da dose** absorvida pelo paciente. 

### Qualidade de Imagem e Ruído
Embora o aumento do pitch reduza a dose, ele também diminui o número total de fótons X coletados por unidade de comprimento do paciente, o que teoricamente elevaria o ruído quântico da imagem. Contudo, scanners modernos utilizam modulação automática de corrente ([[modulacao-de-corrente-mAs]]) acoplada a algoritmos avançados de reconstrução iterativa ([[Reconstrução Iterativa|reconstrucao-iterativa]]) e inteligência artificial ([[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction-dlr]]) para compensar dinamicamente essas perdas, preservando a radiância diagnóstica.

### Artefatos e Perfil de Sensibilidade do Corte (SSP)
Valores elevados de pitch forçam os algoritmos de interpolação a interpolar dados ao longo de distâncias angulares e longitudinais maiores. Isso resulta no alargamento do *Slice Sensitivity Profile* (SSP), o que degrada a resolução espacial no eixo longitudinal ($z$) e pode causar artefatos de borramento estrutural (*windmill artifacts* ou artefatos de cata-vento), especialmente em interfaces de alto contraste (como base do crânio ou junções ósseas).

---

## 4. Conexões e Wikilinks

* [[tomografia-computadorizada-helicoidal]]
* [[reconstrucao-fbp]]
* [[Reconstrução Iterativa|reconstrucao-iterativa]]
* [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction-dlr]]
* [[Métricas de Dose em TC|ctdi-vol]]
* [[modulacao-de-corrente-mAs]]
* [[Artefatos em TC|artefatos-em-tomografia]]
* [[Resolução Espacial|resolucao-espacial]]
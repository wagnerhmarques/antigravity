---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, dosimetria, radioprotecao, metrologia-das-radiacoes]
data: 2026-08-25
---

# dose-absorvida

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **dose-absorvida** ($D$) é a grandeza fundamental da dosimetria das radiações ionizantes, representando a energia média depositada pela radiação ionizante por unidade de massa em um material especificado. Do ponto de vista metrológico, estabelecida pelo *Système International d'Unités* (SI), a sua unidade derivada é o **gray** ($\text{Gy}$), onde $1\text{ Gy} = 1\text{ J}\cdot\text{kg}^{-1}$. 

Historicamente sucedendo o *rad* ($1\text{ rad} = 10^{-2}\text{ Gy}$), a dose-absorvida é aplicável a qualquer tipo de radiação ionizante (fótons, elétrons, prótons, nêutrons e íons pesados) e a qualquer meio material (tecido biológico, ar, água, silício, etc.). 

A fundamentação física baseia-se na transferência de energia dos campos de radiação primários e secundários para os elétrons atômicos e moleculares do meio através de processos de ionização e excitação. A energia transferida não é necessariamente local; portanto, a distinção entre **energia transferida** ($\varepsilon_{\text{tr}}$) e **energia absorvida** ($\varepsilon$) é governada pelo balanço de energia de radiação nas imediações do volume elementar de interesse, considerando o transporte de fótons secundários (como raios $bremsstrahlung$ gerados por elétrons rápidos).

Em Tomografia Computadorizada (TC) e radiobiologia, a dose-absorvida no tecido é o preditor primário de efeitos estocásticos (como indução de câncer) e determinísticos (como eritema cutâneo ou catarata), embora sua correlação direta com o dano biológico exija correções por fatores de qualidade da radiação, resultando em grandezas como a dose equivalente e a dose efetiva.

## 2. Formulação Matemática e Propriedades (se aplicável)

Matematicamente, a dose-absorvida $D$ é definida pelo quociente da energia média $\mathrm{d}\bar{\varepsilon}$ impartida pela radiação ionizante a um elemento de matéria de massa $\mathrm{d}m$:

$$
D = \frac{\mathrm{d}\bar{\varepsilon}}{\mathrm{d}m}
$$

Onde:
- $\mathrm{d}\bar{\varepsilon}$ é a energia total média impartida (energia total fornecida ao volume menos a energia que deixa o volume através de partículas secundárias radiativas).
- $\mathrm{d}m$ é a massa do elemento infinitesimal de volume $\mathrm{d}V$, expressa por $\mathrm{d}m = \rho \, \mathrm{d}V$, sendo $\rho$ a massa específica local do meio.

Portanto, a formulação diferencial pode ser reescrita como:

$$
D(\vec{r}) = \frac{1}{\rho(\vec{r})} \frac{\mathrm{d}\bar{\varepsilon}}{\mathrm{d}V}
$$

Para campos de radiação de fótons estáticos sob condições de equilíbrio eletrônico transitório ou carregado (provenientes de feixes de raios-X de TC), a dose-absorvida em um ponto pode ser relacionada ao kerma no ar livre ($K_{\text{air}}$) por meio de fatores de conversão deFluência de Energia ($\Psi$) e coeficientes de atenuação mássica:

$$
D_{\text{med}} = \Psi \cdot \left( \frac{\bar{\mu}_{\text{en}}}{\rho} \right)_{\text{med}}
$$

Onde $\left( \frac{\bar{\mu}_{\text{en}}}{\rho} \right)_{\text{med}}$ representa o coeficiente de absorção de energia mássica médio espectral para o meio considerado.

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Na Tomografia Computadorizada, a dose-absorvida não é medida diretamente em pacientes durante os exames clínicos, mas inferida através de protocolos padronizados de mensuração utilizando **câmaras de ionização** tipo *pencil beam* em **fantasmas** de polimetilmetacrilato (PMMA) cilíndricos padronizados (fantasmas de cabeça de $16\text{ cm}$ e de corpo de $32\text{ cm}$).

A partir das medições de dose-absorvida em múltiplos pontos (periféricos e centrais), derivam-se as métricas operenciais de otimização e controle de qualidade:
- **CTDI** (*Computed Tomography Dose Index*): Índice de dose que quantifica a dose-absorvida normalizada ao longo do eixo de rotação ($z$) para uma única rotação do tubo.
- **CTDI$_{\text{w}}$** (*Weighted CTDI*): Média ponderada que corrige a distribuição heterogênea de dose entre a periferia e o centro do fantasma:
  
$$
\text{CTDI}_{\text{w}} = \frac{1}{3}\text{CTDI}_{\text{periférica}} + \frac{2}{3}\text{CTDI}_{\text{central}}
$$

- **CTDI$_{\text{vol}}$** e **DLP** (*Dose Length Product*): Métricas que incorporam o *pitch* helicoidal e o comprimento total escaneado, correlacionando-se diretamente com a energia total depositada e a estocasticidade do risco radiológico.

**Otimização e Inteligência Artificial:**
A modelagem precisa da dose-absorvida é essencial para algoritmos de **reconstrução iterativa (IR)** e algoritmos baseados em **Deep Learning (DLR)**. Redes neurais profundas focadas em redução de ruído de dose baixa (*low-dose CT denoising*) utilizam mapas de dose-absorvida derivados de simulações de **Monte Carlo** voxelizadas para treinar modelos preditivos capazes de preservar a textura de ruído e a detectabilidade de lesões em limiares sub-milisievert. Além disso, softwares de modulação de corrente automatizada (*Tube Current Modulation - TCM*) ajustam o fluxo de fótons em tempo real baseados em topogramas para manter a dose-absorvida uniforme independentemente da atenuação geométrica do paciente.

## 4. Conexões e Wikilinks

- [[Métricas de Dose em TC|ctdi]]
- [[Métricas de Dose em TC|dlp]]
- [[kerma]]
- [[fantasmas-de-calibracao]]
- [[Simulação de Monte Carlo|simulacao-monte-carlo]]
- [[Reconstrução Iterativa|reconstrucao-iterativa]]
- [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction]]
- [[otimizacao-em-tc]]
- [[efeitos-biologicos-das-radiacoes]]
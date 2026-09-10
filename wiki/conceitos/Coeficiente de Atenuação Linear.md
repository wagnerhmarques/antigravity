---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, radiologia, radioprotecao, processamento-de-imagem]
data: 2026-08-25
---

# coeficiente-de-atenuacao-linear

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **coeficiente de atenuação linear** ($\mu$) é uma grandeza físico-metrológica fundamental que quantifica a probabilidade de interação e remoção de fótons de radiação ionizante (como raios X ou gama) por unidade de comprimento percorrida em um meio material específico. Em termos macroscópicos, $\mu$ descreve a taxa de atenuação da intensidade de um feixe de radiação colimado (fótons primários) por centímetro de matéria atravessada.

A magnitude de $\mu$ depende intrinsecamente de três fatores fundamentais:
1. **Número atômico ($Z$)** do material: Elementos de alto $Z$ apresentam maior densidade eletrônica e interações mais intensas.
2. **Densidade física ($\rho$)** do meio (geralmente expressa em $\text{g/cm}^3$): Quanto mais compactos estiverem os átomos, maior será a probabilidade de colisão do fóton.
3. **Energia do fóton incidentes ($E$):** O coeficiente diminui à medida que a energia do feixe policromático ou monocromático aumenta, exceto nas descontinuidades de absorção (bordas de absorção K, L, etc.).

As interações predominantes que governam o coeficiente de atenuação linear na faixa de energia diagnóstica da Tomografia Computadorizada (tipicamente de $30\text{ keV}$ a $140\text{ keV}$) são o **Efeito Fotoelétrico** e o **Espalhamento Compton** (Incoerente). O espalhamento Rayleigh (coerente) e a produção de pares possuem contribuições negligenciáveis ou nulas nessa faixa energética.

---

## 2. Formulação Matemática e Propriedades

A formulação macroscópica da atenuação de um feixe de radiação monocromática é descrita pela **Lei de Lambert-Beer**. Para um feixe incidindo perpendicularmente sobre um meio homogêneo de espessura $x$, a variação diferencial da intensidade $I$ é proporcional à intensidade incidente e à espessura infinitesimal $dx$:

$$
dI = -\mu I \, dx
$$

Integrando esta equação diferencial ordinária de primeira ordem para uma espessura finita $x$, obtém-se a intensidade emergente $I(x)$:

$$
I(x) = I_0 \exp\left( -\int_{0}^{x} \mu(x') \, dx' \right)
$$

No caso particular de um meio homogêneo, onde $\mu$ é espacialmente constante, a equação se simplifica para:

$$
I(x) = I_0 e^{-\mu x}
$$

Onde:
* $I_0$ é a intensidade inicial (ou fluxo de fótons incidentes).
* $I(x)$ é a intensidade transmitida após atravessar a espessura $x$.
* $\mu$ é o coeficiente de atenuação linear, expresso tipicamente em $\text{cm}^{-1}$.

### Coeficiente de Atenuação Massico
Como $\mu$ varia diretamente com a densidade física ($\rho$) do material — visto que um gás rarefeito e um líquido da mesma substância química possuem propriedades atômicas idênticas, mas densidades macroscopicamente distintas —, define-se o **coeficiente de atenuação mássico** ($\mu_m$):

$$
\mu_m = \frac{\mu}{\rho}
$$

Onde $\mu_m$ é expresso em $\text{cm}^2/\text{g}$. Esta grandeza é independente do estado físico da matéria (sólido, líquido ou gasoso) e depende estritamente da composição elementar do meio e da energia do fóton, podendo ser aditiva para misturas e compostos químicos através da regra de Bragg:

$$
\mu_m = \sum_{i} w_i (\mu_m)_i
$$

Onde $w_i$ é a fração mássica do $i$-ésimo elemento constitutivo.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

No contexto da **Tomografia Computadorizada (TC)**, o objetivo primário do sistema de aquisição e reconstrução é mapear a distribuição espacial tridimensional dos coeficientes de atenuação linear no interior do corpo do paciente, representados em uma matriz discreta de voxels.

### 1. Problema Direto e Inverso na Reconstrução
Os detectores de TC medem projeções que correspondem à atenuação integral ao longo de trajetórias de raios (linhas de projeção), expressas pela transformada de Radon:

$$
P_{\theta}(t) = \ln\left(\frac{I_0}{I}\right) = \int_{\text{linha}} \mu(x, y) \, ds
$$

Algoritmos de **Retroprojeção Filtrada (FBP)**, métodos Iterativos (IR) e abordagens baseadas em Aprendizado Profundo (Deep Learning Reconstruction - DLR) operam resolvendo o problema inverso para estimar os valores exatos de $\mu(x, y)$ em cada pixel da imagem reconstruída.

### 2. A Escala Hounsfield (HU)
Como os valores absolutos de $\mu$ dependem do espectro de energia do tubo de raios X (endurecimento do feixe ou *beam hardening*) e dificultam a padronização clínica, a TC utiliza a **Escala Hounsfield** para normalizar os coeficientes de atenuação linear em relação à água:

$$
\text{HU} = 1000 \times \frac{\mu - \mu_{\text{água}}}{\mu_{\text{água}} - \mu_{\text{ar}}}
$$

Sabendo que $\mu_{\text{ar}} \approx 0$, a fórmula é frequentemente aproximada por:

$$
\text{HU} = 1000 \times \frac{\mu - \mu_{\text{água}}}{\mu_{\text{água}}}
$$

### 3. Controle de Qualidade e Tomografia Espectral (DECT)
Em **Tomografia Computadorizada de Dupla Energia (Dual-Energy CT - DECT)**, a dependência energética do coeficiente de atenuação linear é explorada para decomposição material (ex: separação de iodo, cálcio e gordura). Ao adquirir dados em dois espectros distintos (ex: $80\text{ kVp}$ e $140\text{ kVp}$), o sistema resolve um sistema de equações lineares explorando a variação de $\mu(E)$ em função do número atômico efetivo e da densidade eletrônica.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|tomografia-computadorizada]]
* [[escala-hounsfield]]
* [[interacao-da-radiacao-com-a-materia]]
* [[efeito-fotoetrico]]
* [[Espalhamento Compton|espalhamento-compton]]
* [[Endurecimento do Feixe|endurecimento-do-feixe]]
* [[Tomografia Computadorizada Espectral|tomografia-de-dupla-energia]]
* [[Reconstrução de Imagem|reconstrucao-de-imagem]]
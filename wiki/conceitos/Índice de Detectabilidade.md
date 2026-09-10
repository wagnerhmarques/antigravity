---
tipo: conceito
aliases:
  - d'
  - dprime
  - detectability-index
  - indice-de-detectabilidade
  - detectabilidade-index
  - indice-de-detectabilidade-em-tomografia-computadorizada
tags:
  - metrologia
  - qualidade-imagem
  - aapm-tg233
  - fisica-medica
---

# Índice de Detectabilidade ($d'$) em Tomografia Computadorizada

## 1. Definição Conceitual e Fundamentação Física

O **Índice de Detectabilidade** ($d'$, *d-prime*) é a métrica objetiva padrão-ouro da física médica contemporânea (formalizada pelo relatório **[[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg233-ct-performance]]**, ICRU Report 54 e ICRU Report 98) para quantificar a qualidade diagnóstica de uma imagem tomográfica baseada em tarefa (*Task-Based Image Quality* - [[Task Based Image Quality|task-based-image-quality]]).

Diferentemente de métricas clássicas puramente físicas como a Relação Sinal-Ruído ([[Contrast To Noise Ratio|CNR]]) e a Resolução Espacial isolada ([[Task Transfer Function|TTF]]), o índice $d'$ sintetiza a capacidade estatística de um observador (humano ou matemático - [[Observadores de Modelo (Model Observers)|model-observers]]) discriminar uma hipótese de sinal presente ($H_1$) contra uma hipótese de apenas ruído de fundo ($H_0$).

---

## 2. Formulação Matemática Rigorosa (Espaço de Fourier & Teoria de Decisão)

### A. Definição Estatística Fundamental (Teoria de Detecção de Sinais)
Pela Teoria de Detecção de Sinais (SDT), $d'$ quantifica a separação normalizada entre as distribuições das variáveis de decisão sob as hipóteses $H_1$ (sinal presente) e $H_0$ (sinal ausente):

$$
d' = \frac{\langle t \rangle_{H_1} - \langle t \rangle_{H_0}}{\sqrt{\frac{1}{2} \left( \sigma_{t, H_1}^2 + \sigma_{t, H_0}^2 \right)}}
$$

No paradigma psicofísico Two-Alternative Forced Choice ([[Estudo de Observadores 2AFC|2-AFC]]), a fração de acertos observados ($P_c$) relaciona-se diretamente com $d'$ através da função de distribuição acumulada da normal padrão ($\Phi$):

$$
P_c = \Phi\left( \frac{d'}{\sqrt{2}} \right) \iff d' = \sqrt{2} \cdot \Phi^{-1}(P_c)
$$

---

### B. Observador Linear Ideal / Hotelling (Prewhitening - PW)
No domínio contínuo da frequência espacial bidimensional $\mathbf{u} = (u, v)$, para ruído estacionário gaussiano:

$$
d'^2_{\text{PW}} = \iint_{-\infty}^{\infty} \frac{\left| W_{\text{task}}(u, v) \right|^2 \cdot \left[ \text{TTF}(u, v) \right]^2}{\text{NPS}(u, v)} \, du \, dv
$$

Onde:
* $W_{\text{task}}(u, v) = \mathcal{F}\{\Delta \mu(x, y)\}$ é a **Função de Tarefa** (*Task Function*)\, dada pela Transformada de Fourier 2D da diferença de atenuação do sinal anatômico/patológico em relação ao fundo circundante;
* $\text{TTF}(u, v)$ é a **[[Task Transfer Function|Task-based Transfer Function]]**, que descreve a resposta em frequência e preservação de contraste do sistema para o contraste específico do sinal;
* $\text{NPS}(u, v)$ é o **[[Noise Power Spectrum|Noise Power Spectrum]]**, que descreve a potência e correlação espacial do ruído estocástico.

---

### C. Observador Não-Branqueador com Filtro Visual Humano (NPWE)
Para predizer a percepção de médicos radiologistas, o modelo NPWE incorpora o filtro visual do olho humano $E(u, v)$ e o ruído interno de decisão ($\sigma_{\text{int}}$):

$$
d'^2_{\text{NPWE}} = \frac{\left[ \iint_{-\infty}^{\infty} \left| W_{\text{task}}(u, v) \right|^2 \cdot \left[ \text{TTF}(u, v) \right]^2 \cdot \left[ E(u, v) \right]^2 \, du \, dv \right]^2}{\iint_{-\infty}^{\infty} \left| W_{\text{task}}(u, v) \right|^2 \cdot \left[ \text{TTF}(u, v) \right]^2 \cdot \text{NPS}(u, v) \cdot \left[ E(u, v) \right]^4 \, du \, dv + \sigma_{\text{int}}^2}
$$

O filtro visual humano $E(f)$ (parametrizado em ciclos por grau de ângulo visual para uma distância de observação $d_{\text{obs}}$) é comumente modelado por:

$$
E(f) = |f|^c \exp\left( -k |f|^d \right)
$$

---

### D. Integração Polar 1D (Simetria Radial / Isotropia)
Quando o sinal e a textura do ruído exibem simetria radial no plano tomográfico ($f = \sqrt{u^2 + v^2}$):

$$
d'^2_{\text{NPWE}} = \frac{\left[ 2\pi \int_{0}^{\infty} \left| W_{\text{task}}(f) \right|^2 \cdot \left[ \text{TTF}(f) \right]^2 \cdot \left[ E(f) \right]^2 \cdot f \, df \right]^2}{2\pi \int_{0}^{\infty} \left| W_{\text{task}}(f) \right|^2 \cdot \left[ \text{TTF}(f) \right]^2 \cdot \text{NPS}(f) \cdot \left[ E(f) \right]^4 \cdot f \, df + \sigma_{\text{int}}^2}
$$

---

### E. Formulação Matricial Discreta (Hotelling & Channelized Hotelling Observer - CHO)
Para imagens discretizadas com vetor de sinal $\Delta\bar{\mathbf{g}} = \bar{\mathbf{g}}_1 - \bar{\mathbf{g}}_0$ e matriz de covariância do ruído $\mathbf{K} \in \mathbb{R}^{N \times N}$:

$$
d'^2_{\text{Hotelling}} = \Delta\bar{\mathbf{g}}^T \mathbf{K}^{-1} \Delta\bar{\mathbf{g}}
$$

Ao aplicar $M$ canais antropomórficos (ex: *Gabor* ou *Dense Difference of Gaussians* - D-DOG) representados pela matriz $\mathbf{U} \in \mathbb{R}^{N \times M}$:

$$
d'^2_{\text{CHO}} = \left( \mathbf{U}^T \Delta\bar{\mathbf{g}} \right)^T \left( \mathbf{U}^T \mathbf{K} \mathbf{U} \right)^{-1} \left( \mathbf{U}^T \Delta\bar{\mathbf{g}} \right)
$$

---

## 3. Contexto no Acervo do Pesquisador & Aplicações

O Índice de Detectabilidade ($d'$) atua como a métrica mestre de otimização em todo o acervo do pesquisador:

1. **Avaliação Não-Linear de Deep Learning ([[Deep Learning Image Reconstruction (DLR)|deep-learning-image-reconstruction]] - DLR):**  
   Conforme documentado em [[Greffier 2026 - Avaliação de DLR em TC com Phantoms|greffier-2026-dlr-ct-phantom]], algoritmos de DLR (TrueFidelity, AiCE, Precise Image) não preservam a linearidade clássica. O cálculo de $d'$ combinando $\text{TTF}_{50\%}$ e $\text{NPS}$ permite comprovar aumentos de até $+154\%$ na detectabilidade de lesões de baixo contraste em protocolos de baixa dose ([[Otimização de Dose em TC|otimizacao-de-dose-em-tc]]).
2. **Observadores Profundos com Atenção ([[Deep Learning Model Observer|deep-learning-model-observer]] - DL-MO):**  
   No projeto de Doutorado Direto FAPESP ([[Projeto Doutorado Direto FAPESP Wagner 2026|projeto-dd-fapesp-wagner-2026]]), o observador convolucional com mecanismos de autoatenuação é treinado para estimar $d'$ diretamente de sinogramas e volumes 3D em phantoms físicos antropomórficos ([[Phantoms Híbridos|phantoms-hibridos]] e [[Pixelprint]]), sendo validado contra experimentos psicofísicos de radiologistas ([[Estudo de Observadores 2AFC|2afc-observer-study]]).
3. **Otimização Multiobjetivo no Espaço de Pareto ([[Otimização Multiobjetivo em TC|otimizacao-multiobjetivo-tc]] / [[Algoritmo Genético NSGA-II|nsga-ii]]):**  
   O índice $d'$ atua como a função-objetivo primária de qualidade de imagem ($\max d'$), balanceada simultaneamente contra a minimização de dose ($\min \text{CTDI}_{\text{vol}}$) e minimização de meio de contraste ([[Otimização e Redução de Meio de Contraste em TC|otimizacao-meio-de-contraste-tc]]).

---

## 4. Conexões & Leituras Recomendadas

* [[Task Transfer Function|task-transfer-function]] — Medição da resolução espacial dependente de contraste
* [[Noise Power Spectrum|noise-power-spectrum]] — Caracterização e textura do ruído estocástico
* [[Observadores de Modelo (Model Observers)|model-observers]] — Modelos matemáticos de observadores computacionais
* [[Deep Learning Model Observer|deep-learning-model-observer]] — Observador baseado em Deep Learning e Atenção
* [[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg233-ct-performance]] — Diretrizes oficiais da AAPM para avaliação baseada em tarefas
* [[Estudo de Observadores 2AFC|2afc-observer-study]] — Protocolo psicofísico de validação com observadores humanos
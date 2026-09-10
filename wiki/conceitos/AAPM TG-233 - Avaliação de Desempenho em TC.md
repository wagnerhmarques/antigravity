---
tipo: conceito
aliases: [aapm-tg233-ct-performance, aapm-tg-233-summary, "aapm tg 233", tg233, TG-233, aapm-tg-233]
tags: [fisica-medica, tomografia-computadorizada, task-based-image-quality, aapm-tg233\, dlp\, dler, nps, ttf]
data: 2026-08-25
---

# aapm-tg233-ct-performance

## 1. Definição Conceitual e Fundamentação Física
O relatório **AAPM Task Group 233 (TG-233)**, intitulado *"An Extension of the ACCR Quality Control Manual for CT: Evaluation of Computed Tomography Systems Using Task-Based Performance Measures"*, constitui o marco metrológico contemporâneo mais avançado para a avaliação da qualidade de imagem em Tomografia Computadorizada (TC). Tradicionalmente, o controle de qualidade baseava-se em métricas visuais subjetivas (como matrizes de furos e testes de barras) ou em métricas pixel-a-pixel simplistas, tais como o Ruído padrão e a Razão Contraste-Ruído ([[Contrast To Noise Ratio|CNR]]). No entanto, com a introdução generalizada de algoritmos de reconstrução iterativa (IR) e, mais recentemente\, de reconstrução baseada em Inteligência Artificial / Deep Learning Reconstruction ([[Greffier 2026 - Avaliação de DLR em TC com Phantoms|DLR]]), essas métricas tradicionais tornaram-se insuficientes. Os algoritmos modernos introduzem não-linearidades espaciais, texturas de ruído não-estacionárias e dependências severas da dose e do objeto digital.

O **AAPM TG-233** substitui esse paradigma obsoleto pela **Qualidade de Imagem Baseada em Tarefas** (*Task-Based Image Quality*), uma abordagem quantitativa que avalia o desempenho dos sistemas de TC simulando a capacidade de um observador (humano ou matemático) realizar uma tarefa diagnóstica específica — tipicamente a detecção ou discriminação de uma lesão de baixo contraste (ex: nódulos pulmonares, lesões hepáticas). A fundamentação física reside na caracterização completa da cadeia de imagem linear e quase-linear através de três pilares fundamentais:
1. A **Função de Transferência de Tarefa ([[task-function|TTF]])**, que descreve a resolução espacial dependente do contraste e do nível de sinal.
2. O **Espectro de Potência de Ruído ([[Noise Power Spectrum|NPS]])**, que quantifica a magnitude e a textura espacial (frequencial) do ruído.
3. O **Índice de Detectabilidade ([[Índice de Detectabilidade|Detectability Index, $d'$]])**\, derivado de modelos de observadores matemáticos ([[NPWE Model Observer|npwe-model-observer]], [[Channelized Hotelling Observer (CHO)|cho-model-observer]]), que sintetiza a TTF e o NPS em uma métrica unificada de desempenho diagnóstico.

---

## 2. Formulação Matemática e Propriedades

A avaliação formal da qualidade de imagem baseada em tarefas fundamenta-se na análise de Fourier do sistema de imagem de TC. 

### A. Função de Transferência de Tarefa (TTF)
A TTF estende o conceito tradicional da Função de Transferência de Modulação (MTF) para objetos de baixo contraste e sistemas não-linearizados, avaliando a resposta espacial em função da amplitude do sinal. Seja $I(x,y)$ a imagem reconstruída de um objeto de teste cilíndrico de inserção com contraste nominal $\Delta C$, a TTF em função da frequência espacial radial $f$ é calculada a partir do perfil de borda linearizado:

$$
\text{TTF}(f) = \left| \frac{\mathcal{F} \left\{ \frac{d}{dr} \text{Perfil}(r) \right\}}{\mathcal{F} \left\{ \frac{d}{dr} \text{Perfil}_{\text{ideal}}(r) \right\}} \right|_{f}
$$

Onde $\mathcal{F}$ denota o operador de Transformada de Fourier unidimensional ou bidimensional radial, e $r$ é a coordenada radial a partir do centro do inserto.

### B. Espectro de Potência de Ruído (NPS)
O NPS bidimensional, $\text{NPS}(f_x, f_y)$, caracteriza a variabilidade espacial e a textura estatística do ruído na imagem, sendo definido como a densidade espectral de potência da imagem de ruído residual $\Delta I(x,y) = I(x,y) - \bar{I}(x,y)$:

$$
\text{NPS}(f_x, f_y) = \lim_{L_x, L_y \to \infty} \frac{\Delta x \Delta y}{L_x L_y} \left| \sum_{n_x} \sum_{n_y} \Delta I(n_x \Delta x, n_y \Delta y) e^{-i 2\pi (f_x n_x \Delta x + f_y n_y \Delta y)} \right|^2
$$

Em sistemas com DLR ou reconstruções iterativas avançadas, o NPS deixa de ser plano (branco) e passa a exibir picos em frequências específicas, alterando a percepção visual da textura do ruído.

### C. Índice de Detectabilidade ($d'$)
O desempenho na detecção de uma tarefa visual (ex: sinal matemático conhecido em fundo estocástico conhecido - SKE/BKE) é quantifiedo pelo índice de detectabilidade $d'$ para um observador modelo linear (como o Non-Prewhitened Match Filter with Eye Filter - NPWE):

$$
d'^2 = \frac{\left[ \iint \text{W}(f_x, f_y) |\text{W}_{\text{task}}(f_x, f_y)|^2 \text{TTF}(f_x, f_y)^2 \, df_x \, df_y \right]^2}{\iint \text{W}(f_x, f_y)^2 \text{NPS}(f_x, f_y) |\text{W}_{\text{task}}(f_x, f_y)|^4 \, df_x \, df_y}
$$

Onde $\text{W}_{\text{task}}(f_x, f_y)$ representa a transformada de Fourier do perfil da tarefa (sinal a ser detectado) e $\text{W}(f_x, f_y)$ é a função de filtro do observador humano (filtro visual).

---

## 3. Contexto no Acervo do Pesquisador & Aplicações

Dentro da LLM Wiki de Física Médica & Tomografia Computadorizada (USP/FAPESP), o termo `aapm-tg233-ct-performance` atua como a **âncora metrológica central** para múltiplos desdobramentos de pesquisa e desenvolvimento em doutorado:

- **Automação de Métricas e Observadores Profundos:** Conforme documentado em `queries/Como devo começar a estruturar o observador profundo, por onde começo?.md` e `queries/Comente sobre a evolução dos modelos de observadores computacionais...md`, o arcabouço do TG-233 é a base conceitual para a automatização de rotinas que extraem TTF, NPS e calculam observadores matemáticos lineares clássicos (`[[NPWE Model Observer|npwe-model-observer]]`, `[[Channelized Hotelling Observer (CHO)|cho-model-observer]]`) e suas extensões baseadas em aprendizado profundo.
- **Desafios da Não-Linearidade em DLR:** Como apontado em `queries/Qual é o estado da arte das tecnologias...md` e `queries/O que é ttf e porque ele é importante?.md`, os modelos clássicos do TG-233 assumem linearidade e estacionaridade de ruído. No entanto, a introdução de algoritmos de Deep Learning Reconstruction (`[[Greffier 2026 - Avaliação de DLR em TC com Phantoms|greffier-2026-dlr-ct-phantom]]`) quebra essas premissas, exigindo adaptações metodológicas (como abordagens quase-lineares) para que a TTF e o NPS continuem oferecendo comparabilidade metrológica rigorosa em exames de ultrabaixa dose.
- **Controle de Qualidade e Otimização de Dose:** O relatório fundamenta metodologias avançadas de controle de qualidade para sistemas de varredura automatizados, integrando-se diretamente com estratégias de otimização de dose e controle automático de exposição (`[[Controle Automático de Exposição em TC|controle-automatico-de-exposicao-ct]]`).

---

## 4. Conexões e Wikilinks
- [[Task Based Image Quality|task-based-image-quality]]
- [[Noise Power Spectrum|noise-power-spectrum]]
- [[task-function|TTF (Função de Transferência de Tarefa)]]
- [[Índice de Detectabilidade|indice-de-detectabilidade]]
- [[NPWE Model Observer|npwe-model-observer]]
- [[Channelized Hotelling Observer (CHO)|cho-model-observer]]
- [[Solomon 2016 - Modelos de Observadores em TC|solomon-2016-observer-models]]
- [[Greffier 2026 - Avaliação de DLR em TC com Phantoms|greffier-2026-dlr-ct-phantom]]
- [[Contrast To Noise Ratio|contrast-to-noise-ratio]]
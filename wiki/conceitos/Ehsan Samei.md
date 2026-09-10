---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada\, dosimetria, qualidade-de-imagem, observadores-computacionais, inteligencia-artificial]
data: 2026-08-25
---

# Ehsan Samei

## 1. Definição Conceitual e Fundamentação Física / Metrológica

Ehsan Samei é uma das figuras proeminentes da Física Médica contemporânea, reconhecido internacionalmente por suas contribuições fundamentais à ciência da imagem médica, com ênfase especial em Tomografia Computadorizada (TC), metrologia de radiação, avaliação de qualidade de imagem e integração de métodos de Inteligência Artificial (IA) na prática clínica. 

Academicamente, Samei estabeleceu marcos conceituais na transição da avaliação puramente física e objetiva de sistemas de imagem para abordagens centradas no desempenho do observador — tanto humano quanto computacional. Sua fundamentação metrológica baseia-se na quantificação rigorosa da transferência de sinal e ruído em sistemas de tomografia\, desmembrando o desempenho do sistema em componentes espaciais, temporais e de contraste.

A atuação de Samei abrange a harmonização entre a otimização da dose de radiação ionizante e a preservação (ou melhoria) da diagnosticabilidade clínica. Ele tem sido pioneiro no desenvolvimento de arcabouços para a caracterização de artefatos, na modelagem de sistemas de reconstrução iterativa e, mais recentemente, na validação metrológica de algoritmos de Aprendizado Profundo (*Deep Learning*) aplicados à reconstrução e análise de imagens em TC.

## 2. Formulação Matemática e Propriedades (se aplicável)

O trabalho de Samei na quantificação de desempenho de imagem em TC fundamenta-se em métricas avançadas de caracterização de sistemas lineares e estacionários (LSI), embora sistemas modernos de TC frequentemente violem tais premissas devido a algoritmos não-lineares. As formulações centrais associadas à sua linha de pesquisa incluem a *Task-Based Modulation Transfer Function* (t-MTF) e o *Noise Power Spectrum* (NPS), integrados na avaliação da *Detective Quantum Efficiency* (DQE) dependente da tarefa.

A função de transferência de modulação baseada em tarefas ($\text{t-MTF}$) para um sinal de interesse $s(x,y)$ é descrita em frequências espaciais $(u, v)$ por:

$$
\text{t-MTF}(u, v) = \frac{\left| \mathcal{F} \left\{ \Delta \mu(x,y) \ast \text{PSF}(x,y) \right\} (u, v) \right|}{\left| \mathcal{F} \left\{ \Delta \mu(x,y) \right\} (u, v) \right|}
$$

Onde $\mathcal{F}\{\cdot\}$ denota a transformada de Fourier bidimensional, $\Delta \mu(x,y)$ representa o perfil espacial do objeto de teste ou sinal clínico simulado (como um nódulo pulmonar ou microcalcificação), $\ast$ é o operador de convolução, e $\text{PSF}(x,y)$ é a função de dispersão de ponto (*Point Spread Function*) do sistema de TC.

Complementarmente, o Espectro de Potência do Ruído bidimensional ($\text{NPS}(u,v)$), que caracteriza a textura e a magnitude espacial do ruído na imagem tomográfica, é formulado estatisticamente como:

$$
\text{NPS}(u, v) = \lim_{X, Y \to \infty} \frac{\Delta x \Delta y}{X Y} \left\langle \left| \sum_{x=1}^{X} \sum_{y=1}^{Y} \left[ I(x,y) - \bar{I} \right] e^{-2\pi i (u x + v y)} \right|^2 \right\rangle
$$

Onde $I(x,y)$ representa os valores de pixel na imagem de ruído reconstruída, $\bar{I}$ é a média do sinal, $\Delta x$ e $\Delta y$ são os tamanhos dos pixels, e $\langle \cdot \rangle$ denota o operador de expectativa estatística sobre múltiplos realizações de exames ou varreduras do mesmo fantoma.

Para avaliar a detectabilidade de lesões combinando resolução, ruído e a natureza da tarefa diagnóstica, Samei contribuiu para o avanço do Índice de Detectabilidade ($d'$) do observador ideal, expresso por:

$$
d'^2 = \iint \frac{\left| W(u,v) \cdot \text{t-MTF}(u,v) \right|^2}{\text{NPS}(u,v)} du dv
$$

Onde $W(u,v)$ representa a transformada de Fourier da tarefa de sinal a ser detectada.

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

As metodologias e filosofias científicas associadas a Ehsan Samei impactam profundamente o ecossistema da Tomografia Computadorizada em várias frentes:

*   **Controle de Qualidade Avançado e Fantomas Antropomórficos:** Samei liderou o desenvolvimento de métricas e ferramentas físicas que transcendem os fantomas geométricos tradicionais (como os de água ou acrílico). Ele promoveu o uso de fantomas antropomórficos de alta fidelidade para mimetizar a complexidade anatômica real, permitindo testes que refletem o desempenho clínico genuíno.
*   **Otimização de Dose e Gestão de Risco:** Seu laboratório tem sido instrumental na definição de protocolos de varredura que equilibram a dosimetria de raios X (mensurada por métricas como $CTDI_{vol}$ e $DLP$) com a utilidade diagnóstica, rejeitando o mero reducionismo de dose em favor da preservação da detectabilidade de lesões.
*   **Avaliação de Reconstrução Iterativa (IR) e Aprendizado Profundo (DLR):** Com a introdução de algoritmos não-lineares de reconstrução e redes neurais para redução de ruído e super-resolução em TC, as métricas tradicionais (como ruído global e MTF linear) tornaram-se insuficientes. Samei desempenhou papel central na criação de arcabouços metrológicos baseados em tarefas para avaliar artefatos de textura, perda de resolução dependente do contraste e alucinações em imagens geradas por IA.
*   **Observadores Computacionais:** A implementação de modelos matemáticos que simulam o desempenho de observadores humanos (como o *Channelized Hotelling Observer* - CHO) em tarefas de detecção e discriminação em TC é fortemente enraizada nas pesquisas impulsionadas por seu grupo, viabilizando avaliações de sistemas de imagem céleres, reprodutíveis e correlacionadas com a percepção clínica.

## 4. Conexões e Wikilinks

*   [[Tomografia Computadorizada|Tomografia Computadorizada]]
*   [[Task Transfer Function|MTF]]
*   [[Noise Power Spectrum|NPS]]
*   [[Detective Quantum Efficiency (DQE)]]
*   [[Reconstrução Iterativa|Reconstrução Iterativa]]
*   [[Inteligencia Artificial IA|Inteligência Artificial em Imagem Médica]]
*   [[Dosimetria em Radiologia|Dosimetria em TC]]
*   [[Observadores de Modelo (Model Observers)|Observadores Computacionais]]
*   [[Controle de Qualidade em TC|Controle de Qualidade]]
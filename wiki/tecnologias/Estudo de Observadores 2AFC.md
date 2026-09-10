---tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, avaliacao-de-imagem, observadores-humanos, psicofisica, model-observers, qualidade-de-imagem]
data: 2026-08-25
aliases: [2afc-observer-study, 2afc, 2-afc, "two-alternative forced choice", roc-curve, "Curva ROC", Curva_ROC_Metodologia_DBM, 2afc.md, 2AFC]
---

# 2afc-observer-study

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **2-Alternative Forced-Choice Observer Study** (Estudo de Observador de Dupla Escolha Forçada, comumente abreviado como **2-AFC**) é um método psicofísico rigoroso utilizado na física médica e na engenharia de imagem para avaliar o desempenho de detecção de sinais visuais (lesões, microcalcificações, estruturas anatômicas sutis) em imagens médicas, com ênfase particular na Tomografia Computadorizada (TC). 

Na metodologia 2-AFC, o observador (que pode ser humano ou computacional, como o *Channelized Hotelling Observer* - CHO) é apresentado a duas imagens (ou regiões de interesse - ROIs) distintas e simultâneas (ou sequenciais) em cada tentativa (*trial*). Sabe-se deterministicamente que:
1. Uma das imagens contém o sinal de interesse adicionado a um fundo ruidoso e estocástico ($sinal + fundo$).
2. A outra imagem contém apenas o fundo ruidoso ($somente-fundo$).

A tarefa do observador é forçadamente decidir qual das duas opções (Esquerda ou Direita, 1 ou 2) contém o sinal. O termo "forçada" (*forced-choice*) é crucial: mesmo que o observador esteja totalmente incerto ou que o sinal seja imperceptível, ele deve obrigatoriamente fazer uma escolha, eliminando vieses de critério de decisão (viés conservador ou liberal) que afetam métricas baseadas em taxas de verdadeiro e falso positivo em limiares fixos, como ocorre na Teoria de Detecção de Sinais (SDT) clássica via curvas ROC (*Receiver Operating Characteristic*).

Matematicamente, a probabilidade de acerto em um teste 2-AFC é diretamente relacionada à acurácia do observador e pode ser convertida sem perdas para a área sob a curva ROC ($AUC$) sob premissas paramétricas ou não-paramétricas, fornecendo uma métrica unidimensional robusta, livre de viés de viés de resposta (*response bias*), para quantificar a visibilidade de estruturas em imagens de TC reconstruídas por métodos analíticos (FBP), iterativos (IR) ou baseados em aprendizado profundo (Deep Learning Reconstruction - DLR).

---

## 2. Formulação Matemática e Propriedades

Seja $g_0(\mathbf{r})$ a imagem de fundo estocástica (ruído quântico, textura anatômica) e $s(\mathbf{r})$ o sinal determinístico a ser detectado na posição $\mathbf{r} \in \mathbb{R}^2$ ou $\mathbb{R}^3$. As duas hipóteses apresentadas ao observador em uma tentativa do teste 2-AFC são:

$$
\begin{aligned}
H_1: \quad & f_1(\mathbf{r}) = g_0(\mathbf{r}) + s(\mathbf{r}) \H_0: \quad & f_0(\mathbf{r}) = g_0(\mathbf{r})
\end{aligned}
$$

O observador calcula uma estatística de teste escalar (ou medida de decisão) $\lambda$ para cada imagem, utilizando um operador de observador linear ou não-linear $\mathcal{W}$:

$$
\lambda_1 = \int \mathcal{W}(\mathbf{r}) f_1(\mathbf{r}) \, d\mathbf{r}, \quad \lambda_0 = \int \mathcal{W}(\mathbf{r}) f_0(\mathbf{r}) \, d\mathbf{r}
$$

O observador escolhe a alternativa 1 se $\lambda_1 > \lambda_0$, e a alternativa 0 caso contrário. O acerto ocorre se, e somente se, a imagem contendo o sinal gerar o maior valor da estatística de decisão:

$$
P_{2AFC} = P\left( \lambda_1 > \lambda_0 \right)
$$

Para um observador ideal ou linear operando sob ruído Gaussiano, a diferença entre as variáveis de decisão $\Delta \lambda = \lambda_1 - \lambda_0$ também se distribui normalmente. A relação entre a probabilidade de acerto no 2-AFC ($P_{2AFC}$) e a detectabilidade índice-de-merito $d'$ é dada por:

$$
P_{2AFC} = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\frac{d'}{\sqrt{2}}} e^{-\frac{x^2}{2}} dx = \Phi\left( \frac{d'}{\sqrt{2}} \right)
$$

Onde $\Phi(\cdot)$ é a função cumulativa de distribuição normal padrão. A partir da probabilidade de acerto empírica obtida em $N$ tentativas do teste 2-AFC, o índice de detectabilidade $d'$ é isolado como:

$$
d' = \sqrt{2} \, \Phi^{-1}(P_{2AFC})
$$

Além disso, a equivalência teórica com a Área sob a Curva ROC ($AUC_{ROC}$) para observadores baseados em limiar de decisão sob distribuições Gaussianas é expressa por:

$$
AUC_{ROC} = \Phi\left( \frac{d'}{2} \in \mathbb{R} \right) = \Phi\left( \frac{\Phi^{-1}(P_{2AFC})}{\sqrt{2}} \right)
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Na Tomografia Computadorizada moderna, o estudo 2-AFC desempenha um papel central na **otimização de protocolos de aquisição e reconstrução de imagem**, substituindo gradualmente testes puramente visuais subjetivos (como *Likert scales*) por abordagens quantitativas psicofísicas e metrológicas:

* **Avaliação de Algoritmos de Reconstrução:** Com a proliferação de algoritmos de reconstrução iterativa penalizada (IR) e DLR, as imagens de TC apresentam texturas de ruído não-estacionárias e dependentes da dose. O 2-AFC permite mensurar precisamente se a supressão de ruído agressiva por redes neurais prejudica ou melhora a detectabilidade de lesões de baixo contraste (p.ex., metástases hepáticas ou nódulos pulmonares incipientes).
* **Protocolos de Baixa Dose de Radiação:** Na busca contínua por conformidade com o princípio ALARA (*As Low As Reasonably Achievable*), o 2-AFC é empregado para determinar o limiar mínimo de produto dose-comprimento (DLP) ou corrente do tubo ($mA$) no qual uma lesão de tamanho e contraste específicos permanece estatisticamente detectável.
* **Validação de Observadores Computacionais (*Model Observers*):** Estudos 2-AFC com observadores humanos são extremamente custosos e demorados devido à fadiga visual. Portanto\, dados de estudos 2-AFC humanos servem como padrão-ouro para validar observadores matemáticos (como o CHO ou o *Non-Prewhitening Match Filter with Spatial Frequency Channels* - NPW-CF), permitindo que milhares de avaliações de qualidade de imagem em TC sejam realizadas computacionalmente em segundos.

---

## 4. Conexões e Wikilinks

* [[Task Based Image Quality|task-based-image-quality]]
* [[Observadores de Modelo (Model Observers)|model-observer]]
* [[Channelized Hotelling Observer (CHO)|channelized-hotelling-observer]]
* [[Índice de Detectabilidade|detectability-index]]
* [[Estudo de Observadores 2AFC|roc-curve]]
* [[Retroprojeção Filtrada (FBP)|filtered-back-projection]]
* [[Reconstrução Iterativa|iterative-reconstruction]]
* [[Deep Learning Image Reconstruction (DLR)|deep-learning-reconstruction]]
* [[Noise Power Spectrum|noise-power-spectrum]]
* [[Task Transfer Function|task-transfer-function]]
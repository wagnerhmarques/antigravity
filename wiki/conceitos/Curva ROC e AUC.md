---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, avaliacao-de-desempenho, estatistica, otimizacao]
data: 2026-08-25
---

# curva-roc-e-auc

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A curva **ROC** (*Receiver Operating Characteristic* — Característica de Operação do Receptor) e sua métrica derivada, a **AUC** (*Area Under the Curve* — Área Sob a Curva), constituem a ferramenta padrão-ouro na Física Médica, na Tomografia Computadorizada (TC) quantitativa e em sistemas de Inteligência Artificial para avaliar o desempenho de sistemas de classificação binária e tarefas de detecção de alvos. 

Originalmente desenvolvida no contexto da teoria de detecção de radar durante a Segunda Guerra Mundial, a metodologia ROC foi adaptada para a psicofísica e, posteriormente, para a radiologia diagnóstica e avaliação de observadores (humanos e computacionais/modelos de observadores). Na TC moderna, a curva ROC quantifica a capacidade de um sistema — seja um algoritmo de reconstrução iterativa (IR), deep learning reconstruction (DLR), um protocolo de baixa dose, ou um modelo de IA de detecção de nódulos pulmonares — de discriminar entre um estado de fundo (*background*, ausência de patologia, tecido saudável) e um estado de sinal presente (*signal-present*, presença de lesão, nódulo, microcalcificação ou artefato crítico).

Do ponto de vista metrológico, a curva ROC mapeia o comportamento do classificador sob todos os limiarizações (*thresholds*) de decisão possíveis. Ela plota a taxa de verdadeiros positivos em função da taxa de falsos positivos. A AUC, por sua vez, fornece um escalar único que resume a acurácia diagnóstica global, independentemente do limiar de decisão escolhido, representando probabilisticamente a capacidade do sistema de classificar corretamente um par de instâncias (uma positiva e uma negativa) escolhidas aleatoriamente.

---

## 2. Formulação Matemática e Propriedades

Seja $D$ uma variável de decisão contínua ou ordinal gerada por um algoritmo de IA ou métrica de imagem, e $S \in \{0, 1\}$ o estado binário real da amostra (onde $0$ denota ausência de patologia e $1$ denota presença). Dado um limiar de decisão $\tau$, a decisão do sistema é dada por:

$$
\hat{S} = \begin{cases} 1, & \text{se } D \ge \tau \\ 0, & \text{se } D < \tau \end{cases}
$$

As métricas fundamentais que compõem os eixos da curva ROC são definidas probabilisticamente a partir das funções densidade de probabilidade (FDP) do escore de decisão para o fundo ($f_0(d)$) e para o sinal ($f_1(d)$):

1. **Taxa de Verdadeiros Positivos (TPR - *True Positive Rate*) / Sensibilidade / $1 - \beta$:**

$$
\text{TPR}(\tau) = P(D \ge \tau \mid S = 1) = \int_{\tau}^{\infty} f_1(d) \, dd
$$

2. **Taxa de Falsos Positivos (FPR - *False Positive Rate*) / $1 - \text{Especificidade}$ / $\alpha$:**

$$
\text{FPR}(\tau) = P(D \ge \tau \mid S = 0) = \int_{\tau}^{\infty} f_0(d) \, dd
$$

A curva ROC é o lugar geométrico dos pontos coordenados $\left(\text{FPR}(\tau), \text{TPR}(\tau)\right)$ parametrizados pelo limiar $\tau \in (-\infty, \infty)$.

### Propriedades da AUC (Area Under the Curve)
A métrica AUC quantifica a área sob a curva ROC paramétrica:

$$
\text{AUC} = \int_{0}^{1} \text{TPR}(\text{FPR}^{-1}(p)) \, dp
$$

Estatisticamente, a AUC possui uma interpretação direta e poderosa: ela é exatamente igual à probabilidade de que um classificador atribua um escore maior a um exemplo positivo escolhido aleatoriamente do que a um exemplo negativo escolhido aleatoriamente:

$$
\text{AUC} = P(D_1 > D_0)
$$

Onde $D_1$ é o escore de uma instância com sinal presente e $D_0$ é o escore de uma instância com fundo. 

* **Limites:** $\text{AUC} = 0.5$ indica desempenho equivalente ao acaso (classificador randômico); $\text{AUC} = 1.0$ representa separabilidade perfeita. Valores abaixo de $0.5$ indicam desempenho pior que o acaso (inversão das classes).
* **Invariância:** A AUC é invariante a transformações estritamente monótonas do escore $D$ e é robusta a desbalanceamentos severos de classes na matriz de confusão (embora a forma visual da curva ROC possa ser afetada pelo número absoluto de amostras negativas em altas taxas de FPR).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Na física da Tomografia Computadorizada e na engenharia de imagem diagnóstica, a curva ROC e a AUC são aplicadas em três domínios críticos:

### A. Avaliação de Observadores e Qualidade de Imagem
Tradicionalmente, a qualidade de imagem em TC era avaliada apenas por métricas físicas puras, como a Função de Transferência de Modulação (MTF), o Ruído de Wiener (NPS) e a Relação Contraste-Ruído (CNR). No entanto, essas métricas falham em prever o desempenho diagnóstico real. A metodologia ROC, estendida através de estudos LROC (*Location-ROC*) e FROC (*Free-response ROC*), permite avaliar **Observadores Humanos** (radiologistas) e **Observadores Computacionais** (como o *Channelized Hotelling Observer* - CHO) na tarefa de detecção de lesões de baixo contraste (p.ex., metástases hepáticas sutis ou nódulos pulmonares ground-glass) em imagens ruidosas de baixa dose.

### B. Otimização de Protocolos de Baixa Dose e Filtros de Reconstrução
Ao implementar novas técnicas de varredura (como modulação de corrente de tubo angular e longitudinal) ou algoritmos avançados de reconstrução (IR e DLR), a curva ROC/AUC serve como métrica definitiva de otimização segundo o princípio ALARA. Permite responder à pergunta: *A redução de 50% na dose de radiação compromete a detectabilidade (AUC) de lesões de alto ou baixo contraste?*

### C. Validação de Modelos de Inteligência Artificial (Deep Learning)
Em sistemas de IA para TC (ex.: triagem automática de embolia pulmonar, hemorragia cerebral ou nódulos em exames de tórax), a AUC-ROC é a métrica padrão exigida por agências regulatórias (FDA, ANVISA) para demonstrar a eficácia diagnóstica do algoritmo antes do deployment clínico, complementada frequentemente pela curva Precision-Recall (AUPRC) em cenários de alta prevalência de classes desbalanceadas.

---

## 4. Conexões e Wikilinks

* [[ruido-nps-e-mtf]]
* [[Reconstrução Iterativa|reconstrucao-iterativa-e-dlr]]
* [[otimizacao-de-dose-e-alara]]
* [[Observadores de Modelo (Model Observers)|observadores-computacionais]]
* [[Qualidade de Imagem em TC|qualidade-de-imagem-em-tc]]
---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, mrmc, estatistica, observadores-humanos, avaliacao-de-imagem]
data: 2026-08-25
---

# Analise_Potencia_MRMC_Eixo2

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Análise de Potência Estatística baseada emprojetos Multi-Reader Multi-Case (MRMC)**, no contexto específico do **Eixo 2** de avaliação de desempenho de sistemas de imagem em Tomografia Computadorizada (TC), refere-se à capacidade metodológica e matemática de detectar diferenças estatisticamente significativas na acurácia diagnóstica entre modalidades de imagem concorrentes (por exemplo, comparação entre reconstrução FBP (*Filtered Backprojection*), reconstrução iterativa (IR) e reconstrução baseada em aprendizado profundo (DLR)).

O paradigma MRMC é o padrão-ouro metrológico na avaliação de qualidade de imagem médica voltada para tarefas (*task-based image quality assessment*). Em TC, a variabilidade inerente aos dados clínicos decorre de duas fontes principais e estocásticas:
1. **Variabilidade entre Leitores (Readers):** Diferença de experiência, critérios perceptuais e viéses cognitivos entre os médicos radiologistas que interpretam os exames.
2. **Variabilidade entre Casos (Cases):** Heterocedasticidade anatômica, patológica e de ruído quântico presente nos diferentes pacientes ou manequins escaneados.

A **Análise de Potência** (*Statistical Power Analysis*) no Eixo 2 calcula a probabilidade $1 - \beta$ de rejeitar corretamente a hipótese nula ($H_0$) de que duas técnicas de TC possuem desempenho diagnóstico equivalente, quando, na realidade, existe uma diferença real (hipótese alternativa $H_1$). No Eixo 2, a atenção desloca-se de métricas estritamente físicas (como a Função de Transferência de Modulação - MTF, ou o Ruído de Wiener - NPS) para métricas de desempenho de detecção e classificação baseadas em observadores, sejam eles humanos (clínicos) ou matemáticos (Observadores Computacionais / *Model Observers*).

---

## 2. Formulação Matemática e Propriedades

A formulação analítica e estatística para a potência MRMC baseia-se amplamente na teoria de **ANOVA de Efeitos Aleatórios** desenvolvida por Robert Berbaum, Stephen Metz e colaboradores (notadamente o modelo Dorfman-Berbaum-Metz - DBM, e a extensão de Obuchowski-Rockette - OR).

### O Modelo de Obuchowski-Rockette (OR) para ROC
Seja $X_{ijk}$ a pontuação de decisão (escore de confiança contínuo ou ordinal) dada pelo leitor $j$ ($j = 1, \dots, J$) para o caso $i$ ($i = 1, \dots, I$) sob a modalidade de imagem $k$ ($k = 1, 2$). O modelo estatístico linear para $X_{ijk}$ é dado por:

$$
X_{ijk} = \mu + \au_k + R_j + C_i + (\tau R)_{jk} + (\tau C)_{ik} + (RC)_{ji} + \varepsilon_{ijk}
$$

Onde:
- $\mu$ é a média global dos escores.
- $\au_k$ é o efeito fixo da modalidade de TC ($k$).
- $R_j$ é o efeito aleatório do leitor $j$, com $R_j \sim \mathcal{N}(0, \sigma_R^2)$.
- $C_i$ é o efeito aleatório do caso $i$, com $C_i \sim \mathcal{N}(0, \sigma_C^2)$.
- $(\tau R)_{jk}$ é a interação entre modalidade e leitor ($\sim \mathcal{N}(0, \sigma_{\tau R}^2)$).
- $(\tau C)_{ik}$ é a interação entre modalidade e caso ($\sim \mathcal{N}(0, \sigma_{\tau C}^2)$).
- $(RC)_{ji}$ é a interação entre leitor e caso ($\sim \mathcal{N}(0, \sigma_{RC}^2)$).
- $\varepsilon_{ijk}$ é o erro experimental aleatório intra-observador/intra-caso ($\sim \mathcal{N}(0, \sigma^2_\varepsilon)$).

### Cálculo da Estatística de Teste e Variabilidade
A estatística de teste $F$ para avaliar a diferença entre as modalidades $k=1$ e $k=2$ é construída utilizando a estimativa da Área Sob a Curva ROC ($AUC$, ou $\theta$) para cada combinação de leitor e modalidade. A variância da diferença entre as médias das AUCs ($d = \hat{\theta}_1 - \hat{\theta}_2$) é governada pela matriz de covariância mista que contabiliza as correlações intra-leitor e intra-caso.

A variância estimada da diferença das médias $\hat{\sigma}_d^2$ no método Obuchowski-Rockette é expressa por:

$$
\hat{\sigma}_d^2 = \frac{1}{J} \left( \sigma_{B}^2 + \sigma_{R}^2 + \sigma_{C}^2 + \sigma_{RC}^2 + \sigma_{\tau R}^2 + \sigma_{\tau C}^2 \right)
$$

Onde os componentes específicos de variância mista refletem as correlações intraclasse (ICC). A potência estatística ($1 - \beta$) é calculada através da distribuição $F$ não-central:

$$
1 - \beta = P \left( F_{(1, J-1)} \ge F_{crit} \mid \lambda \right)
$$

Onde $\lambda$ representa o parâmetro de não-centralidade\, diretamente proporcional ao tamanho do efeito esperado ($\Delta = \mu_1 - \mu_2$) ao quadrado, e inversamente proporcional à variância total do erro MRMC:

$$
\lambda = \frac{J \cdot \Delta^2}{2 \hat{\sigma}_d^2}
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

No ciclo de desenvolvimento e controle de qualidade de sistemas de Tomografia Computadorizada, a Análise de Potencia MRMC do Eixo 2 desempenha papéis fundamentais:

* **Otimização de Dose e Redução de Ruído:** Permite determinar se um novo algoritmo de reconstrução baseada em Inteligência Artificial (Deep Learning Reconstruction - DLR) consegue manter ou superar a detectabilidade clínica de lesões de baixo contraste (como metástases hepáticas sutileza ou nódulos pulmonares em vidro fosco) utilizando doses de radiação substancialmente menores ($mA$ ou $mAs$ reduzidos).
* **Dimensionamento Amostral (*Sample Size Determination*):** Antes de realizar estudos clínicos multicêntricos dispendiosos, a análise de potência calcula o número exato de leitores ($J$) e, crucialmente, o número de casos patológicos e normais ($I$) necessários para atingir uma potência estatística adequada (usualmente $1 - \beta \ge 0.80$ ou $0.90$ para um nível de significância $\alpha = 0.05$).
* **Validação de Observadores Computacionais:** Substituição ou suporte aos leitores humanos por observadores baseados em modelo (como o *Hotelling Observer* ou o *Channelized Hotelling Observer* - CHO), cujas matrizes de covariância MRMC podem ser calculadas analiticamente ou via simulações de Monte Carlo estocásticas (*Bootstrap* não-paramétrico de Essex-Claremont).

---

## 4. Conexões e Wikilinks

* [[Qualidade Imagem Baseada Tarefas Eixo2|Qualidade_Imagem_Baseada_Tarefas_Eixo2]]
* [[Channelized Hotelling Observer (CHO)|cho-model-observer]]
* [[Estudo de Observadores 2AFC|Curva_ROC_Metodologia_DBM]]
* [[Reconstrução Iterativa|reconstrucao-iterativa]]
* [[Otimização de Dose em TC|otimizacao-de-dose-em-tc]]
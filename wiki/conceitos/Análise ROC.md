---
tipo: conceito
titulo: "Análise ROC (Receiver Operating Characteristic) em Imagens Médicas"
data_criacao: 2026-08-27
data_atualizacao: 2026-08-27
tags:
  - "teoria-da-decisao"
  - "roc"
  - "detectabilidade"
  - "psicofisica"
---

# Análise ROC (Receiver Operating Characteristic) em Imagens Médicas

## 1. Fundamentos da Teoria de Detecção de Sinais
A **Análise ROC** é o método psicofísico e estatístico rigoroso para avaliar o desempenho de tomadores de decisão (humanos ou [[Observadores de Modelo (Model Observers)|model-observers]]) em tarefas de detecção binária (Sinal Presente $H_1$ vs. Sinal Ausente $H_0$).

A curva ROC plota a **Taxa de Verdadeiros Positivos (Sensibilidade)** contra a **Taxa de Falsos Positivos ($1 - \text{Especificidade}$)** para todos os limiares de decisão $\lambda$:

$$
\text{TPR}(\lambda) = \int_{\lambda}^{\infty} p(z | H_1) \, dz, \quad \text{FPR}(\lambda) = \int_{\lambda}^{\infty} p(z | H_0) \, dz
$$

---

## 2. A Área sob a Curva (AUC) e o Índice de Detectabilidade ($d'$)
Sob a hipótese clássica de distribuições Gaussianas de mesma variância $\sigma^2$:

$$
\text{AUC} = \Phi\left( \frac{d'}{\sqrt{2}} \right)
$$

Onde $\Phi(\cdot)$ é a função de distribuição cumulativa da normal padrão e $d'$ é o [[Índice de Detectabilidade|indice-de-detectabilidade]]:

$$
d' = \sqrt{2} \cdot \Phi^{-1}(\text{AUC})
$$

Em experimentos de escolha forçada bi-alternativa ([[Estudo de Observadores 2AFC|2afc-observer-study]]), a fração de respostas corretas ($P_c$) é identicamente igual à $\text{AUC}$:

$$
P_c = \text{AUC} \implies d' = \sqrt{2} \cdot \Phi^{-1}(P_c)
$$

---

## 3. Conexões no Acervo
- [[Índice de Detectabilidade|indice-de-detectabilidade]]
- [[Estudo de Observadores 2AFC|2afc-observer-study]]
- [[Observadores de Modelo (Model Observers)|model-observers]]
- [[Teoria de Detecção de Sinais|teoria-de-deteccao-de-sinais]]

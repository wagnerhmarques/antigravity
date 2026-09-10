---tipo: conceito
titulo: "Relação Sinal-Ruído e Contraste (CNR e CNRA)"
data_criacao: 2026-08-23
data_atualizacao: 2026-08-23
tags: [cnr, image-quality, metrics, cnn-limitations]
fontes_origem: ["solomon-2016-observer-models"]
aliases: [CNR, "Relação Contraste-Ruído", contrast-to-noise-ratio]
---

# Relação Sinal-Ruído e Contraste (CNR e CNRA)

A **Relação Contraste-Ruído (CNR)** é uma métrica clássica de primeira ordem baseada nos valores numéricos dos pixels de uma imagem.

## Definições

- **CNR Padrão:**
  

$$
CNR = \frac{|C|}{\sigma_b}
$$

  Onde $C$ é o contraste do sinal em Hounsfield Units (HU) e $\sigma_b$ é o desvio padrão dos pixels no fundo.

- **Area-Weighted CNR (CNRA):**
  

$$
CNRA = \frac{|C| \cdot A}{\sigma_b}
$$

  Onde $A$ é a área nominal da inserção/lesão.

## Limitações Críticas em CT Avançada

Conforme demonstrado por [[Solomon 2016 - Modelos de Observadores em TC|solomon-2016-observer-models]]:
1. **Ausência de Especificidade de Tarefa:** O CNR padrão não correlaciona significativamente com a acurácia humana em tarefas de detecção de baixo contraste ($r = 0.36, p > 0.05$).
2. **Insensibilidade à Textura e Resolução:** Reconstruções iterativas como [[ADMIRE (Advanced Modeled Iterative Reconstruction)|admire-reconstruction]] alteram a textura do ruído (espectro de potência do ruído) e a resolução dependente do contraste. O CNR falha em capturar essa alteração, prevendo falsamente ganhos de detectabilidade que não se confirmam em testes com observadores humanos. Recomenda-se o uso de [[Observadores de Modelo (Model Observers)|model-observers]] e o [[Índice de Detectabilidade|detectability-index]].
---
tipo: conceito
titulo: "Índice de Detectabilidade (d')"
data_criacao: 2026-08-25
data_atualizacao: 2026-08-25
tags:
  - detectabilidade
  - observer-model
  - dosimetria
fontes_origem:
  - "[[Greffier 2026 - Avaliação de DLR em TC com Phantoms|greffier-2026-dlr-ct-phantom]]"
---

# Índice de Detectabilidade (d')

O **Índice de Detectabilidade ($d'$)** é uma figura de mérito psicofísica quantitativa que expressa o desempenho de um observador (humano ou modelo matemático) na execução de uma tarefa de detecção visual específica em imagens médicas.

## Formulação e Modelo do Observador

Em avaliações físicas de tomografia computadorizada, o índice $d'$ é frequentemente computado utilizando um modelo de observador *Non-Pre-Whitening with Eye Filter* (NPWE), que simula a sensibilidade do sistema visual humano às diferentes frequências espaciais:

$$
d'^2 = \frac{ \left[ \iint \left| W(u,v) \right|^2 \cdot TTF^2(u,v) \cdot E^2(u,v) \, du \, dv \right]^2 }{ \iint \left| W(u,v) \right|^2 \cdot TTF^2(u,v) \cdot NPS(u,v) \cdot E^2(u,v) \, du \, dv }
$$

Onde:
* $u, v$: Frequências espaciais bidimensionais.
* $W(u,v)$: Função tarefa\, dada pela FFT do sinal do objeto simulado (diferença entre a hipótese de presença e ausência do objeto).
* $TTF(u,v)$: [[Task Based Image Quality|Função de Transferência Baseada em Tarefa]] para o contraste específico.
* $NPS(u,v)$: [[Noise Power Spectrum|Espectro de Potência do Ruído]].
* $E(u,v)$: Filtro ocular que modela a resposta da visão humana.

## Tarefas Clínicas Típicas em Abdômen
* **Tarefa de Baixo Contraste (Sem Contraste):** Lesão focal hepática ou hematoma (ex.: $10\text{ mm}$, contraste de $85\text{ HU}$). Depende criticamente da redução do ruído de baixa frequência.
* **Tarefa de Alto Contraste (Com Contraste):** Estrutura vascular impregnada ou parênquima arterial (ex.: $10\text{ mm}$, contraste de $350\text{ HU}$). Depende primariamente da resolução de borda ($TTF$).

## Impacto Clínico
De acordo com [[Greffier 2026 - Avaliação de DLR em TC com Phantoms|greffier-2026-dlr-ct-phantom]], a reconstrução por [[Deep Learning Image Reconstruction (DLR)|DLR]] proporciona elevações expressivas no valor de $d'$ (com aumentos de até $500\%+$ em dose ultra-baixa de 1,8 mGy), viabilizando diagnósticos precisos com menor exposição à radiação.
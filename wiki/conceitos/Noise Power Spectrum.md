---tipo: conceito
titulo: "Espectro de Potência do Ruído (NPS)"
data_criacao: 2026-08-25
data_atualizacao: 2026-08-25
tags:
  - nps
  - textura-de-ruido
  - fisica-medica
fontes_origem:
  - "[[Greffier 2026 - Avaliação de DLR em TC com Phantoms|greffier-2026-dlr-ct-phantom]]"
aliases: [noise-power-spectrum, espectro-de-potencia-de-ruido-nps, espectro-de-potencia-do-ruido, nps, NPS, "noise power spectrum", "espectro de potência de ruído", "Espectro de Potência de Ruído (NPS)", "Espectro de Potencia do Ruido", "Espectro de Potência de Ruído - NPS", Espectro_Potencia_Ruido_NPS, "Espectro de Potencia do Ruido (NPS)", "Espectro de Potência do Ruído (NPS)", "Noise Power Spectrum (NPS)", espectro_de_potencia_do_ruido_nps]
---

# Espectro de Potência do Ruído (NPS)

O **Espectro de Potência do Ruído** (*Noise Power Spectrum* - NPS) é a métrica fundamental para decompor a variação do ruído em uma imagem radiológica em suas diferentes frequências espaciais. Diferente do desvio padrão simples (que mede apenas a amplitude do ruído em HU), o NPS descreve tanto a **magnitude** quanto a **textura** (granulometria) do ruído.

## Formulação Matemática

O NPS bidimensional ($NPS_{2D}$) em um conjunto de regiões de interesse (ROIs) é calculado pela Transformada Rápida de Fourier (FFT):

$$
NPS_{2D}(f_x, f_y) = \frac{\Delta_x \Delta_y}{L_x L_y} \frac{1}{N_{\text{ROI}}} \sum_{i=1}^{N_{\text{ROI}}} \left| FFT_{2D} \left\{ \text{ROI}_i(x,y) - \text{FIT}_i(x,y) \right\} \right|^2
$$

Onde:
* $\Delta_x, \Delta_y$: Tamanho do pixel nas direções x e y.
* $L_x, L_y$: Dimensões físicas da ROI.
* $\text{FIT}_i(x,y)$: Ajuste polinomial de segunda ordem para remover variações de baixa frequência de fundo (sinal não homogêneo).

## Métricas Derivadas

1. **Magnitude do Ruído (HU):** Calculada como a raiz quadrada da área sob a curva do $NPS_{2D}$. Corresponde ao desvio padrão global da imagem.
2. **Frequência Espacial Média ($f_{av}$):** Medida da textura do ruído no perfil radial $NPS_{1D}$:
   * Valores mais altos de $f_{av}$ indicam ruído com granulometria mais fina.
   * Valores mais baixos de $f_{av}$ indicam ruído de baixa frequência, associado a aspectos visuais indesejados como borramento ou "aspecto plástico" típico da [[Deep Learning Image Reconstruction (DLR)|reconstrução iterativa (IR)]].

## Comportamento no DLR vs IR
Conforme demonstrado por [[Greffier 2026 - Avaliação de DLR em TC com Phantoms|greffier-2026-dlr-ct-phantom]], algoritmos de [[Deep Learning Image Reconstruction (DLR)|DLR]] deslocam a curva do NPS para frequências espaciais mais altas mantendo ou reduzindo dramaticamente a magnitude do ruído, evitando o desvio indesejado para frequências baixas comum aos algoritmos de IR.
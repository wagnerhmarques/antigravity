---
tipo: tecnologia
titulo: "ADMIRE (Advanced Modeled Iterative Reconstruction)"
data_criacao: 2026-08-23
data_atualizacao: 2026-08-23
tags: [iterative-reconstruction, ct-hardware, siemens\, dose-reduction]
fontes_origem: ["solomon-2016-observer-models"]
---

# ADMIRE (Advanced Modeled Iterative Reconstruction)

O **ADMIRE** é um algoritmo de reconstrução iterativa estatística baseada em modelos (*model-based iterative reconstruction*) desenvolvido pela Siemens Healthcare para tomografia computadorizada.

## Características Principais

- **Modelagem Estatística:** Incorpora modelos do feixe de raios X\, da geometria do scanner e estatísticas dos fótons para reduzir o ruído sem causar perda severa de nitidez marginal.
- **Redução de Dose:** Permite manter o desempenho de detectabilidade de baixo contraste com doses substancialmente menores em comparação à retroprojeção filtrada (FBP).
- **Alteração de Textura de Ruído:** Reconstruções avançadas modificam a correlação espacial do ruído. A avaliação objetiva do ADMIRE exige métricas baseadas em [[Observadores de Modelo (Model Observers)|model-observers]] (como [[Observadores de Modelo (Model Observers)|model-observers]] CHOi ou NPWEi), pois métricas tradicionais como [[Contrast To Noise Ratio|contrast-to-noise-ratio]] falham em refletir adequadamente a acurácia de leitura humana.
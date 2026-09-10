---
tipo: fonte
titulo: "Correlation between human detection accuracy and observer model-based image quality metrics in computed tomography"
data_criacao: 2026-08-23
data_atualizacao: 2026-08-23
tags: [low-contrast-detectability, model-observers, ct-image-quality, admire, fbp]
fontes_origem: ["raw/Correlation between human detection accuracy and observer model-based image quality metrics in computed tomography.md"]
---

# Ficha Analítica: Solomon & Samei (2016)

## Visão Geral
Estudo experimental comparando a acurácia de detecção de baixo contraste por leitores humanos (experimento 2AFC com 11 leitores) com métricas substitutas baseadas em [[Observadores de Modelo (Model Observers)|model-observers]] e métricas pixel-a-pixel tradicionais ([[Contrast To Noise Ratio|contrast-to-noise-ratio]]) em tomografia computadorizada (CT).

## Metodologia & Aquisição
- **Equipamento:** CT Siemens SOMATOM Force (Dual-Source de 3ª geração).
- **Phantom:** Fantoma cilíndrico customizado (diâmetro de 165 mm) contendo 45 inserções de baixo contraste (5 níveis de contraste: 5, 9, 12, 15, 20 HU a 120 kVp; 3 tamanhos: 2, 4, 6 mm).
- **Algoritmos de Reconstrução:** Filtered Back Projection (FBP) e [[ADMIRE (Advanced Modeled Iterative Reconstruction)|admire-reconstruction]] (força 3, kernel BF44).
- **Experimento Humano:** 2AFC (Two-Alternative Forced Choice) SKE/BKE (*Signal Known Exactly / Background Known Exactly*) com 11 observadores (6 físicos, 1 residente, 3 doutorandos, 1 radiologista).
- **Métricas Avaliadas:**
  1. Tradicionais: CNR e CNRA (Area-weighted CNR).
  2. [[Observadores de Modelo (Model Observers)|model-observers]] NPW: NPW, NPWE (com filtro de olho), NPWi (com ruído interno), NPWEi (com olho e ruído interno).
  3. [[Observadores de Modelo (Model Observers)|model-observers]] CHO: CHO (60 filtros de Gabor) e CHOi (com ruído interno).

## Principais Resultados Quantitativos

| Métrica | Correl. Pearson ($r$) | Correl. Spearman ($
ho$) | Erro Discriminador ($E$) | Largura$CI_{95\%}$ |
| :--- | :--- | :--- | :--- | :--- |
| **CNR** | 0.36 ($p > 0.05$) | 0.33 | 0.25 | $2.84 \times 10^{-3}$ |
| **CNRA** | 0.83 | 0.84 | 0.15 | $5.29 \times 10^{-3}$ |
| **NPW** | 0.84 | 0.86 | 0.20 | $4.91 \times 10^{-3}$ |
| **NPWE** | 0.86 | 0.88 | 0.25 | $4.55 \times 10^{-3}$ |
| **NPWi** | 0.86 | 0.91 | 0.30 | $2.16 \times 10^{-3}$ |
| **NPWEi** | **0.88** | **0.90** | 0.25 | $1.24 \times 10^{-3}$ |
| **CHO** | 0.85 | 0.89 | 0.40 | $4.58 \times 10^{-2}$ |
| **CHOi** | 0.87 | 0.84 | **0.45** | $7.95 \times 10^{-2}$ |

## Conclusões Fundamentais
1. **Inadequação do CNR Tradicional:** O CNR não apresentou correlação estatisticamente significativa com a performance humana por não ser uma métrica orientada à tarefa (*task-based*).
2. **Família NPW (NPWEi):** Apresentou a maior correlação geral com humanos e intervalos de confiança estreitos com um número razoável de imagens, sendo ideal para otimização em fundos homogêneos.
3. **Família CHO (CHOi):** Caracterizou com máxima fidelidade as diferenças de textura/resolução introduzidas pelo [[ADMIRE (Advanced Modeled Iterative Reconstruction)|admire-reconstruction]] (maior erro discriminador $E = 0.45$), porém exige conjuntos de dados muito maiores devido a amplos intervalos de confiança.
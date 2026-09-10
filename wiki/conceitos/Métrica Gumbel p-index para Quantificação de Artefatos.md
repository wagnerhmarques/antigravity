---
tipo: conceito
titulo: "Métrica Gumbel p-index para Quantificação de Artefatos"
data_criacao: 2026-08-22
data_atualizacao: 2026-08-22
tags: ["image-quality", "artifacts", "gumbel-distribution", "dosimetry"]
fontes_origem: ["dual-filament-3d-printing-ct-phantoms-pasyar-2026"]
---

# Métrica Gumbel p-index para Quantificação de Artefatos

O **p-index baseado na distribuição de Gumbel** (originalmente descrito por Cammin et al.) é uma métrica robusta e independente de ruído utilizada para quantificar a severidade de artefatos de estria em imagens de tomografia computadorizada.

## Funcionamento
- Uma ROI retangular é posicionada sobre um artefato de estria (ex.: tecido mole dorsal aos parafusos espinhais).
- As maiores diferenças absolutas de intensidade de pixels por coluna são extraídas.
- Ajusta-se uma distribuição de Gumbel por regressão linear em um gráfico de probabilidade para estimar o **parâmetro de localização $\mu$**.
- O valor normalizado ($p$-index) compara o ROI com artefato a um ROI de referência sem metal ($0\%$), permitindo comparações diretas e objetivas entre diferentes níveis de inflição metálica e estratégias de [[Redução de Artefatos Metálicos|reducao-de-artefatos-metalicos]].

## Ver Também
- [[Pixelprint]]
- [[Tomografia Computadorizada Espectral|tomografia-computadorizada-espectral]]

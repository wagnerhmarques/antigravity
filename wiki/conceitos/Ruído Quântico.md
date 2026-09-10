---
tipo: conceito
titulo: "Ruído Quântico (Ruído Fotônico em TC)"
data_criacao: 2026-08-27
data_atualizacao: 2026-08-27
tags:
  - "ruido"
  - "estatistica-poisson"
  - "qualidade-de-imagem"
  - "fisica-medica"
---

# Ruído Quântico (Ruído Fotônico em TC)

## 1. Definição e Modelagem Estatística
O **Ruído Quântico** (*Quantum Noise*) é a principal fonte de flutuação estocástica nas imagens de Tomografia Computadorizada. Ele decorre da natureza corpuscular e probabilística da emissão e detecção de fótons de raios X, governada pela **Distribuição de Poisson**.

Para um número médio de fótons $\bar{N}$ detectados em um elemento de detecção:

$$
P(N) = \frac{\bar{N}^N e^{-\bar{N}}}{N!}
$$

A variância do sinal é igual à média: $\sigma_N^2 = \bar{N}$\, de modo que a razão sinal-ruído (SNR) fotônica é dada por:

$$
\text{SNR}_{\text{quantum}} = \frac{\bar{N}}{\sigma_N} = \frac{\bar{N}}{\sqrt{\bar{N}}} = \sqrt{\bar{N}}
$$

Como a dose de radiação ($D$) é diretamente proporcional à fluência fotônica ($\bar{N} \propto D$), a variância do ruído na imagem tomográfica ($\sigma_{\text{imagem}}^2$) é inversamente proporcional à dose:

$$
\sigma_{\text{imagem}} \propto \frac{1}{\sqrt{D}}
$$

---

## 2. Caracterização no Domínio da Frequência
No domínio espacial e de frequências, o ruído quântico é formalmente quantificado pelo **Espectro de Potência de Ruído** ([[Noise Power Spectrum|noise-power-spectrum]]):

$$
\text{NPS}(u, v) = \lim_{N_x, N_y \to \infty} \frac{\Delta x \Delta y}{N_x N_y} \mathbb{E} \left[ \left| \mathcal{F} \left\{ I(x, y) - \mu(x, y) \right\} \right|^2 \right]
$$

Em [[Retroprojeção Filtrada (FBP)|retroproje-o-filtrada]], o filtro de rampa multiplica o ruído quântico proporcionalmente à frequência espacial ($|u|$), conferindo a textura clássica de "ruído azul" (*ramped noise*).

---

## 3. Conexões no Acervo
- [[Noise Power Spectrum|noise-power-spectrum]]
- [[Índice de Detectabilidade|indice-de-detectabilidade]]
- [[Métricas de Dose em TC|metricas-de-dose-tc]]
- [[Deep Learning Image Reconstruction (DLR)|deep-learning-image-reconstruction]]

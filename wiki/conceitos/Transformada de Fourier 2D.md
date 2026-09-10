---
tipo: conceito
titulo: "Transformada de Fourier Bidimensional em Imagens Médicas"
data_criacao: 2026-08-27
tags: ["processamento-sinais", "fourier", "qualidade-de-imagem"]
---

# Transformada de Fourier Bidimensional em Imagens Médicas

## 1. Formulação Contínua e Discreta
A Transformada de Fourier 2D decompõe uma imagem espacial $f(x, y)$ em um espectro de componentes de frequências espaciais $(u, v)$ (medidas em $\text{mm}^{-1}$ ou $\text{ciclos/mm}$):

$$
F(u, v) = \mathcal{F}_{2D}\{f(x, y)\} = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) \exp\left( -j 2\pi (ux + vy) \right) dx \, dy
$$

## 2. Aplicação no Cálculo do NPS e TTF
- **Cálculo do NPS:** O [[Noise Power Spectrum]] é a densidade espectral de potência da variância do ruído, calculada pela média do quadrado da magnitude da DFT 2D de regiões homogêneas subtraídas de sua média:
$$
\text{NPS}(u, v) = \frac{\Delta x \Delta y}{N_x N_y} \langle |\mathcal{F}_{2D}\{\Delta I(x, y)\}|^2 \rangle
$$

## 3. Conexões
- [[Noise Power Spectrum]]
- [[Task Transfer Function]]
- [[Índice de Detectabilidade]]
- [[Teorema da Fatia Central de Fourier]]

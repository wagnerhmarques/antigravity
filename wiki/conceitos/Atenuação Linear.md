---
tipo: conceito
titulo: "Coeficiente de Atenuação Linear e Lei de Beer-Lambert"
data_criacao: 2026-08-27
tags: ["fisica-radiacoes", "atenuacao", "leis-fundamentais"]
---

# Coeficiente de Atenuação Linear e Lei de Beer-Lambert

## 1. Definição Matemática
Para um feixe monoenergético colimado atravessando um meio homogêneo de espessura $x$, a atenuação da intensidade de fótons segue a **Lei de Beer-Lambert**:

$$
I(x) = I_0 \exp(-\mu x)
$$

Onde $\mu$ é o **coeficiente de atenuação linear** ($\text{cm}^{-1}$), que expressa a probabilidade de interação por unidade de comprimento percorrida:

$$
\mu = \mu_{\text{fotoelétrico}} + \mu_{\text{Compton}} + \mu_{\text{Rayleigh}} + \mu_{\text{produção de pares}}
$$

Nas energias diagnósticas ($20 - 140\text{ keV}$), a atenuação é dominada pela soma:

$$
\mu(E) \approx \tau(E, Z) + \sigma_C(E, \rho_e)
$$

## 2. Base da Tomografia Computadorizada
A reconstrução tomográfica reconstrói o mapa bidimensional $\mu(x, y)$ a partir das integrais de linha (projeções do [[Sinograma]]):

$$
p(L) = -\ln\left( \frac{I(L)}{I_0} \right) = \int_{L} \mu(x, y) \, dl
$$

## 3. Conexões
- [[Efeito Fotoelétrico]]
- [[Espalhamento Compton]]
- [[Transformada de Radon]]
- [[Unidades Hounsfield]]

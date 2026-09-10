---
tipo: conceito
aliases: [transformada-de-radon, radon-transform]
---
# Transformada de Radon
A **Transformada de Radon 2D** mapeia a função espacial de atenuação do objeto $\mu(x, y)$ no espaço de projeções lineares $p(\theta, t)$, formando a base matemática para a aquisição tomográfica:

$$
p(\theta, t) = \mathcal{R}\{\mu(x, y)\} = \iint_{-\infty}^{\infty} \mu(x, y) \, \delta(x \cos\theta + y \sin\theta - t) \, dx \, dy
$$

A reconstrução tomográfica analítica inverte esta transformada através do Teorema da Fatia Central e [[Retroprojeção Filtrada (FBP)|Retroprojeção Filtrada (FBP)]].

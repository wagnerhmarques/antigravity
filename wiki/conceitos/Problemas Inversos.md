---
tipo: conceito
aliases: [problemas-inversos, inverse-problems]
---
# Problemas Inversos em Imagem Tomográfica
A reconstrução tomográfica em regimes de baixa dose e contagem limitada de fótons constitui um problema inverso mal-posto (*ill-posed*):

$$
\hat{\mathbf{\mu}} = \arg\min_{\mathbf{\mu}} \left\{ \frac{1}{2} \|\mathbf{A}\mathbf{\mu} - \mathbf{p}\|_{\mathbf{\Sigma}^{-1}}^2 + \lambda \mathcal{R}(\mathbf{\mu}) \right\}
$$

Onde $\mathbf{A}$ é o operador do sistema de projeção e $\mathcal{R}(\mathbf{\mu})$ é o termo regularizador de suavidade ou a priori baseado em redes neurais ([[Deep Learning Image Reconstruction (DLR)|deep-learning-image-reconstruction]]).

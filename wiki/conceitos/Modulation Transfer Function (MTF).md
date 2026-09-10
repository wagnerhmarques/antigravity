---
tipo: conceito
titulo: "Função de Transferência de Modulação (MTF)"
data_criacao: 2026-08-27
data_atualizacao: 2026-08-27
tags:
  - "resolucao-espacial"
  - "mtf"
  - "qualidade-de-imagem"
  - "optica-fourier"
---

# Função de Transferência de Modulação (MTF)

## 1. Definição e Fundamentação Teórica
A **Função de Transferência de Modulação (MTF)** é a métrica padrão-ouro em sistemas lineares e invariantes no espaço (LSI) para caracterizar a **resolução espacial**. Ela expressa a capacidade do sistema de tomografia em reproduzir o contraste de um objeto em função da frequência espacial ($f$).

Matematicamente, a MTF é a magnitude normalizada da Transformada de Fourier bidimensional da [[Point Spread Function (PSF)|point-spread-function]] ($ext{PSF}$):

$$
\text{MTF}(u, v) = \frac{\left| \iint_{-\infty}^{\infty} \text{PSF}(x, y) e^{-i 2\pi (ux + vy)} \, dx \, dy \right|}{\iint_{-\infty}^{\infty} \text{PSF}(x, y) \, dx \, dy}
$$

### Propriedades Fundamentais:
- $\text{MTF}(0) = 1$ (preservação do contraste em frequência zero).
- **Frequências de Corte:** $\text{MTF}_{50\%}$ e $\text{MTF}_{10\%}$ indicam os limites práticos de resolução de alto contraste.

---

## 2. Transição para Sistemas Não-Lineares (TTF)
Em sistemas modernos com [[Reconstrução Iterativa|reconstrucao-iterativa]] e [[Deep Learning Image Reconstruction (DLR)|deep-learning-image-reconstruction]], a resposta em resolução é dependente do contraste do objeto e do nível de ruído, violando a invariância linear da MTF tradicional.
A extensão moderna padronizada pela [[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg233-ct-performance]] é a **Função de Transferência de Tarefa** ([[Task Transfer Function|task-transfer-function]]), medida em insertos de diferentes contrastes.

---

## 3. Conexões no Acervo
- [[Task Transfer Function|task-transfer-function]]
- [[Point Spread Function (PSF)|point-spread-function]]
- [[Índice de Detectabilidade|indice-de-detectabilidade]]
- [[Qualidade de Imagem em TC|qualidade-de-imagem-em-tc]]

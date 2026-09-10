---
tipo: conceito
titulo: "Task Transfer Function (TTF)"
data_criacao: 2026-08-23
data_atualizacao: 2026-08-23
tags: [resolucao-espacial, ttf, aapm-tg-233, nao-linearidade, qualidade-de-imagem]
fontes_origem: ["[[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg-233-summary]]"]
---

# Task Transfer Function (TTF)

## Definição
A **Task Transfer Function (TTF)** é uma extensão da Função de Transferência de Modulação (MTF) tradicional usada para medir a resolução espacial em sistemas de Tomografia Computadorizada (TC) que empregam algoritmos não-lineares, como reconstruções iterativas.

## Contexto e Necessidade
Em sistemas lineares e invariantes no espaço (como a reconstrução por Retroprojeção Filtrada - FBP), a MTF é independente do contraste do objeto e da dose de radiação. No entanto, algoritmos modernos de reconstrução iterativa alteram a resolução espacial dependendo do nível de ruído e do contraste da estrutura examinada.

## Princípios de Funcionamento
- **Dependência do Contraste:** A TTF mede a resposta em frequência espacial para objetos/inserções de diferentes contrastes (ex.: osso vs. tecido mole).
- **Uso em Fantomas:** Medida utilizando phantoms com cilindros de materiais de atenuação conhecida.
- **Aplicação:** É um componente fundamental para o cálculo do [[Índice de Detectabilidade|indice-de-detectabilidade]], refletindo com maior precisão a qualidade de imagem clínica em condições reais de escaneamento.
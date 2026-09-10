---tipo: conceito
titulo: "Reconstrução Iterativa em Tomografia Computadorizada"
data_criacao: 2026-08-23
data_atualizacao: 2026-08-23
tags:
  - "reconstrucao"
  - "algoritmos"
  - "processamento-de-imagem"
fontes_origem:
  - "raw/AAPM Journal  Wiley Online Library.md"
aliases: [reconstrucao-iterativa, "reconstruções iterativas", iterative-reconstruction, ir, IR, "iterative reconstruction", "reconstrução iterativa", "Reconstrucao Iterativa (IR)", "IR - Reconstrução Iterativa", "Reconstrução Iterativa (IR)", "Iterative Reconstruction (IR)", Iterative_Reconstruction_IR, Reconstrucao_Iterativa_em_TC, Reconstrucao_Iterativa_e_DLR, Reconstrucao_Iterativa_e_DLR_TC, "Reconstrução Iterativa e DLR"]
---

## Definição
A **Reconstrução Iterativa (IR)** é uma classe avançada de algoritmos de reconstrução de imagem em tomografia computadorizada que utiliza modelagem estatística e física do sistema para reduzir ruído e artefatos, permitindo a operação com menores níveis de radiação em comparação à retroprojeção filtrada tradicional (FBP).

## Propriedades e Impacto Operacional
Devido à natureza não-linear dos algoritmos de IR, o desempenho de resolução e ruído torna-se dependente do objeto e da dose. Consequentemente, métricas tradicionais como a relação contraste-ruído (CNR) perdem validade, exigindo abordagens baseadas em [[Task Transfer Function|task-transfer-function]] e [[Detectabilidade Index|detectabilidade-index]].

## Ver Também
- [[Modulação de Corrente de Tubo (TCM)|controle-automatico-exposicao]]
- [[Task Transfer Function|task-transfer-function]]
- [[Noise Power Spectrum|noise-power-spectrum]]

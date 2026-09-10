---
tipo: conceito
aliases: [detectabilidade-index, indice-de-detectabilidade, d']
tags: [fisica-medica, tomografia-computadorizada, qualidade-de-imagem, avaliacao-baseada-em-tarefas]
data: 2026-08-25
---

# detectabilidade-index

## 1. Definição Conceitual e Fundamentação Física
O **índice de detectabilidade** ($d'$ ou *detectability index*)\, derivado da Teoria de Detecção de Sinais (SdT) e da Teoria da Decisão Estatística, representa a métrica de ponta para a quantificação da qualidade de imagem em tomografia computadorizada (TC) moderna e em sistemas de imagem médica avançados. Ao contrário das métricas tradicionais baseadas em pixels ou voxels isolados — tais como o Ruído Quadrático Médio (RMS), a Relação Sinal-Ruído (SNR) e a Relação Contraste-Ruído (CNR) —, o índice de detectabilidade modela explicitamente a tarefa clínica ou o desempenho de um observador ideal (matemático ou humano) na detecção ou discriminação de uma estrutura de interesse (lesão, nódulo, artefato ou detalhe anatômico) imersa em um fundo estocástico ruidoso.

No contexto atual da TC, impulsionado por algoritmos complexos de [[Reconstrução Iterativa|reconstrucao-iterativa]] e metodologias de inteligência artificial (como DLR - *Deep Learning Reconstruction*), as métricas convencionais falham. O ruído em imagens reconstruídas por métodos iterativos ou não-lineares deixa de ser estacionário, apresentando texturas e correções espaciais complexas que alteram drasticamente o comportamento do observador. O [[Detectabilidade Index|detectabilidade-index]] resolve essa limitação ao integrar o perfil espacial do sinal da tarefa através da [[Task Transfer Function|task-transfer-function]] (TTF) e a textura do ruído por meio do [[Noise Power Spectrum|noise-power-spectrum]] (NPS), fornecendo uma avaliação objetiva, quantitativa e clinicamente correlacionada da visibilidade de lesões de baixo contraste.

---

## 2. Formulação Matemática e Propriedades
No domínio espacial ou de Fourier, o índice de detectabilidade para uma tarefa de detecção de sinal conhecido em um fundo estocástico homogêneo (Task-Specific $d'$ para um Observador Ideal de Hotelling ou Prewhitening Matched Filter - PWMF) é formalmente definido como:

$$
(d')^2 = \iint_{-\infty}^{\infty} \frac{\left| \text{TTF}(u, v) \cdot W(u, v) \right|^2}{\text{NPS}(u, v)} \, du \, dv
$$

Onde:
- $\text{TTF}(u, v)$ é a [[Task Transfer Function|task-transfer-function]] bivariada (frequências espaciais $u$ e $v$), que descreve a capacidade do sistema de transferir o contraste do objeto de teste ou lesão-alvo em função da frequência espacial.
- $W(u, v)$ representa a transformada de Fourier do perfil tridimensional ou bidimensional do sinal ou tarefa a ser detectada (por exemplo, uma lesão esférica de baixo contraste com diâmetro específico).
- $\text{NPS}(u, v)$ é o [[Noise Power Spectrum|noise-power-spectrum]] bidimensional da imagem reconstruída, caracterizando a magnitude e a distribuição espacial das texturas de ruído.

Para o Observador Ideal com Pré-branqueamento (PWMF), $d'$ estabelece o limite superior matemático de desempenho para qualquer observador (humano ou algoritmo de IA) na execução daquela tarefa específica sob condições ideais de conhecimento do sinal e do ruído. Em variações mais realistas, como o Observador do Canal de Non-Prewhitening (NPWE), filtros adicionais de percepção humana são aplicados para simular a perda de eficiência do observador humano na remoção de ruído correlacionado.

---

## 3. Contexto no Acervo do Pesquisador & Aplicações
O termo **detectabilidade-index** ocupa uma posição central no acervo de notas e diretrizes de pesquisa do laboratório ([[queries/quais são os termos mais frequentes na minha estruturaco aqui no obsidian?.md]]), sendo classificado com prioridade de frequência "Muito Alta" ($\ge 25$ referências cruzadas) devido à sua relevância na transição paradigmática para a **Qualidade de Imagem Baseada em Tarefas**.

As principais conexões mapeadas no acervo incluem:
- **Padronização e Protocolos Avançados:** Conforme documentado em `[[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg233-ct-performance]]`, o relatório AAPG TG-233 estabelece o [[Detectabilidade Index|detectabilidade-index]] em conjunto com a [[Task Transfer Function|task-transfer-function]] como as métricas fundamentais para a avaliação de desempenho de novos sistemas de tomografia, substituindo metodologias legadas obsoletas.
- **Otimização de Dose e Modulação de Corrente:** Em estudos sobre o [[Modulação de Corrente de Tubo (TCM)|controle-automatico-exposicao]] (`[[Modulação de Corrente de Tubo (TCM)|controle-automatico-exposicao]]`), o índice de detectabilidade garante que reduções agressivas de dose — modeladas por funções logarítmicas de atenuação do paciente $\ln(mA) = \alpha(d_w) + \beta$ — não comprometam a detectabilidade clínica de lesões sutis de baixo contraste.
- **Superação de Métricas Legadas em Reconstrução Avançada:** Conforme evidenciado em `[[Reconstrução Iterativa|reconstrucao-iterativa]]`, a quebra de estacionariedade do ruído provocada por métodos iterativos invalida o uso isolado de CNR e SNR. O [[Detectabilidade Index|detectabilidade-index]], alimentado pelo acoplamento entre [[Task Transfer Function|task-transfer-function]] e [[Noise Power Spectrum|noise-power-spectrum]] (`[[Task Transfer Function|task-transfer-function]]`), surge como a ferramenta obrigatória para auditar a fidelidade diagnóstica e evitar alucinações ou perdas de textura em protocolos de baixa dose.

---

## 4. Conexões e Wikilinks
- [[Índice de Detectabilidade|indice-de-detectabilidade]]
- [[Task Transfer Function|task-transfer-function]]
- [[Noise Power Spectrum|noise-power-spectrum]]
- [[Reconstrução Iterativa|reconstrucao-iterativa]]
- [[Modulação de Corrente de Tubo (TCM)|controle-automatico-exposicao]]
- `[[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg233-ct-performance]]`
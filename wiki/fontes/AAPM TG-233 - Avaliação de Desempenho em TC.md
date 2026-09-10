---tipo: fonte
titulo: "Comprehensive Assessment of CT Performance: AAPM Task Group 233 Report"
autores:
  - "[[Ehsan Samei]]"
  - "[[Donovan Bakalyar]]"
  - "[[Kirsten L Boedeker|Kirsten L. Boedeker]]"
  - "[[Samuel Brady]]"
  - "[[Jiahua Fan]]"
  - "[[Shuai Leng]]"
  - "[[Kyle J. Myers]]"
  - "[[Lucretiu M Popescu|Lucretiu M. Popescu]]"
  - "[[Juan Carlos Ramirez Giraldo]]"
  - "[[Frank Ranallo]]"
  - "[[Justin Solomon]]"
  - "[[Jay Vaishnav]]"
  - "[[Jia Wang]]"
veiculo: "AAPM Journal / Wiley Online Library"
data_criacao: 2026-08-23
data_atualizacao: 2026-08-23
tags:
  - "dosimetria"
  - "tomografia-computadorizada"
  - "física-médica"
  - "otimização"
  - "tg233"
fontes_origem:
  - "raw/AAPM Journal  Wiley Online Library.md"
aliases: [aapm-tg233-ct-performance, aapm-tg-233-summary, "aapm tg 233", tg233, TG-233, aapm-tg-233]
---

## Resumo Executivo
O relatório do **AAPM Task Group 233 (TG233)** estabelece novas diretrizes metodológicas para a avaliação de desempenho de sistemas de tomografia computadorizada (TC), com ênfase no desempenho operacional clínico. Em virtude do avanço tecnológico de algoritmos avançados como [[Reconstrução Iterativa|reconstrucao-iterativa]] (IR) e controle automático de exposição ([[Modulação de Corrente de Tubo (TCM)|controle-automatico-exposicao]] / TCM), as métricas tradicionais de qualidade de imagem tornaram-se insuficientes. O documento detalha abordagens quantitativas para mensuração de ruído, resolução espacial baseada em tarefas ([[Task Transfer Function|task-transfer-function]])\, desempenho de modulação de corrente, e métricas baseadas em tarefas ([[Detectabilidade Index|detectabilidade-index]]). 

## Principais Achados & Dados Quantitativos
- **Modulação de Corrente (TCM):** Introduz testes de adaptação discreta e contínua do produto corrente-tempo ($mAs$) em função do diâmetro equivalente de água ($d_w$), correlacionando $\ln(mA) = \alpha(d_w) + \beta$.
- **Resolução Espacial:** Superação da MTF tradicional pela [[Task Transfer Function|task-transfer-function]] ($TTF_{n,C}$ e $zTTF_{n,C}$), quantificando a resolução em condições de ruído e contraste específicos para sistemas não-lineares.
- **Textura e Ruído:** Utilização do [[Noise Power Spectrum|noise-power-spectrum]] (NPS), índice de não-uniformidade de ruído (NUI) e índice de in-homogeneidade ($\eta$).
- **Desempenho Baseado em Tarefas:** Emprego do índice de detectabilidade ($d'$) baseado no filtro adaptado não-preparador (NPW) e métricas de domínio espacial como LROC e EFROC.

## Contexto Científico e Implicações
A transição de avaliações baseadas estritamente em especificações de aceitação para o *commissioning* operacional e otimização clínica permite a equalização de qualidade de imagem entre diferentes fabricantes e a validação quantitativa de potenciais reduções de dose.

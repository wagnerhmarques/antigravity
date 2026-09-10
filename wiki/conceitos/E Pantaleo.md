---
tipo: conceito
aliases: [E. Pantaleo]
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, revisao-bibliografica]
data: 2026-08-25
---

# E. Pantaleo

## 1. Definição Conceitual e Fundamentação Física
**E. Pantaleo** é um pesquisador e autor ativo no domínio da Física Médica e da Inteligência Artificial aplicada, com contribuições notáveis voltadas para a análise de dados complexos, aprendizado de máquina (*machine learning*) e modelagem estatística em sistemas de imagem e radioterapia. Na literatura recente indexada no acervo do laboratório (USP/FAPESP), seu trabalho figura em revisões abrangentes sobre o impacto disruptivo da inteligência artificial na física médica, abordando desde a otimização de fluxos de trabalho em Tomografia Computadorizada (TC) até a radiômica e a dosimetria computacional avançada.

## 2. Formulação Matemática e Propriedades
Embora o termo refira-se nominalmente a um pesquisador e não a uma equação isolada, o contexto analítico de suas publicações envolve a formulação de algoritmos baseados em aprendizado profundo (*deep learning*) e redes neurais para reconstrução e análise de imagens médicas. No formalismo de otimização de redes neurais convolucionais (CNNs) frequentemente revisado em seus trabalhos, a função de perda (*loss function*) para tarefas de segmentação ou reconstrução em TC pode ser representada por:

$$
\mathcal{L}_{\text{total}}(\theta) = \frac{1}{N} \sum_{i=1}^{N} \left\| f_{\theta}(x_i) - y_i \right\|_2^2 + \lambda \R(\theta)
$$

Onde:
- $x_i$ representa o volume de Tomografia Computadorizada de entrada (por exemplo, imagens com ruído quântico elevado ou baixa dose).
- $y_i$ denota a imagem de referência de alta qualidade (*ground truth*).
- $f_{\theta}$ é o operador não linear parametrizado pelos pesos $\theta$ da rede neural desenvolvida ou analisada pelo grupo de pesquisa.
- $R(\theta)$ representa o termo de regularização para evitar o sobreajuste (*overfitting*) no espaço de parâmetros de alta dimensionalidade.

## 3. Contexto no Acervo do Pesquisador & Aplicações
As ocorrências de **E. Pantaleo** no acervo da LLM Wiki de Física Médica & Tomografia Computadorizada estão estritamente vinculadas à produção bibliográfica recente sobre o estado da arte da inteligência artificial na área. O autor é coautor do artigo de revisão publicado em *La Rivista del Nuovo Cimento* (2025), indexado nos seguintes documentos do acervo:
- [[Inteligência Artificial em Física Médica (Nuovo Cimento)|artificial-intelligence-in-medical-physics-nuovo-cimento]]
- [[Inteligência Artificial em Física Médica (Nuovo Cimento)|artificial-intelligence-in-medical-physics-nuovo-cimento]]

Nesse contexto, as contribuições associadas a Pantaleo coadunam-se com a discussão sobre o controle de qualidade automatizado, a redução de dose em exames de Tomografia Computadorizada via reconstrução baseada em aprendizado profundo (*Deep Learning Reconstruction - DLR*), e a melhoria na detectabilidade de lesões em ambientes clínicos complexos.

## 4. Conexões e Wikilinks
- [[N Amoroso|N. Amoroso]]
- [[R Errico|R. Errico]]
- [[A Monaco|A. Monaco]]
- [[R Bellotti|R. Bellotti]]
- [[Inteligência Artificial em Física Médica (Nuovo Cimento)|artificial-intelligence-in-medical-physics-nuovo-cimento]]
- [[Inteligência Artificial em Física Médica (Nuovo Cimento)|artificial-intelligence-in-medical-physics-nuovo-cimento]]
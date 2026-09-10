---
tipo: conceito
aliases: [R. Bellotti]
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, aprendizado-de-maquina]
data: 2026-08-25
---

# R. Bellotti

## 1. Definição Conceitual e Fundamentação Física
**R. Bellotti** é um pesquisador proeminente na interface entre a Física Médica, a Inteligência Artificial (IA) e o aprendizado de máquina (*machine learning*), com contribuições significativas para a análise de dados complexos em imageamento médico e dosimetria. No contexto do acervo da LLM Wiki de Física Médica & Tomografia Computadorizada (USP/FAPESP), seu trabalho reflete-se na investigação de como algoritmos avançados de aprendizado profundo (*deep learning*) e redes neurais artificiais modelam e transformam o fluxo de trabalho clínico\, desde a otimização de protocolos de aquisição em Tomografia Computadorizada (TC) até a reconstrução de imagens de baixa dose e o suporte à decisão clínica baseada en radiômica.

As pesquisas associadas ao seu nome abordam a transição de métodos analíticos tradicionais (como a Retroprojeção Filtrada - FBP) para abordagens orientadas por dados, explorando a compactação de espaço de características de alta dimensão e a mitigação de artefatos em imagens médicas complexas.

## 2. Formulação Matemática e Propriedades
No âmbito dos modelos de Inteligência Artificial aplicados à Física Médica associados às publicações do grupo de Bellotti, o mapeamento entre o espaço de projeções degradadas ou de baixa dose $\mathbf{y}$ e a imagem reconstruída de alta qualidade $\mathbf{x}$ pode ser formulado através de um problema de otimização convexa regularizada ou por meio de redes generativas adversariais (GANs) e redes neurais profundas:

$$
\hat{\mathbf{x}} = \arg\min_{\mathbf{x}} \left\{ \mathcal{L}_{\text{data}}(\mathbf{A}\mathbf{x}, \mathbf{y}) + \lambda \mathcal{R}(\mathbf{x}) \right\}
$$

Onde:
- $\mathbf{A}$ representa o operador do sistema físico de aquisição (matriz de projeção em Tomografia Computadorizada).
- $\mathcal{L}_{\text{data}}$ é a função de perda baseada no domínio de dados (como a divergência estatística de Poisson para fótons de raio-X).
- $\mathcal{R}(\mathbf{x})$ é o termo de regularização (aprendido via redes neurais profundas) que impõe prioridades estruturais anatômicas.
- $\lambda > 0$ é o hiperparâmetro de regularização que equilibra a fidelidade dos dados e a suavização/restauração da imagem.

Alternativamente, em abordagens baseadas em aprendizado de representação profunda investigadas em coautoria, a extração de características latentes $\mathbf{z}$ de uma imagem médica tridimensional $I(\mathbf{r})$ é parametrizada por uma rede neural com pesos $\boldsymbol{\theta}$:

$$
\mathbf{z} = f_{\boldsymbol{\theta}}\left( I(\mathbf{r}) \right), \quad \mathbf{r} \in \Omega \subset \mathbb{R}^3
$$

## 3. Contexto no Acervo do Pesquisador & Aplicações
O nome de **R. Bellotti** aparece diretamente vinculado ao ecossistema de revisão e prospecção tecnológica sobre IA na física médica, conforme evidenciado no documento [[Inteligência Artificial em Física Médica (Nuovo Cimento)|artificial-intelligence-in-medical-physics-nuovo-cimento]] e na nota de origem [[Inteligência Artificial em Física Médica (Nuovo Cimento)|artificial-intelligence-in-medical-physics-nuovo-cimento]]. 

Suas contribuições editoriais e científicas em coautoria com pesquisadores como [[N Amoroso|N. Amoroso]], [[R Errico|R. Errico]], [[E Pantaleo|E. Pantaleo]] e [[A Monaco|A. Monaco]] contextualizam o estado da arte da IA em domínios críticos da física médica, tais como:
- **Redução de Dose em Tomografia Computadorizada:** Aplicação de algoritmos de reconstrução profunda (DLR - *Deep Learning Reconstruction*) para preservar a detectabilidade de lesões de baixo contraste mesmo sob correntes de tubo reduzidas ($mA$).
- **Radiômica e Caracterização de Tecidos:** Uso de frameworks baseados em aprendizado de máquina para extração quantitativa de biomarcadores de imagem, melhorando a acurácia na avaliação de artefatos e na segmentação de volumes de interesse.
- **Controle de Qualidade Automatizado:** Monitoramento do desempenho de scanners de TC e verificação de parâmetros fantoma por meio de redes neurais convolucionais (CNNs).

## 4. Conexões e Wikilinks
- [[N Amoroso|N. Amoroso]]
- [[R Errico|R. Errico]]
- [[E Pantaleo|E. Pantaleo]]
- [[A Monaco|A. Monaco]]
- [[Inteligência Artificial em Física Médica (Nuovo Cimento)|artificial-intelligence-in-medical-physics-nuovo-cimento]]
- [[Inteligência Artificial em Física Médica (Nuovo Cimento)|artificial-intelligence-in-medical-physics-nuovo-cimento]]
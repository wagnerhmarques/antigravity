---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, reconstrucao-de-imagem, reducao-de-dose, aprendizado-profundo]
data: 2026-08-25
---

# Jiahua Fan

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O Prof. Dr. Jiahua Fan é uma figura proeminente e pesquisador de destaque nas interseções da Física Médica, Engenharia Biomédica, processamento avançado de imagem digital e Inteligência Artificial (IA), com contribuições fundamentais direcionadas à otimização de sistemas de Tomografia Computadorizada (TC). O seu corpo de trabalho acadêmico concentra-se fortemente no desenvolvimento de metodologias computacionais para reconstrução de imagens, redução de ruído quântico e eletrônico, correção de artefatos (como endurecimento de feixe e artefatos metálicos) e minimização da dose de radiação ionizante sem comprometer a acurácia diagnóstica quantitativa.

No contexto metrológico da imagem médica, a pesquisa associada ao escopo de atuação de Jiahua Fan aborda o desafio inerente ao balanço de Pareto entre a dose absorvida pelo paciente ($D$), a resolução espacial ($R$) e a razão sinal-ruído (SNR). À medida que a indústria e a pesquisa avançam rumo a protocolos de baixa dose — cruciais na mitigação de riscos estocásticos induzidos por radiação (principalmente câncer radioinduzido) —, os métodos analíticos tradicionais, como a Retroprojeção Filtrada (FBP, *Filtered Backprojection*), tornam-se altamente limitados devido à ampliação severa do ruído de Poisson e de feixes estocásticos. 

As inovações metodológicas atribuídas a Jiahua Fan e sua equipe acadêmica estruturam-se na aplicação de abordagens avançadas de modelagem estatística, otimização convexa e, mais recentemente, aprendizado profundo (*Deep Learning* - DL), permitindo a transição de algoritmos puramente determinísticos para reconstrutores orientados por dados (*data-driven*) e aprendizado de representação latente.

---

## 2. Formulação Matemática e Propriedades

Para compreender o impacto das formulações computacionais frequentemente estudadas e otimizadas no ecossistema de pesquisa de Jiahua Fan, considere o problema linear discreto da aquisição de dados em Tomografia Computadorizada:

$$
\mathbf{y} = \mathcal{A}\mathbf{x} + \mathbf{e}
$$

Onde:
- $\mathbf{x} \in \mathbb{R}^{N}$ representa a imagem de atenuação linear desconhecida (voxelizada).
- $\mathbf{y} \in \mathbb{R}^{M}$ vetor que denota os dados de projeção medidos (sinograma), transformados pelo logaritmo negative da intensidade detectada.
- $\mathcal{A}: \mathbb{R}^{N} \o \mathbb{R}^{M}$ é a matriz do sistema de projeção geométrica (operador de Radon discretizado).
- $\mathbf{e}$ representa o ruído estatístico combinando flutuações quânticas (distribuição de Poisson) e ruído eletrônico gaussiano.

Em cenários de baixa dose, a inversão direta ou o uso de FBP resulta em instabilidade severa. Os arcabouços de otimização regularizada frequentemente investigados nesses contextos formulam o problema de reconstrução como um problema de minimização de custo penalizado:

$$
\hat{\mathbf{x}} = \arg\min_{\mathbf{x} \ge 0} \left( \frac{1}{2} \|\mathbf{y} - \mathcal{A}\mathbf{x}\|_{\mathbf{W}}^2 + \lambda \mathcal{R}(\mathbf{x}) \right)
$$

Onde:
- $\|\cdot\|_{\mathbf{W}}^2$ denota a norma ponderada estatisticamente de acordo com a variância do ruído de fótons ($W_{ii} = \bar{I}_i$).
- $\mathcal{R}(\mathbf{x})$ é o termo de regularização ou prior estocástico/espacial (como variação total - *Total Variation*, ou penalizações baseadas em dicionários e redes neurais profundas).
- $\lambda > 0$ é o hiperparâmetro de regularização que controla o equilíbrio entre a fidelidade aos dados (*data fidelity*) e a suavização estrutural.

Nas formulações avançadas baseadas em Inteligência Artificial e aprendizado profundo (muitas vezes empregadas para pós-processamento ou correções no domínio dos sinogramas e das imagens), a função de mapeamento não linear $\mathcal{F}_{\Theta}$ parametrizada pelos pesos $\Theta$ da rede neural profunda é otimizada para minimizar uma função de perda (*loss function*) avançada, combinando o erro absoluto médio (MAE) ou erro quadrático médio (MSE) com perdas perceptuais e adversarial (*GANs*):

$$
\mathcal{L}(\Theta) = \frac{1}{K} \sum_{k=1}^{K} \left\| \mathcal{F}_{\Theta}(\tilde{\mathbf{x}}_k) - \mathbf{x}_k^{\text{ref}} \right\|_p^p + \mu \mathcal{L}_{\text{GAN}}(\Theta)
$$

Onde $\tilde{\mathbf{x}}_k$ é a imagem corrompida por ruído de baixa dose, $\mathbf{x}_k^{\text{ref}}$ é a imagem de referência de alta dose (*ground truth*), e $\mu$ pondera a estabilização gerativa.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

As contribuições científicas ligadas ao perfil de Jiahua Fan possuem aplicações diretas e críticas na prática clínica e na pesquisa de ponta em Tomografia Computadorizada:

1. **Reconstrução Iterativa Penalizada (PIR) e Aprendizado Profundo (DLR):** Otimização de algoritmos capazes de preservar bordas anatômicas finas (como trabéculas ósseas e microvasculatura pulmonar) enquanto removem artefatos de granulação decorrentes de varreduras ultrabaixas em exames pediátricos e cardiológicos.
2. **Mitigação de Artefatos Geométricos e Metálicos:** Desenvolvimento de métodos computacionais robustos para a interpolação e preenchimento de dados em falta em sinogramas corrompidos por próteses ortopédicas ou clipes cirúrgicos, reduzindo o *beam-hardening* secundário e o sombreamento por endurecimento de feixe.
3. **Radiômica e Extração de Biomarcadores Quantitativos:** Garantir que a aplicação de algoritmos avançados de IA e filtragem não altere as texturas estatísticas de 1ª e 2ª ordem essenciais para análises radiômicas e oncômicas preditivas, mantendo a reprodutibilidade metrológica dos valores de número CT (Unidades Hounsfield - UH).
4. **Dosimetria Computacional e Otimização de Protocolos:** Suporte ao desenvolvimento de ferramentas de simulação baseadas em Monte Carlo e modelos fantomas virtuais para mapeamento rigoroso da dose orgânica em função de novos paradigmas de varredura espiral e helicoidal.

---

## 4. Conexões e Wikilinks

- [[Reconstrução Iterativa|Reconstrucao Iterativa]]
- [[Deep Learning Image Reconstruction (DLR)|deep-learning-image-reconstruction]]
- [[Retroprojeção Filtrada (FBP)|FBP]]
- [[Reducao de Dose em Tomografia Computadorizada]]
- [[Artefatos em Tomografia Computadorizada]]
- [[Radiomica]]
- [[Qualidade de Imagem em Tomografia Computadorizada]]
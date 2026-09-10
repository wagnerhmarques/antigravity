---
tipo: conceito
aliases: [ttf-task-transfer-function, task-transfer-function, ttf, TTF, funcao-de-transferencia-de-tarefa, "função de transferência da tarefa", "task transfer function", "Função de Transferência de Modulação - FTM", "Função de Transferência de Modulação (MTF)", Funcao_de_Transferencia_Modulada_MTF, "Modulação da Função de Transferência (MTF)", Modulation_Transfer_Function_MTF, "MTF (Modulation Transfer Function)", MTF, funcao_de_transferencia_de_modulacao, FTM]
tags: [fisica-medica, tomografia-computadorizada, resolucao-espacial, aapm-tg233]
data: 2026-08-25
---

# task-transfer-function

## 1. Definição Conceitual e Fundamentação Física
A **Task Transfer Function (TTF)** — ou Função de Transferência de Tarefa — é uma métrica avançada de avaliação de desempenho de sistemas de imagem em Tomografia Computadorizada (TC), introduzida e formalizada de maneira robusta em protocolos modernos como o **AAPM TG-233**. Historicamente, a resolução espacial em TC era avaliada pela Função de Transferência de Modulação (MTF) linear tradicional, tipicamente medida por meio de fios finos ou bordas afiadas em condições altamente idealizadas e de baixo ruído. No entanto, os sistemas modernos de TC empregam algoritmos de reconstrução altamente não-lineares, espaciais e dependentes da dose — como a Reconstrução Iterativa Avançada (AIR) e a Reconstrução de Imagem por Aprendizado Profundo (DLIR) —, invalidando a premissa de linearidade e a aplicabilidade direta da MTF clássica.

A TTF resolve essa limitação ao estender o conceito de resposta de frequência para cenários **task-specific** (dependentes da tarefa) e não-lineares. Ela quantifica a capacidade do sistema de reproduzir o contraste de um objeto de teste em função da frequência espacial, levando em conta o contraste local do fundo, o nível de dose e a geometria da estrutura anatômica simulada. Em essência, a TTF mede a degradação da amplitude de um sinal sinusoidal de teste quando processado por todo o pipeline de aquisição e reconstrução, permitindo prever o comportamento do sistema diante de tarefas clínicas reais (como a detecção de nódulos pulmonares de baixo contraste ou lesões hepáticas).

---

## 2. Formulação Matemática e Propriedades

A determinação da TTF é comumente realizada através da análise de bordas (por exemplo, utilizando esferas ou cilindros uniformes de alto ou baixo contraste imersos em um fundo homogêneo, conforme as diretrizes do AAPM TG-233) ou por métodos baseados em objetos circulares. 

A partir de uma imagem de teste contendo uma interface de transição (borda), obtém-se o Perfil de Borda Edge Profile ($EP$). O primeiro passo consiste em derivar o perfil para obter a *Edge Spread Function* generalizada modificada para tarefas específicas, ou calcular diretamente a Transformada de Fourier da derivada do perfil de borda suavizado ($LSF_{task}$):

$$
LSF_{task}(x) = \frac{d}{dx} \left[ \overline{I}(x) \right]
$$

Onde $\overline{I}(x)$ representa o perfil de intensidade averaged (médio) extraído radialmente da estrutura de teste para mitigar os efeitos do ruído quântico local.

A **Task Transfer Function** normalizada no domínio da frequência espacial bi-dimensional ou radial ($u$) é definida como o módulo da Transformada de Fourier da $LSF_{task}$, normalizada pela sua amplitude na frequência zero ($u = 0$):

$$
TTF(u) = \left| \frac{\mathcal{F} \left\{ LSF_{task}(x) \right\}}{\mathcal{F} \left\{ LSF_{task}(x) \right\}_{u=0}} \right| = \left| \frac{\int_{-\infty}^{\infty} LSF_{task}(x) e^{-j 2 \pi u x} dx}{\int_{-\infty}^{\infty} LSF_{task}(x) dx} \right|
$$

Em sistemas não-lineares, propriedades fundamentais da MTF linear tradicional — como a aditividade e a estipulação estrita de invariância espacial — deixam de valer. Consequentemente, a TTF torna-se dependente de:
1. **Contraste de Fundo ($\Delta C$):** A magnitude do contraste entre o objeto de interesse e o meio envolvente.
2. **Nível de Dose / Ruído ($\sigma^2$):** Devido à supressão de ruído dependente do sinal comum em algoritmos de Inteligência Artificial e Reconstrução Iterativa.
3. **Frequência Espacial ($u, v$):** Avaliada frequentemente em coordenadas polares ou cartesianas para capturar anisotropias na resolução espacial causadas por matrizes de reconstrução e filtros de pós-processamento.

---

## 3. Contexto no Acervo do Pesquisador & Aplicações

No escopo dos projetos de doutorado, investigações em imageamento médico e desenvolvimento de observadores computacionais vinculados à USP/FAPESP, a **task-transfer-function** desempenha um papel central na caracterização física e na otimização de protocolos avançados de tomografia computadorizada. Conforme evidenciado no acervo de notas do pesquisador:

* **Integração com Phantoms Híbridos e Antropomórficos:** Conforme abordado em `queries/o que o projeto de doutorado complementa o projeto AIR e o universal CNPQ?.md` e `queries/O que são phantoms ?.md`, a aferição da TTF deixa de ser feita apenas em phantoms cilíndricos padronizados e passa a ser acoplada a [[Phantoms Híbridos|phantoms-hibridos]] antropomórficos e simulações numéricas para mimetizar condições clínicas reais.
* **Automação de Processos:** No documento `queries/Como devo começar a estruturar o observador profundo, por onde começo?.md`\, destaca-se a necessidade de automação computacional da extração da $TTF(u,v)$ via métodos de borda circular, viabilizando a mensuração em larga escala da resolução espacial em ambientes de pesquisa.
* **Reprodutibilidade Estatística:** A robustez metodológica exige rigor metrológico. O documento `queries/Qual é o estado da arte das tecnologias...` estipula que os cálculos de `[[Noise Power Spectrum|noise-power-spectrum]]` (NPS) e `[[Task Transfer Function|task-transfer-function]]` (TTF) devem atingir níveis elevados de reprodutibilidade intraclasse ($\text{ICC} \ge 0{,}90$).
* **Avaliação de Desempenho e Detectabilidade:** A TTF atua em conjunto com o [[Noise Power Spectrum|espectro-de-potencia-de-ruido-nps]] como uma das entradas fundamentais para o cálculo do [[Índice de Detectabilidade|detectability-index]] ($d'$), permitindo modelar o desempenho de observadores humanos e computacionais ([[Deep Learning Model Observer|deep-learning-model-observer]]) em imagens geradas por algoritmos de reconstrução como [[ADMIRE (Advanced Modeled Iterative Reconstruction)|admire-reconstruction]] e [[Deep Learning Image Reconstruction (DLR)|deep-learning-image-reconstruction]], conforme discutido em `queries/Comente sobre a evolução dos modelos de observadores computacionais...` e `queries/O que é ttf e porque ele é importante?.md`.

---

## 4. Conexões e Wikilinks
- [[Noise Power Spectrum|espectro-de-potencia-de-ruido-nps]]
- [[Índice de Detectabilidade|detectability-index]]
- [[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg-233-sum]]
- [[Phantoms Híbridos|phantoms-hibridos]]
- [[Deep Learning Model Observer|deep-learning-model-observer]]
- [[Deep Learning Image Reconstruction (DLR)|deep-learning-image-reconstruction]]
- [[ADMIRE (Advanced Modeled Iterative Reconstruction)|admire-reconstruction]]
- [[Teoria de Detecção de Sinais|teoria-de-deteccao-de-sinais]]
---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, otimizacao, multiobjetivo\, dosimetria, reconstrucao-de-imagem]
data: 2026-08-25
---

# nsga-ii

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **NSGA-II** (*Non-dominated Sorting Genetic Algorithm II*)\, desenvolvido por Kalyanmoy Deb et al. em 2002, é um algoritmo genético de otimização multiobjetivo baseado em elitismo de ponta. Na Física Médica e na Tomografia Computadorizada (TC), problemas de tomada de decisão frequentemente envolvem a otimização simultânea e conflitante de múltiplos objetivos métricos, como a maximização da qualidade de imagem (quantificada pela resolução espacial e supressão de ruído/artefatos) e a minimização da dose de radiação absorvida pelo paciente (dose efetiva ou dose glandular média).

A fundamentação metodológica do NSGA-II reside na capacidade de encontrar um conjunto de soluções de compromisso conhecidas como **Fronteira de Pareto** (*Pareto Optimal Front*), em vez de convergir para uma única solução ótima ponderada. Uma solução é considerada não-dominada se não puder ser melhorada em nenhum dos objetivos sem degradação em pelo menos um dos outros. O algoritmo opera através de três inovações principais em relação à sua primeira versão (NSGA):
1. **Complexidade computacional reduzida** por meio de um algoritmo de ordenação não-dominada rápido $O(M N^2)$, onde $M$ é o número de objetivos e $N$ o tamanho da população.
2. **Esquema de elitismo explícito**, que preserva as melhores soluções encontradas ao longo das gerações combinando a população atual com a descendente antes da seleção.
3. **Operador de distância de multidão** (*Crowding Distance*), que garante a diversidade das soluções ao longo da Fronteira de Pareto sem a necessidade de parâmetros artificiais como o raio de compartilhamento (*sharing radius*).

Metrologicamente, o NSGA-II atua como um otimizador computacional de alta performance para calibrar sistemas de imageamento complexos, redes neurais de reconstrução iterativa e protocolos de aquisição onde os limites regulatórios de dose e os requisitos diagnósticos estão em constante tensão.

---

## 2. Formulação Matemática e Propriedades

Matematicamente, um problema de otimização multiobjetivo (MOOP) tratado pelo NSGA-II é formulado como:

$$
\min_{\mathbf{x} \in \Omega} \mathbf{F}(\mathbf{x}) = \left( f_1(\mathbf{x}), f_2(\mathbf{x}), \dots, f_M(\mathbf{x}) \right)^T
$$

sujeito a restrições de desigualdade e igualdade:

$$
g_i(\mathbf{x}) \ge 0, \quad i = 1, 2, \dots, p
h_j(\mathbf{x}) = 0, \quad j = 1, 2, \dots, q
$$

onde $\mathbf{x} \in \mathbb{R}^n$ é o vetor de variáveis de decisão (por exemplo, parâmetros de corrente do tubo $\text{mA}$, tensão $kVp$, tempo de rotação, ou hiperparâmetros de uma rede de Deep Learning para reconstrução), e $\Omega$ é o espaço de busca viável.

### 1. Ordenação Não-Dominada (*Non-dominated Sorting*)
Diz-se que uma solução $\mathbf{x}^{(1)}$ domina $\mathbf{x}^{(2)}$ ($\mathbf{x}^{(1)} \prec \mathbf{x}^{(2)}$) se e somente se:

$$
\forall i \in \{1, \dots, M\}, \quad f_i(\mathbf{x}^{(1)}) \le f_i(\mathbf{x}^{(2)})
$$

e

$$
\exists j \in \{1, \dots, M\} \text{ tal que } f_j(\mathbf{x}^{(1)}) < f_j(\mathbf{x}^{(2)})
$$

O algoritmo particiona a população combinada $\mathbf{R}_t = \mathbf{P}_t \cup \mathbf{Q}_t$ (pais e filhos) em diferentes frentes de Pareto hierárquicas: $\mathcal{F}_1, \mathcal{F}_2, \dots$. A frente $\mathcal{F}_1$ contém o conjunto estritamente não-dominado de todo o conjunto.

### 2. Distância de Multidão (*Crowding Distance*)
Para manter a diversidade genética e evitar o aglomeramento de soluções em regiões específicas da Fronteira de Pareto, o NSGA-II calcula a densidade de soluções vizinhas para cada indivíduo $i$ na frente $\mathcal{F}_k$. A distância de multidão $d(i)$ é dada por:

$$
d(i) = \sum_{m=1}^{M} \frac{f_m^{(i+1)} - f_m^{(i-1)}}{f_m^{\max} - f_m^{\min}}
$$

onde $f_m^{(i+1)}$ e $f_m^{(i-1)}$ representam os valores do objetivo $m$ para os vizinhos adjacentes da solução $i$ ordenados de forma ascendente, e $f_m^{\max}, f_m^{\min}$ são os valores extremos do objetivo $m$ na população.

### 3. Operador de Comparação Hierárquica ($<_n$)
Um indivíduo $i$ vence o indivíduo $j$ no torneio de seleção se:
- O rank de Pareto de $i$ for menor que o de $j$ ($rank(i) < rank(j)$); ou
- Pertencem ao mesmo rank, mas $i$ possui maior distância de multidão ($rank(i) == rank(j)$ e $d(i) > d(j)$).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

No ecossistema da Tomografia Computadorizada moderna, o NSGA-II desempenha papéis cruciais na interface entre física de radiação, engenharia de imagem e Inteligência Artificial:

1. **Otimização de Protocolos de Aquisição (Gestão de Dose vs. Qualidade):**
   Ajuste simultâneo de parâmetros como miliamperagem ($\text{mA}$), quilovoltagem ($kVp$), pitch helicoidal e filtros de conversão (bowtie filters). O NSGA-II gera frentes ótimas onde o radiologista pode escolher o ponto de operação ideal baseando-se no índice de ruído aceptável para uma patologia específica (ex: detecção de nódulo pulmonar vs. AVC agudo) minimizando a dose glandular ou efetiva.

2. **Sintonia de Hiperparâmetros em Reconstrução Iterativa (IR) e Aprendizado Profundo (DLR):**
   Modelos de reconstrução baseados em aprendizado profundo (*Deep Learning Reconstruction*) exigem a ponderação de múltiplas funções de perda (*loss functions*), como Erro Quadrático Médio ($MSE$), Percepção Estrutural ($SSIM$) e Perda Perceptual de Redes Neurais. O NSGA-II é empregado para otimizar os pesos dessas perdas durante o treinamento ou para ajustar a regularização em abordagens estatísticas iterativas (como penalização por variação total - *Total Variation*).

3. **Projeto de Filtros de Reconstrução e Geometrias de Detecção:**
   Na fase de projeto de hardwares de TC, o algoritmo auxilia na otimização da disposição geométrica de arranjos de detetores de estado sólido e na escolha de perfis de filtragem para mitigar artefatos de feixe policromático (*beam hardening*).

4. **Calibração de Observadores Computacionais:**
   Otimização de parâmetros para observadores baseados em modelos (*Model-Observers*) que simulam a detecção humana (como a *Channelized Hotelling Observer* - CHO) para avaliar a detectabilidade de lesões de baixo contraste em imagens de TC ruidosas.

---

## 4. Conexões e Wikilinks

- [[Reconstrução Iterativa|reconstrucao-iterativa]]
- [[Aprendizado Profundo em TC|aprendizado-profundo-em-tc]]
- [[Dose Efectiva|dose-efectiva]]
- [[Qualidade de Imagem em TC|qualidade-de-imagem-em-tc]]
- [[Artefatos em TC|artefatos-em-tomografia]]
- [[Filtro de Retroprojeccao|filtro-de-retroprojeccao]]
- [[Dosimetria em TC|dosimetria-em-tc]]
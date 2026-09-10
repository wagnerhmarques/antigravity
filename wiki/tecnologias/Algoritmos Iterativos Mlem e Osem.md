---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-de-imagem, mlem, osem, algoritmos-iterativos, otimizacao]
data: 2026-08-25
---

# Algoritmos Iterativos MLEM e OSEM

## 1. Definição Conceitual e Fundamentação Física / Metrológica

Na Tomografia Computadorizada (TC) e, historicamente\, de forma ainda mais proeminente na Tomografia por Emissão de Pós-trons ([[Tomografia por Emissão de Pósitrons (PET)|PET]]) e Tomografia por Emissão de Fóton Único ([[Tomografia por Emissão de Pósitrons (PET)|SPECT]]), a reconstrução de imagens visa estimar a distribuição espacial de uma propriedade física (como o coeficiente de atenuação linear $\mu$ em TC ou a atividade radioativa em medicina nuclear) a partir de projeções medidas externamente pelos detectores. 

Enquanto a Retroprojeção Filtrada ([[Retroprojeção Filtrada (FBP)|FBP]]) domina o cenário de processamento em tempo real devido à sua eficiência analítica e determinística, ela assume um modelo físico idealizado e linear, negligorando estatísticas de ruído de Poisson, ruído quântico, efeitos de volume parcial, espalhamento de radiação e a geometria real do sistema de aquisição. Isso resulta em degradações severas da imagem (como artefatos de streak e degradação da relação sinal-ruído) quando operando em regimes de baixa dose ([[Tomografia Computadorizada (TC)|Baixa Dose em TC]]).

Para superar essas limitações, os **algoritmos iterativos estatísticos** modelam explicitamente a física da aquisição e a natureza estatística do ruído. O algoritmo **MLEM** (*Maximum Likelihood Expectation Maximization* — Maximização da Esperança por Máxima Verossimilhança) constitui o marco fundamental dessa abordagem no domínio probabilístico, formulado com base na estatística de contagem de fótons (distribuição de Poisson). O MLEM busca maximizar a função de verossimilhança de que a distribuição de imagem estimada geraria as projeções observadas.

Contudo, a principal limitação do MLEM clássico é o seu custo computacional proibitivo. Como a atualização de cada voxel requer o retrocálculo de todas as projeções e re-projeções ao longo de todos os ângulos de visão a cada iteração, o tempo de processamento torna-se impraticável para uso clínico rotineiro. Para contornar esse obstáculo, o algoritmo **OSEM** (*Ordered Subset Expectation Maximization*) foi desenvolvido. O OSEM acelera a convergência do MLEM ao agrupar o conjunto completo de dados de projeção em subconjuntos (*subsets*) ordenados e disjuntos, aplicando atualizações iterativas baseadas em frações dos dados de cada vez, o que reduz drasticamente o número de operações computacionais necessárias por equivalente de iteração completa.

---

## 2. Formulação Matemática e Propriedades

### 2.1 Modelo Físico de Aquisição
O processo físico de formação da projeção pode ser discretizado através de um sistema linear afim. Seja $f_j$ o valor da propriedade física no pixel/voxel $j$ (onde $j = 1, \dots, J$) e $g_i$ a medida de projeção no feixe/detector $i$ (onde $i = 1, \dots, I$). A relação entre a imagem e as projeções é dada por:

$$
g_i = \sum_{j=1}^{J} p_{ij} f_j + r_i + s_i
$$

Onde:
- $p_{ij}$ representa o elemento da **matriz de sistema** (ou matriz de probabilidade), correspondendo à probabilidade ou peso de que um fóton emitido (ou atenuado) no voxel $j$ seja detectado no canal $i$.
- $r_i$ representa termos aditivos de ruído de fundo ou radiação espalhada (*scatter*).
- $s_i$ representa a contribuição de fótons acidentais ou correntes de dark-current (em TC, equivalentemente, modela-se o ruído eletrônico após a transformação logarítmica).

Considerando a natureza corpuscular da radiação ionizante e o processo de contagem, as medições $g_i$ seguem uma **estatística de Poisson**. A probabilidade de observar $g_i$ dados os parâmetros da imagem $f$ é dada por:

$$
P(g_i | f) = \frac{e^{-\bar{g}_i} (\bar{g}_i)^{g_i}}{g_i!}
$$

Onde $\bar{g}_i = \sum_{j=1}^{J} p_{ij} f_j + r_i$ é o valor esperado da medição.

### 2.2 Derivação e Formulação do MLEM
A função de log-verossimilhança $L(f)$ para todas as observações independentes $g_i$ é expressa como:

$$
L(f) = \sum_{i=1}^{I} \left[ g_i \ln\left(\sum_{j=1}^{J} p_{ij} f_j + r_i\right) - \left(\sum_{j=1}^{J} p_{ij} f_j + r_i\right) - \ln(g_i!) \right]
$$

O objetivo é encontrar $f \ge 0$ que maximize $L(f)$. Como a maximização direta é analiticamente intratável devido ao acoplamento linear na soma logarítmica, o algoritmo **EM (Expectation-Maximization)** de Dempster-Laird-Rubin é aplicado. 

A equação de atualização iterativa do MLEM para a estimativa do voxel $f_j^{(n+1)}$ na $(n+1)$-ésima iteração, a partir da estimativa $f_j^{(n)}$, é dada por:

$$
f_j^{(n+1)} = \frac{f_j^{(n)}}{\sum_{i=1}^{I} p_{ij}} \sum_{i=1}^{I} p_{ij} \frac{g_i}{\sum_{k=1}^{J} p_{ik} f_k^{(n)} + r_i}
$$

#### Propriedades Notáveis do MLEM:
1. **Não-negatividade:** Se a estimativa inicial $f^{(0)} > 0$, todas as iterações subsequentes garantem $f^{(n)} \ge 0$, o que reflete a realidade física de coeficientes de atenuação e concentrações de atividade.
2. **Conservação de Massa:** Sob certas condições, a soma total dos valores reconstruídos (contagens totais) tende a se conservar ao longo das iterações.
3. **Monotonicidade:** A função de log-verossimilhança não decresce a cada iteração: $L(f^{(n+1)}) \ge L(f^{(n)})$.

### 2.3 Formulação e Aceleração do OSEM
O MLEM calcula o termo de correção usando *todos* os dados de projeção ($I$ medidas) de uma só vez. O OSEM divide o conjunto total de projeções $I$ em $S$ subconjuntos disjuntos e ordenados $\mathcal{S}_s$ (onde $s = 1, \dots, S$). 

A atualização do OSEM processa sequencialmente cada subconjunto $s$. A fórmula de atualização dentro de uma iteração completa (percorrendo todos os $S$ subconjuntos) é:

$$
f_j^{(n, s+1)} = \frac{f_j^{(n, s)}}{\sum_{i \in \mathcal{S}_s} p_{ij}} \sum_{i \in \mathcal{S}_s} p_{ij} \frac{g_i}{\sum_{k=1}^{J} p_{ik} f_k^{(n, s)} + r_i}
$$

Onde $f_j^{(n, 1)} = f_j^{(n)}$ e a estimativa final do ciclo é $f_j^{(n+1)} = f_j^{(n, S)}$.

* **Fator de Aceleração:** O OSEM acelera a convergência por um fator teórica e empiricamente próximo a $S$ em comparação ao MLEM padrão.
* **Comportamento de Limite (Limit Cycles):** Diferente do MLEM, o OSEM não é um algoritmo de máxima verossimilhança estrito; se executado por um número excessivo de iterações com subconjuntos muito pequenos, ele pode não convergir para o ponto de máxima verossimilhança global, mas sim entrar em ciclos limite (*limit cycles*), amplificando ruído de alta frequência na forma de artefatos espúrios. Por essa razão, a parada precoce (*early stopping*) ou a incorporação de penalizações espaciais ([[Regularização e Reconstrução Iterativa]]) são mandatórias.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

No contexto moderno da Tomografia Computadorizada médica, os algoritmos iterativos estatísticos baseados em MLEM/OSEM e suas evoluções (como os algoritmos penalizados MAP - *Maximum A Posteriori*, e algoritmos baseados em mínimos quadrados ponderados como PWLS) desempenham papéis críticos:

1. **Reconstrução Iterativa ([[Reconstrução Iterativa|IR]]) em Baixa Dose:** Permitem reduzir a corrente do tubo de raio-X ($mA$) sem comprometer a diagnosticabilidade. Ao modelar a estatística real do fóton (mitigando o ruído quântico e o viés decorrente da transformação logarítmica de dados corrompidos por ruído eletrônico em feixes severamente atenuados), evitam-se os artefatos de "quantum mottle" típicos da FBP.
2. **Modelagem Avançada do Sistema (ASM):** A matriz de sistema $p_{ij}$ pode codificar a resposta espacial exata do feixe de raios-X (tamanho focal finito, geometria do arranjo de detectores, resposta temporal e espacial do canal). Isso melhora drasticamente a **Função de Espalhamento de Ponto ([[PSF]])** e a resolução espacial efetiva da imagem reconstruída.
3. **Correção de Efeito de Volume Parcial e Red Artefacts:** Em TC de alta resolução (como TC de Tora e Ossos Temporais) e em modalidades híbridas ([[Tomografia por Emissão de Pósitrons (PET)|PET/CT]]), o MLEM/OSEM mitiga artefatos de endurecimento de feixe e feixes poli-energéticos quando acoplados a modelos de forward-projection espectral.
4. **Sinergia com Inteligência Artificial e DLR:** As limitações computacionais dos algoritmos iterativos tradicionais e a necessidade de regularização heurística abriram espaço para abordagens híbridas. Redes Neurais Profundas ([[Deep Learning Reconstruction (DLR)|Deep Learning Reconstruction - DLR]]) e algoritmos baseados em *Deep Image Prior* ou *Plug-and-Play Priors* utilizam o operador de projeção/retroprojeção derivado do MLEM/OSEM combinados com redes geradoras para denodificação avançada e aceleração drástica da reconstrução em tempo real.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[FBP|FBP (Retroprojeção Filtrada)]]
* [[Reconstrução Iterativa|Reconstrução Iterativa]]
* [[PET (Tomografia por Emissão de Pós-trons)]]
* [[Tomografia por Emissão de Pósitrons (PET)|SPECT]]
* [[Tomografia Computadorizada (TC)|Baixa Dose em TC]]
* [[Regularização e Reconstrução Iterativa]]
* [[Deep Learning Reconstruction (DLR)|Deep Learning Reconstruction - DLR]]
* [[Controle de Qualidade em TC]]
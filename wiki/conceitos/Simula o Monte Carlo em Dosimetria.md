---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, dosimetria, monte-carlo, radioprotecao]
data: 2026-08-25
---

# Simulação Monte Carlo em Dosimetria

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A simulação pelo método de **Monte Carlo (MC)** em física médica e dosimetria representa a abordagem computacional mais rigorosa e fundamental para modelar o transporte e a interação de radiação ionizante (fótons, elétrons, pósitrons, prótons e nêutrons) com a matéria. O método baseia-se na amostragem estatística de distribuições de probabilidade conhecidas para simular o comportamento de partículas individuais, reproduzindo microscopicamente os processos estocásticos associados à física de interações atômicas e nucleares.

Na dosimetria aplicada à Tomografia Computadorizada (TC) e à radioterapia, as simulações MC permitem rastrear o histórico completo de milhões ou bilhões de partículas (histórias) desde a fonte de radiação — como o anodo de raios X e os filtros de conformação da calha — até a sua deposição de energia em volumes de interesse (VOIs) dentro de fantasmas antropomórficos computacionais (fantasmas baseados em *voxels* ou malhas poligonais/NURBS). 

Do ponto de vista metrológico, o cálculo via Monte Carlo é considerado o **padrão-ouro (*gold standard*)** teórica. Diferente dos algoritmos analíticos tradicionais ou métodos determinísticos (como equações de transporte de Boltzmann simplificadas), o MC não faz aproximações drásticas na modelagem do espalhamento múltiplo, da atenuação heterogênea ou da retroesparsação eletrônica. Ele resolve a equação de transporte de radiação por meio de leis fundamentais da mecânica quântica e eletrodinâmica quântica (QED), englobando explicitamente efeitos como:
* O efeito fotoelétrico com emissão de raios X característicos e elétrons Auger;
* Espalhamento Compton coerente (Rayleigh) e incoerente (Compton), considerando correções form-factor e funções de espalhamento inelástico;
* Produção de pares e tripletos;
* Freios radiativos (*Bremsstrahlung*) e aniquilação de pósitrons;
* Dispersão múltipla de elétrons por meio de algoritmos de condensação de etapas (*Condensed History Technique*).

---

## 2. Formulação Matemática e Propriedades

O método fundamenta-se na Lei dos Grandes Números e no Teorema do Limite Central. A grandeza de interesse dosimétrica, tipicamente a dose absorvida $D(\mathbf{r})$ em um ponto ou voxel $\mathbf{r}$, é calculada como o valor esperado da energia depositada por unidade de massa:

$$
D(\mathbf{r}) = \frac{d\bar{E}_{\text{dep}}(\mathbf{r})}{dm} = \frac{1}{\rho(\mathbf{r})} \int_{0}^{\infty} \Phi_E(\mathbf{r}, E) \left( \frac{\mu_{\text{en}}(E)}{\rho} \right) E \, dE
$$

Em uma simulação de Monte Carlo, a dose em um elemento de volume $V$ contendo massa $m$ é estimada pelo somatório estocástico das energias depositadas por todas as histórias de partículas simuladas:

$$
D_{\text{MC}}(V) = \frac{1}{m(V)} \sum_{i=1}^{N} \epsilon_{i, V}
$$

Onde:
* $N$ é o número total de histórias simuladas;
* $\epsilon_{i, V}$ é a energia total depositada no volume $V$ pela $i$-ésima história de partícula (incluindo partículas secundárias geradas em cascata).

A incerteza estatística associada ao cálculo de Monte Carlo (desvio padrão da média, $\sigma_{\bar{D}}$) é inerente à natureza estocástica do método e é inversamente proporcional à raiz quadrada do número de histórias $N$:

$$
\sigma_{\bar{D}} \propto \frac{1}{\sqrt{N}}
$$

Para garantir a convergência e a acurácia dos resultados dosimétricos, a variância estatística $\sigma^2$ da dose depositada em um voxel é estimada através da estimativa da variância da amostra:

$$
\sigma^2(D) = \frac{1}{N(N-1)} \sum_{i=1}^{N} \left( \epsilon_{i, V} - \bar{\epsilon}_V \right)^2
$$

Como simular cada colisão atômica individualmente para elétrons é computacionalmente inviável devido ao altíssimo número de interações de baixa energia (da ordem de $10^5$ a $10^6$ interações por mm), utilizam-se algoritmos de história condensada (como o implementado no código PENELOPE ou EGBnrc/BEAMnrc). A energia média perdida em um passo de comprimento s é governada por equações de poder de parada restrito e irrestrito:

$$
\left( -\frac{dE}{ds} \right)_{\text{tot}} = \left( -\frac{dE}{ds} \right)_{\text{col}} + \left( -\frac{dE}{ds} \right)_{\text{rad}}
$$

Onde os termos representam as perdas colisionais (ionização e excitação, descritas pela teoria de Bethe-Bloch com correções de densidade e de camada) e radiativas (*Bremsstrahlung*).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Em Tomografia Computadorizada, a simulação Monte Carlo desempenha um papel crítico na quantificação de doses de radiação em órgãos, no projeto de novos sistemas de aquisição e na validação de protocolos clínicos:

1. **Dosimetria Específica do Paciente:** Permite calcular a dose absorvida em órgãos específicos (*Organ Dose*) e a Dose Efetiva ($E$) com base em exames reais, utilizando fantasmas computacionais dimensionados de acordo com o índice de massa corporal (IMC) ou o diâmetro de atenuação em água ($D_{w}$). Isso supera as limitações dos índices tradicionais como o $CTDI_{vol}$ e o DLP, que utilizam cilindros acrílicos padronizados de 16 cm e 32 cm.
2. **Modelagem de Feixes Complexos e Validação de QA:** Softwares baseados em MC (como *Geant4*, *MCNP*, *FLUKA*, *TOPAS* e *PENELOPE*) são empregados para modelar detalhadamente a geometria do tubo de raios X, a focalização do feixe, a filtragem acoplada (filtro *bowtie*) e a modulação de corrente angular e longitudinal (*tube current modulation* - TCM).
3. **Desenvolvimento e Treinamento de Observadores Computacionais:** Em tarefas de otimização de algoritmos de reconstrução (FBP, Iterativos e DLR - *Deep Learning Reconstruction*), o MC é utilizado para simular ruído estatístico quântico realista e artefatos de feixe endurecido (*beam hardening*), gerando pares de imagens ruidosas e de referência (*ground truth*) livres de ruído para redes neurais.
4. **Redução de Tempo de Computação (Aceleração por Hardware):** Devido ao elevado custo computacional histórico, o uso de MC em tempo real ou quase real na rotina clínica foi inviável por décadas. Contudo, o advento de simulações aceleradas por unidades de processamento gráfico (GPU), como nos pacotes *Gamos*, *TOPAS-nBio* e ferramentas proprietárias baseadas em *CUDA/OpenCL*, reduziu o tempo de cálculo de horas para segundos, viabilizando sua integração na dosimetria personalizada de rotina.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[Dose Absorvida e Dosimetria em Raio-X]]
* [[CTDI e Índices de Dose em TC]]
* [[Fantasmas Antropomórficos Computacionais]]
* [[Controle de Qualidade em TC|Controle de Qualidade em Radiodiagnóstico]]
* [[Reconstrução Iterativa|Reconstrução Iterativa e DLR]]
* [[Efeitos Estocásticos e Determinísticos da Radiação]]
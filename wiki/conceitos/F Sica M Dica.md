---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, dosimetria, radioprotecao, metrologia-das-radiacoes]
data: 2026-08-25
---

# física-médica

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A Física Médica é uma especialidade da física aplicada que emprega os conceitos, métodos e princípios da física na prática da medicina, com ênfase primária na prevenção, diagnóstico e tratamento de patologias humanas, bem como na proteção radiológica de pacientes, trabalhadores ocupacionalmente expostos (TOE) e do público em geral. No escopo da imaginologia diagnóstica — e, de maneira destacada, na [[Tomografia Computadorizada|tomografia-computadorizada]] (TC) —, a atuação do físico médico fundamenta-se na metrologia das radiações ionizantes, na caracterização de feixes de raios X, na otimização da relação entre qualidade de imagem e dose absorvida, e na garantia de desempenho dos sistemas de imageamento.

Sob a perspectiva metrológica, a fundamentação teórica baseia-se na quantificação rigorosa da interação da radiação eletromagnética (fótons de raios X) com a matéria biológica. Os principais processos de atenuação linear e mássica — incluindo o efeito fotoelétrico, o espalhamento Compton e a produção de pares (embora esta última ocorra apenas em energias superiores aos limiares de limiar de 1,022 MeV, irrelevantes na faixa diagnóstica padrão) — determinam o coeficiente de atenuação linear $\mu(E, \vec{r})$, o qual constitui a base física para a formação da matriz de dados brutos e a posterior reconstrução tomográfica. A metrologia aplicada assegura a rastreabilidade das grandezas dosimétricas a padrões primários, utilizando câmaras de ionização de cavidade calibradas, dosímetros termoluminescentes (TLD) e diodos de estado sólido.

## 2. Formulação Matemática e Propriedades

A propagação e atenuação de um feixe de fótons monoenergéticos através de um meio heterogêneo são descritas pela equação diferencial da atenuação (Lei de Beer-Lambert):

$$
\frac{dI}{I} = -\mu(x) \, dx \implies I(x) = I_0 \exp \left( -\int_{0}^{x} \mu(x') \, dx' \right)
$$

Onde:
- $I_0$ é a intensidade incidente do feixe de radiação;
- $I(x)$ é a intensidade após atravessar uma espessura $x$;
- $\mu(x')$ é o coeficiente de atenuação linear local ($\text{cm}^{-1}$).

Em [[Tomografia Computadorizada|tomografia-computadorizada]], o feixe de raios X é policromático, gerando o fenômeno de endurecimento do feixe (*beam hardening*), onde os fótons de menor energia são preferencialmente absorvidos, deslocando o espectro efetivo para energias mais altas ($\bar{E}$). Para modelar a atenuação policromática, a intensidade detectada é expressa como uma integral sobre o espectro energético $N(E)$:

$$
I = \int_{0}^{E_{\max}} I_0(E) \exp \left( -\int_{L} \mu(x, E) \, dl \right) dE
$$

A dose absorvida $D$, definida como a energia média depositada pela radiação ionizante por unidade de massa em um elemento de volume infinitesimal, é formulada matematicamente como:

$$
D = \frac{d\bar{E}}{dm}
$$

Sendo expressa em Joules por quilograma ($\text{J kg}^{-1}$), unidade denominada Gray ($\text{Gy}$). Em dosimetria de TC, grandezas específicas como o *Computed Tomography Dose Index* (CTDI) são derivadas de integrais do perfil de dose ao longo do eixo z. O $CTDI_{100}$ e o $CTDI_{w}$ (ponderado) são calculados por:

$$
CTDI_{100} = \frac{1}{nT} \int_{-50\,\text{mm}}^{+50\,\text{mm}} D(z) \, dz
CTDI_{w} = \frac{1}{3} CTDI_{100,\text{centro}} + \frac{2}{3} CTDI_{100,\text{periferia}}
$$

Onde $n$ é o número de cortes tomográficos adquiridos simultaneamente e $T$ é a espessura nominal de cada corte. A introdução de técnicas avançadas de [[Reconstrução de Imagem|reconstrucao-de-imagem]] e [[otimizacao-da-dose]] exige o cálculo do $CTDI_{vol}$ e do Produto Dose-Comprimento ($DLP$):

$$
CTDI_{vol} = \frac{CTDI_{w}}{\text{pitch}}
DLP = CTDI_{vol} \times \text{Comprimento de Varredura}
$$

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A interface entre a física médica e a tomografia computadorizada consolida-se por meio de três pilares fundamentais: garantia da qualidade (GQ), otimização dos protocolos clínicos e dosimetria avançada.

1. **Garantia da Qualidade (GQ) e Controle de Qualidade (CQ):** 
   O físico médico desenvolve programas sistemáticos para avaliar parâmetros críticos de desempenho dos scanners de TC, tais como: a linearidade e uniformidade das Unidades Hounsfield (HU), a resolução espacial de alto contraste (através da função de transferência de modulação - [[Modulation Transfer Function (MTF)|mtf]]), a resolução espacial de baixo contraste (avaliada por ruído e detectabilidade com base na teoria de [[Observadores de Modelo (Model Observers)|observadores-computacionais]]), e a constância da taxa de dose.

2. **Otimização da Reconstrução de Imagem e DLR:** 
   Com a transição de algoritmos analíticos tradicionais, como a retroprojeção filtrada ([[Retroprojeção Filtrada (FBP)|fbp]]), para métodos iterativos ([[Reconstrução Iterativa|ir]]) e, mais recentemente, algoritmos baseados em aprendizado profundo ([[Deep Learning Reconstruction (DLR)|dlr]]), o físico médico atua na validação quantitativa da fidelidade da imagem. Isso engloba a prevenção de artefatos (endurecimento de feixe, *ring artifacts*, feixe espalhado) e a garantia de que a redução de ruído promovida por redes neurais não resulte na perda de texturas patológicas sutis ou viés quantitativo nos números CT.

3. **Dosimetria Computacional e Modelagem Fantoma:** 
   O cálculo de risco estocástico e determinístico fundamenta-se na estimativa da dose efetiva ($E$, em Sieverts - $\text{Sv}$), obtida mediante coeficientes de conversão aplicados ao $DLP$. Atualmente, simulações de Monte Carlo acopladas a modelos anatômicos antropomórficos computacionais (fantasomas baseados em *mesh* e Voxel) permitem a dosimetria específica por paciente, orientando protocolos pediátricos e gestacionais de alta complexidade.

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|tomografia-computadorizada]]
- [[Retroprojeção Filtrada (FBP)|fbp]]
- [[Reconstrução Iterativa|ir]]
- [[Deep Learning Reconstruction (DLR)|dlr]]
- [[Modulation Transfer Function (MTF)|mtf]]
- [[otimizacao-da-dose]]
- [[Observadores de Modelo (Model Observers)|observadores-computacionais]]
- [[Reconstrução de Imagem|reconstrucao-de-imagem]]
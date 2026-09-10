---
tipo: tecnologia
tags: [fisica-medica, medicina-nuclear, pet, tomografia-computadorizada, imagem-molecular, dosimetria, inteligencia-artificial]
data: 2026-08-25
---

# Tomografia por Emissão de Positrons (PET)

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A Tomografia por Emissão de Pósitrons (PET, do inglês *Positron Emission Tomography*) é uma modalidade avançada de imagem médica funcional e molecular que permite a visualização e a quantificação tridimensional de processos bioquímicos e fisiológicos *in vivo*. Ao contrário das modalidades de imagem anatômica, como a Tomografia Computadorizada (TC) convencional ou a Ressonância Magnética (RM), que delineiam a morfologia tecidual, a PET mapeia a distribuição espacial de radiofármacos marcados com radionuclídeos emissores de pósitrons ($\beta^+$).

### Fundamentação Física e Aniquilação
O princípio físico fundamental da PET baseia-se no decaimento radioativo por emissão de pósitrons. Um núcleo instável com excesso de prótons decai transformando um próton em um nêutron, emitindo um pósitron ($\beta^+$) e um neutrino eletrônico ($
u_e$):

$$
p 
ightarrow n + \beta^+ + 
u_e
$$

Após ser emitido pelo núcleo radioativo (por exemplo, $^{18}\text{F}$, $^{11}\text{C}$, $^{13}\text{N}$, $^{15}\text{O}$), o pósitron viaja uma curta distância no meio tecido-equivalente — conhecida como *distância de percurso do pósitron* ou *positron range*, tipicamente da ordem de milímetros (dependendo da energia cinética máxima do pósitron) — até perder sua energia cinética através de colisões com elétrons atômicos. 

Quando o pósitron se desacelera o suficiente, ele sofre uma interação de obliteração mútua com um elétron orbital circundante. Esse processo é denominado **aniquilação pósitron-elétron**. 

Na aniquilação, a massa combinada das duas partículas ($m_e^+ + m_e^- \approx 2m_0c^2$) é convertida em energia pura, manifestada sob a forma de dois fótons de radiação gama (fótons de aniquilação). Para satisfazer simultaneamente as leis de conservação de energia e de momento linear (considerando que o par pósitron-elétron possui momento quase nulo no momento da interação devido à prévia termalização), os dois fótons são emitidos em direções estritamente opostas, formando um ângulo de $180^\circ$ idealmente. Cada fóton possui uma energia exata de repouso correspondente à massa do elétron:

$$
E_\gamma = m_0 c^2 \approx 511 \text{ keV}
$$

### Detecção por Coincidência
O sistema de detecção do escâner PET explora essa geometria de emissão oposta. O gantry do equipamento é composto por um anel (ou múltiplos anéis) de cristais cintiladores densos (como LSO:Lu₂SiO₅:Ce, LYSO:Lu_{2-x}Y_xSiO_5:Ce ou BGO:Bi_4Ge_3O_{12}) acoplados a fotodetectores de alta velocidade (tipicamente fotomultiplicadores de silício - SiPMs). 

Quando os dois fótons de 511 keV atingem cristais diametralmente opostos em um intervalo de tempo infinitesimal (janela de coincidência temporal $\tau$, tipicamente entre 4 ns a 10 ns), o sistema registra um **evento de coincidência**. A linha reta que conecta os dois detectores atingidos é denominada **Linha de Resposta (LOR - *Line of Response*)**. 

As coincidências podem ser classificadas em três categorias fundamentais que afetam a relação sinal-ruído (SNR) e a quantificação:
1. **Coincidências Verdadeiras (*True Coincidences*):** O par de fótons originado do mesmo evento de aniquilação atinge os dois detectores sem interações de espalhamento prévias.
2. **Coincidências Espalhadas (*Scattered Coincidences*):** Um ou ambos os fótons sofrem espalhamento Compton no tecido do paciente antes de atingirem os detectores, resultando em um registro incorreto da LOR.
3. **Coincidências Acidentais ou Randômicas (*Random Coincidences*):** Dois fótons provenientes de eventos de aniquilação completamente distintos e independentes atingem os detectores dentro da janela temporal $\tau$, sendo erroneamente interpretados como um único par correlacionado.

## 2. Formulação Matemática e Propriedades

A reconstrução de imagem em PET visa recuperar a distribuição espacial tridimensional da concentração de atividade radioativa, denotada por $f(x, y, z)$, a partir do conjunto de dados coletados em termos de LORs.

### O Modelo de Projeção e a Transformada de Radon
O processo de aquisição pode ser modelado matematicamente através da Equação Integral de Radon modificada para a geometria de emissão. O número esperado de eventos de coincidência registrados ao longo de uma LOR específica parametrizada pela distância $s$ e ângulo $\phi$ (em 2D) é dado por:

$$
p(s, \phi) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) \delta(x \cos\phi + y \sin\phi - s) \, dx \, dy
$$

No entanto, a formulação física real em PET deve incorporar fatores cruciais de degradação do sinal, tais como a atenuação dos fótons pelo meio físico, a eficiência geométrica dos detectores, o tempo morto, e a presença de radiação espalhada e acidental. O modelo estatístico avançado descreve o valor esperado do dado mensurado $y_i$ para a $i$-ésima LOR como uma variável aleatória de Poisson:

$$
\bar{y}_i = \sum_{j=1}^{N} P_{ij} f_j + r_i + s_i
$$

Onde:
- $f_j$ representa a atividade no $j$-ésimo voxel (discretização do espaço).
- $P_{ij}$ é a probabilidade do fóton emitido no voxel $j$ ser detectado na LOR $i$. Esta matriz incorpora a atenuação $A_i$, a eficiência de detecção e a resposta espacial do sistema (PSF - *Point Spread Function*).
- $r_i$ e $s_i$ representam os termos aditivos de contribuição de radiação acidental e espalhada, respectivamente.

### Algoritmos de Reconstrução Iterativa
Devido à natureza estocástica dos dados de contagem em PET e à necessidade de modelar efeitos físicos complexos, os métodos analíticos tradicionais (como a Retroprojeção Filtrada - FBP) foram amplamente suplantados por algoritmos de reconstrução estatística iterativa baseados na máxima verossimilhança (*Maximum Likelihood*).

O algoritmo padrão ouro na prática clínica é o **MLEM (*Maximum Likelihood Expectation Maximization*)** e sua versão acelerada por blocos ordenados, o **OSEM (*Ordered Subset Expectation Maximization*)**:

$$
f_j^{(k+1)} = \frac{f_j^{(k)}}{\sum_{i=1}^{N} P_{ij}} \sum_{i=1}^{N} P_{ij} \frac{y_i}{\sum_{m=1}^{M} P_{im} f_m^{(k)} + r_i + s_i}
$$

Onde $k$ denota o número da iteração. O OSEM agrupa as LORs em subconjuntos disjuntos ($\mathcal{S}_u$), acelerando a convergência em um fator proporcional ao número de subconjuntos utilizados.

### Correção de Tempo de Voo (TOF-PET)
Sistemas PET modernos incorporam a tecnologia **TOF (*Time-Of-Flight*)**, que mede a diferença infinitesimal de tempo de chegada $\Delta t$ entre os dois fótons detectados. A posição espacial estimada do evento de aniquilação ao longo da LOR é dada por:

$$
\Delta x = \frac{c \cdot \Delta t}{2}
$$

Onde $c$ é a velocidade da luz no vácuo. Com uma resolução temporal atual dos fotodetectores da ordem de $\Delta t \approx 200 \text{ ps}$, a incerteza posicional ao longo da LOR é reduzida para cerca de $30 mm$. Matematicamente, isso altera o núcleo de probabilidade $P_{ij}$, restringindo a contribuição do voxel $j$ apenas a uma região restrita da LOR, o que reduz drasticamente a variância da imagem reconstruída, melhorando a SNR conforme o ganho de ganho de SNR TOF:

$$
\text{Gain}_{\text{TOF}} \approx \sqrt{\frac{D}{d}}
$$

Onde $D$ é o diâmetro do objeto e $d$ é a resolução espacial equivalente ao erro temporal de localização.

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimización

### Integração Multimodal: PET/CT
A evolução tecnológica consolidou a fusão hard-ware dos sistemas **PET/CT**, onde um tomógrafo computadorizado de múltiplos cortes (MDCT) é acoplado no mesmo gantry ao sistema PET. 

A Tomografia Computadorizada desempenha um papel duplo e crítico na PET:
1. **Correção de Atenuação (AC):** Os fótons de 511 keV sofrem atenuação exponencial ao atravessar o corpo do paciente. Os mapas de atenuação derivados dos exames de CT (convertidos de unidades Hounsfield - HU para coeficientes de atenuação linear em 511 keV por meio de segmentação e dimensionamento bilinear de energia) são aplicados diretamente nos algoritmos iterativos para corrigir a subestimação de atividade em estruturas profundas.
2. **Correção Anatômica e Fusão de Imagens:** A matriz anatômica de alta resolução do CT permite a localização espacial precisa de anomalias funcionais detectadas pela PET, essencial na oncologia (estadiamento, planejamento de radioterapia), neurologia (focos epilogênicos, demências) e cardiologia (viabilidade miocárdica).

### Otimização, Dosimetria e Controle de Qualidade
* **Dosimetria Interna e Otimização da Dose:** O princípio ALARA (*As Low As Reasonably Achievable*) aplica-se rigorosamente. A otimização da atividade injetada do radiofármaco (ex: $^{18}\text{F-FDG}$) em conjunto com protocolos de varredura CT de baixa dose garante a minimização da dose efetiva combinada ao paciente sem comprometer a detectabilidade de lesões.
* **Algoritmos de Reconstrução Avançados e DLR (*Deep Learning Reconstruction*):** Redes neurais profundas têm sido integradas aos pipelines de reconstrução PET para supressão de ruído em doses ultra-baixas de radiofármaco ou tempos de aquisição reduzidos, permitindo manter a acurácia quantitativa (como o cálculo preciso do SUV - *Standardized Uptake Value*).
* **Controle de Qualidade Metrológico:** Inclui calibração cruzada periódica entre o calibrador de doses (*dose calibrator*), o escáner PET/CT e o poço de contagem (*gamma counter*), assegurando a rastreabilidade metrológica da atividade absoluta para fins de quantificação clínica e ensaios clínicos multicêntricos (ex: diretrizes PERCIST).

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[Reconstrucao de Imagem por OSEM]]
* [[Correcao de Atenuacao em PET-CT]]
* [[Fisica da Radiacao e Dosimetria]]
* [[Inteligencia Artificial IA|Inteligencia Artificial em Imagem Medica]]
* [[Radiofarmacos e Medicina Nuclear]]
---
tipo: tecnologia
tags: [fisica-medica, radioterapia, braquiterapia, hdr, dosimetria, radiobiologia, tomografia-computadorizada]
data: 2026-08-25
---

# Braquiterapia de Alta Taxa de Dose (HDR)

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A Braquiterapia de Alta Taxa de Dose (HDR — *High Dose Rate*) é uma modalidade de radioterapia de distância curta em que fontes radioativas seladas de alta atividade são posicionado diretamente no interior ou nas proximidades do volume tumoral (tratamento intersticial, intracavitário, intraluminal ou de contato). Pela definição clínica e radiológica estabelecida por comissões internacionais como a *International Commission on Radiation Units and Measurements* (ICRU) e a *American Association of Physicists in Medicine* (AAPM), o regime HDR é caracterizado por uma taxa de dose no ponto de prescrição superior a $0.2 \, \text{Gy/min}$ ($12 \, \text{Gy/h}$). Em aplicações clínicas modernas, tipicamente utilizam-se fontes de Irídio-192 ($^{192}\text{Ir}$) com taxas de dose iniciais que podem exceder $10 \, \text{Gy/min}$.

Do ponto de vista metrológico e da física das radiações, a fonte de $^{192}\text{Ir}$ emite fótons gama com um espectro de energia médio de aproximadamente $380 \, \text{keV}$ (variando de $0.1$ a $1.0 \, \text{MeV}$). A calibração primária dessa fonte é rastreada a laboratórios de metrologia (como o NIST ou BIPM) e expressa em termos de **Taxa de Kerma no Ar no Ar Reference** ($S_K$), medida em $\mu\text{Gy}\cdot\text{m}^2/\text{h}$ ou $\text{U}$ ($1 \, \text{U} = 1 \, \mu\text{Gy}\cdot\text{m}^2/\text{h}$). 

O equipamento de pós-carregamento remoto (*afterloader*) armazena a fonte blindada e a conduz através de cateteres flexíveis ou rígidos até os locais anatômicos pré-planejados, permitindo tempo de residência (*dwell times*) altamente calculados para cada posição (*dwell positions*). Isso elimina a exposição ocupacional prévia inerente à braquiterapia manual (low dose rate histórica) e confere conformidade espacial superior à dose absorvida.

---

## 2. Formulação Matemática e Propriedades

O cálculo da dose absorvida em braquiterapia baseia-se amplamente no formalismo do protocolo **AAPM TG-43** (e suas atualizações TG-43U1), que calcula a taxa de dose $\dot{D}(r, \theta)$ em um ponto $(r, \theta)$ no entorno de uma fonte pontual ou linear através de fatores multiplicativos desacoplados:

$$
\dot{D}(r, \theta) = S_K \cdot \Lambda \cdot \frac{G_L(r, \theta)}{G_L(r_0, \theta_0)} \cdot g_L(r) \cdot F(r, \theta)
$$

Onde:
*   $S_K$: É a taxa de kerma no ar de referência da fonte ($\text{U}$).
*   $\Lambda$: É a **constante de taxa de dose** ($\text{cGy}\cdot\text{h}^{-1}\cdot\text{U}^{-1}$), definida na distância de referência $r_0 = 1 \, \text{cm}$ e ângulo de referência $\theta_0 = \pi/2$.
*   $G_L(r, \theta)$: É a **função de geometria**, que modela a distribuição espacial da intensidade da radiação considerando a fonte como uma linha de comprimento $L$ ou como ponto ($L=0$). Para uma fonte pontual:
    
$$
G_P(r) = \frac{1}{r^2}
$$

*   $\phi_g(r)$: É o **fator de transmissão da blindagem e do aplicador**, contabilizando a atenuação imposta por cilindros vaginais, agulhas ou aplicadores metálicos/plásticos.
*   $g_L(r)$: É a **função radial de dose**, que corrige a atenuação e o espalhamento dos fótons ao longo da distância transversal ao longo do eixo da fonte:
    
$$
g_L(r) = \frac{\dot{D}(r, \theta_0) \cdot G_L(r_0, \theta_0)}{\dot{D}(r_0, \theta_0) \cdot G_L(r, \theta)}
$$

*   $F(r, \theta)$: É a **função de anisotropia 2D**, que descreve a variação angular da dose em função da obliquidade da radiação filtrada pela própria cápsula de aço inoxidável da fonte e pelo meio circundante.

A dose total acumulada $D(r, \theta)$ em um ponto de interesse é obtida pela integração ou somatória dos tempos de residência $t_i$ da fonte em cada passo de parada discreto $i$:

$$
D(r, \theta) = \sum_{i} \dot{D}_i(r_i, \theta_i) \cdot t_i
$$

No aspecto radiobiológico, o regime HDR submete os tecidos a taxas depletoras de reparo celular rápido. O modelo Linear-Quadrático (LQ) modifica-se para considerar a repopulação e o subletheal damage repair através do fator de inativação celular, onde a dose biológica efetiva ($\text{BED}$) para um tratamento de braquiterapia HDR fracionada é dada por:

$$
\text{BED} = N \cdot d \left[ 1 + \frac{d}{\alpha/\beta} \right] - \frac{\ln(2)}{\alpha \cdot T_{pot}} \cdot (t_{overall})
$$

Onde $N$ é o número defrações, $d$ é a dose por fração, $\alpha/\beta$ é a razão paramétrica tecidual, e o segundo termo contempla a correção por repopulação tumoral ao longo do tempo total $t_{overall}$.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Embora a braquiterapia HDR seja tradicionalmente planejada com base em imagens de ultrassongrafia ou ressonância magnética (RM) — especialmente no câncer de colo uterino —, a **Tomografia Computadorizada (TC)** desempenha um papel central e indispensável na validação geométrica, no cálculo dosimétrico e na fusão multimodal em tempo real.

1.  **Reconstrução de Aplicadores e Fusão de Imagens:** 
    Após a inserção dos aplicadores no paciente, a aquisição de imagens volumétricas por TC (muitas vezes TC cônica - CBCT integrada ao bunker ou tomografia de alta resolução) fornece a matriz espacial tridimensional necessária para identificar as coordenadas cartesianas $(x, y, z)$ dos canais de transferência da fonte. Algoritmos de reconstrução avançados, incluindo *Iterative Reconstruction* (IR) e técnicas baseadas em *Deep Learning Reconstruction* (DLR), são cruciais para mitigar artefatos de endurecimento de feixe (*beam hardening*) e artefatos metálicos causados por aplicadores de titânio ou aço inoxidável, permitindo uma segmentação precisa dos órgãos em risco (OARs) como bexiga, reto e sigmoide.

2.  **Otimização Baseada em Imagem (Image-Guided Brachytherapy - IGBT):**
    A otimização dos tempos de residência ($t_i$) nos tratamentos HDR modernos emprega algoritmos computacionais avançados de otimização inversa baseados em custos volumétricos (DVH - *Dose-Volume Histogram* optimization). A TC fornece os mapas de densidade eletrônica necessários para algoritmos de cálculo de dose avançados, superando as limitações do formalismo TG-43 (que assume meio homogêneo de água) através de algoritmos de colapso de raios (*Collapsed Cone Convolution*) ou simulações baseadas em **Monte Carlo**. Esses métodos computacionais contabilizam as heterogeneidades de tecidos (osso, ar, tecido adiposo) e a presença de aplicadores densos, otimizando a distribuição espacial da dose para maximizar a cobertura do CTV (*Clinical Target Volume*) e poupar os OARs.

3.  **Controle de Qualidade (CQ) Metrológico:**
    Em termos de instrumentação, a verificação da posição da fonte (*source position check*), a integridade dos cateteres e a calibração do medidor de poço (*biennial well-type ionization chamber*) utilizam protocolos estritos nos quais a exatidão espacial deve ser mantida dentro de tolerâncias inferiores a $\pm 1 \, \text{mm}$.

---

## 4. Conexões e Wikilinks

*   [[Tomografia Computadorizada|Tomografia Computadorizada]]
*   [[Algoritmos de Reconstrução em TC]]
*   [[Dosimetria em Radiologia|Dosimetria da Radiação]]
*   [[Efeitos Biológicos das Radiações (Radiobiologia)]]
*   [[Simula o de Monte Carlo em F Sica M Dica|Simulação de Monte Carlo em Física Médica]]
*   [[Controle de Qualidade em Radioterapia]]
---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, controle-de-qualidade, dosimetria, metrologia, pmma, radiodiagnóstico]
data: 2026-08-25
---

# fantoma-de-pmma

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **fantoma de PMMA** (Poli(metacrilato de metila)), comercialmente conhecido como Lucite, Acrílico ou Plexiglass, é um dispositivo antropomórfico simplificado ou geométrico (frequentemente cilíndrico ou em forma de placas) empregado na física médica e na metrologia das radiações ionizantes, com ênfase primordial na **Tomografia Computadorizada (TC)**. 

Do ponto de vista físico-metrológico, o PMMA é um polímero sintético de fórmula química $\left(\mathrm{C_5\mathcal{H}_8\mathcal{O}_2}\right)_n$, cuja densidade mássica nominal situa-se tipicamente entre $1,18 \, \mathrm{g/cm^3}$ e $1,19 \, \mathrm{g/cm^3}$, e possui número atômico efetivo ($Z_{\text{eff}}$) e número de elétrons por unidade de massa próximos aos do tecido mole humano para energias de raios X diagnósticos. Esta característica faz com que o PMMA sirva como um meio equivalentes a tecidos moles macios de referência para testes de desempenho de imagem e avaliações dosimétricas.

Na rotina de garantia da qualidade (GQ) em TC, os fantomas de PMMA são padronizados em dimensões geométricas estritas — classicamente em cilindros concêntricos com diâmetros representativos da cabeça adulta ($\approx 16 \, \mathrm{cm}$) e do corpo adulto ($\approx 32 \, \mathrm{cm}$), além de fantomas modulares para avaliação de qualidade de imagem (como o fantoma ACR — *American College of Radiology*). Eles permitem simular o espalhamento Compton ($\text{scattering}$) e a atenuação polienergética experimentada pelo feixe de raios X ao atravessar o corpo humano, fornecendo um arcabouço reprodutível e estável para a quantificação de parâmetros físicos fundamentais.

---

## 2. Formulação Matemática e Propriedades (se aplicável)

A interação dos fótons de raios X com o fantoma de PMMA rege-se pela lei de atenuação exponencial de Beer-Lambert para feixes estreitos e modificada para feixes largos (geometria de TC) através do fator de buildup. A transmissão de intensidade é dada por:

$$
I(x) = I_0 \exp \left( -\int_{0}^{x} \mu(E, \vec{r}) \, dl \right)
$$

Onde:
- $I_0$ é a intensidade incidente do feixe polienergético de raios X.
- $\mu(E, \vec{r})$ é o coeficiente de atenuação linear espacialmente dependente, função da energia $E$ e da composição elementar do PMMA.

Para fins de calibração em Tomografia Computadorizada, a resposta do sistema é quantificada em termos de **Número de Tomografia Computadorizada (NTC)**, expresso em Unidades Hounsfield ($\text{HU}$):

$$
\text{HU} = 1000 \times \frac{\mu_{\text{material}}(E) - \mu_{\text{água}}(E)}{\mu_{\text{água}}(E)}
$$

Embora o fantoma seja construído de PMMA, o sistema de aquisição é calibrado tendo a água pura como referência padrão ($\text{HU}_{\text{água}} \equiv 0$). O PMMA possui um valor nominal de NTC padronizado que oscila tipicamente entre $+100 \, \text{HU}$ e $+120 \, \text{HU}$ dependendo do espectro de energia do tubo de raios X (kilovoltagem pico, $\text{kVp}$) e da filtração inerente/adicionada, devido à sua densidade eletrônica superior à da água ($\rho_{e,\text{PMMA}} > \rho_{e,\text{água}}$).

Na dosimetria utilizando câmaras de ionização do tipo lápis inseridas em cavidades específicas do cilindro de PMMA, a dose absorvida no ponto central ou periférico do fantoma correlaciona-se diretamente com o cálculo do **Índice de Dose em Tomografia Computadorizada ($\text{CTDI}$)**. O $\text{CTDI}_{100}$ é matematicamente definido como:

$$
\text{CTDI}_{100} = \frac{1}{nT} \int_{-50\,\mathrm{mm}}^{+50\,\mathrm{mm}} D(z) \, dz
$$

Onde:
- $n$ é o número de cortes tomográficos adquiridos simultaneamente por rotação.
- $T$ é a espessura nominal de cada corte no eixo $z$ ($mm$).
- $D(z)$ é o perfil de dose absorvida ao longo do eixo longitudinal $z$ no interior do fantoma de PMMA.

A partir das medições periféricas ($\text{CTDI}_{\text{periférico}}$) e centrais ($\text{CTDI}_{\text{central}}$), calcula-se o **$\text{CTDI}_{\text{w}}$** (ponderado) e o **$\text{CTDI}_{\text{vol}}$** (volumétrico), fundamentais para a gestão de dose clínica:

$$
\text{CTDI}_{\text{w}} = \frac{1}{3} \text{CTDI}_{\text{central}} + \frac{2}{3} \text{CTDI}_{\text{periférico}}
\text{CTDI}_{\text{vol}} = \frac{\text{CTDI}_{\text{w}}}{\text{pitch}}
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Os fantomas de PMMA constituem o pilar metrológico para a validação operacional e o cumprimento de marcos regulatórios em sistemas de TC modernos, impactando diretamente as seguintes frentes:

1. **Controle de Qualidade (CQ) de Imagem:** Utilizados para avaliar métricas cruciais de desempenho do sistema, tais como:
   - **Ruído da imagem e Uniformidade:** Medindo o desvio padrão e a variação espacial das Unidades Hounsfield ($\text{HU}$) nas regiões central e periférica do cilindro de PMMA.
   - **Linearidade do Número de Tomografia:** Validação da resposta em $\text{HU}$ para diferentes materiais embutidos no fantoma (ex: Teflon, ar, polietileno, água, osso cortical sintético).
   - **Resolução Espacial de Alto e Baixo Contraste:** Uso de padrões internos de malhas de arame, barras ou furos para testar a função de transferência de modulação (MTF) e a detectabilidade de objetos de baixo contraste.

2. **Dosimetria e Otimização de Protocolos:** Os cilindros de PMMA de 16 cm (cabeça) e 32 cm (corpo) são obrigatórios nos testes de aceitação e comissionamento de novos tomógrafos, permitindo estimar a carga de radiação entregue ao paciente. A otimização de parâmetros como $\text{kVp}$, corrente do tubo de raios X baseada em modulação angular e longitudinal ($\text{mA}$ modulado), e espessura de corte é balizada utilizando leituras padronizadas obtidas nestes fantomas.

3. **Validação de Algoritmos de Reconstrução Avançados:** Com a ascensão da Retroprojeção Filtrada ($\text{FBP}$), reconstrução iterativa ($\text{IR}$) e reconstruções baseadas em Inteligência Artificial / Deep Learning ($\text{DLR}$), o fantoma de PMMA fornece o meio homogêneo e heterogêneo controlado para testar a supressão de ruído sem perda de resolução espacial, artefatos de enrijecimento de feixe (*beam hardening*) e distorções de textura de ruído introduzidas por redes neurais profundas.

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|tomografia-computadorizada]]
- [[Unidades Hounsfield|unidades-hounsfield]]
- [[Métricas de Dose em TC|ctdi]]
- [[Dose Absorvida|dose-absorvida]]
- [[Espalhamento Compton|espalhamento-compton]]
- [[Controle de Qualidade em TC|controle-de-qualidade-em-tc]]
- [[Retroprojeção Filtrada (FBP)|retroprojecao-filtrada]]
- [[Reconstrução Iterativa|reconstrucao-iterativa]]
- [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction]]
- [[atenuacao-de-raios-x]]
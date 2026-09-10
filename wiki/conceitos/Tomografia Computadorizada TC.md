---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, radiologia-diagnostica, reconstrucao-de-imagem\, dosimetria]
data: 2026-08-25
---

# tomografia computadorizada (TC)

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A Tomografia Computadorizada (TC) é uma modalidade de imagem médica diagnóstica que utiliza radiação ionizante (raios X) transmitida para gerar mapas tridimensionais (volumétricos) dos coeficientes de atenuação linear de tecidos biológicos. Diferentemente da radiografia convencional, na qual a informação espacial tridimensional é colapsada em uma única projeção planar bidimensional gerando sobreposição anatómica, a TC fundamenta-se na aquisição de múltiplas projeções angulares ao redor do paciente. 

Do ponto de vista físico, o feixe de raios X policromático gerado por um tubo de raios X interage com a matéria primariamente através do Efeito Fotoelétrico e do Espalhamento Compton. A intensidade da radiação transmitida $I$ através de um meio heterogêneo ao longo de uma linha reta (caminho de integração ou linha de projeção) é governada pela Lei de Atenuação de Beer-Lambert:

$$
I = I_0 \exp\left( -\int \mu(x, y) \, ds \right)
$$

Onde $I_0$ é a intensidade do feixe incidente, $ds$ é o elemento diferencial de comprimento ao longo da trajetória do raio, e $\mu(x,y)$ é o coeficiente de atenuação linear espacialmente variante (expresso em $\text{cm}^{-1}$), que depende da densidade mássica do tecido\, do número atômico efetivo ($Z_{eff}$) e da energia dos fótons incidentes.

Metrologicamente, os valores brutos de atenuação são convertidos em uma escala normalizada e independente da máquina conhecida como **Unidades Hounsfield (HU)** ou Número de Tomografia. A calibração é estabelecida tendo a água destilada e o ar sob condições padrão como referências fundamentais:

$$
\text{HU} = 1000 \times \frac{\mu - \mu_{\text{água}}}{\mu_{\text{água}} - \mu_{\text{ar}}}
$$

Onde $\mu_{\text{ar}}$ é tipicamente considerado igual a $0 \text{ cm}^{-1}$ e $\mu_{\text{água}}$ define o ponto zero da escala, enquanto o osso denso e o ar ocupam os extremos superiores e inferiores, respectivamente.

---

## 2. Formulação Matemática e Propriedades (se aplicável)

A reconstrução de imagem em TC baseia-se na resolução matemática do problema inverso de recuperar a função bivariada $\mu(x,y)$ a partir de suas integrais de linha (projeções). Esse conjunto de projeções em múltiplos ângulos $\theta$ constitui a **Transformada de Radon**, formalmente definida como:

$$
P_\theta(t) = \mathcal{R}\{\mu(x,y)\} = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \mu(x,y) \, \delta(x \cos\theta + y \sin\theta - t) \, dx \, dy
$$

Onde $t$ representa a distância do detector ao isocentro do pórtico (coordenada do detector) e $\delta$ é a função delta de Dirac. As varreduras completas coletam $P_\theta(t)$ para $\theta \in [0, \pi]$ (ou $[0, 2\pi]$ em geometrias em leque).

O método analítico clássico para inverter a Transformada de Radon é a **Retroprojeção Filtrada (FBP - *Filtered Backprojection*)**\, derivada do Teorema da Fatia Central (*Central Slice Theorem*). O teorema estabelece que a transformada de Fourier unidimensional de uma projeção paralela $P_\theta(t)$ é igual à secção bidimensional da transformada de Fourier bidimensional da função $\mu(x,y)$ ao longo de uma linha inclinada pelo ângulo $\theta$.

A equação fundamental da FBP é formulada como:

$$
\mu(x,y) = \int_{0}^{\pi} \left[ P_\theta(t) * k(t) \right]_{t = x\cos\theta + y\sin\theta} \, d\theta
$$

Onde $*$ denota a operação de convolução, e $k(t)$ é o núcleo de filtro (*kernel*) rampa no domínio espacial (ou $|
u|$no domínio de Fourier, onde$
u$é a frequência espacial). O filtro rampa é essencial para compensar o desfoque inerente da retroprojeção simples ($\frac{1}{r}$), embora amplifique o ruído de alta frequência, exigindo frequentemente a aplicação de janelamentos suavizadores (Hamming, Hann, Shepp-Logan).

Em sistemas modernos, algoritmos de **Reconstrução Iterativa (IR)** e **Reconstrução Baseada em Aprendizado Profundo (DLR - *Deep Learning Reconstruction*)** substituem ou complementam a FBP. A otimização iterativa minimiza uma função custo regularizada da forma:

$$
\hat{\mu} = \arg\min_{\mu} \left\{ \frac{1}{2} \| \mathbf{y} - \mathcal{A}\mu \|_2^2 + \lambda \mathcal{R}(\mu) \right\}
$$

Onde $\mathbf{y}$ representa os dados de projeção ruidosos, $\mathcal{A}$ é o operador do sistema de varredura (matriz de projeção avistada), $\mathcal{R}(\mu)$ é um termo de regularização espacial (como variação total - *Total Variation*) para supressão de ruído preservando bordas, e $\lambda$ é o parâmetro de regularização.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A TC ocupa um papel central na medicina moderna de precisão, abrangendo desde o diagnóstico oncológico e estadiamento até a angiografia avançada, perfusão cerebral, medicina de urgência e planejamento de radioterapia. Com o advento da TC de dupla energia (*Dual-Energy CT - DECT*) e contagem de fótons (*Photon-Counting Detector CT - PCD-CT*), a modalidade evoluiu de puramente anatômica para funcional e quantitativa.

No entanto\, devido ao uso de radiação ionizante, a otimização dos protocolos é um imperativo ético e físico-médico, regido pelo princípio ALARA (*As Low As Reasonably Achievable*). A gestão de dose envolve métricas dosimétricas padronizadas:

*   **CTDIvol (Índice de Dose de Tomografia Computadorizada Volumétrica):** Medida da intensidade de radiação emitida em um volume escaneado, expresso em miliGrays (mGy), medido em fantomas acrílicos normalizados de 16 cm (cabeça) ou 32 cm (abdome).
*   **DLP (Produto Dose-Comprimento):** O produto do $\text{CTDI}_{\text{vol}}$ pelo comprimento total da varredura ($L$), expressa em $\text{mGy}\cdot\text{cm}$, correlacionando-se diretamente com a energia estocástica total depositada.

A otimização contemporânea baseia-se na modulação automática de corrente do tubo (*Automatic Tube Current Modulation - ATCM*), filtragem de espectro com estanho (*tin filtration*), algoritmos avançados de DLR que permitem reduções drásticas de dose sem perda de detectabilidade de lesões de baixo contraste, e no uso rigoroso de **Observadores Computacionais** (como o Observador de Modelos Humanos e a Matriz de Cúmulo de Canais - *Channelized Hotelling Observer*) para avaliar a qualidade de imagem baseada em tarefas de forma objetiva, mitigando vieses da percepção visual humana.

---

## 4. Conexões e Wikilinks

*   [[Reconstrução de Imagem|reconstrucao-de-imagem]]
*   [[Retroprojeção Filtrada (FBP)|retroprojecao-filtrada-fbp]]
*   [[Reconstrução Iterativa|reconstrucao-iterativa]]
*   [[Deep Learning Image Reconstruction (DLR)|inteligencia-artificial-em-tc]]
*   [[Dosimetria em TC|dosimetria-em-tc]]
*   [[ctdivol-e-dlp]]
*   [[Unidades Hounsfield|unidades-hounsfield]]
*   [[Qualidade de Imagem em TC|qualidade-de-imagem-em-tc]]
*   [[Tomografia Computadorizada Espectral|tomografia-de-dupla-energia]]
*   [[detectores-de-contagem-de-foton]]
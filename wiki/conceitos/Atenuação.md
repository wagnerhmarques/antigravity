---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, radiologia, interacao-da-radiacao, reconstrucao-de-imagem]
data: 2026-08-25
---

# atenuacao

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **atenuação** é o processo físico fundamental pelo qual a intensidade de um feixe de radiação ionizante (especificamente fótons de raios X ou gama) diminui à medida que ele propaga-se e interage com a matéria. Na Tomografia Computadorizada (TC) e na radiologia diagnóstica, a atenuação é o fenômeno primário que codifica a informação anatômica e patológica dos tecidos biológicos em sinais mensuráveis pelos detectores.

Macroscopicamente, a atenuação resulta da combinação de dois efeitos principais de interação fóton-matéria nas energias diagnósticas (tipicamente de 20 a 140 keV):
1. **Efeito Fotoelétrico:** O fóton incidente transfere toda a sua energia para um elétron ligado (geralmente das camadas mais internas, como K ou L), ejectando-o do átomo. Sua probabilidade de ocorrência é fortemente dependente do número atômico efetivo ($Z_{ef}$) do meio e inversamente proporcional ao cubo da energia do fóton ($\propto Z_{ef}^3 / E^3$). É o principal mecanismo responsável pelo contraste tecidual em baixas energias (ex: osso versus tecido mole).
2. **Espalhamento Compton (Inelástico):** O fóton interage com um elétron fracamente ligado ou livre, transferindo parte de sua energia para o elétron de recuo e sendo espalhado em um ângulo $\theta$ com energia reduzida. A probabilidade de interação Compton depende quase linearmente da densidade eletrônica do meio ($\rho_e$, número de elétrons por unidade de massa) e é fracamente dependente de $Z$. Predomina em energias intermediárias e altas.

O espalhamento coerente (Rayleigh) e a produção de pares (relevante apenas para energias $> 1.022 \text{ MeV}$) possuem contribuições desprezíveis ou nulas na faixa de energia da TC convencional. Metrologicamente, a atenuação é quantificada pelo coeficiente de atenuação linear ($\mu$), expresso em unidades de $\text{cm}^{-1}$, que representa a probabilidade de interação por unidade de comprimento percorrida pelo fóton.

---

## 2. Formulação Matemática e Propriedades

Para um feixe monoenergético de fótons incidindo sobre um meio homogêneo com espessura $x$, a variação da intensidade do feixe $I$ em função da distância percorrida é governada pela Lei de Beer-Lambert:

$$
\frac{dI(x)}{dx} = -\mu I(x)
$$

Integrando esta equação diferencial ordinária de primeira ordem para um caminho homogêneo de espessura $L$, obtém-se a forma exponencial clássica:

$$
I(L) = I_0 \exp\left( -\mu L \right)
$$

Onde:
- $I_0$ é a intensidade (ou fluxo) do feixe incidente ($x = 0$).
- $I(L)$ é a intensidade transmitida após atravessar a espessura $L$.
- $\mu$ é o coeficiente de atenuação linear ($\text{cm}^{-1}$).

Quando o meio é heterogêneo — cenário real encontrado na varredura de um paciente em TC —, o coeficiente de atenuação varia espacialmente ao longo da trajetória do raio $L$, denotado por $\mu(x, y)$. A intensidade transmitida é descrita pela integral de linha:

$$
I = I_0 \exp\left( -\int_{L} \mu(x, y) \, dl \right)
$$

Aplicando a transformação logarítmica, define-se a projeção ou medida de atenuação total (também conhecida como linha de projeção ou *sinogram value* $P$):

$$
P = \ln\left( \frac{I_0}{I} \right) = \int_{L} \mu(x, y) \, dl
$$

### O Fenômeno do *Beam Hardening* (Enrijecimento do Feixe)
Na prática clínica, os tubos de raios X geram um espectro policromático de fótons. Como a probabilidade de atenuação ($\mu$) é altamente dependente da energia ($E$), os fótons de menor energia (mais brandos) são preferencialmente absorvidos ao atravessarem as primeiras camadas do objeto (como o crânio ou os ombros), enquanto os fótons de maior energia (mais duros) atravessam com maior facilidade. 

Consequentemente, o feixe torna-se "mais duro" (sua energia média efetiva aumenta) à medida que penetra na matéria. A atenuação policromática deixa de seguir estritamente a lei exponencial simples, gerando artefatos de imagem se não corrigida algoritmicamente:

$$
I_{poli}(L) = \int_{0}^{E_{\max}} I_0(E) \exp\left( -\mu(E) L \right) dE
$$

### Coeficiente de Atenuação Mássica e Número CT
Para normalizar a densidade física, utiliza-se o **coeficiente de atenuação massica** ($\frac{\mu}{\rho}$, em $\text{cm}^2/\text{g}$), onde $\rho$ é a densidade física do meio.

Na TC, os valores de $\mu$ reconstruídos são convertidos em uma escala padronizada e adimensional chamada **Número CT** ou **Unidade Hounsfield (HU)**:

$$
\text{HU} = 1000 \times \frac{\mu - \mu_{agua}}{\mu_{agua} - \mu_{ar}}
$$

Onde $\mu_{agua}$ e $\mu_{ar}$ são os coeficientes de atenuação linear da água e do ar, respectivamente, sob condições padronizadas de calibração do tomógrafo.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A atenuação está no centro de todo o pipeline de aquisição, processamento e controle de qualidade em Tomografia Computadorizada:

* **Reconstrução de Imagem:** Algoritmos de Retroprojeção Filtrada (FBP) e métodos iterativos (IR) baseiam-se na solução matemática da equação integral de linha descrita na Seção 2. O objetivo fundamental da varredura tomográfica é resolver o problema inverso para reconstrução da matriz bidimensional ou tridimensional de $\mu(x, y)$ a partir de múltiplos projeções (sinograma).
* **Correção de *Beam Hardening* (BHC):** Como a modelagem matemática padrão assume feixes monoenergéticos, variações na atenuação espectral causam artefatos de "copo de cerveja" (*cupping artifact*) e bandas escuras. Softwares modernos aplicam correções baseadas em polinômios pré-calculados ou decomposição de materiais base (água/osso) para linearizar as projeções antes da reconstrução.
* **Dosimetria e Atenuação Específica do Paciente:** O cálculo de dose absorvida ($D$, em Gray) depende criticamente de mapas de atenuação derivados de imagens de TC (através da conversão de HU para densidade eletrônica e número atômico efetivo). Sistemas de planejamento radioterápico (TPS) utilizam tabelas de calibração de atenuação para prever a deposição de dose em tecidos tumorais e sadios.
* **Inteligência Artificial e DLR (*Deep Learning Reconstruction*):** Redes neurais profundas são treinadas para mitigar ruídos e artefatos em imagens de baixa dose, onde a incerteza estatística na medição da atenuação (devido ao baixo número fótons detectados, gerando ruído quântico) degrada severamente a qualidade diagnóstica.

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|tomografia-computadorizada]]
- [[Coeficiente de Atenuação Linear|coeficiente-de-atenuacao-linear]]
- [[Unidades Hounsfield|unidade-hounsfield]]
- [[Efeito Fotoelétrico|efeito-fotoelectrico]]
- [[Espalhamento Compton|espalhamento-compton]]
- [[Beam Hardening|beam-hardening]]
- [[lei-de-beer-lambert]]
- [[Reconstrução de Imagem|reconstrucao-de-imagem]]
- [[retroprojetor-filtrado]]
- [[Dosimetria em TC|dosimetria-em-tc]]
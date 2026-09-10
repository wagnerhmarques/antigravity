---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, correcao-de-atenuacao, correcao-de-espalhamento, reconstrucao-de-imagem, inteligencia-artificial]
data: 2026-08-25
---

# Correção de Atenuação e Espalhamento

## 1. Definição Conceitual e Fundamentação Física / Metrológica

No contexto da Tomografia Computadorizada (TC) quantitativa e da imagem híbrida (como SPECT/CT e PET/CT), a **Correção de Atenuação e Espalhamento** constitui o conjunto de processos físicos e computacionais essenciais para mitigar artefatos e imprecisões radiométricas causados pela interação da radiação X com a matéria. 

A atenuação primária da radiação ao atravessar um meio heterogêneo é descrita pela Lei de Beer-Lambert ideal para feixes monoenergéticos. Contudo, feixes de raios X de TC são **policromáticos**, o que induz o fenômeno de *beam hardening* (endurecimento do feixe), onde os fótons de baixa energia são preferencialmente absorvidos, deslocando o espectro médio para energias mais altas à medida que o feixe penetra no objeto. Do ponto de vista metrológico, se não corrigido, isso gera artefatos em forma de "copo de cerveja" (*cupping artifacts*) e bandas escuras entre estruturas densas (como ossos ou próteses metálicas), comprometendo a exatidão dos números de Hounsfield (HU).

O **espalhamento Compton** e, em menor escala, a dispersão coerente (Rayleigh), representam fótons que desviaram de sua trajetória retilínea original ao interagir com elétrons orbitais. Quando esses fótons espalhados atingem os detectores, são erroneamente atribuídos ao feixe primário correspondente à linha de projeção geométrica. Isso resulta em uma perda de contraste global na imagem, subestimação dos coeficientes de atenuação linear ($\mu$), formação de artefatos de sombreamento (*shading*) e degradação severa da relação contraste-ruído (CNR).

A metrologia em TC exige que os valores de pixels sejam quantitativamente fiéis aos coeficientes de atenuação linear reais. Portanto, algoritmos avançados de correção modelam a física da interação fóton-matéria — incluindo a deconvolução de núcleos de espalhamento (*scatter kernels*), simulações baseadas em Monte Carlo aceleradas por hardware, e modelagem espectral iterativa — para isolar o sinal primário puro antes da reconstrução tomográfica.

---

## 2. Formulação Matemática e Propriedades

A aquisição de um projeção em TC sem espalhamento e com atenuação ideal é modelada pela integral de linha do coeficiente de atenuação linear $\mu(x,y,E)$ ao longo do caminho do raio $L$:

$$
I(E) = I_0(E) \exp \left( - \int_L \mu(x,y,E) \, dl \right)
$$

No entanto, o sinal medido no detector $I_{\text{medido}}(E)$ inclui a contribuição do componente de espalhamento $S(E)$:

$$
I_{\text{medido}}(E) = I_{\text{primario}}(E) + S(E) = I_0(E) \exp \left( - \int_L \mu(x,y,E) \, dl \right) + \iint \Psi(x,y,E', \theta) \, dx \, dy
$$

Onde $\Psi$ representa a densidade de fluxo de fótons espalhados em função da posição espacial e do ângulo de deflexão $\theta$.

Para a correção do espalhamento, define-se a fração de espalhamento (*Scatter-to-Primary Ratio*, $SPR$):

$$
SPR(u, v) = \frac{S(u, v)}{I_{\text{primario}}(u, v)}
$$

Onde $(u, v)$ representam as coordenadas espaciais no plano do painel detector. O sinal corrigido das projeções $P_{\text{corr}}(u, v)$ é obtido subtraindo-se a estimativa de espalhamento $\hat{S}(u, v)$ do perfil bruto de projeção $P_{\text{bruto}}(u, v)$:

$$
P_{\text{corr}}(u, v) = -\ln \left( \frac{I_{\text{medido}}(u, v) - \hat{S}(u, v)}{I_0(u, v)} \right)
$$

No que se refere ao endurecimento do feixe, a correção linearizada para um feixe policromático com espectro de energia $Φ(E)$ é formulada mapeando a projeção medida não-linear para uma espessura equivalente de um material de referência (geralmente água, $d_{\text{água}}$) através de uma função polinomial de calibração $C(p)$:

$$
\mu_{\text{efetiva}} \cdot L = C(p) = a_0 + a_1 p + a_2 p^2 + a_3 p^3
$$

Onde $p = -\ln(I/I_0)$ é a projeção bruta, e os coeficientes $\left\{ a_0, a_1, a_2, a_3 \right\}$ são determinados empiricamente a partir de varizes de manequins de calibração de tamanhos conhecidos (*water cylinders*).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A aplicação rigorosa da Correção de Atenuação e Espalhamento (CAS) é vital em múltiplos domínios da física médica moderna:

* **Reconstrução Iterativa (IR) e Aprendizagem Profunda (DLR):** Algoritmos modernos de reconstrução baseadosModelos Físicos Avançados (MBIR) incorporam a matriz do sistema que simula o espalhamento e a polocromaticidade diretamente na função de custo. Redes Neurais Profundas (Deep Learning) são atualmente treinadas para estimar mapas de espalhamento de alta fidelidade em tempo real a partir de dados brutos (*sinogramas*) ou imagens preliminares, superando as limitações de velocidade dos métodos analíticos tradicionais.
* **Tomografia Quantitativa e Imagem Híbrida (PET/CT e SPECT/CT):** Em PET/CT, o mapa de atenuação derivado da TC ($\mu$-map) é convertido para a energia de 511 keV do aniquilamento pósitron-elétron. Erros na correção de atenuação na TC propagam-se diretamente como erros quantitativos graves na quantificação do SUV (*Standardized Uptake Value*) no PET, afetando o diagnóstico oncológico e o monitoramento de resposta terapêutica.
* **Dosimetria Computacional e Observadores:** Na avaliação de dose em órgãos e no uso de simuladores baseados em fantomas antropomórficos virtuais (*mathematical and voxelized phantoms*), a remoção de artefatos de feixe e espalhamento garante que o cálculo de dose via Monte Carlo seja acoplado a mapas de densidade eletrônica precisos.
* **Controle de Qualidade (CQ):** Protocolos de CQ metrológica utilizam manequins padronizados (como o ACR ou cateteres de teste) para auditar a linearidade dos números de Hounsfield e a eficácia dos algoritmos proprietários dos fabricantes na eliminação de artefatos de espalhamento em pacientes obesos ou regiões de alta atenuação (ombros, cavidade pélvica).

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[Reconstrução de Imagem]]
* [[Filtro de retroprojeção (FBP)]]
* [[Reconstrução Iterativa|Reconstrução Iterativa (IR)]]
* [[Inteligencia Artificial IA|Inteligência Artificial em Imagem Médica]]
* [[Artefatos em Tomografia Computadorizada]]
* [[Dosimetria em Radiologia]]
* [[Física das Radiações]]
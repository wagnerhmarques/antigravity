---
tipo: tecnologia
tags: [fisica-medica, ressonancia-magnetica, fisica-nuclear, aquisicao-de-imagem, inteligencia-artificial]
data: 2026-08-25
---

# Ressonancia Magnetica (MRI)

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A Ressonância Magnética (MRI - *Magnetic Resonance Imaging*) é uma modalidade de diagnóstico por imagem avançada baseada nos princípios da Ressonância Magnética Nuclear (RMN). Ao contrário de modalidades que utilizam radiação ionizante (como a [[Tomografia Computadorizada|Tomografia Computadorizada]]), a MRI baseia-se na interação entre campos magnéticos intensos, ondas de rádio (radiofrequência - RF) e os momentos magnéticos intrínsecos dos núcleos atômicos presentes nos tecidos biológicos, primariamente o próton ($^{1}\text{H}$), devido à sua alta abundância natural na água e nas macromoléculas do corpo humano.

Fisicamente, o núcleo de hidrogênio possui um spin nuclear intrínseco (momento angular de spin $\vec{S}$) e, por carregar carga positiva, gera um momento magnético nuclear $\vec{\mu}$:

$$
\vec{\mu} = \gamma \vec{S}
$$

onde $\gamma$ é a razão giromagnética específica do núcleo (para o próton, $\gamma / 2\pi \approx 42.58 \, \text{MHz/T}$).

Quando submetidos a um campo magnético estático externo homogêneo ($B_0$, medido em Tesla), os spins nucleares tendem a se alinhar (paralela ou antiparalelamente) a esse campo, gerando uma magnetização macroscópica líquida $\vec{M}_0$ paralela ao eixo $z$. 

A aplicação de um pulso de radiofrequência na frequência de ressonância exata (frequência de Larmor, $\omega_0 = \gamma B_0$) perturba esse sistema, desviando $\vec{M}_0$ para o plano transversal ($xy$). A equação fundamental da frequência de Larmor é dada por:

$$
\omega_0 = \gamma B_0
$$

O sinal detectável (EID - *Free Induction Decay* ou eco) surge da precessão dessa magnetização transversal líquida ao redor do eixo longitudinal, induzindo corrente elétrica nas bobinas receptoras de RF de acordo com a Lei da Indução de Faraday.

A espacialização do sinal para a formação de imagens tridimensionais é obtida através da superposição de campos magnéticos gradientes lineares ($G_x, G_y, G_z$) sobre o campo principal $B_0$. Isso torna o campo magnético dependente da posição espacial $\vec{r} = (x, y, z)$, modulando linearmente a frequência de precessão local:

$$
\omega(\vec{r}) = \gamma \left( B_0 + \vec{G} \cdot \vec{r} \right)
$$

O sinal coletado no domínio espacial recíproco, conhecido como **espaço $k$**, representa a transformada de Fourier bidimensional ou tridimensional da distribuição espacial da magnetização do objeto.

---

## 2. Formulação Matemática e Propriedades (se aplicável)

A evolução temporal da magnetização macroscópica $\vec{M}(t) = (M_x, M_y, M_z)$ sob a influência de um campo magnético efetivo é descrita fenomenologicamente pelas **Equações de Bloch**:

$$
\frac{d\vec{M}}{dt} = \gamma \left( \vec{M} \times \vec{B} \right) - \frac{M_x \hat{i} + M_y \hat{j}}{T_2} - \frac{(M_z - M_0)\hat{k}}{T_1}
$$

Onde:
- $\vec{B} = B_x(t)\hat{i} + B_y(t)\hat{j} + (B_0 + G_z z)\hat{k}$ é o campo magnético total.
- $T_1$ é a constante de tempo de relaxação spin-rede (longitudinal).
- $T_2$ é a constante de tempo de relaxação spin-spin (transversal).

A solução para a recuperação longitudinal ($M_z$) após um pulso de inversão ($180^\circ$) ou saturação é modelada por:

$$
M_z(t) = M_0 \left( 1 - 2 e^{-\frac{t}{T_1}} \right) \quad \text{(para inversão-recuperação)}
$$

Enquanto o decaimento da componente transversal ($M_{xy}$) é dado por:

$$
M_{xy}(t) = M_{xy}(0) e^{-\frac{t}{T_2^*}}
$$

Onde $T_2^*$ engloba o tempo de relaxação intrínseco $T_2$ e as inomogeneidades do campo magnético principal, expressas pela taxa $\Delta B_0$:

$$
\frac{1}{T_2^*} = \frac{1}{T_2} + \gamma \Delta B_0
$$

O sinal bruto medido no espaço $k$, denotado por $S(k_x, k_y)$, relaciona-se à densidade de prótons ponderada pelas características de relaxação $m(x,y)$ através da transformada de Fourier:

$$
S(k_x, k_y) = \iint_{-\infty}^{\infty} m(x,y) \exp\left( -i 2\pi (k_x x + k_y y) \right) dx \, dy
$$

A imagem final reconstruída $I(x,y)$ é obtida aplicando-se a Transformada de Fourier Inversa (IFT) discreta sobre os dados amostrados do espaço $k$:

$$
I(x,y) = \mathcal{F}^{-1} \left\{ S(k_x, k_y) \right\}
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Embora a Ressonância Magnética e a Tomografia Computadorizada (TC) sejam modalidades anatômicas distintas, os conceitos de processamento de sinal, reconstrução de imagem e otimização computacional convergem fortemente na prática clínica e na pesquisa avançada em física médica:

1. **Reconstrução de Imagem e Aceleração:** Paralelamente aos algoritmos iterativos e de Aprendizado Profundo (*Deep Learning Reconstruction* - DLR) utilizados na otimização de doses e redução de artefatos na [[Tomografia Computadorizada|Tomografia Computadorizada]], a MRI moderna utiliza técnicas avançadas como amostragem comprimida (*Compressed Sensing*) e reconstruções paralelas (SENSE, GRAPPA). Estas técnicas reduzem drasticamente o tempo de aquisição do espaço $k$, mitigando artefatos de movimento.
2. **Fusão Multimodal e Corregistro:** Na oncologia radioterápica e no planejamento cirúrgico, a sinergia entre MRI (alta resolução de partes moles) e TC (alta acurácia geométrica e densitometria em Unidades Hounsfield) exige métodos computacionais robustos de corregistro de imagens baseados em informação mútua e redes neurais profundas.
3. **Controle de Qualidade (CQ) e Metrologia:** Protocolos rigorosos de CQ avaliam a linearidade dos gradientes, a homogeneidade do campo $B_0$ (em partes por milhão - ppm), a relação sinal-ruído (SNR) e a distorção espacial, parâmetros vitais para garantir a fidelidade geométrica comparável à obtida em sistemas de TC helicoidal.
4. **Dosimetria por Gel de Polímero:** Em física de radiações, géis baseados em polímeros e sensíveis à radiação mudam suas taxas de relaxação $T_2$ após a irradiação. A MRI é utilizada como ferramenta dosimétrica tridimensional para validar distribuições complexas de dose em radioterapia de intensidade modulada (IMRT), conectando diretamente a física da MRI com a dosimetria clínica avançada.

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|Tomografia Computadorizada]]
- [[Processamento de Imagem Médica]]
- [[Inteligencia Artificial IA|Inteligencia Artificial em Radiologia]]
- [[Dosimetria de Radiacao]]
- [[Física Nuclear Aplicada]]
---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, radiologia, interacao-da-radiacao, metrologia-das-radiacoes]
data: 2026-08-25
---

# atenuacao-dos-raios-x

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A atenuação dos raios-X refere-se ao decréscimo na intensidade de um feixe de fótons de raios-X ao interagir com a matéria (meio material), seja por processos de absorção (onde a energia do fóton é transferida integralmente para os elétrons do meio) ou por espalhamento (onde o fóton tem sua trajetória desviada e, frequentemente, sua energia reduzida). Do ponto de vista metrológico e radiológico, a atenuação é o fenômeno fundamental que viabiliza a formação de imagens em [[Tomografia Computadorizada|tomografia-computadorizada]] e radiologia diagnóstica, pois traduz as variações de densidade eletrônica, número atômico efetivo ($Z_{eff}$) e espessura anatômica em contrastes espaciais de intensidade de radiação.

Macroscopicamente, a atenuação de um feixe primário, monoenergético, colimado e perpendicular à superfície de um meio homogêneo é descrita pela **Lei de Lambert-Beer**. Quando o feixe penetra no material, a probabilidade de interação por unidade de comprimento percorrido é expressa pelo **coeficiente de atenuação linear** ($\mu$), medido em $\text{cm}^{-1}$. 

Em energias típicas de diagnóstico médico (20 a 150 $\text{keV}$), os mecanismos microscópicos dominantes de interação dos fótons de raios-X com os átomos do meio são:
1. **Efeito Fotoelétrico**: Predominante em energias mais baixas e em meios com alto número atômico ($Z$). O fóton incidente cede toda a sua energia a um elétron orbital (geralmente das camadas mais internas, como K ou L), que é ejectado como um fotoelétron. A seção de parede deste processo é fortemente dependente do número atômico ($\approx Z^3$ a $Z^4$) e inversamente proporcional à energia cúbica do fóton ($\approx E^{-3}$).
2. **Espalhamento Compton (Inelástico)**: Predominante em energias intermediárias a altas e em materiais de baixo número atômico (como tecidos moles e água). Ocorre a colisão elástica/inelástica entre o fóton e um elétron fracamente ligado (ou livre), resultando na ejeção do elétron e no desvio do fóton espalhado com menor energia. A probabilidade deste evento é proporcional à densidade eletrônica ($e^-/\text{cm}^3$) do meio e fracamente dependente de $Z$.
3. **Produção de Pares**: Relevante apenas em energias superiores a $1,022\text{ MeV}$, portanto ausente na faixa diagnóstica padrão, mas presente na física de altas energias e na tomografia por emissão de pósitrons ([[Tomografia por Emissão de Pósitrons (PET)|pet-ct]]).

---

## 2. Formulação Matemática e Propriedades

Para um feixe monoenergético ideal de raios-X, a variação infinitesimal da intensidade do feixe ($\Delta I$ ou $dI$) ao atravessar uma espessura infinitesimal $dx$ de um material é proporcional à intensidade local $I(x)$ e ao coeficiente de atenuação linear $\mu$:

$$
dI(x) = -\mu \, I(x) \, dx
$$

Integrando esta equação diferencial ordinária de primeira ordem ao longo de um caminho linear espessado de $0$ até $x$, obtém-se a forma analítica da Lei de Lambert-Beer:

$$
I(x) = I_0 \, e^{-\int_{0}^{x} \mu(x') \, dx'}
$$

Para um meio perfeitamente homogêneo de espessura $L$, a equação reduz-se a:

$$
I = I_0 \, e^{-\mu L}
$$

Onde:
- $I_0$ é a intensidade (ou fluxo de fótons) incidente.
- $I$ é a intensidade transmitida após atravessar a espessura $L$.
- $\mu$ é o coeficiente de atenuação linear ($\text{cm}^{-1}$).

Como o coeficiente de atenuação linear $\mu$ depende diretamente da densidade física do meio ($\rho$, em $\text{g/cm}^3$), é frequentemente útil normalizar a atenuação em relação à massa, definindo o **coeficiente de atenuação massa** ($\mu_m$):

$$
\mu_m = \frac{\mu}{\rho} \quad \left[\text{cm}^2/\text{g}\right]
$$

Desta forma, a lei de atenuação pode ser reescrita utilizando a espessura mássica ($x_m = \rho L$):

$$
I = I_0 \, e^{-(\mu_m) (\rho L)}
$$

### Feixes Policromáticos e "Beam Hardening"

Na prática clínica, os tubos de raios-X geram feixes **policromáticos** (compostos por um espectro contínuo de energias até o potencial máximo do tubo, $kVp$). Como o coeficiente de atenuação $\mu(E)$ diminui acentuadamente com o aumento da energia do fóton ($E$), os fótons de menor energia (mais "moles") são preferencialmente absorvidos nas camadas mais superficiais do objeto em comparação aos fótons de maior energia (mais "duros").

Isso resulta no fenômeno de **endurecimento do feixe** (*beam hardening*), onde o espectro médio do feixe se desloca para energias mais altas à medida que penetra na matéria. Consequentemente, a atenuação em feixes policromáticos não segue estritamente uma exponencial simples. A intensidade transmitida através de um absorvedor policromático de espessura $L$ é modelada por uma integral sobre o espectro energético $N(E)$:

$$
I(L) = \int_{0}^{E_{\max}} N_0(E) \, e^{-\mu(E) L} \, dE
$$

Este comportamento não-linear exige correções algorítmicas rigorosas na reconstrução de imagem tomográfica para evitar artefatos de feixe endurecido (como sombreamentos em forma de taça ou faixas escuras entre estruturas densas).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A atenuação dos raios-X é a base operativa e o princípio físico fundamental da [[Tomografia Computadorizada|tomografia-computadorizada]]. 

1. **Reconstrução Tomográfica e Projeções**: 
   Os detectores em tomografia medem a intensidade transmitida $I$ em múltiplos ângulos ao redor do paciente. Aplicando a operação logarítmica inversa da Lei de Lambert-Beer, o sistema obtém a **soma de atenuações lineares** (as projeções ou *sinogramas*):
   
   
$$
P = -\ln\left(\frac{I}{I_0}\right) = \int_{L} \mu(x,y) \, dl
$$

   
   Algoritmos de retroprojeção, como a [[Retroprojeção Filtrada (FBP)|retroprojecao-filtrada]] (FBP), bem como métodos iterativos ([[Reconstrução Iterativa|iterative-reconstruction]]) e algoritmos baseados em aprendizado profundo ([[dlr-deep-learning-reconstruction]]), resolvem este problema matemático inverso para mapear a distribuição espacial exata de $\mu(x,y)$ em uma matriz tridimensional de voxels.

2. **Unidades Hounsfield (HU)**:
   Como os coeficientes de atenuação linear absolutos dependem da energia do feixe e da calibração do equipamento, a TC padroniza a escala de cinzas usando as **Unidades Hounsfield** (HU), definidas em relação à atenuação da água ($\mu_{agua}$) e do ar ($\mu_{ar}$):
   
   
$$
\text{HU} = 1000 \times \frac{\mu - \mu_{agua}}{\mu_{agua} - \mu_{ar}} \approx 1000 \times \frac{\mu - \mu_{agua}}{\mu_{agua}}
$$

   
   Isso atribui ao ar o valor fixo de $-1000\text{ HU}$, à água pura $0\text{ HU}$, e aos ossos densos valores que podem ultrapassar $+1000\text{ HU}$.

3. **Controle de Qualidade, Dosimetria e Otimização**:
   - No **controle de qualidade**, a avaliação da atenuação é utilizada para medir a Camada Heminredutora (HVL), garantindo a filtragem adequada do feixe e a segurança radiológica.
   - Em **dosimetria**, o conhecimento detalhado dos coeficientes de atenuação de diferentes tecidos biológicos e materiais simuladores (como água, osso e tecido adiposo equivalente) é indispensável para o cálculo de dose absorvida via algoritmos baseados em *Monte Carlo* ou equações de transporte de radiação.
   - Na **otimização de protocolos**, estratégias como a modulação de corrente do tubo (CARE Dose4D, por exemplo) ajustam a emissão de raios-X dinamicamente com base na variação da atenuação anatômica do paciente ao longo do eixo $z$, garantindo qualidade de imagem diagnóstica com a menor dose possível (princípio ALARA).

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|tomografia-computadorizada]]
- [[Retroprojeção Filtrada (FBP)|retroprojecao-filtrada]]
- [[Reconstrução Iterativa|iterative-reconstruction]]
- [[dlr-deep-learning-reconstruction]]
- [[Tomografia por Emissão de Pósitrons (PET)|pet-ct]]
- [[Qualidade de Imagem em TC|qualidade-de-imagem-em-tc]]
- [[Dosimetria em Radiologia|dosimetria-em-radiologia]]
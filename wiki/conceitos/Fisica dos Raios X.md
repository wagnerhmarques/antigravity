---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, fisica-dos-raios-x, radiodiagnostico, dosimetria, interacao-1-materia]
data: 2026-08-25
---

# fisica-dos-raios-x

## 1. Definição Conceitual e Fundamentação Física / Metrológica

Os raios X são radiação eletromagnética ionizante de alta frequência e comprimento de onda curto, situando-se no espectro eletromagnético entre o ultravioleta extremo e os raios gama. No contexto da Física Médica e da Tomografia Computadorizada (TC), a geração de raios X ocorre fundamentalmente pela conversão de energia cinética de elétrons acelerados em fótons através de interações com o campo eletromagnético nuclear e atômico no interior de um tubo de raios X.

O processo físico de produção envolve um cátodo (filamento de tungstênio) que, quando submetido a uma corrente elétrica, emite elétrons por efeito termiônico. Esses elétrons são acelerados em direção a um ânodo (alvo metálico, tipicamente de liga de tungstênio com rênio) sob uma diferença de potencial elevada ($V$, expressa em quilovolts pico - $\text{kVp}$). Ao incidirem no ânodo, os elétrons sofrem desaceleração abrupta, resultando em dois mecanismos principais de emissão de raios X:

1. **Radiação de Frenamento (Bremsstrahlung):** É o mecanismo predominante no diagnóstico médico. Quando um elétron incidente penetra na eletrosfera e se aproxima do núcleo atômico do material do ânodo, o forte campo eletromagnético nuclear desvia sua trajetória e causa sua desaceleração. A perda de energia cinética ($\Delta E$) é emitida sob a forma de um fóton de raio X. Como a distância de aproximação ao núcleo varia continuamente, o espectro resultante é policromático (contínuo), estendendo-se desde energias próximas a zero até uma energia máxima estipulada pela energia cinética total do elétron ($E_{\text{max}} = e V$).
2. **Radiação Característica:** Ocorre quando um elétron incidente colide com um elétron das camadas mais internas (camada $K$ ou $L$) do átomo do ânodo, ejectando-o do átomo. O vácuo eletrônico resultante é preenchido por um elétron de uma camada externa de maior energia. A transição é acompanhada pela emissão de um fóton cuja energia corresponde exatamente à diferença de energia de ligação entre as camadas envolvidas ($\Delta E = E_{\text{externa}} - E_{\text{interna}}$). Esse processo gera linhas discretas sobrepostas ao espectro contínuo de Bremsstrahlung.

Do ponto de vista metrológico, a caracterização do feixe de raios X exige a medição precisa de grandezas como a tensão máxima do tubo ($\text{kVp}$), a corrente do tubo ($mA$), o produto corrente-tempo ($mAs$) e a **Camada Sem-Redução** (CSR ou *Half-Value Layer* - $\text{HVL}$), que define a espessura de um material atenor (usualmente alumínio ou cobre) necessária para reduzir a intensidade do feixe incidente à metade de seu valor original, servindo como indicador primordial da qualidade (dureza/energia efetiva) do feixe.

---

## 2. Formulação Matemática e Propriedades (se aplicável)

A distribuição energética do espectro de Bremsstrahlung contínuo pode ser modelada empiricamente pela **Lei de Kramers**, que expressa a intensidade da radiação emitidas por unidade de intervalo de comprimento de onda ou energia:

$$
I(\lambda) = C \cdot Z \cdot \left( \frac{\lambda}{\lambda_{\min}} - 1 \right) \frac{1}{\lambda^2}
$$

Onde:
- $C$ é uma constante de proporcionalidade.
- $Z$ é o número atômico do material do ânodo.
- $\lambda$ é o comprimento de onda do fóton.
- $\lambda_{\min}$ é o menor comprimento de onda emitido, determinado pela relação de Duane-Hunt:

$$
\lambda_{\min} = \frac{hc}{e V} \approx \frac{1.24}{\text{kVp}} \quad [\text{nm}]
$$

Sendo $h$ a constante de Planck, $c$ a velocidade da luz no vácuo e $e$ a carga elementar do elétron.

### Atenuação da Radiação na Matéria

Ao interagir com a matéria (tecidos biológicos, filtros, blindagens), a intensidade de um feixe de fótons monoenergéticos decai exponencialmente de acordo com a **Lei de Lambert-Beer**:

$$
I(x) = I_0 \, e^{-\mu x}
$$

Onde:
- $I(x)$ é a intensidade transmitida após atravessar uma espessura $x$ do meio.
- $I_0$ é a intensidade do feixe incidente.
- $\mu$ é o coeficiente de atenuação linear ($\text{cm}^{-1}$), que depende da energia do fóton ($E$), da densidade mássica ($\rho$) e do número atômico efetivo ($Z_{\text{eff}}$) do meio.

Para feixes policromáticos (como os gerados em tubos de raios X clínicos), a atenuação não é puramente exponencial, pois fótons de menor energia (mais brandos) são atenuados preferencialmente em relação aos de maior energia (mais duros), fenômeno conhecido como **Endurecimento do Feixe** (*Beam Hardening*). Nesses casos, a formulação requer a integração sobre todo o espectro de energia $\Phi(E)$:

$$
I(x) = \int_{0}^{E_{\text{max}}} \Phi_0(E) \, e^{-\mu(E)x} \, dE
$$

O coeficiente de atenuação mássica ($\mu / \rho$) é frequentemente utilizado para normalizar as variações de densidade física do meio, permitindo expressar a interação independentemente do estado físico da matéria:

$$
\left(\frac{\mu}{\rho}\right) = \left(\frac{\mu}{\rho}\right)_{\text{fotoelétrico}} + \left(\frac{\mu}{\rho}\right)_{\text{Compton}} + \left(\frac{\mu}{\rho}\right)_{\text{par}}
$$

Onde os termos representam, respectivamente, a contribuição do **Efeito Fotoelétrico** (dominante em baixas energias e altos $Z$), do **Espalhamento Compton** (dominante em energias intermediárias no diagnóstico médico) e da **Produção de Pares** (relevante apenas em energias superiores a $1.022 \text{ MeV}$, fora do escopo diagnóstico padrão).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Na Tomografia Computadorizada (TC) moderna, a física dos raios X dita tanto os limites tecnológicos do hardware quanto os desafios computacionais do pós-processamento:

* **Geometria e Aquisição:** O feixe cônico (*cone-beam*) ou em leque (*fan-beam*) atravessa o paciente sob múltiplos ângulos de projeção. Cada detector mede a atenuação integrada ao longo do trajeto dos raios X, gerando projeções brutas conhecidas como **sinogramas**.
* **Correção de Artefatos:** A natureza policromática do feixe de raios X gera artefatos de endurecimento do feixe, visualizados clinicamente como bandas escuras ou faixas (estrias) entre estruturas densas (ex: ossos ou próteses metálicas). Algoritmos de correção baseados na física da atenuação policromática são aplicados iterativamente ou no pré-processamento para linearizar os dados do sinograma.
* **Dosimetria e Gestão de Dose:** Compreender a interação dos raios X com os tecidos é a base para o cálculo de grandezas dosimétricas como o **CTDI** (*Computed Tomography Dose Index*) e o **DLP** (*Dose-Length Product*). A otimização dos parâmetros físicos ($\text{kVp}$, modulação de corrente angular e longitudinal $mA$) visa garantir a qualidade diagnóstica mínima necessária (*princípio ALARA*) mantendo a restrição de dose ao paciente.
* **Reconstrução e DLR (*Deep Learning Reconstruction*):** Redes neurais profundas e algoritmos de reconstrução iterativa (IR) dependem de modelos estatísticos precisos da física de fótons (incluindo ruído quântico modelado por estatística de Poisson) para mitigar ruídos provenientes de feixes de raios X de baixa intensidade.

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|tomografia-computadorizada]]
- [[interacao-dos-raios-x-com-a-materia]]
- [[efeito-fotoetrico]]
- [[Espalhamento Compton|espalhamento-compton]]
- [[atenuacao-da-radiacao]]
- [[Endurecimento do Feixe|endurecimento-do-feixe]]
- [[qualidade-do-feixe-e-hvl]]
- [[dosimetria-em-tc-ctdi-e-dlp]]
- [[reconstrucao-fbp-e-iterativa]]
- [[Deep Learning Image Reconstruction (DLR)|inteligencia-artificial-em-tc]]
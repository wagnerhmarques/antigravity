---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, raio-x, espectro-de-raios-x, bremsstrahlung, filtragem]
data: 2026-08-25
---

# X-Ray Tube and Spectra

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O tubo de raios-X é o componente eletromecânico fundamental responsável pela geração do feixe de radiação ionizante utilizado em sistemas de Tomografia Computadorizada (TC). Em sua essência, o dispositivo consiste em um invólucro de vidro ou metal a vácuo (geralmente vidro pirex ou metal-cerâmica) que abriga dois eletrodos principais: o cátodo (filamento emissor de elétrons) e o ânodo (alvo metálico onde ocorre a conversão de energia cinética em fótons de raios-X).

O processo físico tem início no circuito de filamento, onde uma corrente elétrica de baixa tensão e alta intensidade ($I_f$) aquece o filamento de tungstênio, provocando a emissão termiônica de elétrons. Uma alta diferença de potencial (tensão do tubo, $kV_p$), aplicada entre o cátodo e o ânodo, acelera esses elétrons em direção ao ponto focal localizado na superfície anódica. Ao colidirem com o material do alvo (usualmente ligas de tungstênio-rênio devido ao alto número atômico $Z = 74$ e ao elevado ponto de fusão), a energia cinética dos elétrons incidentes ($E_k = e \cdot kV_p$) é dissipada através de três mecanismos primários:
1. **Produção de calor:** Mais de 99% da energia cinética dos elétrons é convertida em calor devido a excitações e ionizações não radiativas das camadas atômicas superficiais, exigindo sistemas complexos de resfriamento (circulação de óleo isolante e trocadores de calor).
2. **Radiação de Bremsstrahlung ("radiação de frenagem"):** Ocorre quando um elétron incidente penetra no campo coulombiano do núcleo atômico do tungstênio. O elétron sofre desaceleração e desvio, perdendo energia cinética que é emitida na forma de um fóton de raio-X pol energético.
3. **Radiação Característica:** Ocorre quando um elétron incidente colide com um elétron das camadas internas (camada K ou L) do átomo do alvo, ejetando-o. A lacuna resultante é preenchida por um elétron de uma camada mais externa, emitindo um fóton cuja energia corresponde exatamente à diferença entre os níveis de energia das camadas envolvidas.

O **espectro de raios-X** resultante gerado por um tubo de TC não é monocromático, mas sim policromático (contínuo com linhas discretas sobrepostas). O espectro contínuo de *Bremsstrahlung* estende-se desde energia zero até uma energia máxima estipulada pelo potencial máximo aplicado ($E_{max} = h
u_{max} = e \cdot kV_p$). As linhas características aparecem como picos agudos superpostos ao fundo contínuo (por exemplo, as transições da camada K do tungstênio ocorrem em energias aproximadas de$59\text{ keV}$a$69\text{ keV}$).

Metrologicamente, o feixe emitido sofre modificações espaciais e espectrais antes de interagir com o paciente. A **filtragem inerente** (vidro do tubo, óleo isolante e janela de saída) e a **filtragem adicional** (lâminas de cobre, alumínio ou titânio inseridas no caminho do feixe, frequentemente chamadas de filtros "bow-tie" ou de compensação) absorvem preferencialmente os fótons de baixa energia. Esse processo, denominado **endurecimento do feixe** (*beam hardening*), desloca o espectro efetivo para energias médias mais altas, reduzindo a dose cutânea desnecessária e mitigando artefatos de imagem.

---

## 2. Formulação Matemática e Propriedades

A distribuição espectral do feixe de raios-X em função da energia do fóton $E$, denotada por $N(E)$, pode ser modelada analiticamente ou empiricamente (como nos modelos de Kramers modificado). A intensidade do espectro contínuo de *Bremsstrahlung* é classicamente expressa por:

$$
\frac{dN}{dE} = K \cdot Z \cdot \left( E_{\max} - E \right)
$$

Onde:
- $K$ é uma constante de proporcionalidade que engloba a eficiência de conversão e a corrente do tubo ($mA$).
- $Z$ é o número atômico efetivo do material do ânodo.
- $E_{\max} = e \cdot kV_p$ é a energia máxima do fóton em quilétron-volts ($\text{keV}$).
- $E$ é a energia do fóton analisado ($\text{keV}$).

A fluência total de energia ou o espectro real após a atenuação por camadas de filtração de espessura $x_i$ e coeficientes de atenuação linear $\mu_i(E)$ é dado por:

$$
N_{filtered}(E) = N(E) \cdot \exp \left( - \sum_i \mu_i(E) x_i \right)
$$

O **fluxo de fótons integrado** sobre todo o espectro, que determina a corrente estatística detectada no sistema de aquisição de dados (DAS), é calculado pela integral:

$$
\Phi_{total} = \int_{0}^{e \cdot kV_p} N_{filtered}(E) \, dE
$$

A energia média do espectro ($E_{med}$) e a Camada Heminredutora (CHN ou *Half-Value Layer* - HVL), parâmetro metrológico crítico para controle de qualidade, relacionam-se com a penetrabilidade do feixe. A CHN representa a espessura de material absorvedor (tipicamente alumínio, $Al$) capaz de reduzir a intensidade do feixe incidente à metade:

$$
I(x_{HVL}) = \frac{I_0}{2} = I_0 \int_{0}^{e \cdot kV_p} N_{filtered}(E) e^{-\mu_{Al}(E) x_{HVL}} \, dE
$$

Propriedades geométricas do tubo, como o **tamanho do ponto focal** ($F_s$), afetam diretamente a resolução espacial do sistema de TC. Devido ao princípio do foco linha (*line focus principle*), o ângulo do anodo ($\theta$, tipicamente entre $5^\circ$ e $12^\circ$) permite que a projeção óptica do ponto focal (foco efetivo, $F_{eff}$) seja consideravelmente menor do que a área real de bombardeio eletrônico (foco real, $F_{real}$), otimizando simultaneamente a dissipação térmica e a resolução espacial:

$$
F_{eff} = F_{real} \cdot \sin(\theta)
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Em Tomografia Computadorizada moderna, o comportamento do tubo de raios-X e a forma do seu espectro são elementos centrais para o projeto de algoritmos de reconstrução, protocolos de dose e técnicas avançadas de imagem:

- **Controle de Qualidade (QC) e Metrologia:** A verificação periódica do $kV_p$ efetivo, da filtração total (através da medição da CHN) e da linearidade do rendimento do tubo em função do produto corrente-tempo ($mAs$) é mandatória para garantir a reprodutibilidade dos números de Hounsfield ($HU$) e a conformidade dos níveis de dose diagnóstica.
- **Correção de Endurecimento do Feixe (*Beam Hardening Correction* - BHC):** Como o espectro é policromático, os fótons de baixa energia são atenuados mais rapidamente do que os de alta energia ao atravessarem tecidos densos (como o osso). Isso gera artefatos de "copa de áudio" (*cupping artifacts*) ou bandas escuras. Algoritmos de correção em espaço de projeção ou pós-reconstrução utilizam o conhecimento preciso do espectro $N(E)$ para linearizar as projeções.
- **TC de Dupla Energia (*Dual-Energy CT* - DECT):** Tecnologias baseadas na modulação rápida de $kV_p$ (ex: $80\text{ kVp} / 140\text{ kVp}$), dupla fonte (*dual-source*) ou detectores em camadas (*sandwich detectors*) exploram ativamente as diferenças na dependência energética dos coeficientes de atenuação linear. O sucesso da decomposição material (ex: separação de iodo e cálcio) depende diretamente da separação e estabilidade espectral dos feixes gerados pelo tubo.
- **Reconstrução Baseada em Modelo e Iterativa (IR/DLR):** A modelagem física exata do sistema de aquisição (sistema *forward projector*) em algoritmos iterativos avançados e Deep Learning Reconstruction (DLR) frequentemente incorpora a distribuição espectral do tubo para simular ruído quântico realista e corrigir a degradação de contraste induzida pela polromaticidade.
- **Dosimetria Computacional e Observadores:** Simulações de Monte Carlo para estimativa de dose em órgãos (ex: usando o software CT-Expo ou MCNP) requerem espectros de entrada fidedignos gerados por códigos como IPEM Report 78 ou SpekCalc, parametrizados para o modelo específico do tubo de TC e sua filtração inerente.

---

## 4. Conexões e Wikilinks

- [[Computed Tomography Principles]]
- [[Image Reconstruction Algorithms (FBP, IR, DLR)]]
- [[Radiation Dosimetry and Dose Metrics in CT]]
- [[Image Quality and Artifacts in CT]]
- [[Quality Control and Metrology in Medical Physics]]
- [[Advanced CT Technologies (Dual-Energy, Photon-Counting)]]
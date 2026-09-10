---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, qualidade-de-imagem, adquisicao-de-dados, metrologia]
data: 2026-08-25
---

# espessura de corte

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **espessura de corte** (frequentemente referida em inglês como *slice thickness*) em Tomografia Computadorizada (TC) define a dimensão espacial dovoxel ao longo do eixo longitudinal do paciente (eixo $z$), correspondendo ao perfil de sensibilidade do plano de corte (SSP – *Slice Sensitivity Profile*). Em termos físicos, a espessura de corte determina o volume de tecido cujos coeficientes de atenuação linear efetivos são integrados e representados como um único pixel de tom cinza em uma matriz de imagem bidimensional.

Metrologicamente, a espessura de corte não é um degrau retangular perfeito devido às limitações geométricas do feixe de raios X focal, à abertura finita dos detectores na direção $z$ e à resposta dos filtros de reconstrução. O perfil real do corte é uma função contínua que sofre alargamento decorrente da geometria do feixe cônico (*cone-beam geometry*) e do passo (*pitch*) da hélice nos sistemas helicoidais. A determinação padronizada da espessura de corte é realizada por meio de testes de controle de qualidade utilizando rampas inclinadas ou dispositivos de teste (fantasmas) contendo esferas ou fios metálicos, medindo-se a largura a meia altura (FWHM – *Full Width at Half Maximum*) do SSP resultante.

## 2. Formulação Matemática e Propriedades (se aplicável)

O Perfil de Sensibilidade de Corte\, denotado por $S(z)$\, descreve a resposta do sistema de imagem ao longo do eixo $z$ para uma fonte infinitesimal de radiação. A espessura nominal de corte ($T$) está relacionada à integral deste perfil normalizado:

$$
T = \int_{-\infty}^{\infty} \frac{S(z)}{S_{\max}} \, dz
$$

Onde $S_{\max}$ é o valor máximo do perfil no centro do plano de corte.

Na prática clínica, o perfil $S(z)$ é aproximado por uma função Gaussiana ou uma função sinc modificada pelo filtro de reconstrução (kernel). A resolução espacial longitudinal $\Delta_z$ é diretamente governada por $S(z)$ e pela amostragem do detector. 

Considerando a reconstrução de imagens em TC helicoidal com interpolação $360^\circ$ linear em $z$, a largura efetiva do corte $w$ em função do passo helicoidal $p$ e da largura do colimador do detector $dz$ pode ser modelada como:

$$
w = \sqrt{dz^2 + \left( \frac{p \cdot dz}{2} \right)^2}
$$

O ruído estatístico na imagem ($\sigma$) é inversamente proporcional à raiz quadrada da espessura de corte efetiva, assumindo que os demais parâmetros de aquisição (corrente do tubo $mA$, tensão $kVp$, e tempo de rotação) permaneçam constantes:

$$
\sigma \propto \frac{1}{\sqrt{T}}
$$

Dessa forma, a redução da espessura de corte para melhorar a resolução espacial longitudinal impõe uma penalidade severa na relação sinal-ruído (SNR), exigindo compensações na dose de radiação para manter a detectabilidade de baixo contraste.

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A escolha da espessura de corte é um dos parâmetros de otimização mais críticos na prática da física médica em TC, pois dita o equilíbrio fundamental entre **resolução espacial** e **ruído de imagem**.

- **Protocolos Clínicos e Resolução Isotrópica:** Com o advento dos scanners de múltiplos cortes (*multi-detector CT* - MDCT) com geometrias de fileiras isotrópicas de detectores, tornou-se possível adquirir dados volumétricos com voxels quase isotrópicos (onde $\Delta_x \approx \Delta_y \approx \Delta_z$), permitindo reconstruções multi-planares (MPR) e renderizações tridimensionais (3D/VRT) de alta fidelidade diagnóstica.
- **Detecção de Pequenas Estruturas:** Cortes finos (ex: $0.5\text{ mm}$ a $1.0\text{ mm}$) são imprescindíveis em avaliações de alta resolução, como na análise de parênquima pulmonar para doenças intersticiais, osso temporal, angiotomografias coronarianas e detecção de micro-fraturas.
- **Dosimetria e Gestão de Dose:** Embora cortes mais finos gerem maior ruído por pixel, a prática moderna utiliza algoritmos avançados de reconstrução, como a Reconstrução Iterativa (IR) e Inteligência Artificial baseada em Aprendizado Profundo (DLR – *Deep Learning Reconstruction*), para suprimir o ruído quântico sem sacrificar a espessura de corte fina, viabilizando exames com doses otimizadas.
- **Controle de Qualidade (QC):** A verificação periódica da espessura de corte por meio de fantasmas específicos assegura que o equipamento opere dentro das tolerâncias estabelecidas pelas agências reguladoras, prevenindo artefatos de volume parcial e imprecisões metrológicas em volumetria tumoral.

## 4. Conexões e Wikilinks

- [[perfil de sensibilidade de corte|Perfil de Sensibilidade de Corte (SSP)]]
- [[Resolução Espacial|Resolução Espacial em TC]]
- [[Ruído Quântico|Ruído Quântico e Relação Sinal-Ruído (SNR)]]
- [[Artefato de Volume Parcial|Artefato de Volume Parcial]]
- [[Reconstrução Iterativa|Reconstrução Iterativa (IR)]]
- [[Deep Learning Image Reconstruction (DLR)|Inteligência Artificial e DLR em Tomografia]]
- [[pitada e passo helicoidal|Passo Helicoidal (Pitch)]]
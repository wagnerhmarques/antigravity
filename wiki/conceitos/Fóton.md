---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, fisica-radiologica, radiacao-eletromagnetica, mecanica-quantica]
data: 2026-08-25
---

# fotão

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **fotão** (ou **fóton**) é a partícula elementar mediadora da interação eletromagnética, sendo o quantum fundamental da radiação eletromagnética em todo o espectro, incluindo os raios X utilizados em [[Tomografia Computadorizada|Tomografia Computadorizada (TC)]]. Do ponto de vista da eletrodinâmica quântica (QED) e da mecânica quântica, o fotão exibe a dualidade onda-partícula, comportando-se ora como uma onda eletromagnética clássica regida pelas equações de Maxwell, ora como um corpúsculo corpuscular sem massa de repouso ($m_0 = 0$), desprovido de carga elétrica, mas portador de energia, momento linear e momento angular intrínseco (spin $s = 1$).

Na Física Médica e na metrologia das radiações ionizantes, a interação dos fotões de raios X com a matéria (tecidos biológicos e materiais de blindagem) ocorre em regimes de alta energia onde a natureza quântica discreta do feixe de radiação torna-se dominante. Ao contrário de um modelo puramente contínuo ou determinístico, um feixe de raios X é estocástico e composto por um número finito de fotões discretos. Esta granularidade quântica é a origem fundamental do [[Ruído Quântico]] (ou ruído estatístico de Poisson) nas imagens de TC. 

Metrologicamente, os fotões são caracterizados por sua energia ($E$), frequência ($
u$) e comprimento de onda ($\lambda$). No diagnóstico por imagem em TC, a faixa de energia típica dos fotões situa-se entre$20\text{ keV}$e$140\text{ keV}$, abrangendo processos de interação primários como o [[Efeito Fotoelétrico]] e o [[Espalhamento Compton|efeito Compton]] (espalhamento incoerente), além da produção de pares (embora esta última seja insignificante nas energias diagnósticas usuais).

---

## 2. Formulação Matemática e Propriedades

As propriedades cinemáticas e quânticas de um fotão individual são descritas pelas seguintes formulações fundamentais:

A energia $E$ de um fotão é diretamente proporcional à frequência da onda eletromagnética associada $
u$, conforme a relação de Planck-Einstein:

$$
E = h\nu = \frac{hc}{\lambda}
$$

Onde:
- $h$ é a constante de Planck ($h \approx 6.626 \times 10^{-34}\text{ J}\cdot\text{s}$);
- $\hbar = \frac{h}{2\pi}$ é a constante reduzida de Planck;
- $\omega$ é a frequência angular.

Considerando a relação de dispersão relativística para uma partícula com massa de repouso nula ($m_0 = 0$), o momento linear $p$ do fotão está estritamente vinculado à sua energia através da velocidade da luz no vácuo $c$:

$$
E = p c \implies p = \frac{h 
u}{c} = \frac{h}{\lambda}
$$

Onde $\lambda$ representa o comprimento de onda do fotão.

No contexto da atenuação dos raios X ao atravessar um meio material heterogêneo de espessura $x$, a intensidade macroscopicamente observada de um feixe monoenergético de fotões é modelada pela lei exponencial de Beers-Lambert:

$$
I(x) = I_0 \exp \left( -\int_{0}^{x} \mu(l) \, dl \right)
$$

Onde:
- $I_0$ é a intensidade incidente de fotões;
- $\mu(l)$ é o coeficiente linear de atenuação dependente da posição e da energia do fotão.

No entanto, em nível microscópico e estatístico, o número de fotões $N$ que atravessam um voxel ou atingem um elemento detector individual em um intervalo de tempo fixo não é determinístico, mas flutua de acordo com a distribuição de probabilidade de Poisson. A variância estatística associada ao contagem de fotões $\sigma_N^2$ é igual à média do número de fotões contados $\bar{N}$:

$$
\sigma_N^2 = \bar{N}
$$

Consequentemente, a relação sinal-ruído (SNR) intrínseca limitada pela contagem de fotões é dada por:

$$
\text{SNR} = \frac{\bar{N}}{\sigma_N} = \frac{\bar{N}}{\sqrt{\bar{N}}} = \sqrt{\bar{N}}
$$

Esta relação matemática demonstra que a mitigação do ruído quântico exige um aumento proporcional na dose de radiação (maior número de fotões incidentes), desafio central superado recentemente por técnicas avançadas de [[Reconstrução Iterativa|reconstrução iterativa]] e [[deep learning image reconstruction (DLIR)]].

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A compreensão rigorosa do comportamento dos fotões é o pilar para o projeto, operação e otimização de sistemas modernos de Tomografia Computadorizada:

* **Sistemas de Contagem de Fotões (Photon-Counting Computed Tomography - PCCT):** Ao contrário dos detectores convencionais baseados em cintilação integradora de corrente (que medem a energia total depositada por múltiplos fotões ao longo de um intervalo de tempo), os detectores de contagem de fotões baseados em semicondutores (como CdTe ou CZT) registram individualmente cada fotão que atinge o detector e discriminam sua energia por meio de limiares de discriminação eletrônica (Energy Binning). Isso elimina o ruído eletrônico de fundo, melhora a resolução espacial intrínseca e potencializa o contraste tecidual por meio de imagens multienergéticas (k-edge imaging).
* **Correção de "Beam Hardening" (Endurecimento do Feixe):** Como os feixes de raios X convencionais são policromáticos, os fotões de menor energia são preferencialmente absorvidos à medida que o feixe penetra em estruturas densas (como o osso). Modelar a distribuição espectral dos fotões é essencial para aplicar algoritmos de correção de endurecimento de feixe e evitar artefatos em forma de faixa (*cupping artifacts*).
* **Dosimetria e Otimização do Protocolo:** A otimização da dose de radiação ionizante em exames de TC fundamenta-se na gestão eficiente da fluência de fotões. Ferramentas de modulação de corrente baseadas no tamanho do paciente (como *angular and longitudinal tube current modulation*) ajustam dinamicamente a quantidade de fotões gerados pelo tubo de raios X para manter a qualidade de imagem constante com o mínimo de exposição possível ao paciente.
* **Modelagem Estatística em Reconstrução:** Algoritmos modernos de reconstrução estatística utilizam o conhecimento da física de contagem de fotões e o ruído de Poisson para penalizar incertezas nas projeções cruas, permitindo doses ultrabaixas sem degradação diagnóstica severa.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada (TC)]]
* [[Photon-Counting Computed Tomography (PCCT)]]
* [[Efeito Fotoelétrico]]
* [[Espalhamento Compton|Efeito Compton]]
* [[Atenuação dos Raios X]]
* [[Ruído Quântico]]
* [[Reconstrução Iterativa|Reconstrução Iterativa]]
* [[Deep Learning Image Reconstruction (DLIR)]]
* [[Controle de Qualidade em TC]]
* [[Dosimetria em Radiologia]]
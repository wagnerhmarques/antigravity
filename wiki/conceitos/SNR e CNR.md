---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, qualidade-de-imagem, relacao-sinal-ruido, contraste-ruido, metrologia]
data: 2026-08-25
---

# SNR e CNR

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A Relação Sinal-Ruído (**SNR** - *Signal-to-Noise Ratio*) e a Relação Contraste-Ruído (**CNR** - *Contrast-to-Noise Ratio*) são as métricas fundamentais de qualidade de imagem na Física Médica, atuando como pilares para a avaliação quantitativa e qualitativa de sistemas de imagem por Tomografia Computadorizada (TC). 

O **Signal-to-Noise Ratio (SNR)** quantifica a intensidade relativa do sinal útil (que representa a atenuação real dos tecidos anatômicos) em relação à flutuação estatística aleatória (ruído quântico e eletrônico) inerente ao processo de aquisição e reconstrução. Em termos físicos, o sinal em TC é expresso em unidades Hounsfield (HU) ou em coeficientes de atenuação linear ($\mu$), enquanto o ruído é definido como o desvio padrão dessas medidas em uma região de interesse (ROI) homogênea.

O **Contrast-to-Noise Ratio (CNR)** expande o conceito de SNR ao incorporar a diferença de sinal entre uma estrutura anatômica de interesse (lesão, órgão, vaso) e o seu tecido de fundo circundante (*background*). Enquanto um alto SNR garante uma imagem visualmente "limpa" e sem granulação excessiva, o CNR determina a *detectabilidade* real de estruturas de baixo contraste (como metástases hepáticas precoces ou acidentes vasculares cerebrais isquêmicos incipientes). Sem um CNR adequado, mesmo uma imagem com alto SNR pode falhar em distinguir patologias sutis devido à sobreposição com as flutuações estatísticas do ruído.

Metrologicamente, ambas as métricas são essenciais para o balanço do princípio **ALARA** (*As Low As Reasonably Achievable*), permitindo otimizar protocolos clínicos para entregar a menor dose de radiação ionizante possível sem comprometer o diagnóstico médico.

---

## 2. Formulação Matemática e Propriedades

Matematicamente, o SNR para uma única Região de Interesse (ROI) em uma imagem de Tomografia Computadorizada é definido como a razão entre a média do sinal (geralmente expressa em números de Tomografia Computadorizada, $HU$) e o desvio padrão do ruído ($\sigma$) nessa mesma região:

$$
\text{SNR} = \frac{\bar{S}}{\sigma}
$$

Onde:
- $\bar{S} = \frac{1}{N} \sum_{i=1}^{N} S_i$ é o valor médio do sinal na ROI contendo $N$ pixels/vóxeis.
- $\sigma = \sqrt{\frac{1}{N-1} \sum_{i=1}^{N} (S_i - \bar{S})^2}$ é o desvio padrão estimado do ruído na ROI.

O **CNR**, por sua vez, quantifica a separação entre o sinal de uma estrutura alvo ($\bar{S}_{\text{alvo}}$) e o tecido de fundo ($\bar{S}_{\text{fundo}}$), normalizada pelo desvio padrão do ruído no fundo ($\sigma_{\text{fundo}}$) ou por uma combinação dos desvios padrão:

$$
\text{CNR} = \frac{\left| \bar{S}_{\text{alvo}} - \bar{S}_{\text{fundo}} \right|}{\sigma_{\text{fundo}}}
$$

Em cenários onde a heterogeneidade do tecido exige uma estimativa de ruído pooled (combinada), a formulação assume a forma:

$$
\text{CNR} = \frac{\left| \bar{S}_{\text{alvo}} - \bar{S}_{\text{fundo}} \right|}{\sqrt{\frac{\sigma_{\text{alvo}}^2 + \sigma_{\text{fundo}}^2}{2}}}
$$

### Propriedades Estatísticas e Físicas na TC:
1. **Dependência com a Dose:** Pela estatística de Poisson dos fótons de raios X incidentes (ruído quântico), o desvio padrão do ruído ($\sigma$) é inversamente proporcional à raiz quadrada do produto corrente-tempo ($mAs$) e, por consequência, da dose absorvida ($D$):
   
$$
\sigma \propto \frac{1}{\sqrt{mAs}} \implies \text{SNR} \propto \sqrt{mAs}
$$

2. **Dependência com o Vóxel:** O ruído escala inversamente com as dimensões espaciais do vóxel. Reduzir a espessura de corte ($dz$) ou o campo de visão matricial (aumentando a matriz de reconstrução) reduz o número de fótons por vóxel, elevando $\sigma$ e degradando proporcionalmente o SNR e o CNR.
3. **Filtros de Reconstrução (Kernel):** Kernels agudos (*sharp*) enfatizam altas frequências espaciais, aumentando $\sigma$ e reduzindo o SNR. Kernels suaves (*smooth*) realizam uma suavização espacial (filtragem passa-baixa), reduzindo o ruído e elevando o SNR em detrimento da resolução espacial.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Na prática clínica e na engenharia de imagem de Tomografia Computadorizada, o SNR e o CNR são parâmetros centrais em diversas frentes:

- **Controle de Qualidade (CQ) e Associações de Física Médica:** Protocolos de CQ (como os da AAPM ou ACR) utilizam fantomas de água e polímeros para monitorar o SNR de rotina em scanners de TC. Variações inesperadas no SNR indicam falhas no tubo de raios X, desalinhamento de detectores ou instabilidade na calibração do ar (*air scan calibration*).
- **Avaliação de Algoritmos de Reconstrução:** 
  - Na **Retroprojeção Filtrada (FBP)**, existe um compromisso rígido (*trade-off*) clássico entre resolução espacial e ruído.
  - A **Reconstrução Iterativa (IR)** e os algoritmos baseados em **Inteligência Artificial (Deep Learning Reconstruction - DLR)** modificam drasticamente essa relação. Modelos DLR avançados são treinados para suprimir o ruído texturizado e artefatos de baixa dose sem borrar as bordas anatômicas, resultando em ganhos massivos de CNR e SNR, permitindo exames diagnósticos em faixas de ultra-baixa dose.
- **Teoria de Detecção e Observadores Computacionais:** Em tarefas de detecção de lesões, a detectabilidade ($d'$) descrita pelo Teorema do Observador Ideal (como o *Non-Preembedding Hotelling Observer* ou *Channelized Hotelling Observer*) é diretamente proporcional ao CNR da lesão ponderada pela Função de Transferência de Modulação (MTF) do sistema.
- **Protocolos Pediátricos e Bariátricos:** A otimização de protocolos baseada em CNR garante que pacientes bariátricos (onde a atenuação severa causa "ruído de fóton faminto" ou *photon starvation*) mantenham um CNR mínimo aceitável para visualização de estruturas retroperitoneais, enquanto pacientes pediátricos beneficiam-se de reduções rigorosas de $mAs$ guiadas por limites aceitáveis de SNR.

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|Tomografia Computadorizada]]
- [[Física de Raios-X e Interação com a Matéria]]
- [[Controle de Qualidade em TC]]
- [[Reconstrução Iterativa|Reconstrução Iterativa e DLR]]
- [[Artefatos em Tomografia Computadorizada]]
- [[Dosimetria em Radiodiagn Stico|Dosimetria em Radiodiagnóstico]]
- [[Task Transfer Function|Função de Transferência de Modulação (MTF)]]
---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, dosimetria, ctdi, radioprotecao, inteligencia-artificial]
data: 2026-08-25
---

# ctdi-vol

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **$CTDI_{vol}$** (Índice de Dose em Tomografia Computadorizada Volumétrica, do inglês *Volume Computed Tomography Dose Index*) é a métrica padrão ouro na dosimetria em Tomografia Computadorizada (TC) estabelecida internacionalmente para quantificar a dose de radiação emitida por rotação do tubo de raios X, corrigida para o espaçamento entre cortes ou para o avanço da mesa em varreduras helicoidais. 

Fisicamente, o $CTDI_{vol}$ deriva do $CTDI_{w}$ (Índice de Dose Ponderado), que por sua vez é construído a partir de medições pontuais do kerma no ar integradas ao longo do eixo longitudinal ($z$) utilizando uma câmara de ionização do tipo lápis (*pencil chamber*) de $100\text{ mm}$ de comprimento, inserida em câmara de acrílico (PMMA) normalizada para simular a atenuação e o espalhamento da radiação em fantomas cilíndricos padronizados (cabeça de $16\text{ cm}$ e corpo de $32\text{ cm}$ de diâmetro).

Enquanto o $CTDIw$ descreve a dose média dentro de um único plano de corte transaxial para uma dada rotação, o $CTDI_{vol}$ introduz a correção fundamental para o regime de varredura helicoidal ou sequencial (axial), contabilizando o efeito do *pitch* (passo da hélice) ou da sobreposição/lacuna entre rotações consecutivas. Portanto, o $CTDI_{vol}$ **não** representa a dose absorvida real em um órgão específico de um paciente biológico, mas sim uma métrica padronizada de *saída de radiação* (output) do equipamento sob condições normalizadas de laboratório, servindo como base primária para o cálculo do produto dose-comprimento ([[Métricas de Dose em TC|dlp]]) e para a conformidade com diretrizes regulatórias e níveis de referência diagnóstica ([[nrd]]).

---

## 2. Formulação Matemática e Propriedades

Matematicamente, o $CTDI_{vol}$ é definido a partir do $CTDI_{w}$ ponderado pela taxa de avanço do feixe (frequentemente expressa pelo *pitch* nominal, $P$). 

Primeiramente, o $CTDI_{100}$ em um ponto específico (centro ou periferia do fantoma) é dado pela integral do perfil de dose $D(z)$ ao longo do eixo $z$:

$$
CTDI_{100} = \frac{1}{N \cdot T} \int_{-50\text{ mm}}^{+50\text{ mm}} D(z) \, dz
$$

Onde:
- $N$ é o número de canais de detetores ativados simultaneamente.
- $T$ é a largura nominal de cada corte (em mm) no eixo isocêntrico.
- O produto $N \cdot T$ representa a colimação total nominal do feixe ($T_{total}$).

O Índice de Dose Ponderado ($CTDI_{w}$), que pondera as contribuições da periferia e do centro do fantoma de PMMA para simular a distribuição espacial da dose, é formulado como:

$$
CTDI_{w} = \frac{1}{3} CTDI_{100,\text{centro}} + \frac{2}{3} CTDI_{100,\text{periferia}}
$$

Finalmente, o **$CTDI_{vol}$** é calculado incorporando o fator de correção do *pitch* ($P$):

$$
CTDI_{vol} = \frac{CTDI_{w}}{P}
$$

Em varreduras helicoidais (espirais), o *pitch* ($P$) é definido como o deslocamento da mesa por rotação do tubo ($d$) dividido pela colimação total nominal do feixe ($T_{total}$):

$$
P = \frac{d}{N \cdot T}
$$

Em varreduras sequenciais (axial *stеp-and-shoot*), o parâmetro análogo ao *pitch* é a razão entre o avanço da mesa entre varreduras consecutivas e a colimação total. 

Dessa forma, as propriedades analíticas fundamentais do $CTDI_{vol}$ incluem:
- **Invariância com o comprimento escaneado:** O $CTDI_{vol}$ de uma varredura de $10\text{ cm}$ é teoricamente idêntico ao de uma varredura de $50\text{ cm}$, desde que os parâmetros técnicos ($kVp$, $mAs$, filtração, colimação e *pitch*) permaneçam constantes.
- **Inversamente proporcional ao *pitch*:** Manter a corrente nominal ($mAs$) constante e aumentar o *pitch* dilui a energia entregue ao longo do eixo $z$, reduzindo linearmente o $CTDI_{vol}$.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

### Controle de Qualidade e Conformidade Regulatória
O $CTDI_{vol}$ é a métrica mandatória exigida por agências reguladoras (como a ANVISA no Brasil, a FDA nos EUA e a Comissão Europeia) para a aceitação eissionamento e testes periódicos de controle de qualidade de scanners de TC. Físicos médicos utilizam o $CTDI_{vol}$ exibido na interface da console (*console displayed CTDIvol*) para verificar se a dose irradiada pelo tubo está dentro da tolerância de fábrica (geralmente $\pm 20\%$).

### Otimização de Protocolos e Inteligência Artificial
Com o advento de algoritmos de reconstrução avançados, como a Reconstrução Iterativa ([[Reconstrução Iterativa|ir]]) e métodos baseados em Aprendizagem Profunda ([[Métricas de Dose em TC|dlp]], redes neurais de Redução de Ruído e DLR), tornou-se possível reduzir drasticamente o produto $mAs$ — e, consequentemente, o $CTDI_{vol}$ — sem degradação catastrófica da [[SNR|relacao-sinal-ruido]] ([[SNR]]) ou da [[Resolução Espacial|resolucao-espacial]]. 

Sistemas modernos de TC utilizam softwares de controle automático de exposição ([[aec]]) que modulam dinamicamente a corrente do tubo em tempo real com base no *topogram* (scout), ajustando o $CTDI_{vol}$ localmente para manter a qualidade de imagem constante em regiões de espessuras anatômicas variadas (ex: ombros versus pelve). Em paralelo, modelos de Inteligência Artificial preditivos atuam diretamente na estimativa pré-reconstrução para sugerir o menor $CTDI_{vol}$ viável para um determinado [[fator-de-conversao-dose]] e biotipo do paciente.

---

## 4. Conexões e Wikilinks

- [[Métricas de Dose em TC|dlp]]
- [[nrd]]
- [[Reconstrução Iterativa|ir]]
- [[Métricas de Dose em TC|dlp]] *(Modelos de Deep Learning em TC)*
- [[SNR|relacao-sinal-ruido]]
- [[Resolução Espacial|resolucao-espacial]]
- [[aec]]
- [[fator-de-conversao-dose]]
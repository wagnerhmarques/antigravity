---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada\, dosimetria, aquisicao-de-imagem, otimization-clinica]
data: 2026-08-25
---

# extensão da varredura

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **extensão da varredura** (*scan length* ou *z-coverage* em inglês) refere-se ao comprimento linear total ao longo do eixo longitudinal ($z$) do paciente ou objeto que é irradiado e amostrado durante um exame de Tomografia Computadorizada (TC). Em sistemas helicoidais (espirais) modernos, a extensão da varredura é definida pelo deslocamento da mesa durante o tempo efetivo de exposição dos raios X, enquanto em sistemas sequenciais (*axial step-and-shoot*), corresponde ao somatório das larguras dos cortes efetivos multiplicadas pelo número de rotações e pelo incremento da mesa.

Do ponto de vista metrológico e físico, a extensão da varredura é um parâmetro crítico que determina diretamente:
1. **O volume anatômico exposto** à radiação ionizante primária e dispersa;
2. **A integral da dose de radiação** absorvida, sendo o principal fator determinante para o cálculo do *Dose Length Product* (DLP) e da Dose Efetiva ($E$);
3. **As condições de contorno** para os algoritmos de reconstrução tridimensional, especialmente em topografias complexas que exigem extensões longas (ex: angio-TC de aorta total ou exames de corpo inteiro em oncologia).

A determinação precisa da extensão da varredura é estabelecida no planejamento do exame (*scanogram* ou *topogram*), onde o técnico ou o sistema automatizado define os limites anatômicos de início ($z_{start}$) e término ($z_{\end}$). Desvios indesejados na extensão da varredura — seja por excesso (*overscanning* intencional ou acidental) ou por deficiência — comprometem o princípio ALARA (*As Low As Reasonably Achievable*), gerando irradiação desnecessária de tecidos adjacentes ou perda de diagnóstico por truncamento anatômico longitudinal.

---

## 2. Formulação Matemática e Propriedades

Matematicamente, a extensão da varredura ($L$) em uma aquisição helicoidal é expressa pela diferença entre as posições extremas do centro do feixe de radiação no eixo $z$ ou\, de forma mais operacional, pela velocidade de translação da mesa em função do tempo de exposição efetivo.

Para uma varredura helicoidal contínua, o comprimento linear $L$ é dado por:

$$
L = z_{\end} - z_{start} = v_{table} \cdot T_{\exp}
$$

Onde:
- $z_{start}$ e $z_{\end}$ representam as coordenadas iniciais e finais da mesa (em cm ou mm);
- $v_{table}$ é a velocidade linear da mesa (mm/s);
- $T_{\exp}$ é o tempo total de irradiação efetiva (s).

Levando em conta os parâmetros geométricos do tomógrafo, a velocidade da mesa é governada pelo passo helicoidal (*pitch* $p$), pela colimação total do feixe ($T = N \times \Delta z$, onde $N$ é o número de canais ativos do detector e $\Delta z$ é a largura do detector no eixo $z$ ao isocentro) e pelo tempo de rotação do tubo ($t_{rot}$):

$$
v_{table} = \frac{p \cdot T}{t_{rot}}
$$

Substituindo na equação de extensão, temos:

$$
L = \left( \frac{p \cdot N \cdot \Delta z}{t_{rot}} \right) \cdot T_{\exp}
$$

### Overscanning e Extensão Efetiva de Irradiação

É fundamental distinguir a extensão nominal da imagem reconstruída da extensão real de irradiação ($L_{irrad}$). Devido à geometria de leque ou cone (*cone-beam*) dos sistemas multidetectores (MDCT) e à necessidade de interpolação helicoidal (como 180linear ou 360linear), o tubo de raios X deve permanecer ligado antes do primeiro corte de imagem e após o último corte de imagem para garantir dados suficientes para a reconstrução sem artefatos de borda. 

Portanto, a extensão real da irradiação inclui uma margem de segurança física conhecida como *overscanning* longitudinal ($\Delta L_{over}$):

$$
L_{irrad} = L + \Delta L_{over}
$$

Onde $\Delta L_{over}$ tipicamente abrange de meia a uma rotação completa adicional ($2 \pi$ radianos) distribuída nas extremidades superior e inferior da varredura:

$$
\Delta L_{over} \approx 2 \cdot \left( \frac{p \cdot T}{2} \right) = p \cdot T
$$

O impacto da extensão da varredura na dosimetria é quantificado pelo Produto Dose-Comprimento ($DLP$)\, definido analiticamente pela integração do índice de dose na tomografia computadorizada ($CTDI_{vol}$) ao longo da extensão da varredura $L_{irrad}$:

$$
DLP = \int_{- \infty}^{\infty} CTDI_{vol}(z) \, dz \approx \int_{z_{start} - \epsilon}^{z_{\end} + \epsilon} CTDI_{vol}(z) \, dz
$$

Onde o $CTDI_{vol}$ é normalizado pelo *pitch* e reflete a dose média dentro do volume escaneado:

$$
CTDI_{vol} = \frac{1}{p \cdot T} \int_{- \infty}^{\infty} D(z) \, dz
$$

Logo, o $DLP$ cresce linearmente com o aumento da extensão da varredura, impactando diretamente a estimativa estocástica do risco radiobiológico por meio da conversão da dose efetiva ($E = DLP \cdot E_{chest/abdomen/etc}$).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

### Otimização Ocupacional e do Paciente
A extensão da varredura é um dos alvos principais nos protocolos de otimização de dose em TC. Erros grosseiros na delimitação do *topogram* (por exemplo, incluir o crânio inteiro em um exame de seios da face ou estender a varredura abdominal muito abaixo da sínfise púbica) aumentam o $DLP$ e a dose efetiva sem agregar valor diagnóstico. Softwares modernos de IA e sistemas de posicionamento baseados em visão computacional auxiliam na automação dos limites de varredura (*automatic scan range planning*), reduzindo a variabilidade inter-operador.

### Protocolos Pediátricos e Órgãos Sensitstivos
Em pacientes pediátricos, o controle rigoroso da extensão da varredura é ainda mais crítico devido à maior radiosensibilidade dos tecidos em desenvolvimento. Ferramentas de blindagem protetora de bismuth ou modulação de corrente adaptativa dependem de uma definição precisa de $L$ para evitar artefatos de endurecimento de feixe e garantir que o cálculo automático da dose (*tube current modulation*) funcione corretamente ao longo do eixo longitudinal.

### Reconstrução de Imagem e DLR (*Deep Learning Reconstruction*)
Algoritmos avançados de reconstrução, incluindo Iterative Reconstruction (IR) e Deep Learning Reconstruction (DLR), processam volumes tridimensionais que dependem da consistência dos dados brutos (*sinograma*). Extensões de varredura curtas demais em aquisições helicoidais podem induzir artefatos de truncamento longitudinal em regiões de transição (como a base do crânio ou a transição tóraco-lombar), que são mitigados por modelos matemáticos de predição ou extrapolação de dados.

---

## 4. Conexões e Wikilinks

- [[Métricas de Dose em TC|ctdi-vol]]
- [[DLP Dose Length Product|dlp-dose-length-product]]
- [[Métricas de Dose em TC|dose-efetiva]]
- [[Pitch Helicoidal|pitch-helicoidal]]
- [[Artefatos em TC|artefatos-em-tomografia]]
- [[Reconstrução Iterativa|reconstrucao-iterativa]]
- [[Filtragem e Retroprojecao|filtragem-e-retroprojecao]]
- [[Radioproteção|principio-alara]]
- [[Modulação de Corrente de Tubo (TCM)|modulacao-de-corrente]]
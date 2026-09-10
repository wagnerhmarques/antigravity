---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, controle-de-qualidade, metrologia, dosimetria, radioprotecao]
data: 2026-08-25
---

# Controle de Qualidade em Tomografia

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **Controle de Qualidade em Tomografia Computadorizada (TC)** engloba o conjunto sistemático de procedimentos operacionais, testes físicos, metrológicos e avaliações clínicas destinados a garantir que o sistema de TC opere de maneira otimizada, mantendo a performance de imagem em níveis diagnósticos máximos com a menor dose de radiação ionizante exequível, em estrita conformidade com as normativas regulatórias nacionais e internacionais (como IEC, AAPM e IAEA).

Do ponto de vista metrológico, o controle de qualidade (CQ) fundamenta-se na rastreabilidade de grandezas físicas fundamentais — tais como a kerma no ar, o Índice de Dose em Tomografia Computadorizada ($CTDI$), o ruído estatístico, a modulação espacial e a linearidade do coeficiente de atenuação linear ($\mu$). A degradação gradual de componentes críticos do scanner, como a ampola de raios X (desgaste do ânodo, instabilidade focal), a matriz de detecção de estado sólido (deriva de ganho de canais individuais, degradação de cristais de cintilação como tungstato de cádmio ou garnet de gadolínio e alumínio) e os subsistemas mecânicos de rotação e translação (precisão do pitch e estabilidade do gantry), introduz artefatos e desvios quantitativos que comprometem diretamente a acurácia diagnóstica e a radioproteção do paciente.

Os programas de CQ dividem-se tipicamente em testes de aceitação (comissionamento pelo físico médico no momento da instalação), testes de constância ou rotina (realizados diariamente, semanalmente ou mensalmente por técnicos ou físicos) e testes de estado (avaliações periódicas aprofundadas). Parâmetros fundamentais como a constância das unidades Hounsfield (HU), a resolução espacial de alto e baixo contraste, a uniformidade da imagem e a dosimetria operacional são mensurados utilizando fantasmas (*phantoms*) normalizados, preenchidos com água, acrílico, tecidos equivalentes ou estruturas complexas de teste de alta frequência espacial.

## 2. Formulação Matemática e Propriedades

A avaliação quantitativa da qualidade de imagem em TC baseia-se em métricas matemáticas rigorosas que descrevem a fidelidade espacial, o contraste e o ruído estatístico.

### A. Unidades Hounsfield (HU) e Linearidade

A conversão dos coeficientes de atenuação linear medidos em números de TC (HU) é definida por:

$$
\text{HU} = 1000 \times \frac{\mu - \mu_{\text{água}}}{\mu_{\text{água}} - \mu_{\text{ar}}}
$$

Onde $\mu$, $\mu_{\text{água}}$ e $\mu_{\text{ar}}$ representam, respectivamente, os coeficientes efetivos de atenuação linear do tecido sob análise, da água pura e do ar nas condições de varredura (tensão do tubo $kVp$, filtração e espectro de energia).

### B. Ruído de Imagem e Desvio Padrão

O ruído em uma imagem de TC, denotado por $\sigma_{\text{HU}}$, é quantificado pelo desvio padrão dos valores de pixels medidos em uma região de interesse (ROI) central homogênea em um fantoma de água:

$$
\sigma_{\text{HU}} = \sqrt{\frac{1}{N-1} \sum_{i=1}^{N} \left(\text{HU}_i - \overline{\text{HU}}\right)^2}
$$

Onde $N$ é o número total de pixels na ROI, $\text{HU}_i$ é o valor do $i$-ésimo pixel e $\overline{\text{HU}}$ é a média aritmética dos valores de HU na região. Teoricamente, o ruído é inversamente proporcional à raiz quadrada da dose de radiação absorvida (ou do produto corrente-tempo, $mAs$) e à espessura do corte tomográfico ($\Delta z$), obedecendo à relação:

$$
\sigma_{\text{HU}} \propto \frac{1}{\sqrt{mAs \cdot \Delta z}}
$$

### C. Função de Transferência de Modulação (MTF)

A caracterização da resolução espacial de alto contraste é formalmente descrita pela Função de Transferência de Modulação (MTF), obtida a partir da Transformada de Fourier da Função de Dispersão de Ponto (*Point Spread Function* - PSF) ou da derivada da Função de Dispersão de Borda (*Edge Spread Function* - ESF):

$$
\text{MTF}(f) = \frac{\left| \mathcal{F}\{\text{PSF}(x,y)\} \right|}{\left| \mathcal{F}\{\text{PSF}(x,y)\}\right|_{f=0}}
$$

Onde $f$ representa a frequência espacial expressa em pares de linhas por centímetro ($\text{pl/cm}$). A frequência correspondente ao limiar de $\text{MTF} = 0,1$ (ou 10%) é frequentemente utilizada como métrica padronizada para comparar a resolução espacial limite do sistema.

### D. Dosimetria Operacional ($CTDI_{\text{vol}}$ e DLP)

O Índice de Dose em Tomografia Computadorizada ($\text{CTDI}$) é integrado ao longo do eixo de rotação ($z$) para um único corte, sendo medido com uma câmara de ionização tipo *pencil* de 100 mm de comprimento:

$$
\text{CTDI}_{100} = \frac{1}{nT} \int_{-50\,\text{mm}}^{+50\,\text{mm}} D(z) \, dz
$$

Onde $n$ é o número de cortes tomográficos adquiridos simultaneamente por rotação e $T$ é a espessura nominal de cada corte. O $\text{CTDI}_{w}$ (ponderado) contabiliza a anisotropia da distribuição de dose entre o centro ($c$) e a periferia ($p$) do fantoma cilíndrico de PMMA (acrílico) de diâmetros padronizados (16 cm para crânio e 32 cm para abdômen/corpo):

$$
\text{CTDI}_{w} = \frac{1}{3} \text{CTDI}_{100,\text{centro}} + \frac{2}{3} \text{CTDI}_{100,\text{periferia}}
$$

Para sistemas helicoidais, o $\text{CTDI}_{\text{vol}}$ normaliza a dose pelo fator de hélice ou *pitch* ($P$):

$$
\text{CTDI}_{\text{vol}} = \frac{\text{CTDI}_{w}}{P}
$$

O Produto Dose-Comprimento ($\text{DLP}$), que correlaciona diretamente a energia total depositada no paciente com o volume escaneado de comprimento $L$, é definido como:

$$
\text{DLP} = \text{CTDI}_{\text{vol}} \times L
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

O controle de qualidade rigoroso é o alicerce operacional para a validação clínica de algoritmos avançados de reconstrução e protocolos de varredura. Com a transição generalizada de algoritmos tradicionais de Retroprojeção Filtrada (FBP) para a Reconstrução Iterativa (IR) e sistemas baseados em Inteligência Artificial — como a Reconstrução Baseada em Aprendizado Profundo (DLR, do inglês *Deep Learning Reconstruction*) —, o escopo do CQ evoluiu significativamente. 

Enquanto a FBP apresentava uma relação linear previsível entre ruído e resolução espacial, os algoritmos de DLR introduzem não-linearidades espaciais complexas. Testes de CQ modernos avaliam se a aplicação de DLR remove artefatos de ruído quântico sem suprimir estruturas anatômicas de baixo contraste ou alterar a textura da imagem (frequentemente avaliada por meio da Análise de Textura baseada no Espectro de Potência de Ruído - *Noise Power Spectrum*, NPS).

Ademais, no contexto da otimização de dose e dosimetria clínica, o monitoramento contínuo dos protocolos automáticos de controle de exposição à radiação (*Automatic Tube Current Modulation* - ATCM) através de rotinas de CQ assegura que o sistema adapte dinamicamente a corrente do tubo à atenuação do paciente sem introduzir desvios na qualidade de imagem esperada. A falha em calibrar adequadamente o sistema de detecção ou os filtros de bowtie resulta em superdosagens desnecessárias ou imagens clinicamente diagnosticadas como inaceitáveis devido a artefatos de feixe endurecido e estrias de ruído severas.

---

## 4. Conexões e Wikilinks

*   [[Tomografia Computadorizada|Tomografia Computadorizada]]
*   [[Métricas de Dose em TC|Dosimetria em Tomografia]]
*   [[CTDI e DLP]]
*   [[Filtros de Reconstrucao e FBP]]
*   [[Reconstrucao Iterativa e Deep Learning em TC]]
*   [[Unidades Hounsfield e Calibracao]]
*   [[Artefatos em Tomografia Computadorizada]]
*   [[Modulation Transfer Function (MTF)|Funcao de Transferencia de Modulacao MTF]]
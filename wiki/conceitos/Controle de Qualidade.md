---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, controle-de-qualidade, metrologia, dosimetria, inteligencia-artificial]
data: 2026-08-25
---

# controle-de-qualidade

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **Controle de Qualidade (CQ)** em Tomografia Computadorizada (TC) constitui um conjunto sistemático e periódico de procedimentos operacionais, físicos, metrológicos e computacionais destinados a garantir que um sistema de imagem produza diagnósticos clinicamente acurados com a menor dose de radiação ionizante exequível e otimizada. Sob a perspectiva da Física Médica e da metrologia das radiações, o CQ atua como a linha de defesa primária contra a degradação instrumental, variações na calibração do gerador de alta tensão, instabilidades no tubo de raios X, descalibração dos conjuntos de detetores de estado sólido (geralmente compostos por cerâmicas de tungstato de cádmio ou gadolínio oxissulfeto) e artefatos induzidos pelo software de reconstrução.

Metrologicamente, o CQ diferencia-se em duas vertentes principais:
1. **Controle de Qualidade de Aceitação (Comissionamento):** Realizado pelo físico médico no momento da instalação do equipamento para verificar o atendimento às especificações contratuais e normativas (ex: IEC, AAPM, ACR).
2. **Controle de Qualidade de Rotina (Desempenho):** Executado em frequências diárias, semanais, mensais ou anuais para monitorar a estabilidade a longo prazo (*drift*) dos parâmetros físicos fundamentais.

Os parâmetros avaliados abrangem a exatidão do número de Tomografia (Unidades Hounsfield - UH), a uniformidade espacial, a resolução de alto e baixo contraste, a linearidade espacial, a espessura de corte nominal e efetiva, a taxa de ruído, e a dosimetria por meio de métricas como o *Computed Tomography Dose Index* ($CTDI_{vol}$) e o *Dose-Length Product* ($DLP$). Com a introdução de algoritmos de Inteligência Artificial (IA) e Reconstrução Baseada em Aprendizado Profundo (*Deep Learning Reconstruction* - DLR), o escopo do CQ expandiu-se para validar a integridade semântica e a ausência de alucinações induzidas por redes neurais na imagem médica.

---

## 2. Formulação Matemática e Propriedades

O ecossistema metrológico do CQ em TC apoia-se em formulações matemáticas rigorosas para quantificar a qualidade da imagem e a dose de radiação.

### A. Linearidade e Exatidão do Número de Tomografia (UH)
O Número de Tomografia $UH(x, y)$ em um pixel $(x,y)$ é definido em função do coeficiente de atenuação linear do material $\mu(x,y)$ em relação à água $\mu_{\text{água}}$ e ao ar $\mu_{\text{ar}}$ para o feixe polienergético de raios X:

$$
\text{UH}(x, y) = 1000 \times \frac{\mu(x, y) - \mu_{\text{água}}}{\mu_{\text{água}} - \mu_{\text{ar}}}
$$

Para fins de CQ, utiliza-se um phantom com inserções de materiais tecidos-equivalentes (osso, acrílico, polietileno, PTFE, água e ar). A regressão linear entre os valores medidos de $\text{UH}$ e os coeficientes de atenuação teóricos deve apresentar um coeficiente de correlação $r \ge 0,99$.

### B. Resolução Espacial de Alto Contraste (Função de Espalhamento de Ponto - PSF e MTF)
A capacidade de distinguir pequenas estruturas de alto contraste é avaliada por meio da **Função de Transferência de Modulação (MTF)**, derivada a partir da Transformada de Fourier da Função de Espalhamento de Ponto ($\text{PSF}$) ou da Função de Espalhamento de Linha ($\text{LSF}$):

$$
\text{MTF}(f) = \left| \int_{-\infty}^{\infty} \text{LSF}(x) e^{-i 2 \pi f x} \, dx \right|
$$

Onde $f$ representa a frequência espacial em pares de linhas por centímetro ($\text{lp/cm}$). No CQ, frequentemente reporta-se a frequência espacial correspondente a $\text{MTF} = 0,10$ ($\text{MTF}_{10\%}$) para determinar o limite de resolução espacial do sistema.

### C. Resolução de Baixo Contraste e Relação Sinal-Ruído (SNR)
A capacidade de detecção de objetos com pequenas diferenças de densidade em relação ao fundo é quantificada pela **Relação Sinal-Ruído ($\text{SNR}$)** e pela **Contraste-Ruído-Relação ($\text{CNR}$)**:

$$
\text{SNR} = \frac{\mu_{\text{s}}}{\sigma_{\text{s}}}
\text{CNR} = \frac{|\mu_{\text{s}} - \mu_{\text{f}}|}{\sigma_{\text{f}}}
$$

Onde $\mu_{\text{s}}$ e $\mu_{\text{f}}$ são os valores médios de $\text{UH}$ no sinal (objeto) e no fundo, respectivamente, e $\sigma_{\text{f}}$ é o desvio padrão do ruído medido em uma região de interesse (*ROI*) homogênea no fundo.

### D. Dosimetria: $CTDI_{w}$ e $CTDI_{vol}$
A dose de radiação é parametrizada pelo Índice de Dose de Tomografia Computadorizada Ponderado ($CTDI_{w}$), calculado a partir de medições com câmara de ionização tipo *pencil* de 100 mm em phantoms cilíndricos de polimetilmetacrilato (PMMA) de 16 cm (cabeça) e 32 cm (corpo):

$$
CTDI_{w} = \frac{1}{3} CTDI_{100,\text{centro}} + \frac{2}{3} CTDI_{100,\text{periferia}}
$$

O $CTDI_{vol}$, que contabiliza o espaçamento entre os cortes ou o avanço da mesa através do *Pitch* ($p$), é expresso por:

$$
CTDI_{vol} = \frac{CTDI_{w}}{p}
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

O controle de qualidade transcende a mera conformidade regulatória; ele é o alicerce da **otimização radiológica** (princípio ALARA - *As Low As Reasonably Achievable*). 

* **Validação de Algoritmos de Reconstrução Avançados:** Com a transição de métodos analíticos como a Retroprojeção Filtrada (FBP) para a Reconstrução Iterativa (IR) e DLR, o CQ moderno exige phantoms avançados capazes de avaliar texturas de ruído, resolução espacial dependente da dose e a preservação de estruturas anatômicas sutis. Redes neurais artificiais utilizadas para redução de ruído ou super-resolução podem introduzir artefatos sutis ("alucinações") que não são detectados por métricas tradicionais de ruído, exigindo testes de CQ baseados em observadores computacionais e texturais (ex: *Power Spectrum Analysis* - NPS).
* **Controle de Dose e Gestão de Risco:** Protocolos de CQ asseguram que sistemas de controle automático de exposição (*Automatic Exposure Control* - AEC) operem dentro de margens seguras, modulando a corrente do tubo ($mA$) em função do diâmetro e atenuação do paciente sem comprometer a diagonsabilidade.
* **Mitigação de Artefatos:** Testes diários de calibração de ar (*air calibration*) mitigam artefatos em anel (*ring artifacts*) causados por descalibração ou falha individual de elementos de detetores.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|tomografia-computadorizada]]
* [[Fisica Medica|fisica-medica]]
* [[Reconstrução de Imagem|reconstrucao-de-imagem]]
* [[dosimetria-de-radiacao]]
* [[Inteligência Artificial em Saúde|inteligencia-artificial-em-saude]]
* [[Unidades Hounsfield|unidades-hounsfield]]
* [[Filtro de Reconstrução|filtro-de-reconstrucao]]
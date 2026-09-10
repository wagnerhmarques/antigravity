---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, controle-de-qualidade, metrologia, dosimetria, inteligencia-artificial]
data: 2026-08-25
---

# fantasmas-em-tomografia-computadorizada

## 1. Definição Conceitual e Fundamentação Física / Metrológica

Os **fantasmas em Tomografia Computadorizada (TC)** são dispositivos físicos simuladores, construídos com materiais cujas propriedades de atenuação à radiação X (número atômico efetivo $Z_{\text{eff}}$ e densidade mássica $\rho$) mimetizam os tecidos biológicos humanos. Na física médica e na metrologia em radiodiagnóstico, os fantasmas são instrumentos fundamentais para a padronização, calibração, controle de qualidade (CQ) e otimização de sistemas de imagem por TC.

Do ponto de vista físico, a imagem de TC é uma representação espacial dos coeficientes de atenuação linear macroscópicos ($\mu$) mapeados em unidades Hounsfield (HU). Para que esses valores sejam quantitativamente acurados e reprodutíveis entre diferentes fabricantes e protocolos de escaneamento, o sistema de aquisição e reconstrução deve ser periodicamente auditado utilizando geometrias padronizadas. Os fantasmas fornecem essa referência estática e conhecida, eliminando as variáveis biológicas e permitindo isolar artefatos, avaliar a resolução espacial (através da função de transferência de modulação - FTM ou *MTF*), a resolução de baixo contraste, o ruído textural, a dose de radiação absorvida e a exatidão do número de TC.

Com o advento da reconstrução iterativa (IR) e de algoritmos baseados em inteligência artificial (como redes neurais profundas para *Deep Learning Reconstruction* - DLR), o papel dos fantasmas evoluiu. Hoje, eles não servem apenas para métricas tradicionais de CQ, mas também para validar a preservação de detalhes anatômicos sutis frente à redução severa de dose, evitando a alucinação de texturas ou a remoção excessiva de ruído que possa mascarar patologias reais.

## 2. Formulação Matemática e Propriedades (se aplicável)

A calibração e a avaliação de desempenho utilizando fantasmas fundamentam-se na relação entre o coeficiente de atenuação linear do material do fantasma ($\mu$) e os valores numéricos gerados na imagem, conhecidos como Unidades Hounsfield ($\text{HU}$). A conversão é dada por:

$$
\text{HU} = 1000 \times \frac{\mu - \mu_{\text{água}}}{\mu_{\text{água}} - \mu_{\text{ar}}}
$$

Onde $\mu_{\text{água}}$ e $\mu_{\text{ar}}$ representam os coeficientes de atenuação linear da água pura e do ar nas condições efetivas do feixe de raios X policromático.

Para avaliar o **ruído da imagem** e a sua textura, mede-se o desvio padrão ($\sigma$) dos valores de pixel em uma região de interesse (ROI) circular central colocada sobre um inserto homogêneo do fantasma:

$$
\sigma_{\text{ROI}} = \sqrt{\frac{1}{N - 1} \sum_{i=1}^{N} (\text{HU}_i - \overline{\text{HU}})^{2}}
$$

Onde $N$ é o número de pixels na ROI, $\text{HU}_i$ é o valor de pixel individual e $\overline{\text{HU}}$ é a média dos valores na ROI.

A **Resolução Espacial** é frequentemente quantificada através da Função de Espalhamento de Ponto (*Point Spread Function* - PSF) ou da sua transformada de Fourier, a Função de Transferência de Modulação ($\text{MTF}$), calculada a partir de bordas afiadas ou fios finos (geralmente de tungstênio) embutidos no fantasma:

$$
\text{MTF}(f) = \left| \frac{\mathcal{F}\{\text{PSF}(x, y)\}}{\mathcal{F}\{\text{PSF}(x, y)\}\Big|_{f=0}} \right|
$$

Onde $f$ representa a frequência espacial em pares de linhas por centímetro ($\text{lp/cm}$).

A **Linearidade do Número de TC** é validada ajustando uma regressão linear entre os valores medidos de $\text{HU}$ de diversos insertos do fantasma (por exemplo, tecidos simulados como osso cortical, osso trabecular, fígado, gordura, pulmão) e seus respectivos coeficientes de atenuação teóricos conhecidos, avaliando o coeficiente de determinação ($R^2$) e o desvio máximo aceitável (geralmente dentro de $\pm 4 \text{ HU}$ para água e $\pm 40 \text{ HU}$ para tecidos de alto número atômico).

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

*   **Controle de Qualidade Regulatório (CQ):** Testes rotineiros diários, semanais e anuais exigidos por agências reguladoras (como a ANVISA no Brasil ou órgãos internacionais como o ACR e a AAPM) utilizam fantasmas padronizados (ex: fantasma do *American College of Radiology*) para assegurar a constância da dose, uniformidade, espessura de corte e alinhamento do feixe.
*   **Dosimetria Avançada:** Fantasmas antropomórficos seccionados (*sectioned phantoms*), equipados com câmaras de ionização do tipo *pencil beam* ou dosímetros termoluminescentes (DTLs) e luminescência opticamente estimulada (OSL), permitem mapear a distribuição tridimensional da dose absorvida em órgãos de risco, viabilizando cálculos precisos para protocolos de otimização de dose (*Diagnostic Reference Levels* - DRLs).
*   **Validação de Algoritmos de Reconstrução e DLR:** Com a introdução de modelos de Inteligência Artificial na reconstrução de imagens, os fantasmas texturais (como o fantasma MITA Перфурманс ou fantasmas customizados com padrões fractais e de baixo contraste) são essenciais. Eles permitem quantificar a capacidade de detecção de lesões hepáticas hipodensas ou nódulos pulmonares sob condições de baixa dose, calculando métricas avançadas como a Curva ROC do Observador Humano e do Observador Computacional (IO - *Ideal Observer* e *Channelized Hotelling Observer*).
*   **Mitigação de Artefatos:** Fantasmas específicos com inserções metálicas ou geometrias complexas são empregados para testar algoritmos de correção de artefatos de enrijecimento de feixe (*beam hardening*) e de artefatos metálicos (MAR / iMAR).

## 4. Conexões e Wikilinks

*   [[Unidades Hounsfield|unidades-hounsfield]]
*   [[Modulation Transfer Function (MTF)|funcao-de-transferencia-de-modulacao-mtf]]
*   [[filtros-e-kernels-de-reconstrucao]]
*   [[Reconstrução Iterativa|reconstrucao-iterativa-e-dlr]]
*   [[Controle de Qualidade em TC|controle-de-qualidade-em-tc]]
*   [[Dosimetria em Radiologia|dosimetria-em-tomografia-computadorizada]]
*   [[Artefatos em Tomografia Computadorizada|artefatos-em-tomografia-computadorizada]]
---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, controle-de-qualidade, metrologia, otimizacao-da-dose, inteligencia-artificial]
data: 2026-08-25
---

# garantia-de-qualidade

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Garantia de Qualidade (GQ)** em Tomografia Computadorizada (TC) constitui o conjunto abrangente de operações, protocolos e testes sistemáticos projetados para garantir que um sistema de imagem produza, de forma consistente e reprodutível, diagnósticos de máxima acurácia com a menor dose de radiação ionizante clinicamente aceitável para o paciente. Do ponto de vista metrológico, a GQ fundamenta-se nos princípios da rastreabilidade instrumental, calibração e controle estatístico de processos, assegurando que as grandezas físicas mensuradas — como o Número de Hounsfield (HU), a resolução espacial, a modulação da função de transferência (MTF) e o ruído quântico — permaneçam dentro de tolerâncias estritas estabelecidas por órgãos reguladores internacionais (como a *International Atomic Energy Agency* - IAEA, o *American College of Radiology* - ACR e a *International Electrotechnical Commission* - IEC).

A fundamentação física da GQ envolve a avaliação de parâmetros fundamentales da interação radiação-matéria e da cadeia de aquisição e processamento de sinal. O sistema de TC mede o coeficiente de atenuação linear efetivo $\mu(x,y)$ do voxel, o qual é convertido no Número de Hounsfield ($HU$) através da seguinte relação de calibração padrão:

$$
HU = 1000 \times \frac{\mu - \mu_{\text{água}}}{\mu_{\text{água}} - \mu_{\text{ar}}}
$$

A estabilidade metrológica desta escala requer testes periódicos utilizando fantomas (phantoms) antropomórficos ou geométricos padronizados, compostos por materiais equivalentes a tecidos biológicos. A degradação do sistema, decorrente do desgaste do tubo de raios X (p.ex., corrosão do anodo, instabilidade focal), flutuações no gerador de alta tensão ou desalinhamento dos arranjos de detetores de estado sólido (geralmente compostos por tungstato de cádmio ou cerâmicas cintiladoras acopladas a fotodiodos), manifesta-se imediatamente como artefatos de imagem ou desvios na calibração quantitativa, os quais são mitigados pelos protocolos de GQ.

---

## 2. Formulação Matemática e Propriedades (se aplicável)

A quantificação do desempenho físico em protocolos de GQ baseia-se em métricas estatísticas e funcionais rigorosas. 

### A. Ruído e Uniformidade da Imagem
O ruído da imagem ($\sigma_{HU}$) é avaliado estatisticamente pelo desvio padrão dos valores de $HU$ em uma região de interesse (ROI) central posicionada sobre um meio homogêneo (água):

$$
\sigma_{HU} = \sqrt{\frac{1}{N - 1} \sum_{i=1}^{N} \left( HU_i - \overline{HU} \right)^2}
$$

Onde $N$ representa o número total de pixels na ROI, $HU_i$ é o valor de pixel individual e $\overline{HU}$ é a média aritmética. A uniformidade espacial é avaliada comparando-se os valores médios de $HU$ obtidos em ROIs periféricas (norte, sul, leste, oeste) com a ROI central, quantificada por:

$$
\Delta_{uni} = \left| \overline{HU}_{\text{periférica}} - \overline{HU}_{\text{central}} \right|
$$

### B. Resolução Espacial e Função de Modulação de Transferência (MTF)
A capacidade do sistema em discernir estruturas anatômicas de pequeno porte é caracterizada pela Função de Espalhamento de Ponto (PSF) ou pela Função de Espalhamento de Linha (LSF). A MTF é formalmente definida como o módulo da transformada de Fourier da PSF normalizada:

$$
\text{MTF}(f) = \left| \mathcal{F} \left\{ \text{PSF}(x, y) \right\} \right|
$$

Em testes de rotina de GQ, a frequência espacial correspondente à queda da MTF para 50% ou 10% de seu valor máximo ($\text{MTF}_{50}$ e $\text{MTF}_{10}$) serve como indicador primário da degradação da focalização do feixe ou de alterações nos filtros de retroprojeção filtrada (FBP).

### C. Relação Sinal-Ruído (SNR) e Contraste-Ruído (CNR)
Para avaliar a detectabilidade de lesões de baixo contraste, utiliza-se a Razão Contraste-Ruído, expressa por:

$$
\text{CNR} = \frac{\left| S_{\text{alvo}} - S_{\text{fundo}} \right|}{\sigma_{\text{fundo}}}
$$

Onde $S_{\text{alvo}}$ e $S_{\text{fundo}}$ representam os sinais médios no objeto de interesse e no tecido circundante, respectivamente, e $\sigma_{\text{fundo}}$ é o desvio padrão do ruído no fundo.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A GQ moderna transcende o escopo tradicional de inspeção mecânica e elétrica, integrando-se profundamente com as técnicas avançadas de reconstrução de imagem e inteligência artificial:

1. **Controle em Cadeias de Reconstrução Híbridas e Iterativas (IR):** Algoritmos iterativos reduzem o ruído dependente da dose, mas podem alterar a textura da imagem ("aparência plástica"). Os programas de GQ monitoram a textura espacial através de análise de espectro de potência de ruído (NPS - *Noise Power Spectrum*), assegurando que o processamento iterativo preserve a detectabilidade de lesões sutis.
2. **Validação de Reconstruções Baseadas em Aprendizado Profundo (DLR):** Sistemas de DLR aplicados à supressão de ruído e super-resolução exigem protocolos de GQ dinâmicos. Os testes validam se as redes neurais não introduzem artefatos alucinatórios ou distorções métricas nos valores de $HU$, mantendo a fidelidade quantitativa essencial para oncologia (avaliação de resposta ao tratamento por perfusão e volumetria).
3. **Otimização da Dose e Dosimetria Computacional:** A GQ avalia rotineiramente métricas dosimétricas como o Índice de Dose em Tomografia Computadorizada ($CTDI_{vol}$) e o Produto Dose-Comprimento ($DLP$). A integração com softwares de monitoramento de dose permite ajustar curvas de modulação de corrente automática no eixo $x-y-z$, otimizando o balanço estrito entre o Princípio ALARA (*As Low As Reasonably Achievable*) e a qualidade diagnóstica.
4. **Observer Models (Observadores Computacionais):** A GQ contemporânea incorpora modelos de observadores humanos e matemáticos (como o *Non-Pre-Embedding Hotelling Observer* e o *Channelized Hotelling Observer* - CHO) para prever o desempenho diagnóstico em tarefas específicas de detecção de lesões, automatizando a aprovação de novos protocolos clínicos.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|tomografia-computadorizada]]
* [[Unidades Hounsfield|numero-de-hounsfield]]
* [[Modulation Transfer Function (MTF)|funcao-de-transferencia-de-modulacao]]
* [[Dosimetria em TC|dosimetria-em-tc]]
* [[Reconstrução Iterativa|reconstrucao-iterativa]]
* [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction]]
* [[Radioproteção|principio-alara]]
* [[Ruído Quântico|ruido-quantico]]
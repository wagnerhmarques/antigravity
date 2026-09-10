---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, controle-de-qualidade, inteligencia-artificial, metrologia]
data: 2026-08-25
---

# Software_Testes

## 1. Definição Conceitual e Fundamentação Física / Metrológica

No contexto da Física Médica e da Tomografia Computadorizada (TC) moderna, o termo **Software de Testes** (ou ferramentas computacionais de controle de qualidade automatizado e avaliação metrológica) refere-se ao conjunto de algoritmos, plataformas e sistemas computacionais projetados para verificar, quantificar e auditar o desempenho físico, geométrico\, dosimétrico e algorítmico de sistemas de imagem por TC. 

Com a transição dos sistemas de aquisição convencionais para arquiteturas altamente complexas — envolvendo reconstrução iterativa avançada (IR) e reconstrução baseada em aprendizado profundo (Deep Learning Reconstruction - DLR) —, os métodos tradicionais de controle de qualidade (CQ) baseados em inspeção visual e análise manual de fantasmas (*phantoms*) tornaram-se insuficientes. Os softwares de teste modernos incorporam metodologias rigorosas de processamento de imagem digital, análise de Fourier, teoria de sistemas lineares e inteligência artificial para extração automatizada de métricas de qualidade de imagem (IQA).

Do ponto de vista metrológico, esses softwares atuam como padrões secundários ou ferramentas de rastreabilidade para assegurar a conformidade com normativas internacionais (como IEC 60601-2-44, AAPM TG-233, TG-200 e ACR). Eles minimizam a variabilidade inter-observador, permitem a avaliação de parâmetros complexos como a Função de Transferência de Modulação (MTF), a Função de Espalhamento de Ponta (PSF), o Ruído de Wiener (Spectrally Defined Noise Power - NPS), a Detectabilidade de Baixo Contraste (Low Contrast Detectability - LCD) através de observadores modelo baseados em $d'$, e a precisão espacial em três dimensões.

---

## 2. Formulação Matemática e Propriedades

Os softwares de teste utilizam modelos matemáticos avançados para caracterizar o desempenho dos sistemas de TC. Abaixo estão as formulações fundamentais implementadas computacionalmente para a avaliação da qualidade de imagem:

### Função de Transferência de Modulação (MTF) via Borda (*Edge Method*)
A MTF é calculada a partir da derivada da função de resposta ao degrau (Edge Spread Function - ESF) obtida de uma interface de alto contraste (ex: teflon/ar no fantoma). Seja $ESF(x) o perfil espacial medido perpendicularmente à borda. A Linha de Espalhamento de Ponta (PSF) é obtida por diferenciação numérica:

$$
PSF(x) = \frac{d}{dx} \left[ ESF(x) \right]
$$

A MTF é, portanto, o módulo da Transformada de Fourier unidimensional da PSF normalizada:

$$
MTF(f) = \left| \frac{\int_{-\infty}^{\infty} PSF(x) e^{-j 2 \pi f x} dx}{\int_{-\infty}^{\infty} PSF(x) dx} \right|
$$

Onde $f$ representa a frequência espacial em pares de linhas por centímetro ($\text{lp/cm}$).

### Espectro de Potência do Ruído (NPS)
Para avaliar a textura e a magnitude espacial do ruído em imagens de TC, o software calcula o NPS bidimensional a partir de regiões de interesse (ROI) homogêneas em imagens de fantasmas de água ou acrílico. Seja $I(x, y)$ a matriz de intensidade da ROI e $\bar{I}$ a média global da ROI, a imagem de ruído residual é definida como $\Delta I(x, y) = I(x, y) - \bar{I}$. O NPS 2D é computado como:

$$
NPS(f_x, f_y) = \frac{\Delta x \Delta y}{N_x N_y} \left| \sum_{x=0}^{N_x-1} \sum_{y=0}^{N_y-1} \left[ \Delta I(x, y) \right] e^{-j 2 \pi (f_x x + f_y y)} \right|^2
$$

Onde $\Delta x$ e $\Delta y$ são os tamanhos dos pixels, e $N_x, N_y$ são as dimensões da matriz da ROI.

### Detectabilidade de Baixo Contraste Baseada em Observador Modelo ($d'$ - Index)
A avaliação da detectabilidade visual é substituída em softwares modernos por métricas objetivas como a Detectabilidade Indexada ($d'$), que correlaciona a física do sistema com a performance de observadores humanos ideais ou humanos-canal:

$$
d' = \frac{\left| \iint W(f_x, f_y) \cdot S(f_x, f_y) \, df_x \, df_y \right|^2}{\iint W(f_x, f_y)^2 \cdot NPS(f_x, f_y) \, df_x \, df_y + \sigma_{add}^2}
$$

Onde $S(f_x, f_y)$ é a Transformada de Fourier do sinal (objeto de baixo contraste a ser detectado), $W(f_x, f_y)$ é a função de ponderação do canal (filtro visual do observador), e $\sigma_{add}^2$ representa o ruído interno adicional do observador.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

No fluxo de trabalho clínico e de pesquisa em Tomografia Computadorizada, os **Softwares de Testes** desempenham papéis críticos:

1. **Controle de Qualidade Automatizado (Auto-QC):** Permitem a execução diária ou semanal de testes de constância sem intervenção humana direta na análise. O técnico posiciona o fantoma padronizado, realiza a varredura com protocolos clínicos e o software processa os dados em segundo plano, enviando alertas automáticos caso a deriva (*drift*) de parâmetros como Número CT (unidades Hounsfield), uniformidade, ruído ou resolução espacial ultrapasse os limites de tolerância estabelecidos.
2. **Auditoria de Algoritmos de Reconstrução Avançada:** Com a proliferação de algoritmos de reconstrução iterativa (IR) e inteligência artificial (DLR), a relação sinal-ruído e a resolução espacial tornam-se dependentes do nível de dose e do contraste da lesão (não-linearidade espacial). Softwares de teste especializados são essenciais para mapear a degradação ou preservação de detalhes finos sob diferentes doses de radiação ($CTDIvol$).
3. **Otimização de Protocolos e Dosimetria:** Auxiliam físicos médicos a correlacionar a dose absorvida pelo paciente com a qualidade diagnóstica objetiva ($d'$ e MTF), permitindo o ajuste fino dos parâmetros de aquisição (kVp, mAs modulado, pitch e espessura de corte) para atingir o princípio ALARA (*As Low As Reasonably Achievable*).
4. **Validação de Modelos de Inteligência Artificial:** Em ambientes de pesquisa, ferramentas de software testam a robustez de redes neurais convolucionais (CNNs) e modelos gerativos aplicados à redução de artefatos, segmentação automática de órgãos e predição de dose, garantindo que não ocorra a alucinação de estruturas anatômicas durante o processamento de imagem.

---

## 4. Conexões e Wikilinks

* [[Controle de Qualidade em TC|Controle_Qualidade_TC]]
* [[Função Transferencia Modulacao|Funcao_Transferencia_Modulacao]]
* [[Espectro Potencia Ruído|Espectro_Potencia_Ruido]]
* [[Reconstrução Iterativa|Reconstrucao_Iterativa]]
* [[Deep Learning Image Reconstruction (DLR)|Deep_Learning_Reconstruction]]
* [[Dosimetria CTDI|Dosimetria_CTDI]]
* [[Fantasmas TC|Fantasmas_TC]]
* [[Otimização Dose|Otimizacao_Dose]]
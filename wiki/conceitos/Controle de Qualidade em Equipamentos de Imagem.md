---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, controle-de-qualidade, metrologia, radioprotecao, dosimetria, inteligencia-artificial]
data: 2026-08-25
---

# Controle de Qualidade em Equipamentos de Imagem

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **Controle de Qualidade (CQ) em Equipamentos de Imagem** constitui um conjunto sistemático e normatizado de procedimentos operacionais, físicos, metrológicos e computacionais destinados a garantir que sistemas de diagnóstico por imagem — com ênfase particular em Tomografia Computadorizada (TC) — operem com o máximo desempenho diagnóstico, reprodutibilidade metrológica e estrita adesão aos princípios de radioproteção (*As Low As Reasonably Achievable* - ALARA). 

Do ponto de vista metrológico, o CQ fundamenta-se na rastreabilidade de grandezas físicas fundamentais (tais como kerma no ar, dose absorvida, número de Hounsfield, modulação da função de transferência e tempo de varredura) a padrões nacionais e internacionais de medida. A degradação intrínseca de componentes de hardware do sistema de imagem — como a descalibração focal do tubo de raios X, o desgaste térmico e mecânico do conjunto ânodo-cátodo, o envelhecimento dos cintiladores detectores de alta densidade (por exemplo, granada de ítrio e gadolínio - GOS ou tungstato de cádmio - $\text{CdWO}_4$) e o descasamento dos canais de conversão analógica-digital (ADC) — introduz artefatos sistemáticos e degrada a acurácia quantitativa das imagens.

O programa de CQ divide-se classicamente em:
1. **Controle de Aceitação**: Realizado na instalação do equipamento para verificar o atendimento às especificações contratuais e regulatórias.
2. **Controle de Estado (ou Desempenho)**: Avaliação periódica ampla para assegurar que o equipamento mantém suas características operacionais ótimas ao longo do tempo.
3. **Controle de Rotina (ou Constância)**: Testes diários ou semanais de alta sensibilidade para detecção precoce de falhas catastróficas ou desvios drásticos de calibração.

---

## 2. Formulação Matemática e Propriedades

A avaliação cuantitativa do desempenho de sistemas de tomografia computadorizada no contexto do CQ exige o tratamento rigoroso de métricas físicas de ruído, resolução espacial e densidade. 

### Relação Sinal-Ruído (SNR) e Desvio Padrão do Número de Hounsfield ($\text{HU}$)
O número de Hounsfield é definido linearmente com base no coeficiente de atenuação linear do tecido ($𝜇$) em relação à água ($\mu_{\text{água}}$) e ao ar ($\mu_{\text{ar}}$):

$$
\text{HU} = 1000 \times \frac{\mu - \mu_{\text{água}}}{\mu_{\text{água}} - \mu_{\text{ar}}}
$$

O ruído da imagem em uma região de interesse homogênea (ROI) é quantificado pelo desvio padrão ($\sigma_{\text{HU}}$) dos pixels internos à ROI:

$$
\sigma_{\text{HU}} = \sqrt{\frac{1}{N-1} \sum_{i=1}^{N} \left( \text{HU}_i - \overline{\text{HU}} \right)^2}
$$

Onde $N$ é o número total de pixels na amostra e $\overline{\text{HU}}$ é o valor médio de atenuação na ROI.

### Função de Espalhamento de Ponto (PSF) e Função de Transferência de Modulação (MTF)
A resolução espacial é formalmente caracterizada pela **Função de Espalhamento de Ponto (PSF - *Point Spread Function*)**, que representa a resposta do sistema a uma fonte pontual ideal. No domínio espacial bi-dimensional, a PSF, denotada por $PSF(x,y)$, sofre transformações devido à geometria de varredura e aos filtros de reconstrução. 

Aplicando a Transformada de Fourier bidimensional $\mathcal{F}\{\cdot\}$, obtém-se a **Função de Transferência Optical/Spatial de Modulação (MTF - *Modulation Transfer Function*)**:

$$
\text{MTF}(f_x, f_y) = \left| \iint_{-\infty}^{\infty} PSF(x,y) e^{-j 2\pi (f_x x + f_y y)} \, dx \, dy \right|
$$

Em testes práticos de CQ, frequentemente utiliza-se a derivada da Função de Espalhamento de Borda (*Edge Spread Function* - ESF) para estimar a *Line Spread Function* (LSF), cuja transformada de Fourier unidimensional gera a $\text{MTF}(f)$:

$$
\text{LSF}(x) = \frac{d}{dx} \left[ \text{ESF}(x) \right]
\text{MTF}(f) = \left| \int_{-\infty}^{\infty} \text{LSF}(x) e^{-j 2\pi f x} \, dx \right|
$$

### Dosimetria: CTDI e $DLP$
A métrica fundamental de entrega de dose em Tomografia Computadorizada é o **Índice de Dose em Tomografia Computadorizada (CTDI - *Computed Tomography Dose Index*)**, medido no interior de fantasmas cilíndricos de acrílico padrão (16 cm para crânio e 32 cm para abdômen/corpo):

$$
\text{CTDI}_{\text{w}} = \frac{1}{3} \text{CTDI}_{\text{centro}} + \frac{2}{3} \text{CTDI}_{\text{periferia}}
$$

Para contabilizar o efeito do passo helicoidal (*pitch* $p$), define-se o $\text{CTDI}_{\text{vol}}$:

$$
\text{CTDI}_{\text{vol}} = \frac{\text{CTDI}_{\text{w}}}{p}
$$

O **Produto Dose-Comprimento (DLP - *Dose-Length Product*)** integra a dose ao longo do eixo longitudinal $z$ do paciente para uma varredura de comprimento $L$:

$$
\text{DLP} = \text{CTDI}_{\text{vol}} \times L
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

O CQ atua como a infraestrutura crítica de segurança e eficácia diagnóstica em parques de imagem avançados. Suas aplicações diretas englobam:

* **Otimização de Protocolos de Reconstrução**: Com a transição de algoritmos tradicionais de Retroprojeção Filtrada (FBP) para a Reconstrução Iterativa (IR) e algoritmos baseados em Inteligência Artificial / Aprendizado Profundo (*Deep Learning Reconstruction* - DLR), o CQ deve validar se a redução de ruído promovida por DLR não resulta na supressão de microestruturas patológicas (por exemplo, nódulos pulmonares subsólidos ou microcalcificações mamográficas).
* **Monitoramento Quantitativo em Oncologia e Perfusão**: A radiômica e a quantificação longitudinal de volumes tumorais dependem criticamente da estabilidade do número de Hounsfield. Desvios de calibração menores que 5 $\text{HU}$ podem alterar significativamente a classificação textural de lesões em modelos preditivos de IA.
* **Controle de Qualidade Automatizado por IA (AI-QC)**: Sistemas modernos de TC incorporam rotinas de CQ embutidas que utilizam simuladores virtuais e redes neurais para analisar diária e autonomamente o ruído eletrônico, a uniformidade do campo de fótons e a deriva dos detectores, minimizando a necessidade de intervenção humana física com fantasmas (*phantoms*).

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[Física das Radiações|Física da Radiação]]
* [[Dosimetria em Radiologia]]
* [[Reconstrução de Imagem]]
* [[Filtros de Reconstrução e Processamento]]
* [[Inteligencia Artificial IA|Inteligência Artificial em Imagem Médica]]
* [[Artefatos em Tomografia Computadorizada]]
* [[Radioproteção e Otimização]]
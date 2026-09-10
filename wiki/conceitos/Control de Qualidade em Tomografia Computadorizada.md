---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, controle-de-qualidade, metrologia, dosimetria, inteligencia-artificial]
data: 2026-08-25
---

# Control de Qualidade em Tomografia Computadorizada

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **Control de Qualidade (CQ) em Tomografia Computadorizada (TC)** constitui o conjunto sistemático de procedimentos físicos, metrológicos e operacionais projetados para garantir que um sistema de TC produza consistentemente imagens diagnósticas de alta qualidade com o mínimo de dose de radiação ionizante necessária, mantendo a segurança do paciente e da equipe. Do ponto de vista metrológico, o CQ fundamenta-se na rastreabilidade de grandezas físicas — como o Kerma no ar, o Índice de Dose em Tomografia Computadorizada ($\text{CTDI}$), o Ruído Quântico, a Função de Resposta ao Ponto ($\text{PSF}$) e a Função de Transferência de Modulação ($\text{MTF}$) — em relação aos padrões primários de laboratórios metrológicos nacionais e internacionais.

O processo de CQ divide-se classicamente em testes de aceitação (comissionamento), testes de estado (periódicos) e controle de qualidade rotineiro (diário). Com a evolução tecnológica introduzida pela [[Reconstrução Iterativa|Reconstrução Iterativa (IR)]] e por algoritmos baseados em [[Inteligência Artificial e Deep Learning em TC (DLR)]], o CQ moderno transcendeu a mera avaliação visual de simuladores (phantoms) de acrílico ou água, incorporando avaliações quantitativas automatizadas de texturas de imagem, resolução de baixo contraste em frequências espaciais complexas e a estabilidade de redes neurais profundas frente a desvios de calibração do scanner (drift).

## 2. Formulação Matemática e Propriedades

A avaliação quantitativa da qualidade de imagem e da dosimetria em TC depende de formulações matemáticas rigorosas aplicadas sobre imagens de phantoms padronizados.

### 2.1 Dosimetria e o Índice CTDI
A grandeza básica para dosimetria em TC é o Índice de Dose em Tomografia Computadorizada ($\text{CTDI}$), definido a partir da integração do perfil de dose axial $D(z)$ ao longo do eixo de rotação $z$, normalizado pelo comprimento de colimação nominal $N \cdot T$:

$$
\text{CTDI}_{100} = \frac{1}{N \cdot T} \int_{-50\,\text{cm}}^{+50\,\text{cm}} D(z) \, dz
$$

Onde $N$ é o número de canais de detetores ativos e $T$ é a espessura do tom individual no isocentro. Para estimar a dose média na seção transversal do phantom cilíndrico de Polimetilmetacrilato (PMMA), utiliza-se o $\text{CTDI}_{\text{w}}$ (Weighted CTDI):

$$
\text{CTDI}_{\text{w}} = \frac{1}{3} \text{CTDI}_{100,\text{centro}} + \frac{2}{3} \text{CTDI}_{100,\text{periferia}}
$$

Para protocolos helicoidais, o fator de ponderação temporal/espacial é incorporado através do produto dose-comprimento ($\text{DLP}$):

$$
\text{DLP} = \text{CTDI}_{\text{vol}} \cdot L_{\text{scan}} = \left( \frac{\text{CTDI}_{\text{w}}}{\text{pitch}} \right) \cdot L_{\text{scan}}
$$

Onde $\text{CTDI}_{\text{vol}}$ representa a dose nominal normalizada pelo avanço da mesa ($\text{pitch}$), e $L_{\text{scan}}$ é o comprimento total escaneado.

### 2.2 Ruído, Textura e Resolução Espacial
O ruído da imagem ($\sigma$), avaliado tipicamente como o desvio padrão dos números de Hounsfield ($\text{HU}$) em uma região de interesse ($\text{ROI}$) homogênea de um phantom de água, é expresso por:

$$
\sigma = \sqrt{\frac{1}{N-1} \sum_{i=1}^{N} (\text{HU}_i - \overline{\text{HU}})^2}
$$

A resolução espacial é caracterizada pela Função de Transferência de Modulação ($\text{MTF}$), obtida através da transformada de Fourier da $\text{PSF}$ ou pelo método da borda inclinada (*slanted-edge method*):

$$
\text{MTF}(f) = \frac{|\mathcal{F}\{\text{PSF}(x,y)\}|}{|\mathcal{F}\{\text{PSF}(0,0)\}|}
$$

Onde $f$ representa a frequência espacial em pares de linhas por centímetro ($\text{lp/cm}$). A frequência de corte correspondente a $\text{MTF} = 0.1$ (ou $10\%$) é frequentemente utilizada como métrica de limite de resolução espacial de alta contrastagem.

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

O CQ desempenha um papel central na garantia da conformidade regulatória e na otimização clínica na era da [[Tomografia Computadorizada de Múltiplas Fontes e Detectores (MDCT)]] e dos sistemas de contagem de fótons ([[Tomografia Computadorizada por Contagem de Fótons (PCCT)]]). 

1. **Otimização do Balanço Dose-Qualidade:** Através de testes periódicos, os físicos médicos validam o desempenho dos sistemas de controle automático de exposição ($\text{CARE Dose}$, $\text{Imdose}$, etc.), garantindo que a corrente do tubo ($mA$) seja modulada de forma ideal de acordo com a atenuação do paciente.
2. **Monitoramento de Algoritmos Avançados:** Com a introdução de modelos de [[Reconstrução Iterativa|Reconstrução Iterativa (IR)]] e [[Inteligência Artificial e Deep Learning em TC (DLR)]], o CQ passou a monitorar artefatos induzidos por inteligência artificial, como a supressão excessiva de texturas (efeito "plástico" ou perda de resolução de baixo contraste), assegurando que redes neurais treinadas não introduzam viéses diagnósticos.
3. **Avaliação Metrológica de Unidades Hounsfield:** A constância da calibração numérica para água ($0\,\text{HU}$) e ar ($-1000\,\text{HU}$) é imperativa para a exatidão de exames de perfusão cerebral, quantificação de nódulos pulmonares e densitometria óssea quantitativa ([[QCT]]).

## 4. Conexões e Wikilinks

* [[Índice de Dose em Tomografia Computadorizada (CTDI)]]
* [[Função de Transferência de Modulação (MTF) em TC]]
* [[Reconstrução Iterativa|Reconstrução Iterativa (IR)]]
* [[Inteligência Artificial e Deep Learning em TC (DLR)]]
* [[Tomografia Computadorizada por Contagem de Fótons (PCCT)]]
* [[Física da Radiação e Dosimetria X]]
* [[Artefatos em Tomografia Computadorizada]]
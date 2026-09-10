---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, qualidade-de-imagem, metrologia, radiologia, inteligencia-artificial]
data: 2026-08-25
---

# Image Quality Metrics

## 1. Definição Conceitual e Fundamentação Física / Metrológica

As **Métricas de Qualidade de Imagem** (do inglês, *Image Quality Metrics* — IQMs) constituem o arcabouço quantitativo e metrológico utilizado para avaliar, caracterizar e otimizar a fidelidade com que um sistema de imagem médica — com ênfase particular na Tomografia Computadorizada (TC) — representa a realidade anatômica e patológica de um objeto escaneado. 

Do ponto de vista da física médica, a qualidade de imagem em TC não é uma entidade absoluta, mas sim um balanço complexo, frequentemente antagônico, regido pelo **Princípio ALARA** (*As Low As Reasonably Achievable*), pela dose de radiação ionizante administrada, pela resolução espacial, pela resolução de contraste e pelo nível de ruído estatístico inerente ao processo de detecção de fótons de raios X.

Historicamente, a avaliação da qualidade de imagem baseava-se em inspeções visuais subjetivas por radiologistas e físicos médicos, utilizando fantasmas (*phantoms*) de teste. Embora essenciais para a percepção humana, tais métodos carecem de reprodutibilidade quantitativa rigorosa. A transição para métricas objetivas permitiu estabelecer padrões metrológicos estritos baseados na Teoria dos Sistemas Lineares Invariantes no Espaço (LSI). Sob essa ótica, um sistema de TC pode ser modelado como um operador linear que mapeia o coeficiente de atenuação linear real do paciente, $\mu(x,y,z)$, na imagem reconstruída, $\hat{\mu}(x,y,z)$, através de uma função de transferência de degradação modulada por ruído quântico e artefatos de reconstrução.

As métricas modernas dividem-se em duas grandes vertentes:
1. **Métricas Físico-Matemáticas Traducionais:** Avaliam propriedades fundamentais do sistema de imagem independentemente do conteúdo anatômico (ex: Função de Espalhamento de Ponta, Ruído de Fundo, Função de Transferência de Modulação).
2. **Métricas Baseadas em Tarefas (*Task-based Image Quality Metrics*):** Avaliam a detectabilidade de um sinal específico de interesse (uma lesão ou microcalcificação) por um observador ideal ou humano, integrando ruído, resolução e a geometria da tarefa diagnóstica.

---

## 2. Formulação Matemática e Propriedades

A rigorosa quantificação da qualidade de imagem em TC requer ferramentas matemáticas avançadas provenientes da análise de Fourier e da estatística estocástica.

### 2.1. Ruído de Imagem e Desvio Padrão
O ruído em TC é primariamente governado pelas estatísticas de Poisson associadas ao número de fótons detectados ($N$). O desvio padrão do ruído ($\sigma$) em uma região de interesse (ROI) homogênea é classicamente expresso como:

$$
\sigma = \sqrt{\frac{1}{N_{pixels}} \sum_{i \in ROI} \left( \hat{\mu}_i - \bar{\mu} \right)^2}
$$

Onde $\hat{\mu}_i$ representa o valor do número CT (em unidades Hounsfield, HU) no pixel $i$, e $\bar{\mu}$ é a média dos números CT na ROI.

### 2.2. Função de Transferência de Modulação (MTF)
A resolução espacial é caracterizada pela **Função de Transferência de Modulação (MTF)**, que descreve a capacidade do sistema de transmitir o contraste de objetos em diferentes frequências espaciais ($u, v$). A MTF é o módulo da Transformada de Fourier bidimensional da Função de Espalhamento de Ponto (PSF - *Point Spread Function*):

$$
\text{MTF}(u, v) = \left| \mathcal{F} \left\{ \text{PSF}(x, y) \right\} \right| = \left| \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \text{PSF}(x, y) e^{-j 2\pi (ux + vy)} \, dx \, dy \right|
$$

Na prática clínica, frequentemente utiliza-se a Função de Espalhamento de Linha (LSF - *Line Spread Function*) ou o método da borda afiada (*edge method*) para derivar a MTF.

### 2.3. Espectro de Potência do Ruído (NPS)
O ruído em TC não é puramente branco; ele é texturizado e colorido pelos filtros de retroprojeção (FBP) e algoritmos de reconstrução iterativa (IR). O **Espectro de Potência do Ruído** (NPS - *Noise Power Spectrum* ou *Wiener Spectrum*) quantifica a distribuição espacial da variância do ruído no domínio de Fourier:

$$
\text{NPS}(u, v) = \lim_{L_x, L_y \to \infty} \frac{1}{L_x L_y} \left| \iint_{L_x, L_y} \left[ \hat{\mu}(x, y) - \bar{\mu} \right] e^{-j 2\pi (ux + vy)} \, dx \, dy \right|^2
$$

### 2.4. Detectabilidade de Modelos de Observadores (Detectability Index, $d'$)
A métrica mais abrangente na avaliação baseada em tarefas é o **Índice de Detectability** ($d'$), derivado da teoria estatística de decisão (Teoria de Detecção de Sinais). Para um Observador Ideal de Hotelling ou Linear (CHO - *Channelized Hotelling Observer*), $d'$ é definido como:

$$
d'^2 = \frac{\left[ \iint \Delta s(u, v) W(u, v) \, du \, dv \right]^2}{\iint \text{NPS}(u, v) |W(u, v)|^2 \, du \, dv}
$$

Onde $\Delta s(u, v)$ é a transformada de Fourier do sinal de interesse (ex: uma lesão esférica contrastada) e $W(u, v)$ representa a função de ponderação ou os canais visuais que mimetizam o sistema visual humano.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

As IQMs desempenham um papel central no ciclo de vida tecnológico da Tomografia Computadorizada, atuando em quatro pilares fundamentais:

### 3.1. Controle de Quality Assurance (QA) e Conformidade Regulatória
Físicos médicos utilizam métricas fundamentais (como ruído, uniformidade, linearidade do número CT e MTF via fantasmas como o *Catphan*) para garantir que o tomógrafo opere dentro dos limites aceitáveis estabelecidos por agências reguladoras (ex: ANVISA, FDA, ACR). Desvios nessas métricas indicam degradação do tubo de raios X, falhas em anéis de detetores ou problemas de calibração.

### 3.2. Otimização de Protocolos de Aquisição
O balanço entre dose de radiação e qualidade de imagem é mediado por IQMs. Ao introduzir novos protocolos de varredura (ex: redução de quilovoltagem pico - $kVp$, modulação de corrente automática de tubo - *ATCM*), as métricas baseadas em tarefas asseguram que a detectabilidade diagnóstica de patologias sutis (como nódulos pulmonares precoces ou pequenos acidentes vasculares cerebrais) não seja comprometida pela diminuição do produto corrente-tempo ($mAs$).

### 3.3. Avaliação de Algoritmos de Reconstrução Avançados
Com a evolução da TC, métodos tradicionais de **Retroprojeção Filtrada (FBP)** foram complementados e substituídos pela **Reconstrução Iterativa (IR)** e, mais recentemente, por **Reconstrução Baseada em Inteligência Artificial / Deep Learning (DLR)**. 
* O desafio com DLR e IR agressiva é a alteração não linear da textura do ruído e a supressão de detalhes de baixo contraste (falsos artefatos de "borracha"). 
* Métricas tradicionais como o desvio padrão falham em caracterizar imagens geradas por DLR. Portanto, o uso combinado de **NPS** e **MTF task-specific** tornou-se obrigatório para certificar que a inteligência artificial não está "alucinando" estruturas anatômicas ou removendo patologias reais.

### 3.4. Otimização Automatizada por IA
Sistemas modernos de TC utilizam feedback em tempo real baseado em métricas de qualidade de imagem estimadas a partir de *scouts* (topogramas) para ajustar dinamicamente os parâmetros de exposição para cada paciente específico, maximizando o $d'$ para a tarefa clínica pretendida.

---

## 4. Conexões e Wikilinks

- [[Retroprojeção Filtrada (FBP)|Filtered Backprojection]]
- [[Reconstrução Iterativa|Iterative Reconstruction]]
- [[Deep Learning Image Reconstruction (DLR)|Deep Learning Reconstruction]]
- [[Modulation Transfer Function (MTF)|Modulation Transfer Function]]
- [[Noise Power Spectrum|Noise Power Spectrum]]
- [[Task Based Image Quality|Task-Based Image Quality]]
- [[Hounsfield Unit]]
- [[Radiation Dosimetry in CT]]
- [[Computed Tomography QA]]
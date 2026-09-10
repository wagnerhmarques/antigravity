---
tipo: conceito
aliases: [impressao-3d-duplo-filamento\, dual-filament-3d-printing]
tags: [fisica-medica, tomografia-computadorizada, manufatura-aditiva, phantoms-hibridos, pixelprint]
data: 2026-08-25
---

# impressao-3d-duplo-filamento

## 1. Definição Conceitual e Fundamentação Física
A **impressão 3D de duplo filamento** (ou *dual-filament 3d printing*) refere-se a uma técnica avançada de fabricação aditiva por deposição de material fundido (FDM/FFF) que utiliza simultaneamente dois polímeros com propriedades de atenuação radiológica e mecânicas distintas. No contexto da Física Médica e da Tomografia Computadorizada (TC), essa tecnologia supera as limitações tradicionais dos fantomas homogêneos ou impressos com monofilamentos convencionais. 

Permite a deposição espacialmente controlada de materiais com números atômicos efetivos ($Z_{\text{eff}}$) e densidades mássicas ($\rho$) customizadas, simulando com alta fidelidade o coeficiente de atenuação linear ($\mu$) de diferentes tecidos biológicos (como tecido adiposo, muscular, ósseo trabecular e cortical) em energias de raios X diagnósticos. A técnica atua como pilar físico para a criação de texturas anatômicas realistas (*clutter* anatômico), permitindo o estudo rigoroso de tarefas visuais complexas e a otimização de protocolos clínicos sem a exposição desnecessária de pacientes.

## 2. Formulação Matemática e Propriedades
A atenuação dos fótons de raios X através de um fantoma fabricado por duplo filamento é governada pela lei de atenuação de Beer-Lambert, onde o coeficiente de atenuação linear $\mu(E, \vec{r})$ em um ponto espacial $\vec{r}$ e energia $E$ é modulado pela fração volumétrica dos dois filamentos depositados:

$$
\mu(E, \vec{r}) = w_1(\vec{r})\mu_1(E) + w_2(\vec{r})\mu_2(E)
$$

Onde:
- $w_1(\vec{r})$ e $w_2(\vec{r})$ representam as funções de distribuição espacial das densidades relativas dos filamentos 1 e 2, sujeitas à restrição de preenchimento $w_1(\vec{r}) + w_2(\vec{r}) = 1$ em zonas de voxel misto.
- $\mu_1(E)$ e $\mu_2(E)$ são os coeficientes de atenuação mássica efetiva dos materiais puros (por exemplo, PETG, ABS, PLA dopado com bário ou carbonato de cálcio) em função do espectro policromático da fonte de raios X.

Para a avaliação de qualidade de imagem baseada em tarefas (*task-based image quality*), a textura gerada pela impressão de duplo filamento introduz um ruído estrutural estocástico modelado pelo espectro de potência de ruído anatômico (NPS - *Noise Power Spectrum*):

$$
\text{NPS}_{\text{anat}}(\mathbf{f}) = \lim_{L \to \infty} \frac{1}{2\pi L^2} \left\langle \left| \mathcal{T} \left\{ \Delta \mu(\vec{r}) \right\} \right|^2 \right\rangle
$$

Onde $\mathbf{f}$ representa o vetor de frequência espacial bidimensional/tridimensional, e $\mathcal{T}$ é o operador de transformação de Fourier aplicado às flutuações espaciais de atenuação $\Delta \mu(\vec{r})$.

## 3. Contexto no Acervo do Pesquisador & Aplicações
No acervo de pesquisas do doutorado (USP/FAPESP), a técnica de **impressao-3d-duplo-filamento** está fortemente integrada ao arcabouço metodológico do [[Pixelprint]] e ao desenvolvimento de fantomas avançados (`[[queries/O que são phantoms ?.md]]`, `[[quais são os termos mais frequentes na minha estruturaco aqui no obsidian?.md]]`). 

Suas principais aplicações e conexões no laboratório incluem:
- **Fantomas Híbridos e Textura Anatômica:** Utilizada para fundir estruturas geométricas de controle com regiões antropomórficas impressas em 3D, permitindo reproduzir o *clutter* anatômico realista (fígado, pulmão e crânio) essencial para estudos psicofísicos 2AFC e a avaliação de observadores computacionais (`[[queries/Comente sobre a evolução dos modelos de observadores computacionais...md]]`).
- **Simulação de Atenuação Torácica:** Conforme documentado em `[[USP/TCC - Modelos perceptivos.md]]`, a tecnologia viabilizou a modelagem da atenuação radiológica do tórax humano, incluindo a árvore traqueobrônquica, superfícies pleurais, vértebras em PETG e parênquima pulmonar simulado.
- **Redução de Artefatos e TC Espectral:** Atua na validação de algoritmos de correção (`[[queries/O que é pixel print ?.md]]`, `[[pixelprint.md]]`), permitindo simular gradientes complexos de endurecimento de feixe e artefatos metálicos controlados (*Tunable Metal-Artifact Intensity*, conforme `[[dual-filament-3d-printing-ct-phantoms-pasyar-2026.md]]`).
- **Extração de NPS/TTF:** Permite a extração rigorosa da Função de Transferência de Tarefa (TTF) e do NPS em geometrias que mimetizam a heterogeneidade biológica (`[[queries/Qual é o estado da arte das tecnologias que envolvem meu trabalho de doutorado...md]]`).

## 4. Conexões e Wikilinks
- [[Pixelprint]]
- [[Phantoms Híbridos|phantoms-hibridos]]
- [[Redução de Artefatos Metálicos|reducao-de-artefatos-metalicos]]
- [[Tomografia Computadorizada Espectral|tomografia-computadorizada-espectral]]
- [[Métrica Gumbel p-index para Quantificação de Artefatos|metrica-gumbel-p-index]]
- [[Task Based Image Quality|task-based-image-quality]]
- [[USP/TCC - Modelos perceptivos]]
- [[Pasyar 2026 - Impressão 3D de Phantoms para TC|dual-filament-3d-printing-ct-phantoms-pasyar-2026]]
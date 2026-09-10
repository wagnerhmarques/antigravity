---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, qualidade-de-imagem, processamento-de-sinal, metrologia]
data: 2026-08-25
---

# funcao-de-dispersao-de-ponto

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Função de Dispersão de Ponto** (conhecida globalmente como *Point Spread Function* - **PSF**) é a resposta de um sistema de imagem linear e invariante no espaço (LSI - *Linear Space-Invariant*) a uma entrada idealmente pontual, descrita matematicamente pela função delta de Dirac. Em Tomografia Computadorizada (TC) e na Física Médica em geral, a PSF quantifica o grau de desfocagem (*blurring*), degradação e espalhamento espacial introduzido pelo sistema de aquisição e reconstrução de imagem.

Fisicamente, a formação de imagem na TC não é perfeita. Uma fonte de fótons de raios X com dimensões finitas no ponto focal, o tamanho e a geometria dos elementos do arrasto de detetores, o movimento do gantry, os algoritmos de interpolação e os filtros de rampa aplicados na retroprojeção filtrada (FBP) contribuem para que um objeto infinitesimal (um ponto hiperdenso sub-resolução, como uma microesfera metálica) seja representado na imagem final como uma mancha difusa tridimensional. 

Metrologicamente, a PSF atua como a assinatura espacial do sistema de imagem. Se a PSF for rigorosamente conhecida em todas as coordenadas do volume escaneado, o sistema de formação de imagem pode ser modelado como um operador linear integral. A largura a meia altura (*Full Width at Half Maximum* - FWHM) e a largura a décimo máximo (*Full Width at Tenth Maximum* - FWTM) da PSF são métricas padronizadas para avaliar a resolução espacial intrínseca e o desempenho de modulação de contraste de scanners de TC.

## 2. Formulação Matemática e Propriedades (se aplicável)

Considerando um sistema de imagem contínuo em duas dimensões (ou estendido para três dimensões), let $f(x, y)$ ser a distribuição de atenuação real de um objeto e $g(x, y)$ a imagem reconstruída. A operação do sistema é descrita pela integral de convolução:

$$
g(x, y) = \iint_{-\infty}^{\infty} f(\xi, \eta) \cdot \text{PSF}(x - \xi, y - \eta) \, d\xi \, d\eta + n(x, y)
$$

Onde:
- $\text{PSF}(x, y, \xi, \eta)$ é a função de dispersão de ponto variante no espaço. Assumindo a aproximação de invariância espacial local, ela é simplificada para $\text{PSF}(x - \xi, y - \eta)$.
- $n(x, y)$ representa o ruído estocástico inerente (principalmente ruído quântico de Poisson).

No contexto de sistemas lineares, a transformada de Fourier bidimensional da PSF define a **Função de Transferência de Modulação** (MTF - *Modulation Transfer Function*), que é a métrica fundamental no domínio da frequência espacial $u, v$:

$$
\text{MTF}(u, v) = \left| \mathcal{F} \left\{ \text{PSF}(x, y) \right\} \right| = \left| \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \text{PSF}(x, y) e^{-j 2 \pi (ux + vy)} \, dx \, dy \right|
$$

Propriedades fundamentais da PSF na TC:
1. **Normalização**: O volume sob a PSF é tipicamente normalizado para preservar a integridade radiométrica (o valor médio de uma área uniforme não deve ser alterado pela desfocagem):
   
$$
\iint_{-\infty}^{\infty} \text{PSF}(x, y) \, dx \, dy = 1
$$

2. **Anisotropia**: Em TC helicoidal, a PSF frequentemente apresenta comportamento anisotrópico, sendo mais degradada no eixo longitudinal ($z$) em comparação aos eixos axiais ($x, y$), devido à interpolação helicoidal e à inclinação do feixe.
3. **Fator de Desconversão**: A largura da PSF correlaciona-se diretamente com a frequência de corte do filtro de reconstrução (kernel). Filtros agudos (*sharp kernels*) resultam em uma PSF mais estreita (maior resolução, maior ruído), enquanto filtros suaves (*smooth kernels*) geram uma PSF larga (menor resolução, menor ruído).

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A modelagem e a medição precisa da PSF são pilares essenciais na garantia da qualidade e no avanço tecnológico da TC:

* **Controle de Qualidade e Metrologia**: Phantoms contendo fios finos de tungstênio ou esferas de alto contraste são escaneados rotineiramente para extrair a PSF e, por conseguinte, a MTF. Isso assegura que o tomógrafo atenda aos padrões regulatórios de resolução espacial.
* **Reconstrução Iterativa Avançada (IR)**: Algoritmos estatísticos e baseados em modelos (MBIR - *Model-Based Iterative Reconstruction*) incorporam explicitamente a PSF do sistema no processo de retroprojeção e projeção direta (*forward projection*). Ao modelar a ótica do sistema e o tamanho focal do tubo dentro da matriz do sistema, o algoritmo consegue desfazer parcialmente o efeito de borramento da PSF, melhorando a nitidez sem amplificar excessivamente o ruído.
* **Inteligência Artificial e Aprendizado Profundo (DLR)**: Redes neurais convolucionais (CNNs) e modelos generativos aplicados à melhoria de imagem (*super-resolution* e redução de ruído em TC) utilizam a PSF como *ground truth* física para treinar redes a recuperar detalhes estruturais perdidos devido às limitações físicas do scanner.
* **Dosimetria e Avaliação de Observadores Computacionais**: Na avaliação de detectores de lesões por observadores ideais (como o *Channelized Hotelling Observer* - CHO), a PSF define o limite superior da detectabilidade de estruturas pequenas de baixo contraste (ex.: nódulos pulmonares incipientes ou lesões hepáticas).

## 4. Conexões e Wikilinks

- [[funcao-de-transf-modulacao|Função de Transferência de Modulação (MTF)]]
- [[funcao-de-transf-de-fase|Função de Transferência de Fase (PTF)]]
- [[Reconstrução Iterativa|Reconstrução Iterativa (IR)]]
- [[Filtro de Rampa|Filtro de Rampa e Kernels de Reconstrução]]
- [[ruido-em-tc|Ruído e Estatística em Tomografia Computadorizada]]
- [[Resolução Espacial|Resolução Espacial em TC]]
- [[tomografia-computadorizada-de-espiral|Tomografia Computadorizada Helicoidal / Espiral]]
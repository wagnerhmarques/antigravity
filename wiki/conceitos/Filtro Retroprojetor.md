---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-de-imagem, processamento-de-sinal, fbp]
data: 2026-08-25
---

# Filtro-Retroprojetor

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **Filtro-Retroprojetor** (frequentemente associado ao algoritmo de Retroprojeção Filtrada ou *Filtered Backprojection* - FBP) é o método analítico clássico e fundamental de reconstrução tomográfica utilizado em Tomografia Computadorizada (TC) médica. Historicamente, a retroprojeção simples (ou direta) de perfis de atenuação adquiridos em múltiplos ângulos resulta em imagens severamente borradas, com uma degradação espacial caracterizada por uma resposta a impulso cuja amplitude decai com o inverso da frequência espacial ($1/\rho$ no espaço de Fourier bidimensional). 

Do ponto de vista da física matemática, a retroprojeção pura atua como um operador que suaviza excessivamente as altas frequências espaciais, borrando as bordas e as interfaces teciduais. Para mitigar esse artefato físico inerente à geometria de aquisição de feixe cônico ou paralelo, o **Filtro-Retroprojetor** aplica um filtro de rampa (ou filtros apodizados derivados deste) aos dados de projeção (sinograma) no domínio espacial ou de Fourier *antes* de realizar a operação geométrica de retroprojeção espacial. Essa filtragem prévia compensa analiticamente o desfoque $1/\rho$, restaurando a resolução espacial, a nitidez e a fidelidade quantitativa dos coeficientes de atenuação linear ($\mu$) reconstruídos.

Metrologicamente, o desempenho do sistema baseado em FBP é avaliado por meio de funções de transferência de modulação (MTF), ruído textural e análise de limiar de detectabilidade em simuladores padronizados (fantasmas de controle de qualidade). Embora técnicas iterativas (IR) e de aprendizado profundo (DLR) tenham dominado o cenário clínico moderno devido à redução de dose, o algoritmo de FBP permanece como referência padrão ("ground truth" analítica) e base computacional de alta velocidade.

---

## 2. Formulação Matemática e Propriedades

A reconstrução por Filtro-Retroprojetor fundamenta-se no Teorema da Projeção Central (ou Teorema do Slice-Projection). Seja $f(x, y)$ a distribuição espacial bidimensional do coeficiente de atenuação linear do objeto, e seja $P_\theta(t)$ a projeção paralela obtida ao longo de uma linha de integração com ângulo $\theta$, onde $t$ representa a coordenada espacial ao longo do detector:

$$
P_\theta(t) = \iint_{-\infty}^{\infty} f(x, y) \delta(x \cos\theta + y \sin\theta - t) \, dx \, dy
$$

A transformada de Fourier unidimensional da projeção $P_\theta(t)$ em relação à coordenada $t$, denotada por $\mathcal{F}\{P_\theta(t)\} = S_\theta(\omega)$, corresponde exatamente a uma fatia radial bidimensional da transformada de Fourier bidimensional de $f(x, y)$, expressa em coordenadas polares $(\omega, \theta)$:

$$
S_\theta(\omega) = \int_{-\infty}^{\infty} P_\theta(t) e^{-j 2 \pi \omega t} \, dt = F(\omega \cos\theta, \omega \sin\theta)
$$

Para recuperar a imagem original $f(x, y)$ a partir de suas projeções, aplica-se a transformada de Fourier inversa bidimensional em coordenadas polares. Ao converter o jacobiano da transformação de coordenadas cartesianas para polares, surge o termo $|\omega|$ (fator de rampa):

$$
f(x, y) = \int_{0}^{\pi} \left[ \int_{-\infty}^{\infty} S_\theta(\omega) |\omega| e^{j 2 \pi \omega t} \, d\omega \right]_{\theta = x \cos\theta + y \sin\theta} \, d\theta
$$

A expressão entre colchetes representa a operação de **filtragem** da projeção. O filtro ideal de rampa no domínio da frequência é dado por $H(\omega) = |\omega|$. No entanto, como $|\omegaادی|$ acentua infinitamente as altas frequências, amplificando o ruído quântico de alta frequência inerente aos fótons de raios X detectados, aplica-se uma função de janela (apodização) $W(\omega)$, resultando no filtro modificado:

$$
Q_\theta(t) = \int_{-\infty}^{\infty} S_\theta(\omega) |\omega| W(\omega) e^{j 2 \pi \omega t} \, d\omega
$$

Finalmente, a etapa de **retroprojeção** acumula as projeções filtradas $Q_\theta(t)$ ao longo de todas as trajetórias angulares $\theta$ que cruzam o ponto $(x, y)$:

$$
f_{\text{FBP}}(x, y) = \int_{0}^{\pi} Q_\theta(x \cos\theta + y \sin\theta) \, \, d\theta
$$

Discretizadamente, para um sistema com $N_\theta$ projeções angulares e $N_s$ amostras de detector, a operação computacional opera em tempo $O(N_\theta N_s \log N_s + N_\theta N_s^2)$, caracterizando-se por uma eficiência determinística linear notável em termos de complexidade algorítmica.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

O Filtro-Retroprojetor e suas variantes otimizadas desempenham papéis críticos no fluxo de trabalho da Tomografia Computadorizada clínica e industrial:

* **Reconstrução em Tempo Real:** Devido à sua natureza puramente analítica e não iterativa, o FBP é altamente paralelizável em arquiteturas de hardware dedicadas (GPUs e ASICs), permitindo a reconstrução volumétrica quase instantânea após a aquisição helicoidal ou axial.
* **Controle de Qualidade (QC) e Metrologia:** Os físicos médicos utilizam a FBP rotineiramente para testes de aceitação e controle de qualidade de rotina. Como o FBP possui uma resposta linear ao ruído e à resolução, ele evita os artefatos não-lineares introduzidos por certas rotinas de reconstrução iterativa, facilitando a avaliação objetiva da MTF, da Noise Power Spectrum (NPS) e da resolução de baixo contraste.
* **Otimização de Dose e Filtros de Apodização:** A escolha do filtro de rampa combinado com janelas de suavização (como Hann, Hamming, Butterworth ou Shepp-Logan) permite ao físico sintonizar o balanço entre resolução espacial e supressão de ruído (dose). Filtros agudos aumentam a nitidez (ideais para estruturas ósseas e pulmões), enquanto filtros suaves reduzem o ruído quântico em exames de tecidos moles (como abdômen e cérebro), impactando diretamente na otimização da dose de radiação ionizante sob o princípio ALARA.
* **Base para Algoritmos Híbridos e Iterativos:** Em abordagens modernas, imagens reconstruídas via FBP servem frequentemente como estimativa inicial (*initial guess*) para algoritmos de Reconstrução Iterativa (IR) baseados em modelos estatísticos ou métodos de Aprendizado Profundo (DLR), acelerando a convergência e servindo como padrão comparativo de validação de artefatos.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[Reconstrução de Imagem]]
* [[Retroprojeção Simples]]
* [[Teorema da Projeção Central]]
* [[Filtro de Rampa]]
* [[Reconstrução Iterativa|Reconstrução Iterativa]]
* [[Inteligencia Artificial em Tomografia Computadorizada]]
* [[Fisica Medica]]
* [[Controle de Qualidade em TC|Controle de Qualidade em Radiologia]]
* [[Ruído Quântico e Dose em Radiologia]]
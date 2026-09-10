---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-de-imagem, processamento-de-sinal, fourier]
data: 2026-08-25
---

# filtered-back-projection

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Filtered Back-Projection** (FBP) — Retroprojeção Filtrada — é o algoritmo analítico padrão ouro clássico utilizado na reconstrução de imagens em Tomografia Computadorizada (TC) médica. Historicamente, os sistemas de TC baseavam-se puramente na retroprojeção simples (*simple back-projection*), técnica que acumula os valores de atenuação ao longo das linhas de projeção (raios) correspondentes aos ângulos de aquisição. Contudo, a retroprojeção simples padece de um grave artefato matemático e físico: a distribuição da densidade reconstruída sofre um desfoque inerente caracterizado por uma resposta ao impulso no espaço real proporcional a $1/r$, onde $r$ é a distância radial ao centro. Isso resulta em uma perda severa de nitidez e em um borramento generalizado (efeito de estrela e perda de altas frequências espaciais).

Para resolver esse problema, a FBP introduz uma etapa de filtragem no domínio das frequências espaciais antes da retroprojeção geométrica. Com base no Teorema do Slice Central (ou Teorema da Projeção-Fatia), a transformada de Fourier unidimensional de uma projeção paralela em um dado ângulo corresponde a uma fatia central bidimensional da transformada de Fourier bidimensional do objeto original. Consequentemente, para compensar a atenuação das altas frequências inerente à amostragem radial densa no centro do espaço de Fourier (densidade de pontos inversamente proporcional ao raio), aplica-se um filtro passa-alta rampa (*ramp filter*) às projeções unidimensionais. Do ponto de vista metrológico, a FBP traduz de forma exata e determinística os dados de projeção coletados pelos detectores em um mapa espacial quantitativo de coeficientes de atenuação linear ($\mu$), mantendo a fidelidade geométrica e permitindo a mensuração precisa de unidades Hounsfield (HU), desde que os devidos ajustes de calibração sejam aplicados.

---

## 2. Formulação Matemática e Propriedades (se aplicável)

Matematicamente, o processo de reconstrução por FBP para um feixe paralelo pode ser formalizado em duas etapas principais: filtragem e retroprojeção.

Seja $P_\theta(t)$ a projeção paralela obtida a um ângulo $\theta$, onde $t$ é a coordenada espacial ao longo do detector:

$$
P_\theta(t) = \iint_{-\infty}^{\infty} f(x,y) \delta(x \cos\theta + y \sin\theta - t) \, dx\, dy
$$

onde $f(x,y)$ representa a distribuição espacial do coeficiente de atenuação linear do objeto.

### A. Etapa de Filtragem
A projeção filtrada $\tilde{P}_\theta(t)$ é obtida pela convolução da projeção original $P_\theta(t)$ com um núcleo de filtro $q(t)$, ou equivalentemente, pela multiplicação no domínio da frequência:

$$
\tilde{P}_\theta(t) = P_\theta(t) * q(t) = \mathcal{F}^{-1} \left\{ \mathcal{F}\{P_\theta(t)\} \cdot |
u| \right\}
$$

onde $
u$denota a frequência espacial associada à coordenada$t$, e$|
u|$ é o filtro rampa ideal (*ramp filter*). Na prática clínica, devido à ampliação do ruído de alta frequência inerente aos detectores, o filtro rampa puro é multiplicado por uma função de janela (como os filtros *Ram-Lak*, *Hann*, *Hamming* ou *Butterworth*) para controlar o balanço entre resolução espacial e supressão de ruído:

$$
Q(
u) = |
u| \cdot W(
u)
$$

onde $W(
u)$ é a janela de apodização.

### B. Etapa de Retroprojeção
A imagem reconstruída $f(x,y)$ é obtida pela integração (retroprojeção) das projeções filtradas sobre todos os ângulos de projeção $\theta$ variando de $0$ a $\pi$ (ou $2\pi$ dependendo da formulação do feixe):

$$
f(x,y) = \int_{0}^{\pi} \tilde{P}_\theta(x \cos\theta + y \sin\theta) \,\, d\theta
$$

Em sistemas modernos de geometria cônica (*cone-beam CT*), formulações analíticas estendidas como o algoritmo de **Feldkamp-Davis-Kress (FDK)** adaptam a FBP clássica para corrigir o desvio angular fora do plano central, aplicando ponderações de distância e reordenamento dos dados de projeção antes da retroprojeção 3D.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A importância da FBP reside na sua extrema eficiência computacional, previsibilidade linear e estabilidade determinística. Por ser uma solução analítica direta, a FBP não requer processos iterativos complexos, permitindo que a reconstrução de matrizes volumétricas densas ocorra em tempo quase real, o que é mandatório em ambientes de emergência e exames de trauma.

No entanto, no contexto da otimização de dose em radiologia diagnóstica, a FBP apresenta limitações severas. Como a operação de filtragem envolve um ganho expressivo nas altas frequências espaciais, o ruído quântico presente nos dados brutos (sinograma) é amplificado de maneira desproporcional. Consequentemente, reduzir a corrente do tubo (mAs) ou a dose de radiação para o paciente resulta em imagens reconstruídas por FBP excessivamente ruidosas, degradando a detectabilidade de lesões de baixo contraste. 

Essa limitação impulsionou o desenvolvimento de métodos avançados:
1. **Reconstrução Iterativa (IR - *Iterative Reconstruction*):** Incorporam modelos estatísticos de ruído e modelos físicos do sistema no processo de otimização, permitindo suprimir artefatos e ruído sem sacrificar a resolução espacial.
2. **Reconstrução Baseada em Aprendizado Profundo (DLR - *Deep Learning Reconstruction*):** Redes neurais treinadas para mapear sinogramas de baixa dose ou imagens FBP ruidosas diretamente em imagens de alta qualidade diagnóstica.

Apesar da ascensão da IR e da DLR, a FBP continua a ser a métrica de referência em protocolos de controle de qualidade metrológico, testes de aceitação de equipamentos de TC, e serve como linha de base analítica para avaliar a fidelidade espacial e a ausência de vieses em novos algoritmos de inteligência artificial.

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|computed-tomography]]
- [[Image Reconstruction|image-reconstruction]]
- [[Reconstrução Iterativa|iterative-reconstruction]]
- [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction]]
- [[spatial-resolution-mtf]]
- [[Radiation Dosimetry|radiation-dosimetry]]
- [[Simulação de Monte Carlo|monte-carlo-simulation]]
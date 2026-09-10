---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, aquisicao, formacao-de-imagem, dosimetria, metrologia]
data: 2026-08-25
---

# aquisição

## 1. Definição Conceitual e Fundamentação Física / Metrológica

No contexto da Tomografia Computadorizada (TC) e da Física Médica, o termo **aquisição** refere-se ao processo físico, eletrônico e computacional pelo qual a radiação X atenuada ao atravessar um volume anatômico é convertida em sinais elétricos mensuráveis, digitalizada e armazenada na forma de dados brutos (frequentemente denominados *raw data* ou projeções). 

Do ponto de vista metrológico, a aquisição representa a etapa inicial da cadeia de formação de imagem, onde a distribuição espacial do coeficiente de atenuação linear $\mu(x, y, z)$ do objeto é amostrada de forma discreta no espaço, no tempo e em energia. O processo fundamenta-se na Lei de Atenuação de Lambert-Beer para feixes policromáticos:

$$
I = I_0 \exp \left( -\int_L \mu(l) \, dl \right)
$$

Onde $I_0$ é a intensidade do feixe incidente de fótons de raios X, $I$ é a intensidade emergente após a travessia do caminho linear $L$, e $\mu(l)$ é o coeficiente de atenuação linear ao longo da trajetória.

A aquisição moderna em TC é helicoidal (espiral) ou volumétrica (cone-beam), caracterizada pela rotação síncrona e contínua do tubo de raios X e da matriz de detetores (geralmente compostos de cintiladores acoplados a fotodiodos ou detetores de conversão direta baseados em telureto de cádmio e zinco - CZT) ao redor do paciente, enquanto a mesa de exame translada longitudinalmente. A qualidade desta etapa é governada por parâmetros estritos de amostragem espacial (passo de hélice ou *pitch*, largura do colimador), amostragem temporal (tempo de rotação do pórtico) e amostragem estatística (produto corrente-tempo, mAs).

---

## 2. Formulação Matemática e Propriedades

O processo de aquisição discretiza o objeto contínuo em um conjunto de projeções angulares $\mathcal{P}_\beta(s)$, onde $\beta$ representa o ângulo de projeção do tubo de raios X e $s$ a coordenada do detetor no plano de leque (*fan-beam*) ou cone (*cone-beam*). A relação entre o dado adquirido e o perfil de atenuação é expressa pelo logaritmo negativo do sinal normalizado:

$$
P_\beta(s) = -\ln \left( \frac{I(\beta, s)}{I_0} \right) = \int_L \mu(x, y) \, dl
$$

Para uma geometria de feixe paralelo ideal, a transformada de Radon bidimensional modela perfeitamente a aquisição:

$$
\mathcal{R}\{\mu(x,y)\} = P_\theta(s) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \mu(x,y) \delta(x \cos\theta + y \sin\theta - s) \, dx \, dy
$$

### Propriedades Estatísticas e Ruído na Aquisição
A precisão metrológica da aquisição é limitada pela flutuação estatística quântica dos fótons de raios X, descrita pela estatística de Poisson. O número médio de fótons detectados $\bar{N}$ em um elemento de detetor segue uma distribuição de Poisson com variância igual à própria média:

$$
\sigma^2(N) = \bar{N}
$$

Aplicando a propagação de incertezas na transformação logarítmica para obter o dado de projeção $P$, a variância do ruído no dado de aquisição bruto é inversamente proporcional ao número de fótons detectados:

$$
\sigma^2(P) \approx \frac{1}{\bar{N}} = \frac{1}{\bar{N}_0 \exp(-P)}
$$

Esta relação matemática demonstra que regiões de alta atenuação (estruturas densas, pacientes obesos) sofrem com baixa contagem de fótons ($\bar{N} \to 0$), resultando em degradação severa da relação sinal-ruído (SNR) e artefatos de quantum mottle na fase de aquisição se a exposição ($mAs$) não for compensada adaptativamente.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A otimização da aquisição é o pilar central para a prática do princípio ALARA (*As Low As Reasonably Achievable*) na radiologia diagnóstica. O projeto e a execução dos protocolos de aquisição impactam diretamente a dose absorvida pelo paciente e a detectabilidade de lesões.

*   **Controle de Qualidade (CQ) e Metrologia:** Os testes de aceitação e rotina avaliam a linearidade da aquisição, a eficiência de conversão do detetor, o ruído eletrônico inerente, a resposta espacial (função de transferência de modulação - MTF da aquisição) e artefatos de anel decorrentes de descalibrações individuais dos elementos do detetor.
*   **Modulação Automática de Corrente (mA):** Sistemas modernos ajustam dinamicamente a intensidade do feixe de raios X durante a aquisição angular e longitudinal com base no topograma (*scout view*), otimizando a dose com base na atenuação anatômica tridimensional.
*   **Impacto na Reconstrução e Inteligência Artificial:** Algoritmos avançados de reconstrução, como a Retroprojeção Filtrada (FBP), Iterativa (IR) e Reconstrução Baseada em Aprendizado Profundo (DLR), dependem estritamente da fidelidadade dos dados obtidos na aquisição. Reduções drásticas de dose na aquisição geram ruídos não-gaussianos complexos que desafiam modelos lineares tradicionais, exigindo redes neurais treinadas para mitigar artefatos diretamente a partir de dados de aquisição subamostrados.

---

## 4. Conexões e Wikilinks

*   [[Tomografia Computadorizada|tomografia-computadorizada]]
*   [[Reconstrução de Imagem|reconstrucao-de-imagem]]
*   [[filtragem]]
*   [[Retroprojeção Filtrada (FBP)|fbp]]
*   [[iterativa]]
*   [[Deep Learning Reconstruction (DLR)|dlr]]
*   [[ruido]]
*   [[Dose]]
*   [[otimizacao]]
*   [[artefatos]]
*   [[Qualidade de Imagem em TC|qualidade-de-imagem]]
*   [[Observadores de Modelo (Model Observers)|observadores-computacionais]]
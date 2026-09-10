---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, formacao-de-imagem, radiodiagnostico, reconstrucao-de-imagem]
data: 2026-08-25
---

# tomografia-computadorizada

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A Tomografia Computadorizada (TC) é uma modalidade de imagem médica diagnóstica baseada na obtenção de múltiplos projeções radiográficas adquiridas sob diferentes ângulos de incidência ao redor de um eixo de rotação. Fundamentada na interação da radiação X ionizante com a matéria, a TC supera as limitações da radiografia planar bidimensional (projeção sumária) ao resolver espacialmente a distribuição tridimensional dos coeficientes de atenuação linear linear $\mu(x, y, z)$ dos tecidos biológicos.

Fisicamente, a atenuação do feixe de raios X policromático ao atravessar o meio é governada pela Lei de Beer-Lambert modificada para trajetos lineares:

$$
I = I_0 \exp \left( - \int_L \mu(x, y) \, dl \right)
$$

onde $I_0$ é a intensidade do feixe incidente, $I$ é a intensidade emergente após percorrer o caminho linear $L$, e $\mu(x, y)$ representa o coeficiente de atenuação linear espacialmente variante no plano de corte transversal. 

Do ponto de vista metrológico, os valores brutos de atenuação são convertidos em unidades normalizadas e independentes do equipamento\, denominadas Unidades Hounsfield ($\text{UH}$) ou *Hounsfield Units*:

$$
\text{UH} = 1000 \times \frac{\mu - \mu_{\text{água}}}{\mu_{\text{água}} - \mu_{\text{ar}}}
$$

Esta escala estabelece o ar como $-1000\text{ UH}$, a água destilada sob condições padrão como $0\text{ UH}$, e tecidos densos ou ossos corticais variando tipicamente entre $+700\text{ UH}$ e $+3000\text{ UH}$. A calibração metrológica rigorosa do sistema de TC assegura a reprodutibilidade quantitativa essencial para análises densitométricas, perfusão tecidual e radiômica.

---

## 2. Formulação Matemática e Propriedades

O processo de formação de imagem em TC fundamenta-se na matemática da transformada de Radon e em seu teorema de inversão. Uma projeção paralela unidimensional, coletada em um determinado ângulo $\theta$, é matematicamente descrita como um sinograma, onde cada linha representa a integral de linha (transformada de Radon) do coeficiente de atenuação:

$$
P_{\theta}(t) = \mathcal{R}\{\mu(x, y)\} = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \mu(x, y) \delta(x \cos\theta + y \sin\theta - t) \, dx \, dy
$$

onde $t$ representa a coordenada de transposição do detector perpendicular ao feixe central, e $\delta$ é a função delta de Dirac.

### O Teorema da Seção Central (Fourier Slice Theorem)
O princípio matemático que viabiliza a reconstrução analítica estabelece que a Transformada de Fourier unidimensional de uma projeção paralela $P_{\theta}(t)$ obtida no ângulo $\theta$ corresponde exatamente a uma linha radial através da origem, orientada no mesmo ângulo $\theta$\, da Transformada de Fourier bidimensional da função original $\mu(x, y)$:

$$
S_{\theta}(\omega) = \mathcal{F}_{1D}\{P_{\theta}(t)\} = \iint_{-\infty}^{\infty} \mu(x, y) e^{-j 2\pi \omega (x \cos\theta + y \sin\theta)} \, dx \, dy = M(\omega \cos\theta, \omega \sin\theta)
$$

### Retroprojeção Filtrada (Filtered Backprojection - FBP)
Para evitar a perda de resolução espacial e o desfoque característico da retroprojeção simples ($\mu_{\text{BS}}(x,y) = \int_{0}^{\pi} P_{\theta}(x \cos\theta + y \sin\theta) \, \, d\theta$), aplica-se um filtro de rampa (frequência espacial $|\omega|$) no domínio de Fourier antes da retroprojeção. A equação formal da FBP é dada por:

$$
\mu(x, y) = \int_{0}^{\pi} \left[ \int_{-\infty}^{\infty} S_{\theta}(\omega) |\omega| e^{j 2\pi \omega t} \, d\omega \right]_{t = x \cos\theta + y \sin\theta} \, d\theta
$$

No domínio espacial, a operação equivale à convolução das projeções com um núcleo de alta frequência (kernel):

$$
\mu(x, y) = \int_{0}^{\pi} \left( P_{\theta} * k \right)(x \cos\theta + y \sin\theta) \, \, d\theta
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A evolução tecnológica da TC tem sido guiada pela necessidade de otimização do balanço entre qualidade de imagem (resolução espacial, contraste e baixo ruído) e dose de radiação absorvida pelo paciente, em consonância com o princípio ALARA (*As Low As Reasonably Achievable*).

### Evolução dos Algoritmos de Reconstrução
1. **Retroprojeção Filtrada (FBP):** Historicamente padrão devido à sua alta velocidade computacional. No entanto, em regimes de baixa dose, a amplificação de ruído de alta frequência degrada severamente a detectabilidade de lesões de baixo contraste.
2. **Reconstrução Iterativa (IR):** Algoritmos estatísticos (como *Maximum Likelihood Expectation Maximization* - MLEM, e métodos penalizados) modelam a física estatística dos fótons (distribuição de Poisson) e a geometria do sistema óptico. Permitem reduções expressivas de dose (frequentemente entre $30\%$ e $60\%$) com preservação da nitidez.
3. **Reconstrução Baseada em Aprendizado Profundo (Deep Learning Reconstruction - DLR):** Redes neurais convolucionais (CNNs) e arquiteturas generativas treinadas em pares de imagens de alta dose (baixo ruído) e baixa dose (alto ruído) realizam a denoising e a recuperação de detalhes anatômicos com eficiência sem precedentes, operando em tempo real.

### Dosimetria e Controle de Qualidade
A avaliação dos riscos estocásticos e determinísticos da radiação ionizante exige o monitoramento rigoroso de métricas dosimétricas padronizadas:
- **$CTDI_{w}$ (Computed Tomography Dose Index Weighted):** Média ponderada da dose absorvida em câmara de ionização em PMMA (polimetilmetacrilato) nos eixos central e periférico de fantomas cilíndricos de $16\text{ cm}$ (cabeça) e $32\text{ cm}$ (corpo).
- **$DLSP$ (Dose-Length Product):** Produto do $CTDI_{vol}$ pelo comprimento total escaneado ($z$), correlacionando-se diretamente com o risco energético integral depositado no paciente.

O controle de qualidade periódico abrange a avaliação da linearidade do número de Hounsfield, uniformidade espacial do ruído, modulação da função de transferência óptica (MTF), e resolução de baixo contraste utilizando fantomas especializados (ex: ACR, Catphan).

---

## 4. Conexões e Wikilinks

- [[Reconstrução Iterativa|reconstrucao-iterativa]]
- [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction]]
- [[Unidades Hounsfield|unidades-hounsfield]]
- [[Transformada de Radon|transformada-de-radon]]
- [[dose-em-tomografia-computadorizada]]
- [[Artefatos em TC|artefatos-em-tomografia]]
- [[filtro-de-rampa-fbp]]
---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-de-imagem, processamento-de-sinal]
data: 2026-08-25
---

# Filtro de Retroprojeção (FBP)

## 1. Definição Conceitual e Fundamentação Física / Metrológica
O **Filtro de Retroprojeção** (*Filtered Backprojection* - FBP) é o algoritmo analítico padrão ouro histórico e amplamente utilizado na reconstrução de imagens em Tomografia Computadorizada (TC). Fisicamente, a aquisição de dados em TC mede a atenuação de feixes de raios X colimados que atravessam o paciente em múltiplos ângulos de projeção $\theta$, resultando em um conjunto de dados conhecido como **Projeções Paralelas** ou **Sinograma** ($\mathcal{P}_{\theta}(t)$).

A retroprojeção simples (*Simple Backprojection*), que consiste em "espalhar" de volta os valores medidos ao longo do caminho original do feixe através da matriz de imagem, padece de um grave artefato físico-matemático: a convolução com o núcleo de amostragem no domínio espacial resulta em um desfoque característico cuja resposta ao impulso decai com a frequência espacial $\frac{1}{r}$. Metrologicamente, isso significa que a imagem retroprojetada de forma simples representa uma versão borrada da distribuição real do coeficiente de atenuação linear $\mu(x,y)$. 

Para corrigir essa degradação inerente, o algoritmo FBP aplica um filtro de rampa (*ramp filter*) no domínio das frequências (ou uma convolução equivalente no domínio espacial) antes da etapa de retroprojeção. Este filtro amplifica as altas frequências espaciais para compensar exatamente a atenuação $1/|\omega$ imposta pela geometria da transformada de Radon bidimensional, restaurando a resolução espacial e a acurácia quantitativa da imagem tomográfica.

## 2. Formulação Matemática e Propriedades (se aplicável)

A formulação do FBP baseia-se no **Teorema da Fatia Central** (*Central Slice Theorem*), que estabelece que a transformada de Fourier unidimensional de uma projeção paralela $\mathcal{P}_{\theta}(t)$ em um ângulo $\theta$ corresponde a uma linha radial através da origem da transformada de Fourier bidimensional da imagem $\mu(x,y)$.

Matematicamente, a reconstrução por FBP para projeções paralelas é expresso pela fórmula de inversão de Radon:

$$
\mu(x,y) = \int_{0}^{\pi} \left[ \int_{-\infty}^{\infty} \mathcal{P}_{\theta}(t) \, |\omega| \, e^{i 2\pi \omega t} \, d\omega \right]_{t = x\cos\theta + y\sin\theta} \, d\theta
$$

Onde:
* $\mu(x,y)$ é o mapa espacial dos coeficientes de atenuação linear (em unidades Hounsfield, após calibração).
* $\mathcal{P}_{\theta}(t)$ é a projeção adquirida na posição $t$ e ângulo $\theta$.
* $t = x\cos\theta + y\sin\theta$ define a linha de integração (coordenada de detecção).
* $|\omega|$ é o **filtro de rampa ideal** no domínio da frequência $\omega$.

### Modificações do Filtro de Rampa
Como o filtro de rampa ideal $|\omega$ amplifica excessivamente o ruído de alta frequência inerente aos fótons contados (estatística de Poisson), filtros apodizados (*windowed ramp filters*) são empregados na prática clínica para controlar o balanço entre resolução espacial e supressão de ruído:

$$
\mathcal{H}(\omega) = |\omega| \cdot W(\omega)
$$

Onde $W(\omega)$ representa uma função janela de corte (e.g., *Hamming*, *Hanning*, *Butterworth*, ou *Shepp-Logan*). A formulação discreta na prática implementa-se via convolução linear:

$$
\mu(x,y) \approx \frac{\pi}{N_{\text{projeções}}} \sum_{i=1}^{N_{\text{projeções}}} \tilde{\mathcal{P}}_{\theta_i} (x\cos\theta_i + y\sin\theta_i)
$$

Onde $\tilde{\mathcal{P}}$ é a projeção filtrada obtida pela convolução discreta da projeção original com um núcleo espacial $h(t)$.

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Na prática clínica moderna e no controle de qualidade metrológico, o FBP desempenha papéis fundamentais:

* **Velocidade Computacional:** Devido à sua natureza puramente analítica e direta (não iterativa), o FBP requer uma carga computacional extremamente baixa comparado aos métodos avançados, permitindo a reconstrução quase instantânea de volumes volumétricos extensos.
* **Linearidade e Estacionariedade do Ruído:** O FBP é um operador linear. Isso garante que a textura do ruído e a resolução espacial sejam globalmente previsíveis e espacialmente invariantes (ignorando artefatos de feixe cônico ou subamostragem angular), o que facilita a validação metrológica em testes de garantia de qualidade (QA) com fantasmas (*phantoms*).
* **Baseline para Dosimetria e IA:** O FBP serve como referência fundamental para o treinamento e validação de algoritmos de **Reconstrução Iterativa (IR)** e de **Aprendizado Profundo (*Deep Learning Reconstruction* - DLR)**. Redes neurais modernas frequentemente utilizam imagens FBP de baixa dose como entrada (*input*) para mapear e estimar imagens de alta qualidade equivalentes à varredura convencional (*noise/artifact reduction*).
* **Limitações:** Em regimes de baixa dose de radiação ionizante (baixo número de fótons), o FBP amplifica severamente o ruído estipulado, gerando artefatos de estrias (*streaking artifacts*). Isso impulsionou a transição parcial da indústria para abordagens de reconstrução iterativa e baseadas em inteligência artificial.

## 4. Conexões e Wikilinks
* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[Teorema da Fatia Central]]
* [[Reconstrução Iterativa|Reconstrução Iterativa (IR)]]
* [[Deep Learning em Tomografia Computadorizada]]
* [[Controle de Qualidade em TC]]
* [[Física das Radiações e Dosimetria]]
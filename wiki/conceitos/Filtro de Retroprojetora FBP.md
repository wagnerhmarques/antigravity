---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-de-imagem, processamento-de-sinal, fbp]
data: 2026-08-25
---

# Filtro_de_Retroprojetora_FBP

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **Filtro de Retroprojetora** (conhecido formalmente no contexto da Tomografia Computadorizada como *Filtered Backprojection* ou **FBP**) é o algoritmo analítico padrão ouro histórico e de referência para a reconstrução de imagens tomográficas bidimensionais e tridimensionais a partir de projeções (projeções paralelas ou em leque) adquiridas em múltiplos ângulos.

Do ponto de vista da física médica e metrologia de imagem, a retroprojeção simples (*Simple Backprojection* - SBP), que consiste em "espalhar" o valor de intensidade de cada raio X medido de volta ao longo da trajetória em que o feixe viajou, padece de um grave artefato inerente: ela reconstrói a imagem como uma convolução da verdadeira distribuição do coeficiente de atenuação linear $\mu(x,y)$ com a função $1/r$ (onde $r$ é a distância radial no plano da imagem). Isso resulta em uma perda severa de resolução espacial, gerando um efeito de borramento (*blurring*) generalizado e uma degradação expressiva da função de espalhamento de ponto (*Point Spread Function* - PSF).

Para corrigir matematicamente esse borramento físico, aplica-se um **filtro de rampa** (*ramp filter*) ou filtros apodizados equivalentes (como Shepp-Logan, Hamming, Hann) no domínio das frequências espaciais *antes* de realizar a operação de retroprojeção. Este filtro compensa o decaimento de alta frequência inerente à geometria da projeção central, amplificando as altas frequências espaciais e restaurando a nitidez estrutural e a exatidão quantitativa da imagem reconstruída.

## 2. Formulação Matemática e Propriedades (se aplicável)

A base matemática da Retroprojetora Filtrada fundamenta-se no **Teorema da Fatia Central** (*Central Slice Theorem* ou *Fourier Slice Theorem*), o qual estabelece que a transformada de Fourier unidimensional de uma projeção paralela obtida a um ângulo $\theta$ é igual a uma fatia bidimensional da transformada de Fourier bidimensional da imagem original $\mu(x,y)$ passando pela origem com o mesmo ângulo $\theta$.

Seja $p_\theta(t)$ o perfil de projeção obtido a um ângulo $\theta$, onde $t$ representa a coordenada espacial ao longo do detector:

$$
p_\theta(t) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \mu(x,y) \, \delta(x \cos\theta + y \sin\theta - t) \, dx \, dy
$$

A transformada de Fourier 1D do perfil de projeção é dada por:

$$
P_\theta(\omega) = \mathcal{F}\{p_\theta(t)\} = \int_{-\infty}^{\infty} p_\theta(t) e^{-j 2 \pi \omega t} \, dt
$$

Onde $\omega$ é a frequência espacial. Pelo Teorema da Fatia Central, a reconstrução exata exige a inversão da transformada de Fourier 2D em coordenadas polares, o que introduz um fator Jacobiano $|\omega|$ (o filtro de rampa). 

A equação analítica da Retroprojetora Filtrada (FBP) no espaço real é formulada como:

$$
\mu(x,y) = \int_{0}^{\pi} Q_\theta (x \cos\theta + y \sin\theta) \, \, d\theta
$$

Onde $Q_\theta(t)$ representa o perfil de projeção filtrado, obtido pela convolução (*convolution*) do perfil original $p_\theta(t)$ com um núcleo de filtro $k(t)$:

$$
Q_\theta(t) = p_\theta(t) * k(t) = \int_{-\infty}^{\infty} p_\theta(\tau) k(t - \tau) \, d\tau
$$

No domínio da frequência, a operação de filtragem corresponde a uma multiplicação simples:

$$
Q_\theta(\omega) = P_\theta(\omega) \cdot |\omega|
$$

### Modificações e Filtros Apodizados
Como o filtro de rampa ideal $|\omega|$ amplifica excessivamente o ruído quântico de alta frequência presente nas medições reais de raios X, filtros de janela (apodização) são multiplicados ao filtro de rampa para atenuar as frequências mais altas:

$$
K(\omega) = |\omega| \cdot W(\omega)
$$

Onde $W(\omega)$ pode ser:
- **Shepp-Logan**: $W(\omega) = \frac{\sin(\pi \omega / \omega_c)}{\pi \omega / \omega_c}$ para $|\omega| \le \omega_c$
- **Hamming**: $W(\omega) = 0.54 + 0.46 \cos\left(\frac{\pi \omega}{\omega_c}\right)$
- **Hann**: $W(\omega) = 0.5 \left(1 + \cos\left(\frac{\pi \omega}{\omega_c}\right)\right)$

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Apesar do avanço massivo de algoritmos de Reconstrução Iterativa (*Iterative Reconstruction* - IR) e Inteligência Artificial baseada em Reconstrução Profunda (*Deep Learning Reconstruction* - DLR), o **Filtro de Retroprojetora (FBP)** continua sendo fundamental na prática clínica e na física médica moderna por motivos cruciais:

1. **Velocidade Computacional Extrema**: A FBP possui complexidade computacional linear-logarítmica otimizada, permitindo a reconstrução volumétrica em tempo real (quase instantânea) após a aquisição dos dados brutos (*sinograma*), requisito indispensável em exames de emergência, angio-TC e protocolos cardíacos dinâmicos.
2. **Linearidade e Previsibilidade de Ruído**: Diferente dos métodos iterativos e de aprendizado profundo (que podem introduzir não-linearidades espaciais, distorções de textura de ruído ou perda de resolução de baixo contraste em doses ultrabaixas), a FBP mantém uma resposta linear. Isso torna a análise de ruído, a avaliação da função de transferência de modulação ([[MTF_Funcao_de_Transferencia_de_Modulacao]]) e a dosimetria extremamente previsíveis e padronizadas.
3. **Padrão de Referência Metrológico**: Em testes de controle de qualidade e acreditação de equipamentos de TC (segundo diretrizes da AAPM e IEC), os parâmetros de dose e qualidade de imagem são frequentemente calibrados com base na FBP para garantir reprodutibilidade inter-institucional.
4. **Limitações na Otimização de Dose**: O calcanhar de Aquiles da FBP é a sua vulnerabilidade ao ruído quântico quando submetida a varreduras de baixa dose de radiação. Como o filtro de rampa amplifica as altas frequências, reduções drásticas na corrente do tubo (mAs) resultam em imagens severamente degradadas por ruído estocástico, impulsionando a necessidade de métodos híbridos ou reconstrutores avançados baseados em inteligência artificial.

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|Tomografia_Computadorizada]]
- [[Reconstrução Iterativa|Reconstrucao_Iterativa]]
- [[Deep Learning Reconstruction (DLR)|Deep_Learning_Reconstruction_DLR]]
- [[MTF_Funcao_de_Transferencia_de_Modulacao]]
- [[Sinograma]]
- [[Qualidade de Imagem em TC|Qualidade_de_Imagem_em_TC]]
- [[ControledeQualidade_FisicaMedica]]
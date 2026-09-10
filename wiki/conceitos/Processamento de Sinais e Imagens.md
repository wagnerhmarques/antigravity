---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, processamento-de-sinais, transformada-de-fourier, reconstrução-de-imagem, inteligencia-artificial]
data: 2026-08-25
---

# Processamento de Sinais e Imagens

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **Processamento de Sinais e Imagens** no contexto da Física Médica e da Tomografia Computadorizada (TC) engloba o conjunto de operações matemáticas, físicas e computacionais aplicadas para transformar dados brutos de aquisição (sinais analógicos e digitais) em representações visuais e quantitativas de alta fidelidade anatômica e funcional. 

Fisicamente, o processo inicia-se com a interação da radiação X ionizante com os tecidos biológicos, onde a atenuação é governada pela **Lei de Beer-Lambert**. Os fótons remanescentes que atravessam o paciente são convertidos por detectores de estado sólido (geralmente baseados em granada de gadolínio e cérmio - GOS, ou tungstato de cádmio - $CdWO_4$) em sinais elétricos analógicos. Estes sinais sofrem amostragem temporal, quantização analógica-digital (ADC) e correções preliminares (correção de ganho, offset, calibração a ar e correção de feixe policromático ou *beam-hardening*).

Metrologicamente, o processamento de sinais e imagens visa garantir a rastreabilidade, a acurácia dos números de Hounsfield (HU), a repetibilidade radiômica e a minimização de artefatos, mantendo o balanço rigoroso entre a dose absorvida pelo paciente (otimizada pelo princípio ALARA) e a detectabilidade de baixo contraste, conforme avaliado por métricas de desempenho de sistemas de imagem como a Função de Transferência de Modulação (MTF), a Função de Espalhamento de Ponta (PSF) e o Espectro de Potência de Ruído (NPS).

---

## 2. Formulação Matemática e Propriedades

O pipeline matemático fundamenta-se na teoria dos sistemas lineares e shift-invariants (LSI), na transformada de Radon e nas transformadas integrais.

### A Transformada de Radon e Projeções
Seja $f(x,y)$ a função bidimensional representando o coeficiente de atenuação linear do tecido. A projeção paralela (sinograma) $p(\theta, t)$ é dada pela integral de linha ao longo de uma trajetória de raio X com ângulo $\theta$ e distância perpendicular $t$ ao isocentro:

$$
p(\theta, t) = \iint_{-\infty}^{\infty} f(x,y) \, \delta(x \cos\theta + y \sin\theta - t) \, dx \, dy
$$

### O Teorema da Seção Central (Fourier Slice Theorem)
O teorema fundamental que une o processamento de sinais à reconstrução de imagens estabelece que a Transformada de Fourier unidimensional de uma projeção paralela $P(\theta, \omega)$, tomada em relação à variável espacial $t$, é igual a uma fatia radial bidimensional da Transformada de Fourier bidimensional da imagem original $F(u, v)$:

$$
P(\theta, \omega) = \mathcal{F}_{1D}\{p(\theta, t)\} = F(\omega \cos\theta, \omega \sin\theta)
$$

### Retroprojeção Filtrada (Filtered Back-Projection - FBP)
Para recuperar a imagem $f(x,y)$ a partir das projeções, aplica-se o algoritmo analítico de FBP, que inclui a filtragem em rampa (*ramp filter*) no domínio da frequência para compensar o desfoque inerente à simples retroprojeção:

$$
f(x,y) = \int_{0}^{\pi} \left[ \int_{-\infty}^{\infty} P(\theta, \omega) |\omega| e^{j 2 \pi \omega t} d\omega \right]_{t = x \cos\theta + y \sin\theta} \, d\theta
$$

Onde $|\omega|$ representa o filtro rampa ideal no espaço de Fourier, frequentemente multiplicado por janelas de suavização (como Hamming, Hann ou Shepp-Logan) para controle de ruído de alta frequência.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

O processamento avançado de sinais e imagens é o núcleo tecnológico que viabiliza a evolução contínua da Tomografia Computadorizada:

- **Reconstrução Iterativa (IR) e Iterativa Baseada em Modelo (MBIR):** Superam as limitações da FBP ao incorporar estatísticas de ruído sofisticadas (Poisson e Gaussiana) e modelos físicos precisos do sistema de variação espacial (tamanho focal, geometria do detector), permitindo reduções drásticas na corrente do tubo ($mAs$) sem degradação catastrófica da relação sinal-ruído (SNR).
- **Tomografia Computadorizada Espectral e de Contagem de Fótons (PCCT):** O processamento de sinais em nível de fóton individual permite discriminar múltiplos limites de energia (*energy bins*), viabilizando a decomposição material quantitativa (ex: mapas de iodo, cálcio e água virtual) e a eliminação de artefatos de endurecimento de feixe.
- **Inteligência Artificial e Reconstrução Profunda (DLR - Deep Learning Reconstruction):** Redes neurais convolucionais (CNNs) e modelos generativos são treinados para mapear dados de baixa dose/ruídos para o domínio de alta qualidade FBP/MBIR, preservando a textura da imagem e otimizando a detectabilidade de lesões sutis.
- **Controle de Qualidade e Radiômica:** Extração de features quantitativas de textura (matrizes de co-ocorrência de níveis cinza - GLCM) exigem pipelines de processamento de imagem padronizados (reamostragem, normalização de intensidade e filtragem de espaço de Fourier) para garantir a reprodutibilidade em biomarcadores de imagem para oncologia de precisão.

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|Tomografia Computadorizada]]
- [[Reconstrução de Imagem|Reconstrucao de Imagem]]
- [[Filtro de Retroprojetor]]
- [[Dosimetria em Radiologia]]
- [[Qualidade de Imagem e Artefatos]]
- [[Inteligencia Artificial IA|Inteligencia Artificial em Radiologia]]
- [[Física das Radiações|Fisica da Radiacao]]
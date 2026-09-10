---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, reconstrucao-de-imagem, reducao-de-dose, tomografia-quantitativa]
data: 2026-08-25
---

# Jia Wang

## 1. Definição Conceitual e Fundamentação Física / Metrológica

No contexto da Física Médica\, da Tomografia Computadorizada (TC) e da Inteligência Artificial aplicada à imagem diagnóstica, **Jia Wang** refere-se a uma figura de proeminência acadêmica e científica global, cujas contribuições fundamentais moldaram o estado da arte em algoritmos de reconstrução avançados, processamento de imagem baseado em aprendizado de máquina (*Machine Learning*), tomografia espectral (DECT e contagem de fótons - PCCT) e otimização de protocolos para redução drástica da dose de radiação ionizante.

Do ponto de vista metrológico, o trabalho associado à escola de pesquisa liderada por Jia Wang aborda os desafios inerentes à quantificação precisa em TC. A metrologia em TC exige que os números de Tomografia Computadorizada (expressos em Unidades Hounsfield, $\text{HU}$) permaneçam estritamente lineares e fiéis ao coeficiente de atenuação linear macroscópico ($\mu$) do meio para raios X policromáticos. As inovações metodológicas focam na mitigação de artefatos físicos severos — como endurecimento do feixe (*beam hardening*), ofuscamento (*photon starvation*), espalhamento Compton e ruído quântico exacerbado em varreduras de baixa dose.

A integração de abordagens analíticas clássicas, como a Retroprojeção Filtrada (FBP), com técnicas variacionais de otimização convexa e, mais recentemente, com a Inteligência Artificial (Deep Learning Reconstruction - DLR e Redes Neurais Baseadas in Physics-Informed Neural Networks - PINNs), redefine os limites fundamentais do teorema de amostragem de Nyquist-Shannon em geometrias de feixe cônico (*cone-beam CT*).

## 2. Formulação Matemática e Propriedades (se aplicável)

Os frameworks matemáticos associados aos avanços metodológicos em reconstrução de TC desenvolvidos sob a égide de pesquisas contemporâneas (como as de Jia Wang e colaboradores) envolvem a formulação de problemas inversos mal-postos (*ill-posed inverse problems*). 

Considere o modelo de aquisição de dados discretizado:

$$
y = \mathcal{A}(f) + \epsilon
$$

Onde:
- $y \in \mathbb{R}^M$ representa o vetor de projeções ruidosas (sinograma, após correção logarítmica).
- $f \in \mathbb{R}^N$ é a imagem de interesse (distribuição espacial do coeficiente de atenuação linear).
- $\mathcal{A}: \mathbb{R}^N \o \mathbb{R}^M$ denota o operador linear de Radon discretizado (matriz do sistema de projeção/retroprojeção).
- $\epsilon$ representa o vetor de ruído estatístico (tipicamente modelado como uma combinação de ruído de Poisson e Gaussiano).

Para superar a instabilidade e o sobreajuste (*overfitting*) decorrentes da inversão direta ou de varreduras de baixa dose, formula-se o problema de otimização por regularização variacional (como variação total - *Total Variation*, ou prioris aprendidas por Inteligência Artificial):

$$
\hat{f} = \arg\min_{f \ge 0} \left( \frac{1}{2} \| \mathcal{A}(f) - y \|_{\Sigma^{-1}}^2 + \lambda \mathcal{R}(f) \right)
$$

Onde:
- $\| \cdot \|_{\Sigma^{-1}}^2$ é a norma ponderada pela matriz de covariância do ruído $\Sigma$, refletindo a estatística de fótons de Poisson.
- $\mathcal{R}(f)$ é o termo regularizador (ou *prior* estrutural).
- $\lambda > 0$ é o hiperparâmetro de regularização que equilibra a fidelidade aos dados e a suavização anatômica.

Em abordagens modernas de Inteligência Artificial e *Deep Learning*, o termo regularizador $\mathcal{R}(f)$ ou o próprio operador de inversão é substituído ou complementado por arquiteturas de redes neurais profundas, tais como Redes geradoras adversariais (GANs)\, difusão reversa (*Diffusion Models*) ou métodos de desdobramento de algoritmos iterativos (*Deep Unrolling* / *Learned Primal-Dual*), garantindo a preservação de texturas finas e a supressão de artefatos de estrias (*streaking artifacts*).

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

As metodologias associadas ao escopo de pesquisa de Jia Wang possuem impacto direto e profundo em diversas frentes da física médica e operação clínica:

1. **Reconstrução Iterativa Baseada模型 (MBIR) e Aprendizado Profundo (DLR):** Superação das limitações visuais e quantitativas da FBP tradicional, permitindo a manutenção da detectabilidade de lesões de baixo contraste (como metástases hepáticas ou pequenos nódulos pulmonares) mesmo sob reduções drásticas de produto corrente-tempo ($mAs$).
2. **Gerenciamento e Otimização de Dose:** Desenvolvimento de algoritmos que permitem protocolos de TC pediátrica e exames cardiológicos ultrabaixos em dose, alinhados estritamente com os princípios de radioproteção (*ALARA* - *As Low As Reasonably Achievable*).
3. **Tomografia Computadorizada Quantitativa (QCT):** Aprimoramento da acurácia na mensuração de densidade mineral óssea e caracterização tecidual baseada em números CT, viabilizando biomarcadores de imagem precisos para oncologia e cardiologia preventiva.
4. **Correção Avançada de Artefatos:** Mitigação algorítmica robusta de artefatos metálicos (OMA), artefatos por endurecimento de feixe policromático e artefatos de movimento respiratório e cardíaco.

## 4. Conexões e Wikilinks

- [[Retroprojeção Filtrada (FBP)|Retroprojecao Filtrada (FBP)]]
- [[Reconstrução Iterativa|Reconstrucao Iterativa (IR)]]
- [[Deep Learning Image Reconstruction (DLR)|DLR]]
- [[Transformada de Radon|Transformada de Radon]]
- [[Control de Qualidade em Tomografia Computadorizada]]
- [[Reducao de Dose em Tomografia Computadorizada]]
- [[Fisica da Tomografia Computadorizada]]
- [[Unidades Hounsfield|Unidades Hounsfield]]
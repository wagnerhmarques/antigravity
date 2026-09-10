---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, artefatos, correcao-de-espalhamento, qualidade-de-imagem, reconstrucao-de-imagem]
data: 2026-08-25
---

# Scatter Artifacts and Correction

## 1. Definição Conceitual e Fundamentação Física / Metrológica

Os artefatos de espalhamento (*Scatter Artifacts*) em Tomografia Computadorizada (TC) representam uma das principais degradações radiométricas que afetam a qualidade cuantitativa e qualitativa das imagens diagnósticas. Fisicamente, o espalhamento surge primariamente devido ao Efeito Compton, onde fótons de raios X de alta energia incidentes sobre o paciente sofrem desvio de trajetória e perda parcial de energia ao colidir com elétrons periféricos dos átomos constituintes dos tecidos biológicos. 

Quando esses fótons espalhados incidem sobre os elementos do detector, eles carregam informações espaciais incorretas. Como o sistema de aquisição de TC assume, por princípio fundamental de reconstrução, que todos os fótons detectados viajaram em linhas retas ininterruptas (trajetos primários) desde a fonte de raios X até o detector, o sinal decorrente do espalhamento é erroneamente interpretado como uma atenuação menor do que a real. 

Metrologicamente, a radiação espalhada atua como um sinal de fundo aditivo, suave e de baixa frequência espacial que contamina a projeção pura (sinograma). Os principais efeitos clínicos e quantitativos decorrentes desse fenômeno incluem:
* **Efeito de Copo de Vinho (*Cupping Artifact*):** Redução artificial dos valores de Número CT (unidades Hounsfield - HU) no centro de objetos grandes e homogêneos (como o abdome ou a cabeça), simulando uma concavidade no perfil de atenuação.
* **Erros de Quantificação:** Distorção severa na mensuração de coeficientes de atenuação linear, prejudicando exames de densitometria quantitativa por TC (QCT) e análises de perfusão.
* **Bandas e Estrias (*Streaking Artifacts*):** Ocorrem frequentemente em regiões de alta densidade anatômica adjacentes a estruturas de baixo número atômico (ex: junção crânio-facial, ombros ou próteses ortopédicas), onde o gradiente de espalhamento apresenta variações abruptas.

A mitigação e correção do espalhamento exigem uma abordagem combinada que engloba hardware especializado (collimadores 2D/3D, grades antidifusoras) e algoritmos computacionais avançados de correção pós-aquisição.

---

## 2. Formulação Matemática e Propriedades

Seja $I_0(E)$ o espectro de fótons incidentes e $\mu(\vec{r}, E)$ o coeficiente de atenuação linear tridimensional. O sinal ideal medido em um detector para um raio específico (linha de projeção $L$) sem espalhamento é dado pela lei de Atenuação de Beer-Lambert modificada para espectros policromáticos:

$$
I_{\text{primary}}(L) = \int_{0}^{E_{\max}} I_0(E) \exp \left( -\int_{L} \mu(\vec{r}, E) \, dl \right) dE
$$

Na presença de radiação espalhada, o sinal total detectado $I_{\text{total}}(L)$ é a superposição do sinal primário e do componente de espalhamento $I_{\text{scatter}}(L)$:

$$
I_{\text{total}}(L) = I_{\text{primary}}(L) + I_{\text{scatter}}(L)
$$

A fração de espalhamento (*Scatter-to-Primary Ratio* - SPR), denotada por $R_{\text{SPR}}(L)$, é uma métrica fundamental definida como:

$$
R_{\text{SPR}}(L) = \frac{I_{\text{scatter}}(L)}{I_{\text{primary}}(L)}
$$

Em sistemas modernos de TC multidetectores (MDCT) com grande cobertura em eixo $z$ (cone-beam CT ou ampla abertura de leque), o SPR pode exceder valores de $0.5$ a $1.0$ (ou seja, o sinal espalhado pode igualar ou superar o sinal primário no centro do detector).

O processo de correção de espalhamento busca estimar $I_{\text{scatter}}(L)$ para subtraí-lo do sinograma medido:

$$
\hat{I}_{\text{primary}}(L) = I_{\text{total}}(L) - \hat{I}_{\text{scatter}}(L)
$$

### Métodos de Modelagem Computacional

1. **Abordagens Baseadas em Convolução (Convolution-Based Scatter Estimation - CSE):**
   Assume-se que o espalhamento é uma versão suavizada (borrada) do perfil de fótons primários. A estimativa é modelada por uma operação de convolução espacial:
   
   
$$
\hat{I}_{\text{scatter}}(x, y) = \left[ w * I_{\text{total}} \right] (x, y) = \iint_{-\infty}^{\infty} I_{\text{total}}(x - x', y - y') \, h(x', y') \, dx' \, dy'
$$

   
   Onde $h(x', y')$ representa o núcleo de dispersão (*kernel* de espalhamento), empiricamente ou analiticamente ajustado em função da geometria do feixe e da espessura do objeto estimada a partir de uma pré-reconstrução.

2. **Simulações de Monte Carlo (MC):**
   Abordagem rigorosa baseada no rastreamento estatístico de trajetórias de fótons. A equação de transporte de radiação é resolvida probabilisticamente para simular interações de espalhamento Compton:
   
   
$$
I_{\text{scatter, MC}}(L) = \lim_{N \to \infty} \frac{1}{N} \sum_{i=1}^{N} \text{Peso}_{\text{Compton}, i}
$$

   
   Embora computacionalmente custosa, a aceleração via hardware moderno (GPU) permitiu a integração de algoritmos de Monte Carlo em tempo quase real nos fluxos de reconstrução clínica.

3. **Abordagens Baseadas em Aprendizado Profundo (*Deep Learning-Based Correction*):**
   Redes neurais profundas (como U-Nets convolucionais ou arquiteturas baseadas em transformadores) são treinadas com pares de sinogramas (com e sem espalhamento, obtidos via simulação de alta fidelidade):
   
   
$$
\mathcal{L}_{\text{DLR}} = \left\| \mathcal{M}_{\theta}(I_{\text{total}}) - I_{\text{scatter}} \right\|_1 + \lambda \, \text{SSIM}\left( \mathcal{R}\left(I_{\text{total}} - \mathcal{M}_{\theta}(I_{\text{total}})\right), \mu_{\text{reference}} \right)
$$

   
   Onde $\mathcal{M}_{\theta}$ é o modelo preditivo parametrizado por $\theta$, e $\mathcal{R}$ representa o operador de retroprojeção ou reconstrução.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A gestão adequada dos artefatos de espalhamento é crítica em diversos domínios da física médica e da engenharia de imagem:

* **Controle de Qualidade (CQ) e Metrologia:** Em testes de constância de sistemas de TC, a presença de artefatos de *cupping* induzidos por espalhamento pode falsear testes de uniformidade e linearidade de número CT, exigindo a aplicação de correções algorítmicas antes da avaliação métrica de ruído e resolução.
* **Tomografia Computadorizada de Cone-Beam (CBCT):** Devido à ampla abertura do cone de raios X, o volume irradiado é significativamente maior, elevando o SPR drasticamente em comparação à TC de leque convencional (*fan-beam*). Métodos avançados de correção baseados em feixes de intercepção (*beam stoppers*), grades móveis ou estimativa por Monte Carlo são mandatórios para viabilizar o uso de CBCT em radioterapia guiada por imagem (IGRT).
* **Otimização de Dose e Protocolos Pediátricos:** Reduzir a dose de radiação administrada diminui a razão sinal-ruído (SNR), tornando o sinal de espalhamento proporcionalmente mais deletério. Algoritmos robustos de correção de espalhamento acoplados a métodos de reconstrução iterativa (IR) e inteligência artificial (DLR) permitem a manutenção da diagnosticabilidade em exames de baixa dose (*low-dose CT*).
* **Observadores Computacionais:** Na avaliação de desempenho de sistemas de imagem por meio de modelos matemáticos de detecção (ex: *Channelized Hotelling Observer* - CHO), artefatos residuais de espalhamento introduzem vieses estruturais que degradam a detectabilidade de lesões sutis de baixo contraste, como nódulos pulmonares precoces ou lesões hepáticas focais.

---

## 4. Conexões e Wikilinks

* [[Tomographic Reconstruction Framework]]
* [[FBP|Filtered Backprojection (FBP)]]
* [[Iterative Reconstruction Algorithms]]
* [[Deep Learning Reconstruction (DLR)|Deep Learning Reconstruction (DLR)]]
* [[Beam Hardening Artifacts]]
* [[Cone-Beam CT (CBCT) Physics]]
* [[Monte Carlo Simulations in Medical Physics]]
* [[CT Image Quality Metrics]]
* [[Radiation Dosimetry in CT]]
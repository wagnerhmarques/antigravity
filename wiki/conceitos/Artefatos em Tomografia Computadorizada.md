---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, qualidade-de-imagem, correcao-de-artefatos, processamento-de-sinal]
data: 2026-08-25
---

# Artefatos_em_Tomografia_Computadorizada

## 1. Definição Conceitual e Fundamentação Física / Metrológica

Em Tomografia Computadorizada (TC), um **artefato** é definido como qualquer discrepância sistemática entre os valores de número de Tomografia Computadorizada (unidades Hounsfield, HU) na imagem reconstruída e os coeficientes de atenuação linear verdadeiros do objeto anatômico escaneado. Os artefatos degradam a qualidade diagnóstica da imagem, podem mascarar patologias sutis ou gerar achados falsos-positivos, constituindo uma limitação fundamental na otimização do produto entre qualidade de imagem e dose de radiação ionizante.

A formação de artefatos decorre da violação das premissas fundamentais do modelo matemático ideal de reconstrução tomográfica — em especial a equação de atenuação de feixe monocromático de Beer-Lambert e a linearidade espacial do sistema. As origens físicas e instrumentais podem ser categorizadas em três domínios principais:

1. **Físico-Interacionais:** Originam-se da interação da radiação X policromática com a matéria, gerando o endurecimento do feixe (*beam hardening*), espalhamento Compton (*scatter*) e efeitos de volume parcial (*partial volume effect*).
2. **Baseados no Paciente:** Causados pela dinâmica do paciente durante a aquisição, incluindo movimentos voluntários e involuntários (respiração, batimentos cardíacos, peristaltismo) e a presença de materiais de alta densidade metálica (próteses ortopédicas, materiais de osteossíntese, clipes cirúrgicos, contraste iodado denso).
3. **Baseados no Sistema/Instrumentais:** Decorrem de falhas\, descalibrações ou limitações físicas do *scanner* de TC, tais como defasagens de amostragem, falhas ou deriva nos elementos do detector (anéis anômalos em sistemas *third-generation*, *ring artifacts*), ruído quântico decorrente de contagens estatísticas insuficientes (baixo *mAs*), além de artefatos de amostragem por violação do Teorema de Nyquist-Shannon (aliasing).

---

## 2. Formulação Matemática e Propriedades

Para compreender a gênese dos artefatos, parte-se do feixe policromático. A intensidade do feixe de raios X após atravessar um meio heterogêneo não segue a lei exponencial simples de Beer-Lambert para um único coeficiente $\mu$. A intensidade medida $I$ é dada por:

$$
I = \int_{0}^{E_{\max}} I_0(E) \exp \left( - \int_L \mu(x, y, E) \, dl \right) dE
$$

Onde $I_0(E)$ é o espectro de energia inicial e $\mu(x, y, E)$ é o coeficiente de atenuação linear dependente da posição $(x,y)$ e da energia $E$. Como os algoritmos de retroprojeção filtrada (FBP) assumem um feixe monocromático com um coeficiente efetivo $\mu_{eff}$, a projeção logarítmica efetiva $p_{\theta}(t)$ sofre uma não-linearidade:

$$
p_{\theta}(t) = -\ln \left( \frac{I}{I_0} \right) = -\ln \left( \frac{\int_{0}^{E_{\max}} I_0(E) \exp \left( - \int_L \mu(x, y, E) \, dl \right) dE}{\int_{0}^{E_{\max}} I_0(E) \, dE} \right)
$$

Devido à atenuação preferencial dos fótons de baixa energia (endurecimento do feixe), o espectro se desloca para energias mais altas (*mean energy upshift*). Isso causa o surgimento de artefatos em forma de faixa (*cupping artifact* e *dark bands*) entre estruturas hiperdensas.

Matematicamente, o efeito do *cupping artifact* pode ser modelado na imagem reconstruída $f(r, \theta)$ pela superposição de um erro radial de baixa frequência $\epsilon(r)$:

$$
f_{reconstruida}(r, \theta) = f_{verdadeira}(r, \theta) + \epsilon(r)
$$

Onde $\epsilon(r)$ é tipicamente aproximado por uma função polinomial radial:

$$
\epsilon(r) = \sum_{k=1}^{N} a_k r^{2k}
$$

No caso de artefatos metálicos severos, a projeção sofre de extinção de fótons (o feixe é completamente atenuado em certas orientações), resultando em dados corrompidos nos projeções sinogramas $P(s, \theta)$. A operação de retroprojeção filtrada aplica um filtro rampa $H(w) = |w|$ no domínio de Fourier, amplificando os erros de alta frequência espacial gerados por descontinuidades abruptas no sinograma:

$$
\hat{f}(x, y) = \int_{0}^{\pi} \left[ \int_{-\infty}^{\infty} P(s, \theta) |w| e^{2\pi i w s} \, ds \right]_{s = x\cos\theta + y\sin\theta} \, \, d\theta
$$

Essa operação projeta raios de erro em forma de estrela (*streak artifacts*) centrados na posição do objeto de alta densidade.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A mitigação e o controle de artefatos são essenciais para a garantia da precisão quantitativa e qualitativa na prática clínica e em pesquisa (como na radiômica e na dosimetria baseada em imagens). A presença de artefatos altera diretamente os valores de número CT ($\text{HU}$), o que compromete a segmentação automática de órgãos de risco e volumes tumorais em planejamento radioterápico.

Estratégias modernas de correção e otimização operam em múltiplos estágios do pipeline de aquisição e reconstrução:

* **Pré-reconstrução (Correção no Sinograma):** Técnicas de equalização de calibração para *ring artifacts*, filtragem adaptativa de feixe policromático baseada em modelos numéricos (*Beam Hardening Correction - BHC*), e algoritmos de interpolação ou substituição de dados corrompidos para artefatos metálicos (*Normalized Metal Artifact Reduction - NMAR*).
* **Algoritmos de Reconstrução Iterativa (IR) e Aprendizado Profundo (DLR):** Algoritmos como a Reconstrução Iterativa Baseada em Modelo (MBIR) incorporam estatísticas de ruído e modelos físicos complexos de formação de imagem diretamente na função custo a ser otimizada:
  

$$
\hat{\mu} = \arg\min_{\mu} \left\{ \frac{1}{2} || \mathbf{Y} - \mathcal{P}(\mu) ||_{\Sigma^{-1}}^{2} + \beta R(\mu) \right\}
$$

  Onde $\mathbf{Y}$ representa os dados de projeção medidos, $\mathcal{P}$ o operador de projeção forward (incorporando espalhamento e policromaticidade), $\Sigma$ a matriz de covariância do ruído e $R(M)$ o termo de regularização. Redes neurais profundas (DLR) treinadas com pares de imagens sintéticas/clínicas corrompidas e limpas também demonstram alta eficácia na supressão de artefatos de movimento e metal.
* **Controle de Qualidade (QC):** Protocolos metrológicos utilizam fantasmas (*phantoms*) específicos para monitoramento periódico da uniformidade do número CT, linearidade e presença de artefatos de anel ou de feixe, garantindo a conformidade com as normas internacionais de segurança e desempenho do equipamento.

---

## 4. Conexões e Wikilinks

* [[Fisica dos Raios X|Fisica_dos_Raios_X]]
* [[Interacao_Radiacao_Materia]]
* [[Reconstrucao_Tomografica]]
* [[FBP|Retroprojecao_Filtrada]]
* [[Reconstrução Iterativa|Reconstrucao_Iterativa]]
* [[Deep_Learning_em_Tomografia]]
* [[Unidades Hounsfield|Unidades_Hounsfield]]
* [[Controle de Qualidade em TC|Controle_de_Qualidade_em_TC]]
* [[Métricas de Dose em TC|Dosimetria_em_Tomografia]]
* [[Filtros_e_Kernel_de_Reconstrucao]]
---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, aprendizado-de-maquina, reconstrucao-de-imagem]
data: 2026-08-25
---

# aprendizado de maquina

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **aprendizado de máquina** (*machine learning*, ML) constitui um subcampo da inteligência artificial (IA) e da ciência da computação focado no desenvolvimento de algoritmos e modelos estatísticos que permitem a sistemas computacionais inferir padrões a partir de dados empíricos, sem a necessidade de programação explícita de regras determinísticas. Na interface com a Física Médica e a Tomografia Computadorizada (TC), o aprendizado de máquina atua como uma ponte entre a aquisição de sinais físicos brutos (projeções atenuadas de raios X) e a interpretação diagnóstica de alto nível, operando em regimes de otimização de alta dimensionalidade.

Metrologicamente, os algoritmos de aprendizado de máquina em imageamento médico lidam com a incerteza estatística inerente à contagem de fótons (ruído quântico de Poisson) e com as limitações dos sistemas de detecção físicos. Enquanto os métodos analíticos tradicionais modelam a física do sistema de forma determinística — como na Retroprojeção Filtrada (FBP) baseada na Transformada de Radon inversa —, o aprendizado de máquina parametriza a função de mapeamento inversa por meio de otimização estocástica baseada em dados. 

O paradigma divide-se fundamentalmente em:
* **Aprendizado supervisionado:** Onde o modelo é treinado com pares de dados de entrada e rótulos de referência (*ground truth*), amplamente aplicado em tarefas de segmentação de órgãos de risco, detecção de nódulos pulmonares e classificação de patologias.
* **Aprendizado não supervisionado:** Focado na descoberta de estruturas latentes em dados não rotulados, como na redução de dimensionalidade e na detecção de anomalias anatômicas.
* **Aprendizado por reforço:** Onde um agente maximiza uma recompensa acumulada por meio de iterações com o ambiente, com aplicações emergentes na otimização de protocolos de escaneamento em tempo real.

---

## 2. Formulação Matemática e Propriedades

Formalmente, o aprendizado de máquina supervisionado busca aproximar uma função desconhecida $f: \mathcal{X} \to \mathcal{Y}$ a partir de um conjunto de treinamento $\mathcal{D} = \{(\mathbf{x}_i, \mathbf{y}_i)\}_{i=1}^{N}$, onde $\mathbf{x}_i \in \mathcal{X}$ representa o espaço de entrada (ex.: sinogramas corrompidos por ruído ou imagens de TC de baixa dose) e $\mathbf{y}_i \in \mathcal{Y}$ representa o espaço de saída (ex.: imagens de alta resolução espacial e baixo ruído).

Aparametrização da hipótese $f_{\mathbf{w}}(\mathbf{x})$ é realizada por meio de um vetor de pesos e vieses $\mathbf{w}$ (em redes neurais profundas, $\mathbf{w}$ engloba todos os tensores de pesos sinápticos). O objetivo do processo de otimização (treinamento) é minimizar o risco empírico $\mathcal{R}(\mathbf{w})$, quantificado por uma função de perda (*loss function*) $\mathcal{L}(\cdot, \cdot)$:

$$
\mathcal{R}(\mathbf{w}) = \frac{1}{N} \sum_{i=1}^{N} \mathcal{L}\left(f_{\mathbf{w}}(\mathbf{x}_i), \mathbf{y}_i\right) + \lambda \mathcal{R}(\mathbf{w})
$$

onde $\lambda \mathcal{R}(\mathbf{w})$ representa um termo de regularização (como a norma $L_1$ ou $L_2$ dos pesos) destinado a prevenir o sobreajuste (*overfitting*).

Em contextos de reconstrução de imagem em TC baseada em aprendizado profundo (*Deep Learning Reconstruction* - DLR), a função de perda frequentemente combina divergências estatísticas e perceptuais para preservar a textura anatômica e mitigar artefatos de aliasing. Por exemplo, a perda combinada L1 e estrutural (SSIM) é expressa como:

$$
\mathcal{L}_{\text{total}} = \alpha \frac{1}{M} \sum_{j=1}^{M} \left| \mathbf{y}_j - f_{\mathbf{w}}(\mathbf{x})_j \right| + (1 - \alpha) \left( 1 - \text{SSIM}(\mathbf{y}, f_{\mathbf{w}}(\mathbf{x})) \right)
$$

onde $\alpha$ pondera a contribuição de cada métrica no domínio espacial de $M$ voxels.

A otimização dos parâmetros $\mathbf{w}$ é tipicamente executada via algoritmos de gradiente descendente estocástico (SGD) ou variantes adaptativas como o Adam (*Adaptive Moment Estimation*), atualizando iterativamente os pesos através do cálculo do gradiente:

$$
\mathbf{w}^{(t+1)} = \mathbf{w}^{(t)} - \eta 
abla_{\mathbf{w}} \mathcal{L}\left(f_{\mathbf{w}^{(t)}}(\mathbf{x}_i), \mathbf{y}_i\right)
$$

sendo $\eta$ a taxa de aprendizado (*learning rate*).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

No escopo da Tomografia Computadorizada moderna, o aprendizado de máquina revolucionou três pilares fundamentais: **reconstrução de imagem**, **dosimetria e otimização de dose**, e **controle de qualidade quantitativo**.

### A. Reconstrução de Imagem (DLR e IR Avançada)
Os métodos analíticos (FBP) amplificam o ruído de alta frequência quando submetidos a doses reduzidas de radiação. Técnicas de aprendizado de máquina atuam em duas frentes principais de reconstrução:
1. **Pós-processamento no domínio da imagem:** Redes neurais convolucionais (CNNs) atuam como filtros adaptativos de remoção de ruído (*denoising*), mapeando imagens de baixa dose (ruidosas) para estimativas de alta dose.
2. **Reconstrução híbrida ou no domínio dos dados brutos (*sinograma*):** Modelos aprendem a inversa da Transformada de Radon diretamente, ou incorporam priors aprendidos dentro de algoritmos de Reconstrução Iterativa (IR) baseados em otimização convexa (como *Plug-and-Play* priors e *Deep Image Prior*).

### B. Dosimetria e Gestão de Dose
O aprendizado de máquina permite a estimativa precisa da dose absorvida em órgãos específicos de forma personalizada. Modelos preditivos utilizam os parâmetros de aquisição do escaneamento (corrente do tubo $mA$, tensão $kVp$, tempo de rotação, perfil de hélice/pitch) e os topogramas do paciente para prever mapas tridimensionais de distribuição de dose (índices $CTDI_{vol}$ e $DLP$ customizados), superando as limitações dos fantomas geométricos padrão.

### C. Radiômica e Extração de Biomarcadores
A intersecção do aprendizado de máquina com a análise de imagens de TC deu origem à **radiômica**, permitindo a extração automatizada de centenas defeatures quantitativas de textura, formato e intensidade de voxels. Esses modelos classificam lesões hepáticas, pulmonares e oncológicas, correlacionando características fenotípicas da imagem com perfis genotípicos e prognósticos clínicos.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|tomografia-computadorizada]]
* [[Reconstrução de Imagem|reconstrucao-de-imagem]]
* [[Retroprojeção Filtrada (FBP)|retroprojecao-filtrada]]
* [[Reconstrução Iterativa|reconstrucao-iterativa]]
* [[Radioproteção|dose-de-radiacao]]
* [[tomografia-computadorizada-de-baixa-dose]]
* [[Ruído Quântico|ruido-quantico]]
* [[Artefatos em TC|artefatos-em-tc]]
* [[Controle de Qualidade em TC|controle-de-qualidade]]
* [[Radiomica]]
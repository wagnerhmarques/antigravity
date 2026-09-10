---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, xai, deep-learning, dosimetria, controle-de-qualidade]
data: 2026-08-25
---

# Explainable AI (XAI)

## 1. Definição Conceitual e Fundamentação Física / Metrológica

Explainable AI (XAI) — ou Inteligência Artificial Explicável — engloba um conjunto de metodologias, algoritmos e arcabouços analíticos projetados para tornar os outputs de modelos complexos de aprendizado de máquina, especialmente redes neurais profundas (*Deep Learning*), compreensíveis e auditáveis por seres humanos (especialmente físicos médicos, radiologistas e tecnólogos). 

No contexto da Física Médica e da Tomografia Computadorizada (TC), os algoritmos de ponta frequentemente operam como "caixas-pretas" (*black boxes*). Embora modelos baseados em aprendizado profundo alcancem desempenho superior em tarefas como reconstrução de imagem, segmentação de órgãos de risco e estimativa de dose, sua falta de transparência intrínseca representa uma barreira crítica para a translação clínica regulatória e metrológica. A XAI busca mitigar esse problema ao quantificar a importância de recursos (*feature importance*), mapear a atenção espacial do modelo e fornecer justificativas causais ou correlacionais para predições específicas.

Sob a perspectiva metrológica, a XAI introduz métricas de confiabilidade e rastreabilidade para sistemas de IA. A ausência de interpretabilidade em um algoritmo de IA aplicado à TC pode ocultar falhas sistêmicas perigosas, tais como:
* **Alucinações estruturais**: Inserção ou remoção espúria de artefatos anatômicos ou patológicos (p.ex., nódulos pulmonares simulados ou apagados) em imagens reconstruídas por Redes Neurais Profundas.
* **Vieses de domínio (*domain shift*)**: Degradação oculta na acurácia do modelo quando aplicado a dados adquiridos em scanners de diferentes fabricantes ou com protocolos de varredura distintos.
* **Apreensão de artefatos em vez de anatomia**: O modelo pode classificar uma tomografia com base em artefatos de *beam-hardening* ou ruído quântico em vez de características teciduais reais.

Portanto, a XAI atua como um instrumento de controle de qualidade metrológico, permitindo avaliar a robustez, a estabilidade e a fidelidade física das inferências geradas por modelos de IA.

---

## 2. Formulação Matemática e Propriedades

Para formalizar a interpretabilidade em modelos de IA aplicados à imagem médica, utilizam-se abordagens baseadas em atribuição de feições (*feature attribution*), perturbação e gradientes.

### Grad-CAM (Gradient-weighted Class Activation Mapping)
Amplamente utilizado para gerar mapas de localização visual de alta resolução que destacam regiões importantes na imagem de TC para a tomada de decisão do modelo (p.ex., classificação de embolia pulmonar). 

Dado um mapa de ativação de uma camada convolucional profunda $\mathbf{A}^k$ (onde $k$ denota o $k$-ésimo canal), o gradiente da pontuação da classe $y^c$ (para a classe $c$) em relação ao mapa de ativação $\mathbf{A}^k$ é globalmente pooled para calcular os pesos de importância $\alpha_k^c$:

$$
\alpha_k^c = \frac{1}{Z} \sum_{i} \sum_{j} \frac{\partial y^c}{\partial A_{i,j}^k}
$$

onde $Z$ é o número total de pixels/voxels no mapa de ativação ($i, j$ são as coordenadas espaciais). O mapa Grad-CAM L $L_{\text{Grad-CAM}}^c$ é obtido pela combinação linear ponderada das ativações do mapa, seguida por uma função de ativação ReLU para reter apenas as características que influenciam positivamente a classe de interesse:

$$
L_{\text{Grad-CAM}}^c = \text{ReLU}\left( \sum_{k} \alpha_k^c \mathbf{A}^k \xrightleftharpoons{} \text{Resize}\to \Omega_{\text{input}} \right)
$$

onde $\Omega_{\text{input}}$ denota o domínio espacial da imagem de TC original.

### Shapley Additive exPlanations (SHAP)
Baseado na Teoria dos Jogos cooperativos, o SHAP atribui a cada pixel ou voxel $x_i$ um valor de Shapley $\phi_i$, que representa sua contribuição marginal para a predição do modelo $f(x)$ em relação a uma linha de base (referência) $E[f(x)]$:

$$
\phi_i(f, x) = \sum_{S \subseteq \mathcal{F} \setminus \{i\}} \frac{|S|! (|\mathcal{F}| - |S| - 1)!}{|\mathcal{F}|!} \left[ f_x(S \cup \{i\}) - f_x(S) \right]
$$

onde $\mathcal{F}$ é o conjunto de todas as características (voxels/features), $S$ é um subconjunto de características excluindo o i-ésimo, e $f_x(S)$ é a predição condicionada ao subconjunto $S$.

### Propriedades Axiomáticas Requeridas em Física Médica
Para que métodos de XAI sejam válidos em aplicações críticas de TC, eles devem satisfazer rigorosamente os seguintes axiomas metrológicos:
1. **Conservação (Efficiency)**: A soma das atribuições de todas as feições deve igualar a diferença entre a predição do modelo e o valor esperado:
   
$$
\sum_{i=1}^{M} \phi_i(x) = f(x) - E[f(x)]
$$

2. **Sensibilidade (Dummy/Null Player)**: Se uma feição $i$ não contribui para a diferença no output do modelo para todas as entradas possíveis, seu valor de atribuição deve ser estritamente zero ($\phi_i = 0$).
3. **Simetria**: Se duas feições $x_i$ e $x_j$ contribuem identicamente para todas as combinações de subconjuntos, suas atribuições devem ser iguais ($\phi_i = \phi_j$).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A integração de XAI na Tomografia Computadorizada abrange desde a aquisição dos dados brutos até o pós-processamento clínico:

* **Reconstrução Baseada em Aprendizado Profundo (DLR - *Deep Learning Reconstruction*)**: Redes neurais profundas são aplicadas para remover ruído e artefatos de feixe cônico em varreduras de baixa dose (*Low-Dose CT*). Métodos de XAI permitem auditar se a rede está efetivamente recuperando informações anatômicas reais a partir de dados sinogramas ruidosos ou se está interpolando texturas de forma alucinatória. A explicabilidade ajuda a garantir a conformidade com o princípio ALARA (*As Low As Reasonably Achievable*).
* **Controle de Qualidade (QC) Automatizado**: Sistemas de IA que avaliam o desempenho de scanners de TC (verificação de número CT, uniformidade, resolução espacial MTF através de imagens de fantasmas) utilizam XAI para demonstrar aos físicos médicos *quais* regiões do fantasma (p.ex., bordas de inserções de teflon ou acrílico) provocaram um alerta de falha no equipamento.
* **Dosimetria Computacional e Mapas de Dose**: Em TC com controle automático de corrente (mA) e protocolos de modulação espacial, modelos preditivos de dose orgânica usam XAI para evidenciar quais parâmetros topográficos do paciente (diâmetro anteroposterior, índice de massa corporal efetivo) dominaram o cálculo da dose absorvida.
* **Observadores Computacionais e Modelos de Percepção Visual**: Na avaliação de qualidade de imagem baseada em tarefas (*task-based image quality*), a XAI ajuda a desvendar se os observadores artificiais que simulam a detecção de lesões pelo olho humano estão utilizando critérios físicos idênticos aos da radiologia diagnóstica (como o Teorema de Hotelling ou ROC de desvio padrão de ruído).

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[Reconstrução de Imagem|Reconstrução de Imagem em TC]]
* [[Filtros e Retroprojeção (FBP)]]
* [[Redes Neurais Profundas em Imagem Médica]]
* [[Controle de Qualidade em TC]]
* [[Dosimetria em Radiologia]]
* [[Otimização de Dose em TC|Redução de Dose em TC]]
* [[Artefatos em Tomografia Computadorizada]]
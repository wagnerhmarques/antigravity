---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, processamento-de-imagens, radioterapia]
data: 2026-08-25
---

# Fusão de Imagens Médicas

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Fusão de Imagens Médicas** é o processo computacional de integrar informações complementares provenientes de duas ou mais modalidades de imagem diagnóstica ou terapêutica, gerando uma representação única, unificada e sinérgica. O objetivo fundamental é associar a alta resolução espacial e anatômica (característica de modalidades como a Tomografia Computadorizada - [[Tomografia Computadorizada|Tomografia Computadorizada]]) com a sensibilidade funcional, metabólica ou molecular (fornecida por modalidades como a Ressonância Magnética - RM, Tomografia por Emissão de Pósitrons - [[Tomografia por Emissão de Pósitrons (PET)|PET-CT]] ou Tomografia por Emissão de Fóton Único - SPECT).

Do ponto de vista metrológico, o processo exige rigor na cuantização espacial e na correção de artefatos. A fusão bem-sucedida depende de duas etapas estritamente sequenciais:
1. **Registro de Imagens (*Image Registration*)**: O alinhamento espacial de múltiplos conjuntos de dados para um único referencial de coordenadas, podendo ser rígido (translação e rotação para estruturas ósseas rígidas) ou não-rígido/elástico (deformações locais para acomodar movimentação orgânica ou variações anatômicas em tecidos moles).
2. **Combinação de Intensidades (*Intensity Fusion*)**: A integração propriamente dita dos voxels correspondentes, cujos métodos variam desde a simples visualização sobreposta (blending) até abordagens avançadas baseadas em transformada de wavelets ou redes neurais profundas.

Na prática clínica, a fusão mitiga as limitações inerentes a cada modalidade isolada: enquanto a [[Tomografia Computadorizada|Tomografia Computadorizada]] fornece o mapa eletrônico de atenuação (indispensável para cálculos de dose em radioterapia através dos números de Hounsfield), modalidades funcionais mapeiam processos fisiopatológicos em nível molecular, cuja localização anatômica exata seria impossível sem a referência estrutural co-registrada.

---

## 2. Formulação Matemática e Propriedades

Seja $I_A(x)$ a imagem anatômica de referência (por exemplo, TC) e $I_B(x)$ a imagem funcional ou secundária (por exemplo, PET ou RM), definidas em um domínio espacial contínuo ou discretizado $x \in \Omega \subset \mathbb{R}^n$ (onde $n=3$ para volumes tridimensionais).

### 2.1. O Problema de Otimização no Registro
O registro espacial busca encontrar uma transformação espacial otimizada $\mathcal{T}_{\mu}: \Omega \to \Omega$, parametrizada por um vetor de parâmetros $\mu$, que mapeie os pontos de $I_B$ para o espaço de $I_A$. O problema é formulado como a minimização de uma função de custo (ou energia) $C(\mu)$:

$$
\hat{\mu} = \arg\min_{\mu} \left\{ \mathcal{D}\left(I_A, I_B(\mathcal{T}_{\mu}(x))\right) + \lambda \mathcal{R}(\mu) \right\}
$$

Onde:
- $\mathcal{D}(\cdot, \cdot)$ é a métrica de **similaridade** ou dessemelhança entre as imagens. Para modalidades multimodais (como TC e PET), métricas baseadas na intensidade direta falham; utiliza-se frequentemente a **Informação Mútua (Mutual Information - MI)**, definida com base nas entropias marginais $H$ e conjunta $H(A,B)$:

$$
\text{MI}(A, B) = H(A) + H(B) - H(A, B)
$$

- $\mathcal{R}(\mu)$ é um termo de **regularização** espacial que penaliza deformações não físicas ou excessivamente irregulares (especialmente em registros não-rígidos).
- $\lambda$ é o hiperparâmetro de regularização que equilibra a precisão do ajuste e a suavidade da transformação.

### 2.2. Modelos de Transformação Espacial
A transformação $\mathcal{T}_{\mu}$ pode ser modelada de diversas formas:
* **Rígida**: Apenas rotações e translações, descritas por uma matriz homogênea $T \in \mathbb{R}^{4 \times 4}$:
  
  
$$
x' = R x + t
$$

* **Afim**: Inclui cisalhamento (*shear*) e escala além da rotação e translação.
* **Não-Rígida (Deformável)**: Incorpora campos de deslocamento local $u(x)$, de modo que:
  
  
$$
\mathcal{T}(x) = x + u(x)
$$

### 2.3. Estratégias de Combinação de Intensidades
Uma vez obtida a transformação otimizada $\mathcal{T}_{\hat{\mu}}$, o voxel fundado $I_F(x)$ em um ponto $x$ pode ser gerado por operadores lineares ou não-lineares. Em abordagens baseadas em aprendizado de máquina e redes neurais profundas ([[Inteligência Artificial na Tomografia Computadorizada]]), a fusão é modelada como uma função de mapeamento não-linear parametrizada por pesos sinápticos $\theta$:

$$
I_F(x) = \Phi_{\theta}\left( I_A(x), I_B(\mathcal{T}_{\hat{\mu}}(x)) \right)
$$

Onde $\Phi_{\theta}$ é otimizada via treinamento supervisionado ou redes geradoras adversariais (GANs) para preservar simultaneamente os detalhes de alta frequência espacial da TC (bordas ósseas e interfaces teciduais) e a distribuição de intensidade dos marcadores funcionais.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A fusão de imagens desempenha um papel central na moderna [[Tomografia Computadorizada|Tomografia Computadorizada]] clínica e na física médica através de múltiplos domínios:

1. **Planejamento em Radioterapia (RT)**: 
   A delineação de volumes alvo tumorais (GTV, CTV) e órgãos a arriscar (OARs) baseia-se fortemente na fusão de imagens de TC de planejamento com RM (maior contraste de partes moles, essencial no cérebro, próstata e pelve) e PET (delimitando a real extensão metabólica do tumor). Os mapas de densidade eletrônica da TC são mantidos para o cálculo rigoroso do espalhamento e absorção de radiação pelo algoritmo de dose, enquanto os contornos são definidos a partir do espaço fundido.

2. **Gerenciamento do Movimento Respiratório (*4D-CT e PET/CT*)**:
   Em locais sujeitos a artefatos de respiração (como tórax e abdome superior), a fusão de fases respiratórias de [[Tomografia Computadorizada|Tomografia Computadorizada]] 4D com exames PET adquiridos sob sincronização respiratória (*respiratory gating*) reduz os erros de descasamento espacial (*mismatch*), otimizando o volume de tratamento e preservando o tecido sadio.

3. **Correção de Atenuação em Medicina Nuclear Híbrida**:
   Em sistemas [[Tomografia por Emissão de Pósitrons (PET)|PET-CT]] e SPECT/CT, a fusão é inerente ao hardware e ao software de aquisição. A imagem de TC de baixa dose é convertida em mapas de coeficientes de atenuação linear para fótons de 511 keV (no caso do PET), corrigindo os fótons atenuados pelos tecidos do paciente e permitindo a quantificação absoluta da atividade metabólica (Standardized Uptake Value - SUV).

4. **Observadores Computacionais e Dosimetria Interna**:
   Na teranóstica e na radioterapia molecular, a fusão de imagens anatômicas de TC com imagens funcionais seriadas permite estimar a distribuição tridimensional de dose absorvida em órgãos-alvo e medula óssea, utilizando modelos fantomas e observadores ideais para otimizar protocolos e garantir a conformidade regulatória e metrológica.

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|Tomografia Computadorizada]]
- [[Tomografia por Emissão de Pósitrons (PET)|PET-CT]]
- [[Inteligência Artificial na Tomografia Computadorizada]]
- [[Controle de Qualidade em Tomografia Computadorizada]]
- [[Reconstrução de Imagem em Tomografia Computadorizada]]
- [[Dosimetria em Radiologia|Dosimetria em Tomografia Computadorizada]]
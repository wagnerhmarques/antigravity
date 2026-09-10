---
tipo: conceito
aliases: [R. Errico, Rosaria Errico]
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, aprendizado-de-maquina]
data: 2026-08-25
---

# R. Errico

## 1. Definição Conceitual e Fundamentação Física
**R. Errico** (Rosaria Errico) é uma pesquisadora e física atuante na interface entre a Inteligência Artificial (IA) e a Física Médica. Suas contribuições recentes concentram-se na análise crítica, sistematização e revisão do estado da arte da aplicação de métodos de aprendizado de máquina (*machine learning*) e aprendizado profundo (*deep learning*) em imageamento médico, radioterapia e dosimetria. 

No contexto da Tomografia Computadorizada (TC) e da Física Médica moderna, o trabalho associado a Errico aborda como algoritmos baseados em dados (*data-driven algorithms*) estão redefinindo o fluxo clínico\, desde a reconstrução de imagens em baixa dose até a radiômica e a predição de resposta ao tratamento. A fundamentação física subjacente a essas abordagens envolve a otimização de operadores de reconstrução inversa, a mitigação de artefatos de feixe endurecido e ruído quântico através de Redes Neurais Convolucionais (CNNs) e Redes Generativas Adversariais (GANs), mantendo a fidelidade quantitativa essencial para diagnósticos precisos.

## 2. Formulação Matemática e Propriedades
As metodologias revisadas ou desenvolvidas no escopo das pesquisas de R. Errico envolvem frequentemente a formulação de problemas inversos mal-postos em Tomografia Computadorizada, regularizados por aprendizado profundo. Seja o operador de projeção linear (transformada de Radon) $\mathcal{A}: \mathbb{R}^{N} \o \mathbb{R}^{M}$, o problema de reconstrução de imagem a partir de sinogramas ruidosos $\mathbf{y}$ pode ser expresso como:

$$
\mathbf{y} = \mathcal{A}\mathbf{x} + \boldsymbol{\epsilon}
$$

Onde $\mathbf{x}$ representa a matriz de atenuação linear do Voxel (imagem de TC) e $\boldsymbol{\epsilon}$ denota o ruído estatístico (geralmente modelado como uma combinação de Poisson e Gaussiano). Os arcabouços computacionais discutidos por Errico et al. utilizam regularização baseada em aprendizado profundo (*Deep Learning Reconstruction - DLR*), onde a função de custo a ser otimizada incorpora um prior aprendido $\mathcal{R}_{\theta}(\mathbf{x})$:

$$
\arg\min_{\mathbf{x}} \left\{ \frac{1}{2} \|\mathcal{A}\mathbf{x} - \mathbf{y}\|_2^2 + \lambda \mathcal{R}_{\theta}(\mathbf{x}) \right\}
$$

Onde $\mathcal{R}_{\theta}(\mathbf{x})$ representa uma rede neural parametrizada por $\theta$ (por exemplo, atuando como um redutor de ruído ou denoiser proximal), e $\lambda$ é o hiperparâmetro de regularização que equilibra a consistência dos dados e o prior anatômico.

## 3. Contexto no Acervo do Pesquisador & Aplicações
O nome de R. Errico aparece no acervo da pesquisa USP/FAPESP vinculado ao artigo de revisão abrangente publicado na *La Rivista del Nuovo Cimento* em 2025:

- No documento [[Inteligência Artificial em Física Médica (Nuovo Cimento)|artificial-intelligence-in-medical-physics-nuovo-cimento]] e na fonte original [[Inteligência Artificial em Física Médica (Nuovo Cimento)|artificial-intelligence-in-medical-physics-nuovo-cimento]], Errico figura como coautora ao lado de pesquisadores de destaque como [[N Amoroso|N. Amoroso]], [[E Pantaleo|E. Pantaleo]], [[A Monaco|A. Monaco]] e [[R Bellotti|R. Bellotti]].

No escopo da nossa LLM Wiki de Física Médica & Tomografia Computadorizada, a menção a R. Errico serve como âncora bibliográfica para a compreensão das tendências globais na adoção de inteligência artificial na física médica. Suas obras fornecem a base teórica e taxonômica para classificar como modelos de IA impactam o controle de qualidade, a otimização da dose de radiação ionizante e a melhoria na detectabilidade de lesões em exames de TC de baixa dose.

## 4. Conexões e Wikilinks
- [[N Amoroso|N. Amoroso]]
- [[R Bellotti|R. Bellotti]]
- [[E Pantaleo|E. Pantaleo]]
- [[A Monaco|A. Monaco]]
- [[Inteligência Artificial em Física Médica (Nuovo Cimento)|artificial-intelligence-in-medical-physics-nuovo-cimento]]
- [[Inteligência Artificial em Física Médica (Nuovo Cimento)|artificial-intelligence-in-medical-physics-nuovo-cimento]]
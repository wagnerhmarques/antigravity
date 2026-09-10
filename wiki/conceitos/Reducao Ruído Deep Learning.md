---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, reducao-ruido, dlr, aprendizagem-profunda]
data: 2026-08-25
---

# Reducao_Ruido_Deep_Learning

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A Redução de Ruído baseada em Deep Learning (DLR - *Deep Learning Reconstruction* ou algoritmos de *Denoising* baseados em redes neurais profundas) representa uma mudança de paradigma na engenharia de imagem da Tomografia Computadorizada (TC). Historicamente, a supressão de ruído e artefatos em TC dependia de métodos analíticos — como a Retroprojeção Filtrada ([[FBP|Retroprojecao_Filtrada]]) com filtros de rampa suavizados, que sacrificam a resolução espacial — ou de métodos iterativos estatísticos ([[Reconstrução Iterativa|Reconstrucao_Iterativa]]), que modelam o ruído de Poisson-Gaussiano no domínio dos dados brutos (*sinograma*), mas exigem alto custo computacional e tempo de reconstrução.

Fisicamente, o ruído quântico em TC é governado pela estatística de contagem de fótons de raio X incidentes no detector, aproximando-se de uma distribuição de Poisson modulada pelos processos de conversão fotoelétrica e eletrônica (adicionando ruído gaussiano eletrônico). Quando se reduzem os parâmetros de exposição (corrente do tubo de raios X, $mA$, ou tempo de rotação) para minimizar a dose absorvida pelo paciente ($D$), a relação sinal-ruído ($SNR$) degrada-se severamente, gerando imagens com forte granulação, perda de contrastabilidade de baixo contraste e artefatos de estrias.

As técnicas de *Deep Learning* aplicadas a esse cenário operam através de redes neurais convolucionais (CNNs) ou arquiteturas baseadas em *Transformers*, treinadas para mapear imagens degradadas por alto ruído (provenientes de baixas doses) em imagens de referência de alta qualidade (obtidas com doses plenas ou médias de referência, consideradas o padrão-ouro). O fundamento metrológico reside na capacidade desses algoritmos de aprender priors estatísticos complexos e não-lineares da anatomia humana, distinguindo estruturas anatômicas reais de flutuações estocásticas de ruído. Isso permite preservar a resolução espacial de alto contraste enquanto remove agressivamente o ruído quântico e o ruído texturizado indesejado, superando as limitações dos filtros espaciais tradicionais (como o filtro Gaussiano ou *Non-Local Means*) que frequentemente promovem o borramento (*blurring*) de bordas anatômicas finas.

## 2. Formulação Matemática e Propriedades (se aplicável)

Matematicamente, o problema de redução de ruído pode ser formulado como a estimação de uma imagem limpa $\mathbf{x} \in \mathbb{R}^{N}$ a partir de uma imagem ruidosa corrompida $\mathbf{y} \in \mathbb{R}^{N}$, onde:

$$
\mathbf{y} = \mathcal{H}(\mathbf{x}) + \mathbf{n}
$$

sendo $\mathcal{H}$ o operador do sistema (frequentemente aproximado como a identidade em abordagens aplicadas ao domínio da imagem, ou o projetor avançado em abordagens no domínio dos dados brutos) e $\mathbf{n}$ o termo de ruído estocástico e eletrônico.

Em uma abordagem baseada em aprendizado supervisionado, o objetivo é treinar uma rede neural parametrizada por pesos e vieses $\theta$ (representada pelo operador $\mathcal{F}_\theta(\mathbf{y})$) para minimizar uma função de perda (*loss function*) $\mathcal{L}$ sobre um conjunto de treinamento com $M$ pares de imagens $(\mathbf{y}_i, \mathbf{x}_i)$:

$$
\theta^* = \arg\min_{\theta} \frac{1}{M} \sum_{i=1}^{M} \mathcal{L}\left(\mathcal{F}_\theta(\mathbf{y}_i), \mathbf{x}_i\right)
$$

As funções de perda mais comuns combinam perdas baseadas em pixels com perdas perceptuais para evitar o efeito de borramento excessivo:

1. **Erro Quadrático Médio (MSE) / Norma $L_2$:**
   
$$
\mathcal{L}_{MSE}(\theta) = \frac{1}{N} \left\| \mathcal{F}_\theta(\mathbf{y}) - \mathbf{x} \right\|_2^2
$$

   *Propriedade:* Conduce a valores ótimos baseados na média condicional, mas tende a produzir imagens excessivamente suavizadas (perda de texturas finas).

2. **Erro Absoluto Médio (MAE) / Norma $L_1$:**
   
$$
\mathcal{L}_{L1}(\theta) = \frac{1}{N} \left\| \mathcal{F}_\theta(\mathbf{y}) - \mathbf{x} \right\|_1
$$

   *Propriedade:* Preserva melhor as bordas agudas em comparação ao MSE, embora ainda possa sofrer de falta de nitidez textural.

3. **Perda Perceptual Baseada em Redes Pré-treinadas (Feature Reconstruction Loss):**
   
$$
\mathcal{L}_{perc}(\theta) = \frac{1}{C_j H_j W_j} \left\| \phi_j(\mathcal{F}_\theta(\mathbf{y})) - \phi_j(\mathbf{x}) \right\|_2^2
$$

   onde $\phi_j$ representa os mapas de características extraídos da camada $j$ de uma rede de classificação de imagens pré-treinada (ex: VGG-16).

4. **Perda Adversarial (no contexto de Redes Generativas Adversariais - GANs):**
   
$$
\min_{\theta} \max_{D} \mathbb{E}_{\mathbf{x}} [\log D(\mathbf{x})] + \mathbb{E}_{\mathbf{y}} [\log (1 - D(\mathcal{F}_\theta(\mathbf{y})))]
$$

   onde $D$ é a rede discriminadora. Esta formulação força a imagem gerada a possuir texturas estatisticamente indistinguibles das imagens reais de alta dose.

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A integração de algoritmos de Redução de Ruído por Deep Learning na cadeia de reconstrução de TC transformou profundamente a prática clínica e a metrologia dos exames radiológicos:

* **Otimização de Dose e Princípio ALARA:** Permite reduções drásticas na carga de radiação ionizante (frequentemente entre 40% e 80% dependendo do protocolo e da região anatômica) mantendo ou melhorando a detectabilidade de lesões de baixo contraste (como metástases hepáticas ou pequenos nódulos pulmonares).
* **Mitigação de Artefatos de Fótons Escassos (*Photon Starvation*):órgãos densos como ombros, pelve ou crânio causam forte atenuação e ruído extremo. Modelos de DLR conseguem restaurar a integridade numérica dos números CT (unidades Hounsfield - HU), preservando a exatidão quantitativa essencial para exames de perfusão e radioterapia.**
* **Controle de Qualidade e Metrologia de Imagem:** Diferente dos filtros tradicionais que alteram a Função de Dispersão de Ponto (PSF) e a Modulação da Função de Transferência (MTF) de maneira uniforme e indesejada, implementações modernas de DLR buscam preservar a resolução espacial original ao mesmo tempo em que eliminam o ruído. Contudo, impõem novos desafios para os físicos médicos no [[Controle de Qualidade em TC|Controle_Qualidade_TC]], exigindo o desenvolvimento de métodos de avaliação baseados em observadores modelo e texturas artificiais ([[Textura_Imagem_TC]]).

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia_Computadorizada]]
* [[FBP|Retroprojecao_Filtrada]]
* [[Reconstrução Iterativa|Reconstrucao_Iterativa]]
* [[Controle de Qualidade em TC|Controle_Qualidade_TC]]
* [[Textura_Imagem_TC]]
* [[Dosimetria em TC|Dosimetria_Em_TC]]
---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, ruido-quantico, estatistica-de-poisson, qualidade-de-imagem\, dosimetria, filtragem]
data: 2026-08-25
---

# ruído

## 1. Definição Conceitual e Fundamentação Física / Metrológica

Em Tomografia Computadorizada (TC) de raios X, o **ruído** é definido como a flutuação espacial e temporal indesejada nos valores de pixels ou voxels de uma imagem reconstruída, a qual não representa variações reais no coeficiente de atenuação linear ($\mu$) do objeto escaneado. O ruído degrada a detectabilidade de estruturas de baixo contraste e limita a resolução de contraste da modalidade.

A origem fundamental do ruído na TC moderna é a natureza estatística corpuscular da radiação ionizante\, descrita pela mecânica quântica como fótons individuais de raios X. O feixe de raios X gerado pelo tubo não é um fluxo perfeitamente contínuo e homogêneo, mas sim um processo estocástico regido pela estatística de contagem de fótons. 

Quando um feixe de raios X policromático com intensidade incidente $N_0$ atravessa um meio material de espessura $x$ e coeficiente de atenuação linear efetivo $\mu$, o número médio de fótons $N$ que emerge e atinge o detector é dado pela lei de atenuação exponencial:

$$
N = N_0 \exp\left( -\int \mu(x) \, dx \right)
$$

Como a emissão de fótons pelo tubo de raios X e a sua detecção subsequente são eventos independentes que ocorrem a uma taxa média constante no tempo, o processo de contagem de fótons segue uma **distribuição de Poisson**. Consequentemente, a incerteza padrão (desvio padrão) associada ao número de fótons contidos em um determinado elemento de detecção é igual à raiz quadrada do número médio de fótons detectados ($\sigma_N = \sqrt{N}$). 

Essa relação fundamental estabelece o compromisso clássico (trade-off) da Tomografia Computadorizada: para reduzir o ruído estatístico (aumentando a precisão da medição), é necessário aumentar o número de fótons detectados, o que implica obrigatoriamente em um incremento na dose de radiação absorvida pelo paciente ($D$).

Além do ruído quântico primário (frequentemente denominado *quantum noise* ou *photon shot noise*), a cadeia de aquisição de sinal da TC introduz outras fontes estocásticas e determinísticas:
* **Ruído Eletrônico:** Originado nos circuitos de leitura dos fotodiodos e amplificadores dos detectores (especialmente relevante em baixas doses, onde $N$ é pequeno).
* **Ruído Estrutural e de Discretização:** Decorrente da quantização analógica-digital e de imperfeições na resposta espacial dos elementos do detector.
* **Artefatos de Feixe Policromático (Beam Hardening):** Embora estritamente sejam artefatos determinísticos, interagem de maneira complexa com o ruído, alterando sua textura e amplitude espacial através do processo de retroprojeção.

---

## 2. Formulação Matemática e Propriedades (se aplicável)

A quantificação do ruído em imagens de TC é realizada tipicamente por meio do **desvio padrão** ($\sigma$) dos números de Hounsfield (HU) em uma região de interesse (ROI - *Region of Interest*) homogênea, como um fantoma de água.

Matematicamente, seja $I(x,y)$ a matriz da imagem reconstruída e $I_{\text{ROI}}$ a média dos valores de intensidade em uma ROI contendo $M$ pixels:

$$
\sigma_{\text{ROI}} = \sqrt{ \frac{1}{M - 1} \sum_{i=1}^{M} \left( I(i) - \overline{I}_{\text{ROI}} \right)^2 }
$$

No domínio espacial, a propagação do erro estatístico das projeções (sinograma) através de algoritmos de reconstrução linear, como a **Retroprojeção Filtrada (FBP - *Filtered Backprojection*)**, afeta drasticamente a textura e a magnitude do ruído. Se o filtro rampa (usado para mitigar o desfoque $1/r$ da retroprojeção simples) for multiplicado por um filtro de corte de alta frequência (como *Hann*, *Hamming* ou *Butterworth*), o espectro de potência do ruído é modificado.

A **Função de Espalhamento de Potência do Ruído (NPS - *Noise Power Spectrum*)**, também conhecida como Wiener Spectrum\, descreve a distribuição espacial e a textura do ruído em função da frequência espacial $(f_x, f_y)$. Ela é definida como a transformada de Fourier bidimensional da função de autocorrelação espacial do ruído $R(\Delta x, \Delta y)$:

$$
\text{NPS}(f_x, f_y) = \lim_{X,Y \to \infty} \frac{1}{X Y} \left\langle \left| \iint_{X,Y} \left[ I(x,y) - \overline{I} \right] e^{-j 2 \pi (f_x x + f_y y)} \, dx \, dy \right|^2 \right\rangle
$$

Onde $\langle \cdot \rangle$ representa o operador de ensemble (média sobre múltiplas realizações/scans). A variância total do ruído $\sigma^2$ na imagem pode ser obtida integrando o NPS sobre todo o plano de frequências espaciais:

$$
\sigma^2 = \iint_{-\infty}^{\infty} \text{NPS}(f_x, f_y) \, df_x \, df_y
$$

Para sistemas ideais com FBP, a variância do ruído escala inversamente com o cubo do tamanho do pixel ($d^3$), inversamente com a espessura do corte ($z$), e inversamente com a dose de radiação ($D$), obedecendo aproximadamente à lei de scaling:

$$
\sigma^2 \propto \frac{e^{\mu t}}{E \cdot \text{Dose} \cdot d^3 \cdot z}
$$

Onde $E$ representa a eficiência quântica do detector e $t$ a espessura do objeto.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

O gerenciamento do ruído é o eixo central do princípio **ALARA** (*As Low As Reasonably Achievable*) em radiologia diagnóstica. Otimizar um protocolo de TC significa maximizar a qualidade diagnóstica da imagem — o que frequentemente exige a minimização do ruído — mantendo a dose de radiação ao paciente no menor nível tecnicamente exequível.

### Impacto nas Técnicas de Reconstrução
1. **Retroprojeção Filtrada (FBP):** Como é um algoritmo analítico linear, a FBP amplifica severamente o ruído de alta frequência inerente aos dados de projeção. Para conter o ruído, os radiologistas são forçados a utilizar filtros de suavização espacial que degradam a resolução espacial.
2. **Reconstrução Iterativa (IR - *Iterative Reconstruction*):** Algoritmos estatísticos e híbridos (ex. ASiR, AIDR, SAFIRE, Veo) incorporam modelos estatísticos precisos do ruído (distribuição de Poisson e Gaussiana combinadas) e modelos do sistema óptico (*forward/backward projections*). Isso permite suprimir o ruído de forma não linear no espaço bruto de dados ou na imagem, preservando as bordas anatômicas e permitindo reduções drásticas de dose (frequentemente entre 30% e 70%).
3. **Reconstrução Baseada em Aprendizado Profundo (DLR - *Deep Learning Reconstruction*):** Redes neurais profundas treinadas em pares de imagens de alto ruído (baixa dose) e baixo ruído (alta dose) aprendem a mapear e remover o ruído mantendo a textura visual natural e a acurácia radiômica.

### Controle de Qualidade (CQ) e Metrologia
O monitoramento do ruído é um teste obrigatório nos programas de garantia da qualidade de equipamentos de TC. Utilizando fantomas cilíndricos padronizados preenchidos com água, mede-se o desvio padrão em ROIs centrais e periféricas. Desvios inesperados nos valores de ruído indicam falhas no tubo de raios X (instabilidade no fluxo de corrente do filamento)\, degradação dos elementos do detector ou problemas de calibração do feixe.

### Observadores Computacionais
Na avaliação avançada de qualidade de imagem, o ruído não é analisado isoladamente, mas em conjunto com a resolução espacial através da **Teoria de Detecção de Sinais**. O uso de observadores modelo (como o *Non-Prewhitening Matched Filter* com canal de visibilidade - NPWE) avalia a detectabilidade de lesões de baixo contraste (ex. nódulos hepáticos incipientes) em ambientes dominados por ruído estocástico texturizado, superando as limitações do olho humano e das métricas tradicionais baseadas unicamente na Razão Sinal-Ruído (SNR - *Signal-to-Noise Ratio*) e Razão Contraste-Ruído (CNR - *Contrast-to-Noise Ratio*).

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|tomografia-computadorizada]]
* [[Retroprojeção Filtrada (FBP)|retroprojecao-filtrada]]
* [[Reconstrução Iterativa|reconstrucao-iterativa]]
* [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction]]
* [[funcao-de-espalhamento-de-potencia-do-ruido]]
* [[estatistica-de-poisson]]
* [[Radioproteção|dose-de-radiacao]]
* [[Radioproteção|alara]]
* [[Controle de Qualidade em TC|controle-de-qualidade]]
* [[Resolução Espacial|resolucao-espacial]]
* [[resolucao-de-contraste]]
* [[SNR|relacao-sinal-ruido]]
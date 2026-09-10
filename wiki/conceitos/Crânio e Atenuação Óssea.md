---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, neuroimagem, dosimetria, processamento-de-imagem, artefactos]
data: 2026-08-25
---

# crânio

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **crânio** humano constitui uma estrutura osteofibrosa complexa que envolve e protege o encéfalo, os órgãos dos sentidos e as porções iniciais dos sistemas respiratório e digestório. Do ponto de vista da física médica e da tomografia computadorizada (TC), o crânio representa um dos volumes anatômicos mais desafiadores devido à sua extrema heterogeneidade estrutural e alto número atômico efetivo ($Z_{ef}$) em comparação aos tecidos moles adjacentes.

Anatomicamente, o crânio divide-se na calota craniana (neurocrânio) e na base do crânio, sendo composto predominantemente por osso cortical (denso e compacto) externamente, osso trabecular (esponjoso ou *diplõe*) internamente, e medula óssea. Esta arquitetura sanduíche gera uma variação acentuada nos coeficientes de atenuação linear ($\mu$) para os feixes de raios X policromáticos utilizados na TC.

Metrologicamente, a quantificação da densidade mineral óssea e a imagem diagnóstica do crânio são fundamentadas na escala de Hounsfield (HU). Enquanto o parênquima cerebral oscila entre $20\text{ HU}$ e $45\text{ HU}$, o osso cortical do crânio pode atingir valores superiores a $+1000\text{ HU}$ a $+3000\text{ HU}$. Essa discrepância extrema de atenuação é a principal fonte de artefatos de imagem, tais como o endurecimento do feixe (*beam hardening*), efeitos de volume parcial e espalhamento Compton exacerbado.

## 2. Formulação Matemática e Propriedades (se aplicável)

A interação dos fótons de raios X com o tecido ósseo do crânio é regida pela lei de atenuação de Beer-Lambert para feixes policromáticos. O feixe emergente $I$ é expresso por:

$$
I = I_0 \int_{E} \Phi(E) \exp \left( -\int_L \mu(x, y, z, E) \, dl \right) dE
$$

Onde:
- $I_0$ é a intensidade inicial do feixe.
- $\Phi(E)$ é o espectro de energia dos fótons de raios X.
- $\mu(x, y, z, E)$ é o coeficiente de atenuação linear espacial e energético, altamente dependente do efeito fotoelétrico ($\propto Z^3/E^3$) predominante nas energias mais baixas encontradas na interface óssea.

O valor em Unidades Hounsfield ($\text{HU}$) para um voxel contendo estrutura craniana é definido por:

$$
\text{HU} = 1000 \times \frac{\mu_{\text{tecido}} - \mu_{\text{água}}}{\mu_{\text{água}} - \mu_{\text{ar}}}
$$

Devido ao endurecimento do feixe ao atravessar o osso cortical denso, o espectro policromático sofre deslocamento para energias médias mais altas (*beam hardening*), alterando $\mu_{\text{tecido}}$ de forma não linear ao longo do caminho do raio. O erro resultante na projeção $\Delta p$ pode ser modelado por:

$$
\Delta p = -\ln \left[ \int \Phi(E) e^{-\int \mu(E) dl} dE \right] + \int \Phi(E) \left[ -\int \mu(E) dl \right] dE
$$

Para mitigar esse efeito, algoritmos de correção baseados em polinômios ou métodos iterativos baseados em decomposição de materiais (como TC de dupla energia - *Dual-Energy CT*) resolvem a densidade eletrônica $\rho_e$ e o número atômico efetivo $Z_{ef}$ através de:

$$
\mu(E) = a_1(E) f_{\text{KN}}(E) \rho_e + a_2(E) f_{\text{PE}}(Z) \rho_m
$$

Onde $f_{\text{KN}}$ representa a função de Klein-Nishina para o espalhamento Compton e $f_{\text{PE}}$ representa a dependência do efeito fotoelétrico.

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A aquisição e processamento de imagens tomográficas do crânio exigem protocolos específicos de otimização para equilibrar a qualidade diagnóstica e a dose de radiação absorvida:

- **Protocolos de Aquisição (Neuro-TC):** Utilizam-se potenciais de tubo elevados (tipicamente $120\text{ kVp}$ a $140\text{ kVp}$) para garantir penetração adequada através da base do crânio e reduzir artefatos de feixe endurecido, embora técnicas modernas de $80\text{ kVp}$ a $100\text{ kVp}$ combinadas com filtragem iterativa avançada venham sendo aplicadas para otimização da relação contraste-ruído (CNR) em tecidos moles cerebrais.
- **Dosimetria:** O crânio abriga órgãos criticamente radiossensíveis, como o cristalino, a glândula tireoide (nas varreduras de base) e a medula óssea ativa. Métodos de modulação de corrente de tubo tridimensional ($\text{angular e longitudinal}$) são essenciais para adaptar a dose à geometria elíptica e altamente densa do crânio.
- **Reconstrução de Imagem:** 
  - **FBP (Filtered Backprojection):** Tradicionalmente propensa a artefatos de raias (*streaking*) entre as porções petrosas do osso temporal.
  - **IR (Iterative Reconstruction) e DLR (Deep Learning Reconstruction):** Indispensáveis para mitigar ruídos quânticos severos decorrentes da alta atenuação óssea, permitindo reduções significativas na dose sem perda de resolutividade espacial para avaliação de hemorragias sutis ou fraturas cranianas complexas.
- **Controle de Qualidade:** Fichas antropomórficas de crânio (*phantoms*) contendo inserções com densidades equivalentes ao osso cortical e trabecular são utilizadas rotineiramente para avaliar a acurácia numérica da escala HU e a eficácia dos algoritmos de correção de artefatos.

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|tomografia-computadorizada]]
- [[Coeficiente de Atenuação Linear|coeficiente-de-atenuacao-linear]]
- [[Unidades Hounsfield|unidade-hounsfield]]
- [[artefato-de-endurecimento-de-feixe]]
- [[filtragem-iterativa]]
- [[reconstrucao-por-retroprojetocao-filtrada]]
- [[Tomografia Computadorizada Espectral|tomografia-de-dupla-energia]]
- [[dosimetria-em-radiodiagnostico]]
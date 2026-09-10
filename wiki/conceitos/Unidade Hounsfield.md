---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, metrologia, reconstrucao-de-imagem, radiologia-digital]
data: 2026-08-25
---

# Unidade Hounsfield

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Unidade Hounsfield** (símbolo: **HU**, do inglês *Hounsfield Unit*), historicamente denominada *Hounsfield Number* ou *pixel value*, constitui a unidade de medida padronizada e adimensional utilizada em Tomografia Computadorizada (TC) para expressar o coeficiente de atenuação linear dos raios X em um determinado voxel, relativo ao coeficiente de atenuação da água pura sob condições padronizadas de temperatura e pressão. 

Desenvolvida matematicamente a partir dos princípios pioneiros de reconstrução tomográfica por Godfrey Hounsfield — laureado com o Nobel de Fisiologia ou Medicina em 1979 —, a escala Hounsfield estabelece um referencial metrológico quantitativo que supera as limitações qualitativas da radiografia convencional. Na radiografia convencional, a imagem é uma projeção planar bidimensional que comprime a atenuação tridimensional dos tecidos em uma escala de cinzas dependente de fatores cinemáticos do feixe (kVp, mAs) e da resposta do receptor de imagem (filme-sensível ou painel plano). Em contraste, a TC reconstrói numericamente mapas espaciais tridimensionais de coeficientes de atenuação linear locais ($\mu$), e a conversão desses valores para HU padroniza a escala de cinzas de forma independente do equipamento, do feixe policromático (em primeira aproximação) e do algoritmo de detecção.

Na escala Hounsfield convencional:
* O ar seco (nas condições padrão de câmara de calibração) é fixado em $-1000\text{ HU}$.
* A água destilada e quimicamente pura é fixada em $0\text{ HU}$.
* O osso cortical denso ou materiais metálicos de alta densidade podem atingir valores superiores a $+1000\text{ HU}$ ou até $+3000\text{ HU}$ dependendo da calibração do tomógrafo.

A importância metrológica da HU reside na sua capacidade de transformar uma imagem diagnóstica em um mapa quantitativo de densidade eletrônica e número atômico efetivo, viabilizando a diferenciação tecidual precisa (por exemplo, distinguindo cistos renais de conteúdos sólidos com base em variações sutis de atenuação) e o planejamento radioterápico avançado, onde os valores de HU são convertidos diretamente em densidades relativas de fótons para o cálculo de distribuição de dose.

---

## 2. Formulação Matemática e Propriedades

O valor de um pixel/voxel em Unidades Hounsfield ($\text{HU}_x$) em um ponto espacial $x$ é matematicamente definido pela seguinte equação de normalização linear:

$$
\text{HU}_x = 1000 \times \frac{\mu_x - \mu_{\text{água}}}{\mu_{\text{água}} - \mu_{\text{ar}}}
$$

Onde:
* $\mu_x$ representa o coeficiente de atenuação linear efetivo do tecido ou material contido no voxel analisado ($\text{cm}^{-1}$).
* $\mu_{\text{água}}$ é o coeficiente de atenuação linear efetivo da água pura sob condições normais de referência ($\text{cm}^{-1}$).
* $\mu_{\text{ar}}$ é o coeficiente de atenuação linear efetivo do ar atmosférico sob condições normais de referência ($\text{cm}^{-1}$). Dado que $\mu_{\text{ar}} \approx 0\text{ cm}^{-1}$, a equação é frequentemente simplificada na prática clínica para:

$$
\text{HU}_x = 1000 \times \frac{\mu_x - \mu_{\text{água}}}{\mu_{\text{água}}}
$$

### Propriedades Físico-Matemáticas Avançadas:
1. **Linearidade do Sistema:** O sistema de reconstrução de TC assume uma relação linear estrita entre os números digitais brutos (após a aplicação do logaritmo negativo nas projeções cruas) e o coeficiente de atenuação linear reconstruído.
2. **Dependência Energética (Feixe Policromático):** Como os tubos de raios X produzem um espectro de raios X policromático, o coeficiente de atenuação $\mu$ depende da energia dos fótons. Consequentemente, $\mu_x$ e $\mu_{\text{água}}$ variam com o potencial do tubo ($\text{kVp}$) selecionado e com a filtração inerente e adicional. Isso introduz artefatos de *beam-hardening* (endurecimento do feixe), fazendo com que o valor em HU de um mesmo tecido varie sutilmente se escaneado sob diferentes protocolos de tensão de pico.
3. **Conversão para Densidade Eletrônica e Número Atômico:** Em TC de dupla energia (*Dual-Energy CT* - DECT), a decomposição material baseia-se na extensão da formulação da HU em diferentes níveis energéticos para extração de mapas de densidade eletrônica relativa ($\rho_e$) e número atômico efetivo ($Z_{\text{eff}}$), expressos pelas relações fundamentais de espalhamento Compton e efeito fotoelétrico:

$$
\mu(E) \approx \rho_e \left[ Z_{\text{eff}}^{3.5} F_{\text{photo}}(E) + F_{\text{Compton}}(E) \right]
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A calibração, estabilidade e precisão das Unidades Hounsfield são pilares fundamentais no fluxo de trabalho clínico e na pesquisa avançada em imagem médica:

* **Controle de Qualidade (QC) e Metrologia:** Os testes periódicos de controle de qualidade de tomógrafos computadorizados utilizam **fantasmas de calibração** (como os fantasmas do ACR - *American College of Radiology* ou CATPHAN). Nesses dispositivos, inserções de materiais equivalentes a tecidos (tecido adiposo, água, tecidos moles, osso, acrílico, teflon) são escaneadas para verificar se os valores médios de HU medidos estão dentro de tolerâncias estritas (tipicamente $\pm 4\text{ HU}$ para a água e faixas específicas para os demais materiais). Desvios indicam problemas na calibração do gerador, desvios na filtragem do feixe ou falhas de calibração do detector.
* **Redução de Artefatos e Algoritmos de Reconstrução:** Algoritmos modernos de reconstrução, incluindo a Retroprojeção Filtrada (FBP), Reconstrução Iterativa (IR) e abordagens baseadas em Aprendizado Profundo (*Deep Learning Reconstruction* - DLR), dependem da fidelidade dos valores de HU para preservar a quantificação precisa de estruturas anatômicas sob baixas doses de radiação. Ruídos quânticos gerados por protocolos de baixa dose manifestam-se como desvios estatísticos na distribuição de pixels, alterando a precisão do desvio padrão ($\sigma_{\text{HU}}$) e degradando o contraste de baixo contraste.
* **Radioterapia Guiada por Imagem (IGRT) e Dosimetria Computacional:** No planejamento de tratamentos radioterápicos, curvas de calibração específicas convertem matrizes de HU em curvas de densidade relativa eletrônica e stopping power relativo (SPR) para fótons e prótons. Erros sistemáticos na calibração de HU traduzem-se diretamente em erros no cálculo volumétrico da dose absorvida no volume-alvo tumoral e nos órgãos de risco (OAR).
* **Radiômica e Inteligência Artificial (IA):** A extração de biomarcadores quantitativos de textura e morfologia (radiômica) depende diretamente da reprodutibilidade dos valores de HU. Variações na aquisição (diferentes fabricantes de scanners, protocolos de reconstrução ou níveis de dose) induzem artefatos de *harmonização de features*, exigindo técnicas avançadas de normalização baseadas em quantil ou reamostragem em HU para assegurar a robustez de modelos preditivos baseados em IA.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[Coeficiente de Atenuação Linear]]
* [[Filtração e Espectro de Raios X]]
* [[Reconstrução de Imagem|Reconstrução de Imagem em TC]]
* [[Retroprojeção Filtrada (FBP)|Retroprojeção Filtrada]]
* [[Reconstrução Iterativa|Reconstrução Iterativa]]
* [[Tomografia Computadorizada Espectral|Tomografia de Dupla Energia]]
* [[Controle de Qualidade em TC|Controle de Qualidade em Radiodiagnóstico]]
* [[Dosimetria em Radioterapia]]
* [[Radiômica e Inteligência Artificial]]
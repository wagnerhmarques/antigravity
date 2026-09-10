---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, artefatos, qualidade-de-imagem, fisica-dos-raios-x]
data: 2026-08-25
---

# beam-hardening

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O endurecimento do feixe (conhecido em inglês como *beam-hardening*) é um fenômeno físico que ocorre quando um feixe de raios X policromático — isto é, composto por fótons de diferentes energias (espectro contínuo) — propaga-se através de um meio material. À medida que o feixe penetra no objeto, os fótons de menor energia (raios X moles) possuem uma seção de choque de atenuação significativamente maior (predominantemente devido ao efeito fotoelétrico) em comparação aos fótons de maior energia (raios X duros). 

Consequentemente, a taxa de atenuação não é uniforme ao longo do espectro: os fótons de baixa energia são preferencialmente absorvidos nas camadas mais superficiais do material percorrido. O feixe emergente torna-se, portanto, progressivamente "mais duro" (com uma energia média efetiva maior e um espectro deslocado para frequências mais altas) do que o feixe incidente.

Em Tomografia Computadorizada (TC), os algoritmos tradicionais de reconstrução de imagem (como a Retroprojeção Filtrada - FBP) fundamentam-se na **Lei de Beer-Lambert** estritamente para radiação **monocromática**:

$$
I = I_0 \exp\left(-\int \mu(x,y) \, dl\right)
$$

Onde $I_0$ é a intensidade incidente, $I$ é a intensidade transmitida e $\mu(x,y)$ é o coeficiente de atenuação linear. Como o feixe polienergético viola a linearidade assumida por esta equação (a atenuação não é linear com a espessura do material), o sistema de reconstrução interpreta erroneamente a redução não linear da intensidade como se houvesse variações espaciais anômalas na densidade ou número atômico efetivo do tecido. Isso gera artefatos visuais característicos na imagem tomográfica final, primordialmente divididos em duas categorias:

1. **Efeito de Endurecimento Geral (CUPPING EFFECT / Efeito Taça):** Ocorre tipicamente em objetos cilíndricos homogêneos (como a cabeça ou o abdome). Os fótons centrais sofrem maior endurecimento e, portanto, parecem ser menos atenuados do que o previsto pela lei linear, resultando em uma subestimação dos valores de número de Hounsfield ($HU$) no centro da imagem em comparação à periferia, criando um perfil visual semelhante a uma taça.
2. **Efeito de Faixas e Estrias (STREAKS & DARK BANDS):** Ocorre na presença de estruturas de alta densidade e número atômico efetivo elevado adjacentes a tecidos moles (por exemplo, os ossos do crânio, implantes metálicos ortopédicos ou agentes de contraste iodados concentrados). As fortes variações espectrais ao longo de trajetórias específicas criam bandas escuras e claras (estrias) que irradiam entre essas estruturas densas.

---

## 2. Formulação Matemática e Propriedades (se aplicável)

Para modelar matematicamente o fenômeno, considere um feixe de raios X policromático com um espectro de intensidade inicial dado por $S_0(E)$, onde $E$ representa a energia do fóton. A intensidade medida $I$ após o feixe atravessar um material de espessura $L$ e coeficiente de atenuação linear dependente da energia $\mu(E, x)$ ao longo do caminho de integração $L$ é expressa por:

$$
I = \int_{0}^{E_{\max}} S_0(E) \exp\left( -\int_{L} \mu(E, x) \, dl \right) dE
$$

O coeficiente de atenuação linear $\mu(E, x)$ de um elemento ou composto químico pode ser decomposto nas contribuições dos principais processos de interação (efeito fotoelétrico, espalhamento Compton e espalhamento Coerente/Rayleigh):

$$
\mu(E, x) = \rho_e(x) \left[ Z_{\text{eff}}(x)^3 \cdot f_{\text{PE}}(E) + f_{\text{Compton}}(E) + f_{\text{Rayleigh}}(E) \right]
$$

Onde:
- $\rho_e(x)$ é a densidade eletrônica espacial.
- $Z_{\text{eff}}(x)$ é o número atômico efetivo do meio.
- $f_{\text{PE}}(E)$, $f_{\text{Compton}}(E)$ e $f_{\text{Rayleigh}}(E)$ são funções conhecidas que descrevem a dependência energética das seções de choque de interação.

O logaritmo negativo da razão de intensidades medido pelo sistema de aquisição (a projeção bruta ou sinograma modificado $p$) é dado por:

$$
p = -\ln\left( \frac{I}{I_0} \right) = -\ln\left( \frac{\int_{0}^{E_{\max}} S_0(E) \exp\left( -\int_{L} \mu(E, x) \, dl \right) dE}{\int_{0}^{E_{\max}} S_0(E) \, dE} \right)
$$

Se o feixe fosse monocromático com energia efetiva $E_{\text{eff}}$, teríamos $p = \int_L \mu(E_{\text{eff}}, x) \, dl$, mantendo a linearidade. Contudo, devido à integral no numerador, $p$ não é uma função linear de $\int_L \mu(E, x) \, dl$. 

Para quantificar a não-linearidade, define-se a função de correção polinomial empírica aplicada ao sinograma bruto medido $p_{\text{med}}$ para estimar o sinograma corrigido $p_{\text{corr}}$:

$$
p_{\text{corr}} = a_1 p_{\text{med}} + a_2 p_{\text{med}}^2 + a_3 p_{\text{med}}^3 + \dots = \sum_{n=1}^{N} a_n p_{\text{med}}^n
$$

Onde os coeficientes $\left\{ a_1, a_2, \dots, a_N \right\}$ são determinados por meio de calibração utilizando cilindros de referência (como água ou polímeros acrílicos) de diâmetros conhecidos.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

O controle e a correção do *beam-hardening* são fundamentais na metrologia radiológica e na garantia da qualidade em Tomografia Computadorizada:

* **Correção Pré-Reconstrução (Linearização de Sinograma):** A técnica clássica desenvolvida por Herman e tutoriais subsequentes consiste em aplicar polinômios de correção diretamente sobre os dados do sinograma antes de submetê-los à filtragem e retroprojeção. Isso restaura a consistência matemática dos dados projetados.
* **Correções baseadas em Segmentação (Dual-Pass / Split-Water Correction):** Em tomografia de crânio, o feixe é corrigido assumindo um componente primário de água e um componente ósseo separado. O algoritmo segmenta preliminarmente o osso, calcula o endurecimento teórico esperado e subtrai o artefato projetado.
* **Tomografia Computadorizada de Dupla Energia (DECT - *Dual-Energy CT*):** Representa a abordagem física definitiva para a eliminação do *beam-hardening*. Ao adquirir dados com dois espectros de raios X distintos (por exemplo, com tensões de tubo de $80\text{ kVp}$ e $140\text{ kVp}$, ou com filtragem rápida em fontes de alta rotação), o sistema pode resolver matematicamente a decomposição material em termos de duas bases (como Água e Iodo, ou Osso e Tecido Mole), eliminando completamente a dependência do espectro policromático e gerando imagens quantitativas precisas (mapas de número atômico e densidade eletrônica).
* **Impacto em Inteligência Artificial e Reconstrução Iterativa (IR/DLR):** Redes Neurais Profundas (*Deep Learning Reconstruction*) treinadas para redução de artefatos de *beam-hardening* operam tanto no domínio do sinograma quanto no domínio da imagem. Modelos baseados em aprendizado profundo conseguem mitigar artefatos severos causados por próteses metálicas, onde o endurecimento extremo do feixe é acompanhado por perda total de fótons (*photon starvation*), superando métodos analíticos tradicionais.

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|tomografia-computadorizada]]
- [[espectro-de-raios-x]]
- [[lei-de-beer-lambert]]
- [[Artefatos em TC|artefatos-em-tc]]
- [[retroprojetor-filtrado-fbp]]
- [[Tomografia Computadorizada Espectral|tomografia-de-dupla-energia]]
- [[Unidades Hounsfield|numero-de-hounsfield]]
- [[reconstrucao-por-aprendizado-profundo]]
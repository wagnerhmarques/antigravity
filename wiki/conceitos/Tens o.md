---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, radiologia-diagnostica, qualidade-da-imagem\, dosimetria, instrumentacao]
data: 2026-08-25
---

# tensão

## 1. Definição Conceitual e Fundamentação Física / Metrológica

No contexto da Física Médica e da Tomografia Computadorizada (TC), o termo **tensão** refere-se especificamente à diferença de potencial elétrico aplicada entre o cátodo e o ânodo (alvo) do tubo de raios-X, comumente denotada por $kVp$ (*Kilovoltage Peak* — Pico de Kilovoltagem). Trata-se de um dos parâmetros eletrotécnicos mais fundamentais no controle da qualidade do feixe de radiação X, pois determina diretamente a energia cinética máxima dos elétrons acelerados no vácuo do tubo.

Do ponto de vista físico e metrológico, a tensão aplicada dita a severidade da interação dos elétrons com o material do ânodo (geralmente tungstênio, $Z = 74$). Quando os elétrons de alta energia colidem com o alvo, sua desaceleração súbita resulta na emissão de radiação de frenagem (*Bremsstrahlung*), formando um espectro contínuo de fótons cujas energias variam desde zero até o valor máximo correspondente à tensão de pico aplicada em quilovolts ($keV$). Além disso, a energia limiar para a excitação de camadas internas (como a camada $K$ do tungstênio, com energia de ligação de aprox. $69.5\text{ keV}$) depende estritamente de que a tensão do tubo ultrapasse esse limiar, permitindo a superposição de raios-X característicos ao espectro contínuo.

Metrologicamente, a aferição da tensão do tubo é crítica para a garantia da qualidade (CQ) em equipamentos de TC. Variações na tensão nominal versus a tensão efetivamente entregue impactam diretamente a penetrabilidade do feixe, o coeficiente de atenuação linear efetivo dos tecidos escaneados e, por conseguinte, a exatidão dos números de Tomografia Computadorizada (unidades Hounsfield - HU).

## 2. Formulação Matemática e Propriedades (se aplicável)

A energia cinética máxima ($E_{\max}$) adquirida por um elétron acelerado no campo eletrostático do tubo de raios-X é diretamente proporcional à tensão de pico aplicada ($V$ ou $kVp$), expressa por:

$$
E_{\max} = e \cdot V
$$

onde:
- $e$ é a carga elementar do elétron ($1.602 \times 10^{-19}\text{ C}$).
- $V$ é a diferença de potencial elétrico aplicada em volts ($\text{V}$).

O espectro de energia dos fótons de raios-X gerados, $\Phi(E)$, em função da energia do fóton $E$, pode ser modelado de forma simplificada pela lei de Kramers para o *Bremsstrahlung*:

$$
\Phi(E) = C \cdot Z \cdot \left( \frac{E_{\max} - E}{E} \right)
$$

onde:
- $C$ é uma constante de proporcionalidade.
- $Z$ é o número atômico do material do ânodo.
- $E$ é a energia do fóton gerado ($0 \le E \le E_{\max}$).

A intensidade total ou o rendimento energético ($I$) do feixe de raios-X gerado é proporcional ao quadrado da tensão e à corrente do tubo ($I_t$, em miliampères - mA):

$$
I \propto Z \cdot I_t \cdot V^2
$$

No tocante à atenuação da radiação através de um meio homogêneo de espessura $x$, a intensidade do feixe transmitido $I(x)$ depende da energia média do feixe, a qual é modulada pela tensão escolhida:

$$
I(x) = I_0 \cdot \int_{0}^{E_{\max}} \Phi(E) \cdot e^{-\mu(E) \cdot x} \, dE
$$

onde $\mu(E)$ representa o coeficiente de atenuação linear dependente da energia para o tecido biológico em questão.

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A escolha da tensão ($kVp$) em tomografia computadorizada afeta profundamente o balanço entre a qualidade da imagem (relação sinal-ruído - RSR, artefatos) e a dose absorvida pelo paciente. Suas principais aplicações e frentes de otimização incluem:

*   **Contraste e Número Hounsfield (HU):** Reduzir a tensão (ex: de $120\text{ kVp}$ para $70\text{ ou }80\text{ kVp}$) aumenta o coeficiente de atenuação fotoelétrica, especialmente em estruturas com elementos de maior número atômico ou em exames contrastados com iodo ou gadolínio. Isso eleva marcadamente o contraste iodado e a conspicuidade de lesões vasculares ou parenquimatosas.
*   **Otimização de Dose e Ruído Quântico:** Como a produção de fótons escala quadraticamente com a tensão, reduções no $kVp$ exigem compensações na corrente ($mA$) ou no produto corrente-tempo ($mAs$) para manter o ruído quântico aceitável. Protocolos de $kVp$ baixo (*Low-kVp imaging*) são cruciais na otimização de dose pediátrica e em exames angiotomográficos.
*   **Correção de Endurecimento do Feixe (*Beam Hardening*):** Espectros gerados a menores tensões são mais policromáticos e propensos a artefatos de endurecimento do feixe se não forem rigorosamente corrigidos por algoritmos de pré-processamento e filtragem de bancada (como filtros de alumínio/cobre adicionais).
*   **Sistemas Avançados de Reconstrução:** Algoritmos modernos de Reconstrução Iterativa (IR) e Reconstrução Baseada em Aprendizado Profundo (*Deep Learning Reconstruction* - DLR) permitem mitigar o aumento de ruído associado a varreduras com tensões reduzidas, viabilizando exames de alta diagnosticabilidade em doses sub-milsievert.

## 4. Conexões e Wikilinks

*   [[Tomografia Computadorizada|tomografia-computadorizada]]
*   [[Modulação de Corrente de Tubo (TCM)|corrente]]
*   [[Qualidade de Imagem em TC|qualidade-da-imagem]]
*   [[Dosimetria]]
*   [[espectro-de-raios-x]]
*   [[Unidades Hounsfield|unidades-hounsfield]]
*   [[Reconstrução Iterativa|reconstrucao-iterativa]]
*   [[Machine Learning|aprendizado-profundo]]
---
tipo: conceito
tags: [fisica-medica, radiobiologia, modelo-linear-quadratico, protecao-radiologica, dosimetria, inteligencia-artificial]
data: 2026-08-25
---

# Radiobiologia e Modelo Linear-Quadrático

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A radiobiologia estuda os efeitos das radiações ionizantes nos sistemas biológicos, abrangendo desde o nível molecular e celular até tecidos e organismos inteiros. No contexto da física médica e da proteção radiológica — com especial relevância para procedimentos de alta dose como a tomografia computadorizada (TC) intervencionista e helicoidal avançada —, a compreensão quantitativa da sobrevivência celular após a irradiação é fundamental para avaliar riscos estocásticos (como indução de câncer) e otimizar protocolos clínicos.

O **Modelo Linear-Quadrático (LQ)** é o formalismo radiobiológico padrão de ouro para descrever a curva de sobrevivência celular em função da dose absorvida. O modelo fundamenta-se na premissa de que o dano letal ao DNA (principalmente quebras bicatenárias — *double-strand breaks*, DSBs) pode ocorrer por dois mecanismos distintos de ação das trilhas de radiação:

1. **Mecanismo Linear ($\alpha$):** O dano letal é causado por uma única trilha de radiação (ou um único evento de ionização/excitação) que atravessa o alvo crítico (o núcleo celular/DNA), induzindo uma lesão irreparável ou de difícil reparo de forma direta. A probabilidade de ocorrência é proporcional à dose ($D$).
2. **Mecanismo Quadrático ($\beta$):** O dano letal resulta da interação cumulativa de dois eventos independentes causados por duas trilhas de radiação distintas (ou duas sub-lesões que, quando combinadas, tornam-se letais). A probabilidade de ocorrência é proporcional ao quadrado da dose ($D^2$).

Metrologicamente, os parâmetros $\alpha$ e $\beta$ descrevem a radiosensibilidade intrínseca de uma linhagem celular ou tecido, sendo expressos em $\text{Gy}^{-1}$ e $\text{Gy}^{-2}$, respectivamente.

---

## 2. Formulação Matemática e Propriedades

A fração de sobrevivência celular ($SF$ - *Surviving Fraction*), definida como a razão entre o número de células clonogênicas viáveis após a irradiação e o número inicial de células, é expressa no Modelo Linear-Quadrático pela seguinte equação:

$$
SF = \exp\left( -\alpha D - \beta D^2 \right)
$$

Onde:
* $SF$ é a fração de sobrevivência adimensional ($0 < SF \le 1$).
* $D$ é a dose absorvida, medida em Gray ($\text{Gy}$).
* $\alpha$ é o coeficiente linear ($\text{Gy}^{-1}$), representando o componente de dano letal único.
* $\beta$ é o coeficiente quadrático ($\text{Gy}^{-2}$), representando o componente de dano letal acumulativo.

### Propriedades Analíticas e Derivadas

1. **Taxa de Inclusão do Dano:** O logaritmo natural negativo da fração de sobrevivência ($\ln(SF)$) exibe uma dependência polinomial de segunda ordem com a dose:
   
   
$$
-\ln(SF) = \alpha D + \beta D^2
$$

2. **Razão $\alpha/\beta$:** Um parâmetro clínico-biológico crucial derivado do modelo é a razão $\alpha/\beta$ (medida em $\text{Gy}$). Ela representa o nível de dose no qual o componente linear de morte celular iguala-se ao componente quadrático:

   
$$
\alpha D = \beta D^2 \implies D = \frac{\alpha}{\beta}
$$

   * **Tecidos com alta razão $\alpha/\beta$ ($\approx 10\text{ Gy}$):** Tecidos de resposta aguda (tumores, tecidos com alta taxa de renovação celular). Suas curvas de sobrevivência são mais inclinadas, exibindo menor curvatura em doses baixas.
  * **Tecidos com baixa razão $\alpha/\beta$ ($\approx 2 \text{ a } 3\text{ Gy}$):** Tecidos de resposta tardia (órgãos de risco normais, medula espinhal, tecido nervoso). Suas curvas exibem maior curvatura, indicando maior capacidade de reparo celular em doses fracionadas.

3. **Dose Efetiva Biológica (BED - *Biologically Effective Dose*):** Para contabilizar o fracionamento de dose ou taxas de dose variáveis (comum em radioterapia, mas conceitualmente aplicável à avaliação de risco cumulativo em exames seriados de TC), o conceito de BED é formulado como:

   
$$
\text{BED} = D \left( 1 + \frac{d}{\alpha/\beta} \right) = nd \left( 1 + \frac{d}{\alpha/\beta} \right)
$$

   Onde $n$ é o número defrações e $d$ é a dose por fração.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Embora o Modelo Linear-Quadrático tenha nascido no contexto da radio-oncologia, sua aplicação na **Tomografia Computadorizada (TC)** e na física de imagem diagnóstica reveste-se de grande importância nas seguintes frentes:

* **Avaliação de Risco Estocástico (Radioproteção):** O risco de indução de neoplasias secundárias decorrentes de exames diagnósticos de alta dose (como TC perfusão cerebral, exames cardíacos multipásicos e protocolos oncológicos de corpo inteiro) é modelado utilizando o formalismo linear a baixas doses. Como a dose de uma TC típica ($10\text{ mGy} \text{ a } 50\text{ mGy}$) situa-se na região de baixa dose da curva de sobrevivência, o termo quadrático ($\beta D^2$) torna-se quase desprezível, justificando a adoção do modelo linear simples (LNT - *Linear No-Threshold*) para estimativa de risco populacional.
* **Otimização de Protocolos via Inteligência Artificial:** Algoritmos modernos de Reconstrução Iterativa Profunda (DLR - *Deep Learning Reconstruction*) e Redes Neurais para Redução de Ruído permitem reduzir drasticamente a corrente do tubo ($mA$) e, consequentemente, a dose ($CTDIvol$ e $DLP$). A radiobiologia computacional fornece o arcabouço matemático para simular o balanço entre a perda de qualidade de imagem (ruído quântico e artefatos) e a preservação do diagnóstico clínico versus o decréscimo do dano radiobiológico ao paciente.
* **Dosimetria de Órgãos e Simulações Monte Carlo:** Cálculos avançados de dose em órgãos utilizando simulações de Monte Carlo (como *Geant4* ou *MCNP*) integradas a fantomas antropomórficos computacionais (voxelizados e NURBS) fornecem mapas tridimensionais de dose. Ao aplicar o modelo LQ com mapas de sensibilidade tecidual ($\alpha$ e $\beta$ específicos de órgãos), torna-se possível estimar a probabilidade de complicações em tecidos normais (NTCP - *Normal Tissue Complication Probability*) mesmo em cenários complexos de irradiação diagnóstica.

---

## 4. Conexões e Wikilinks

* [[Dosimetria em Radiologia|Dosimetria em Tomografia Computadorizada]]
* [[CTDI e DLP]]
* [[Filtros de Reconstrução e Reconstrução Iterativa]]
* [[Inteligencia Artificial IA|Inteligência Artificial em Tomografia Computadorizada]]
* [[Proteção Radiológica e Princípio ALARA]]
* [[Efeitos Biológicos das Radiações Ionizantes]]
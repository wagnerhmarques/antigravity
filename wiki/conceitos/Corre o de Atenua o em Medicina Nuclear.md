---
tipo: conceito
tags: [fisica-medica, medicina-nuclear, pet-ct, spect-ct, tomografia-computadorizada, reconstrucao-de-imagem]
data: 2026-08-25
---

# Correção de Atenuação em Medicina Nuclear

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Correção de Atenuação (AC)** em Medicina Nuclear é um processo computacional e físico indispensável para quantificar com precisão a distribuição espacial de radiofármacos em exames de Tomografia por Emissão de Pósitrons (PET) e Tomografia por Emissão de Fóton Único (SPECT). 

Fisicamente, os fótons gama emitidos pelos radionuclídeos no interior do paciente (por exemplo, fótons de $511\text{ keV}$ na aniquilação $e^+ - e^-$ no PET ou os fótons de $140\text{ keV}$ do $^{99m}\text{Tc}$ no SPECT) sofrem interações com a matéria ao longo de sua trajetória até os detectores externos. Os principais mecanismos de atenuação são o **Efeito Fotoelétrico** (dominante em energias mais baixas, como no SPECT) e o **Espalhamento Compton** (dominante na faixa de energia do PET). 

Devido à atenuação exponencial descrita pela Lei de Beer-Lambert, uma porcentagem significativa dos fótons emitidos é absorvida ou desviada antes de atingir os detectores. Sem a correção adequada, as regiões centrais do corpo humano (como o mediastino ou o abdome) parecerão artificialmente hipoativas em comparação às regiões periféricas, gerando artefatos graves de heterogeneidade, subestimação de atividade tumoral e potenciais erros de diagnóstico em oncologia, cardiologia e neurologia.

Metrologicamente, a AC converte dados de contagem puramente qualitativos em mapas quantitativos de atividade em unidades padronizadas, como o *Standardized Uptake Value* (SUV), permitindo a comparabilidade longitudinal de exames e a dosimetria interna individualizada para terapias com radionuclídeos.

---

## 2. Formulação Matemática e Propriedades

### A. Atenuação no SPECT
No SPECT, o fóton emitido a partir de um ponto $\mathbf{r}$ dentro de um meio com coeficiente de atenuação linear $\mu(\mathbf{r}, E)$ viaja em direção a um detector. A probabilidade de sobrevivência do fóton (ou seja, de não sofrer interação ao longo do trajeto L até o detector) é dada por:

$$
P(\mathbf{r}, \theta) = \exp\left( -\int_{L} \mu(\mathbf{l}) \, dl \right)
$$

O projeção medida $p_{\theta}(s)$ ao longo de uma linha de resposta (LoR) parametrizada pelo ângulo $\theta$ e distância $s$ é a integral da atividade radioativa $f(\mathbf{r})$ ponderada por este fator de atenuação:

$$
p_{\theta}(s) = \int_{-\infty}^{\infty} f(\mathbf{r}) \delta(x \cos\theta + y \sin\theta - s) \exp\left( -\int_{(x,y)}^{(\infty)} \mu(x', y') \, dl' \right) dx\, dy
$$

### B. Atenuação no PET
No PET, a detecção baseia-se na coincidência de dois fótons colineares ($180^\circ \pm \approx 0.25^\circ$) gerados na aniquilação de um pósitron. Surpreendentemente, a probabilidade total de detecção do par de fótons que atravessa o corpo ao longo de uma corda inteira (LoR) depende **apenas da espessura total do tecido atravessado**, independentemente do local exato da aniquilação ao longo da linha.

Seja um par de fótons emitidos em um ponto $\mathbf{r}$ sobre uma LoR que conecta os detectores $A$ e $B$. A probabilidade de o par alcançar o anel de detecção sem atenuação é:

$$
P_{AB} = \exp\left( -\int_{A}^{B} \mu(\mathbf{l}) \, dl \right)
$$

Portanto, o fator de correção de atenuação ($ACF$) para uma dada LoR é o inverso dessa probabilidade:

$$
ACF_{AB} = \exp\left( \int_{A}^{B} \mu(\mathbf{l}) \, dl \right)
$$

### C. Mapas de Atenuação Baseados em Tomografia Computadorizada (CT-AC)
Para calcular o integral de linha de $\mu$, o sistema moderno híbrido (PET/CT ou SPECT/CT) utiliza um mapa de atenuação derivado da imagem de Tomografia Computadorizada. Como a CT opera em energias de raios X (espectro polichromático centrado tipicamente entre $80$ e $140\text{ kVp}$), enquanto o PET opera em $511\text{ keV}$, é necessária uma transformação matemática (escala bilinear de conversão) para mapear os números Hounsfield (HU) medidos na CT para os coeficientes de atenuação lineares $\mu$ na energia de interesse do radionuclídeo:

$$
\mu(E) = \begin{cases} 
\mu_{\text{água}}(E) \left[ 1 + \frac{HU}{1000} \right], & \text{se } HU \le 0 \\
\mu_{\text{água}}(E) + \frac{HU}{1000} \left[ \mu_{\text{osso}}(E) - \mu_{\text{água}}(E) \right], & \text{se } HU > 0 
\end{cases}
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A sinergia entre a Tomografia Computadorizada (CT) e a Medicina Nuclear revolucionou a acurácia diagnóstica através dos sistemas híbridos SPECT/CT e PET/CT. A CT não serve apenas para localização anatômica, mas constitui a base física fundamental para a geração dos mapas de atenuação de alta resolução espacial e baixo ruído.

### Otimização e Desafios Tecnológicos
1. **Truncamento de Imagem:** Quando o campo de visão (FoV) transaxial da CT é menor que o do paciente (comum em pacientes obesos ou braços posicionados ao lado do corpo), ocorre truncamento do mapa de atenuação. Algoritmos de extrapolação e preenchimento de contorno são necessários para evitar artefatos de "anel" ou superestimação de atividade nas bordas.
2. **Artefatos Metálicos:** Próteses ortopédicas ou materiais de contraste iodado de alta densidade geram extremos nos números Hounsfield na CT. Na conversão para $\mu$, esses valores causam artefatos severos de "streak" (raias) e sub/supercorreção na imagem de emissão molecular. Técnicas de interpolação e algoritmos de *Deep Learning* para correção de artefatos metálicos (MAR) na CT são cruciais antes da aplicação do AC.
3. **Erros de Incompatibilidade Temporal (*Misregistration*):** Movimentos respiratórios ou cardíacos entre a aquisição da CT e do PET/SPECT geram desalinhamentos espaciais entre o mapa de atenuação e os dados funcionais. Isso resulta em artefatos de falso positivo (ex: aparente captação no diafragma ou bordas pulmonares). Otimizações envolvem varreduras de CT em respiração livre com média temporal, gating respiratório (*4D-PET/CT*) e algoritmos de registro de imagem baseados em deformação elástica.
4. **Reconstrução Iterativa (OSEM / MAP):** A incorporação rigorosa do operador de atenuação nos algoritmos de reconstrução iterativa (como *Ordered Subset Expectation Maximization*) garante a convergência rápida para a distribuição real de radiofármaco, preservando a resolução quantitativa sem amplificar excessivamente o ruído estatístico.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[Tomografia por Emissão de Pósitrons (PET)|PET-CT]]
* [[SPECT-CT]]
* [[Reconstrucao de Imagem Iterativa]]
* [[Filtro de Retroprojetcao FBP|Filtro de Retroprojetcao (FBP)]]
* [[Numeros Hounsfield]]
* [[Efeito Compton e Efeito Fotoeletrico]]
* [[Dosimetria Interna]]
* [[Artefatos em Tomografia Computadorizada]]
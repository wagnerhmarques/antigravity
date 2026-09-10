---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, geometria-do-feixe, dosimetria, qualidade-de-imagem]
data: 2026-08-25
---

# Filtro Borboleta e Geometria do Feixe

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **filtro borboleta** (*bow-tie filter*, frequentemente traduzido como filtro gravata-borboleta) é um componente físico de atenuação diferencial posicionado na saída do tubo de raios-X, imediatamente após a colimação primária, em sistemas de Tomografia Computadorizada (TC). Sua função primária é modular a distribuição espacial da intensidade e do espectro de energia do feixe de raios-X policromático antes que este atravesse o paciente.

Geometricamente, o corpo humano apresenta uma seção transversal tipicamente ovalada ou elíptica, sendo mais espessa na região central e progressivamente mais delgada nas periferias (ombros, cabeça, membros). Se um feixe de raios-X de intensidade homogênea (*flat beam*) fosse emitido em direção ao paciente, a radiação transmitida que atinge os detectores centrais seria severamente atenuada em comparação à radiação que atinge os detectores periféricos. Isso resultaria em:
1. **Dinâmica de sinal excessiva** nos canais do detector, excedendo a capacidade de conversão analógica-digital (ADC) ou introduzindo ruído quântico severo no centro devido à escassez de fótons detectados.
2. **Dose desnecessária** depositada nos tecidos periféricos delgados, que exigem muito menos fótons para atingir a mesma relação sinal-ruído (SNR) estatística que o centro denso.

O filtro borboleta possui uma geometria tridimensional côncava (mais espesso nas extremidades laterais e mais delgado no centro, assemelhando-se ao perfil de uma gravata-borboleta). Ao atenuar seletivamente os fótons destinados às regiões periféricas do paciente, o filtro equaliza a carga de radiação transmitida que chega à coroa de detecção. 

Do ponto de vista metrológico, o filtro borboleta otimiza a eficiência de contagem de fótons, reduz o espalhamento Compton gerado por radiação excedente nas bordas, padroniza a variação estatística (ruído) em todo o campo de visão (*Field of View* - FOV) e atua como um elemento de endurecimento do feixe (*beam hardening*), filtrando componentes de baixa energia que seriam absorvidas superficialmente.

---

## 2. Formulação Matemática e Propriedades

Para modelar matematicamente a ação do filtro borboleta, consideremos a intensidade do feixe de raios-X incidente e o perfil de atenuação espacial. Seja $\Phi_0(E)$ o fluxo de fótons incidentes por unidade de energia e área antes do filtro, e $\mu_f(E)$ o coeficiente de atenuação linear do material do filtro (tipicamente alumínio, teflon ou latão).

A espessura do filtro borboleta varia em função do ângulo de projeção ou posição transversal $\xi$ do raio no leque (*fan-beam*). Denotamos por $T_f(\xi)$ a função de espessura do filtro. O feixe emergente do filtro, $\Phi_{out}(\xi, E)$, é dado por:

$$
\Phi_{out}(\xi, E) = \Phi_0(E) \exp \left( -\mu_f(E) T_f(\xi) \right)
$$

Considerando a geometria do feixe em leque, a intensidade integrada sobre o espectro de energia para um raio específico no ângulo $\xi$ é:

$$
I(\xi) = \int_{0}^{E_{\max}} \Phi_0(E) \exp \left( -\mu_f(E) T_f(\xi) \right) dE
$$

O objetivo ideal do projeto do filtro borboleta é encontrar uma função de perfil de espessura $T_f(\xi)$ tal que, ao atravessar um phantom cilíndrico ou elíptico de raio equivalente $R(\xi)$ e coeficiente médio $\mu_{obj}(E)$, a intensidade total que atinge o detector $I_{\det}(\xi)$ seja aproximadamente constante ou varie suavemente de acordo com a predição algorítmica:

$$
I_{\det}(\xi) = I(\xi) \exp \left( - \int_{-R(\xi)}^{R(\xi)} \mu_{obj}(s, E) ds \right) \approx \text{constante}
$$

Como os scanners modernos operam com diferentes protocolos clínicos (ex: crânio versus abdômen), a geometria do feixe e a atenuação exigida mudam drasticamente. Por essa razão, os sistemas multidetectores (MDCT) utilizam múltiplos filtros borboleta intercambiáveis montados em um tambor motorizado, selecionados automaticamente com base no *bow-tie category* (Head, Body Small, Body Large, Cardiovascular).

A atenuação diferencial introduzida afeta diretamente o valor numérico dos coeficientes de atenuação linear reconstruídos na imagem mapeada em unidades Hounsfield (HU), exigindo correções rigorosas no pré-processamento de calibração do ganho dos canais do detector ($C_i$).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

### Controle de Qualidade e Dosimetria
O filtro borboleta é um parâmetro crítico no cálculo e medição de dose em tomografia. Métodos dosimétricos como o cálculo do **CTDI** (*Computed Tomography Dose Index*) consideram intrinsecamente a presença do filtro borboleta associado ao feixe clínico. A remoção incorreta ou falha mecânica no posicionamento do filtro borboleta resulta em overdoses catastróficas na pele e tecidos superficiais do paciente, além de saturação severa dos detectores.

### Reconstrução de Imagem e Algoritmos Iterativos
Nos algoritmos de retroprojeção filtrada (FBP) tradicionais, assume-se que o ruído estatístico é uniformemente distribuído ou que a correção de log-transformação ($\ln(I_0/I)$) lineariza perfeitamente o problema. Como o filtro borboleta reduz drasticamente o número de fótons nas bordas do FOV, o ruído quântico nessas regiões tendeu a ser amplificado. 

Em técnicas modernas de reconstrução iterativa (IR) e reconstrução baseada em aprendizado profundo (*Deep Learning Reconstruction* - DLR), o conhecimento exato da matriz de modelagem do sistema (*System Matrix*), que inclui a função de transmissão espacial do filtro borboleta, permite a ponderação estatística correta (máxima verossimilhança ponderada por ruído - * penalized weighted least squares*). Isso evita artefatos de anel (*ring artifacts*) e mantém a resolução espacial uniforme independentemente da distância ao isocentro.

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|Tomografia Computadorizada]]
- [[Física do Raio-X e Interação com a Matéria]]
- [[Endurecimento do Feixe e Correções]]
- [[Reconstrução de Imagem (FBP, Iterativa e DLR)]]
- [[Dosimetria em Radiologia e CTDI]]
- [[Qualidade de Imagem e Ruído Quântico]]
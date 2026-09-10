---
tipo: conceito
aliases: [Radioprotecao]
tags: [fisica-medica, tomografia-computadorizada]
data: 2026-08-25
---

# Radioprotecao

## 1. Definição Conceitual e Fundamentação Física
A **Radioproteção** em Tomografia Computadorizada (TC) constitui o conjunto de medidas científicas, técnicas e administrativas destinadas a proteger os pacientes, os profissionais ocupacionalmente expostos (POEs) e o público contra os efeitos deletérios da radiação ionizante, sem comprometer o benefício clínico diagnóstico inerente ao procedimento. Fundamenta-se nos três pilares fundamentais estabelecidos pela Comissão Internacional de Proteção Radiológica (ICRP): **Justificação**, **Otimização** e **Limitação de Dose**. 

Na física médica aplicada à TC, a otimização atinge seu grau máximo através da aplicação rigorosa do princípio **ALARA** (*As Low As Reasonably Achievable*), balanceando a qualidade de imagem necessária para a acurácia diagnóstica com a menor energia depositada nos tecidos biológicos. A interação da radiação X com a matéria biológica ocorre predominantemente por efeito Compton e efeito fotoelétrico, resultando em ionizações que podem induzir danos diretos ou indiretos (via espécies reativas de oxigênio) ao DNA celular, cujas consequências estocásticas (como indução de neoplasias) exigem rigoroso controle quantitativo da dose absorvida e da dose efetiva.

## 2. Formulação Matemática e Propriedades
A quantificação e a gestão da radioproteção em TC exigem o uso de grandezas dosimetrias padronizadas. A energia depositada por unidade de massa é a **Dose Absorvida ($D$)**:

$$
D = \frac{d\epsilon}{dm}
$$

Onde $d\epsilon$ é a energia média impartida pela radiação ionizante a um material de massa $dm$. 

Para avaliar o risco biológico estocástico em tecidos e órgãos específicos, utiliza-se a **Dose Equivalente ($H_T$)**, que pondera a dose absorvida pelo fator de peso da radiação ($w_R$, que para raios X e gama é igual a 1):

$$
H_T = \sum_{R} w_R D_{T,R}
$$

A extensão do dano estocástico a corpo inteiro é quantificada pela **Dose Efetiva ($E$)**, expressa em Sieverts (Sv), que incorpora os fatores de ponderação tecidual ($w_T$) recomendados pela ICRP:

$$
E = \sum_{T} w_T H_T = \sum_{T} w_T \sum_{R} w_R D_{T,R}
$$

No contexto específico da tomografia computadorizada, a métrica fundamental de saída do equipamento é o **Índice de Dose da Tomografia Computadorizada ($CTDI$)**, tipicamente medido em câmaras de ionização de lápis de $100\text{ mm}$ em fantomas acrílicos normalizados ($CTDI_{100}$):

$$
CTDI_{100} = \int_{-50\text{ mm}}^{+50\text{ mm}} \frac{D(z)}{N \cdot T} dz
$$

Onde $N$ é o número de tomografias por rotação e $T$ é a espessura do corte nominal. Para contabilizar a variação da dose ao longo do eixo longitudinal ($z$) em varreduras helicoidais\, define-se o $CTDI_{w}$ (ponderado) e o $CTDI_{vol}$:

$$
CTDI_{vol} = \frac{CTDI_{w}}{\text{pitch}}
$$

Por fim, a carga global de radiação entregue ao paciente ao longo de todo o comprimento varrido ($L$) é expressa pelo **Produto Dose-Comprimento ($DLP$)**:

$$
DLP = CTDI_{vol} \times L
$$

A correlação entre o $DLP$ e a dose efetiva ($E$) é estabelecida por coeficientes de conversão específicos por região anatômica ($k$):

$$
E = DLP \times k
$$

## 3. Contexto no Acervo do Pesquisador & Aplicações
No acervo de pesquisa do laboratório USP/FAPESP, a **Radioprotecao** atua como o eixo transversal que une a física de aquisição de imagem e o diagnóstico avançado. Ela não é tratada de forma isolada, mas como restrição de contorno e objetivo otimização em múltiplos frentes tecnológicas:

1. **Relação com DRL (Níveis de Referência Diagnósticos):** Conforme documentado em [[Níveis de Referência Diagnóstica (DRL)|drl]], a radioproteção orienta a definição dos limiares aceitáveis de dose para exames padronizados, servindo como benchmark para mitigar a variabilidade injustificada de dose entre diferentes centros clínicos.
2. **Sinergia com Algoritmos Avançados e IA:** A busca constante pela radioproteção impulsiona o desenvolvimento de técnicas de [[Reconstrução Iterativa|Reconstrucao Iterativa]] e abordagens baseadas em **Deep Learning Reconstruction (DLR)**, permitindo a manutenção da detectabilidade de baixo contraste mesmo sob reduções drásticas de corrente no tubo (mAs), conforme apontado em [[Radioproteção|alara]].
3. **Garantia de Qualidade:** A eficácia da radioproteção depende criticamente da integridade dos sistemas de imageamento, exigindo protocolos rigorosos de [[Controle de Qualidade em TC]] para assegurar que os parâmetros de kilovoltagem ($kVp$), miliamperagem ($mA$) e filtragem estejam perfeitamente calibrados.

## 4. Conexões e Wikilinks
* [[Radioproteção|alara]]
* [[Níveis de Referência Diagnóstica (DRL)|drl]]
* [[Efeitos Biologicos da Radiação|Efeitos Biologicos da Radiacao]]
* [[Controle de Qualidade em TC]]
* [[Métricas de Dose em TC|CTDI]]
* [[Métricas de Dose em TC|DLP]]
* [[Reconstrução Iterativa|Reconstrucao Iterativa]]
* [[Fisica Medica]]
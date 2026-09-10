---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, observadores-modelados, npwe, modelagem-linear, qualidade-de-imagem]
data: 2026-08-25
---

# NPWE_assume_modelagem_linear

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O termo **NPWE_assume_modelagem_linear** refere-se à premissa fundamental inerente ao observador modelo *Non-Prewhitening Matched Filter with Eye Filter* (NPWE) de que a tarefa de detecção de sinal e a formação de imagem no sistema de Tomografia Computadorizada (TC) operam sob o regime de **linearidade** (e, frequentemente\, de Invariância Espacial Local, ou LSIS). 

No contexto da Física Médica e da avaliação de qualidade de imagem baseada em tarefas (*task-based image quality*), o observador NPWE é amplamente utilizado para predizer o desempenho de observadores humanos na detecção de lesões de baixo contraste (como nódulos pulmonares incipientes ou metástases hepáticas). A hipótese de modelagem linear estabelece que:
1. O sistema de imagem (incluindo aquisição, filtragem, retroprojeção ou reconstrução iterativa linearizada) satisfaz o princípio da superposição.
2. A resposta do sistema a um sinal de entrada (a lesão acrescida ao fundo anatômico ou ruído) é diretamente proporcional à amplitude do sinal.
3. As flutuações estocásticas do ruído quântico e eletrônico, bem como a degradação espacial imposta pela função de dispersão do ponto (PSF), podem ser tratadas através de operações lineares em espaços de Fourier ou de matrizes de covariância lineares.

Embora os algoritmos modernos de reconstrução em TC — como a Reconstrução Iterativa (IR) e a Reconstrução Baseada em Aprendizado Profundo (DLR) — introduzam fortes não-linearidades (por exemplo, limiares de limitação de arestas, penalidades de regularização baseadas em norma $L_1$ e redes neurais profundas), a aplicação do NPWE frequentemente assume uma aproximação linearizada local (através de *Local Impulse Responses* - LIR) para manter a tractabilidade matemática na premissa de que o observador humano responde linearmente a variações sutilíssimas de contraste perto de um ponto de operação.

---

## 2. Formulação Matemática e Propriedades

Matematicamente, a premissa de modelagem linear permite expressar a imagem reconstruída $\hat{f}(x)$ como a aplicação de um operador linear sobre o objeto original $f(x)$ somado ao ruído estocástico $n(x)$:

$$
\hat{f}(x) = \mathcal{H} * f(x) + n(x)
$$

Onde $\mathcal{H}$ representa a resposta impulsiva espacialmente variante do sistema de TC. Sob a hipótese de linearidade, o sinal esperado da lesão na imagem\, denotado por $s(x)$, é independentemente somado ao fundo estocástico $b(x)$ e ao ruído $n(x)$.

O observador modelo NPWE calcula uma estatística de decisão $t$ baseada na correlação cruzada entre o sinal template esperado e a imagem sob teste, modificada pela função de sensibilidade visual humana (filtro ocular $W$):

$$
t = \iint W(u, v) \, S^*(u, v) \, \left[ \hat{F}_{s+n}(u, v) - \hat{F}_n(u, v) \right] \, du \, dv
$$

Onde:
- $(u, v)$ são as coordenadas no domínio da frequência espacial.
- $S(u, v)$ é a transformada de Fourier do sinal determinístico da lesão (cuja linearidade garante que $S(u, v) = \mathcal{F}\{\mathcal{H} * s\}$).
- $W(u, v)$ é a função de transferência do filtro ocular (tipicamente modelada empiricamente, como a função de Mann-Ginsburg).
- $\hat{F}_{s+n}$ e $\mathcal{F}_n$ representam as transformadas de Fourier das imagens com sinal+ruído e apenas ruído, respectivamente.

A métrica de desempenho fundamental do NPWE é a detectabilidade mensurada pelo Índice de Detectabilidade ($d'$):

$$
(d')^2 = \frac{\left[ \iint W(u, v) |S(u, v)|^2 \, du \, dv \right]^2}{\iint W^2(u, v) |S(u, v)|^2 W_{nn}(u, v) \, du \, dv}
$$

Onde $W_{nn}(u, v)$ é o Espectro de Potência de Wiener (NPS - *Noise Power Spectrum*) do fundo ruidoso. A validade estrita dessa formulação analítica do $d'$ depende diretamente da **linearidade** do sistema de imagem, pois garante que o NPS ($W_{nn}$) e a função de transferência de modulação (MTF, contida em $S$) sejam independentes da magnitude do sinal de fundo e aditivos.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Em tomografia computadorizada contemporânea, a suposição de modelagem linear pelo NPWE desempenha papéis críticos:

- **Controle de Qualidade Baseado em Tarefas:** Permite substituir testes subjetivos com observadores humanos por métricas computacionais rápidas e reprodutíveis para avaliar protocolos de dose e qualidade de imagem.
- **Validação de Algoritmos Avançados:** Com a proliferação de algoritmos iterativos e DLR, a verificação da degradação da detectabilidade de lesões requer ferramentas que consigam isolar a resposta linear efetiva. Quando a não-linearidade é severa, o uso direto do NPWE clássico falha, exigindo a expansão para modelos linearizados via LIR (*Local Impulse Response*).
- **Otimização de Parâmetros de Aquisição:** Otimização de correntes de tubo ($mAs$), tensões ($kVp$), filtros de reconstrução (kernels) e intensidades de regularização iterativa, buscando maximizar o $d'$ para tarefas clínicas específicas (ex: detecção de lesões hepáticas hipodensas).

---

## 4. Conexões e Wikilinks

- [[Observadores de Modelo (Model Observers)|model-observers]]
- [[NPWE Model Observer|NPWE]]
- [[Task Based Image Quality|Task_Based_Image_Quality]]
- [[Noise Power Spectrum|Noise_Power_Spectrum_NPS]]
- [[Task Transfer Function|MTF]]
- [[Retroprojeção Filtrada (FBP)|FBP]]
- [[Reconstrução Iterativa|IR]]
- [[Deep Learning Image Reconstruction (DLR)|DLR]]
- [[Índice de Detectabilidade|d']]
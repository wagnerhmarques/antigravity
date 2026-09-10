---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, percepcao-visual, avaliacao-de-imagem, observadores-humanos]
data: 2026-08-25
---

# 2AFC_compara_desempenho_perceptual

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O método **2AFC** (*Two-Alternative Forced-Choice*, ou Escolha Forçada de Duas Alternativas) é um paradigma psicofísico fundamental aplicado na Física Médica e na avaliação de qualidade de imagem em Tomografia Computadorizada (TC). Ele é projetado para quantificar o desempenho perceptual de observadores (seja o sistema visual humano ou [[Observadores de Modelo (Model Observers)|observadores_computacionais_ideal]]) na detecção ou discriminação de sinais visuais sutis imersos em ruído estocástico e artefatos de reconstrução.

Em um teste 2AFC clássico, o observador é apresentado a duas imagens (ou dois volumes de TC) em cada ensaio (*trial*):
1. **Imagem Contendo o Sinal (Target):** Apresenta a estrutura anatômica ou patológica de interesse (ex.: um nódulo pulmonar simulado, uma microcalcificação ou um artefato de feixe) combinada com o ruído de fundo e a textura da imagem.
2. **Imagem de Referência (Background/Control):** Contém apenas o ruído de fundo e a textura, sem o sinal de interesse.

O termo "escolha forçada" decorre da restrição metodológica de que o observador deve obrigatoriamente indicar\, dentre as duas opções apresentadas espacial ou temporalmente, qual delas contém o sinal, mesmo que sua certeza seja mínima ou que o sinal esteja abaixo do limiar de percepção consciente. 

A principal vantagem metrológica do 2AFC em relação a métodos de resposta livre ou escalas rating (como ROC convencional) é a eliminação do viés de critério de decisão (*decision threshold bias*). Em testes com escalas Likert ou sim/não, observadores conservadores tendem a relatar menos positivos verdadeiros do que observadores liberais. Como o 2AFC impõe uma escolha binária direta baseada em uma comparação relativa, o viés do observador é efetivamente neutralizado, tornando a acurácia percentual obtida uma medida pura e robusta da sensibilidade perceptual e da detectabilidade física do sinal.

---

## 2. Formulação Matemática e Propriedades

Matematicamente, o desempenho no paradigma 2AFC é expresso pela probabilidade de acerto correto do observador\, denotada por $P_{2AFC}$. Para um observador ideal ou sub-ótimo operando sob a Teoria da Detecção de Sinais (SDT - *Signal Detection Theory*), assume-se que o observador calcula uma variável de decisão escalar $z$ para cada imagem apresentada.

Seja $z_s$ a variável de decisão associada à imagem contendo o sinal e $z_n$ a variável de decisão associada à imagem apenas com ruído. O observador seleciona a imagem correta se:

$$
z_s > z_n
$$

A probabilidade de acerto $P_{2AFC}$ é dada pela integral da função de densidade de probabilidade conjunta das variáveis de decisão. Assumindo que as distribuições de $z_s$ e $z_n$ são Gaussianas com médias $\mu_s$ e $\mu_n$, e desvios padrão $\sigma_s$ e $\sigma_n$, a probabilidade de escolha correta em um teste 2AFC é equivalente à área sob a curva ROC (*Receiver Operating Characteristic*) para uma tarefa de detecção com sinal conhecido exatamente (*Signal Known Exactly* - SKE):

$$
P_{2AFC} = \int_{-\infty}^{\infty} f_n(z) \left[ \int_{-\infty}^{z} f_s(z') dz' \right] dz
$$

Onde $f_n(z)$ e $f_s(z)$ representam as distribuições de probabilidade para o ruído e para o sinal mais ruído, respectivamente. 

Quando as variâncias das distribuições são iguais ($\sigma_s = \sigma_n = \sigma$), a relação entre a probabilidade de acerto $P_{2AFC}$ e o índice de detectabilidade tradicional d' (d-prime) é expressa analiticamente pela função erro complementar ($\text{erfc}$) ou pela distribuição normal padrão acumulada $\Phi$:

$$
d' = \frac{\mu_s - \mu_n}{\sigma} = \sqrt{2} \, \Phi^{-1}(P_{2AFC})
$$

Esta propriedade matemática é de suma importância, pois permite converter uma proporção simples de acertos experimentais obtida em ensaios psicofísicos de 2AFC diretamente em uma métrica de desempenho contínua e parametrizada ($d'$), facilitando a comparação rigorosa entre diferentes algoritmos de reconstrução tomográfica.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

No ecossistema moderno da Tomografia Computadorizada, o 2AFC desempenha um papel central na validação e otimização de tecnologias avançadas:

* **Avaliação de Reconstruções Iterativas (IR) e Aprendizado Profundo (DLR):** Algoritmos de Deep Learning for Reconstruction (DLR) frequentemente alteram a textura do ruído e introduzem borramentos direcionais não lineares. Métodos tradicionais baseados em métricas de erro de pixel (como RMSE ou PSPS) falham em correlacionar-se com a detectabilidade clínica. O 2AFC, acoplado a observadores humanos ou a [[Observadores de Modelo (Model Observers)|observadores_computacionais_ideal]], permite mensurar se a supressão de ruído por IA preserva ou degrada a detectabilidade de lesões de baixo contraste (ex.: metástases hepáticas ou AVCs precoces).
* **Otimização de Protocolos de Dose Baixa:** Permite determinar o limite inferior de produto dose-comprimento ($DLP$) ou corrente do tubo ($mA$) no qual a detectabilidade de estruturas anatômicas críticas atinge o limiar aceitável, auxiliando no cumprimento dos princípios ALARA.
* **Padronização de Ensaios Clínicos de Imagem:** O 2AFC serve como bancada de testes metrológica para aprovação regulatória de novos scanners de TC e filtros de reconstrução, fornecendo curvas de desempenho livres de subjetividade humana ligada a critérios de exaltação ou hesitação diagnóstica.

---

## 4. Conexões e Wikilinks

* [[Observadores de Modelo (Model Observers)|observadores_computacionais_ideal]]
* [[teoria_deteccao_sinais_tc]]
* [[Reconstrução Iterativa|reconstrucao_iterativa_ir]]
* [[Deep Learning Reconstruction (DLR)|deep_learning_reconstruction_dlr]]
* [[Qualidade Imagem TC|qualidade_imagem_tc]]
* [[ruido_textura_imagem_tc]]
* [[otimizacion_dosis_tomografia]]
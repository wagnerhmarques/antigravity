---
tipo: conceito
aliases: [fisica-medica]
tags: [fisica-medica, tomografia-computadorizada]
data: 2026-08-25
---

# fisica-medica

## 1. Definição Conceitual e Fundamentação Física
A Física Médica é a aplicação dos conceitos, métodos e teorias da física à medicina e à biologia humana, atuando primordialmente nas áreas de diagnóstico por imagem, radioterapia e medicina nuclear. No escopo da radiologia diagnóstica — e em particular na Tomografia Computadorizada (TC) —, a física médica fundamenta-se na interação da radiação ionizante (raios X) com a matéria biológica. O objetivo central é a otimização da relação entre a qualidade diagnóstica da imagem e a dose de radiação absorvida pelo paciente, garantindo a conformidade com os princípios de Justificação, Otimização e Limitação de Dose (ALARA - *As Low As Reasonably Achievable*).

Do ponto de vista físico, a formação da imagem em TC baseia-se na atenuação diferencial dos fótons de raios X ao atravessarem o volume anatômico, regida pela lei de atenuação de Beer-Lambert. A quantificação precisa dessa atenuação requer o rigor metrológico promovido pela física médica, que abrange desde a calibração de unidades Hounsfield (HU) até a avaliação de parâmetros complexos de desempenho de imagem, tais como a Função de Dispersão de Ponto (PSF), a Função de Transferência de Tarefa (TTF) e a Curva de Detectabilidade (d'-index).

## 2. Formulação Matemática e Propriedades
A atenuação de um feixe de raios X monoenergético ao percorrer um meio material de espessura $x$ é descrita pela equação exponencial clássica:

$$
I(x) = I_0 \exp\left( -\int_{0}^{x} \mu(l) \, dl \right)
$$

Onde:
- $I_0$ é a intensidade inicial do feixe de fótons.
- $I(x)$ é a intensidade do feixe após atenuado pela distância $x$.
- $\mu(l)$ é o coeficiente de atenuação linear espacialmente variante ($\text{cm}^{-1}$).

Para sistemas de Tomografia Computadorizada moderna, a reconstrução da imagem mapeia os coeficientes de atenuação linear para a escala normalizada de Unidades Hounsfield ($\text{HU}$):

$$
\text{HU} = 1000 \times \frac{\mu - \mu_{\text{agua}}}{\mu_{\text{agua}} - \mu_{\text{ar}}}
$$

Onde $\mu$, $\mu_{\text{agua}}$ e $\mu_{\text{ar}}$ representam, respectivamente, os coeficientes de atenuação linear do tecido analisado\, da água pura e do ar nas condições padrão de calibração do equipamento.

A propagação de incertezas na estimativa de ruído ($\sigma$) associada à contagem estatística de fótons em detectores de tomografia segue a estatística de Poisson, sendo modelada no domínio da imagem reconstruída por:

$$
\sigma^2 \propto \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \frac{1}{I_0} W(u,v) \, du \, dv
$$

Onde $W(u,v)$ representa o filtro de rampa e de apodização (kernel) aplicado no espaço de Fourier durante a retroprojeção filtrada (FBP).

## 3. Contexto no Acervo do Pesquisador & Aplicações
No acervo de pesquisas e notas do laboratório (USP/FAPESP), o termo [[Fisica Medica|fisica-medica]] emerge como a disciplina estruturante que unifica o ferramental metodológico e experimental da Tomografia Computadorizada. As menções no acervo destacam três eixos principais de aplicação e integração:

1. **Controle de Qualidade e Metrologia com Fantomas:** Conforme documentado em [[queries/O que são phantoms ?.md]], a física médica utiliza [[Phantoms Híbridos|phantoms]] para simular a atenuação radiológica, a densidade e as características geométricas dos tecidos biológicos humanos, servindo como instrumentos indispensáveis para a validação de protocolos clínicos e físicos.
2. **Integração com Inteligência Artificial e Inovação Responsável:** A nota [[queries/você tem a capacidade de obter informações por meio de fontes que não estão na pasta raw?.md]] contextualiza a física médica na fronteira com a [[Inteligência Artificial em Saúde|inteligencia-artificial-em-saude]] e a [[Inovação Responsável em Saúde (Responsible Research and Innovation - RRI)|inovacao-responsavel-em-saude]], abordando os limites de acesso a dados e a governança de algoritmos baseados em aprendizado profundo (DLR - *Deep Learning Reconstruction*).
3. **Avaliação Avançada de Desempenho de Imagem:** Conforme evidenciado em [[queries/quais são os termos mais frequentes na minha estruturaco aqui no obsidian?.md]], a física médica conecta-se diretamente a métricas quantitativas de ponta, como o [[Detectabilidade Index|detectabilidade-index]], a caracterização de detectores de contagem de fótons ([[Photon Counting Detector CT (PCD-CT)|photon-counting-detector-ct]]) e a avaliação de desempenho baseada em tarefas ([[Task Transfer Function|task-transfer-function]]), além da gestão de ruído ([[Noise Power Spectrum|noise-power-spectrum]]).

## 4. Conexões e Wikilinks
- [[Tomografia Computadorizada|tomografia-computadorizada]]
- [[Phantoms Híbridos|phantom]]
- [[Detectabilidade Index|detectabilidade-index]]
- [[Photon Counting Detector CT (PCD-CT)|photon-counting-detector-ct]]
- [[Task Transfer Function|task-transfer-function]]
- [[Inteligência Artificial em Saúde|inteligencia-artificial-em-saude]]
- [[Inovação Responsável em Saúde (Responsible Research and Innovation - RRI)|inovacao-responsavel-em-saude]]
---
tipo: conceito
aliases: [Samuel Brady]
tags: [fisica-medica, tomografia-computadorizada, controle-de-qualidade, aapm, metrologia]
data: 2026-08-25
---

# Samuel Brady

## 1. Definição Conceitual e Fundamentação Física
**Samuel Brady** é um pesquisador e físico médico proeminente, amplamente reconhecido por suas contribuições significativas à metrologia em radiologia diagnóstica, padronização de protocolos de imagem e avaliação de desempenho de sistemas de Tomografia Computadorizada (TC). No contexto da física médica moderna, o seu trabalho está intimamente ligado ao desenvolvimento, revisão e implementação de relatórios de força-tarefa (Task Groups) da *American Association of Physicists in Medicine (AAPM)*. 

Suas contribuições abordam diretamente a necessidade de harmonização nas métricas de qualidade de imagem, otimização da dose de radiação ionizante e caracterização avançada de desempenho de scanners de TC, abrangendo desde sistemas tradicionais de varredura helicoidal até tecnologias emergentes de reconstrução iterativa e baseada em inteligência artificial (Deep Learning Reconstruction - DLR).

## 2. Formulação Matemática e Propriedades
Embora seja um autor e colaborador institucional e não um epônimo de lei física direta, a atuação científica de Samuel Brady fundamenta-se em formulações matemáticas rigorosas aplicadas à avaliação da qualidade de imagem em TC. Isso inclui a quantificação da função de transferência de modulação (MTF), a análise de ruído por meio do espectro de potência de ruído (NPS) e a avaliação da detectabilidade de lesões com base no modelo de observador ideal e humano (Task-Transfer Function - TTF e Detective Quantum Efficiency - DQE).

A avaliação de desempenho quantitativo descrita nos compêndios normativos dos quais participa utiliza formalismos como a estimativa do ruído padrão $\sigma$ em uma região de interesse (ROI) homogênea\, definida por:

$$
\sigma = \sqrt{\frac{1}{N-1} \sum_{i=1}^{N} \left( x_i - \bar{x} \right)^2}
$$

Onde $\left\{ x_i \right\}$ representa os valores de número de Hounsfield (HU) ou atenuação pixel a pixel, $N$ é o número total de pixels na amostra, e $\bar{x}$ é a média aritmética dos valores na ROI. Da mesma forma, a caracterização espacial da resolução por meio da MTF a partir de uma borda ou fio delgado é expressa no domínio espacial e transformada para o domínio de frequência $f$ via transformada de Fourier:

$$
\text{MTF}(f) = \frac{\left| \mathcal{F} \left\{ \frac{d}{dx} \text{LSF}(x) \right\} \right|}{\left| \mathcal{F} \left\{ \frac{d}{dx} \text{LSF}(x) \right\} \right|_{f=0}}
$$

## 3. Contexto no Acervo do Pesquisador & Aplicações
No acervo da LLM Wiki de Física Médica & Tomografia Computadorizada (USP/FAPESP), o nome de Samuel Brady aparece estritamente vinculado a marcos normativos e literários fundamentais para a avaliação de desempenho de equipamentos de TC. Suas ocorrências estão mapeadas nos seguintes documentos centrais:

* No documento [[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg233-ct-performance]], Brady figura como um dos coautores especialistas responsáveis pelo estabelecimento de métricas avançadas de desempenho de imagem em tomografia computadorizada, alinhando-se aos esforços do AAPM Task Group 233 na transição para métricas baseadas em tarefas (*task-based image quality metrics*).
* No documento [[AAPM Journal Wiley Online Library|AAPM Journal  Wiley Online Library]], sua autoria reitera a participação direta na validação de metodologias rigorosas voltadas à padronização de testes de controle de qualidade, otimização de protocolos clínicos e avaliação de artefatos em imagens de TC.

A presença de Samuel Brady no acervo conecta-se diretamente com pesquisas sobre [[Ehsan Samei]], [[Donovan Bakalyar]], [[Kirsten L Boedeker|Kirsten L. Boedeker]], [[Shuai Leng]] e [[Kyle J. Myers]], formando a rede de autoridade científica que fundamenta os padrões atuais de metrologia em imagem médica no laboratório.

## 4. Conexões e Wikilinks
* [[Ehsan Samei]]
* [[Donovan Bakalyar]]
* [[Kirsten L Boedeker|Kirsten L. Boedeker]]
* [[Shuai Leng]]
* [[Kyle J. Myers]]
* [[Lucretiu M Popescu|Lucretiu M. Popescu]]
* [[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg233-ct-performance]]
* [[AAPM Journal Wiley Online Library|AAPM Journal  Wiley Online Library]]
---
tipo: sintese
titulo: "O Índice de Detectabilidade (d') em Tomografia Computadorizada: Fundamentação, Métricas e Formulação Matemática"
data_criacao: 2026-08-27
data_atualizacao: 2026-08-27
tags:
  - "detectabilidade"
  - "qualidade-de-imagem"
  - "observadores-de-modelo"
  - "dosimetria"
  - "física-médica"
perguntas_origem: ["queries/o que é índice de detectabilidade e como ele pode ser calculado ?.md"]
fontes_relacionadas:
  - "[[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg233-ct-performance]]"
  - "[[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg-233-summary]]"
  - "[[Greffier 2026 - Avaliação de DLR em TC com Phantoms|greffier-2026-dlr-ct-phantom]]"
  - "[[Projeto Doutorado Direto FAPESP Wagner 2026|projeto-dd-fapesp-wagner-2026]]"
  - "[[Solomon 2016 - Modelos de Observadores em TC|solomon-2016-observer-models]]"
  - "[[Model Observers e Detectabilidade em Raios X|model-observers-and-detectability-index-in-x-ray-imaging]]"
---

# O Índice de Detectabilidade ($d'$) em Tomografia Computadorizada: Fundamentação, Métricas e Formulação Matemática

## 1. Introdução e Contexto Conceitual
O **Índice de Detectabilidade ($d'$)** é uma figura de mérito quantitativa baseada em tarefas (*task-based image quality metric*)\, derivada diretamente da [[Teoria de Detecção de Sinais|teoria-de-deteccao-de-sinais]] (SDT). Na física médica moderna e na Tomografia Computadorizada (TC), o $d'$ substitui com vantagens metrológicas as métricas tradicionais baseadas puramente em pixels ou ruído isolado — como o desvio padrão global ou a Relação Contraste-Ruído convencional ([[Contrast To Noise Ratio|contrast-to-noise-ratio]]) —, as quais falham em prever a acurácia diagnóstica humana em sistemas não-lineares que empregam [[Reconstrução Iterativa|reconstrucao-iterativa]] ou [[Deep Learning Image Reconstruction (DLR)|deep-learning-image-reconstruction]].

Conforme estabelecido nos relatórios de referência da física médica ([[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg233-ct-performance]] e [[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg-233-summary]]), o índice $d'$ unifica três pilares fundamentais da formação da imagem diagnóstica:
1. A tarefa clínica específica a ser desempenhada (ex.: detecção de lesão hepática de baixo contraste ou microcalcificação de alto contraste);
2. A resolução espacial do sistema de imagem orientada ao contraste ([[Task Transfer Function|Task Transfer Function - TTF]]);
3. As propriedades estatísticas e texturais do ruído ([[Noise Power Spectrum|Noise Power Spectrum - NPS]]).

---

## 2. Formulação Matemática do Índice de Detectabilidade

O cálculo analítico de $d'$ no domínio de Fourier computa a separação estatística entre as distribuições de resposta para imagens contendo um sinal-alvo (*Signal Present*) e imagens de fundo puro (*Signal Absent*), simuladas por um observador matemático ou [[Observadores de Modelo (Model Observers)|observadores-de-modelo]]. 

Utilizando o observador modelo padrão *Non-Pre-Whitening with Eye Filter* (NPWE), a formulação matemática bidimensional expressa-se como:

$$
{d'}^2 = \frac{ \left[ \iint \left| W(u,v) \right|^2 \cdot \text{TTF}^2(u,v) \cdot E^2(u,v) \, du \, dv \right]^2 }{ \iint \left| W(u,v) \right|^2 \cdot \text{TTF}^2(u,v) \cdot \text{NPS}(u,v) \cdot E^2(u,v) \, du \, dv }
$$

Onde:
* $u, v$: Coordenadas no domínio de frequência espacial bidimensional;
* $W(u,v)$: Função tarefa, correspondente à Transformada de Fourier bidimensional da diferença espacial entre o sinal da lesão e o fundo;
* $\text{TTF}(u,v)$: [[Task Transfer Function|Função de Transferência Baseada em Tarefa]], que quantifica a resposta espacial do tomógrafo para o contraste específico da lesão;
* $\text{NPS}(u,v)$: [[Noise Power Spectrum|Espectro de Potência de Ruído]], caracterizando a magnitude e a textura do ruído nas frequências espaciais;
* $E(u,v)$: Filtro ocular que modela a sensibilidade espacial do sistema visual humano.

---

## 3. Metodologia de Cálculo e Abordagens Computacionais

O cálculo do $d'$ em ambientes clínicos e de pesquisa (como nos estudos de [[Greffier 2026 - Avaliação de DLR em TC com Phantoms|greffier-2026-dlr-ct-phantom]] e [[Projeto Doutorado Direto FAPESP Wagner 2026|projeto-dd-fapesp-wagner-2026]]) segue um fluxo metrológico rigoroso:

```
[Aquisição de Imagem em Phantom] ──► [Extração de ROIs (Fundo e Objeto)]
                                            │
                                            ▼
[Cálculo do NPS(u,v)] ◄────────────────────┴────────────────────► [Cálculo da TTF(u,v)]
        │                                                                   │
        └──────────────────────────┬────────────────────────────────────────┘
                                   ▼
                  [Aplicação do Modelo de Observador]
                  (NPW, NPWE, CHO ou [[Deep Learning Model Observer|deep-learning-model-observer]])
                                   │
                                   ▼
                     [Computação do Índice (d')]
```

### Principais Observadores de Modelo Utilizados:
1. **NPW (*Non-Pre-Whitening Observer*):** Modelo linear básico que não compensa o ruído interno, amplamente utilizado por sua estabilidade estatística.
2. **NPWE (*Non-Pre-Whitening with Eye Filter*):** Incorpora o filtro visual humano $E(u,v)$, elevando drasticamente a correlação com testes psicofísicos humanos ([[Solomon 2016 - Modelos de Observadores em TC|solomon-2016-observer-models]]).
3. **CHO (*Channelized Hotelling Observer*):** Emprega canais de frequência espacial (como filtros de Gabor) para simular o córtex visual humano, sendo robusto na avaliação de texturas complexas introduzidas por algoritmos de [[ADMIRE (Advanced Modeled Iterative Reconstruction)|admire-reconstruction]] ou [[Deep Learning Image Reconstruction (DLR)|deep-learning-image-reconstruction]].
4. **DLMO ([[Deep Learning Model Observer|deep-learning-model-observer]]):** Redes neurais profundas e Vision Transformers treinados para estimar diretamente a detectabilidade em cenários não-lineares complexos com alta fidelidade à percepção de especialistas humanos.

---

## 4. Relevância Clínica e Otimização de Protocolos
O emprego do índice de detectabilidade ($d'$) permite:
* **Validação de Ultrabaixa Dose:** Comprovar que protocolos de tomografia computadorizada operando em níveis restritos de radiação ($CTDI_{vol} < 2\text{ mGy}$) mantêm a detectabilidade diagnóstica intacta quando apoiados por algoritmos avançados de [[Deep Learning Image Reconstruction (DLR)|deep-learning-image-reconstruction]] ([[Greffier 2026 - Avaliação de DLR em TC com Phantoms|greffier-2026-dlr-ct-phantom]]).
* **Otimização Multiobjetivo:** Integrar o $d'$ como função de mérito no vetor de otimização de protocolos clínicos, balanceando a tríade de Dose, Tempo e Desempenho ([[Otimização Multiobjetivo em TC|otimizacao-multiobjetivo-tc]]).

## 🔗 Referências e Conexões na Wiki
- [[Índice de Detectabilidade|detectability-index]]
- [[Task Transfer Function|task-transfer-function]]
- [[Noise Power Spectrum|espectro-de-potencia-de-ruido-nps]]
- [[Observadores de Modelo (Model Observers)|observadores-de-modelo]]
- [[Deep Learning Model Observer|deep-learning-model-observer]]
- [[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg233-ct-performance]]
- [[Greffier 2026 - Avaliação de DLR em TC com Phantoms|greffier-2026-dlr-ct-phantom]]

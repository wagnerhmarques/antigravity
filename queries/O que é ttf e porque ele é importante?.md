> 📅 **Data:** 2026-08-27 | 🔗 **Conexões:** [[Task Transfer Function]], [[Modulation Transfer Function (MTF)]], [[Não-Linearidade em Reconstrução]], [[Índice de Detectabilidade]], [[AAPM TG-233 - Avaliação de Desempenho em TC]]

## 1. O que é a Task Transfer Function (TTF)?

A **Task Transfer Function (TTF)** é a métrica padrão-ouro em física médica e metrologia de Tomografia Computadorizada (TC) para quantificar a **resolução espacial** de sistemas de imagem modernos. Ela representa uma extensão e generalização avançada da tradicional Função de Transferência de Modulação (MTF).

Enquanto a MTF convencional pressupõe que o sistema de imagem seja linear e invariante no espaço (condição válida para a antiga Retroprojeção Filtrada - FBP), os tomógrafos atuais empregam algoritmos complexos e não-lineares, como a [[reconstrucao-iterativa]] (IR) e a [[Deep Learning Image Reconstruction (DLR)]] (DLR). Nesses sistemas avançados, a nitidez e a resolução espacial dependem fortemente do contraste do objeto\, do nível de dose de radiação ($CTDI_{vol}$) e da textura local do ruído.

A TTF resolve essa limitação ao medir a capacidade do sistema de transferir o contraste de um objeto de teste em função da frequência espacial, considerando o contraste específico da tarefa clínica avaliada ([[Task Transfer Function]]).

---

## 2. Formulação Matemática e Metodologia de Medição

A TTF é habitualmente extraída utilizando a técnica da borda circular (*circular edge technique*) em insertos circulares padronizados de fantomas de controle de qualidade (como o Mercury v4.0 ou o catphan):

$$
\text{TTF}(u,v) = \left| \mathcal{F} \left\{ \frac{d}{dr} \text{ESF}(r) \right\} \right|
$$

Onde:
- $\mathcal{F}\{\cdot\}$ denota a Transformada de Fourier;
- $\text{ESF}(r)$ é a Função de Dispersão de Borda (*Edge Spread Function*) medida radialmente na interface entre o inserto (ex.: Iodo ou *Solid Water*) e o fundo do fantoma.

### Principais Métricas Derivadas:
- **$f_{50}$:** Frequência espacial (em $\text{lp/cm}$ ou $\text{mm}^{-1}$) na qual a amplitude da TTF decai para $50\%$ de seu valor original. Serve como índice comparativo de nitidez.
- **$f_{10}$:** Frequência espacial limite na qual a resposta decai para $10\%$.

---

## 3. Por que a TTF é Importante na Física Médica Moderna?

A importância da TTF reside na sua capacidade de superar as falhas das métricas visuais tradicionais e lineares, atuando como pilar central na avaliação e otimização de protocolos radiológicos:

1. **Caracterização de Algoritmos Não-Lineares:** Sistemas de [[reconstrucao-iterativa]] frequentemente aplicam suavizações adaptativas que reduzem o ruído mas sacrificam a nitidez de pequenas estruturas. A TTF consegue mapear precisamente essa variação dependente de contraste.
2. **Componente Obrigatório do [[Índice de Detectabilidade]]:** A TTF não opera isoladamente. No ecossistema de avaliação baseada em tarefas ([[task-based-image-quality]]), o cálculo analítico do índice de detectabilidade ($d'$) — que prediz a acurácia diagnóstica humana — exige o produto combinado da resolução espacial (TTF) e das propriedades do ruído via [[noise-power-spectrum|espectro-de-potencia-de-ruido-nps]] (NPS):

$$
{d'}^2 = \frac{ \left[ \iint \left| W(u,v) \right|^2 \cdot \text{TTF}^2(u,v) \cdot E(u,v) \, du \, dv \right]^2 }{ \iint \left| W(u,v) \right|^2 \cdot \text{TTF}^2(u,v) \cdot \text{NPS}(u,v) \cdot E^2(u,v) \, du \, dv }
$$

3. **Diretrizes do AAPM (TG-233):** O relatório do AAPM Task Group 233 estabelece formalmente que a avaliação de desempenho de scanners de TC em ambiente clínico e de aceitação deve substituir a MTF analítica pela TTF, garantindo comparabilidade metrológica rigorosa entre diferentes fabricantes ([[aapm-tg233-ct-performance]], [[aapm-tg233-ct-performance|aapm-tg-233-summary]]). 
4. **Validação de Ultrabaixa Dose com DLR:** Estudos recentes demonstram que algoritmos de [[Deep Learning Image Reconstruction (DLR)]] mantêm ou elevam os valores de $f_{50}$ na TTF mesmo sob condições de radiação extremamente restritas ($CTDI_{vol} < 2\text{ mGy}$), validando a segurança diagnóstica de protocolos otimizados ([[greffier-2026-dlr-ct-phantom]]).

---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, radioprotecao, dosimetria, otimizacao, inteligencia-artificial]
data: 2026-08-25
---

# justificação

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **justificação** constitui o primeiro pilar fundamental do sistema de proteção radiológica, estabelecido pela Comissão Internacional de Proteção Radiológica (ICRP) e incorporado nas normativas internacionais e nacionais de segurança nuclear (como a norma NN 3.01 da Comissão Nacional de Energia Nuclear - CNEN no Brasil). Em Física Médica e, de forma muito particular, em [[Tomografia Computadorizada|tomografia-computadorizada]] (TC) — uma modalidade reconhecida por sua alta dose efetiva comparada a exames radiográficos convencionais —, a justificação refere-se ao processo decisório de avaliar e demonstrar que os benefícios diagnósticos ou terapêuticos globais de uma exposição à radiação ionizante para um indivíduo ou para a sociedade superam o detrimento radiológico potencial que tal exposição possa causar.

Do ponto de vista metrológico e bioético, a justificação opera em três níveis distintos de aplicação:
1. **Nível Geral:** A aprovação do uso de uma determinada prática envolvendo radiação (por exemplo, a utilização de varreduras de TC de corpo inteiro para triagem de indivíduos assintomáticos).
2. **Nível Específico (ou Procedural):** A validação de um procedimento radiológico específico para um grupo de pacientes com uma condição clínica bem delimitada.
3. **Nível Individual:** A aplicação da norma para o paciente específico que se apresenta ao serviço de saúde, ponderando se a indicação clínica daquele exame particular, naquele momento temporal e com os parâmetros técnicos propostos, é estritamente necessária para guiar o manejo clínico.

Na era da [[Inteligencia Artificial|inteligencia-artificial]] e dos exames de alta complexidade, a justificação deixou de ser apenas um ato médico subjetivo e passou a integrar algoritmos de suporte à decisão clínica (CDSS) e ferramentas de monitoramento de dose integradas ao fluxo de trabalho, garantindo que indicações redundantes ou inapropriadas sejam mitigadas antes da aquisição dos dados brutos ($p$-sinogramas).

---

## 2. Formulação Matemática e Propriedades (se aplicável)

Embora a justificação seja primordialmente um princípio ético, clínico e regulatório, a tomada de decisão quantitativa que a sustenta pode ser formalizada através de modelos de utilidade esperada e balanço de risco-benefício. 

Seja $\mathcal{B}$ o benefício clínico líquido associado à realização do exame de tomografia computadorizada, expresso em termos de ganho de expectativa de vida ajustada por qualidade (QALY) ou probabilidade de acerto diagnóstico precoce que altere positivamente a conduta terapêutica. Seja $\mathcal{R}$ o detrimento radiológico total, que é proporcional à dose efetiva coletiva ou individual $E$ (em Sieverts, Sv) multiplicada pelo coeficiente nominal de probabilidade de efeitos estocásticos (indução de câncer hereditário ou fatal) $\gamma_T$ para o tecido ou órgão irradiado $T$.

O critério fundamental de justificação pode ser expresso pela inequação de otimização de utilidade:

$$
\mathcal{B} > \mathcal{R} + \mathcal{C}
$$

Onde $\mathcal{C}$ representa os custos operacionais, econômicos e os riscos diretos inerentes ao procedimento (incluindo potenciais reações adversas a meios de contraste iodados nefrotóxicos). 

O detrimento total $R$ para um exame de TC helicoidal com perfil de dose ao longo do eixo $z$, representado pelo índice de dose em tomografia computadorizada ponderado ($CTDI_{w}$) e corrigido pelo produto dose-comprimento ($DLP$), é calculado considerando a sensibilidade específica dos órgãos:

$$
R = \sum_{T} w_T H_T = \sum_{T} w_T \left( \sum_{R} \int_{-\infty}^{\infty} D_T(z) \, dz \right)
$$

Onde:
- $w_T$ é o fator de peso tecidual definido pela ICRP para o órgão ou tecido $T$.
- $H_T$ é a dose equivalente no tecido $T$.
- $D_T(z)$ é a taxa de dose absorvida distribuída espacialmente ao longo do eixo longitudinal $z$ do tomógrafo.

A justificação exige que, para que o exame seja aceito, o ganho informacional da imagem reconstruída — mensurado, por exemplo, através da redução da incerteza no diagnóstico diferencial expressa pela entropia de Shannon $H(X)$ da distribuição de probabilidade das hipóteses clínicas — supere estritamente o risco estocástico incremental imposto pela dose $E$:

$$
\Delta H(X) = H(X_{\text{pré-exame}}) - H(X_{\text{pós-exame}}) > k \cdot \left( \sum_{T} w_T E_T \right)
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A justificação está intrinsecamente conectada aos demais princípios da radioproteção: a **otimização** (frequentemente resumida pelo acrônimo ALARA - *As Low As Reasonably Achievable*) e a **limitação de dose**. Enquanto a otimização atua *após* a decisão de realizar o exame (ajustando parâmetros como quilovoltagem $kVp$, corrente do tubo $mA$, tempo de rotação e algoritmos de reconstrução como [[Retroprojeção Filtrada (FBP)|fbp]], [[Reconstrução Iterativa|iterative-reconstruction]] ou [[Deep Learning Reconstruction (DLR)|dlr]]), a justificação atua *antes*, impedindo que exames desnecessários sejam realizados.

No ecossistema moderno da Tomografia Computadorizada, a justificação ganha relevância crítica em cenários específicos:
- **Exames de Múltiplas Fases (Protocolos Multidásicos):** Fases arterial, portal e tardia em TC abdominal devem ser rigorosamente justificadas individualmente, pois cada varredura adicional multiplica a carga dosimétrica imposta ao paciente.
- **Rastreio Populacional (*Screening*):** Programas como rastreamento de câncer de pulmão com TC de baixa dose (LDCT) exigem rigorosos critérios de justificação baseados em histórico de tabagismo e faixa etária, a fim de garantir que a razão benefício-risco permaneça positiva em larga escala.
- **Integração com Inteligência Artificial:** Sistemas baseados em aprendizado de máquina (*Machine Learning*) e Grandes Modelos de Linguagem ([[llm]]) são aplicados no ponto de atendimento (*point-of-care*) para analisar prontuários eletrônicos e diretrizes clínicas, avaliando instantaneamente a aderência da ordem médica aos critérios de adequação (*Appropriateness Criteria*), reduzindo a incidência de solicitações de TC injustificadas.

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|tomografia-computadorizada]]
- [[otimizacao-da-dose]]
- [[Retroprojeção Filtrada (FBP)|fbp]]
- [[Reconstrução Iterativa|iterative-reconstruction]]
- [[Deep Learning Reconstruction (DLR)|dlr]]
- [[Qualidade de Imagem em TC|qualidade-de-imagem]]
- [[Dosimetria em TC|dosimetria-em-tc]]
- [[Inteligencia Artificial|inteligencia-artificial]]
- [[llm]]
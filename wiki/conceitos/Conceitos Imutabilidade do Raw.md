---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, raw-data, metrologia, processamento-de-sinal, reconstrucao-de-imagem, ia]
data: 2026-08-25
---

# conceitos/Imutabilidade do Raw

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O conceito de **Imutabilidade do Raw** (ou integridade e imutabilidade dos dados brutos de aquisição) refere-se ao princípio metrológico, físico e computacional segundo o qual os dados primários de atenuação — medidos diretamente pelos detectores de raios X de um sistema de Tomografia Computadorizada (TC) antes de qualquer processamento matemático de reconstrução de imagem — devem ser preservados em seu estado original, bit-a-bit, sem sofrer modificações irreversíveis, perdas por compressão com perdas (*lossy compression*) ou sobrescritas arbitrárias.

Fisicamente, o conjunto de dados *raw* (frequentemente denominado *projections* ou *sinogram*) representa as contagens de fótons incidentes convertidas em correntes elétricas, integradas, digitalizadas por conversores analógico-digital (A/D) e convertidas em valores lineares de atenuação através da aplicação do logaritmo da intensidade relativa de fótons incidentes ($I_0$) e transmitidos ($I$). Metrologicamente, esses dados constituem a **fonte primária de verdade metrológica** do escaneamento do paciente. 

Qualquer alteração algorítmica aplicada diretamente sobre o domínio do *raw data* (como correções de endurecimento de feixe (*beam hardening*), calibração de ganho de canal, correção de *crosstalk* ou filtragens de ruído) deve ser registrada de forma reversível ou mantida em paralelo com o conjunto de dados brutos puro (não processado), garantindo a reprodutibilidade científica, a conformidade regulatória (como diretrizes da FDA e IEC) e a viabilidade de reprocessamento por algoritmos avançados de reconstrução, tais como a Reconstrução Iterativa (IR) e Reconstrução Baseada em Aprendizado Profundo (DLR).

## 2. Formulação Matemática e Propriedades (se aplicável)

Seja $I_{\beta, i}$ a intensidade de fótons medida pelo canal de detecção $i$ no ângulo de projeção $\beta$, e $I_0$ a intensidade incidente estimada na ausência de objeto. O dado bruto ideal e não corrigido no sinograma, $p_{\text{raw}}(\beta, i)$, é modelado pela lei de atenuação de Beer-Lambert discretizada:

$$
p_{\text{raw}}(\beta, i) = \ln \left( \frac{I_0}{I_{\beta, i}} \right)
$$

O princípio da imutabilidade dita que o conjunto de dados original $\mathcal{P}_{\text{raw}} = \left\{ p_{\text{raw}}(\beta, i) \mid \beta \in [0, 2\pi), i \in \{1, \dots, N_d\} \right\}$ deve ser armazenado sem truncamentos de ponto flutuante que comprometam a faixa dinâmica (*dynamic range*). 

Se uma operação de correção física $C$ ou filtragem $F$ for aplicada para gerar um sinograma modificado $p_{\text{mod}}(\beta, i)$, a relação deve ser estritamente mapeada de forma paramétrica, preservando a matriz original:

$$
p_{\text{mod}}(\beta, i) = F \left( C \left( p_{\text{raw}}(\beta, i); \mathbf{\theta}_c \right); \mathbf{\theta}_f \right)
$$

Onde $\mathbf{\theta}_c$ e $\mathbf{\theta}_f$ representam os vetores de parâmetros de calibração e filtragem, respectivamente. A imutabilidade garante que $\mathcal{P}_{\text{raw}}$ permaneça acessível para reavaliações onde novos modelos de correção $\mathbf{\theta}_c'$ superem os originais, evitando a propagação de artefatos irreversíveis induzidos por processamentos legados.

As propriedades fundamentais associadas a este conceito incluem:
1. **Linearidade Estatística:** Os dados mantêm a distribuição de Poisson original inerente à contagem de fótons antes de transformações lineares ou não-lineares complexas:
   
$$
\sigma^2 \left( p_{\text{raw}}(\beta, i) \right) \propto \frac{1}{I_{\beta, i}}
$$

2. **Reversibilidade Algorítmica:** Garantia de que a cadeia de processamento possa ser desfeita ou reexecutada a partir do marco zero.
3. **Não-degradação da Informação Mútua:** Preservação máxima da entropia de Shannon contida no sinal físico original detectado.

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Em Tomografia Computadorizada moderna, a imutabilidade do *raw data* deixou de ser apenas um requisito de arquivamento para se tornar um **pilar crítico de otimização clínica e computacional**:

* **Reconstrução Baseada em Aprendizado Profundo (DLR):** Redes neurais convolucionais e modelos generativos aplicados para redução de ruído e artefatos em TC frequentemente operam com máxima eficiência quando alimentados diretamente com dados no domínio do sinograma ou na interface híbrida sinograma-imagem. Sem a imutabilidade do *raw*, o treinamento e a inferência de modelos DLR sofrem de viés inducido por pré-processamentos proprietários do fabricante.
* **Protocolos de Baixa Dose e Redução de Ruído:** Técnicas avançadas de filtragem estatística iterativa (como *Penalized Likelihood Estimation* - Regularized algorithms) exigem o conhecimento exato da estatística de ruído de fótons (Poisson/Gaussiana mista) presente estritamente no *raw data* não corrompido por interpolações lineares da retroprojeção filtrada (FBP).
* **Radiômica e Biomarcadores Quantitativos:** Estudos de estabilidade radiômica demonstram que variações nos algoritmos de pós-processamento de imagem alteram texturas e características quantitativas. O acesso ao *raw* imutável permite padronizar a reconstrução *post-hoc*, mitigando artefatos de scanner e melhorando a repetibilidade de biomarcadores em oncologia.
* **Controle de Qualidade (QC) e Metrologia:** Permite aos físicos médicos auditar a calibração do scanner, avaliar a degradação de elementos individuais do detector e recalcular métricas de desempenho do sistema sem interferência de heurísticas de software aplicadas pelo console do equipamento.

## 4. Conexões e Wikilinks

* [[conceitos/Sinograma]]
* [[conceitos/Reconstrucao-Iterativa]]
* [[tecnologias/Deep-Learning-Reconstruction]]
* [[conceitos/Estatistica-de-Foton-e-Ruido]]
* [[conceitos/Correcao-de-Endurecimento-de-Feixe]]
* [[tecnologias/Filtro-de-Retroprojecao-FBP]]
* [[conceitos/Radiomica-e-Quantificacao]]
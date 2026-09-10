# SISTEMA DE ORIENTAÇÃO — DOUTORADO DIRETO EM FÍSICA MÉDICA

**Wagner Henrique Marques | IFUSP | Bolsa FAPESP** **Sessão:** 2026-08-17

---

## SISTEMA DE ORIENTAÇÃO ATIVO

**Papel confirmado.** Atuo como sistema de orientação acadêmica sênior em Física Médica. As regras do prompt estão registradas: não trato decisões metodológicas como fatos consumados; exijo hipóteses falsificáveis; não permito dois pipelines paralelos; cobro por marcos; interrompo escopo excessivo; e minha prioridade é maximizar a probabilidade de uma contribuição científica sólida, publicável e executável em 60 meses.

---

## DIAGNÓSTICO INICIAL

Li o rascunho de 14/08/2026, o projeto do Davi, o projeto AIR e o prompt mestre. O projeto está bem articulado estruturalmente. A pergunta central é precisa, os eixos têm precedência lógica e a Tabela 1 de critérios a priori é um ponto forte. Contudo, identifico três riscos que precisam ser tratados agora.

---

### Risco 1 — Dependência crítica do pipeline do Davi sem auditoria formal

> **[GARGALO CRÍTICO]**

O rascunho afirma que "o pipeline metrológico automatizado advindo de dissertação de mestrado do grupo (FAPESP 2025/26836-5)" já está em desenvolvimento. O projeto do Davi confirma que o NPWE é o observador principal e que HO/CHO são comparativos. Mas nenhum documento atual especifica: qual estado de maturidade do código existe hoje? Há testes automatizados? A saída é compatível com o que o Eixo 2 precisa consumir?

Você não pode iniciar o Eixo 1 sem antes auditar o que o Davi já produziu. Se você começar a reimplementar sem auditar, vai gerar dois pipelines paralelos que não conversam — exatamente o cenário que o prompt interdita. Antes de qualquer linha de código sua, preciso saber o estado real da infraestrutura do Davi.

---

### Risco 2 — Comprometimento metodológico prematuro com "mecanismo de atenção"

O resumo do rascunho já fixa a arquitetura: _"observador de aprendizado profundo, com mecanismo de atenção"_. O objetivo geral também repete isso. Isso é um problema.

**Mecanismo de atenção não é hipótese — é pressuposto.** Se a arquitetura já está no resumo, a comparação com alternativas mais simples (CNN pura, MLP sobre patches de NPS/TTF, ou até um modelo paramétrico não-linear) deixa de ser uma decisão científica e passa a ser uma justificativa post-hoc. O prompt é explícito: não recomende uma técnica simplesmente porque ela é moderna. Uma CNN treinada diretamente sobre pares de ROIs pode responder à pergunta científica com menor risco de overfitting, maior interpretabilidade e menor custo computacional — especialmente dado o tamanho esperado do dataset de 2AFC.

**Recomendação:** O rascunho deve reformular o objetivo e o resumo para descrever a classe do observador — _não-linear, baseado em aprendizado de máquina_ — e reservar a decisão de arquitetura para o protocolo experimental do Eixo 2, após análise do dataset disponível.

---

### Risco 3 — Operacionalização do estudo 2AFC como gargalo não controlado

O rascunho especifica corretamente que o 2AFC será o conjunto calibrador, com mínimo de 20 leitores por anatomia e análise MRMC. São três anatomias: **mínimo de 60 leitores especializados**. Isso é uma operação de grande porte logístico que depende de aprovação em CEP, recrutamento, treinamento, agendamento e honorários.

O problema não é científico — é temporal. Se o recrutamento do estudo 2AFC não começar no Ano 1, ele pode bloquear toda a calibração do Eixo 2 no Ano 2. E se o Eixo 2 atrasar, os Eixos 3 e 4 são arrastados junto.

**O estudo 2AFC precisa de protocolo CEP submetido antes do término do Semestre 2.** Isso não é discutível: é precedência de cronograma.

---

## DEFINIÇÃO DO EIXO 1

O Eixo 1 estará **concluído** quando as seguintes condições forem verificáveis simultaneamente:

**1. Pipeline integrado com o Davi:** O código do Davi foi auditado, suas convenções de entrada/saída foram documentadas, e o módulo do Wagner é compatível com esse pipeline (formatos, unidades, metadados).

**2. Automação validada no phantom de tórax:** NPS, TTF e d′ são calculados automaticamente para o phantom de tórax em pelo menos dois equipamentos e duas famílias de reconstrução (FBP + um método não-linear), com ICC ≥ 0,90 contra medidas de referência manual.

**3. Reprodutibilidade documentada:** Outro pesquisador consegue executar o pipeline a partir do repositório versionado, sem intervenção do Wagner.

**4. Entregável de software registrado:** Versão v1.0 do módulo de análise comprometida no repositório, com testes unitários básicos e documentação no Obsidian.

> O Eixo 1 não requer dados de abdome ou crânio — esses phantoms estão em finalização e não podem ser gargalo do Eixo 1. O tórax é suficiente e necessário.

---

## TRÊS PRIMEIRAS TAREFAS

---

### Tarefa 1 — Auditoria do pipeline do Davi

**Objetivo:** Determinar o estado real de maturidade do código do Davi: o que existe, o que funciona, o que está faltando, quais são os formatos de entrada e saída, e o que é necessário para integrá-lo com o trabalho do Wagner.

**Entregável:** Documento `[[Auditoria Pipeline Davi Yyyymm|Auditoria_Pipeline_Davi_YYYYMM]]` com inventário de módulos existentes, estado de cada módulo (funcional / parcial / ausente), convenções de formato\, dependências de bibliotecas, e lista de gaps que o Wagner precisa preencher.

**Notas Obsidian:**

- `[[Auditoria Pipeline Davi Yyyymm|Auditoria_Pipeline_Davi_YYYYMM]]`
- `[[Convencoes Pipeline Compartilhado|Convencoes_Pipeline_Compartilhado]]`
- `[[Dependencias Eixo1|Dependencias_Eixo1]]`

**Dependências:** Acesso ao repositório do Davi (ou reunião conjunta de alinhamento).

**Critério de conclusão:** É possível responder às oito perguntas do critério de integração (seção 8 do prompt mestre) para pelo menos o módulo de NPS do Davi.

**Prazo:** 22/08/2026 — **P0 Bloqueador**

---

### Tarefa 2 — Auditoria do dataset disponível

**Objetivo:** Inventariar exatamente quais dados de imagem estão disponíveis agora: quais tomógrafos, quais famílias de reconstrução, quais níveis de dose, em qual anatomia (phantom de tórax prioritário).

**Entregável:** Tabela `[[Dataset TC Disponivel Yyyymm|Dataset_TC_Disponivel_YYYYMM]]` com: scanner × reconstrução × dose × formato de arquivo × localização no servidor × status de conversão DICOM. Incluir o que está no InRad-HCFMUSP e o que está na Radboudumc.

**Notas Obsidian:**

- `[[Dataset TC Disponivel Yyyymm|Dataset_TC_Disponivel_YYYYMM]]`
- `[[Mapa Dados Tese|Mapa_Dados_Tese]]`

**Dependências:** Acesso aos dados do InRad e ao repositório do estágio BEPE/Radboudumc.

**Critério de conclusão:** É possível saber, sem ambiguidade, com quais dados o Eixo 1 pode começar imediatamente e quais aquisições ainda precisam ser realizadas.

**Prazo:** 29/08/2026 — **P1 Crítico**

---

### Tarefa 3 — Protocolo CEP para o estudo 2AFC

**Objetivo:** Iniciar a elaboração do protocolo de pesquisa para submissão ao Comitê de Ética em Pesquisa (CEP) referente ao estudo 2AFC com radiologistas.

**Entregável:** Rascunho inicial do protocolo CEP com: população-alvo (leitores por especialidade/anatomia), número amostral e análise de potência MRMC, método de amostragem de casos, plataforma de apresentação das imagens, critérios de inclusão/exclusão de leitores, e estratégia de randomização e mascaramento.

**Notas Obsidian:**

- `[[Protocolo CEP e Estudo 2AFC com Radiologistas|Protocolo_CEP_2AFC_Radiologistas]]`
- `[[Análise de Potência MRMC|Analise_Potencia_MRMC_Eixo2]]`
- `[[Cronograma Cep|Cronograma_CEP]]`

**Dependências:** Revisão da literatura sobre dimensionamento MRMC (Hillis et al., 2011 já referenciado no projeto); alinhamento com o orientador sobre hospital parceiro e plataforma de leitura.

**Critério de conclusão:** Rascunho revisável pelo orientador, com análise de potência formal e linha do tempo estimada para aprovação CEP → recrutamento → execução.

**Prazo:** 05/09/2026 — **P1 Crítico**

---

## PRIMEIRO MARCO VERIFICÁVEL

> **Marco 1 — Infraestrutura de baseline estabelecida**
> 
> **Data-alvo:** Mês 6 (Fevereiro/2027)
> 
> **Critério:** Pipeline automatizado de NPS/TTF/d′ integrado com o código do Davi, validado no phantom de tórax em ≥ 2 scanners e ≥ 2 famílias de reconstrução, com ICC ≥ 0,90, versionado em repositório\, documentado em Obsidian, e reprodutível por terceiro.
> 
> **Produto paralelo obrigatório:** Protocolo CEP do estudo 2AFC submetido até o Mês 6.

Esse marco é a condição necessária para qualquer trabalho subsequente. Não avance para o Eixo 2 antes de ele estar verificado.

---

## PLANO DE AÇÃO

|#|Tarefa|Entregável|Obsidian|Prazo|Prioridade|
|---|---|---|---|---|---|
|1|Auditar pipeline do Davi|`[[Auditoria Pipeline Davi Yyyymm|Auditoria_Pipeline_Davi_YYYYMM]]`|`[[Convencoes Pipeline Compartilhado|Convencoes_Pipeline_Compartilhado]]`, `[[Dependencias Eixo1|Dependencias_Eixo1]]`|22/08/2026|**P0 Bloqueador**|
|2|Inventariar dataset TC disponível|`[[Dataset TC Disponivel Yyyymm|Dataset_TC_Disponivel_YYYYMM]]`|`[[Mapa Dados Tese|Mapa_Dados_Tese]]`|29/08/2026|**P1 Crítico**|
|3|Rascunho protocolo CEP 2AFC|Protocolo revisável pelo orientador|`[[Protocolo CEP e Estudo 2AFC com Radiologistas|Protocolo_CEP_2AFC_Radiologistas]]`, `[[Cronograma Cep|Cronograma_CEP]]`|05/09/2026|**P1 Crítico**|

---

## NOTA EDITORIAL — RASCUNHO 14/08/2026

> O rascunho usa "mecanismo de atenção" e "Vision Transformer" no resumo e nos objetivos como se fossem decisões tomadas. Antes de submeter à FAPESP, isso precisa ser reescrito. A banca avaliadora — e futuramente a banca de defesa — vai cobrar justificativa experimental para essa escolha. Se a justificativa não existir ainda, não a antecipe no texto.
> 
> **Reformulação sugerida:** _"observador baseado em aprendizado de máquina, com arquitetura a ser definida após análise do dataset disponível e comparação sistemática com alternativas"_
> 
> Isso não enfraquece o projeto — protege você de um compromisso prematuro que pode se tornar dívida técnica.

---

_Gerado em 2026-08-17 | Sistema de Orientação Acadêmica Sênior — Física Médica IFUSP_
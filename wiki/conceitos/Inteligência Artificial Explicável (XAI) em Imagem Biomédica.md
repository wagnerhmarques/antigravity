---
tipo: conceito
titulo: "Inteligência Artificial Explicável (XAI) em Imagem Biomédica"
data_criacao: 2026-08-25
data_atualizacao: 2026-08-25
tags:
  - "xai"
  - "interpretabilidade"
  - "grad-cam"
  - "modelos-conceituais"
fontes_origem:
  - "[[Wong 2026 - IA no Imageamento Biomédico|wong-2026-ai-biomedical-imaging]]"
---

# Inteligência Artificial Explicável (XAI) em Imagem Biomédica

## Visão Geral
A adoção de sistemas de aprendizado profundo no diagnóstico por imagem requer superar a opacidade inerente às redes neurais profundas (o problema da "caixa-preta"). As técnicas de **Explainable AI (XAI)** buscam fornecer justificativas interpretáveis para as predições do modelo, promovendo a confiança clínica e a conformidade regulatória.

## Categorização das Técnicas Pós-Hoc

1. **Métodos Baseados em Perturbação:**
   - *Mecanismo:* Alteram regiões da imagem de entrada e avaliam o impacto relativo na saída.
   - *Exemplos:* Integrated Gradients (IG), LIME.

2. **Métodos Baseados em Gradiente:**
   - *Mecanismo:* Utilizam a propagação para trás (*backpropagation*) para mapear pixels de maior influência na classificação sem alterar os pesos.
   - *Exemplos:* Saliency Maps, Guided Backpropagation, Class Activation Mapping (CAM) e **Grad-CAM**.

3. **Métodos Baseados em Decomposição:**
   - *Mecanismo:* Decompõem a pontuação de predição distribuindo a relevância camada por camada.
   - *Exemplos:* Layer-wise Relevance Propagation (LRP), SGLRP, Concept Relevance Propagation (CRP).

4. **Métodos Baseados em Conceito:**
   - *Mecanismo:* Conectam conceitos legíveis por humanos às representações abstratas internas da rede.
   - *Exemplos:* Concept Activation Vectors (CAVs), Automatic Concept-based Explanation (ACE), ConceptSHAP.

## Limitações dos Mapas de Saliência e Novas Fronteiras
Conforme analisado em [[Wong 2026 - IA no Imageamento Biomédico|wong-2026-ai-biomedical-imaging]], os mapas de visualização tradicionais (como Grad-CAM) possuem limitações severas na prática clínica:
- **Instabilidade e Ruído:** Podem variar significativamente sob perturbações imperceptíveis na imagem ou ruídos de aquisição.
- **Desconexão com o Raciocínio Clínico:** Localizar uma anomalia visualmente não explica a etiologia ou o diagnóstico diferencial necessário para a conduta médica.

### Paradigmas Emergentes de XAI
- **Explicações Contrafactuais:** Ferramentas como **TraCE** e **GANterfactual** permitem ao clínico simular como alterações mínimas na imagem alterariam o diagnóstico da IA.
- **Redes Baseadas em Protótipos:** Arquiteturas como **XProtoNet** e **PCPPN** justificam suas predições exibindo regiões prototípicas de casos de treinamento semelhantes.
- **Concept Bottleneck Models (CBM):** Forçam a rede a prever primeiramente um conjunto de conceitos clínicos intermediários e auditáveis antes de emitir o diagnóstico final.

## Páginas Relacionadas
- [[Generalist Medical AI (GMAI) e Modelos de Fundação|generalist-medical-ai]]
- [[Modos de Integração de IA no Fluxo de Trabalho Clínico|modos-de-integracao-de-ia-clinica]]
- [[Wong 2026 - IA no Imageamento Biomédico|wong-2026-ai-biomedical-imaging]]
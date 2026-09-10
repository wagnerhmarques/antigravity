---tipo: tecnologia
titulo: "Reconstrução de Imagem Baseada em Deep Learning (DLR) em TC"
data_criacao: 2026-08-25
data_atualizacao: 2026-08-25
tags:
  - dlr
  - rede-neural
  - reconstrucao-de-imagem
fontes_origem:
  - "[[Greffier 2026 - Avaliação de DLR em TC com Phantoms|greffier-2026-dlr-ct-phantom]]"
aliases: [deep-learning-image-reconstruction\, deep-learning-reconstruction\, dlr, DLR, "deep learning reconstruction", "reconstrução por deep learning"]
---

# Reconstrução de Imagem Baseada em Deep Learning (DLR) em TC

A **Reconstrução de Imagem Baseada em Deep Learning** (*Deep-Learning Image Reconstruction* - DLR) representa a terceira grande geração de algoritmos de reconstrução em Tomografia Computadorizada (TC), sucedendo a Projeção Retrofiltrada (FBP) e a Reconstrução Iterativa (IR).

## Princípio de Funcionamento
Ao contrário dos algoritmos de IR convencionais que utilizam modelos físicos repetitivos e simplificados para estimar o ruído (o que frequentemente gera degradação na textura da imagem e aspecto plástico/borrado), o DLR utiliza redes neurais profundas (DNNs ou CNNs) treinadas com volumosos conjuntos de dados de alta qualidade (ex.: dados de baixa dose emparelhados com imagens de alta dose reconstruídas por Model-Based IR ou FBP de alta qualidade).

As redes aprendem a diferenciar o sinal anatômico verdadeiro do ruído quântico e dos artefatos de amostragem, realizando a supressão do ruído sem alterar a textura fundamental do tecido.

## Principais Implementações Comerciais no Mercado

| Fabricante | Nome Comercial do DLR | Arquitetura | Dataset de Treinamento |
| :--- | :--- | :--- | :--- |
| **Canon Medical** | **AiCE** (Advanced Intelligent Clear-IQ Engine) | Deep Neural Network (DNN) | Dados de pacientes / Model-based IR |
| **GE Healthcare** | **TrueFidelity™** | Deep Neural Network (DNN) | Phantoms e pacientes / FBP de alta dose |
| **Philips Healthcare** | **Precise Image** | Convolutional Neural Network (CNN) | Pacientes / Imagens similares a FBP |
| **United Imaging** | **DELTA** | Convolutional Neural Network (CNN) | Pacientes / FBP de alta dose |

## Vantagens com relação à Reconstrução Iterativa (IR)
1. **Preservação da Textura:** Mantém a frequência espacial média ($f_{av}$) do [[Noise Power Spectrum|NPS]] alta, garantindo o aspecto natural dos tecidos parenquimatosos.
2. **Manutenção da Resolução Espacial:** Elevação dos valores de $f_{50}$ na [[Task Based Image Quality|TTF]] mesmo em exames de ultrabaixa dose ($CTDI_{vol} < 2\text{ mGy}$).
3. **Ganhos Drásticos de Detectabilidade:** Aumento significativo no [[Índice de Detectabilidade|$d'$]] para lesões de baixo e alto contraste em protocolos abdominais, permitindo otimização de dose de acordo com o princípio ALARA/ALADA.
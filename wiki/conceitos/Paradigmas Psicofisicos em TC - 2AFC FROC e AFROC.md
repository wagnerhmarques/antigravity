# Paradigmas Psicofísicos em Tomografia Computadorizada: 2AFC, FROC e AFROC

> [!NOTE]
> Nota conceitual de fundamentação teórica para o Eixo 2 do Doutorado Direto (FMUSP/InRad - IFUSP), abordando os paradigmas de avaliação perceptual humana e sua aplicação na calibração de observadores de aprendizado profundo (DLMO).

---

## 1. O Problema da Calibração Perceptual

Na avaliação da qualidade de imagem baseada em tarefas (*task-based image quality*), observadores computacionais puros baseados em redes neurais operam sob condições determinísticas com precisão numérica ideal. Todavia, a decisão médica clínica é proferida por **observadores humanos** (médicos radiologistas), cuja percepção visual é modulada por:
- Flutuações ópticas retinianas e limitações de resolução angular.
- **Ruído interno estocástico** perceptual (incerteza intrínseca de limiar no córtex visual).
- Fadiga observacional e variabilidade inter/intra-observador.

A **calibração perceptual** consiste em ancorar o modelo de Deep Learning (DLMO) nas respostas reais de especialistas humanos, garantindo que o índice de detectabilidade estimado computacionalmente reproduza a capacidade diagnóstica humana sob ruídos complexos e não lineares de reconstruções por aprendizado profundo (DLR).

---

## 2. Comparativo dos Paradigmas Psicofísicos

| Dimensão | ROC Clássico | 2AFC (*Two-Alternative Forced Choice*) | FROC (*Free-response ROC*) | AFROC (*Alternative Free-response ROC*) |
| :--- | :--- | :--- | :--- | :--- |
| **Apresentação** | 1 imagem isolada por tentativa. | 2 imagens (ou ROIs) simultâneas lado a lado. | Imagem/fatia volumétrica inteira. | Imagem/fatia volumétrica inteira. |
| **Tarefa do Leitor** | Atribuir nota de certeza global de presença de lesão ($1$ a $5$). | Escolha forçada: indicar qual imagem contém o sinal ($H_1$). | Clicar livremente em todas as lesões suspeitas e pontuar confiança. | Clicar livremente em todas as lesões suspeitas e pontuar confiança. |
| **Informação de Localização** | Nenhuma (ignora onde a lesão está). | Intrínseca (Sinal Conhecido Exatamente - SKE). | Explícita (coordenadas $(x,y)$ com raio de aceitação). | Explícita (coordenadas $(x,y)$ com raio de aceitação). |
| **Eixo X da Curva** | Fração de Falsos Positivos ($FPF \in [0, 1]$). | Proporção de escolhas corretas ($P_C$). | Taxa média de falsos positivos por imagem ($\in [0, \infty)$). | Probabilidade do pior falso positivo exceder o limiar ($\in [0, 1]$). |
| **Métrica Síntese** | $\text{AUC} \in [0{,}5; 1{,}0]$ | $P_C = \text{AUC} \iff d'_v = \sqrt{2}\Phi^{-1}(P_C)$ | FOM de FROC (não limitada a $1$). | $\text{AUC}_{\text{AFROC}}$ ($A_1 \in [0{,}5; 1{,}0]$). |
| **Tratamento Estatístico MRMC** | Padrão (Dorfman-Berbaum-Metz / Obuchowski-Rockette). | Direto via variância binominal e MRMC contínuo. | Complexo (depende de jackknife livre). | Totalmente compatível com análise MRMC formal (Chakraborty, 2017). |

---

## 3. Detalhamento dos Métodos

### 3.1. Paradigma 2AFC (Two-Alternative Forced Choice)
O paradigma 2AFC apresenta ao radiologista pares de regiões de interesse ($64 \times 64$ pixels):
- Um patch contendo ruído/tecido de fundo sem lesão ($H_0$).
- Um patch contendo a lesão/alvo de interesse centrada ($H_1$).

#### Propriedade Fundamental: Livre de Critério (*Criterion-Free*)
No ROC clássico, leitores "conservadores" hesitam em dar notas altas, enquanto leitores "agressivos" marcam positivo com facilidade. No 2AFC, o leitor é obrigado a escolher uma das duas opções. Isso elimina matematicamente o viés do limiar decisório individual:
$$P_C = \text{AUC} = \Phi\left( \frac{d'_v}{\sqrt{2}} \right) \iff d'_v = \sqrt{2} \, \Phi^{-1}(P_C)$$
onde $\Phi$ é a função de distribuição acumulada da normal padrão.

* **Aplicação no Doutorado:** Utilizado para **calibrar o ruído interno estocástico ($\sigma_{\text{int}}$)** do DLMO com rapidez e alta eficiência amostral.

---

### 3.2. Paradigma FROC (Free-response ROC)
Projetado para mimetizar a busca visual livre na rotina médica, onde uma fatia ou volume pode abrigar $0, 1, 2 \dots K$ lesões:
1. O radiologista varre a imagem livremente e marca pontos suspeitos com o mouse, atribuindo um nível de confiança $C_i \in (0, 1]$.
2. Uma marcação é classificada como **Verdadeiro Positivo (TP)** se estiver dentro de uma distância radial de tolerância $R_{\text{tol}}$ em relação ao centroide da lesão real no phantom (ex.: $R_{\text{tol}} = 5\text{ mm}$):
   $$\| (x_{\text{marcado}}, y_{\text{marcado}}) - (x_{\text{real}}, y_{\text{real}}) \| \le R_{\text{tol}}$$
3. Marcações fora da vizinhança de qualquer lesão real são registradas como **Falsos Positivos (FP)**.

#### A Curva FROC:
- **Eixo das Ordenadas (Y):** Fração de Localização de Lesões:
  $$\text{LLF} = \frac{\text{Número de Lesões Reais Corretamente Marcadas}}{\text{Total de Lesões Reais no Estudo}}$$
- **Eixo das Abscissas (X):** Fração de Localização de Não-Lesões:
  $$\text{NLF} = \frac{\text{Número Total de Falsos Positivos}}{\text{Número Total de Imagens}}$$

> [!WARNING]
> Como um leitor pode marcar múltiplos falsos positivos em uma mesma imagem, $\text{NLF}$ pode assumir valores superiores a $1{,}0$ (ex.: $2{,}5$ falsos positivos por imagem). Portanto, **a curva FROC não possui uma integral normalizada de probabilidade**, inviabilizando o uso direto da Área sob a Curva tradicional ($\text{AUC}$).

---

### 3.3. Paradigma AFROC (Alternative Free-response ROC)
Desenvolvido por Chakraborty e Berbaum (2004) para solucionar o problema de normalização do FROC:
- Em fatias ou volumes que **não possuem lesões** (*casos normais*), o sistema descarta os múltiplos falsos positivos e retém apenas a marcação de **maior confiança** ($Z_{\max} = \max_j C_j$).
- Se a imagem normal não tiver nenhuma marcação, atribui-se $Z_{\max} = -\infty$.

#### Definição da Curva AFROC:
- **Eixo Y:** Fração de Lesões Detectadas ($\text{LLF} \in [0, 1]$).
- **Eixo X:** Probabilidade de que o falso positivo de maior confiança em uma imagem normal supere o limiar de corte decisório $\zeta$:
  $$\text{FPF}_{\text{AFROC}}(\zeta) = P(Z_{\max} > \zeta \mid \text{Caso Normal}) \in [0, 1]$$

#### Vantagens do AFROC:
1. O espaço da curva fica estritamente confinado ao quadrado unitário $[0, 1] \times [0, 1]$.
2. A área sob a curva AFROC ($\text{AUC}_{\text{AFROC}}$ ou estatística $A_1$) é uma medida formal da capacidade de ordenação diagnóstica do observador.
3. Permite a aplicação completa da **Teoria Multi-Leitor Multi-Caso (MRMC)** de Chakraborty (2017), decompondo as variâncias entre casos (imagens de phantom) e leitores (médicos experientes vs. residentes).

---

## 4. Integração Metodológica no Doutorado Direto

```
                [Aquisição nos 7 Tomógrafos do InRad]
                                  │
                                  ▼
      ┌───────────────────────────┴───────────────────────────┐
      │                                                       │
      ▼                                                       ▼
[ROIs Isoladas 64x64]                               [Fatias Volumétricas Reais]
      │                                                       │
      ▼                                                       ▼
[Paradigma 2AFC]                                     [Paradigma AFROC / FROC]
• Extração de d'_v humano                           • Busca livre com cliques
• Ajuste fino do ruído estocástico                  • Avaliação de falsos alarmes
  σ_int no DLMO                                     • Validação em escala anatômica
      │                                                       │
      └───────────────────────────┬───────────────────────────┘
                                  │
                                  ▼
                [Validação Estatística MRMC (p < 0,05)]
           Comprovação de superioridade do DLMO frente
                 aos modelos analíticos (NPWE / CHO)
```

---

## 🔗 Referências e Conexões
- [[Manual de Instrucoes e SOP do Doutorado]] — Procedimentos operacionais para coleta 2AFC e análise MRMC.
- [[Deep Learning Model Observers e Tempo Operacional na Otimizacao de TC]] — Formulação da injeção de ruído estocástico $\varepsilon_{\text{int}} \sim \mathcal{N}(0, \sigma_{\text{int}}^2)$.
- CHAKRABORTY, D. P. *Observer Performance Methods for Diagnostic Imaging*. CRC Press, 2017.
- CHAKRABORTY, D. P.; BERBAUM, K. S. *Observer operating characteristic analysis: the alternative free-response ROC*. Medical Physics, 2004.

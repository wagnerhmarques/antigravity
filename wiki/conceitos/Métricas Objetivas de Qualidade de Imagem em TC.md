---
tipo: conceito
titulo: "Métricas Objetivas e Automatizadas de Qualidade de Imagem em TC"
data_criacao: 2026-08-22
data_atualizacao: 2026-08-22
tags:
  - processamento-de-imagens
  - qualidade-objetiva
  - automacao
  - inteligencia-artificial
fontes_origem:
  - "[[Hoeijmakers 2026 - Qualidade de Imagem em TC Moderna|hoeijmakers-2026-image-quality-modern-ct]]"
---

# Métricas Objetivas e Automatizadas de Qualidade de Imagem em TC

## 1. Classificação Estrutural de Métricas *Reference-Free*
Na avaliação de exames clínicos de tomografia computadorizada, a ausência de uma imagem de referência perfeita ("ground truth") exige o emprego de métodos objetivos livres de referência (*reference-free*). Essas abordagens superam as restrições das medições manuais de regiões de interesse (ROIs), que sofrem de dependência de operador, viés de posicionamento e falta de representatividade volumétrica global.

```
                     Métricas Objetivas de Qualidade em TC
                                      │
     ┌──────────────────┬─────────────┴────────────┬──────────────────┐
     ▼                  ▼                          ▼                  ▼
  [Ruído]          [Contraste]           [Resolução Espacial]     [Compostas/IA]
  - NPS clínico    - Perfis lineares     - ESF ar-pele            - Detectabilidade (d')
  - GNL / GNI      - Histograma de HU    - TTF (FWHM)             - Estimabilidade
  - CNN noise map  - Segmentação auto    - Gradientes 2D borda    - Classificadores CNN
```

---

## 2. Principais Métricas por Domínio Físico

### A. Métricas de Ruído
1. **Global Noise Level (GNL) e Global Noise Index (GNI):**
   - Calculam o desvio-padrão local em janelas móveis (ex.: máscara $7 \times 7$) em regiões homogêneas de tecido mole ou ar ao redor do paciente.
   - O valor de ruído global é definido como a moda ou mediana do histograma de desvios-padrão locais, filtrando bordas e transições anatômicas.
2. **Noise Power Spectrum (NPS) Clínico:**
   - Determina a autocovariância do sinal em órgãos homogêneos (ex.: parênquima hepático) ou dados de contagem bruta sem necessidade de fantons ou múltiplas exposições repetidas.
3. **Mapas de Ruído por Redes Neurais Convolucionais (CNN):**
   - Redes treinadas em fantons com mapas de ruído absoluto geram predições pixel a pixel do desvio-padrão em dados clínicos.

### B. Métricas de Resolução Espacial
1. **Edge Spread Function (ESF) e Task Transfer Function (TTF) In Vivo:**
   - Avaliam a nitidez da transição na interface física entre o ar e a pele do paciente ou em margens vasculares.
   - A diferenciação da ESF produz a Line Spread Function (LSF), cuja transformada de Fourier fornece a TTF. A largura a meia altura ($FWHM$) da TTF atua como índice direto de resolução espacial.
2. **Edge Rise Slope (ERS):**
   - Razão entre a diferença de atenuação pico-a-vale em uma estrutura anatômica (ex.: veia porta ou parede aórtica) e a distância espacial correspondente (medida em $\Delta HU / \text{pixel}$).

### C. Métricas Compostas e Orientadas à Tarefa (*Task-Based*)
1. **Índice de Detectabilidade ($d'$):**
   - Combina a função de transferência da tarefa (TTF), o espectro de potência do ruído (NPS) e o modelo visual humano (observador não pré-esbranquiçado com canal visual - NPW/CHO) para prever a detectabilidade de lesões com contraste específico (ex.: nódulo de $-15\text{ HU}$ no fígado):
   

$$
d'^2 = \frac{\left[ \iint |W(u,v)|^2 \cdot |\text{TTF}(u,v)|^2 \cdot E(u,v) \, du \, dv \right]^2}{\iint |W(u,v)|^2 \cdot |\text{TTF}(u,v)|^2 \cdot \text{NPS}(u,v) \cdot E^2(u,v) \, du \, dv}
$$

---

## 3. Automação e Auditoria em Tempo Real
A substituição definitiva de ROIs manuais por pipelines automatizados com segmentação profunda (ex.: isolamento automático de fígado e músculo paraespinhal) permite a avaliação volumétrica instantânea no próprio console da TC. Isso possibilita:
- Detecção imediata de exames subótimos antes de o paciente sair da sala;
- Monitoramento contínuo da estabilidade dos tubos e detectores;
- Auditoria populacional e otimização automatizada de protocolos de dose e contraste ([[Otimização e Redução de Meio de Contraste em TC|otimizacao-meio-de-contraste-tc]]).

---

## Referências Cruzadas
- [[Hoeijmakers 2026 - Qualidade de Imagem em TC Moderna|hoeijmakers-2026-image-quality-modern-ct]]
- [[Photon Counting Detector CT (PCD-CT)|photon-counting-detector-ct]]
- [[Virtual Monoenergetic Imaging (VMI)|virtual-monoenergetic-imaging]]
- [[Avaliação Subjetiva por Comparação aos Pares (Pairwise Comparison)|avaliacao-pareada-qualidade-imagem]]